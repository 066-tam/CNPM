from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from src.infrastructure.databases.base import Base

class CourseRegister(Base):
    __tablename__ = "course_registers"
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    __table_args__ = (UniqueConstraint("course_id","user_id", name="uq_course_user"),)
