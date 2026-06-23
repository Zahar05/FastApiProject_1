from unittest.mock import Mock, patch

from app.services.task_status_service import TaskStatusService


@patch("app.services.task_status_service.AsyncResult")
def test_get_status_pending(mock_async_result):
    task = Mock()

    task.status = "PENDING"

    task.failed.return_value = False
    task.successful.return_value = False

    mock_async_result.return_value = task

    service = TaskStatusService()

    result = service.get_status("123")

    assert result == {
        "task_id": "123",
        "status": "PENDING",
    }


@patch("app.services.task_status_service.AsyncResult")
def test_get_status_success(mock_async_result):
    task = Mock()

    task.status = "SUCCESS"

    task.failed.return_value = False
    task.successful.return_value = True

    task.result = {
        "status": "success",
        "email": "user@test.com",
    }

    mock_async_result.return_value = task

    service = TaskStatusService()

    result = service.get_status("123")

    assert result == {
        "task_id": "123",
        "status": "SUCCESS",
        "result": str(task.result),
    }


@patch("app.services.task_status_service.AsyncResult")
def test_get_status_failed(mock_async_result):
    task = Mock()

    task.status = "FAILURE"

    task.failed.return_value = True
    task.successful.return_value = False

    task.result = Exception("Something went wrong")

    mock_async_result.return_value = task

    service = TaskStatusService()

    result = service.get_status("123")

    assert result == {
        "task_id": "123",
        "status": "FAILURE",
        "detail": str(task.result),
    }


# Что здесь проверяем
#
# Три ветки твоего метода:
#
# if task.failed():
# elif task.successful():
#
# и случай
#
# PENDING
# STARTED
# RETRY
#
# когда не выполняется ни одна ветка.
