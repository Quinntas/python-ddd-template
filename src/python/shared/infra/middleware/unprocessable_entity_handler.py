from collections import defaultdict

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

from src.python.shared.responses.json_response import json_response


def unprocessable_entity(request: Request, exception: RequestValidationError) -> JSONResponse:
    reformatted_message = defaultdict(list)
    for pydantic_error in exception.errors():
        loc, msg = pydantic_error["loc"], pydantic_error["msg"]
        filtered_loc = loc[1:] if loc[0] in ("body", "query", "path") else loc
        field_string = ".".join(filtered_loc)
        reformatted_message[field_string].append(msg)
    return json_response(
        {"error": "validation error", "details": reformatted_message}, status_code=422
    )
