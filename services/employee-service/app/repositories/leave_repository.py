import uuid
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.leave import Leave

class LeaveRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, leave: Leave) -> Leave:
        self.db.add(leave)
        await self.db.commit()
        await self.db.refresh(leave)
        return leave

    async def get_by_id(self, leave_id: uuid.UUID) -> Leave | None:
        result = await self.db.execute(select(Leave).where(Leave.id == leave_id))
        return result.scalar_one_or_none()

    async def list(self, page: int, page_size: int, employee_id: uuid.UUID | None, status_filter: str | None):
        query = select(Leave)
        count_query = select(func.count()).select_from(Leave)
        if employee_id:
            query = query.where(Leave.employee_id == employee_id)
            count_query = count_query.where(Leave.employee_id == employee_id)
        if status_filter:
            query = query.where(Leave.status == status_filter)
            count_query = count_query.where(Leave.status == status_filter)
        query = query.order_by(Leave.created_at.desc()).offset((page - 1) * page_size).limit(page_size)

        total = (await self.db.execute(count_query)).scalar_one()
        rows = (await self.db.execute(query)).scalars().all()
        return rows, total

    async def update(self, leave: Leave) -> Leave:
        await self.db.commit()
        await self.db.refresh(leave)
        return leave