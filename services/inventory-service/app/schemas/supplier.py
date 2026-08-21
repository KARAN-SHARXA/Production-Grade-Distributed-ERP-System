from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class SupplierBase(BaseModel):
    name: str
    code: str
    email: str | None = None
    phone: str | None = None
    address: str | None = None
    contact_person: str | None = None
    is_active: bool = True


class SupplierCreate(SupplierBase):
    pass


class SupplierUpdate(BaseModel):
    name: str | None = None
    code: str | None = None
    email: str | None = None
    phone: str | None = None
    address: str | None = None
    contact_person: str | None = None
    is_active: bool | None = None


class SupplierResponse(SupplierBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    created_at: datetime
    updated_at: datetime