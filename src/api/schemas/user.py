from pydantic import BaseModel, EmailStr
from src.domain.models.constants import Role

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    role: Role

class UserRead(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: Role
    class Config: orm_mode = True