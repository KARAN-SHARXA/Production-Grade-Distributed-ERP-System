from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.stock import Stock
from app.repositories.product import ProductRepository
from app.repositories.stock import StockRepository
from app.repositories.warehouse import WarehouseRepository
from app.schemas.stock import StockCreate, StockUpdate


class StockService:

    @staticmethod
    async def create_stock(
        db: AsyncSession,
        data: StockCreate,
    ) -> Stock:

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

        existing = await StockRepository.get_by_product_and_warehouse(
            db,
            data.product_id,
            data.warehouse_id,
        )

        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Stock already exists for this product and warehouse",
            )

        stock = Stock(
            product_id=data.product_id,
            warehouse_id=data.warehouse_id,
            quantity=data.quantity,
            reserved_quantity=data.reserved_quantity,
        )

        return await StockRepository.create(
            db,
            stock,
        )

    @staticmethod
    async def get_stock(
        db: AsyncSession,
        stock_id: UUID,
    ) -> Stock:

        stock = await StockRepository.get_by_id(
            db,
            stock_id,
        )

        if not stock:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Stock not found",
            )

        return stock

    @staticmethod
    async def get_stock_by_product_and_warehouse(
        db: AsyncSession,
        product_id: UUID,
        warehouse_id: UUID,
    ) -> Stock:

        stock = await StockRepository.get_by_product_and_warehouse(
            db,
            product_id,
            warehouse_id,
        )

        if not stock:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Stock not found",
            )

        return stock

    @staticmethod
    async def get_stocks(
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
    ) -> list[Stock]:

        return await StockRepository.get_all(
            db,
            skip,
            limit,
        )

    @staticmethod
    async def get_product_stocks(
        db: AsyncSession,
        product_id: UUID,
    ) -> list[Stock]:

        product = await ProductRepository.get_by_id(
            db,
            product_id,
        )

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found",
            )

        return await StockRepository.get_by_product(
            db,
            product_id,
        )

    @staticmethod
    async def get_warehouse_stocks(
        db: AsyncSession,
        warehouse_id: UUID,
    ) -> list[Stock]:

        warehouse = await WarehouseRepository.get_by_id(
            db,
            warehouse_id,
        )

        if not warehouse:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Warehouse not found",
            )

        return await StockRepository.get_by_warehouse(
            db,
            warehouse_id,
        )

    @staticmethod
    async def update_stock(
        db: AsyncSession,
        stock_id: UUID,
        data: StockUpdate,
    ) -> Stock:

        stock = await StockService.get_stock(
            db,
            stock_id,
        )

        update_data = data.model_dump(
            exclude_unset=True,
        )

        if (
            "reserved_quantity" in update_data
            and update_data["reserved_quantity"] > stock.quantity
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Reserved quantity cannot exceed available quantity",
            )

        for field, value in update_data.items():
            setattr(stock, field, value)

        return await StockRepository.update(
            db,
            stock,
        )

    @staticmethod
    async def increase_stock(
        db: AsyncSession,
        product_id: UUID,
        warehouse_id: UUID,
        quantity: int,
    ) -> Stock:

        if quantity <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Quantity must be greater than zero",
            )

        stock = await StockService.get_stock_by_product_and_warehouse(
            db,
            product_id,
            warehouse_id,
        )

        stock.quantity += quantity

        return await StockRepository.update(
            db,
            stock,
        )

    @staticmethod
    async def decrease_stock(
        db: AsyncSession,
        product_id: UUID,
        warehouse_id: UUID,
        quantity: int,
    ) -> Stock:

        if quantity <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Quantity must be greater than zero",
            )

        stock = await StockService.get_stock_by_product_and_warehouse(
            db,
            product_id,
            warehouse_id,
        )

        available_quantity = (
            stock.quantity - stock.reserved_quantity
        )

        if quantity > available_quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Insufficient available stock",
            )

        stock.quantity -= quantity

        return await StockRepository.update(
            db,
            stock,
        )
