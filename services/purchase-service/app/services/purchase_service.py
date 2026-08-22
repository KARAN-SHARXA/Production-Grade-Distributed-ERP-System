from sqlalchemy.ext.asyncio import AsyncSession

from app.models.purchase import PurchaseOrder
from app.models.purchase_item import PurchaseItem
from app.schemas.purchase import PurchaseCreate


async def create_purchase_order(db: AsyncSession, data: PurchaseCreate):
    total = 0

    purchase = PurchaseOrder(
        supplier_id=data.supplier_id,
        employee_id=data.employee_id,
        notes=data.notes,
    )

    db.add(purchase)
    await db.flush()

    for item in data.items:
        line_total = item.quantity * item.unit_price
        total += line_total

        purchase_item = PurchaseItem(
            purchase_id=purchase.id,
            product_id=item.product_id,
            quantity=item.quantity,
            unit_price=item.unit_price,
            line_total=line_total,
        )

        db.add(purchase_item)

    purchase.total_amount = total

    await db.commit()
    await db.refresh(purchase)

    return purchase