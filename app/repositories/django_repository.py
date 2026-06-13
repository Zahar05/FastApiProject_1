from app.services.django_client import DjangoClient

class DjangoRepository:
    def __init__(self, django_client: DjangoClient):
        self.django_client = django_client

    def get_image_info(self, image_id: int) -> dict:
        return self.django_client.get_image_info(image_id)


