from sqlalchemy.orm import Session
from src.repositories.course_repository import CourseRepository
from src.models.course_model import Course

class CourseService:
    def __init__(self, db: Session):
        self.repo = CourseRepository(db)

    def list(self): return self.repo.list()

    def create(self, title: str, description: str | None = None, program_id: int | None = None):
        return self.repo.create(Course(title=title, description=description, program_id=program_id))

    def update(self, course_id: int, **data):
        return self.repo.update(course_id, **data)

    def delete(self, course_id: int): self.repo.delete(course_id)