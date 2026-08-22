from fastapi import FastAPI

from app.core.config import settings
from app.api.v1 import purchase_router, purchase_action_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Purchase Management Service for Distributed ERP",
)

app.include_router(
    purchase_router,
    prefix="/api/v1",
)

app.include_router(
    purchase_action_router,
    prefix="/api/v1",
)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }