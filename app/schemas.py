from pydantic import BaseModel

class AssetCreate(BaseModel):
    symbol: str
    quantity: float
    average_price: float

class AssetRead(AssetCreate):
    id: int