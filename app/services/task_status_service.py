from celery.result import AsyncResult
from app.tasks.celery_app import celery_app


class TaskStatusService:

    def get_status(self, task_id: str) -> dict:
        task: AsyncResult = AsyncResult(task_id, app=celery_app)
        # task = AsyncResult(task_id, app=celery_app)

        response = {
            "task_id": task_id,
            "status": task.status,
        }

        if task.failed():
            response["detail"] = str(task.result)

        elif task.successful():
            response["result"] = str(task.result)

        # elif task.successful():
        #     response["result"] = task.result

        return response
