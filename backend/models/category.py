from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class Category(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

    # Back-reference to expenses
    expenses: List["Expense"] = Relationship(back_populates="category")
