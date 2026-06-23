import smtplib
from email.message import EmailMessage
from app.core.config import settings


class EmailService:

    def send(self, email: str, subject: str, message: str) -> bool:

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = settings.SENDER_EMAIL
        msg["To"] = email
        msg.set_content(message)

        with smtplib.SMTP(
            settings.SMTP_HOST,
            settings.SMTP_PORT,
        ) as server:
            server.starttls()
            server.login(
                settings.SMTP_USER,
                settings.SMTP_PASSWORD,
            )
            server.send_message(msg)

        return True


# class EmailService:
#
#     def send(self, email: str, subject: str, message: str) -> bool:
#
#         smtp_host = os.getenv("SMTP_HOST")
#         smtp_port = int(os.getenv("SMTP_PORT"))
#         smtp_user = os.getenv("SMTP_USER")
#         smtp_password = os.getenv("SMTP_PASSWORD")
#         sender_email = os.getenv("SENDER_EMAIL")
#
#         # smtp_host = os.getenv("SMTP_HOST")
#         # smtp_port = int(os.getenv("SMTP_PORT"))
#         # smtp_user = os.getenv("SMTP_USER")
#         # smtp_password = os.getenv("SMTP_PASSWORD")
#         # sender_email = os.getenv("SENDER_EMAIL")
#
#         msg = EmailMessage()
#         msg["Subject"] = subject
#         msg["From"] = settings.SENDER_EMAIL
#         msg["To"] = email
#         msg.set_content(message)
#
#         with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
#             server.starttls()
#             server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
#             server.send_message(msg)
#
#         return True
#


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
