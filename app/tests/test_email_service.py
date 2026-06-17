import os
from unittest.mock import MagicMock, patch
import pytest
import smtplib

# Импортируем сам сервис
from app.services.email_service import EmailService


@pytest.fixture(autouse=True)
def mock_env_variables():
    """Фикстура для принудительной установки переменных окружения на время тестов."""
    with patch.dict(os.environ, {
        "SMTP_HOST": "://test.com",
        "SMTP_PORT": "587",
        "SMTP_USER": "test_user",
        "SMTP_PASSWORD": "test_password",
        "SENDER_EMAIL": "noreply@test.com"
    }):
        yield


def test_send_email_success():
    """Тест успешной отправки email с проверкой вызова всех SMTP методов."""
    service = EmailService()

    # Мокаем контекстный менеджер smtplib.SMTP
    with patch("smtplib.SMTP") as mock_smtp_class:
        # Создаем фейковый экземпляр сервера, который возвращает контекстный менеджер
        mock_server = MagicMock()
        mock_smtp_class.return_value.__enter__.return_value = mock_server

        # Вызываем тестируемый метод
        result = service.send(
            email="recipient@example.com",
            subject="Test Subject",
            message="Test Message Body"
        )

        # Проверяем, что метод вернул True
        assert result is True

        # Проверяем, что SMTP клиент инициализировался с правильными параметрами из env
        mock_smtp_class.assert_called_once_with("://test.com", 587)

        # Проверяем вызовы обязательных методов отправки внутри контекста
        mock_server.starttls.assert_called_once()
        mock_server.login.assert_called_once_with("test_user", "test_password")

        # Проверяем, что сообщение было отправлено
        mock_server.send_message.assert_called_once()

        # Дополнительно проверим, правильно ли сформировалось EmailMessage
        called_msg = mock_server.send_message.call_args[0][0]
        assert called_msg["Subject"] == "Test Subject"
        assert called_msg["From"] == "noreply@test.com"
        assert called_msg["To"] == "recipient@example.com"


def test_send_email_smtp_exception():
    """Тест поведения сервиса, если SMTP сервер выбросит ошибку (например, неверный пароль)."""
    service = EmailService()

    with patch("smtplib.SMTP") as mock_smtp_class:
        mock_server = MagicMock()
        # Настраиваем метод login так, чтобы он вызывал исключение аутентификации
        mock_server.login.side_effect = smtplib.SMTPAuthenticationError(535, "Authentication failed")
        mock_smtp_class.return_value.__enter__.return_value = mock_server

        # Проверяем, падает ли приложение с ошибкой (или обрабатывает её)
        # Так как в исходном коде нет блока try/except, ошибка должна проброситься наверх
        with pytest.raises(smtplib.SMTPAuthenticationError):
            service.send(
                email="recipient@example.com",
                subject="Test Subject",
                message="Test Message Body"
            )
