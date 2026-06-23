# from app.services.document_process_service import DocumentProcessService
from fastapi import APIRouter, Depends
from app.schemas.analyze import AnalyzeDocumentRequest, AnalyzeDocumentResponse
from app.tasks.analyze_doc_task import analyze_doc_task
from app.dependencies.depend_services import get_service_name
from app.core.exceptions import ImageNotFoundException, OCRException

router = APIRouter(tags=["Documents"])


@router.post(
    "/analyze_doc",
    response_model=AnalyzeDocumentResponse,
)
def analyze_doc(request: AnalyzeDocumentRequest):
    task = analyze_doc_task.delay(request.image_id, request.email)

    return AnalyzeDocumentResponse(detail="Document analysis started", task_id=task.id)


@router.get("/service_info")
def service_info(service_name: str = Depends(get_service_name)):
    return {"service_name": service_name}


@router.get("/test_404")
def test_404():
    raise ImageNotFoundException(123)


@router.get("/test_ocr")
def test_ocr():
    raise OCRException("OCR processing failed")
