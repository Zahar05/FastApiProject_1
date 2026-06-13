from app.tasks.celery_app import celery_app

from app.services.email_service import EmailService


@celery_app.task
def send_email_task(email: str, subject: str, message: str) -> bool:

    service = EmailService()

    return service.send( email=email, subject=subject, message=message)
