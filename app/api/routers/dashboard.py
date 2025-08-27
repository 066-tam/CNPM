from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.repositories.application_repo import ApplicationRepository
from app.repositories.job_repo import JobRepository
from app.repositories.kpi_repo import KPIRepository

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/summary")
def summary(db: Session = Depends(get_db)):
    apps = ApplicationRepository(db).list()
    jobs = JobRepository(db).list()
    kpis = KPIRepository(db).list()
    return {
        "total_jobs": len(jobs),
        "total_applications": len(apps),
        "avg_kpi": (sum(k.value for k in kpis)/len(kpis)) if kpis else 0.0,
    }
