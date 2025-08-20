import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/ims_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Intern Management System (IMS)"
    environment: str = "dev"
    database_url: str = "sqlite:///./default.db"
    allow_origins: list[str] = ["*"]

    class Config:
        env_file = ".env"

settings = Settings()
