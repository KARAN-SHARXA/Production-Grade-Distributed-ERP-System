import uuid
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.security import require_permission, CurrentUser
from app.repositories.employee_repository import EmployeeRepository
from app.services.employee_service import EmployeeService
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeOut
from app.schemas.common import PaginatedResponse, APIResponse

router = APIRouter(prefix="/employees", tags=["Employees"])

def get_service(db: AsyncSession = Depends(get_db)) -> EmployeeService:
    return EmployeeService(EmployeeRepository(db))

@router.post("", response_model=APIResponse[EmployeeOut], status_code=201)
async def create_employee(
    payload: EmployeeCreate,
    service: EmployeeService = Depends(get_service),
    _: CurrentUser = Depends(require_permission("employee:create")),
):
    employee = await service.create_employee(payload)
    return APIResponse(data=employee, message="Employee created successfully")

@router.get("", response_model=PaginatedResponse[EmployeeOut])
async def list_employees(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    search: str | None = None,
    department_id: uuid.UUID | None = None,
    status_filter: str | None = None,
    sort_by: str = "created_at",
    sort_dir: str = "desc",
    service: EmployeeService = Depends(get_service),
    _: CurrentUser = Depends(require_permission("employee:read")),
):
    rows, total, total_pages = await service.list_employees(
        page, page_size, search, department_id, status_filter, sort_by, sort_dir
    )
    return PaginatedResponse(data=rows, total=total, page=page, page_size=page_size, total_pages=total_pages)

@router.get("/{employee_id}", response_model=APIResponse[EmployeeOut])
async def get_employee(
    employee_id: uuid.UUID,
    service: EmployeeService = Depends(get_service),
    _: CurrentUser = Depends(require_permission("employee:read")),
):
    employee = await service.get_employee(employee_id)
    return APIResponse(data=employee)

@router.patch("/{employee_id}", response_model=APIResponse[EmployeeOut])
async def update_employee(
    employee_id: uuid.UUID,
    payload: EmployeeUpdate,
    service: EmployeeService = Depends(get_service),
    _: CurrentUser = Depends(require_permission("employee:update")),
):
    employee = await service.update_employee(employee_id, payload)
    return APIResponse(data=employee, message="Employee updated successfully")

@router.delete("/{employee_id}", response_model=APIResponse)
async def delete_employee(
    employee_id: uuid.UUID,
    service: EmployeeService = Depends(get_service),
    _: CurrentUser = Depends(require_permission("employee:delete")),
):
    await service.delete_employee(employee_id)
    return APIResponse(message="Employee deleted successfully")