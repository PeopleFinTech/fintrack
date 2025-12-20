from fastapi import FastAPI
from app.api.router import api_router
from db import create_db_and_tables

app = FastAPI(title="FinTrack API")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(api_router)
