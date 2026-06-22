from app.core.exceptions import (
    ImageNotFoundException,
    OCRException,
    EmailSendException,
)


def test_image_not_found_exception():

    exc = ImageNotFoundException(123)

    assert exc.image_id == 123
    assert str(exc) == "Image with id=123 not found"


def test_ocr_exception():

    exc = OCRException("OCR failed")

    assert exc.detail == "OCR failed"
    assert str(exc) == "OCR failed"


def test_email_send_exception():

    exc = EmailSendException("Email failed")

    assert exc.detail == "Email failed"
    assert str(exc) == "Email failed"


# Что здесь проверяется
#
# Для:
#
# exc = ImageNotFoundException(123)
#
# проверяем две вещи:
#
# assert exc.image_id == 123
#
# атрибут сохранился.
#
# И:
#
# assert str(exc) == "Image with id=123 not found"
#
# текст ошибки формируется правильно.
#
# Запуск
# pytest app/tests/unit_tests/test_exceptions.py -v
#
# Ожидаемый результат:
#
# test_image_not_found_exception PASSED
# test_ocr_exception PASSED
# test_email_send_exception PASSED