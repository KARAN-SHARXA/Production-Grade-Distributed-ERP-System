from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.core.database import get_db
from app.models.purchase import PurchaseOrder, PurchaseStatus
from app.schemas.purchase import (
    PurchaseCreate,
    PurchaseUpdate,
    PurchaseResponse,
)
from app.services.purchase_service import create_purchase_order

router = APIRouter(
    prefix="/purchases",
    tags=["Purchases"],
)


@router.post("/", response_model=PurchaseResponse, status_code=201)
async def create_purchase(
    data: PurchaseCreate,
    db: AsyncSession = Depends(get_db),
):
    return await create_purchase_order(db, data)


@router.get("/", response_model=list[PurchaseResponse])
async def get_purchases(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(PurchaseOrder).options(
            selectinload(PurchaseOrder.items)
        )
    )
    return result.scalars().all()


@router.get("/{purchase_id}", response_model=PurchaseResponse)
async def get_purchase(
    purchase_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(PurchaseOrder)
        .options(selectinload(PurchaseOrder.items))
        .where(PurchaseOrder.id == purchase_id)
    )

    purchase = result.scalar_one_or_none()

    if not purchase:
        raise HTTPException(404, "Purchase not found")

    return purchase


@router.put("/{purchase_id}", response_model=PurchaseResponse)
async def update_purchase(
    purchase_id: UUID,
    data: PurchaseUpdate,
    db: AsyncSession = Depends(get_db),
):
    purchase = await db.get(PurchaseOrder, purchase_id)

    if not purchase:
        raise HTTPException(404, "Purchase not found")

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(purchase, key, value)

    await db.commit()
    await db.refresh(purchase)

    result = await db.execute(
        select(PurchaseOrder)
        .options(selectinload(PurchaseOrder.items))
        .where(PurchaseOrder.id == purchase.id)
    )

    return result.scalar_one()


@router.delete("/{purchase_id}")
async def delete_purchase(
    purchase_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    purchase = await db.get(PurchaseOrder, purchase_id)

    if not purchase:
        raise HTTPException(404, "Purchase not found")

    await db.delete(purchase)
    await db.commit()

    return {"message": "Purchase deleted successfully"}