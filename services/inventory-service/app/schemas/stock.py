from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class StockBase(BaseModel):
    product_id: UUID
    warehouse_id: UUID
    quantity: int = Field(default=0, ge=0)
    reserved_quantity: int = Field(default=0, ge=0)


class StockCreate(StockBase):
    pass


class StockUpdate(BaseModel):
    quantity: int | None = Field(default=None, ge=0)
    reserved_quantity: int | None = Field(default=None, ge=0)


class StockResponse(StockBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    created_at: datetime
    updated_at: datetime
