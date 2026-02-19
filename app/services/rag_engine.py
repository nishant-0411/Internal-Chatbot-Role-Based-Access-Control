# Retrieval logic

from app.services.ingestion import collection, role_folder_mapping
import requests
from app.core.config import settings

def retrieve_context(query:str, user_role:str):

    user_role = user_role.casefold()

    if user_role == "c-level":
        results = collection.query(
            query_texts=[query],
            n_results=8
        )
    else:
        allowed_depts = [dept for dept, roles in role_folder_mapping.items() if user_role in [r.casefold() for r in roles]]

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


def generate_response(query: str, user_role: str):
    context = retrieve_context(query, user_role)

    if not context:
        return "No relevant documents found for your role"
    
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

    
    try:

        response = requests.post(
            settings.OLLAMA_URL,
            json = {
                "model": settings.OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        return response.json()["response"]
    
    except Exception as e:
        error_msg = str(e)

        if "429" in error_msg or "Quota exceeded" in error_msg:
            return "I'm currently experiencing high traffic. Please try again in a minute."
        
        return f"Error generating response: {error_msg}"

