from sqlalchemy.orm import Session
from app.models.settings import Setting
from typing import Iterable, Optional

class SettingRepository:
    def __init__(self, db: Session): self.db = db
    def list(self) -> Iterable[Setting]: return self.db.query(Setting).all()
    def get(self, _id: int) -> Optional[Setting]: return self.db.get(Setting, _id)
    def create(self, obj: Setting) -> Setting:
        self.db.add(obj); self.db.flush(); return obj
    def update(self, _id: int, **data) -> Setting:
        obj = self.get(_id); 
        for k,v in data.items(): setattr(obj, k, v)
        self.db.flush(); return obj
    def delete(self, _id: int) -> None:
        obj = self.get(_id); 
        if obj: self.db.delete(obj)