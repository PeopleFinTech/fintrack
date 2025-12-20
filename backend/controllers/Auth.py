from sqlmodel import Session, select
from models import User
from fastapi import HTTPException
from dotenv import load_dotenv
import os

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
    def check_token(token: str)-> User:
        id = jwt.decode(token, SECRET_KEY, algorithms=["HS256"]).get("sub")
        exp = jwt.decode(token, SECRET_KEY, algorithms=["HS256"]).get("exp")
        if not id or not exp:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        if exp < datetime.now():
            raise HTTPException(status_code=401, detail="Token expired")
        user = User.filter(id=id).first()
        if not user:
            raise HTTPException(status_code=401, detail="No user found")
        return user
