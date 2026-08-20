from typing import Generic, TypeVar, List
from pydantic import BaseModel

T = TypeVar("T")

class PaginatedResponse(BaseModel, Generic[T]):
    success: bool = True
    data: List[T]
    total: int
    page: int
    page_size: int
    total_pages: int

class APIResponse(BaseModel, Generic[T]):
    success: bool = True
    data: T | None = None
    message: str = ""