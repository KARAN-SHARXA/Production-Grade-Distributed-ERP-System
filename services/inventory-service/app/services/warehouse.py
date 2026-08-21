from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.warehouse import Warehouse
from app.repositories.warehouse import WarehouseRepository
from app.schemas.warehouse import (
    WarehouseCreate,
    WarehouseUpdate,
)


class WarehouseService:

    @staticmethod
    async def create_warehouse(
        db: AsyncSession,
        data: WarehouseCreate,
    ) -> Warehouse:

        existing_code = await WarehouseRepository.get_by_code(
            db,
            data.code,
        )

        if existing_code:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Warehouse with this code already exists",
            )

        existing_name = await WarehouseRepository.get_by_name(
            db,
            data.name,
        )

        if existing_name:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Warehouse with this name already exists",
            )

        warehouse = Warehouse(
            name=data.name,
            code=data.code,
            address=data.address,
            manager_name=data.manager_name,
            is_active=data.is_active,
        )

        return await WarehouseRepository.create(
            db,
            warehouse,
        )

    @staticmethod
    async def get_warehouse(
        db: AsyncSession,
        warehouse_id: UUID,
    ) -> Warehouse:

        warehouse = await WarehouseRepository.get_by_id(
            db,
            warehouse_id,
        )

        if not warehouse:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Warehouse not found",
            )

        return warehouse

    @staticmethod
    async def get_warehouses(
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
    ) -> list[Warehouse]:

        return await WarehouseRepository.get_all(
            db,
            skip,
            limit,
        )

    @staticmethod
    async def update_warehouse(
        db: AsyncSession,
        warehouse_id: UUID,
        data: WarehouseUpdate,
    ) -> Warehouse:

        warehouse = await WarehouseService.get_warehouse(
            db,
            warehouse_id,
        )

        update_data = data.model_dump(
            exclude_unset=True,
        )

        if "code" in update_data:

            existing = await WarehouseRepository.get_by_code(
                db,
                update_data["code"],
            )

            if existing and existing.id != warehouse_id:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Warehouse with this code already exists",
                )

        if "name" in update_data:

            existing = await WarehouseRepository.get_by_name(
                db,
                update_data["name"],
            )

            if existing and existing.id != warehouse_id:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Warehouse with this name already exists",
                )

        for field, value in update_data.items():
            setattr(warehouse, field, value)

        return await WarehouseRepository.update(
            db,
            warehouse,
        )

    @staticmethod
    async def delete_warehouse(
        db: AsyncSession,
        warehouse_id: UUID,
    ) -> None:

        warehouse = await WarehouseService.get_warehouse(
            db,
            warehouse_id,
        )

        warehouse.is_active = False

        await WarehouseRepository.update(
            db,
            warehouse,
        )
