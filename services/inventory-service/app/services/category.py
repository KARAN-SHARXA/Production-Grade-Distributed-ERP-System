from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category import Category
from app.repositories.category import CategoryRepository
from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate,
)


class CategoryService:

    @staticmethod
    async def create_category(
        db: AsyncSession,
        data: CategoryCreate,
    ) -> Category:
        existing = await CategoryRepository.get_by_name(
            db,
            data.name,
        )

        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Category with this name already exists",
            )

        category = Category(
            name=data.name,
            description=data.description,
            is_active=data.is_active,
        )

        return await CategoryRepository.create(
            db,
            category,
        )

    @staticmethod
    async def get_category(
        db: AsyncSession,
        category_id: UUID,
    ) -> Category:
        category = await CategoryRepository.get_by_id(
            db,
            category_id,
        )

        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found",
            )

        return category

    @staticmethod
    async def get_categories(
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
    ) -> list[Category]:
        return await CategoryRepository.get_all(
            db,
            skip,
            limit,
        )

    @staticmethod
    async def update_category(
        db: AsyncSession,
        category_id: UUID,
        data: CategoryUpdate,
    ) -> Category:
        category = await CategoryService.get_category(
            db,
            category_id,
        )

        update_data = data.model_dump(
            exclude_unset=True,
        )

        if "name" in update_data:
            existing = await CategoryRepository.get_by_name(
                db,
                update_data["name"],
            )

            if existing and existing.id != category_id:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Category with this name already exists",
                )

        for field, value in update_data.items():
            setattr(category, field, value)

        return await CategoryRepository.update(
            db,
            category,
        )

    @staticmethod
    async def delete_category(
        db: AsyncSession,
        category_id: UUID,
    ) -> None:
        category = await CategoryService.get_category(
            db,
            category_id,
        )

        category.is_active = False

        await CategoryRepository.update(
            db,
            category,
        )
