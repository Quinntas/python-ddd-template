from fastapi import APIRouter

from src.python.client.useCases.createClient.init import create_client_controller
from src.python.client.useCases.getCurrentClient.init import get_current_client_controller
from src.python.client.useCases.login.init import login_controller
from src.python.client.useCases.updateClient.init import update_client_controller

client_router = APIRouter()

client_router.post("/create")(create_client_controller.execute)

client_router.post("/login")(login_controller.execute)

client_router.get("/getCurrent")(get_current_client_controller.execute)

client_router.put("/update")(update_client_controller.execute)
