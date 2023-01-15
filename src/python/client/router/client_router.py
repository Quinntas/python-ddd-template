from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import HTTPBasic, OAuth2PasswordRequestForm

from src.python.client.model.client_model import Client
from src.python.client.validation.client_validation import validate_client
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
    if len(_client.password) < 6:
        raise HTTPException(400, detail='password must be at least 6 characters long')
    _client.password = gen_pbkdf2_sha256(_client.password)
    current_dt = get_curr_dt()
    _client.email_verified_at = 'never'
    _client.created_at = current_dt
    _client.updated_at = current_dt

    await db.insert_value(Tables.clients.value, Databases.delivery.value, _client.get_dict())

    return json_response(_client.default_response(), status_code=201)


@client.get("/")
async def get(_client: Client = Depends(validate_client)):
    return json_response(_client.default_response())


@client.put("/")
async def put(__client: Client, _client: Client = Depends(validate_client)):
    await db.update_value(Tables.clients.value, Databases.delivery.value, __client.put_response(),
                          {'uuid': _client.uuid})
    _client = __client
    return json_response(_client.put_response())


@client.patch("/verify_email")
async def verify_email(_client: Client = Depends(validate_client)):
    await db.update_value(Tables.clients.value, Databases.delivery.value, {'email_verified_at': get_curr_dt()},
                          {'uuid': _client.uuid})
    return json_response({'message': 'email verified'})


@client.patch("/change_password")
async def change_password(request: Request, _client: Client = Depends(validate_client)):
    try:
        body = await request.json()
    except Exception:
        raise HTTPException(400, detail='no body in request')
    if 'password' not in body:
        raise HTTPException(400, detail='missing password field in body')
    if len(body['password']) < 6:
        raise HTTPException(400, detail='password must be at least 6 characters long')
    new_password = gen_pbkdf2_sha256(body['password'])
    await db.update_value(Tables.clients.value, Databases.delivery.value, {'password': new_password},
                          {'uuid': _client.uuid})
    return json_response({'message': 'password changed'})


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
