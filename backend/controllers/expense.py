from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from models import User, Category, Expense
from typing import List
from fastapi import HTTPException

class ExpenseController:
    @staticmethod
    def add(session: Session, user: User, name: str, amount: float, category:str ):
        categoryModel = session.exec(select(Category).where(Category.name == category)).first()
        if categoryModel:
            category_id = categoryModel.id
        else:
            catgoryModel = Category(name=category)
            session.add(catgoryModel)
            session.commit()
            session.refresh(catgoryModel)
            category_id = catgoryModel.id
        
        expense = Expense(name=name, amount=amount, category_id= category_id, user_id= user.id)
        session.add(expense)
        session.commit()
        session.refresh(expense)

        return expense

    @staticmethod
    def update(session: Session, user: User, id:int, name: str, amount: float, category:str ):
        expenseModel = session.exec(select(Expense).where(Expense.id ==id).options(selectinload(Expense.category))).first()
        if not expenseModel:
            raise HTTPException(status_code= 404, detail = 'expense not found')
        if expenseModel.category.name != category:
            categoryModel = session.exec(select(Category).where(Category.name == category)).first()
            if categoryModel:
                category_id = categoryModel.id
            else:
                catgoryModel = Category(name=category)
                session.add(catgoryModel)
                session.commit()
                session.refresh(catgoryModel)
                category_id = catgoryModel.id
        else:
            category_id = expenseModel.category.id
        
        expenseModel.name = name
        expenseModel.amount = amount
        expenseModel.category_id = category_id


        session.add(expenseModel)
        session.commit()
        session.refresh(expenseModel)

        return expenseModel

    @staticmethod
    def delete(session: Session, user: User, id:int):
        expenseModel = session.exec(select(Expense).where(Expense.id ==id)).first()
        if not expenseModel:
            raise HTTPException(status_code= 404, detail = 'expense not found')
        session.delete(expenseModel)
        session.commit()
        return {'success': True}

    @staticmethod
    def all(session: Session, user_id: int) -> List[Expense]:
        expenses = session.exec(
            select(Expense)
            .where(Expense.user_id == user_id)
            .options(selectinload(Expense.category))
        ).all()


        return expenses
