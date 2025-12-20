from sqlmodel import SQLModel, Field, create_engine, Session, select
from datetime import datetime, timedelta
import bcrypt
import uuid
import jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str = Field(index=True, nullable=False, unique=True)
    password: str = Field(nullable=False)
    name: str
    is_active: bool = Field(default=True)
    is_deleted: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def hash_password(self, password: str):
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode(), self.password.encode())

    def generate_token(self, expire_days: int = 1) -> str:
        payload = {
            "sub": str(self.id),
            "exp": datetime.utcnow() + timedelta(days=expire_days)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")