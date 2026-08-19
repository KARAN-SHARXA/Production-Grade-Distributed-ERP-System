from datetime import datetime, timedelta, timezone

import jwt
from pydantic_settings import BaseSettings

from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)

class JWTSettings(BaseSettings):
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        extra = "ignore"

jwt_settings = JWTSettings()


def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=jwt_settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        jwt_settings.JWT_SECRET_KEY,
        algorithm=jwt_settings.JWT_ALGORITHM,
    )


def decode_access_token(token: str) -> dict:
    return jwt.decode(
        token,
        jwt_settings.JWT_SECRET_KEY,
        algorithms=[jwt_settings.JWT_ALGORITHM],
    )