from sqlalchemy.orm import Session
from src.models.course_model import Course
from typing import Optional, Iterable

class CourseRepository:
    def __init__(self, db: Session): self.db = db

    def list(self) -> Iterable[Course]:
        return self.db.query(Course).all()

    def get(self, course_id: int) -> Optional[Course]:
        return self.db.query(Course).get(course_id)

    def create(self, course: Course) -> Course:
        self.db.add(course); self.db.flush(); return course

    def update(self, course_id: int, **data) -> Course:
        course = self.get(course_id)
        for k,v in data.items(): setattr(course, k, v)
        self.db.flush(); return course

    def delete(self, course_id: int) -> None:
        course = self.get(course_id)
        if course: self.db.delete(course)