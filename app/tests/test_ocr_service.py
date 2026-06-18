# from io import BytesIO
# from unittest.mock import MagicMock, patch
# import pytest
# import requests
#
# # ИСПРАВЛЕНО: Исправлен путь импорта (добавлена приставка app.)
# from app.core.exceptions import OCRException
# from app.services.ocr_service import OCRService
#
#
# @pytest.fixture
# def fake_image_content():
#     """Фикстура, создающая минимальный валидный байт-код PNG-картинки для PIL."""
#     from PIL import Image
#     img = Image.new('RGB', (10, 10), color='white')
#     img_byte_arr = BytesIO()
#     img.save(img_byte_arr, format='PNG')
#     return img_byte_arr.getvalue()
#
#
# # =====================================================================
# # ТЕСТЫ ДЛЯ OCRService
# # =====================================================================
#
# @patch("app.services.ocr_service.pytesseract.image_to_string")
# @patch("app.services.ocr_service.requests.get")
# def test_extract_text_success(mock_requests_get, mock_image_to_string, fake_image_content):
#     """Тест успешного скачивания и распознавания текста на изображении."""
#     service = OCRService()
#
#     # 1. Настраиваем мок для requests: возвращаем статус 200 и бинарник фейк-картинки
#     mock_response = MagicMock()
#     mock_response.status_code = 200
#     mock_response.content = fake_image_content
#     mock_requests_get.return_value = mock_response
#
#     # 2. Настраиваем мок для pytesseract: возвращаем ожидаемый текст
#     mock_image_to_string.return_value = "Распознанный тестовый текст"
#
#     # Вызываем целевой метод
#     image_url = "https://example.com"
#     result = service.extract_text(image_url)
#
#     # Проверки
#     assert result == "Распознанный тестовый текст"
#
#     # Проверяем, что скачивание произошло по правильному URL
#     mock_requests_get.assert_called_once_with(image_url)
#
#     # Проверяем, что была вызвана функция raise_for_status()
#     mock_response.raise_for_status.assert_called_once()
#
#     # ИСПРАВЛЕНО: Проверяем именованные аргументы (kwargs) вызова pytesseract
#     mock_image_to_string.assert_called_once()
#     assert mock_image_to_string.call_args.kwargs["lang"] == "rus+eng"
#
#
# @patch("app.services.ocr_service.requests.get")
# def test_extract_text_http_error(mock_requests_get):
#     """Тест поведения при сетевой ошибке (404), когда сервис оборачивает её в OCRException."""
#     service = OCRService()
#
#     # Настраиваем requests так, чтобы raise_for_status выбрасывал HTTPError
#     mock_response = MagicMock()
#     mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error")
#     mock_requests_get.return_value = mock_response
#
#     # Проверяем, что метод выбросит OCRException, а не HTTPError
#     with pytest.raises(OCRException):
#         service.extract_text("https://example.com")
#
#
#
#
#
#
# # from io import BytesIO
# # from unittest.mock import MagicMock, patch
# # import pytest
# # import requests
# #
# # # Импортируем тестируемый сервис
# # from app.services.ocr_service import OCRService
# # from core.exceptions import OCRException
# #
# #
# # @pytest.fixture
# # def fake_image_content():
# #     """Фикстура, создающая минимальный валидный байт-код PNG-картинки для PIL."""
# #     # Пустая белая картинка 10x10 пикселей в памяти
# #     from PIL import Image
# #     img = Image.new('RGB', (10, 10), color='white')
# #     img_byte_arr = BytesIO()
# #     img.save(img_byte_arr, format='PNG')
# #     return img_byte_arr.getvalue()
# #
# #
# # # =====================================================================
# # # ТЕСТЫ ДЛЯ OCRService
# # # =====================================================================
# #
# # @patch("app.services.ocr_service.pytesseract.image_to_string")
# # @patch("app.services.ocr_service.requests.get")
# # def test_extract_text_success(mock_requests_get, mock_image_to_string, fake_image_content):
# #     """Тест успешного скачивания и распознавания текста на изображении."""
# #     service = OCRService()
# #
# #     # 1. Настраиваем мок для requests: возвращаем статус 200 и бинарник фейк-картинки
# #     mock_response = MagicMock()
# #     mock_response.status_code = 200
# #     mock_response.content = fake_image_content
# #     mock_requests_get.return_value = mock_response
# #
# #     # 2. Настраиваем мок для pytesseract: возвращаем ожидаемый текст
# #     mock_image_to_string.return_value = "Распознанный тестовый текст"
# #
# #     # Вызываем целевой метод
# #     image_url = "https://example.com"
# #     result = service.extract_text(image_url)
# #
# #     # Проверки
# #     assert result == "Распознанный тестовый текст"
# #
# #     # Проверяем, что скачивание произошло по правильному URL
# #     mock_requests_get.assert_called_once_with(image_url)
# #
# #     # Проверяем, что была вызвана функция raise_for_status()
# #     mock_response.raise_for_status.assert_called_once()
# #
# #     # Проверяем, что pytesseract запускался с нужными языковыми пакетами
# #     mock_image_to_string.assert_called_once()
# #     assert mock_image_to_string.call_args[1]["lang"] == "rus+eng"
# #
# #
# # @patch("app.services.ocr_service.requests.get")
# # def test_extract_text_http_error(mock_requests_get):
# #     """Тест поведения при сетевой ошибке (404), когда сервис оборачивает её в OCRException."""
# #     service = OCRService()
# #
# #     # Настраиваем requests так, чтобы raise_for_status выбрасывал HTTPError
# #     mock_response = MagicMock()
# #     mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error")
# #     mock_requests_get.return_value = mock_response
# #
# #     # ИСПРАВЛЕНО: Теперь мы ожидаем, что метод выбросит OCRException, а не HTTPError
# #     with pytest.raises(OCRException):
# #         service.extract_text("https://example.com")
#
#
#
#
# # @patch("app.services.ocr_service.requests.get")
# # def test_extract_text_http_error(mock_requests_get):
# #     """Тест поведения при сетевой ошибке (например, картинка не найдена - 404)."""
# #     service = OCRService()
# #
# #     # Настраиваем requests так, чтобы raise_for_status выбрасывал HTTPError
# #     mock_response = MagicMock()
# #     mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error")
# #     mock_requests_get.return_value = mock_response
# #
# #     # Проверяем, что ошибка пробрасывается наверх и ломает выполнение
# #     with pytest.raises(requests.exceptions.HTTPError):
# #         service.extract_text("https://example.com")
