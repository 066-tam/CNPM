from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    assignee_id: int | None = None

class TodoRead(BaseModel):
    id: int
    title: str
    done: bool
    assignee_id: int | None
    class Config: orm_mode = True