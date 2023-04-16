import enum

from sqlalchemy import Column, Integer, String, Enum, Boolean, and_
from sqlalchemy.orm import relationship

from db import Base
from models.branches import Branches


class UserRole(enum.Enum):
    ADMIN = "ADMIN"
    CUSTOMER = "CUSTOMER"

    BRANCH_ADMIN = "BRANCH_ADMIN"
    BRANCH_WORKER = "BRANCH_WORKER"


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    address = Column(String(255))
    role = Column(Enum(UserRole))
    status = Column(Boolean, default=False)
    token = Column(String(255))
    branch_id = Column(Integer)

    branch = relationship('Branches', foreign_keys=[branch_id], primaryjoin=lambda: and_(Branches.id == Users.branch_id),
                        lazy="joined")
