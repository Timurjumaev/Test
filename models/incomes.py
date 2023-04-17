import enum

from sqlalchemy import Column, Integer, Numeric, DateTime, Enum, String, ForeignKey

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

    # kimdan
    source_id = Column(Integer)
    # source = relationship()

    # nma uchun
    for_id = Column(Integer)

    # kimga
    branch_id = Column(Integer, ForeignKey("branches.id", ondelete="SET NULL"))

    # kim yaratgan
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
