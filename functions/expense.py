from datetime import datetime
from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.branches import Branches
from models.expenses import Expenses
from models.users import Users, UserRole
from schemas.expense import CreateExpense
from utils import db_operations


def get_all_expenses(
        current_user: Users,
        db: Session
):
    if current_user.role == UserRole.CUSTOMER:
        branches = db.query(Branches).filter_by(owner_id=current_user.id).all()
        expenses = None
        for branch in branches:
            expense = db.query(Expenses).filter_by(branch_id=branch.id).all()

            if expenses:
                expenses += expense

            expenses = expense

        return expenses

    if not current_user.branch_id:
        raise HTTPException(
            detail="User haven't branch",
            status_code=status.HTTP_400_BAD_REQUEST
        )

    return db.query(Expenses).filter_by(branch_id=current_user.branch_id).all()


def get_expense_by_id(
        current_user: Users,
        db: Session,
        expense_id: int,
        branch_id: Optional[int] = None
):
    if current_user.role == UserRole.CUSTOMER:
        if not branch_id:
            raise HTTPException(
                detail="Branch id korsatilmagan",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        # Customer get qilyatgan branch ozinikimi yoki yogmi shuni tekshiryappmiz
        # argar boshqa branch expensini get qilmohchi bosa null qaytariladi
        branch = db.query(Branches).filter_by(id=branch_id, owner_id=current_user.id).first()
        if not branch:
            return branch

    else:
        branch_id = current_user.branch_id

    return db.query(Expenses).filter_by(id=expense_id, branch_id=branch_id).first()


def create_new_expense(
        data: CreateExpense,
        current_user: Users,
        db: Session
):
    expense = Expenses(
        **data.dict(),
        data=datetime.now(),
        user_id=current_user.id,
        branch_id=current_user.branch_id
    )

    if not current_user.branch_id:
        raise HTTPException(
            detail="User haven't branch",
            status_code=status.HTTP_400_BAD_REQUEST
        )

    db_operations.save_in_db(db, expense)

    return expense
