from sqlalchemy import Column, Integer, String, Text, ForeignKey, UniqueConstraint
from app.db.base import Base

class TrainingProgram(Base):
    __tablename__ = "training_programs"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    program_id = Column(Integer, ForeignKey("training_programs.id"), nullable=True)

class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    __table_args__ = (UniqueConstraint("course_id","user_id", name="uq_course_user"),)
