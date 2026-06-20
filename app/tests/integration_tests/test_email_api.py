from unittest.mock import patch

# from .conftest import client


@patch("app.api.routers.email.send_email_task.delay")
def test_send_email_success(mock_delay, client):
    mock_delay.return_value.id = "email-task"

    response = client.post(
        "/send_message_to_email",
        json={
            "email": "user@test.com",
            "subject": "Hello",
            "message": "World"
        }
    )

    assert response.status_code == 200

    assert response.json() == {
        "detail": "Email task started: email-task"
    }

    mock_delay.assert_called_once_with(
        "user@test.com",
        "Hello",
        "World"
    )


def test_send_email_validation_error(client):
    response = client.post(
        "/send_message_to_email",
        json={}
    )

    assert response.status_code == 422
