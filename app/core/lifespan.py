from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app):

    app.state.service_name = app.title

    yield

# @asynccontextmanager
# async def lifespan(app):
#     print("Application startup")
#
#     app.state.service_name = "Document Analyzer Service"
#     app.state.version = "1.0.0"
#
#     yield
#
#     print("Application shutdown")






# from contextlib import asynccontextmanager
# from app.repositories.django_repository import DjangoRepository
# from app.services.django_client import DjangoClient
# from app.services.document_analyze_service import DocumentAnalyzeService
# from app.services.document_process_service import DocumentProcessService
# from app.services.ocr_service import OCRService
#
#
# @asynccontextmanager
# async def lifespan(app):
#
#     django_client = DjangoClient()
#
#     django_repository = DjangoRepository(
#         django_client=django_client
#     )
#
#     ocr_service = OCRService()
#
#     document_analyze_service = DocumentAnalyzeService(
#         django_repository=django_repository,
#         ocr_service=ocr_service,
#     )
#
#     app.state.document_process_service = (
#         DocumentProcessService(
#             document_analyze_service=document_analyze_service
#         )
#     )
#
#     yield ЭТО ПРИВОДИТ К ЦИКЛИЧЕСКОМУ ИМПОРТУ!!!!!

