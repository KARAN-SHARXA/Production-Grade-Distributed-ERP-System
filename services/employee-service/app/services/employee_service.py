import uuid
from fastapi import HTTPException, status
from app.repositories.employee_repository import EmployeeRepository
from app.schemas.employee import EmployeeCreate, EmployeeUpdate

class EmployeeService:
    def __init__(self, repo: EmployeeRepository):
        self.repo = repo

    async def create_employee(self, data: EmployeeCreate):
        return await self.repo.create(data)

    async def get_employee(self, employee_id: uuid.UUID):
        employee = await self.repo.get_by_id(employee_id)
        if not employee:
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Employee not found")
        return employee

    async def list_employees(self, page, page_size, search, department_id, status_filter, sort_by, sort_dir):
        rows, total = await self.repo.list(page, page_size, search, department_id, status_filter, sort_by, sort_dir)
        total_pages = (total + page_size - 1) // page_size if page_size else 1
        return rows, total, total_pages

    async def update_employee(self, employee_id: uuid.UUID, data: EmployeeUpdate):
        employee = await self.get_employee(employee_id)
        return await self.repo.update(employee, data)

    async def delete_employee(self, employee_id: uuid.UUID):
        employee = await self.get_employee(employee_id)
        await self.repo.soft_delete(employee)