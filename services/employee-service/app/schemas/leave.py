import uuid
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict
from app.models.leave import LeaveStatus

class LeaveCreate(BaseModel):
    employee_id: uuid.UUID
    start_date: date
    end_date: date
    reason: str

class LeaveReview(BaseModel):
    status: LeaveStatus  # APPROVED or REJECTED

class LeaveOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    employee_id: uuid.UUID
    start_date: date
    end_date: date
    reason: str
    status: LeaveStatus
    reviewed_by: uuid.UUID | None
    created_at: datetime