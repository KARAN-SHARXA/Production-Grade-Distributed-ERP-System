import uuid
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.security import require_permission, get_current_user, CurrentUser
from app.repositories.leave_repository import LeaveRepository
from app.services.leave_service import LeaveService
from app.schemas.leave import LeaveCreate, LeaveReview, LeaveOut
from app.schemas.common import PaginatedResponse, APIResponse

router = APIRouter(prefix="/leaves", tags=["Leaves"])

def get_service(db: AsyncSession = Depends(get_db)) -> LeaveService:
    return LeaveService(LeaveRepository(db))

@router.post("", response_model=APIResponse[LeaveOut], status_code=201)
async def apply_leave(
    payload: LeaveCreate,
    service: LeaveService = Depends(get_service),
    _: CurrentUser = Depends(get_current_user),
):
    return APIResponse(data=await service.apply(payload), message="Leave request submitted")

@router.get("", response_model=PaginatedResponse[LeaveOut])
async def list_leaves(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    employee_id: uuid.UUID | None = None,
    status_filter: str | None = None,
    service: LeaveService = Depends(get_service),
    _: CurrentUser = Depends(require_permission("leave:read")),
):
    rows, total, total_pages = await service.list(page, page_size, employee_id, status_filter)
    return PaginatedResponse(data=rows, total=total, page=page, page_size=page_size, total_pages=total_pages)

@router.patch("/{leave_id}/review", response_model=APIResponse[LeaveOut])
async def review_leave(
    leave_id: uuid.UUID,
    payload: LeaveReview,
    service: LeaveService = Depends(get_service),
    user: CurrentUser = Depends(require_permission("leave:approve")),
):
    leave = await service.review(leave_id, payload.status, uuid.UUID(user.id))
    return APIResponse(data=leave, message=f"Leave {payload.status.value.lower()}")