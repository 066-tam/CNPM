
from pydantic import BaseModel
from typing import Optional
from datetime import date

class DailyLogCreate(BaseModel):
    content: str
    log_date: date

class DailyLogRead(BaseModel):
    id: int; user_id: int; log_date: date; content: str
    class Config: from_attributes = True

class KPICreate(BaseModel):
    name: str; target: float

class KPIRead(BaseModel):
    id: int; user_id: int; name: str; target: float; value: float
    class Config: from_attributes = True

class FeedbackCreate(BaseModel):
    to_user: int; body: str

class FeedbackRead(BaseModel):
    id: int; from_user: int; to_user: int; body: str
    class Config: from_attributes = True

class AssessmentCreate(BaseModel):
    intern_id: int; comment: str; score: int

class AssessmentRead(BaseModel):
    id: int; intern_id: int; mentor_id: int; comment: str; score: int
    class Config: from_attributes = True

class MessageCreate(BaseModel):
    receiver_id: int; body: str

class MessageRead(BaseModel):
    id: int; sender_id: int; receiver_id: int; body: str
    class Config: from_attributes = True
