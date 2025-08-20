
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.recruitment import InterviewCreate, InterviewRead
from app.schemas.training import ProgramCreate, ProgramRead, CourseCreate, CourseRead
from app.schemas.ops import KPICreate, KPIRead
from app.services.ops_service import OpsService
from app.services.training_service import TrainingService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/interviews", response_model=InterviewRead, status_code=201)
def schedule_interview(payload: InterviewCreate, db: Session = Depends(get_db)):
    return OpsService(db).schedule_interview(**payload.dict())

@router.post("/programs", response_model=ProgramRead, status_code=201)
def create_program(payload: ProgramCreate, db: Session = Depends(get_db)):
    return TrainingService(db).create_program(**payload.dict())

@router.post("/courses", response_model=CourseRead, status_code=201)
def create_course(payload: CourseCreate, db: Session = Depends(get_db)):
    return TrainingService(db).create_course(**payload.dict())

@router.post("/kpis", response_model=KPIRead, status_code=201)
def set_kpi(user_id: int, payload: KPICreate, db: Session = Depends(get_db)):
    return OpsService(db).set_kpi(user_id=user_id, name=payload.name, target=payload.target)
