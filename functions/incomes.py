from datetime import datetime
from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.branches import Branches
from models.incomes import Incomes
from models.users import Users, UserRole
from schemas.incomes import CreateIncome, UpdateIncome
from utils import db_operations


def get_all_incomes(
        current_user: Users,
        db: Session
):
    if current_user.role == UserRole.CUSTOMER:
        branches = db.query(Branches).filter_by(owner_id=current_user.id).all()
        incomes = None
        for branch in branches:
            income = db.query(Incomes).filter_by(branch_id=branch.id).all()

            if incomes:
                incomes += income

            incomes = income

        return incomes

    return db.query(Incomes).filter_by(branch_id=None).all()


def get_income_by_id(
        current_user: Users,
        db: Session,
        income_id: int,
        branch_id: Optional[int] = None,
):
    if current_user.role == UserRole.CUSTOMER:
        if not branch_id:
            raise HTTPException(
                detail="Branch id korsatilmagan",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        # Customer get qilyatgan branch ozinikimi yoki yogmi shuni tekshiryappmiz
        # argar boshqa branch incominini get qilmohchi bosa null qaytariladi
        branch = db.query(Branches).filter_by(id=branch_id, owner_id=current_user.id).first()
        if not branch:
            return branch

    else:
        branch_id = None

    return db.query(Incomes).filter_by(id=income_id, branch_id=branch_id).first()


def create_new_income(
        data: CreateIncome,
        current_user: Users,
        db: Session
):
    income = Incomes(
        **data.dict(),
        data=datetime.now(),
        user_id=current_user.id,
    )

    if current_user.role == UserRole.CUSTOMER:
        income.branch_id = None
    else:
        if not current_user.branch_id:
            raise HTTPException(
                detail="User haven't branch",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        income.branch_id = current_user.branch_id

    db_operations.save_in_db(db, income)

    return income


def update_old_income(
        income_id: int,
        data: UpdateIncome,
        current_user: Users,
        db: Session
):
    pass
