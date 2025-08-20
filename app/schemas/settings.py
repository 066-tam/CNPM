from pydantic import BaseModel
class SettingCreate(BaseModel):
    key: str; value: str
class SettingRead(BaseModel):
    id: int; key: str; value: str
    class Config: from_attributes = True