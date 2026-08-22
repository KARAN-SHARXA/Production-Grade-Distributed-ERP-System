from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str

    JWT_SECRET: str
    JWT_ALGORITHM: str

    REDIS_URL: str

    APP_NAME: str = "Purchase Service"
    APP_VERSION: str = "1.0.0"

    ENVIRONMENT: str = "development"

    HOST: str = "0.0.0.0"
    PORT: int = 8004

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()