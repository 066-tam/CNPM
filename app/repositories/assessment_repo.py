
from sqlalchemy.orm import Session
from app.models.ops import Assessment
from typing import Iterable, Optional

class AssessmentRepository:
    def __init__(self, db: Session): self.db = db
    def list(self) -> Iterable[Assessment]: return self.db.query(Assessment).all()
    def get(self, _id: int) -> Optional[Assessment]: return self.db.get(Assessment, _id)
    def create(self, obj: Assessment) -> Assessment:
        self.db.add(obj); self.db.flush(); return obj
    def update(self, _id: int, **data) -> Assessment:
        obj = self.get(_id); 
        for k,v in data.items(): setattr(obj, k, v)
        self.db.flush(); return obj
    def delete(self, _id: int) -> None:
        obj = self.get(_id); 
        if obj: self.db.delete(obj)