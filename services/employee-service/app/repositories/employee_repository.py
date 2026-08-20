import uuid
from sqlalchemy import select, func, or_
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate

class EmployeeRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: EmployeeCreate) -> Employee:
        employee = Employee(**data.model_dump())
        self.db.add(employee)
        await self.db.commit()
        await self.db.refresh(employee)
        return employee

    async def get_by_id(self, employee_id: uuid.UUID) -> Employee | None:
        result = await self.db.execute(
            select(Employee).where(Employee.id == employee_id, Employee.is_deleted == False)  # noqa: E712
        )
        return result.scalar_one_or_none()

    async def list(
        self, page: int, page_size: int, search: str | None,
        department_id: uuid.UUID | None, status_filter: str | None, sort_by: str, sort_dir: str,
    ):
        query = select(Employee).where(Employee.is_deleted == False)  # noqa: E712
        count_query = select(func.count()).select_from(Employee).where(Employee.is_deleted == False)  # noqa: E712

        if search:
            like = f"%{search}%"
            cond = or_(Employee.full_name.ilike(like), Employee.email.ilike(like), Employee.employee_code.ilike(like))
            query = query.where(cond)
            count_query = count_query.where(cond)

        if department_id:
            query = query.where(Employee.department_id == department_id)
            count_query = count_query.where(Employee.department_id == department_id)

        if status_filter:
            query = query.where(Employee.employment_status == status_filter)
            count_query = count_query.where(Employee.employment_status == status_filter)

        sort_col = getattr(Employee, sort_by, Employee.created_at)
        query = query.order_by(sort_col.desc() if sort_dir == "desc" else sort_col.asc())
        query = query.offset((page - 1) * page_size).limit(page_size)

        total = (await self.db.execute(count_query)).scalar_one()
        rows = (await self.db.execute(query)).scalars().all()
        return rows, total

    async def update(self, employee: Employee, data: EmployeeUpdate) -> Employee:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(employee, field, value)
        await self.db.commit()
        await self.db.refresh(employee)
        return employee

    async def soft_delete(self, employee: Employee) -> None:
        employee.is_deleted = True
        await self.db.commit()