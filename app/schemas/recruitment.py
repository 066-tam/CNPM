from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime

class CampaignCreate(BaseModel):
    title: str
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None

class CampaignRead(BaseModel):
    id: int; title: str; description: Optional[str] = None
    class Config: from_attributes = True

class JobCreate(BaseModel):
    title: str
    campaign_id: int
    description: Optional[str] = None

class JobRead(BaseModel):
    id: int; title: str; campaign_id: int; description: Optional[str] = None
    class Config: from_attributes = True

class ApplicationCreate(BaseModel):
    job_id: int; full_name: str; email: EmailStr; cv_url: Optional[str] = None

class ApplicationRead(BaseModel):
    id: int; job_id: int; full_name: str; email: EmailStr; status: str
    class Config: from_attributes = True

class InterviewCreate(BaseModel):
    application_id: int
    scheduled_at: datetime
    channel: str = "online"
    room: Optional[str] = None

class InterviewRead(BaseModel):
    id: int; application_id: int; scheduled_at: datetime; channel: str; room: Optional[str] = None
    class Config: from_attributes = True
