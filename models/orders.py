from sqlalchemy import Column, Integer

from db import Base


class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
