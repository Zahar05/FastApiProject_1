class EmailService:
    def send(
        self,
        email: str,
        subject: str,
        message: str,
    ) -> bool:
        print(
            f"Send email to={email}, "
            f"subject={subject}"
        )

        return True