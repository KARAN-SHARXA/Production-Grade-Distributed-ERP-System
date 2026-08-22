from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class PurchaseItemCreate(BaseModel):
    product_id: UUID
    quantity: int = Field(..., gt=0)
    unit_price: float = Field(..., gt=0)


class PurchaseItemResponse(PurchaseItemCreate):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    line_total: float