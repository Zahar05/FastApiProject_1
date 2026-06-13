from app.services.document_analyze_service import (DocumentAnalyzeService)
from app.tasks.send_email_task import send_email_task


class DocumentProcessService:

    def __init__(self, document_analyze_service: DocumentAnalyzeService):
        self.document_analyze_service = (document_analyze_service)

    def process(self, image_id: int, email: str) -> dict:
        text = self.document_analyze_service.analyze(image_id)

        result = send_email_task.delay(
            email=email,
            subject="Image analyzed",
            message=text,
        )

        return {
            "text": text,
            "email_task_id": result.id,
        }

