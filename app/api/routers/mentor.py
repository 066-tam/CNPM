from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.ops import DailyLogCreate, DailyLogRead, AssessmentCreate, AssessmentRead, MessageCreate, MessageRead
from app.services.ops_service import OpsService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/daily-logs", response_model=DailyLogRead, status_code=201)
def log_daily(user_id: int, payload: DailyLogCreate, db: Session = Depends(get_db)):
    return OpsService(db).log_daily(user_id=user_id, content=payload.content, log_date=payload.log_date)

@router.post("/assessments", response_model=AssessmentRead, status_code=201)
def assess(mentor_id: int, payload: AssessmentCreate, db: Session = Depends(get_db)):
    return OpsService(db).assess(intern_id=payload.intern_id, mentor_id=mentor_id, comment=payload.comment, score=payload.score)

@router.post("/messages", response_model=MessageRead, status_code=201)
def send_message(sender_id: int, payload: MessageCreate, db: Session = Depends(get_db)):
    return OpsService(db).send_message(sender_id=sender_id, receiver_id=payload.receiver_id, body=payload.body)
