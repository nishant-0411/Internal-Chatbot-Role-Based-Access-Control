# Database engine + SessionLocal
# Infrastructure Config only

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "nishantkhatkar_secretkey"
    ACCESS_TOKENS_EXPIRE_MINUTES: int = 600
    OLLAMA_MODEL: str = "phi3"
    OLLAMA_URL: str = "http://localhost:11434/api/generate"
    COLLECTION_NAME: str = "internal_docs"
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()

DATABASE_URL = "sqlite:///./users_database.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit = False,
    bind = engine
)
