from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.supplier import Supplier
from app.schemas.supplier import (
    SupplierCreate,
    SupplierUpdate,
    SupplierResponse,
)

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])


@router.post("/", response_model=SupplierResponse, status_code=201)
async def create_supplier(
    data: SupplierCreate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Supplier).where(
            (Supplier.name == data.name) |
            (Supplier.code == data.code)
        )
    )

    existing = result.scalar_one_or_none()

    if existing:
        raise HTTPException(status_code=409, detail="Supplier already exists")

    supplier = Supplier(**data.model_dump())

    db.add(supplier)
    await db.commit()
    await db.refresh(supplier)

    return supplier


@router.get("/", response_model=list[SupplierResponse])
async def get_suppliers(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Supplier))
    return result.scalars().all()


@router.get("/{supplier_id}", response_model=SupplierResponse)
async def get_supplier(
    supplier_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    supplier = await db.get(Supplier, supplier_id)

    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")

    return supplier


@router.put("/{supplier_id}", response_model=SupplierResponse)
async def update_supplier(
    supplier_id: UUID,
    data: SupplierUpdate,
    db: AsyncSession = Depends(get_db),
):
    supplier = await db.get(Supplier, supplier_id)

    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(supplier, key, value)

    await db.commit()
    await db.refresh(supplier)

    return supplier


@router.delete("/{supplier_id}")
async def delete_supplier(
    supplier_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    supplier = await db.get(Supplier, supplier_id)

    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")

    await db.delete(supplier)
    await db.commit()

    return {"message": "Supplier deleted successfully"}