from sqlalchemy import Column, Integer, Text, ForeignKey
from src.infrastructure.databases.base import Base

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True)
    from_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    to_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    body = Column(Text, nullable=False)
