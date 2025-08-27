from sqlalchemy.orm import Session
from app.models.ops import Interview
from typing import Iterable, Optional

class InterviewRepository:
    def __init__(self, db: Session): self.db = db
    def list(self) -> Iterable[Interview]: return self.db.query(Interview).all()
    def get(self, _id: int) -> Optional[Interview]: return self.db.get(Interview, _id)
    def create(self, obj: Interview) -> Interview:
        self.db.add(obj); self.db.flush(); return obj
    def update(self, _id: int, **data) -> Interview:
        obj = self.get(_id); 
        for k,v in data.items(): setattr(obj, k, v)
        self.db.flush(); return obj
    def delete(self, _id: int) -> None:
        obj = self.get(_id); 
        if obj: self.db.delete(obj)
