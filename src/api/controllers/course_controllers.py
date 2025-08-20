from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.infrastructure.databases.base import db_session
from src.services.course_service import CourseService
from pydantic import BaseModel

class CourseCreate(BaseModel):
    title: str
    description: str | None = None
    program_id: int | None = None

class CourseRead(BaseModel):
    id: int
    title: str
    description: str | None
    program_id: int | None
    class Config: orm_mode = True

router = APIRouter()

def get_db():
    with db_session() as s:
        yield s

@router.get("/", response_model=list[CourseRead])
def list_courses(db: Session = Depends(get_db)):
    return CourseService(db).list()

@router.post("/", response_model=CourseRead, status_code=201)
def create_course(payload: CourseCreate, db: Session = Depends(get_db)):
    return CourseService(db).create(**payload.dict())