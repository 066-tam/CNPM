
from sqlalchemy.orm import Session
from app.models.ops import Feedback
from typing import Iterable, Optional

class FeedbackRepository:
    def __init__(self, db: Session): self.db = db
    def list(self) -> Iterable[Feedback]: return self.db.query(Feedback).all()
    def get(self, _id: int) -> Optional[Feedback]: return self.db.get(Feedback, _id)
    def create(self, obj: Feedback) -> Feedback:
        self.db.add(obj); self.db.flush(); return obj
    def update(self, _id: int, **data) -> Feedback:
        obj = self.get(_id); 
        for k,v in data.items(): setattr(obj, k, v)
        self.db.flush(); return obj
    def delete(self, _id: int) -> None:
        obj = self.get(_id); 
        if obj: self.db.delete(obj)