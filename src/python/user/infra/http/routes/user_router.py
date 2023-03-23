from fastapi import APIRouter

from src.python.user.use_cases.get_current_user.init import get_current_user_controller
from src.python.user.use_cases.login.init import login_controller

user_router = APIRouter()

user_router.post("/login")(login_controller.execute)
user_router.get("/getCurrent")(get_current_user_controller.execute)
