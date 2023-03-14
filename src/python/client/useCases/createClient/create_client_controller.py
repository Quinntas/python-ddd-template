
from src.python.client.dto.new_client_dto import NewClientDTO
from src.python.client.useCases.createClient.create_client_usecase import CreateClientUseCase
from src.python.shared.core.base_controller import BaseController
from src.python.shared.responses.json_response import json_response


class CreateClientController(BaseController):
    def __init__(self, create_client_usecase: CreateClientUseCase):
        self.create_client_usecase = create_client_usecase

    async def execute(self, new_client: NewClientDTO):
        await self.create_client_usecase.execute(new_client)
        return json_response({"success": "true"}, status_code=201)
