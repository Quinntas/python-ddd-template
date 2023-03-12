from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPBasic, OAuth2PasswordRequestForm

from src.python.client.useCases.login.login_usecase import LoginUseCase
from src.python.shared.core.base_controller import BaseController
from src.python.shared.core.value_object.value_object_exception import ValueObjectException
from src.python.shared.responses.json_response import json_response

security = HTTPBasic()


class LoginController(BaseController):
    def __init__(self, login_usecase: LoginUseCase):
        self.login_usecase = login_usecase

    async def execute(self, form_data: OAuth2PasswordRequestForm = Depends(security)):
        try:
            token = await self.login_usecase.execute(form_data)
            return json_response(token)

        except HTTPException as error:
            raise HTTPException(error.status_code, error.detail)

        except ValueObjectException as error:
            raise HTTPException(400, detail=error.error_value)

        except Exception:
            raise HTTPException(500, {
                "message": "An unexpected error occurred",
            })
