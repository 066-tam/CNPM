
from fastapi import FastAPI
from app.db.session import engine, SessionLocal
from app.db.base import Base
from app.middleware.logging import LoggingMiddleware
from app.core.config import settings
from app.api.routers import auth, hr, coordinator, mentor, intern, admin, dashboard

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)
app.add_middleware(LoggingMiddleware)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(hr.router, prefix="/hr", tags=["HR Managers"])
app.include_router(coordinator.router, prefix="/coordinator", tags=["Internship Coordinators"])
app.include_router(mentor.router, prefix="/mentor", tags=["Mentors"])
app.include_router(intern.router, prefix="/intern", tags=["Interns"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard & Analytics"])
