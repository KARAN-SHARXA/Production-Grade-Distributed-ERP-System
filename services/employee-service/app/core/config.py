from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SERVICE_NAME: str = "employee-service"
    DATABASE_URL: str  # postgresql+asyncpg://user:pass@host:5432/employee_db
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()