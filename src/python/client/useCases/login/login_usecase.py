from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from src.python.client.repo.client_repo import get_client_with_user_id
from src.python.shared.core.base_usecase import UseCase
from src.python.shared.encryption.encryption import verify_encryption
from src.python.shared.encryption.jwt_handler import sign_jwt
from src.python.user.repo.user_repo import get_user_with_email


class LoginUseCase(UseCase):
    async def execute(self, form_data: OAuth2PasswordRequestForm):
        if form_data.username == "" or form_data.password == "":
            raise HTTPException(401)

        user_info = await get_user_with_email(form_data.username)

        if not user_info:
            raise HTTPException(404, 'user was not found')

        if verify_encryption(form_data.password, user_info.password) is False:
            raise HTTPException(401)

        client_info = await get_client_with_user_id(user_info.id)

        if not user_info:
            raise HTTPException(404, 'client was not found')

        return sign_jwt({
            'client_public_id': client_info.publicId,
            'user_public_id': user_info.publicId,
            'email_verified': user_info.email_verified,
            'role': user_info.role
        })
