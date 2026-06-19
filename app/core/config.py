from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    SERVICE_NAME: str = "Сервис Анализа Документов"
    DJANGO_API_URL: str = "http://web:8000"
    REDIS_URL: str
    APP_VERSION: str = "1.0.0"
    CELERY_APP_NAME: str = "document_analyzer"
    OCR_LANGUAGES: str = "rus+eng"

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASSWORD: str
    SENDER_EMAIL: str
    HTTP_TIMEOUT: int = 10
    DJANGO_IMAGES_ENDPOINT: str = "/api/images"


settings = Settings()


# Обычно в config.py кладут:
#
# URL Redis
# URL PostgreSQL
# URL Django API
# SMTP настройки почты
# секретные ключи
# настройки Celery
# параметры OCR
# настройки логирования