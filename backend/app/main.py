from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from app.api.router import api_router
from db import create_db_and_tables

app = FastAPI(title="FinTrack API")

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

if ENVIRONMENT == "development":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
            "http://localhost:80",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(api_router)
