from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey

from db import Base


class Branches(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    address = Column(String(255))
    map_long = Column(Float)
    map_lat = Column(Float)
    status = Column(Boolean)

    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    tariff_id = Column(Integer, ForeignKey("tariffs.id", ondelete="SET NULL"))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
