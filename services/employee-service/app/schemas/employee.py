import uuid
from datetime import date, datetime
from pydantic import BaseModel, EmailStr, ConfigDict
from app.models.employee import EmploymentStatus

class EmployeeCreate(BaseModel):
    employee_code: str
    full_name: str
    email: EmailStr
    phone: str | None = None
    designation: str
    department_id: uuid.UUID | None = None
    joining_date: date
    salary: float
    employment_status: EmploymentStatus = EmploymentStatus.ACTIVE

class EmployeeUpdate(BaseModel):
    full_name: str | None = None
    phone: str | None = None
    designation: str | None = None
    department_id: uuid.UUID | None = None
    salary: float | None = None
    employment_status: EmploymentStatus | None = None

class EmployeeOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    employee_code: str
    full_name: str
    email: str
    phone: str | None
    designation: str
    department_id: uuid.UUID | None
    joining_date: date
    salary: float
    employment_status: EmploymentStatus
    created_at: datetime
    updated_at: datetime