from fastapi import Request, HTTPException
from prisma.errors import UniqueViolationError
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import JSONResponse

from src.python.shared.core.value_object.value_object_exception import ValueObjectException
from src.python.shared.responses.json_response import json_response


def item_not_found(detail: str | dict) -> JSONResponse:
    return json_response({"error": "item not found", "details": detail}, status_code=404)


def unauthorized(detail: str | dict) -> JSONResponse:
    return json_response({"error": "unauthorized", "details": detail}, status_code=401)


def bad_request(detail: str | dict) -> JSONResponse:
    return json_response({"error": "bad request", "details": detail}, status_code=400)


def method_not_allowed() -> JSONResponse:
    return json_response({"error": "method not allowed"}, status_code=405)


def internal_server_error(detail: str | dict) -> JSONResponse:
    # await log_internal_server_error(request)
    return json_response({"error": "internal server error", "details": detail}, status_code=500)


def forbidden(detail: str | dict) -> JSONResponse:
    return json_response({"error": "forbidden access", "details": detail}, status_code=403)


def http_exception_handler(code: int, detail: str | dict) -> JSONResponse:
    match code:
        case 400:
            return bad_request(detail)
        case 401:
            return unauthorized(detail)
        case 403:
            return forbidden(detail)
        case 404:
            return item_not_found(detail)
        case 405:
            return method_not_allowed()
        case 500:
            return internal_server_error(detail)
    return internal_server_error(detail)


class ExceptionHandler(BaseHTTPMiddleware):
    def __init__(
            self,
            app,
    ):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        try:
            return await call_next(request)

        except UniqueViolationError as e:
            return bad_request({
                "message": "missing the following fields",
                "fields": e.meta['target']
            })

        except HTTPException as error:
            return http_exception_handler(error.status_code, error.detail)

        except ValueObjectException as e:
            return bad_request({
                "message": e.error_value,
            })

        except Exception:
            return internal_server_error({
                "message": "An unexpected error occurred",
            })
