from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from db import Base


def get_in_db(
        session: Session,
        model: Base,
        ident: int
):
    obj = session.query(model).get(ident)
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Запись с идентификатором {ident} нет в базе!"
        )
    return obj


def save_in_db(
        session: Session,
        obj: Base
):
    session.add(obj)
    check_unique(session)
    session.refresh(obj)


def update_in_db(
        session: Session,
        obj: Base
):
    check_unique(session)
    session.refresh(obj)


def delete_in_db(
        session: Session,
        obj: Base
):
    session.delete(obj)
    session.commit()


def check_unique(session: Session) -> None:
    try:
        session.commit()
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Такое имя уже занято"
        )
