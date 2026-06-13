import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

class EmailService:

    def send(self, email: str, subject: str, message: str) -> bool:

        smtp_host = os.getenv("SMTP_HOST")
        smtp_port = int(os.getenv("SMTP_PORT"))
        smtp_user = os.getenv("SMTP_USER")
        smtp_password = os.getenv("SMTP_PASSWORD")
        sender_email = os.getenv("SENDER_EMAIL")

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = email
        msg.set_content(message)

        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)

        return True



# class EmailService:
#     def send(self, email: str, subject: str, message: str) -> bool:
#
#         print(
#             f"Send email to={email}\n"
#             f"Subject: {subject}\n"
#             f"Message:\n{message}"
#         )
#         return True


# class EmailService:
#     def send(self, email: str, subject: str) -> bool:
#         print(
#             f"Send email to={email}, "
#             f"subject={subject}"
#         )
#
#         return True