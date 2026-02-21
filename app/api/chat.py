# chat request and answer generation w.h.o rag_engine
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.api.dependencies import get_current_user
from app.services.rag_engine import generate_response
from app.core.logger import logger
import time

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/chat")
def chat(requests: ChatRequest, current_user: dict = Depends(get_current_user)):
    start_time = time.time()

    username = current_user.get("sub")
    user_role= current_user["role"]

    logger.info(f"/chat endpoint hit | User: {username} | Role: {user_role}")
    logger.info(f"User Query: {requests.query}")

    try:
        answer = generate_response(
            query=requests.query,
            user_role=user_role
        )

        total_time = round(time.time() - start_time, 2)

        logger.info(f"Chat response generated successfully | Time: {total_time}s")
        logger.info("-" * 60)

        return {
            "response": answer
        }

    except Exception as e:
        logger.error(f"Chat endpoint error | User: {username} | Error: {str(e)}")
        raise e