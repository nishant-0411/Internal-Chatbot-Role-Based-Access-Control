# Retrieval logic

from app.services.ingestion import collection, role_folder_mapping
import requests
from app.core.config import settings
from app.core.logger import logger
import time

def retrieve_context(query:str, user_role:str):

    user_role = user_role.casefold()

    if user_role == "c-level":
        results = collection.query(
            query_texts=[query],
            n_results=8
        )
    else:
        allowed_depts = [dept for dept, roles in role_folder_mapping.items() \
                        if user_role in [r.casefold() for r in roles]]

        if not allowed_depts:
             allowed_depts = []

        results = collection.query(
            query_texts=[query],
            n_results=8,
            where = {"department": {"$in" : allowed_depts}}
        )
    
    documents_nested  = results.get("documents",[])

    if not documents_nested: return "" 
    documents = documents_nested[0]
    if documents and isinstance(documents[0], list):
        documents = documents[0]

    return "\n\n".join(documents)


def estimate_tokens(text: str):
    return len(text)


def generate_response(query: str, user_role: str):
    start_time= time.time()
    logger.info(f"Incoming query: {query}")
    logger.info(f"User role: {user_role}")

    context = retrieve_context(query, user_role)

    if context:
        logger.info(f"Context Found | Length: {len(context)} characters")
    else:
        logger.warning("No internal context found. Using fallback mode.")

    if not context:
        prompt = f"""
        You are an AI assistant.

        The user asked:
        {query}

        There is no relevant information available in the company knowledge base.

        Inform the user politely that no company data was found.
        Then provide a helpful answer based on general knowledge.

        Answer:
        """
    else:
        prompt = f"""
        You are an internal company knowledge assistant.

        Answer ONLY using the provided context.
        Be concise and professional.
        Do NOT add external knowledge.
        If the answer is not clearly found, say:
        "I don't have enough information in the company knowledge base."

        Context:
        {context}

        Question:
        {query}

        Answer:
        """

    input_tokens = estimate_tokens(prompt)
    logger.info(f"Estimated Input Tokens: {input_tokens}")

    try:
        response = requests.post(
            settings.OLLAMA_URL,
            json={
                "model": settings.OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        answer = response.json()["response"]

        output_tokens = estimate_tokens(answer)
        total_time = round(time.time() - start_time, 2)

        logger.info(f"Estimated Output Tokens: {output_tokens}")
        logger.info(f"Response Time: {total_time} seconds")
        logger.info("Response generated successfully.")
        logger.info("-" * 60)

        return answer

    except Exception as e:
        error_msg = str(e)

        logger.error(f"Error generating response: {error_msg}")

        if "429" in error_msg or "Quota exceeded" in error_msg:
            return "I'm currently experiencing high traffic. Please try again in a minute."

        return f"Error generating response: {error_msg}"