from pydantic import BaseModel


class CreatePhone(BaseModel):
    phone: str
    comment: str
    source: str
    source_id: int


class UpdatePhone(BaseModel):
    id: int
    phone: str
    comment: str
    source: str
    source_id: int