from unittest.mock import patch

from app.services.task_status_service import TaskStatusService


@patch.object(TaskStatusService, "get_status")
def test_get_task_status_success(mock_get_status, client):
    mock_get_status.return_value = {"task_id": "abc123", "status": "SUCCESS", "result": "done"}

    response = client.get("/tasks/abc123")

    assert response.status_code == 200

    assert response.json() == {"task_id": "abc123", "status": "SUCCESS", "result": "done"}

    mock_get_status.assert_called_once_with("abc123")
