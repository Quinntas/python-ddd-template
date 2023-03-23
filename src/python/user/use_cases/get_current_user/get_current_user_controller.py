from fastapi import Depends
from fastapi.security import HTTPBasic

from src.python.shared.core.base_controller import BaseController
from src.python.shared.core.base_usecase import UseCase
from src.python.shared.responses.json_response import json_response
from src.python.user.domain.user import User
from src.python.user.validation.user_validation import validate_user

security = HTTPBasic()


class GetCurrentUserController(BaseController):
    def __init__(self, get_current_entity_usecase: UseCase):
        self.get_current_entity_usecase = get_current_entity_usecase

    async def execute(self, user: User = Depends(validate_user)):
        result = await self.get_current_entity_usecase.execute(user)
        return json_response(result)
