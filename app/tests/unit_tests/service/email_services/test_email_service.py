from unittest.mock import MagicMock, patch

import pytest
import smtplib

from app.services.email_service import EmailService


@patch("smtplib.SMTP")
def test_send_email_success(mock_smtp):

    fake_server = MagicMock()

    mock_smtp.return_value.__enter__.return_value = (
        fake_server
    )

    service = EmailService()

    result = service.send(
        email="user@test.com",
        subject="Hello",
        message="Test message",
    )

    assert result is True

    fake_server.starttls.assert_called_once()

    fake_server.login.assert_called_once()

    fake_server.send_message.assert_called_once()


@patch("smtplib.SMTP")
def test_send_email_auth_error(mock_smtp):

    fake_server = MagicMock()

    fake_server.login.side_effect = (
        smtplib.SMTPAuthenticationError(
            535,
            b"auth failed",
        )
    )

    mock_smtp.return_value.__enter__.return_value = (
        fake_server
    )

    service = EmailService()

    with pytest.raises(
        smtplib.SMTPAuthenticationError
    ):
        service.send(
            email="user@test.com",
            subject="Hello",
            message="Test message",
        )