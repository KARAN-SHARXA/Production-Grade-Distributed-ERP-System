from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.stock_movement import (
    StockMovement,
    StockMovementType,
)
from app.repositories.product import ProductRepository
from app.repositories.stock import StockRepository
from app.repositories.stock_movement import StockMovementRepository
from app.repositories.warehouse import WarehouseRepository
from app.schemas.stock_movement import StockMovementCreate


class StockMovementService:

    @staticmethod
    async def create_movement(
        db: AsyncSession,
        data: StockMovementCreate,
    ) -> StockMovement:

        product = await ProductRepository.get_by_id(
            db,
            data.product_id,
        )

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found",
            )

        warehouse = await WarehouseRepository.get_by_id(
            db,
            data.warehouse_id,
        )

        if not warehouse:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Warehouse not found",
            )

        stock = await StockRepository.get_by_product_and_warehouse(
            db,
            data.product_id,
            data.warehouse_id,
        )

        if not stock:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Stock record not found for this product and warehouse",
            )

        if data.movement_type in (
            StockMovementType.PURCHASE,
            StockMovementType.RETURN,
        ):
            stock.quantity += data.quantity

        elif data.movement_type == StockMovementType.SALE:
            available_quantity = (
                stock.quantity - stock.reserved_quantity
            )

            if data.quantity > available_quantity:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Insufficient available stock",
                )

            stock.quantity -= data.quantity

        elif data.movement_type == StockMovementType.ADJUSTMENT:
            stock.quantity = data.quantity

        elif data.movement_type == StockMovementType.TRANSFER:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Transfer movement requires a dedicated transfer operation",
            )

        movement = StockMovement(
            product_id=data.product_id,
            warehouse_id=data.warehouse_id,
            movement_type=data.movement_type.value,
            quantity=data.quantity,
            reference_id=data.reference_id,
            notes=data.notes,
        )

        db.add(movement)

        await db.commit()
        await db.refresh(movement)

        return movement

    @staticmethod
    async def get_movement(
        db: AsyncSession,
        movement_id: UUID,
    ) -> StockMovement:

        movement = await StockMovementRepository.get_by_id(
            db,
            movement_id,
        )

        if not movement:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Stock movement not found",
            )

        return movement

    @staticmethod
    async def get_movements(
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
    ) -> list[StockMovement]:

        return await StockMovementRepository.get_all(
            db,
            skip,
            limit,
        )

    @staticmethod
    async def get_product_movements(
        db: AsyncSession,
        product_id: UUID,
        skip: int = 0,
        limit: int = 100,
    ) -> list[StockMovement]:

        product = await ProductRepository.get_by_id(
            db,
            product_id,
        )

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found",
            )

        return await StockMovementRepository.get_by_product(
            db,
            product_id,
            skip,
            limit,
        )

    @staticmethod
    async def get_warehouse_movements(
        db: AsyncSession,
        warehouse_id: UUID,
        skip: int = 0,
        limit: int = 100,
    ) -> list[StockMovement]:

        warehouse = await WarehouseRepository.get_by_id(
            db,
            warehouse_id,
        )

        if not warehouse:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Warehouse not found",
            )

        return await StockMovementRepository.get_by_warehouse(
            db,
            warehouse_id,
            skip,
            limit,
        )
