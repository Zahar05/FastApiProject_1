from unittest.mock import patch

# from .conftest import client


@patch("app.api.routers.documents.analyze_doc_task.delay")
def test_analyze_doc_success(mock_delay, client):
    mock_delay.return_value.id = "task-123"

    response = client.post("/analyze_doc", json={"image_id": 1, "email": "user@test.com"})

    assert response.status_code == 200

    assert response.json() == {"detail": "Document analysis started", "task_id": "task-123"}

    mock_delay.assert_called_once_with(1, "user@test.com")


def test_analyze_doc_validation_error(client):
    response = client.post("/analyze_doc", json={})

    assert response.status_code == 422
