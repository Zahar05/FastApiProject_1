from fastapi import APIRouter

from app.schemas.email import (SendEmailRequest, SendEmailResponse)

router = APIRouter(tags=["Email"])

@router.post("/send_message_to_email", response_model=SendEmailResponse)
def send_message_to_email(request: SendEmailRequest):
    return SendEmailResponse(detail=f"Email scheduled for {request.email}")
