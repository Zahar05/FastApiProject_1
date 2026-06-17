from unittest.mock import MagicMock, patch
import pytest
from fastapi.testclient import TestClient

# Импортируем наше FastAPI приложение
from app.main import app
from app.dependencies.depend_services import get_service_name

# Создаем тестового клиента FastAPI
client = TestClient(app)


# Фикстура для переопределения зависимости get_service_name
@pytest.fixture(autouse=True)
def override_dependencies():
    # Переопределяем зависимость на тестовую заглушку
    app.dependency_overrides[get_service_name] = lambda: "test_service_name"
    yield
    # Очищаем переопределения после выполнения каждого теста
    app.dependency_overrides.clear()


# =====================================================================
# ТЕСТЫ ДЛЯ РОУТЕРА: app/api/routers/documents.py
# =====================================================================

@patch("app.api.routers.documents.analyze_doc_task.delay")
def test_analyze_doc_success(mock_celery_task):
    """Тест успешного запуска задачи анализа документа."""
    # Настраиваем мок так, чтобы он возвращал объект с id задачи
    mock_task_instance = MagicMock()
    mock_task_instance.id = "test-task-uuid-123"
    mock_celery_task.return_value = mock_task_instance

    # Данные для отправки (соответствуют AnalyzeDocumentRequest)
    payload = {
        "image_id": 123,
        "email": "user@example.com"
    }

    response = client.post("/analyze_doc", json=payload)

    # Проверки статус-кода и схемы ответа (AnalyzeDocumentResponse)
    assert response.status_code == 200
    assert response.json() == {
        "detail": "Document analysis started",
        "task_id": "test-task-uuid-123"
    }

    # Проверяем, что задача Celery была вызвана с нужными аргументами
    mock_celery_task.assert_called_once_with(123, "user@example.com")


def test_analyze_doc_invalid_payload():
    """Тест на валидацию входных данных (переданы неверные поля)."""
    # Передаем пустой словарь (отсутствуют image_id и email)
    payload = {}

    response = client.post("/analyze_doc", json=payload)

    # FastAPI должен вернуть 422 Unprocessable Entity
    assert response.status_code == 422


def test_service_info_success():
    """Тест эндпоинта /service_info с проверкой внедрения зависимостей."""
    response = client.get("/service_info")

    assert response.status_code == 200
    # Проверяем, что вернулось значение из нашей фикстуры-заглушки
    assert response.json() == {
        "service_name": "test_service_name"
    }

# =====================================================================
# ТЕСТЫ ДЛЯ РОУТЕРА: app/api/routers/email.py
# =====================================================================

@patch("app.api.routers.email.send_email_task.delay")
def test_send_message_to_email_success(mock_celery_task):
    """Тест успешного запуска задачи отправки email."""
    # Настраиваем мок для Celery
    mock_task_instance = MagicMock()
    mock_task_instance.id = "email-task-uuid-777"
    mock_celery_task.return_value = mock_task_instance

    # Данные для отправки (соответствуют SendEmailRequest)
    payload = {
        "email": "test@example.com",
        "subject": "Hello Topic",
        "message": "Hello World Body Text"
    }

    response = client.post("/send_message_to_email", json=payload)

    # Проверки
    assert response.status_code == 200
    assert response.json() == {
        "detail": "Email task started: email-task-uuid-777"
    }

    # Проверяем корректность передачи аргументов в Celery
    mock_celery_task.assert_called_once_with(
        "test@example.com",
        "Hello Topic",
        "Hello World Body Text"
    )


def test_send_message_to_email_invalid_payload():
    """Тест валидации для отправки email."""
    # Пропускаем обязательные поля subject и message
    payload = {
        "email": "not-an-email-string"
    }

    response = client.post("/send_message_to_email", json=payload)
    assert response.status_code == 422