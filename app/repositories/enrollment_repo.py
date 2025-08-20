from sqlalchemy.orm import Session
from app.models.training import Enrollment
from typing import Iterable, Optional

class EnrollmentRepository:
    def __init__(self, db: Session): self.db = db
    def list(self) -> Iterable[Enrollment]: return self.db.query(Enrollment).all()
    def get(self, _id: int) -> Optional[Enrollment]: return self.db.get(Enrollment, _id)
    def create(self, obj: Enrollment) -> Enrollment:
        self.db.add(obj); self.db.flush(); return obj
    def update(self, _id: int, **data) -> Enrollment:
        obj = self.get(_id); 
        for k,v in data.items(): setattr(obj, k, v)
        self.db.flush(); return obj
    def delete(self, _id: int) -> None:
        obj = self.get(_id); 
        if obj: self.db.delete(obj)