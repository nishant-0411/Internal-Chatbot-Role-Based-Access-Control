# login endpoint and authentication
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.models import User
from sqlalchemy.orm import Session
from app.core.config import SessionLocal
from app.core.security import verify_password, create_access_tokens
from app.api.dependencies import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/jwt_validation")
def get_me(user = Depends(get_current_user)):
    return {
        "message": "You are authenticated",
        "user": user
    }

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == form_data.username).first()
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "user does not exist"
        )
    
    if not verify_password(form_data.password, existing.hashed_password):
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "incorrect password"
        )
    
    access_token = create_access_tokens(
        data={
            "sub": existing.username,
            "role": existing.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }