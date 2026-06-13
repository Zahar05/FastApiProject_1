from fastapi import FastAPI

from app.core.lifespan import lifespan
from app.api.routers.documents import router as documents_router
from fastapi.exceptions import RequestValidationError

from app.core.exceptions import (ImageNotFoundException, OCRException, EmailSendException)

from app.core.exception_handlers import (image_not_found_handler, validation_exception_handler,
    ocr_exception_handler, email_exception_handler,
)
from app.api.routers.email import router as email_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Document Analyzer Service", version="1.0.0", lifespan=lifespan)

    app.include_router(documents_router)
    app.include_router(email_router)

    app.add_exception_handler(ImageNotFoundException, image_not_found_handler)

    app.add_exception_handler(RequestValidationError, validation_exception_handler)

    app.add_exception_handler(OCRException, ocr_exception_handler)

    app.add_exception_handler(EmailSendException, email_exception_handler)

    return app

app = create_app()
