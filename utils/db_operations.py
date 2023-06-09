from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from db import Base


def get_in_db(
        db: Session,
        model,
        ident: int
):
    obj = db.query(model).get(ident)
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Bazada bunday malumot yoq"
        )
    return obj


def save_in_db(
        db: Session,
        obj: Base
):
    db.add(obj)
    check_unique(db)
    db.refresh(obj)


def update_in_db(
        db: Session,
        obj: Base
):
    check_unique(db)
    db.refresh(obj)


def check_unique(session: Session) -> None:
    try:
        session.commit()
    except IntegrityError as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{err.orig}"
        )
