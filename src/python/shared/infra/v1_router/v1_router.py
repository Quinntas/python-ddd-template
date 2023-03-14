from fastapi import APIRouter

from src.python.client.infra.http.routes.client_router import client_router

v1_router = APIRouter()

v1_router.include_router(
    client_router,
    prefix="/client",
    tags=["Client UseCases"]
)
