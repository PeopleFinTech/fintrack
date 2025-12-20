from sqlmodel import Session, select
from models import User
from fastapi import HTTPException
from dotenv import load_dotenv
import os
import jwt
from datetime import datetime

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

class AuthController:
    @staticmethod
    def register(session: Session, email: str, name: str, password: str) -> User:
        # Check if user exists
        existing = session.exec(select(User).where(User.email == email)).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        user = User(email=email, name=name)
        user.hash_password(password)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    @staticmethod
    def login(session: Session, email: str, password: str) -> str:
        user = session.exec(select(User).where(User.email == email)).first()
        if not user or not user.verify_password(password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return user.generate_token()
    
    @staticmethod
    def check_token(session: Session, token: str)-> User:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("sub")
        exp_ts = payload.get("exp")

        if not user_id or not exp_ts:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        exp_dt = datetime.utcfromtimestamp(exp_ts)
        now = datetime.utcnow()

        if exp_dt < now:
            raise HTTPException(status_code=401, detail="Token expired")

        user = session.exec(
            select(User)
            .where(User.id == user_id)
        ).first()
        if not user:
            raise HTTPException(status_code=401, detail="No user found")

        return user
