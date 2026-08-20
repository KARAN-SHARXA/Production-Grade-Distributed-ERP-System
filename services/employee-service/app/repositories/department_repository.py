import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.department import Department
from app.schemas.department import DepartmentCreate, DepartmentUpdate

class DepartmentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: DepartmentCreate) -> Department:
        dept = Department(**data.model_dump())
        self.db.add(dept)
        await self.db.commit()
        await self.db.refresh(dept)
        return dept

    async def get_by_id(self, dept_id: uuid.UUID) -> Department | None:
        result = await self.db.execute(select(Department).where(Department.id == dept_id))
        return result.scalar_one_or_none()

    async def list_all(self) -> list[Department]:
        result = await self.db.execute(select(Department))
        return result.scalars().all()

    async def update(self, dept: Department, data: DepartmentUpdate) -> Department:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(dept, field, value)
        await self.db.commit()
        await self.db.refresh(dept)
        return dept

    async def delete(self, dept: Department) -> None:
        await self.db.delete(dept)
        await self.db.commit()