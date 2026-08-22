from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.schemas.purchase_item import PurchaseItemCreate, PurchaseItemResponse


class PurchaseCreate(BaseModel):
    supplier_id: UUID
    employee_id: UUID
    notes: str | None = None
    items: list[PurchaseItemCreate]


class PurchaseUpdate(BaseModel):
    notes: str | None = None
    status: str | None = None


class PurchaseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    supplier_id: UUID
    employee_id: UUID
    status: str
    total_amount: float
    notes: str | None
    created_at: datetime
    updated_at: datetime
    items: list[PurchaseItemResponse]