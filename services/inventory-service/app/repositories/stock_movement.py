from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.stock_movement import StockMovement


class StockMovementRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        movement: StockMovement,
    ) -> StockMovement:
        db.add(movement)
        await db.commit()
        await db.refresh(movement)
        return movement

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        movement_id: UUID,
    ) -> StockMovement | None:
        result = await db.execute(
            select(StockMovement).where(
                StockMovement.id == movement_id
            )
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_product(
        db: AsyncSession,
        product_id: UUID,
        skip: int = 0,
        limit: int = 100,
    ) -> list[StockMovement]:
        result = await db.execute(
            select(StockMovement)
            .where(StockMovement.product_id == product_id)
            .order_by(StockMovement.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())

    @staticmethod
    async def get_by_warehouse(
        db: AsyncSession,
        warehouse_id: UUID,
        skip: int = 0,
        limit: int = 100,
    ) -> list[StockMovement]:
        result = await db.execute(
            select(StockMovement)
            .where(StockMovement.warehouse_id == warehouse_id)
            .order_by(StockMovement.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())

    @staticmethod
    async def get_all(
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
    ) -> list[StockMovement]:
        result = await db.execute(
            select(StockMovement)
            .order_by(StockMovement.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())
