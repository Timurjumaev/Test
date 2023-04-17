from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db import database
from functions.incomes import get_all_incomes, get_income_by_id, create_new_income, update_old_income
from models.users import Users, UserRole
from schemas.incomes import CreateIncome, UpdateIncome
from utils.login import get_current_active_user

incomes_router = APIRouter(
    prefix="/incomes",
    tags=["Incomes operations"]
)


@incomes_router.get("/")
def get_incomes(
        income_id: Optional[int] = None,
        branch_id: Optional[int] = None,
        current_user: Users = Depends(get_current_active_user),
        db: Session = Depends(database)
):
    if current_user.role in [UserRole.ADMIN, UserRole.CUSTOMER]:
        if income_id:
            return get_income_by_id(
                income_id=income_id,
                branch_id=branch_id,
                current_user=current_user,
                db=db
            )

        return get_all_incomes(
            current_user=current_user,
            db=db
        )

    raise HTTPException(
        detail="Role error",
        status_code=status.HTTP_400_BAD_REQUEST
    )


@incomes_router.post("/")
def create_income(
        data: CreateIncome,
        current_user: Users = Depends(get_current_active_user),
        db: Session = Depends(database)
):
    if current_user.role in [UserRole.CUSTOMER, UserRole.BRANCH_WORKER]:
        print("hjkl")
        return create_new_income(
            data=data,
            current_user=current_user,
            db=db
        )

    raise HTTPException(
        detail="Role error",
        status_code=status.HTTP_400_BAD_REQUEST
    )


# @incomes_router.put("/")
def update_income(
        income_id: int,
        data: UpdateIncome,
        current_user: Users = Depends(get_current_active_user),
        db: Session = Depends(database)
):
    if current_user.role == UserRole.ADMIN:
        tariffs = update_old_income(
            income_id=income_id,
            data=data,
            current_user=current_user,
            db=db
        )
        return tariffs

    raise HTTPException(
        detail="Role error",
        status_code=status.HTTP_400_BAD_REQUEST
    )
