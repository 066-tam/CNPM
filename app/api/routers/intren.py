
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.ops import FeedbackCreate, FeedbackRead, MessageRead
from app.services.ops_service import OpsService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/feedback", response_model=FeedbackRead, status_code=201)
def send_feedback(from_user: int, payload: FeedbackCreate, db: Session = Depends(get_db)):
    return OpsService(db).send_feedback(from_user=from_user, to_user=payload.to_user, body=payload.body)

@router.get("/inbox", response_model=list[MessageRead])
def inbox(user_id: int, db: Session = Depends(get_db)):
    return OpsService(db).inbox(user_id=user_id)
