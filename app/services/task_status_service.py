from celery.result import AsyncResult
from app.tasks.celery_app import celery_app


class TaskStatusService:

    def get_status(self, task_id: str) -> dict:
        task = AsyncResult(task_id, app=celery_app)
        return {
            "task_id": task_id,
            "status": task.status,
            "result": task.result,
        }



# from celery.result import AsyncResult
#
#
# class TaskStatusService:
#
#     def get_status(self, task_id: str) -> dict:
#
#         task = AsyncResult(task_id)
#
#         return {
#             "task_id": task_id,
#             "status": task.status,
#             "result": task.result,
#         }
