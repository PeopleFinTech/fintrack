from fastapi import APIRouter
from app.api.v1 import auth, health, expense

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(health.router)
v1_router.include_router(auth.router)
v1_router.include_router(expense.router)
