from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPBasic

from src.python.client.domain.client import Client
from src.python.client.dto.update_client_dto import UpdateClientDTO
from src.python.client.useCases.updateClient.update_client_usecase import UpdateClientUseCase
from src.python.client.validation.client_validation import validate_client
from src.python.shared.core.base_controller import BaseController
from src.python.shared.core.value_object.value_object_exception import ValueObjectException
from src.python.shared.responses.json_response import json_response

security = HTTPBasic()


class UpdateClientController(BaseController):
    def __init__(self, update_client_usecase: UpdateClientUseCase):
        self.update_client_usecase = update_client_usecase

    async def execute(self, __client: UpdateClientDTO, _client: Client = Depends(validate_client)):
        try:
            await self.update_client_usecase.execute(__client, _client)
            return json_response({}, status_code=204)

        except HTTPException as error:
            raise HTTPException(error.status_code, error.detail)

        except ValueObjectException as error:
            raise HTTPException(400, detail=error.error_value)

        except Exception:
            raise HTTPException(500, {
                "message": "An unexpected error occurred",
            })
