from app.services.retrieval import retrieve
from app.services.streaming import stream_ollama
from app.core.logger import logger

def build_prompt(query, contexts, history=None):

    conversation_context = ""
    if history:
        for msg in history:
            conversation_context += f"{msg['role']}: {msg['content']}\n"

    if not contexts:
        logger.warning("No internal context found. Using general mode.")

        return f"""
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

    context_text = ""

    for idx, ctx in enumerate(contexts, 1):
        context_text += f"\n[Document {idx} | Score: {ctx['score']}]\n"
        context_text += ctx["content"] + "\n"

    return f"""
    You are a friendly, intelligent AI assistant for the company.
    Your goal is to be helpful and polite.

    If the user is saying hello or making casual conversation, respond naturally and politely.
    
    If the user is asking a specific question, use the provided Company Context below to inform your answer. 
    If the relevant information is in the Company Context, prioritize that information.

    Conversation History:
    {conversation_context}

    Company Context:
    {context_text}

    User Message:
    {query}

    Answer:
    """

def stream_response(query: str, user_role: str, conversation_history=None):
    logger.info(f"User Role: {user_role}")
    logger.info(f"User Query: {query}")

    contexts = retrieve(query, user_role)
    prompt = build_prompt(query, contexts, conversation_history)

    return stream_ollama(prompt)