class ImageNotFoundException(Exception):
    def __init__(self, image_id: int):
        self.image_id = image_id
        super().__init__(f"Image with id={image_id} not found")


class OCRException(Exception):
    def __init__(self, detail: str):
        self.detail = detail
        super().__init__(detail)


class EmailSendException(Exception):
    def __init__(self, detail: str):
        self.detail = detail
        super().__init__(detail)



# class ImageNotFoundException(Exception):
#     def __init__(self, image_id: int):
#         self.image_id = image_id
#
#
# class OCRException(Exception):
#     def __init__(self, detail: str):
#         self.detail = detail
#
#
# class EmailSendException(Exception):
#     def __init__(self, detail: str):
#         self.detail = detail