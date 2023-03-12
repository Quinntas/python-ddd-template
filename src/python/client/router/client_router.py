from fastapi import APIRouter
from fastapi.security import HTTPBasic

from src.python.client.useCases.createClient.init import create_client_controller

client = APIRouter()

security = HTTPBasic()

client.post("/create")(create_client_controller.execute)
