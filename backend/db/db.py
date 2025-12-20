from sqlmodel import SQLModel, create_engine, Session
import os

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://fintrack:fintrack@db:3306/fintrack")

engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    from models import User, Category, Budget, Expense

    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
