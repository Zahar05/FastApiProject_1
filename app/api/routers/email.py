from fastapi import APIRouter
from app.schemas.email import (SendEmailRequest, SendEmailResponse,)
from app.tasks.send_email_task import send_email_task

router = APIRouter(tags=["Email"])

@router.post("/send_message_to_email", response_model=SendEmailResponse)
def send_message_to_email(request: SendEmailRequest):
    task = send_email_task.delay(
        request.email,
        request.subject,
        request.message,
    )

    return SendEmailResponse(detail=f"Email task started: {task.id}")



# from fastapi import APIRouter
#
# from app.schemas.email import (SendEmailRequest, SendEmailResponse)
#
# router = APIRouter(tags=["Email"])
#
# @router.post("/send_message_to_email", response_model=SendEmailResponse)
# def send_message_to_email(request: SendEmailRequest):
#     return SendEmailResponse(detail=f"Email scheduled for {request.email}")
