from sqlalchemy.orm import Session
from app.models.recruitment import Job
from typing import Iterable, Optional

class JobRepository:
    def __init__(self, db: Session): self.db = db
    def list(self) -> Iterable[Job]: return self.db.query(Job).all()
    def get(self, _id: int) -> Optional[Job]: return self.db.get(Job, _id)
    def create(self, obj: Job) -> Job:
        self.db.add(obj); self.db.flush(); return obj
    def update(self, _id: int, **data) -> Job:
        obj = self.get(_id); 
        for k,v in data.items(): setattr(obj, k, v)
        self.db.flush(); return obj
    def delete(self, _id: int) -> None:
        obj = self.get(_id); 
        if obj: self.db.delete(obj)