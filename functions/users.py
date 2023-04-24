from fastapi import HTTPException

from utils.pagination import pagination
from models.users import Users
from utils.login import get_password_hash


def all_users(search, page, limit, db):
    if search :
        search_formatted = "%{}%".format(search)
        search_filter = (Users.name.like(search_formatted))
    else :
        search_filter = Users.id > 0
    users = db.query(Users).filter(search_filter).order_by(Users.name.asc())
    return pagination(users, page, limit)


def one_user(id, db):
    return db.query(Users).filter(Users.id == id).first()


def create_user_r(form, db):
    if db.query(Users).filter(Users.username == form.username).first() is None:
        password_hash = get_password_hash(form.password)
        new_user_db = Users(
            name=form.name,
            username=form.username,
            password=form.password,
            password_hash=password_hash,
            address=form.address,
            role=form.role,
            status=form.status
        )
        db.add(new_user_db)
        db.commit()
        db.refresh(new_user_db)
        return new_user_db
    return ("Username error")





def update_user_r(form, db):
    if one_user(form.id, db) is None:
        raise HTTPException(status_code=400, detail="Bunday id raqamli user mavjud emas")
    if db.query(Users).filter(Users.username == form.username).first() is None:
        password_hash = get_password_hash(form.password_hash)
        db.query(Users).filter(Users.id == form.id).update({
            Users.name: form.name,
            Users.username: form.username,
            Users.password: form.password,
            Users.password_hash: password_hash,
            Users.address: form.address,
            Users.role: form.role,
            Users.status: form.status
        })
        db.commit()
    return ("Username error")

