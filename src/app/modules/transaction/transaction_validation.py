
from datetime import datetime

from pydantic import BaseModel, Field


class CreateTransaction(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    amount: float = Field(..., gt=0)
    type: str = Field(..., enum=["income", "expense"])
    category: str = Field(..., min_length=2, max_length=100)