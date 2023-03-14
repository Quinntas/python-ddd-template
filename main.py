import socket

import uvicorn
from decouple import config
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import JSONResponse

from src.python.shared.infra.database.prisma_handler import prisma
from src.python.shared.infra.http.app_details import app_details
from src.python.shared.infra.middleware.exception_handler import ExceptionHandler
from src.python.shared.infra.middleware.process_time import ProcessTime
from src.python.shared.infra.middleware.unprocessable_entity_handler import unprocessable_entity
from src.python.shared.infra.v1_router.v1_router import v1_router

SESSION_SECRET = config('SESSION_SECRET')
PORT = config('PORT')

app = FastAPI(**app_details)


# Favicon
@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('data/icon.ico')


# Exception Handler
@app.exception_handler(RequestValidationError)
async def validation_error(request: Request, exception: RequestValidationError) -> JSONResponse:
    return unprocessable_entity(exception)


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
app.add_middleware(ExceptionHandler)
app.add_middleware(ProcessTime)
app.add_middleware(SessionMiddleware, secret_key=SESSION_SECRET)

# Routers
app.include_router(
    v1_router,
    prefix="/api/v1",
)


def main():
    host = socket.gethostbyname(socket.gethostname())
    uvicorn.run("main:app", host=host, port=PORT, server_header=False, reload=True)


if __name__ == "__main__":
    pass
