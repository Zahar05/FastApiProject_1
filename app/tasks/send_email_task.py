from app.tasks.celery_app import celery_app
from app.services.email_service import EmailService
import logging

logger = logging.getLogger(__name__)

@celery_app.task
def send_email_task(email: str, subject: str, message: str):
    try:
        EmailService().send(email=email, subject=subject, message=message)
        return {
            "status": "success",
            "email": email,
        }

    except Exception as e:
        logger.exception("Email sending failed")
        return {
            "status": "failed",
            "reason": str(e),
        }



# from app.tasks.celery_app import celery_app
#
# from app.services.email_service import EmailService
#
#
# @celery_app.task
# def send_email_task(email: str, subject: str, message: str) -> bool:
#
#     service = EmailService()
#
#     return service.send( email=email, subject=subject, message=message)
