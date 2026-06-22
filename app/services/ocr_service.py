import requests
from io import BytesIO
from PIL import Image
import pytesseract
from app.core.exceptions import OCRException
from app.core.config import settings
# Инициализируем импорт DTO для явного указания типа данных
from app.schemas.django_client_dto import DjangoImageDTO


class OCRService:
    # 1. Изменяем аргумент: вместо image_path: str принимаем image_data: DjangoImageDTO
    def extract_text(self, image_data: DjangoImageDTO) -> str:
        try:
            # 2. Преобразуем объект HttpUrl в строку для requests.get
            url_str = str(image_data.image_url)

            response = requests.get(url_str, timeout=settings.HTTP_TIMEOUT)
            response.raise_for_status()

            image = Image.open(BytesIO(response.content))

            return pytesseract.image_to_string(
                image,
                lang=settings.OCR_LANGUAGES
            )

        except Exception as e:
            raise OCRException(str(e))





# import requests
# from io import BytesIO
# from PIL import Image
# import pytesseract
# from app.core.exceptions import OCRException
# from app.core.config import settings
#
#
# class OCRService:
#     def extract_text(self, image_path: str) -> str:
#         try:
#             response = requests.get(image_path, timeout=settings.HTTP_TIMEOUT)
#             response.raise_for_status()
#
#             image = Image.open(BytesIO(response.content))
#
#             return pytesseract.image_to_string(
#                 image,
#                 lang=settings.OCR_LANGUAGES
#             )
#
#         except Exception as e:
#             raise OCRException(str(e))






# class OCRService:
#     def extract_text(self, image_path: str) -> str:
#         response = requests.get(image_path)
#         response.raise_for_status()
#         image = Image.open(BytesIO(response.content))
#
#         return pytesseract.image_to_string(image, lang="rus+eng")





# from PIL import Image
# import pytesseract
#
# class OCRService:
#
#     def extract_text(self, image_path: str) -> str:
#         return pytesseract.image_to_string(Image.open(image_path), lang="rus+eng")



# class OCRService: после поключения Джанго
#
#     def extract_text(self, image_path: str) -> str:
#         image = Image.open(image_path)
#         text = pytesseract.image_to_string(image, lang="eng")
#         return text



# class OCRService:
#     def extract_text(self, image_path: str) -> str:
#         """
#         Временная заглушка.
#         Позже здесь будет pytesseract.
#         """
#         return f"OCR text from {image_path}"