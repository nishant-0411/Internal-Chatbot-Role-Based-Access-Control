from fastapi import FastAPI, Body
from app.api import auth

app = FastAPI(title = "Internal Chatbot Api")

app.include_router(auth.router)

@app.get("/")
def root():
    return {"Internal Chatbot Backend Running"}

    
