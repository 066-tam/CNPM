# Placeholder for external consultant entity used by HR/Coordinators if needed.
from sqlalchemy import Column, Integer, String
from src.infrastructure.databases.base import Base

class Consultant(Base):
    __tablename__ = "consultants"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
