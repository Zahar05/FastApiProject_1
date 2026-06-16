import requests


class DjangoClient:

    def get_image_info(self, image_id: int) -> dict:
        response = requests.get(
            f"http://web:8000/api/images/{image_id}/"
        )
        #     f"http://django_app:8000/api/images/{image_id}/"
        # )

        #     f"http://127.0.0.1:8000/api/images/{image_id}/"
        # )

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
