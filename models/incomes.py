import enum

from sqlalchemy import Column, Integer, Numeric, DateTime, Enum, String, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class IncomeType(enum.Enum):
    USER = "USER"


class Incomes(Base):
    __tablename__ = "incomes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Numeric(20, 3))
    data = Column(DateTime)
    type = Column(Enum(IncomeType))
    comment = Column(String(255))

    source_id = Column(Integer)
    # source = relationship()

    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
    for_id = Column(Integer, ForeignKey("orders.id", ondelete="SET NULL"))
