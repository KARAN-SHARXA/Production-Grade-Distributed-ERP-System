import uuid
from fastapi import HTTPException, status
from app.repositories.department_repository import DepartmentRepository
from app.schemas.department import DepartmentCreate, DepartmentUpdate

class DepartmentService:
    def __init__(self, repo: DepartmentRepository):
        self.repo = repo

    async def create(self, data: DepartmentCreate):
        return await self.repo.create(data)

    async def get(self, dept_id: uuid.UUID):
        dept = await self.repo.get_by_id(dept_id)
        if not dept:
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Department not found")
        return dept

    async def list_all(self):
        return await self.repo.list_all()

    async def update(self, dept_id: uuid.UUID, data: DepartmentUpdate):
        dept = await self.get(dept_id)
        return await self.repo.update(dept, data)

    async def delete(self, dept_id: uuid.UUID):
        dept = await self.get(dept_id)
        await self.repo.delete(dept)