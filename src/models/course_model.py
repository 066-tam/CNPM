from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from src.infrastructure.databases.base import Base

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    program_id = Column(Integer, ForeignKey("programs.id"), nullable=True)

    program = relationship("Program")
