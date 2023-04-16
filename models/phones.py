from sqlalchemy import *
from sqlalchemy.orm import relationship

from db import Base
from models.users import Users


class Phones(Base):
    __tablename__ = "phones"

    id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(String(255))
    comment = Column(String(255))
    source = Column(String(255))
    source_id = Column(Integer)
    user_id = Column(Integer)

    user = relationship('Users', foreign_keys=[source_id],
                        primaryjoin=lambda: and_(Users.id == Phones.source_id, Phones.source == "user"))
    # bazaga Customer modeli qoshilgandan keyin bu qismi ishlaydi
    # customer = relationship('Customers', foreign_keys=[source_id],
    #                      primaryjoin=lambda: and_(Customers.id == Phones.source_id, Phones.source == "customer"))

    theuser = relationship('Users', foreign_keys=[user_id], primaryjoin=lambda: and_(Users.id == Phones.user_id),
                        lazy="joined")
