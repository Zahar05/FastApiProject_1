from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.core.exceptions import (
    ImageNotFoundException,
    OCRException,
    EmailSendException,
)


# 1. Для ImageNotFoundException
async def image_not_found_handler(request: Request, exc: Exception) -> JSONResponse:
    assert isinstance(exc, ImageNotFoundException)
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": str(exc)})


# 2. Для RequestValidationError
async def validation_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    assert isinstance(exc, RequestValidationError)
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={"detail": exc.errors()})


# 3. Для OCRException
async def ocr_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    assert isinstance(exc, OCRException)
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(exc)})


# 4. Для EmailSendException
async def email_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    assert isinstance(exc, EmailSendException)
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": str(exc)})


# async def image_not_found_handler(
#     request: Request,
#     exc: ImageNotFoundException,
# ) -> Response:
#     return JSONResponse(
#         status_code=404,
#         content={"detail": f"Image with id={exc.image_id} not found"},
#     )
#
#
# async def validation_exception_handler(
#     request: Request,
#     exc: RequestValidationError,
# ) -> Response:
#     return JSONResponse(
#         status_code=422,
#         content={"detail": "Validation error"},
#     )
#
#
# async def ocr_exception_handler(
#     request: Request,
#     exc: OCRException,
# ) -> Response:
#     return JSONResponse(
#         status_code=422,
#         content={"detail": exc.detail},
#     )
#
#
# async def email_exception_handler(
#     request: Request,
#     exc: EmailSendException,
# ) -> Response:
#     return JSONResponse(
#         status_code=422,
#         content={"detail": exc.detail},
#     )
