from app.services.django_client import DjangoClient
from app.schemas.django_client_dto import DjangoImageDTO


class DjangoRepository:
    def __init__(self, django_client: DjangoClient):
        self.django_client = django_client

    def get_image_info(self, image_id: int) -> DjangoImageDTO:
        return self.django_client.get_image_info(image_id)
