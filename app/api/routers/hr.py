
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.recruitment import CampaignCreate, CampaignRead, JobCreate, JobRead, ApplicationCreate, ApplicationRead
from app.services.recruitment_service import RecruitmentService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/campaigns", response_model=CampaignRead, status_code=201)
def create_campaign(payload: CampaignCreate, db: Session = Depends(get_db)):
    return RecruitmentService(db).create_campaign(**payload.dict())

@router.post("/jobs", response_model=JobRead, status_code=201)
def create_job(payload: JobCreate, db: Session = Depends(get_db)):
    return RecruitmentService(db).create_job(**payload.dict())

@router.post("/applications", response_model=ApplicationRead, status_code=201)
def submit_application(payload: ApplicationCreate, db: Session = Depends(get_db)):
    return RecruitmentService(db).submit_application(**payload.dict())
