from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime

class DjangoImageDTO(BaseModel):
    id: int
    title: str
    image_url: HttpUrl = Field(..., alias="image")  # Забирает ключ "image" и проверяет как URL
    uploaded_at: datetime

    model_config = {
        "populate_by_name": True  # Позволяет обращаться и по .image_url, и создавать через 'image'
    }
