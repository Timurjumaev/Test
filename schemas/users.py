from pydantic import BaseModel

from models.users import UserRole


class CreateUser(BaseModel):
    name: str
    username: str
    password: str
    address: str
    role: UserRole
    branch_id: int
    status: bool


class UpdateUser(BaseModel):
    id: int
    name: str
    username: str
    password: str
    address: str
    role: UserRole
    branch_id: int
    status: bool

