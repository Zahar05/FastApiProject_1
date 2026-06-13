from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.core.exceptions import (ImageNotFoundException, OCRException, EmailSendException)


async def image_not_found_handler(exc: ImageNotFoundException):
    return JSONResponse(status_code=404,content={"detail": f"Image with id={exc.image_id} not found"})


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    return JSONResponse(
        status_code=422,
        content={
            "detail": "Validation error"
        },
    )


async def ocr_exception_handler(
    request: Request,
    exc: OCRException,
):
    return JSONResponse(
        status_code=422,
        content={
            "detail": "OCR processing failed"
        },
    )


async def email_exception_handler(
    request: Request,
    exc: EmailSendException,
):
    return JSONResponse(
        status_code=422,
        content={
            "detail": "Email sending failed"
        },
    )