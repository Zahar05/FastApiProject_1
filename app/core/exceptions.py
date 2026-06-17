class ImageNotFoundException(Exception):
    def __init__(self, image_id: int):
        self.image_id = image_id


class OCRException(Exception):
    def __init__(self, detail: str):
        self.detail = detail


class EmailSendException(Exception):
    def __init__(self, detail: str):
        self.detail = detail