import enum

from sqlalchemy import Column, Integer, Numeric, DateTime, Enum, String, ForeignKey

from db import Base


class ExpenseType(enum.Enum):
    USER = "USER"


class Expenses(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Numeric(20, 3))
    data = Column(DateTime)
    type = Column(Enum(ExpenseType))
    comment = Column(String(255))

    source_id = Column(Integer)
    # source = relationship()

    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
    # for_id = Column(Integer, ForeignKey("orders.id", ondelete="SET NULL"))
