from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.api import auth
from app.api import chat
from app.core.logger import logger
from app.services.index_builder import build_index
from app.services.retrieval import initialize_bm25

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Internal Chatbot API is starting up...")
    logger.info("Routers registered: auth, chat")
    
    # Initialize in-memory BM25 index
    try:
        build_index()
        initialize_bm25()
    except Exception as e:
        logger.error(f"Error initializing indexes: {e}")

    logger.info("-" * 60)

    yield
    logger.info("🛑 Internal Chatbot API is shutting down...")
    logger.info("-" * 60)

app = FastAPI(title = "Internal Chatbot Api",lifespan=lifespan)

# Add CORS Middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production, but "*" is fine for local dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(chat.router)

@app.get("/")
def root():
    logger.info("Root endpoint accessed.")
    return {"Internal Chatbot Backend Running"}


