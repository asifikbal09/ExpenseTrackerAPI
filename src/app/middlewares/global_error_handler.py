from fastapi import Request
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
from starlette.exceptions import HTTPException as StarletteHTTPException

from src.app.utils.sendResponse import send_response


async def global_exception_handler(
    request: Request,
    exc: Exception,
):
    return send_response(
        status_code=500,
        success=False,
        message="Something went wrong. Please try again later.",
        data=None,
    )


async def http_exception_handler(
    request: Request,
    exc: StarletteHTTPException,
):
    return send_response(
        status_code=exc.status_code,
        success=False,
        message=exc.detail,
        data=None,
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    return send_response(
        status_code=422,
        success=False,
        message="Validation error",
        data=exc.errors(),
    )



async def database_exception_handler(
    request: Request,
    exc: SQLAlchemyError,
):
    return send_response(
        status_code=500,
        success=False,
        message="Database error occurred. Please try again later.",
        data=None,
    )