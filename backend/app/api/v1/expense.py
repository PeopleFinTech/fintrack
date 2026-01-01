from fastapi import APIRouter, Form, Depends, Cookie, HTTPException
from typing import Annotated
from sqlmodel import Session
from db import get_session
from controllers import AuthController, ExpenseController
from models import Expense

router = APIRouter(prefix="/expense")

@router.post('/add', response_model=Expense)
def add(
    name:str = Form(...),
    amount: float = Form(...),
    category: str = Form(...),
    access_token: Annotated[str | None, Cookie()] = None,
    session: Session = Depends(get_session)
):
    try:
        if not access_token:
            raise HTTPException(status_code=401, detail="Unauthorized")
        authController = AuthController()
        user = authController.check_token(session, access_token)
    except Exception as e:
        print(f"JWT decode error: {e}")
        raise HTTPException(status_code=401, detail="Unauthorized")

    expenseController= ExpenseController()
    
    return expenseController.add(session, user, name, amount, category)

@router.patch('/update/{id}', response_model=Expense)
def update(
    id: int,
    name:str = Form(...),
    amount: float = Form(...),
    category: str = Form(...),
    access_token: Annotated[str | None, Cookie()] = None,
    session: Session = Depends(get_session)
):
    try:
        if not access_token:
            raise HTTPException(status_code=401, detail="Unauthorized")
        authController = AuthController()
        user = authController.check_token(session, access_token)
    except Exception as e:
        print(f"JWT decode error: {e}")
        raise HTTPException(status_code=401, detail="Unauthorized")

    expenseController= ExpenseController()
    
    return expenseController.update(session, user, id,  name, amount, category)

@router.delete('/{id}')
def update(
    id: int,
    access_token: Annotated[str | None, Cookie()] = None,
    session: Session = Depends(get_session)
):
    try:
        if not access_token:
            raise HTTPException(status_code=401, detail="Unauthorized")
        authController = AuthController()
        user = authController.check_token(session, access_token)
    except Exception as e:
        print(f"JWT decode error: {e}")
        raise HTTPException(status_code=401, detail="Unauthorized")

    expenseController= ExpenseController()
    
    return expenseController.delete(session, user, id)

@router.get('/all')
def all(
    access_token: Annotated[str | None, Cookie()] = None,
    session: Session = Depends(get_session)
):
    try:
        if not access_token:
            raise HTTPException(status_code=401, detail="Unauthorized")
        authController = AuthController()
        user = authController.check_token(session, access_token)
    except Exception as e:
        print(f"JWT decode error: {e}")
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    expenseController= ExpenseController()
    expenses = expenseController.all(session, user.id)

    result = [
        {
            "id": e.id,
            "name": e.name,
            "amount": e.amount,
            "date": e.date,
            "category": e.category.name if e.category else None,
            "category_id": e.category_id
        }
        for e in expenses
    ]
    return result