from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db import database
from functions.expense import get_expense_by_id, get_all_expenses, create_new_expense
from models.users import Users, UserRole
from schemas.expense import CreateExpense
from utils.login import get_current_user

expenses_router = APIRouter(
    prefix="/expenses",
    tags=["Expenses operations"]
)


@expenses_router.get("/")
def get_expenses(
        expense_id: Optional[int] = None,
        branch_id: Optional[int] = None,
        current_user: Users = Depends(get_current_user),
        db: Session = Depends(database)
):
    if current_user.role in [UserRole.BRANCH_WORKER, UserRole.CUSTOMER]:
        if expense_id:
            return get_expense_by_id(
                current_user=current_user,
                db=db,
                expense_id=expense_id,
                branch_id=branch_id
            )

        return get_all_expenses(
            current_user=current_user,
            db=db
        )

    raise HTTPException(
        detail="Role error",
        status_code=status.HTTP_400_BAD_REQUEST
    )


@expenses_router.post("/")
def create_expense(
        data: CreateExpense,
        current_user: Users = Depends(get_current_user),
        db: Session = Depends(database)
):
    if current_user.role == UserRole.BRANCH_WORKER:
        return create_new_expense(
            data=data,
            current_user=current_user,
            db=db
        )

    raise HTTPException(
        detail="Role error",
        status_code=status.HTTP_400_BAD_REQUEST
    )
