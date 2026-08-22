import uuid

from sqlalchemy import ForeignKey, Integer, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class PurchaseItem(Base):
    __tablename__ = "purchase_items"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    purchase_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("purchase_orders.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    product_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
        index=True,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    unit_price: Mapped[float] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    line_total: Mapped[float] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    purchase = relationship(
        "PurchaseOrder",
        back_populates="items",
    )