import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.security import require_permission, CurrentUser
from app.repositories.department_repository import DepartmentRepository
from app.services.department_service import DepartmentService
from app.schemas.department import DepartmentCreate, DepartmentUpdate, DepartmentOut
from app.schemas.common import APIResponse

router = APIRouter(prefix="/departments", tags=["Departments"])

def get_service(db: AsyncSession = Depends(get_db)) -> DepartmentService:
    return DepartmentService(DepartmentRepository(db))

@router.post("", response_model=APIResponse[DepartmentOut], status_code=201)
async def create_department(
    payload: DepartmentCreate,
    service: DepartmentService = Depends(get_service),
    _: CurrentUser = Depends(require_permission("department:create")),
):
    dept = await service.create(payload)
    return APIResponse(data=dept, message="Department created successfully")

@router.get("", response_model=APIResponse[list[DepartmentOut]])
async def list_departments(
    service: DepartmentService = Depends(get_service),
    _: CurrentUser = Depends(require_permission("department:read")),
):
    return APIResponse(data=await service.list_all())

@router.patch("/{dept_id}", response_model=APIResponse[DepartmentOut])
async def update_department(
    dept_id: uuid.UUID,
    payload: DepartmentUpdate,
    service: DepartmentService = Depends(get_service),
    _: CurrentUser = Depends(require_permission("department:update")),
):
    return APIResponse(data=await service.update(dept_id, payload), message="Updated successfully")

@router.delete("/{dept_id}", response_model=APIResponse)
async def delete_department(
    dept_id: uuid.UUID,
    service: DepartmentService = Depends(get_service),
    _: CurrentUser = Depends(require_permission("department:delete")),
):
    await service.delete(dept_id)
    return APIResponse(message="Department deleted successfully")