from pydantic import BaseModel, EmailStr
from typing import Literal
Role = Literal["Admin","HR","Coordinator","Mentor","Intern"]

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: Role

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    class Config: from_attributes = True
