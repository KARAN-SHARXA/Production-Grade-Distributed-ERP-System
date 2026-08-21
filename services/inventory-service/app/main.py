from fastapi import FastAPI

from app.core.config import settings

from app.api.v1.categories import router as category_router
from app.api.v1.products import router as product_router
from app.api.v1.warehouses import router as warehouse_router
from app.api.v1.stocks import router as stock_router
from app.api.v1.stock_movements import router as stock_movement_router
from app.api.v1.supplier import router as supplier_router
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Inventory Management Service for Distributed ERP",
)

app.include_router(category_router, prefix="/api/v1")
app.include_router(product_router, prefix="/api/v1")
app.include_router(warehouse_router, prefix="/api/v1")
app.include_router(stock_router, prefix="/api/v1")
app.include_router(stock_movement_router, prefix="/api/v1")
app.include_router(supplier_router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }