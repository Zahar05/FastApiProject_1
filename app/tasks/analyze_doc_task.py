from app.tasks.celery_app import celery_app

from app.services.document_analyze_service import (DocumentAnalyzeService)
from app.repositories.django_repository import (DjangoRepository)

from app.services.django_client import DjangoClient
from app.services.ocr_service import OCRService


@celery_app.task
def analyze_doc_task(image_id: int) -> str:

    service = DocumentAnalyzeService(
        django_repository=DjangoRepository(
            django_client=DjangoClient(),
        ),
        ocr_service=OCRService(),
    )

    return service.analyze(image_id)

