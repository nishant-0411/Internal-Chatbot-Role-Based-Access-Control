from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.models import Employee
from app.core.config import SessionLocal
from app.core.security import verify_password, create_access_tokens
from app.api.dependencies import get_current_user
from app.core.logger import logger
import time

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/jwt_validation")
def get_me(user=Depends(get_current_user)):
    logger.info(f"JWT validation successful for user: {user.get('sub')} | Role: {user.get('role')}")
    return {
        "message": "You are authenticated",
        "user": user
    }


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    start_time = time.time()
    logger.info(f"Login attempt for email: {form_data.username}")

    existing = db.query(Employee).filter(Employee.email == form_data.username).first()

    if not existing:
        logger.warning(f"Login failed - employee not found: {form_data.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="employee does not exist"
        )

    if not verify_password(form_data.password, existing.hashed_password):
        logger.warning(f"Login failed - incorrect password for: {form_data.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect password"
        )

    access_token = create_access_tokens(data={"sub": existing.email,  "role": existing.role})

    total_time = round(time.time() - start_time, 2)

    logger.info( f"Login successful | Employee: {existing.email} | Role: {existing.role} | Time: {total_time}s")
    logger.info("-" * 60)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }