import uuid
from fastapi import HTTPException, status
from app.repositories.leave_repository import LeaveRepository
from app.models.leave import Leave, LeaveStatus
from app.schemas.leave import LeaveCreate

class LeaveService:
    def __init__(self, repo: LeaveRepository):
        self.repo = repo

    async def apply(self, data: LeaveCreate):
        if data.end_date < data.start_date:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, "end_date cannot be before start_date")
        leave = Leave(**data.model_dump())
        return await self.repo.create(leave)

    async def get(self, leave_id: uuid.UUID):
        leave = await self.repo.get_by_id(leave_id)
        if not leave:
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Leave request not found")
        return leave

    async def list(self, page, page_size, employee_id, status_filter):
        rows, total = await self.repo.list(page, page_size, employee_id, status_filter)
        total_pages = (total + page_size - 1) // page_size if page_size else 1
        return rows, total, total_pages

    async def review(self, leave_id: uuid.UUID, new_status: LeaveStatus, reviewer_id: uuid.UUID):
        leave = await self.get(leave_id)
        if leave.status != LeaveStatus.PENDING:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, "Leave already reviewed")
        leave.status = new_status
        leave.reviewed_by = reviewer_id
        return await self.repo.update(leave)
        # TODO Phase 12: publish LeaveApproved/LeaveRejected event -> notification-service