import prisma
from fastapi import APIRouter, HTTPException

from src.python.client.dto.new_client_dto import NewClientDTO
from src.python.client.repo.client_repo import create_client
from src.python.shared.encryption.encryption import gen_pbkdf2_sha256
from src.python.shared.responses.json_response import json_response

create_client_route = APIRouter(
    prefix='/create',
    tags=['client']
)


@create_client_route.post("/")
async def create(new_client: NewClientDTO):
    new_client.password = gen_pbkdf2_sha256(new_client.password)

    try:
        await create_client(new_client)
    except prisma.errors.UniqueViolationError as e:
        raise HTTPException(400, {
            "message": "the following fields already exists",
            "fields": e.meta['target']
        })

    return json_response({"success": "true"}, status_code=201)
