from app.repositories.django_repository import DjangoRepository
from app.services.ocr_service import OCRService


class DocumentAnalyzeService:

    def __init__(self, django_repository: DjangoRepository, ocr_service: OCRService):
        self.django_repository = django_repository
        self.ocr_service = ocr_service

    def analyze(self, image_id: int) -> str:

        image_info = self.django_repository.get_image_info(image_id)
        text = self.ocr_service.extract_text(image_info["image"])
        # text = self.ocr_service.extract_text(image_info["image_url"])

        return text

