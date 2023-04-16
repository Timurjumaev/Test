from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.phones import all_phones, one_phone, create_phone_e, update_phone_e
from utils.login import get_current_active_user
from schemas.phones import CreatePhone, UpdatePhone
from schemas.users import CreateUser
from db import database

phones_router = APIRouter(
    prefix="/phones",
    tags=["Phones operations"]
)


@phones_router.get("/get_phones")
def get_phones(search: str = None, id: int = 0, page: int = 0, limit: int = 25, db: Session = Depends(database),
              current_user: CreateUser = Depends(get_current_active_user)):
    if page < 0 or limit < 0:
        raise HTTPException(status_code=400, detail="page yoki limit 0 dan kichik kiritilmasligi kerak")
    if id > 0:
        return one_phone(id, db)
    return all_phones(search, page, limit, db)


@phones_router.post("/create_phone")
def create_phone(new_phone: CreatePhone, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    create_phone_e(new_phone, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@phones_router.put("/update_phone")
def update_phone(this_phone: UpdatePhone, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    update_phone_e(this_phone, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
