from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.stock_movement import (
    StockMovementCreate,
    StockMovementResponse,
)
from app.services.stock_movement import StockMovementService


router = APIRouter(
    prefix="/stock-movements",
    tags=["Stock Movements"],
)


@router.post(
    "/",
    response_model=StockMovementResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_stock_movement(
    data: StockMovementCreate,
    db: AsyncSession = Depends(get_db),
):
    return await StockMovementService.create_movement(
        db,
        data,
    )


@router.get(
    "/",
    response_model=list[StockMovementResponse],
)
async def get_stock_movements(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    return await StockMovementService.get_movements(
        db,
        skip,
        limit,
    )


@router.get(
    "/{movement_id}",
    response_model=StockMovementResponse,
)
async def get_stock_movement(
    movement_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await StockMovementService.get_movement(
        db,
        movement_id,
    )


@router.get(
    "/product/{product_id}",
    response_model=list[StockMovementResponse],
)
async def get_product_movements(
    product_id: UUID,
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    return await StockMovementService.get_product_movements(
        db,
        product_id,
        skip,
        limit,
    )


@router.get(
    "/warehouse/{warehouse_id}",
    response_model=list[StockMovementResponse],
)
async def get_warehouse_movements(
    warehouse_id: UUID,
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    return await StockMovementService.get_warehouse_movements(
        db,
        warehouse_id,
        skip,
        limit,
    )
