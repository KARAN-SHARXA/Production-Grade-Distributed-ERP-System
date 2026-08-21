from uuid import UUID
from pydantic import BaseModel

class StockAdjustmentRequest(BaseModel):
    stock_id: UUID
    quantity: int
    reason: str