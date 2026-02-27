# Security utilities :- Password hashing, jwt creation, jwt verification
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from app.core.config import settings
from app.core.logger import logger

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def hash_password(password: str) -> str:
    logger.info("Password hashing initiated.")
    return pwd_context.hash(password)

def verify_password(normal_password: str, hashed_password: str) -> bool:
    result = pwd_context.verify(normal_password, hashed_password)
    if result:
        logger.info("Password verification successful.")
    else:
        logger.warning("Password verification failed.")
    return result

def create_access_tokens(data: dict) -> str:
    logger.info(f"Creating access token for user: {data.get('sub')} | Role: {data.get('role')}")

    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKENS_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    logger.info("Access token created successfully.")
    return token

def decode_token(token: str):
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        logger.info(
            f"Token decoded successfully | User: {data.get('sub')} | Role: {data.get('role')}"
        )
        return data
    except JWTError as e:
        logger.warning(f"JWT decoding failed: {str(e)}")
        return None
    
