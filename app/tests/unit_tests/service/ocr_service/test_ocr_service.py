from unittest.mock import patch, Mock
import pytest
from app.services.ocr_service import OCRService
from app.core.exceptions import OCRException

# Импортируем DTO, чтобы сконструировать объект для теста
from app.schemas.django_client_dto import DjangoImageDTO


@patch("app.services.ocr_service.pytesseract.image_to_string")
@patch("app.services.ocr_service.Image.open")
@patch("app.services.ocr_service.requests.get")
def test_extract_text_success(
    mock_get,
    mock_image_open,
    mock_ocr,
):
    service = OCRService()

    mock_response = Mock()
    mock_response.content = b"fake-image"
    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    mock_image = Mock()
    mock_image_open.return_value = mock_image

    mock_ocr.return_value = "recognized text"

    # 1. Создаем фейковый объект DTO вместо строки URL
    fake_dto = DjangoImageDTO(
        id=1, title="Test OCR", image="http://example.com/image.jpg", uploaded_at="2026-06-22T12:00:00Z"
    )

    # 2. Передаем DTO в сервис
    result = service.extract_text(fake_dto)

    assert result == "recognized text"
    mock_get.assert_called_once_with("http://example.com/image.jpg", timeout=10)


@patch("app.services.ocr_service.requests.get")
def test_extract_text_http_error(mock_get):
    service = OCRService()

    mock_get.side_effect = Exception("Connection error")

    # Создаем фейковый объект DTO для теста с ошибкой
    fake_dto = DjangoImageDTO(
        id=1, title="Test OCR Error", image="http://example.com/image.jpg", uploaded_at="2026-06-22T12:00:00Z"
    )

    with pytest.raises(OCRException) as exc:
        service.extract_text(fake_dto)

    assert "Connection error" in str(exc.value)


# from unittest.mock import Mock, patch
# import pytest
# from app.core.exceptions import OCRException
# from app.services.ocr_service import OCRService
#
#
# @patch("app.services.ocr_service.pytesseract.image_to_string")
# @patch("app.services.ocr_service.Image.open")
# @patch("app.services.ocr_service.requests.get")
# def test_extract_text_success(
#     mock_get,
#     mock_image_open,
#     mock_ocr,
# ):
#     service = OCRService()
#
#     mock_response = Mock()
#     mock_response.content = b"fake-image"
#     mock_response.raise_for_status.return_value = None
#
#     mock_get.return_value = mock_response
#
#     mock_image = Mock()
#     mock_image_open.return_value = mock_image
#
#     mock_ocr.return_value = "recognized text"
#
#     result = service.extract_text(
#         "http://example.com/image.jpg"
#     )
#
#     assert result == "recognized text"
#
#     mock_get.assert_called_once()
#     mock_response.raise_for_status.assert_called_once()
#
#     mock_image_open.assert_called_once()
#
#     mock_ocr.assert_called_once()
#
#
# @patch("app.services.ocr_service.requests.get")
# def test_extract_text_http_error(mock_get):
#     service = OCRService()
#
#     mock_get.side_effect = Exception("Connection error")
#
#     with pytest.raises(OCRException) as exc:
#         service.extract_text(
#             "http://example.com/image.jpg"
#         )
#
#     assert "Connection error" in str(exc.value)
