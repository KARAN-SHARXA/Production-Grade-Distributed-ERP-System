import uuid
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.security import get_current_user, CurrentUser
from app.repositories.attendance_repository import AttendanceRepository
from app.services.attendance_service import AttendanceService
from app.schemas.attendance import AttendanceOut
from app.schemas.common import APIResponse

router = APIRouter(prefix="/attendance", tags=["Attendance"])

def get_service(db: AsyncSession = Depends(get_db)) -> AttendanceService:
    return AttendanceService(AttendanceRepository(db))

@router.post("/check-in/{employee_id}", response_model=APIResponse[AttendanceOut])
async def check_in(
    employee_id: uuid.UUID,
    service: AttendanceService = Depends(get_service),
    _: CurrentUser = Depends(get_current_user),
):
    return APIResponse(data=await service.check_in(employee_id), message="Checked in")

@router.post("/check-out/{employee_id}", response_model=APIResponse[AttendanceOut])
async def check_out(
    employee_id: uuid.UUID,
    service: AttendanceService = Depends(get_service),
    _: CurrentUser = Depends(get_current_user),
):
    return APIResponse(data=await service.check_out(employee_id), message="Checked out")

@router.get("/{employee_id}", response_model=APIResponse[list[AttendanceOut]])
async def employee_attendance(
    employee_id: uuid.UUID,
    page: int = Query(1, ge=1),
    page_size: int = Query(30, ge=1, le=100),
    service: AttendanceService = Depends(get_service),
    _: CurrentUser = Depends(get_current_user),
):
    return APIResponse(data=await service.list_for_employee(employee_id, page, page_size))