# Database model:- contains sqlalchemy mode

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(String, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    department = Column(String)
    role = Column(String, index=True)
    manager_id = Column(String)
    salary = Column(Float)
    leave_balance = Column(Integer)
    leaves_taken = Column(Integer)
    attendance_pct = Column(Float)
    performance_rating = Column(Integer)
    hashed_password = Column(String)