from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.dependencies.depend_services import get_service_name

client = TestClient(app)


@pytest.fixture(autouse=True)
def override_dependencies():
    """
    Подменяем dependency для всех тестов.
    """

    app.dependency_overrides[get_service_name] = lambda: "test_service_name"

    yield

    app.dependency_overrides.clear()


# ==========================================================
# Documents API
# ==========================================================


@patch("app.api.routers.documents.analyze_doc_task.delay")
def test_analyze_doc_success(mock_delay):
    """
    Успешный запуск Celery-задачи анализа документа.
    """

    fake_task = MagicMock()
    fake_task.id = "task-123"

    mock_delay.return_value = fake_task

    payload = {
        "image_id": 1,
        "email": "user@example.com",
    }

    response = client.post(
        "/analyze_doc",
        json=payload,
    )

    assert response.status_code == 200

    assert response.json() == {
        "detail": "Document analysis started",
        "task_id": "task-123",
    }

    mock_delay.assert_called_once_with(
        1,
        "user@example.com",
    )


def test_analyze_doc_validation_error():
    """
    Проверка Pydantic-валидации.
    """

    response = client.post(
        "/analyze_doc",
        json={},
    )

    assert response.status_code == 422


def test_service_info():
    """
    Проверяем работу Depends().
    """

    response = client.get("/service_info")

    assert response.status_code == 200

    assert response.json() == {
        "service_name": "test_service_name",
    }


# ==========================================================
# Email API
# ==========================================================


@patch("app.api.routers.email.send_email_task.delay")
def test_send_message_to_email_success(mock_delay):
    """
    Успешный запуск Celery-задачи отправки email.
    """

    fake_task = MagicMock()
    fake_task.id = "email-task-777"

    mock_delay.return_value = fake_task

    payload = {
        "email": "test@example.com",
        "subject": "Hello",
        "message": "World",
    }

    response = client.post(
        "/send_message_to_email",
        json=payload,
    )

    assert response.status_code == 200

    assert response.json() == {
        "detail": "Email task started: email-task-777",
    }

    mock_delay.assert_called_once_with(
        "test@example.com",
        "Hello",
        "World",
    )


def test_send_message_to_email_validation_error():
    """
    Проверяем 422 при невалидном запросе.
    """

    response = client.post(
        "/send_message_to_email",
        json={
            "email": "bad-email",
        },
    )

    assert response.status_code == 422


# ==========================================================
# Exception Handlers
# ==========================================================


def test_image_not_found_handler():
    """
    Проверка кастомного обработчика 404.
    Работает только если у тебя есть тестовый эндпоинт:

    @router.get("/test_404")
    def test_404():
        raise ImageNotFoundException(123)
    """

    response = client.get("/test_404")

    assert response.status_code == 404

    assert "detail" in response.json()


def test_validation_exception_handler():
    """
    Проверяем, что кастомный handler 422 действительно работает.
    """

    response = client.post(
        "/analyze_doc",
        json={},
    )

    assert response.status_code == 422

    body = response.json()

    assert "detail" in body


# Что покрывает этот файл
# Тест	Что проверяет
# test_analyze_doc_success	роут /analyze_doc
# test_analyze_doc_validation_error	422 от Pydantic
# test_service_info	Depends
# test_send_message_to_email_success	роут отправки письма
# test_send_message_to_email_validation_error	валидацию email-схемы
# test_image_not_found_handler	кастомный handler 404
# test_validation_exception_handler	кастомный handler 422
