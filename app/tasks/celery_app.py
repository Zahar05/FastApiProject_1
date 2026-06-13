from celery import Celery

celery_app = Celery(
    "document_analyzer"
)

celery_app.conf.update(
    task_always_eager=True,
)
