from pydantic_settings import BaseSettings
from pydantic import field_validator
from typing import List

class Settings(BaseSettings):
    app_name: str = "Intern Management System"
    secret_key: str = "super-secret-key-change-me"
    access_token_expire_minutes: int = 60 * 24
    database_url: str = "sqlite:///./ims.db"
    cors_origins: List[str] = ["*"]

    @field_validator("cors_origins", mode="before")
    def parse_cors(cls, v):
        if isinstance(v, str):
            return [x.strip() for x in v.split(",")]
        return v

    class Config:
        env_file = ".env"

settings = Settings()
