from starlette.responses import FileResponse


async def favicon():
    return FileResponse('data/icon.ico')
