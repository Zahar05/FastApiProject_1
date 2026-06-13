import requests


class DjangoClient:
    def get_image_info(self, image_id: int) -> dict:
        """
        Временная заглушка.
        Позже будет запрос в Django API.
        """

        return {
            "id": image_id,
            "title": f"image_{image_id}",
            "image_url": f"http://django:8000/media/{image_id}.jpg",
        }
