import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class PurchaseStatus(str, Enum):
    DRAFT = "DRAFT"
    APPROVED = "APPROVED"
    RECEIVED = "RECEIVED"
    CANCELLED = "CANCELLED"


class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    supplier_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
        index=True,
    )

    employee_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
        index=True,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default=PurchaseStatus.DRAFT.value,
        nullable=False,
    )

    total_amount: Mapped[float] = mapped_column(
        Numeric(12, 2),
        default=0,
    )

    notes: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    items = relationship(
        "PurchaseItem",
        back_populates="purchase",
        cascade="all, delete-orphan",
    )