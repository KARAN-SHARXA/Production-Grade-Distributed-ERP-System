from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category import Category


class CategoryRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        category: Category,
    ) -> Category:
        db.add(category)
        await db.commit()
        await db.refresh(category)
        return category

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        category_id: UUID,
    ) -> Category | None:
        result = await db.execute(
            select(Category).where(Category.id == category_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_name(
        db: AsyncSession,
        name: str,
    ) -> Category | None:
        result = await db.execute(
            select(Category).where(Category.name == name)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_all(
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
    ) -> list[Category]:
        result = await db.execute(
            select(Category)
            .order_by(Category.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())

    @staticmethod
    async def update(
        db: AsyncSession,
        category: Category,
    ) -> Category:
        await db.commit()
        await db.refresh(category)
        return category

    @staticmethod
    async def delete(
        db: AsyncSession,
        category: Category,
    ) -> None:
        await db.delete(category)
        await db.commit()
