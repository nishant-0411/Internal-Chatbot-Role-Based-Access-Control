# chat request and answer generation w.h.o rag_engine
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.api.dependencies import get_current_user
from app.services.rag_engine import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/chat")
def chat(requests: ChatRequest, current_user: dict = Depends(get_current_user)):
    user_role= current_user["role"]
    answer = generate_response(
        query=requests.query,
        user_role=user_role
    )

    return {
        "response": answer
    }