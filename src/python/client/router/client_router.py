from fastapi import APIRouter
from fastapi.security import HTTPBasic

from src.python.client.router.routes.client_create import create_client_route
from src.python.client.router.routes.client_get import get_client_route
from src.python.client.router.routes.client_login import login_client_route
from src.python.client.router.routes.client_put import put_client_route

client = APIRouter()

security = HTTPBasic()

client.include_router(create_client_route)
client.include_router(login_client_route)
client.include_router(get_client_route)
client.include_router(put_client_route)
