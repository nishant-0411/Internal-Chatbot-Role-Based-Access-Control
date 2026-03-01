from fastapi import APIRouter, Depends
from app.api.dependencies import get_current_user
from app.core.cache import add_message, get_messages, redis_client
from app.core.logger import logger
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from app.services.rag_orchestrator import stream_response
import time

router = APIRouter()

class ChatRequest(BaseModel):
    query: str
    conversation_id: str

@router.post("/chat")
def chat(requests: ChatRequest, current_user: dict = Depends(get_current_user)):

    start_time = time.time()

    username = current_user.get("sub")
    user_role = current_user["role"]
    conversation_id = requests.conversation_id

    logger.info(f"/chat | User: {username} | Role: {user_role} | Conv: {conversation_id}")
    logger.info(f"User Query: {requests.query}")

    history = get_messages(username=username, conversation_id=conversation_id)

    def response_generator():
        full_answer = ""

        try:
            logger.info("Streaming response started.")

            for chunk in stream_response(
                query=requests.query,
                user_role=user_role,
                conversation_history=history
            ):
                full_answer += chunk
                yield chunk

            add_message(username, conversation_id, "user", requests.query)
            add_message(username, conversation_id, "assistant", full_answer)

            total_time = round(time.time() - start_time, 2)

            logger.info("Streaming completed successfully.")
            logger.info(f"Response Length: {len(full_answer)} characters")
            logger.info(f"Total Time: {total_time}s")
            logger.info("-" * 60)

        except Exception as e:
            logger.error(f"Streaming error | User: {username} | Error: {str(e)}")
            raise e

    return StreamingResponse(response_generator(), media_type="text/plain")