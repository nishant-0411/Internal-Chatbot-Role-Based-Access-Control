# Database model:- contains sqlalchemy mode

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base # helps to write a table as a python class

Base = declarative_base()

class User(Base):
    __tablename__= "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)

