from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api import auth
from app.api import chat
from app.core.logger import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Internal Chatbot API is starting up...")
    logger.info("Routers registered: auth, chat")
    logger.info("-" * 60)

    yield
    logger.info("🛑 Internal Chatbot API is shutting down...")
    logger.info("-" * 60)

app = FastAPI(title = "Internal Chatbot Api",lifespan=lifespan)

app.include_router(auth.router)
app.include_router(chat.router)

@app.get("/")
def root():
    logger.info("Root endpoint accessed.")
    return {"Internal Chatbot Backend Running"}

