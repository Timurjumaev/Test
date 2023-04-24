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

    # kimga
    destination_id = Column(Integer)
    # destination = relationship()

    # nam uchun
    for_id = Column(Integer)

    # kimdan
    branch_id = Column(Integer, ForeignKey("branches.id", ondelete="SET NULL"))

    # kim yaratgan
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
