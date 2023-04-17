from sqlalchemy.orm import Session

from models.tariffs import Tariffs
from models.users import Users
from schemas.tariifs import UpdateTariff, CreateTariff
from utils import db_operations


def get_all_tariffs(
        db: Session
):
    return db.query(Tariffs).all()


def get_tariff_by_id(
        tariff_id: int,
        db: Session
):
    tariff = db_operations.get_in_db(
        db=db,
        model=Tariffs,
        ident=tariff_id
    )

    return tariff


def create_new_tariff(
        data: CreateTariff,
        current_user: Users,
        db: Session
):
    tariff = Tariffs(
        **data.dict(),
        user_id=current_user.id
    )

    db_operations.save_in_db(db, tariff)

    return tariff


def update_old_tariff(
        data: UpdateTariff,
        db: Session
):
    tariff = get_tariff_by_id(
        tariff_id=data.id,
        db=db
    )

    for field, value in data:
        if field != "id":
            setattr(tariff, field, value)

    db_operations.update_in_db(db, tariff)

    return tariff
