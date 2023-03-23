from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from src.python.shared.encryption.jwt_handler import decode_jwt
from src.python.user.domain.user import User
from src.python.user.mapper.index import user_mapper
from src.python.user.repo.index import user_repo

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="api/v1/client/login",
    scheme_name="JWT"
)


async def validate_user(token=Depends(oauth2_scheme)) -> User:
    jwt_response = decode_jwt(token)

    if jwt_response is None:
        raise HTTPException(403, detail="could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    elif jwt_response.is_expired:
        raise HTTPException(401, detail="token expired", headers={"WWW-Authenticate": "Bearer"})

    _user = await user_repo.get_user_with_public_id(jwt_response.payload['user_public_id'])

    return user_mapper.to_domain(_user)
