from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPBasic

from src.python.client.domain.client import Client
from src.python.client.useCases.getCurrentClient.get_current_client_usecase import GetCurrentClientUseCase
from src.python.client.validation.client_validation import validate_client
from src.python.shared.core.base_controller import BaseController
from src.python.shared.core.value_object.value_object_exception import ValueObjectException
from src.python.shared.responses.json_response import json_response

security = HTTPBasic()


class LoginController(BaseController):
    def __init__(self, get_current_client_usecase: GetCurrentClientUseCase):
        self.get_current_client_usecase = get_current_client_usecase

    async def execute(self, _client: Client = Depends(validate_client)):
        try:
            token = await self.get_current_client_usecase.execute(_client)
            return json_response(token)

        except HTTPException as error:
            raise HTTPException(error.status_code, error.detail)

        except ValueObjectException as error:
            raise HTTPException(400, detail=error.error_value)

        except Exception:
            raise HTTPException(500, {
                "message": "An unexpected error occurred",
            })
