from fastapi import HTTPException
from utils.pagination import pagination
from models.phones import Phones
import math


def all_phones(search, page, limit, db):
    if search :
        search_formatted = "%{}%".format(search)
        search_filter = (Phones.phone.like(search_formatted))
    else :
        search_filter = Phones.id > 0
    phones = db.query(Phones).filter(search_filter).order_by(Phones.source.asc())
    return pagination(phones, page, limit)


def one_phone(id, db):
    return db.query(Phones).filter(Phones.id == id).first()


def create_phone_e(form, db, thisuser):
    new_phone_db = Phones(
        phone=form.phone,
        comment=form.comment,
        source=form.source,
        source_id=form.source_id,
        user_id=thisuser.id
    )
    db.add(new_phone_db)
    db.commit()
    db.refresh(new_phone_db)


def update_phone_e(form, db, thisuser):
    if one_phone(form.id, db) is None:
        raise HTTPException(status_code=400, detail="Bunday id raqamli phone mavjud emas")
    db.query(Phones).filter(Phones.id == form.id).update({
        Phones.phone: form.phone,
        Phones.comment: form.comment,
        Phones.source: form.source,
        Phones.source_id: form.source.id,
        Phones.user_id: thisuser.id
    })
    db.commit()
