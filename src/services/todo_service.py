from sqlalchemy.orm import Session
from src.repositories.todo_repository import TodoRepository
from src.models.todo_model import Todo

class TodoService:
    def __init__(self, db: Session):
        self.repo = TodoRepository(db)

    def list(self): return self.repo.list()

    def create(self, title: str, assignee_id: int | None = None):
        return self.repo.create(Todo(title=title, assignee_id=assignee_id))

    def complete(self, todo_id: int):
        return self.repo.update(todo_id, done=True)

    def delete(self, todo_id: int):
        self.repo.delete(todo_id)
