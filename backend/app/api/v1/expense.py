from fastapi import APIRouter, Form, Depends, Header, HTTPException
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
    authorization: str = Header(...),
    session: Session = Depends(get_session)
):
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=405, detail="Invalid auth scheme")
        authController = AuthController()
        user = authController.check_token(session, token)
    except Exception as e:
        print(f"JWT decode error: {e}")  # prints to container log
        raise HTTPException(status_code=401, detail="Invalid authorization header")

    expenseController= ExpenseController()
    
    return expenseController.add(session, user, name, amount, category)

@router.patch('/update/{id}', response_model=Expense)
def update(
    id: int,
    name:str = Form(...),
    amount: float = Form(...),
    category: str = Form(...),
    authorization: str = Header(...),
    session: Session = Depends(get_session)
):
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=405, detail="Invalid auth scheme")
        authController = AuthController()
        user = authController.check_token(session, token)
    except Exception as e:
        print(f"JWT decode error: {e}")  # prints to container log
        raise HTTPException(status_code=401, detail="Invalid authorization header")

    expenseController= ExpenseController()
    
    return expenseController.update(session, user, id,  name, amount, category)

@router.delete('/{id}')
def update(
    id: int,
    authorization: str = Header(...),
    session: Session = Depends(get_session)
):
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=405, detail="Invalid auth scheme")
        authController = AuthController()
        user = authController.check_token(session, token)
    except Exception as e:
        print(f"JWT decode error: {e}")  # prints to container log
        raise HTTPException(status_code=401, detail="Invalid authorization header")

    expenseController= ExpenseController()
    
    return expenseController.delete(session, user, id)

@router.get('/all')
def all(
    authorization: str = Header(...),
    session: Session = Depends(get_session)
):
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid auth scheme")
        authController = AuthController()
        user = authController.check_token(session, token)
    except Exception as e:
        print(f"JWT decode error: {e}")
        raise HTTPException(status_code=401, detail="Invalid authorization header")
    
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