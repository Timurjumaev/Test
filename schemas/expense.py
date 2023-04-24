from typing import Optional

from pydantic import BaseModel

from models.expenses import ExpenseType
from models.incomes import IncomeType


class CreateExpense(BaseModel):
    amount: float
    type: ExpenseType
    comment: Optional[str] = None
    destination_id: int
    for_id: int


class UpdateExpense(BaseModel):
    id: int
    amount: float
    type: IncomeType
    comment: Optional[str] = None
