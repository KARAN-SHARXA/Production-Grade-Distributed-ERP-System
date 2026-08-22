from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.purchase import PurchaseOrder, PurchaseStatus

router = APIRouter(
    prefix="/purchases",
    tags=["Purchase Actions"],
)


@router.post("/{purchase_id}/approve")
async def approve_purchase(
    purchase_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    purchase = await db.get(PurchaseOrder, purchase_id)

    if not purchase:
        raise HTTPException(404, "Purchase not found")

    if purchase.status != PurchaseStatus.DRAFT.value:
        raise HTTPException(400, "Only draft purchase can be approved")

    purchase.status = PurchaseStatus.APPROVED.value

    await db.commit()

    return {"message": "Purchase approved successfully"}


@router.post("/{purchase_id}/receive")
async def receive_goods(
    purchase_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    purchase = await db.get(PurchaseOrder, purchase_id)

    if not purchase:
        raise HTTPException(404, "Purchase not found")

    if purchase.status != PurchaseStatus.APPROVED.value:
        raise HTTPException(
            400,
            "Purchase must be approved before receiving",
        )

    purchase.status = PurchaseStatus.RECEIVED.value

    await db.commit()

    return {
        "message": "Goods received successfully",
        "purchase_status": purchase.status,
    }