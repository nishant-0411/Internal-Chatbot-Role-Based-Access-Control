from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.models import Employee
from app.core.config import SessionLocal
from app.core.security import verify_password, create_access_tokens, hash_password
from pydantic import BaseModel
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

class RegisterRequest(BaseModel):
    employee_id: str
    full_name: str
    email: str
    department: str
    role: str
    manager_id: str
    password: str

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user_data: RegisterRequest, db: Session = Depends(get_db)):
    logger.info(f"Registration attempt for email: {user_data.email}")

    existing_user = db.query(Employee).filter(
        (Employee.email == user_data.email) | (Employee.employee_id == user_data.employee_id)
    ).first()
    
    if existing_user:
        logger.warning(f"Registration failed - employee already exists: {user_data.email} or {user_data.employee_id}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Employee with this email or ID already exists"
        )
    
    hashed_pwd = hash_password(user_data.password)
    
    new_employee = Employee(
        employee_id=user_data.employee_id,
        full_name=user_data.full_name,
        email=user_data.email,
        department=user_data.department,
        role=user_data.role,
        manager_id=user_data.manager_id,
        hashed_password=hashed_pwd,
        salary=0.0,
        leave_balance=0,
        leaves_taken=0,
        attendance_pct=100.0,
        performance_rating=0
    )
    
    try:
        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)
        logger.info(f"Registration successful for employee: {new_employee.email}")
        return {"message": "Registration successful"}
    except Exception as e:
        logger.error(f"Error during registration: {str(e)}")
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Registration failed due to internal server error"
        )