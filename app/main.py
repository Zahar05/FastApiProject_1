from fastapi import FastAPI

from app.core.lifespan import lifespan
from app.api.routers.documents import router as documents_router
from fastapi.exceptions import RequestValidationError
from app.core.exceptions import ImageNotFoundException, OCRException, EmailSendException

from app.core.exception_handlers import (
    image_not_found_handler,
    validation_exception_handler,
    ocr_exception_handler,
    email_exception_handler,
)
from app.api.routers.health import router as health_router
from app.api.routers.email import router as email_router
from app.api.routers import tasks
from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.SERVICE_NAME, version=settings.APP_VERSION, lifespan=lifespan)

    app.include_router(tasks.router)
    app.include_router(documents_router)
    app.include_router(email_router)
    app.include_router(health_router)

    app.add_exception_handler(ImageNotFoundException, image_not_found_handler)

    app.add_exception_handler(RequestValidationError, validation_exception_handler)

    app.add_exception_handler(OCRException, ocr_exception_handler)

    app.add_exception_handler(EmailSendException, email_exception_handler)

    return app


app = create_app()
