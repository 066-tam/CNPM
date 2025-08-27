from sqlalchemy.orm import Session
from app.models.ops import KPI
from typing import Iterable, Optional

class KPIRepository:
    def __init__(self, db: Session): self.db = db
    def list(self) -> Iterable[KPI]: return self.db.query(KPI).all()
    def get(self, _id: int) -> Optional[KPI]: return self.db.get(KPI, _id)
    def create(self, obj: KPI) -> KPI:
        self.db.add(obj); self.db.flush(); return obj
    def update(self, _id: int, **data) -> KPI:
        obj = self.get(_id); 
        for k,v in data.items(): setattr(obj, k, v)
        self.db.flush(); return obj
    def delete(self, _id: int) -> None:
        obj = self.get(_id); 
        if obj: self.db.delete(obj)