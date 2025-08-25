from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: Optional[str]
    role: Optional[str]

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None
    role: str

class UserRead(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str]
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class InternshipCreate(BaseModel):
    title: str
    description: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class InternshipRead(InternshipCreate):
    id: int
    created_by: Optional[int]
    created_at: datetime

    class Config:
        orm_mode = True

class InternProfileCreate(BaseModel):
    user_id: int
    university: Optional[str] = None
    major: Optional[str] = None
    year: Optional[str] = None
    resume: Optional[str] = None

class InternProfileRead(InternProfileCreate):
    id: int

    class Config:
        orm_mode = True

class ApplicationCreate(BaseModel):
    internship_id: int

class ApplicationRead(BaseModel):
    id: int
    internship_id: int
    user_id: int
    status: str
    applied_at: datetime

    class Config:
        orm_mode = True

class TrainingCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TrainingRead(TrainingCreate):
    id: int
    coordinator_id: Optional[int]
    created_at: datetime

    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_to: Optional[int] = None
    due_date: Optional[datetime] = None

class TaskRead(TaskCreate):
    id: int
    mentor_id: Optional[int]
    status: str
    created_at: datetime

    class Config:
        orm_mode = True

class FeedbackCreate(BaseModel):
    task_id: Optional[int] = None
    to_user_id: Optional[int] = None
    content: str

class FeedbackRead(FeedbackCreate):
    id: int
    from_user_id: Optional[int]
    created_at: datetime

    class Config:
        orm_mode = True

class PerformanceCreate(BaseModel):
    intern_id: int
    kpi_name: str
    kpi_value: float

class PerformanceRead(PerformanceCreate):
    id: int
    mentor_id: Optional[int]
    recorded_at: datetime

    class Config:
        orm_mode = True