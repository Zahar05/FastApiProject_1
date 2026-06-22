# import requests
# from app.core.config import settings
# from app.schemas.django_client_dto import DjangoImageDTO
#
#
# class DjangoClient:
#
#     def get_image_info(self, image_id: int) -> DjangoImageDTO:
#         """Получает данные о картинке из Django и возвращает валидированный DTO"""
#         response = requests.get(
#             f"{settings.DJANGO_API_URL}{settings.DJANGO_IMAGES_ENDPOINT}/{image_id}/",
#             timeout=settings.HTTP_TIMEOUT,
#         )
#
#         response.raise_for_status()
#
#         # Метод model_validate автоматически сопоставит ключ "image" с полем image_url
#         return DjangoImageDTO.model_validate(response.json())





import requests
from app.core.config import settings


class DjangoClient:

    def get_image_info(self, image_id: int) -> dict:
        '''Получение информации о картинке'''
        response = requests.get(
            f"{settings.DJANGO_API_URL}{settings.DJANGO_IMAGES_ENDPOINT}/{image_id}/",
            timeout=settings.HTTP_TIMEOUT,
        )

        response.raise_for_status()

        return response.json()




# import requests
#
#
# class DjangoClient:
#     def get_image_info(self, image_id: int) -> dict:
#         """
#         Временная заглушка.
#         Позже будет запрос в Django API.
#         """
#
#         return {
#             "id": image_id,
#             "title": f"image_{image_id}",
#             "image_url": f"http://django:8000/media/{image_id}.jpg",
#         }
