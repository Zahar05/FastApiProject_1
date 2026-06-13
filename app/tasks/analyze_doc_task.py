from app.dependencies.depend_services import (build_document_process_service)
from app.tasks.celery_app import celery_app


@celery_app.task
def analyze_doc_task(image_id: int, email: str) -> str:
    service = build_document_process_service()
    return service.process(image_id=image_id, email=email)




# from app.dependencies.depend_services import (build_document_analyze_service)
# from app.tasks.celery_app import celery_app
# from app.tasks.send_email_task import send_email_task
#
#
# @celery_app.task
# def analyze_doc_task(
#     image_id: int,
#     email: str,
# ) -> str:
#
#     service = build_document_analyze_service()
#
#     text = service.analyze(image_id)
#     send_email_task.delay(email=email, subject="Image analyzed", message=text)
#
#     return text




# from app.tasks.celery_app import celery_app
# from app.services.document_analyze_service import (DocumentAnalyzeService)
# from app.repositories.django_repository import (DjangoRepository)
# from app.services.django_client import DjangoClient
# from app.services.ocr_service import OCRService
# from app.tasks.send_email_task import send_email_task
#
#
# @celery_app.task
# def analyze_doc_task(image_id: int, email: str) -> str:
#     service = DocumentAnalyzeService(django_repository=DjangoRepository(django_client=DjangoClient()),
#         ocr_service=OCRService(),
#     )
#     text = service.analyze(image_id)
#
#     send_email_task.delay(email=email, subject="Image analyzed", message=text)
#
#     return text



# from app.tasks.celery_app import celery_app
# from app.services.document_analyze_service import (DocumentAnalyzeService)
# from app.repositories.django_repository import (DjangoRepository)
#
# from app.services.django_client import DjangoClient
# from app.services.ocr_service import OCRService
# from app.services.email_service import EmailService
#
#
# @celery_app.task
# def analyze_doc_task(image_id: int, email: str) -> str:
#     service = DocumentAnalyzeService(
#         django_repository=DjangoRepository(django_client=DjangoClient()),
#         ocr_service=OCRService(),
#     )
#     text = service.analyze(image_id)
#
#     EmailService().send(email=email, subject="Image analyzed", message=text)
#
#     return text



# from app.tasks.celery_app import celery_app
#
# from app.services.document_analyze_service import (DocumentAnalyzeService)
# from app.repositories.django_repository import (DjangoRepository)
#
# from app.services.django_client import DjangoClient
# from app.services.ocr_service import OCRService
#
#
# @celery_app.task
# def analyze_doc_task(image_id: int) -> str:
#
#     service = DocumentAnalyzeService(
#         django_repository=DjangoRepository(
#             django_client=DjangoClient(),
#         ),
#         ocr_service=OCRService(),
#     )
#
#     return service.analyze(image_id)

