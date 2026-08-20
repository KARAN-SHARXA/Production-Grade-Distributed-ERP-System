import uuid
from datetime import datetime, timezone
from fastapi import HTTPException, status
from app.repositories.attendance_repository import AttendanceRepository
from app.models.attendance import Attendance, AttendanceStatus

class AttendanceService:
    def __init__(self, repo: AttendanceRepository):
        self.repo = repo

    async def check_in(self, employee_id: uuid.UUID):
        today = datetime.now(timezone.utc).date()
        existing = await self.repo.get_by_employee_and_date(employee_id, today)
        if existing:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, "Already checked in today")
        record = Attendance(employee_id=employee_id, date=today,
                             check_in=datetime.now(timezone.utc), status=AttendanceStatus.PRESENT)
        return await self.repo.create(record)

    async def check_out(self, employee_id: uuid.UUID):
        today = datetime.now(timezone.utc).date()
        record = await self.repo.get_by_employee_and_date(employee_id, today)
        if not record:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, "No check-in found for today")
        record.check_out = datetime.now(timezone.utc)
        return await self.repo.update(record)

    async def list_for_employee(self, employee_id: uuid.UUID, page: int, page_size: int):
        return await self.repo.list_for_employee(employee_id, page, page_size)