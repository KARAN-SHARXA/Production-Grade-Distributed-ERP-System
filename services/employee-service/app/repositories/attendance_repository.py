import uuid
from datetime import date
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.attendance import Attendance

class AttendanceRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_employee_and_date(self, employee_id: uuid.UUID, day: date) -> Attendance | None:
        result = await self.db.execute(
            select(Attendance).where(Attendance.employee_id == employee_id, Attendance.date == day)
        )
        return result.scalar_one_or_none()

    async def create(self, record: Attendance) -> Attendance:
        self.db.add(record)
        await self.db.commit()
        await self.db.refresh(record)
        return record

    async def update(self, record: Attendance) -> Attendance:
        await self.db.commit()
        await self.db.refresh(record)
        return record

    async def list_for_employee(self, employee_id: uuid.UUID, page: int, page_size: int):
        query = select(Attendance).where(Attendance.employee_id == employee_id) \
            .order_by(Attendance.date.desc()).offset((page - 1) * page_size).limit(page_size)
        result = await self.db.execute(query)
        return result.scalars().all()