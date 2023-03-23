from decouple import config
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.middleware.sessions import SessionMiddleware

from src.python.shared.domain.favicon import favicon
from src.python.shared.events.shutdown import shutdown
from src.python.shared.events.startup import startup
from src.python.shared.infra.http.app_details import app_details
from src.python.shared.infra.middleware.exception_handler import ExceptionHandler
from src.python.shared.infra.middleware.process_time import ProcessTime
from src.python.shared.infra.middleware.unprocessable_entity_handler import unprocessable_entity
from src.python.shared.infra.v1_router.v1_router import v1_router

SESSION_SECRET = config('SESSION_SECRET')
PORT = config('PORT')

app = FastAPI(**app_details)

# Favicon
app.get('/favicon.ico', include_in_schema=False)(favicon)

# Exception Handler
app.exception_handler(RequestValidationError)(unprocessable_entity)

# Events
app.on_event('startup')(startup)
app.on_event('shutdown')(shutdown)

# Middleware
app.add_middleware(ExceptionHandler)
app.add_middleware(ProcessTime)
app.add_middleware(SessionMiddleware, secret_key=SESSION_SECRET)

# Routers
app.include_router(v1_router, prefix="/api/v1")
