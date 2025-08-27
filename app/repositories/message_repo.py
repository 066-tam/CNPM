from sqlalchemy.orm import Session
from app.models.ops import Message
from typing import Iterable, Optional

class MessageRepository:
    def __init__(self, db: Session): self.db = db
    def list(self) -> Iterable[Message]: return self.db.query(Message).all()
    def get(self, _id: int) -> Optional[Message]: return self.db.get(Message, _id)
    def create(self, obj: Message) -> Message:
        self.db.add(obj); self.db.flush(); return obj
    def update(self, _id: int, **data) -> Message:
        obj = self.get(_id); 
        for k,v in data.items(): setattr(obj, k, v)
        self.db.flush(); return obj
    def delete(self, _id: int) -> None:
        obj = self.get(_id); 
        if obj: self.db.delete(obj)