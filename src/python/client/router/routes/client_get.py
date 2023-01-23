from fastapi import APIRouter, Depends

from src.python.client.domain.client_model import Client
from src.python.client.mapper.client_mapper import to_dict
from src.python.client.validation.client_validation import validate_client
from src.python.shared.responses.json_response import json_response

get_client_route = APIRouter(
    prefix='/me',
    tags=['client']
)


@get_client_route.get("/")
async def get(_client: Client = Depends(validate_client)):
    return json_response(to_dict(_client))
