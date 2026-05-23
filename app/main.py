from fastapi import FastAPI

from app.routes.healthcare_routes import router
from app.core.config import settings
from app.core.exception_handler import (
    global_exception_handler
)
from app.core.middleware import (
    request_timing_middleware
)


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    description="AI-powered healthcare follow-up agent API"
)


@app.get("/")
async def root():
    return {
        "message": "CD Pipeline Successfully Working 🚀",
        "status": "healthy",
        "version": settings.API_VERSION
    }


app.include_router(router)


app.middleware("http")(
    request_timing_middleware
)


app.add_exception_handler(
    Exception,
    global_exception_handler
)