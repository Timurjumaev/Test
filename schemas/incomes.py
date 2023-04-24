from typing import Optional

from pydantic import BaseModel

from models.incomes import IncomeType


class CreateIncome(BaseModel):
    amount: float
    type: IncomeType
    comment: Optional[str] = None
    source_id: int
    for_id: int


class UpdateIncome(BaseModel):
    id: int
    amount: float
    type: IncomeType
    comment: Optional[str] = None
