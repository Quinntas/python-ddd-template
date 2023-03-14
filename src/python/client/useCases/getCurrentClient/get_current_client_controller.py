from fastapi import Depends
from fastapi.security import HTTPBasic

from src.python.client.domain.client import Client
from src.python.client.useCases.getCurrentClient.get_current_client_usecase import GetCurrentClientUseCase
from src.python.client.validation.client_validation import validate_client
from src.python.shared.core.base_controller import BaseController
from src.python.shared.responses.json_response import json_response

security = HTTPBasic()


class LoginController(BaseController):
    def __init__(self, get_current_client_usecase: GetCurrentClientUseCase):
        self.get_current_client_usecase = get_current_client_usecase

    async def execute(self, _client: Client = Depends(validate_client)):
        token = await self.get_current_client_usecase.execute(_client)
        return json_response(token)
