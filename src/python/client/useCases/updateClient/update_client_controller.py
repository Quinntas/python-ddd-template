from fastapi import Depends
from fastapi.security import HTTPBasic

from src.python.client.domain.client import Client
from src.python.client.dto.update_client_dto import UpdateClientDTO
from src.python.client.useCases.updateClient.update_client_usecase import UpdateClientUseCase
from src.python.client.validation.client_validation import validate_client
from src.python.shared.core.base_controller import BaseController
from src.python.shared.responses.json_response import json_response

security = HTTPBasic()


class UpdateClientController(BaseController):
    def __init__(self, update_client_usecase: UpdateClientUseCase):
        self.update_client_usecase = update_client_usecase

    async def execute(self, __client: UpdateClientDTO, _client: Client = Depends(validate_client)):
        await self.update_client_usecase.execute(__client, _client)
        return json_response({}, status_code=204)
