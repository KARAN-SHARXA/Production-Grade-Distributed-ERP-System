import uuid
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class DepartmentCreate(BaseModel):
    name: str
    description: str | None = None

class DepartmentUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    is_active: bool | None = None

class DepartmentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    name: str
    description: str | None
    is_active: bool
    created_at: datetime
    updated_at: datetime