from fastapi import status
from fastapi.responses import JSONResponse


def send_response(success: bool, message: str, data: dict|object | None = None, status_code: int = status.HTTP_200_OK):
    response_content = {
        "success": success,
        "message": message,
        "data": data
    }
    return JSONResponse(content=response_content, status_code=status_code)