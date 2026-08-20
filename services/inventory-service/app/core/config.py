from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Inventory Service"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    HOST: str = "0.0.0.0"
    PORT: int = 8003

    DATABASE_URL: str

    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"

    REDIS_URL: str = "redis://localhost:6379/0"

    LOW_STOCK_THRESHOLD: int = 10

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()