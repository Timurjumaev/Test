from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.users import create_user_r, all_users, one_user, update_user_r
from models.users import UserRole
from utils.login import get_current_active_user
from schemas.users import CreateUser, UpdateUser
from db import database

users_router = APIRouter(
    prefix="/users",
    tags=["Users operation"]
)


@users_router.get("/get_users")
def get_users(search: str = None, id: int = 0, page: int = 1, limit: int = 25, db: Session = Depends(database),
              current_user: CreateUser = Depends(get_current_active_user)):
    if current_user.role == UserRole.ADMIN:
        if page < 0 or limit < 0:
            raise HTTPException(status_code=400, detail="page yoki limit 0 dan kichik kiritilmasligi kerak")
        if id > 0:
            return one_user(id, db)
        return all_users(search, page, limit, db)
    raise HTTPException(status_code=401, detail='You is not admin user!')

@users_router.post("/create_user")
def create_user(new_user: CreateUser, db: Session = Depends(database)):
                # current_user: CreateUser = Depends(get_current_active_user)):

        create_user_r(new_user, db)
        raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")



@users_router.put("/update_user")
def update_user(this_user: UpdateUser, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=400, detail="Sizga ruhsat berilmagan")
    update_user_r(this_user, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")






