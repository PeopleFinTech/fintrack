from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import os

app = FastAPI(title="FinTrack API")
api_router = APIRouter(prefix="/api")  # Add /api prefix

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")


@api_router.get("/health")
async def health_check():
    return {"status": "ok"}


class Expense(BaseModel):
    id: int
    name: str
    amount: float


@api_router.get("/expenses")
async def list_expenses():
    return [
        {"id": 1, "name": "Coffee", "amount": 3.5},
        {"id": 2, "name": "Groceries", "amount": 45.0},
    ]


app.include_router(api_router)
