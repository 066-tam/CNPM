from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.infrastructure.databases.base import Base

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True)
    subject = Column(String(255), nullable=False)
    when = Column(DateTime, nullable=False)
    mentor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    intern_id = Column(Integer, ForeignKey("users.id"), nullable=False)