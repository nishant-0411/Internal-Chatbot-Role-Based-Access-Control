from app.services.ingestion import get_collection
from app.core.config import settings
from app.core.logger import logger
from typing import List, Optional
import time
import json
import requests

def retrieve_context(query: str, user_role: str):
    collection = get_collection()
    user_role = user_role.casefold()
    print("Searching for role:", user_role)
    
    # Workaround for ChromaDB $contains issue with string metadata
    res_all = collection.get(include=["metadatas"])
    all_metadatas = res_all.get("metadatas", [])
    roles = set(m.get("role_access", "") for m in all_metadatas if m and "role_access" in m)
    matched_roles = [r for r in roles if f"|{user_role}|" in r]

    if not matched_roles:
        logger.warning(f"No matched documents for user role: {user_role}")
        return "", []

    results = collection.query(
        query_texts=[query],
        n_results=8,
        where={"role_access": {"$in": matched_roles}},
        include=["documents", "distances", "metadatas"]
    )
    print("Query Results Count:", len(results.get("documents", [[]])[0]))
    documents_nested = results.get("documents", [])
    distances_nested = results.get("distances", [])
    metadata_nested = results.get("metadatas", [])

    if not documents_nested or not distances_nested:
        logger.warning("No documents returned from vector DB.")
        return "", []

    documents = documents_nested[0]
    distances = distances_nested[0]
    metadatas = metadata_nested[0]

    if not documents:
        return "", []

    best_distance = distances[0]
    logger.info(f"Best distance: {best_distance}")

    if best_distance > 1.3:
        logger.warning("Best match too weak. Triggering fallback.")
        return "", []

    top_docs = documents[:8]
    top_meta = metadatas[:8]

    logger.info("Using top 8 retrieved documents.")
    return "\n\n".join(top_docs), top_meta

def estimate_tokens(text: str):
    return len(text)

def generate_response(query: str, user_role: str, conversation_history: Optional[List[dict]] = None):
    start_time = time.time()

    logger.info(f"Incoming query: {query}")
    logger.info(f"User role: {user_role}")

    context, sources = retrieve_context(query, user_role)

    conversation_context = ""

    if conversation_history:
        for msg in conversation_history:
            conversation_context += f"{msg['role']}: {msg['content']}\n"

    if not context:
        prompt = f"""
        You are an AI assistant.

        Conversation History:
        {conversation_context}

        User Question:
        {query}

        There is no relevant information available in the company knowledge base.

        Inform the user politely that no company data was found.
        Then provide a helpful answer based on general knowledge.

        Answer:
        """
    else:
        prompt = f"""
        You are a company internal knowledge assistant.

        You MUST answer using ONLY the information provided in the Company Context below.

        STRICT RULES:
        - Do NOT provide generic industry advice.
        - Do NOT make assumptions.
        - If answer not found say exactly:
        "I don't have enough information in the company knowledge base."

        Conversation History:
        {conversation_context}

        Company Context:
        {context}

        User Question:
        {query}

        Answer strictly based on Company Context:
        """

    input_tokens = estimate_tokens(prompt)
    logger.info(f"Estimated Input Tokens: {input_tokens}")

    try:
        response = requests.post(
            settings.OLLAMA_URL,
            json={
                "model": settings.OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_ctx": 8192
                }
            },
            timeout=60
        )

        answer = response.json()["response"]

        output_tokens = estimate_tokens(answer)
        total_time = round(time.time() - start_time, 2)

        logger.info(f"Estimated Output Tokens: {output_tokens}")
        logger.info(f"Response Time: {total_time}s")
        logger.info("-" * 60)

        if sources:
            citation_text = "\n\nSources:\n"
            for meta in sources:
                citation_text += f"- {meta.get('source_file')} ({meta.get('department')})\n"
            answer += citation_text

        return answer

    except Exception as e:
        logger.error(f"Error generating response: {str(e)}")
        return "Error generating response. Please try again."


def stream_response(query: str, user_role: str, conversation_history=None):

    logger.info("Streaming mode retrieval started")
    logger.info(f"User Role: {user_role}")
    logger.info(f"User Query: {query}")

    context, sources = retrieve_context(query, user_role)

    logger.info(f"Retrieved context length: {len(context)}")

    conversation_context = ""
    if conversation_history:
        for msg in conversation_history:
            conversation_context += f"{msg['role']}: {msg['content']}\n"

    if not context:
        logger.warning("⚠️ No context found. Entering fallback mode.")

        prompt = f"""
        You are an AI assistant.

        Conversation History:
        {conversation_context}

        User Question:
        {query}

        There is no relevant information available in the company knowledge base.

        Inform the user politely that no company data was found.
        Then provide a helpful answer based on general knowledge.

        Answer:
        """
    else:
        logger.info("✅ Context found. Using strict internal mode.")

        prompt = f"""
        You are a company internal knowledge assistant.

        You MUST answer using ONLY the information provided in the Company Context below.

        STRICT RULES:
        - Do NOT provide generic industry advice.
        - Do NOT make assumptions.
        - Do NOT add outside knowledge.
        - If the answer is not found in the context, say exactly:
        "I don't have enough information in the company knowledge base."

        Conversation History:
        {conversation_context}

        Company Context:
        {context}

        User Question:
        {query}

        Answer strictly based only on the Company Context:
        """

    try:
        response = requests.post(
            settings.OLLAMA_URL,
            json={
                "model": settings.OLLAMA_MODEL,
                "prompt": prompt,
                "stream": True,
                "options": {
                    "num_ctx": 8192
                }
            },
            stream=True
        )

        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                yield data.get("response", "")

    except Exception as e:
        logger.error(f"Streaming error: {str(e)}")
        yield "Error generating response."