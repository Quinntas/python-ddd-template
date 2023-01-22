from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from src.python.client.domain.client_model import Client
from src.python.shared.encryption.jwt_handler import decode_jwt

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="api/v1/client/login",
    scheme_name="JWT"
)


async def validate_client(token=Depends(oauth2_scheme)) -> Client:
    jwt_response = decode_jwt(token)

    if jwt_response is None:
        raise HTTPException(403, detail="could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    elif jwt_response.is_expired:
        raise HTTPException(401, detail="token expired", headers={"WWW-Authenticate": "Bearer"})

    # _client = await db.select_from_params(Tables.clients.value, Databases.delivery.value,
    #                                      {"uuid": jwt_response.payload['uuid']}, 'ONE')

    # if not _client:
    #    raise HTTPException(404)

    # return _list_loader(Client, _client)
