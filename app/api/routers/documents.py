from fastapi import APIRouter
from app.schemas.analyze import (AnalyzeDocumentRequest,AnalyzeDocumentResponse)

from app.tasks.analyze_doc_task import analyze_doc_task


router = APIRouter(tags=["Documents"])

@router.post(
    "/analyze_doc",
    response_model=AnalyzeDocumentResponse,
)
def analyze_doc(
    request: AnalyzeDocumentRequest,
    ):
    task = analyze_doc_task.delay(request.image_id)

    return AnalyzeDocumentResponse(detail="Document analysis started", task_id=task.id)

