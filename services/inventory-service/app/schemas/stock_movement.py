from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class StockMovementType(str, Enum):
    PURCHASE = "PURCHASE"
    SALE = "SALE"
    RETURN = "RETURN"
    ADJUSTMENT = "ADJUSTMENT"
    TRANSFER = "TRANSFER"


class StockMovementBase(BaseModel):
    product_id: UUID
    warehouse_id: UUID
    movement_type: StockMovementType
    quantity: int = Field(..., gt=0)
    reference_id: str | None = Field(default=None, max_length=100)
    notes: str | None = None


class StockMovementCreate(StockMovementBase):
    pass


class StockMovementResponse(StockMovementBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    created_at: datetime
