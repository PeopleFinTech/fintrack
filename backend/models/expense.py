from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, List
import uuid
from models import Category


class Expense(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    amount: float
    date: datetime = Field(default_factory=datetime.utcnow)
    
    # Foreign key to Category
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    
    # Optional: relationship to Category
    category: Optional[Category] = Relationship(back_populates="expenses")
