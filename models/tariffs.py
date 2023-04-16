from sqlalchemy import Column, Integer, String, ForeignKey, Numeric

from db import Base


class Tariffs(Base):
    __tablename__ = "tariffs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    cost = Column(Numeric(20, 3), nullable=False)
    comment = Column(String(255))

    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
