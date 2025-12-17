from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(title="FinTrack API")

# Optional: Read env variables
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")


@app.get("/api/health")
async def health_check():
    """
    Simple health check endpoint.
    Returns 200 OK and basic info.
    """
    return {
        "status": "ok",
        "database_url": DATABASE_URL,
    }


# Example expense model
class Expense(BaseModel):
    id: int
    name: str
    amount: float


# Dummy expenses endpoint
@app.get("/api/expenses")
async def list_expenses():
    return [
        {"id": 1, "name": "Coffee", "amount": 3.5},
        {"id": 2, "name": "Groceries", "amount": 45.0},
    ]
