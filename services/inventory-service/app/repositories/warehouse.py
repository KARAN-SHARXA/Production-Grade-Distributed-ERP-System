from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.warehouse import Warehouse


class WarehouseRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        warehouse: Warehouse,
    ) -> Warehouse:
        db.add(warehouse)
        await db.commit()
        await db.refresh(warehouse)
        return warehouse

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        warehouse_id: UUID,
    ) -> Warehouse | None:
        result = await db.execute(
            select(Warehouse).where(Warehouse.id == warehouse_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_code(
        db: AsyncSession,
        code: str,
    ) -> Warehouse | None:
        result = await db.execute(
            select(Warehouse).where(Warehouse.code == code)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_name(
        db: AsyncSession,
        name: str,
    ) -> Warehouse | None:
        result = await db.execute(
            select(Warehouse).where(Warehouse.name == name)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_all(
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
    ) -> list[Warehouse]:
        result = await db.execute(
            select(Warehouse)
            .order_by(Warehouse.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())

    @staticmethod
    async def update(
        db: AsyncSession,
        warehouse: Warehouse,
    ) -> Warehouse:
        await db.commit()
        await db.refresh(warehouse)
        return warehouse

    @staticmethod
    async def delete(
        db: AsyncSession,
        warehouse: Warehouse,
    ) -> None:
        await db.delete(warehouse)
        await db.commit()
