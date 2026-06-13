import requests
from io import BytesIO
from PIL import Image
import pytesseract


class OCRService:
    def extract_text(self, image_path: str) -> str:
        response = requests.get(image_path)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))

        return pytesseract.image_to_string(image, lang="rus+eng")



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