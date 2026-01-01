from fastapi import APIRouter, Form, Depends, Response, status, HTTPException, Cookie
from sqlmodel import Session
from db import get_session
from controllers import AuthController
from models import User

router = APIRouter(prefix="/auth")

@router.post("/register", response_model=User)
def register(
    email: str = Form(...),
    name: str = Form(...),
    password: str = Form(...),
    session: Session = Depends(get_session),
    response: Response = Response()
):
    registeredData = AuthController.register(session, email, name, password)
    response.set_cookie(key="access_token", value=registeredData["token"], samesite="lax", httponly=True, secure=True, max_age=60*60*24)
    return registeredData["user"]

@router.post("/login")
def login(
    email: str = Form(...),
    password: str = Form(...),
    session: Session = Depends(get_session),
    response: Response = Response()
):
    loggedInData = AuthController.login(session, email, password)
    response.set_cookie(key="access_token", value=loggedInData["token"], samesite="lax", httponly=True, secure=True, max_age=60*60*24)
    return loggedInData["user"]


@router.get("/logout")
def logout(
    response: Response = Response()
):
    response.delete_cookie(key="access_token")
    response.status_code = status.HTTP_200_OK
    return {"message": "Logged out successfully"}

@router.get("/me")
def me(
    access_token: str = Cookie(None),
    session: Session = Depends(get_session)
):
    if not access_token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    authController = AuthController()
    user = authController.check_token(session, access_token)
    return user