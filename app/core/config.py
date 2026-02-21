# Database engine + SessionLocal
# Infrastructure Config only

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings
from app.core.logger import logger

class Settings(BaseSettings):
    SECRET_KEY: str 
    ACCESS_TOKENS_EXPIRE_MINUTES: int
    OLLAMA_MODEL: str 
    OLLAMA_URL: str 
    COLLECTION_NAME: str 
    ALGORITHM: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
logger.info("Application settings loaded successfully.")
logger.info(f"Ollama Model: {settings.OLLAMA_MODEL}")
logger.info(f"Collection Name: {settings.COLLECTION_NAME}")
logger.info(f"Token Expiry (minutes): {settings.ACCESS_TOKENS_EXPIRE_MINUTES}")

DATABASE_URL = settings.DATABASE_URL

logger.info("Initializing database engine...")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

logger.info("Database engine initialized successfully.")

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit = False,
    bind = engine
)

logger.info("SessionLocal configured successfully.")
logger.info("-" * 60)