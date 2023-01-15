from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic, OAuth2PasswordRequestForm

from src.python.client.model.client_model import Client
from src.python.shared.encryption.encryption import gen_pbkdf2_sha256, verify_encryption
from src.python.shared.encryption.jwt_handler import sign_jwt, decode_jwt
from src.python.shared.infra.database.database import database as db
from src.python.shared.infra.database.enums.databases import Databases
from src.python.shared.infra.database.enums.tables import Tables
from src.python.shared.responses.json_response import json_response
from src.python.shared.utils.model_loader import _list_loader
from src.python.shared.utils.time_handler import get_curr_dt

client = APIRouter()

security = HTTPBasic()


@client.post("/")
async def create(_client: Client):
    _client.password = gen_pbkdf2_sha256(_client.password)
    current_dt = get_curr_dt()
    _client.created_at = current_dt
    _client.updated_at = current_dt

    await db.insert_value(Tables.clients.value, Databases.delivery.value, _client.get_dict())

    return json_response(_client.default_response(), status_code=201)


@client.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(security)):
    if form_data.username == "" or form_data.password == "":
        raise HTTPException(401)

    client_info = await db.select_from_params(Tables.clients.value, Databases.delivery.value,
                                              {"email": form_data.username}, 'ONE')

    if client_info is None:
        raise HTTPException(404)

    _client = _list_loader(Client, client_info)

    if verify_encryption(form_data.password, _client.password) is False:
        raise HTTPException(401)

    token = sign_jwt({'uuid': _client.uuid})
    print(decode_jwt(token['token']))
    return json_response(token)
