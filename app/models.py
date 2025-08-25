from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    full_name: Optional[str] = None
    hashed_password: str
    role: str  # 'admin','hr','coordinator','mentor','intern'
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

    profile: Optional['InternProfile'] = Relationship(back_populates='user')

class InternProfile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='user.id')
    university: Optional[str] = None
    major: Optional[str] = None
    year: Optional[str] = None
    resume: Optional[str] = None

    user: User = Relationship(back_populates='profile')

class Internship(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    created_by: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Application(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    internship_id: int = Field(foreign_key='internship.id')
    user_id: int = Field(foreign_key='user.id')
    status: str = Field(default='applied')  # applied, interviewing, accepted, rejected
    applied_at: datetime = Field(default_factory=datetime.utcnow)

class TrainingProgram(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    coordinator_id: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    assigned_to: Optional[int] = None  # user id (intern)
    mentor_id: Optional[int] = None
    due_date: Optional[datetime] = None
    status: str = Field(default='todo')
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Feedback(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    task_id: Optional[int] = None
    from_user_id: Optional[int] = None
    to_user_id: Optional[int] = None
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class PerformanceEntry(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    intern_id: int
    mentor_id: Optional[int] = None
    kpi_name: str
    kpi_value: float
    recorded_at: datetime = Field(default_factory=datetime.utcnow)
