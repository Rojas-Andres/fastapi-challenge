from fastapi import FastAPI
from app.infrastructure.api.routers import locations_router
from app.core.middleware import ErrorHandlerMiddleware  # noqa: E402
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Aplicación My World", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(ErrorHandlerMiddleware)
app.include_router(
    locations_router.router, prefix="/api/v1/locations", tags=["locations"]
)
