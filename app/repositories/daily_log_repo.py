
from sqlalchemy.orm import Session
from app.models.ops import DailyLog
from typing import Iterable, Optional

class DailyLogRepository:
    def __init__(self, db: Session): self.db = db
    def list(self) -> Iterable[DailyLog]: return self.db.query(DailyLog).all()
    def get(self, _id: int) -> Optional[DailyLog]: return self.db.get(DailyLog, _id)
    def create(self, obj: DailyLog) -> DailyLog:
        self.db.add(obj); self.db.flush(); return obj
    def update(self, _id: int, **data) -> DailyLog:
        obj = self.get(_id); 
        for k,v in data.items(): setattr(obj, k, v)
        self.db.flush(); return obj
    def delete(self, _id: int) -> None:
        obj = self.get(_id); 
        if obj: self.db.delete(obj)
