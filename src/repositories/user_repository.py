from sqlalchemy.orm import Session
from src.models.user_model import User
from typing import Optional, Iterable

class UserRepository:
    def __init__(self, db: Session): self.db = db

    def list(self) -> Iterable[User]:
        return self.db.query(User).all()

    def get(self, user_id: int) -> Optional[User]:
        return self.db.query(User).get(user_id)

    def get_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter_by(email=email).first()

    def create(self, user: User) -> User:
        self.db.add(user); self.db.flush(); return user

    def delete(self, user_id: int) -> None:
        user = self.get(user_id)
        if user: self.db.delete(user)