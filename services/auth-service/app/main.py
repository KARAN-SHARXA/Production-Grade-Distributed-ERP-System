from fastapi import FastAPI
from sqlalchemy import text
from app.core.database import engine


app = FastAPI(
    title="ERP Authentication Service",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "message": "ERP Auth Service is running"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "auth-service"
    }


@app.get("/db-test")
async def database_test():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))

            return {
                "status": "success",
                "database": "connected",
                "result": result.scalar()
            }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }