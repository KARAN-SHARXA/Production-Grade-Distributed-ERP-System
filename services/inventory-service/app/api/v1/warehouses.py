from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.warehouse import (
    WarehouseCreate,
    WarehouseResponse,
    WarehouseUpdate,
)
from app.services.warehouse import WarehouseService


router = APIRouter(
    prefix="/warehouses",
    tags=["Warehouses"],
)


@router.post(
    "/",
    response_model=WarehouseResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_warehouse(
    data: WarehouseCreate,
    db: AsyncSession = Depends(get_db),
):
    return await WarehouseService.create_warehouse(db, data)


@router.get(
    "/",
    response_model=list[WarehouseResponse],
)
async def get_warehouses(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    return await WarehouseService.get_warehouses(
        db,
        skip,
        limit,
    )


@router.get(
    "/{warehouse_id}",
    response_model=WarehouseResponse,
)
async def get_warehouse(
    warehouse_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await WarehouseService.get_warehouse(
        db,
        warehouse_id,
    )


@router.put(
    "/{warehouse_id}",
    response_model=WarehouseResponse,
)
async def update_warehouse(
    warehouse_id: UUID,
    data: WarehouseUpdate,
    db: AsyncSession = Depends(get_db),
):
    return await WarehouseService.update_warehouse(
        db,
        warehouse_id,
        data,
    )


@router.delete(
    "/{warehouse_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_warehouse(
    warehouse_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    await WarehouseService.delete_warehouse(
        db,
        warehouse_id,
    )
