from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.infrastructure.databases.base import db_session
from src.api.schemas.todo import TodoCreate, TodoRead
from src.services.todo_service import TodoService

router = APIRouter()

def get_db():
    with db_session() as s:
        yield s

@router.get("/", response_model=list[TodoRead])
def list_todos(db: Session = Depends(get_db)):
    return TodoService(db).list()

@router.post("/", response_model=TodoRead, status_code=201)
def create_todo(payload: TodoCreate, db: Session = Depends(get_db)):
    return TodoService(db).create(**payload.dict())

@router.post("/{todo_id}/complete", response_model=TodoRead)
def complete(todo_id: int, db: Session = Depends(get_db)):
    todo = TodoService(db).complete(todo_id)
    if not todo: raise HTTPException(404, "Todo not found")
    return todo

@router.delete("/{todo_id}", status_code=204)
def delete(todo_id: int, db: Session = Depends(get_db)):
    TodoService(db).delete(todo_id)
    return None
