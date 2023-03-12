import socket
import time
from collections import defaultdict

import uvicorn
from decouple import config
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, FileResponse
from starlette.middleware.sessions import SessionMiddleware

from src.python.client.router.client_router import client
from src.python.shared.infra.database.prisma_handler import prisma
from src.python.shared.responses.json_response import json_response
from src.python.shared.utils.log import log_internal_server_error

SESSION_SECRET = config('SESSION_SECRET')
PORT = config('PORT')

app = FastAPI(
    title="Delivery",
    description="Delivery - Luna Cloud Services",
    version="1.0",
    contact={
        "name": "Caio Quintas Santiago",
        "email": "caioquintassantiago@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
    terms_of_service="MIT"
)


@app.get('/')
async def about():
    return json_response({
        "title": app.title,
        "description": app.description,
        "contact": app.contact,
        "license": app.license_info,
        "terms_of_service": app.terms_of_service
    })


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('data/icon.ico')


@app.exception_handler(404)
def item_not_found(request: Request, exception: HTTPException) -> JSONResponse:
    return json_response({"error": "item not found", "details": exception.detail}, status_code=404)


@app.exception_handler(401)
def unauthorized(request: Request, exception: HTTPException) -> JSONResponse:
    return json_response({"error": "unauthorized", "details": exception.detail}, status_code=401)


@app.exception_handler(400)
def bad_request(request: Request, exception: HTTPException) -> JSONResponse:
    return json_response({"error": "bad request", "details": exception.detail}, status_code=400)


@app.exception_handler(405)
def method_not_allowed(request: Request, exception: HTTPException) -> JSONResponse:
    return json_response({"error": "method not allowed"}, status_code=405)


@app.exception_handler(500)
async def internal_server_error(request: Request, exception: HTTPException) -> JSONResponse:
    await log_internal_server_error(request)
    return json_response({"error": "internal server error"}, status_code=500)


@app.exception_handler(403)
def forbidden(request: Request, exception: HTTPException) -> JSONResponse:
    return json_response({"error": "forbidden access", "details": exception.detail}, status_code=403)


@app.exception_handler(RequestValidationError)
async def validation_error(request: Request, exception: RequestValidationError) -> JSONResponse:
    reformatted_message = defaultdict(list)
    for pydantic_error in exception.errors():
        loc, msg = pydantic_error["loc"], pydantic_error["msg"]
        filtered_loc = loc[1:] if loc[0] in ("body", "query", "path") else loc
        field_string = ".".join(filtered_loc)
        reformatted_message[field_string].append(msg)
    return json_response({"error": "validation error", "details": reformatted_message}, status_code=422)


# Events
@app.on_event('startup')
async def startup():
    print('[DATABASE] Connecting to the database')
    await prisma.connect()
    print(f'[APP] App is running on {PORT}')
    # await log_it("Application starting up", LOG_PATH)


@app.on_event('shutdown')
async def shutdown():
    print('[DATABASE] Disconnecting to the database')
    await prisma.disconnect()
    print('[APP] App is shut down')
    # await log_it("Application shutting down", LOG_PATH)


# Middleware
@app.middleware("http")
async def add_process_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.add_middleware(SessionMiddleware, secret_key=SESSION_SECRET)

# Routers
app.include_router(
    client,
    prefix="/api/v1/client",
    tags=["client"]
)


def main():
    host = socket.gethostbyname(socket.gethostname())
    uvicorn.run("main:app", host=host, port=PORT, server_header=False)


if __name__ == "__main__":
    pass
    # main()
