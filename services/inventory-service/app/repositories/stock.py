from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.stock import Stock


class StockRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        stock: Stock,
    ) -> Stock:
        db.add(stock)
        await db.commit()
        await db.refresh(stock)
        return stock

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        stock_id: UUID,
    ) -> Stock | None:
        result = await db.execute(
            select(Stock).where(Stock.id == stock_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_product_and_warehouse(
        db: AsyncSession,
        product_id: UUID,
        warehouse_id: UUID,
    ) -> Stock | None:
        result = await db.execute(
            select(Stock).where(
                Stock.product_id == product_id,
                Stock.warehouse_id == warehouse_id,
            )
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_product(
        db: AsyncSession,
        product_id: UUID,
    ) -> list[Stock]:
        result = await db.execute(
            select(Stock)
            .where(Stock.product_id == product_id)
            .order_by(Stock.created_at.desc())
        )
        return list(result.scalars().all())

    @staticmethod
    async def get_by_warehouse(
        db: AsyncSession,
        warehouse_id: UUID,
    ) -> list[Stock]:
        result = await db.execute(
            select(Stock)
            .where(Stock.warehouse_id == warehouse_id)
            .order_by(Stock.created_at.desc())
        )
        return list(result.scalars().all())

    @staticmethod
    async def get_all(
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
    ) -> list[Stock]:
        result = await db.execute(
            select(Stock)
            .order_by(Stock.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())

    @staticmethod
    async def update(
        db: AsyncSession,
        stock: Stock,
    ) -> Stock:
        await db.commit()
        await db.refresh(stock)
        return stock

    @staticmethod
    async def delete(
        db: AsyncSession,
        stock: Stock,
    ) -> None:
        await db.delete(stock)
        await db.commit()
