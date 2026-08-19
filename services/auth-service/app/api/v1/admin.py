
from fastapi import APIRouter, Depends

from app.api.permissions import require_permission
from app.models.user import User


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get(
    "/users",
    dependencies=[
        Depends(require_permission("user:read"))
    ]
)
def get_users():

    return {
        "message": "You have permission to read users"
    }


@router.post(
    "/users",
    dependencies=[
        Depends(require_permission("user:create"))
    ]
)
def create_user():

    return {
        "message": "You have permission to create users"
    }


@router.put(
    "/users",
    dependencies=[
        Depends(require_permission("user:update"))
    ]
)
def update_user():

    return {
        "message": "You have permission to update users"
    }


@router.delete(
    "/users",
    dependencies=[
        Depends(require_permission("user:delete"))
    ]
)
def delete_user():

    return {
        "message": "You have permission to delete users"
    }

