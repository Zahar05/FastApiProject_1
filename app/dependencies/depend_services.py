# from app.services.email_service import EmailService
from app.services.ocr_service import OCRService
from app.services.django_client import DjangoClient
from app.repositories.django_repository import DjangoRepository
from app.services.document_analyze_service import (DocumentAnalyzeService)
from app.services.document_process_service import (DocumentProcessService)


def build_document_process_service() -> DocumentProcessService:
    return DocumentProcessService(document_analyze_service=build_document_analyze_service())

def build_document_analyze_service() -> DocumentAnalyzeService:
    return DocumentAnalyzeService(
        django_repository=DjangoRepository(
            django_client=DjangoClient(),
        ),
        ocr_service=OCRService(),
    )


# def get_ocr_service() -> OCRService:
#     return OCRService()
#
# def get_email_service() ->EmailService:
#     return EmailService()
#
# def get_django_client() -> DjangoClient:
#     return DjangoClient()
#
# def get_django_repository() -> DjangoRepository:
#     return DjangoRepository(django_client=get_django_client())


# def get_document_analyze_service() -> DocumentAnalyzeService:
#     return DocumentAnalyzeService(
#         django_repository=get_django_repository(),
#         ocr_service=get_ocr_service(),
#     )


# def get_document_analyze_service() -> DocumentAnalyzeService:
#     return build_document_analyze_service()
