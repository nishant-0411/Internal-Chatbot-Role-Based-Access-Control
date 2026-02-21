from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.security import decode_token
from app.core.logger import logger

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    logger.info(f"Token received for authentication (partial): {token[:15]}...")

    data = decode_token(token)
    if data is None:
        logger.warning("Invalid or expired token attempt detected.")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    
    username = data.get("sub")
    role = data.get("role")

    logger.info(f"Token validated successfully | User: {username} | Role: {role}")
    
    return data

