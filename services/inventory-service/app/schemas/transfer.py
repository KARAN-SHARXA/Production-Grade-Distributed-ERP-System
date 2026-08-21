from uuid import UUID

from pydantic import BaseModel, Field


class StockTransferRequest(BaseModel):
    product_id: UUID
    from_warehouse: UUID
    to_warehouse: UUID
    quantity: int = Field(..., gt=0)
    reason: str = Field(..., min_length=3, max_length=255)