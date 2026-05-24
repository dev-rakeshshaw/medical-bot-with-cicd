from fastapi import FastAPI
from fastapi import Response

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
        "message": "GitHub Actions CD Successfully Working 🚀",
        "status": "healthy",
        "version": settings.API_VERSION
    }

@app.head("/")
async def health_check():
    return Response(status_code=200)

app.include_router(router)


app.middleware("http")(
    request_timing_middleware
)


app.add_exception_handler(
    Exception,
    global_exception_handler
)