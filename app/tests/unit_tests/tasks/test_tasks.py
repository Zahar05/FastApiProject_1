from unittest.mock import Mock, patch
from app.tasks.send_email_task import send_email_task
from app.tasks.analyze_doc_task import analyze_doc_task


@patch("app.tasks.send_email_task.EmailService")
def test_send_email_task_success(
    mock_email_service,
):
    service = Mock()

    mock_email_service.return_value = service

    result = send_email_task(
        "user@test.com",
        "Hello",
        "Message",
    )

    service.send.assert_called_once_with(
        email="user@test.com",
        subject="Hello",
        message="Message",
    )

    assert result == {
        "status": "success",
        "email": "user@test.com",
    }


@patch("app.tasks.send_email_task.EmailService")
def test_send_email_task_failure(
    mock_email_service,
):
    service = Mock()

    service.send.side_effect = Exception("SMTP error")

    mock_email_service.return_value = service

    result = send_email_task(
        "user@test.com",
        "Hello",
        "Message",
    )

    assert result == {
        "status": "failed",
        "reason": "SMTP error",
    }


@patch("app.tasks.analyze_doc_task.time.sleep")
@patch("app.tasks.analyze_doc_task.build_document_process_service")
def test_analyze_doc_task_success(
    mock_builder,
    mock_sleep,
):
    service = Mock()

    service.process.return_value = "analysis completed"

    mock_builder.return_value = service

    result = analyze_doc_task(
        image_id=1,
        email="user@test.com",
    )

    mock_sleep.assert_called_once_with(10)

    service.process.assert_called_once_with(
        image_id=1,
        email="user@test.com",
    )

    assert result == "analysis completed"
