from fastapi import APIRouter, Depends
from app.schemas.analyze import (AnalyzeDocumentRequest,AnalyzeDocumentResponse)

from app.services.document_analyze_service import (DocumentAnalyzeService)
from app.dependencies.depend_services import (get_document_analyze_service)
from app.tasks.analyze_doc_task import analyze_doc_task


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
    task = analyze_doc_task.delay(request.image_id)

    return AnalyzeDocumentResponse(detail="Document analysis started", task_id=task.id)




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