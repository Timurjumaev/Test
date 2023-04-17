from typing import Optional

from pydantic import BaseModel


class CreateTariff(BaseModel):
    name: str
    cost: float
    comment: Optional[str] = None


class UpdateTariff(BaseModel):
    id: int
    name: str
    cost: float
    comment: Optional[str] = None
