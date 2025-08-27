from pydantic import BaseModel
from typing import Optional

class ProgramCreate(BaseModel):
    title: str
    description: Optional[str] = None

class ProgramRead(BaseModel):
    id: int; title: str; description: Optional[str] = None
    class Config: from_attributes = True

class CourseCreate(BaseModel):
    title: str
    description: Optional[str] = None
    program_id: Optional[int] = None

class CourseRead(BaseModel):
    id: int; title: str; description: Optional[str] = None; program_id: Optional[int] = None
    class Config: from_attributes = True
