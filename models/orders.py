from sqlalchemy import Column, Integer, String

from db import Base


class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
