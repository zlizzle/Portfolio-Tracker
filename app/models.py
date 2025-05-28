from sqlmodel import SQLModel, Field
from typing import Optional

class Asset(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    symbol: str
    quantity: float
    average_price: float