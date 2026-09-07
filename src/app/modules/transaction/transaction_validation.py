from pydantic import BaseModel, Field

from typing import Optional, Literal


class CreateTransaction(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    amount: float = Field(..., gt=0)
    type: Literal["income", "expense"] = Field(..., description="The type of the transaction")
    category: str = Field(..., min_length=2, max_length=100)
    
class UpdateTransaction(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=100)
    amount: Optional[float] = Field(default=None, gt=0)
    type: Optional[Literal["income", "expense"]] = None
    category: Optional[str] = Field(default=None, min_length=2, max_length=100)
    
    