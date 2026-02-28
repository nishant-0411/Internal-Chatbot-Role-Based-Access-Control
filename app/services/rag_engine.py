from app.services.index_builder import get_collection
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
        logger.warning("⚠️ No context found. Entering general mode.")

        prompt = f"""
        You are a friendly, intelligent AI assistant for the company.
        Your goal is to be helpful and polite.
        
        If the user is saying hello or making casual conversation, respond naturally and politely.
        If they are asking a specific question, answer it to the best of your general knowledge.

        Conversation History:
        {conversation_context}

        User Message:
        {query}

        Answer:
        """
    else:
        logger.info("✅ Context found. Using contextual internal mode.")

        prompt = f"""
        You are a friendly, intelligent AI assistant for the company.
        Your goal is to be helpful and polite.

        If the user is saying hello or making casual conversation, respond naturally and politely.
        
        If the user is asking a specific question, use the provided Company Context below to inform your answer. 
        If the relevant information is in the Company Context, prioritize that information.

        Conversation History:
        {conversation_context}

        Company Context:
        {context}

        User Message:
        {query}

        Answer:
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