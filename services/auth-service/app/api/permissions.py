
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.core.database import get_db
from app.models.user import User


def require_permission(permission_name: str):

    def permission_checker(
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
    ):
        # User ka role check karo
        if not current_user.role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User has no role assigned"
            )

        # Role ki permissions check karo
        permissions = current_user.role.permissions

        # Required permission available hai ya nahi
        has_permission = any(
            permission.name == permission_name
            for permission in permissions
        )

        if not has_permission:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permission required: {permission_name}"
            )

        return current_user

    return permission_checker

