from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional
from models import User, Category


class Budget(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    
    # Foreign keys
    user_id: int = Field(foreign_key="user.id")
    category_id: int = Field(foreign_key="category.id")
    
    # Relationships
    user: Optional[User] = Relationship()
    category: Optional[Category] = Relationship()
    
    amount: float
    monthly_budget: bool = False
    yearly_budget: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
