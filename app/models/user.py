from sqlalchemy import Column, Integer, String, Enum
from app.db.base import Base
from enum import Enum as PyEnum

class Role(str, PyEnum):
    admin = "Admin"
    hr = "HR"
    coordinator = "Coordinator"
    mentor = "Mentor"
    intern = "Intern"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(Enum(Role), nullable=False)
