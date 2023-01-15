from datetime import datetime as dt

from fastapi import Request


async def log_it(log_file_path: str, title: str, text: str = ''):
    with open(log_file_path, "a+") as f:
        if text != '':
            text = f'\n- {text}'
        f.write(f"[{dt.utcnow().strftime('%m/%d/%Y-%H:%M:%S')}] {title} {text}\n\n")


async def log_internal_server_error(request: Request):
    body = await request.json()
    url = "http://" + request.url.hostname + request.url.path
    client = request.client.host + ":" + str(request.client.port)
    headers = request.headers

    log_text = f"- URL: {url}\n- Client: {client}\n- Body: {body}\n- Headers: {headers}"

    await log_it("INTERNAL SERVER ERROR LOG", log_text)
