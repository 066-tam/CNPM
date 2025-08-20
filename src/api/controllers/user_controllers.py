from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.infrastructure.databases.base import db_session
from src.api.schemas.user import UserCreate, UserRead
from src.models.user_model import User
from src.repositories.user_repository import UserRepository

router = APIRouter()

def get_db():
    with db_session() as s:
        yield s

@router.get("/", response_model=list[UserRead])
def list_users(db: Session = Depends(get_db)):
    return UserRepository(db).list()

@router.post("/", response_model=UserRead, status_code=201)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    if repo.get_by_email(payload.email):
        raise HTTPException(409, "Email already exists")
    user = User(**payload.dict())
    return repo.create(user)
