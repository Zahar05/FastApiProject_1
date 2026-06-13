from fastapi import APIRouter, Depends
from app.schemas.analyze import (AnalyzeDocumentRequest,AnalyzeDocumentResponse)

# from app.services.ocr_service import OCRService
# from app.dependencies.depend_services import get_ocr_service
# from app.services.django_client import DjangoClient
# from app.dependencies.depend_services import get_django_client
# from app.repositories.django_repository import DjangoRepository
# from app.dependencies.depend_services import get_django_repository

from app.services.document_analyze_service import (DocumentAnalyzeService)
from app.dependencies.depend_services import (get_document_analyze_service)


router = APIRouter(tags=["Documents"])

@router.post(
    "/analyze_doc",
    response_model=AnalyzeDocumentResponse,
)
def analyze_doc(
    request: AnalyzeDocumentRequest,
    document_service: DocumentAnalyzeService = Depends(get_document_analyze_service),
    # ocr_service: OCRService = Depends(get_ocr_service),
    # django_repository: DjangoRepository = Depends(get_django_repository),
    # django_client: DjangoClient = Depends(get_django_client),
):
    text = document_service.analyze(request.image_id)
    # image_info = django_client.get_image_info(request.image_id# )
    # image_info = django_repository.get_image_info(request.image_id# )
    # text = ocr_service.extract_text(image_info["image_url"]# )

    return AnalyzeDocumentResponse(
        detail=text,
        task_id="temporary-task-id",
    )




# @router.post(
#     "/analyze_doc",
#     response_model=AnalyzeDocumentResponse,
# )
# def analyze_doc(
#     request: AnalyzeDocumentRequest,
#     ocr_service: OCRService = Depends(get_ocr_service),
# ):
#     text = ocr_service.extract_text(
#         f"image_{request.image_id}.jpg"
#     )
#
#     return AnalyzeDocumentResponse(
#         detail=text,
#         task_id="temporary-task-id",
#     )





# from fastapi import APIRouter
#
# router = APIRouter(tags=["Documents"])
#
#
# @router.get("/health")
# async def health_check():
#     return {
#         "detail": "Service is running"
#     }