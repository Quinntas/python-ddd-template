from fastapi.responses import JSONResponse


def json_response(content: dict, content_lang: str = 'en-US', content_type: str = 'application/json',
                  status_code: int = 200):
    headers = {
        "server": "Luna Cloud Servers",
        "content-language": content_lang,
        "content-type": content_type,
        "cache-control": 'no-cache, no-store'
    }
    return JSONResponse(content=content, headers=headers, status_code=status_code)
