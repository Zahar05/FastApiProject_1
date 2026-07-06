from unittest.mock import Mock
import pytest
from app.core.exceptions import ImageNotFoundException, OCRException
from app.services.document_analyze_service import DocumentAnalyzeService

# Импортируем DTO, чтобы создать фейковый объект для тестов
from app.schemas.django_client_dto import DjangoImageDTO


def test_analyze_success():
    """Тест успешного анализа метода analyze с использованием DTO"""
    django_repository = Mock()
    ocr_service = Mock()

    # Создаем фейковый DTO-объект, который как будто вернул репозиторий
    fake_dto = DjangoImageDTO(
        id=1,
        title="Test Doc",
        image="http://fake-image-url.com",
        uploaded_at="2026-06-22T12:00:00Z",
    )
    django_repository.get_image_info.return_value = fake_dto
    ocr_service.extract_text.return_value = "Passport number 123456"

    service = DocumentAnalyzeService(django_repository, ocr_service)
    result = service.analyze(1)

    django_repository.get_image_info.assert_called_once_with(1)
    # ГЛАВНОЕ: проверяем, что в OCR передается сам объект DTO целиком
    ocr_service.extract_text.assert_called_once_with(fake_dto)
    assert result == "Passport number 123456"


def test_analyze_image_not_found():
    """Тест в случае ошибки метода get_image_info"""
    django_repository = Mock()
    ocr_service = Mock()

    django_repository.get_image_info.side_effect = ImageNotFoundException(1)

    service = DocumentAnalyzeService(django_repository, ocr_service)

    with pytest.raises(ImageNotFoundException):
        service.analyze(1)

    django_repository.get_image_info.assert_called_once_with(1)
    ocr_service.extract_text.assert_not_called()


def test_analyze_ocr_failed():
    """Тест в случае ошибки метода ocr_service.extract_text"""
    django_repository = Mock()
    ocr_service = Mock()

    fake_dto = DjangoImageDTO(
        id=1,
        title="Test Doc",
        image="http://fake-image-url.com",
        uploaded_at="2026-06-22T12:00:00Z",
    )
    django_repository.get_image_info.return_value = fake_dto
    ocr_service.extract_text.side_effect = OCRException("OCR failed")

    service = DocumentAnalyzeService(django_repository, ocr_service)

    with pytest.raises(OCRException):
        service.analyze(1)

    django_repository.get_image_info.assert_called_once_with(1)
    # Проверяем, что в OCR ушел именно наш DTO объект
    ocr_service.extract_text.assert_called_once_with(fake_dto)


# from unittest.mock import Mock
# import pytest
# from app.core.exceptions import ImageNotFoundException, OCRException
# from app.services.document_analyze_service import DocumentAnalyzeService
#
#
# def test_analyze_success():
#     """Тест успешного сценария метода analyze"""
#     django_repository = Mock()
#     ocr_service = Mock()
#
#     django_repository.get_image_info.return_value = {
#         "image": "http://fake-image-url"
#     }
#     ocr_service.extract_text.return_value = "Passport number 123456"
#
#     service = DocumentAnalyzeService(django_repository, ocr_service)
#     result = service.analyze(1)
#
#     django_repository.get_image_info.assert_called_once_with(1)
#     ocr_service.extract_text.assert_called_once_with("http://fake-image-url")
#     assert result == "Passport number 123456"
#
#
# def test_analyze_image_not_found():
#     """Тест в случае падения метода get_image_info"""
#     django_repository = Mock()
#     ocr_service = Mock()
#
#     django_repository.get_image_info.side_effect = ImageNotFoundException(1)
#
#     service = DocumentAnalyzeService(django_repository, ocr_service)
#
#     # pytest.raises корректно перехватит ошибку, и код пойдет дальше
#     with pytest.raises(ImageNotFoundException):
#         service.analyze(1)
#
#     # Теперь эти проверки гарантированно выполнятся
#     django_repository.get_image_info.assert_called_once_with(1)
#     ocr_service.extract_text.assert_not_called()
#
#
# def test_analyze_ocr_failed():  # Исправлено имя функции
#     """Тест в случае ошибки метода ocr_service.extract_text"""
#     django_repository = Mock()
#     ocr_service = Mock()
#
#     django_repository.get_image_info.return_value = {
#         "image": "http://fake-image-url"
#     }
#     ocr_service.extract_text.side_effect = OCRException("OCR failed")
#
#     service = DocumentAnalyzeService(django_repository, ocr_service)
#
#     with pytest.raises(OCRException):
#         service.analyze(1)
#
#     django_repository.get_image_info.assert_called_once_with(1)
#     ocr_service.extract_text.assert_called_once_with("http://fake-image-url")
