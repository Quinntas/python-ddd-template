from fastapi import Depends
from fastapi.security import HTTPBasic, OAuth2PasswordRequestForm

from src.python.client.useCases.login.login_usecase import LoginUseCase
from src.python.shared.core.base_controller import BaseController
from src.python.shared.responses.json_response import json_response

security = HTTPBasic()


class LoginController(BaseController):
    def __init__(self, login_usecase: LoginUseCase):
        self.login_usecase = login_usecase

    async def execute(self, form_data: OAuth2PasswordRequestForm = Depends(security)):
        token = await self.login_usecase.execute(form_data)
        return json_response(token)
