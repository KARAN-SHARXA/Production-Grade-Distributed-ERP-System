import uuid
from datetime import date, datetime
from enum import Enum as PyEnum
from sqlalchemy import String, Date, DateTime, ForeignKey, Enum, Numeric, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class EmploymentStatus(str, PyEnum):
    ACTIVE = "ACTIVE"
    ON_LEAVE = "ON_LEAVE"
    SUSPENDED = "SUSPENDED"
    TERMINATED = "TERMINATED"

class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID | None] = mapped_column(nullable=True)  # links to auth-service user
    employee_code: Mapped[str] = mapped_column(String(30), unique=True, index=True)

    full_name: Mapped[str] = mapped_column(String(150), index=True)
    email: Mapped[str] = mapped_column(String(150), unique=True, index=True)
    phone: Mapped[str | None] = mapped_column(String(20), nullable=True)

    designation: Mapped[str] = mapped_column(String(100))
    department_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("departments.id"), nullable=True)

    joining_date: Mapped[date] = mapped_column(Date)
    salary: Mapped[float] = mapped_column(Numeric(12, 2))
    employment_status: Mapped[EmploymentStatus] = mapped_column(
        Enum(EmploymentStatus), default=EmploymentStatus.ACTIVE
    )

    is_deleted: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    department: Mapped["Department"] = relationship(back_populates="employees")