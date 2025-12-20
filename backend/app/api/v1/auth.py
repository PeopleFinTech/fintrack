from fastapi import APIRouter, Form, Depends
from sqlmodel import Session
from db import get_session
from controllers.Auth import AuthController
from models.user import User

router = APIRouter(prefix="/auth")

@router.post("/register", response_model=User)
def register(
    email: str = Form(...),
    name: str = Form(...),
    password: str = Form(...),
    session: Session = Depends(get_session)
):
    return AuthController.register(session, email, name, password)

@router.post("/login")
def login(
    email: str = Form(...),
    password: str = Form(...),
    session: Session = Depends(get_session)
):
    token = AuthController.login(session, email, password)
    return {"access_token": token, "token_type": "bearer"}
