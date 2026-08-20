from fastapi import APIRouter
from app.api.v1 import employees, departments, attendance, leaves

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(employees.router)
api_router.include_router(departments.router)
api_router.include_router(attendance.router)
api_router.include_router(leaves.router)