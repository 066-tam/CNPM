from sqlalchemy.orm import Session
from app.models.training import Course
from typing import Iterable, Optional

class CourseRepository:
    def __init__(self, db: Session): self.db = db
    def list(self) -> Iterable[Course]: return self.db.query(Course).all()
    def get(self, _id: int) -> Optional[Course]: return self.db.get(Course, _id)
    def create(self, obj: Course) -> Course:
        self.db.add(obj); self.db.flush(); return obj
    def update(self, _id: int, **data) -> Course:
        obj = self.get(_id); 
        for k,v in data.items(): setattr(obj, k, v)
        self.db.flush(); return obj
    def delete(self, _id: int) -> None:
        obj = self.get(_id); 
        if obj: self.db.delete(obj)