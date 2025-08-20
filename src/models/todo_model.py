from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from src.infrastructure.databases.base import Base

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    done = Column(Boolean, default=False)
    assignee_id = Column(Integer, ForeignKey("users.id"), nullable=True)
