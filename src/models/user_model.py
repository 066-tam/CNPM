from sqlalchemy import Column, Integer, String, Enum
from src.infrastructure.databases.base import Base
from src.domain.models.constants import Role

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    role = Column(Enum(Role), nullable=False)
