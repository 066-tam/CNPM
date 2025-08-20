from sqlalchemy import Column, Integer, String, Text
from src.infrastructure.databases.base import Base

class Program(Base):
    __tablename__ = "programs"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
