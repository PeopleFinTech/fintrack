from fastapi import FastAPI, APIRouter

app = FastAPI(title="FinTrack API")
api_router = APIRouter(prefix="/api")

@api_router.get("/health")
async def health_check():
    return {"status": "ok"}

@api_router.get("/expenses")
async def list_expenses():
    return [
        {"id": 1, "name": "Coffee", "amount": 3.5},
        {"id": 2, "name": "Groceries", "amount": 45.0},
    ]

app.include_router(api_router)