from sqlalchemy.orm import Session
from src.models.todo_model import Todo
from typing import Optional, Iterable

class TodoRepository:
    def __init__(self, db: Session): self.db = db

    def list(self) -> Iterable[Todo]:
        return self.db.query(Todo).all()

    def get(self, todo_id: int) -> Optional[Todo]:
        return self.db.query(Todo).get(todo_id)

    def create(self, todo: Todo) -> Todo:
        self.db.add(todo); self.db.flush(); return todo

    def update(self, todo_id: int, **data) -> Todo:
        todo = self.get(todo_id); 
        for k,v in data.items(): setattr(todo, k, v)
        self.db.flush(); return todo

    def delete(self, todo_id: int) -> None:
        todo = self.get(todo_id)
        if todo: self.db.delete(todo)
