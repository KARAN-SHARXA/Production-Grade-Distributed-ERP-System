from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.api.v1.router import api_router
from app.core.config import settings

app = FastAPI(title="Employee Service", version="1.0.0")

app.include_router(api_router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(status_code=422, content={"success": False, "message": "Validation error", "errors": exc.errors()})

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": settings.SERVICE_NAME}

@app.get("/ready")
def ready_check():
    return {"status": "ready"}