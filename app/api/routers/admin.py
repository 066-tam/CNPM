
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.user import UserCreate, UserRead
from app.schemas.settings import SettingCreate, SettingRead
from app.models.user import Role
from app.services.admin_service import AdminService
from app.repositories.user_repo import UserRepository

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users", response_model=UserRead, status_code=201)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    svc = AdminService(db)
    return svc.create_user(name=payload.name, email=payload.email, role=Role(payload.role), password=payload.password)

@router.get("/users", response_model=list[UserRead])
def list_users(db: Session = Depends(get_db)):
    return UserRepository(db).list()

@router.post("/settings", response_model=SettingRead, status_code=201)
def upsert_setting(payload: SettingCreate, db: Session = Depends(get_db)):
    return AdminService(db).upsert_setting(payload.key, payload.value)