from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from app.core.config import settings

bearer_scheme = HTTPBearer()

class CurrentUser:
    def __init__(self, id: str, email: str, role: str, permissions: list[str]):
        self.id = id
        self.email = email
        self.role = role
        self.permissions = permissions

def get_current_user(creds: HTTPAuthorizationCredentials = Depends(bearer_scheme)) -> CurrentUser:
    try:
        payload = jwt.decode(creds.credentials, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
    except JWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid or expired token")
    return CurrentUser(
        id=payload.get("sub"),
        email=payload.get("email"),
        role=payload.get("role"),
        permissions=payload.get("permissions", []),
    )

def require_permission(permission: str):
    def checker(user: CurrentUser = Depends(get_current_user)) -> CurrentUser:
        if permission not in user.permissions and user.role != "SUPER_ADMIN":
            raise HTTPException(status.HTTP_403_FORBIDDEN, f"Missing permission: {permission}")
        return user
    return checker