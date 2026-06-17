from fastapi import APIRouter
from app.services.task_status_service import TaskStatusService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/{task_id}")
def get_task_status(task_id: str):

    service = TaskStatusService()

    return service.get_status(task_id)
