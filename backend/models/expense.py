from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, List
import uuid
from models import Category, User


class Expense(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    amount: float
    date: datetime = Field(default_factory=datetime.utcnow)
    
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    category: Optional[Category] = Relationship(back_populates="expenses")

    user_id: int = Field(foreign_key="user.id")
    user: Optional[User] = Relationship()
