from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.repositories.category import CategoryRepository
from app.repositories.product import ProductRepository
from app.schemas.product import ProductCreate, ProductUpdate


class ProductService:

    @staticmethod
    async def create_product(
        db: AsyncSession,
        data: ProductCreate,
    ) -> Product:

        category = await CategoryRepository.get_by_id(
            db,
            data.category_id,
        )

        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found",
            )

        existing = await ProductRepository.get_by_sku(
            db,
            data.sku,
        )

        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Product with this SKU already exists",
            )

        product = Product(
            sku=data.sku,
            name=data.name,
            description=data.description,
            category_id=data.category_id,
            unit_price=data.unit_price,
            cost_price=data.cost_price,
            reorder_level=data.reorder_level,
            is_active=data.is_active,
        )

        return await ProductRepository.create(
            db,
            product,
        )

    @staticmethod
    async def get_product(
        db: AsyncSession,
        product_id: UUID,
    ) -> Product:

        product = await ProductRepository.get_by_id(
            db,
            product_id,
        )

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found",
            )

        return product

    @staticmethod
    async def get_products(
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
    ) -> list[Product]:

        return await ProductRepository.get_all(
            db,
            skip,
            limit,
        )

    @staticmethod
    async def update_product(
        db: AsyncSession,
        product_id: UUID,
        data: ProductUpdate,
    ) -> Product:

        product = await ProductService.get_product(
            db,
            product_id,
        )

        update_data = data.model_dump(
            exclude_unset=True,
        )

        if "sku" in update_data:

            existing = await ProductRepository.get_by_sku(
                db,
                update_data["sku"],
            )

            if existing and existing.id != product_id:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Product with this SKU already exists",
                )

        if "category_id" in update_data:

            category = await CategoryRepository.get_by_id(
                db,
                update_data["category_id"],
            )

            if not category:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Category not found",
                )

        for field, value in update_data.items():
            setattr(product, field, value)

        return await ProductRepository.update(
            db,
            product,
        )

    @staticmethod
    async def delete_product(
        db: AsyncSession,
        product_id: UUID,
    ) -> None:

        product = await ProductService.get_product(
            db,
            product_id,
        )

        product.is_active = False

        await ProductRepository.update(
            db,
            product,
        )
