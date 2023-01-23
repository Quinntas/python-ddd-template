from fastapi import APIRouter, Depends, HTTPException

from src.python.client.domain.client_avatar import ClientAvatar
from src.python.client.domain.client_model import Client
from src.python.client.domain.client_phone_number import ClientPhoneNumber
from src.python.client.dto.update_client_dto import UpdateClientDTO
from src.python.client.repo.client_repo import put_client
from src.python.client.validation.client_validation import validate_client
from src.python.shared.core.value_object.value_object_exception import ValueObjectException
from src.python.shared.responses.json_response import json_response

put_client_route = APIRouter(
    prefix='/put',
    tags=['client']
)


@put_client_route.get("/")
async def put(__client: UpdateClientDTO, _client: Client = Depends(validate_client)):
    try:
        __client.avatar = ClientAvatar(__client.avatar).get_value()
        __client.phone_number = ClientPhoneNumber(__client.phone_number).get_value()
    except ValueObjectException as error:
        raise HTTPException(400, detail=error.error_value)
    await put_client(__client, _client.publicId.get_value())
    return json_response({'success': True})
