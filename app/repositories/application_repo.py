from sqlalchemy.orm import Session
from app.models.recruitment import Application
from typing import Iterable, Optional

class ApplicationRepository:
    def __init__(self, db: Session): self.db = db
    def list(self) -> Iterable[Application]: return self.db.query(Application).all()
    def get(self, _id: int) -> Optional[Application]: return self.db.get(Application, _id)
    def create(self, obj: Application) -> Application:
        self.db.add(obj); self.db.flush(); return obj
    def update(self, _id: int, **data) -> Application:
        obj = self.get(_id); 
        for k,v in data.items(): setattr(obj, k, v)
        self.db.flush(); return obj
    def delete(self, _id: int) -> None:
        obj = self.get(_id); 
        if obj: self.db.delete(obj)