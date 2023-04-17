from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db import database
from functions.tariifs import get_all_tariffs, get_tariff_by_id, update_old_tariff, create_new_tariff
from models.users import Users, UserRole
from schemas.tariifs import CreateTariff, UpdateTariff
from utils.login import get_current_active_user

tariffs_router = APIRouter(
    prefix="/tariffs",
    tags=["Tariffs operations"]
)


@tariffs_router.get("/")
def get_tariffs(
        tariff_id: Optional[int] = None,
        current_user: Users = Depends(get_current_active_user),
        db: Session = Depends(database)
):
    if current_user.role in [UserRole.ADMIN, UserRole.CUSTOMER]:
        if tariff_id:
            return get_tariff_by_id(
                tariff_id=tariff_id,
                db=db
            )

        return get_all_tariffs(
            db=db
        )

    raise HTTPException(
        detail="Role error",
        status_code=status.HTTP_400_BAD_REQUEST
    )


@tariffs_router.post("/")
def create_tariff(
        data: CreateTariff,
        current_user: Users = Depends(get_current_active_user),
        db: Session = Depends(database)
):
    if current_user.role == UserRole.ADMIN:
        tariff = create_new_tariff(
            data=data,
            current_user=current_user,
            db=db
        )
        return tariff

    raise HTTPException(
        detail="Role error",
        status_code=status.HTTP_400_BAD_REQUEST
    )


@tariffs_router.put("/")
def update_tariff(
        data: UpdateTariff,
        current_user: Users = Depends(get_current_active_user),
        db: Session = Depends(database)
):
    if current_user.role == UserRole.ADMIN:
        tariff = update_old_tariff(
            data=data,
            db=db
        )
        return tariff

    raise HTTPException(
        detail="Role error",
        status_code=status.HTTP_400_BAD_REQUEST
    )
