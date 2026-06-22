from app.repositories.django_repository import DjangoRepository
from app.services.ocr_service import OCRService


class DocumentAnalyzeService:

    def __init__(self, django_repository: DjangoRepository, ocr_service: OCRService):
        self.django_repository = django_repository
        self.ocr_service = ocr_service

    def analyze(self, image_id: int) -> str:
        """Получение информации о картинке в виде DTO, передача её в OCR_service.py и возврат распознанного текста"""

        # 1. Теперь django_repository (через DjangoClient) возвращает объект DjangoImageDTO
        image_dto = self.django_repository.get_image_info(image_id)

        # 2. Передаем весь DTO-объект целиком в обновленный метод extract_text
        text = self.ocr_service.extract_text(image_dto)

        return text

    # def analyze(self, image_id: int) -> str:
    #     """Получение информации о картинке, передача ссылки в OCR_service.py и возврат распознанного текста"""
    #
    #     image_info = self.django_repository.get_image_info(image_id)
    #     text = self.ocr_service.extract_text(image_info["image"])
    #     # text = self.ocr_service.extract_text(image_info["image_url"])
    #
    #     return text

