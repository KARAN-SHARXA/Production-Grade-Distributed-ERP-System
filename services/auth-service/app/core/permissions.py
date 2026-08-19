from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User


def require_permission(permission_name: str):

    def permission_checker(
        current_user: User = Depends(...),
        db: Session = Depends(get_db)
    ):
        if not current_user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User account is inactive"
            )

        permission = next(
            (
                permission
                for permission in current_user.role.permissions
                if permission.name == permission_name
            ),
            None
        )

        if not permission:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied"
            )

        return current_user

    return permission_checker