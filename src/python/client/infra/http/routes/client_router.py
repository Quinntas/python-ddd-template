from fastapi import APIRouter

from src.python.client.use_cases.create_client.init import create_client_controller
from src.python.client.use_cases.get_current_client.init import get_current_client_controller

client_router = APIRouter()

client_router.post("/create")(create_client_controller.execute)

client_router.get("/getCurrent")(get_current_client_controller.execute)
