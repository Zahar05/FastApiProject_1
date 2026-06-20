from unittest.mock import Mock, patch

import pytest

from app.core.exceptions import OCRException
from app.services.ocr_service import OCRService


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

    result = service.extract_text(
        "http://example.com/image.jpg"
    )

    assert result == "recognized text"

    mock_get.assert_called_once()
    mock_response.raise_for_status.assert_called_once()

    mock_image_open.assert_called_once()

    mock_ocr.assert_called_once()


@patch("app.services.ocr_service.requests.get")
def test_extract_text_http_error(mock_get):
    service = OCRService()

    mock_get.side_effect = Exception("Connection error")

    with pytest.raises(OCRException) as exc:
        service.extract_text(
            "http://example.com/image.jpg"
        )

    assert "Connection error" in str(exc.value)



# уже полностью в актуальном виде под твою текущую архитектуру, чтобы их можно было просто скопировать и запускать через:
# pytest app/tests/unit_tests -v
#
# Что здесь проверяем
# test_extract_text_success
#
# Проверяем весь happy path:
#
# requests.get()
# ↓
# Image.open()
# ↓
# pytesseract.image_to_string()
# ↓
# вернулся текст
# test_extract_text_http_error
#
# Проверяем блок:
#
# except Exception as e:
#     raise OCRException(str(e))
#
# То есть любое исключение должно превратиться в OCRException.