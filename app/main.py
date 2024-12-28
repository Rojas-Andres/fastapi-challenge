from fastapi import FastAPI
from app.infrastructure.api.routers import locations_router


app = FastAPI(title="Aplicación My World", version="0.1.0")

app.include_router(
    locations_router.router, prefix="/api/v1/locations", tags=["locations"]
)
