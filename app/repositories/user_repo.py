from sqlalchemy.orm import Session
from app.models.user import User
from typing import Iterable, Optional

class UserRepository:
    def __init__(self, db: Session): self.db = db
    def list(self) -> Iterable[User]: return self.db.query(User).all()
    def get(self, _id: int) -> Optional[User]: return self.db.get(User, _id)
    def create(self, obj: User) -> User:
        self.db.add(obj); self.db.flush(); return obj
    def update(self, _id: int, **data) -> User:
        obj = self.get(_id); 
        for k,v in data.items(): setattr(obj, k, v)
        self.db.flush(); return obj
    def delete(self, _id: int) -> None:
        obj = self.get(_id); 
        if obj: self.db.delete(obj)