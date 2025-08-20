
from sqlalchemy.orm import Session
from app.models.user import User, Role
from app.repositories.user_repo import UserRepository
from app.core.security import verify_password, get_password_hash, create_access_token

class AuthService:
    def __init__(self, db: Session):
        self.users = UserRepository(db)

    def authenticate(self, email: str, password: str):
        user = next((u for u in self.users.list() if u.email == email), None)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return create_access_token({"sub": str(user.id), "role": user.role.value})

    def ensure_admin(self):
        admins = [u for u in self.users.list() if u.role == Role.admin]
        if not admins:
            admin = User(name="Admin", email="admin@ims.local", hashed_password=get_password_hash("admin123"), role=Role.admin)
            self.users.create(admin)
