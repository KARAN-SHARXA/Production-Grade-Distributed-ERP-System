from fastapi import FastAPI

app = FastAPI(
    title="ERP Authentication Service",
    version="1.0.0"
)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "auth-service"
    }


@app.get("/")
async def root():
    return {
        "message": "ERP Auth Service is running"
    }
