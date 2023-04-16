from pydantic import BaseModel


class CreateUser(BaseModel):
    name: str
    username: str
    password: str
    address: str
    role: str
    branch_id: int
    status: bool


class UpdateUser(BaseModel):
    id: int
    name: str
    username: str
    password: str
    address: str
    role: str
    branch_id: int
    status: bool

