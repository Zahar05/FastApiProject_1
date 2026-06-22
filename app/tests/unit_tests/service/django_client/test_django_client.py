from unittest.mock import MagicMock, patch
import pytest
import requests

from app.services.django_client import DjangoClient
# Импортируем наш DTO класс для проверки типа
from app.schemas.django_client_dto import DjangoImageDTO


@patch("app.services.django_client.requests.get")
def test_get_image_info_success(mock_get):
    fake_response = MagicMock()

    # Данные должны содержать все обязательные поля DTO и валидный URL в "image"
    fake_response.json.return_value = {
        "id": 1,
        "title": "Test Image",
        "image": "http://django_app:8000/media/images/test.jpg",
        "uploaded_at": "2026-06-22T12:00:00Z"
    }

    mock_get.return_value = fake_response
    client = DjangoClient()
    result = client.get_image_info(1)

    # Теперь проверяем, что вернулся объект DTO, а не сырой словарь
    assert isinstance(result, DjangoImageDTO)
    assert result.id == 1
    assert result.title == "Test Image"
    assert str(result.image_url) == "http://django_app:8000/media/images/test.jpg"

    mock_get.assert_called_once()


@patch("app.services.django_client.requests.get")
def test_get_image_info_http_error(mock_get):
    fake_response = MagicMock()

    fake_response.raise_for_status.side_effect = (
        requests.exceptions.HTTPError("404")
    )

    mock_get.return_value = fake_response
    client = DjangoClient()

    with pytest.raises(requests.exceptions.HTTPError):
        client.get_image_info(1)



# from unittest.mock import MagicMock, patch
#
# import pytest
# import requests
#
# from app.services.django_client import DjangoClient
#
#
# @patch("app.services.django_client.requests.get")
# def test_get_image_info_success(mock_get):
#
#     fake_response = MagicMock()
#
#     fake_response.json.return_value = {
#         "id": 1,
#         "image": "test.jpg",
#     }
#
#     mock_get.return_value = fake_response
#
#     client = DjangoClient()
#
#     result = client.get_image_info(1)
#
#     assert result == {
#         "id": 1,
#         "image": "test.jpg",
#     }
#
#     mock_get.assert_called_once()
#
#
# @patch("app.services.django_client.requests.get")
# def test_get_image_info_http_error(mock_get):
#
#     fake_response = MagicMock()
#
#     fake_response.raise_for_status.side_effect = (
#         requests.exceptions.HTTPError("404")
#     )
#
#     mock_get.return_value = fake_response
#
#     client = DjangoClient()
#
#     with pytest.raises(requests.exceptions.HTTPError):
#         client.get_image_info(1)
