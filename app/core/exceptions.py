class ImageNotFoundException(Exception):
    def __init__(self, image_id: int):
        self.image_id = image_id


class OCRException(Exception):
    pass


class EmailSendException(Exception):
    pass