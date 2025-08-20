
from sqlalchemy.orm import Session
from app.models.settings import Setting
from app.models.user import User, Role
from app.repositories.setting_repo import SettingRepository
from app.repositories.user_repo import UserRepository
from app.core.security import get_password_hash

class AdminService:
    def __init__(self, db: Session):
        self.settings = SettingRepository(db)
        self.users = UserRepository(db)

    def upsert_setting(self, key: str, value: str):
        existing = next((s for s in self.settings.list() if s.key == key), None)
        if existing: return self.settings.update(existing.id, value=value)
        return self.settings.create(Setting(key=key, value=value))

    def create_user(self, name: str, email: str, role: Role, password: str):
        user = User(name=name, email=email, role=role, hashed_password=get_password_hash(password))
        return self.users.create(user)
