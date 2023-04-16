from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class Warehouses(Base):
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    address = Column(String(255))
    map_long = Column(Float)
    map_lat = Column(Float)

    # source = relationship()
    source_id = Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
