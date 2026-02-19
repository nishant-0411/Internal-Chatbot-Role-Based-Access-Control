from fastapi import FastAPI, Body
from app.api import auth
from app.api import chat

app = FastAPI(title = "Internal Chatbot Api")

app.include_router(auth.router)
app.include_router(chat.router)

@app.get("/")
def root():
    return {"Internal Chatbot Backend Running"}

    
