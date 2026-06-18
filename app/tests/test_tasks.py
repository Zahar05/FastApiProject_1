# from unittest.mock import MagicMock, patch
# import pytest
#
# # Импортируем саму задачу Celery
# from app.tasks.send_email_task import send_email_task
#
#
# # =====================================================================
# # ТЕСТЫ ДЛЯ ФОНОВОЙ ЗАДАЧИ: app/tasks/send_email_task.py
# # =====================================================================
#
# @patch("app.tasks.send_email_task.EmailService")
# def test_send_email_task_success(mock_email_service_class):
#     """Тест успешного выполнения фоновой задачи отправки email."""
#     # Создаем фейковый экземпляр сервиса и настраиваем успешный возврат
#     mock_service_instance = MagicMock()
#     mock_service_instance.send.return_value = True
#     mock_email_service_class.return_value = mock_service_instance
#
#     # Вызываем задачу Celery напрямую как обычную функцию (без .delay())
#     result = send_email_task(
#         email="task_user@example.com",
#         subject="Task Subject",
#         message="Task Content"
#     )
#
#     # Проверяем возвращаемый словарь при успехе
#     assert result == {
#         "status": "success",
#         "email": "task_user@example.com",
#     }
#
#     # Проверяем, что EmailService был вызван с нужными параметрами
#     mock_email_service_class.assert_called_once()
#     mock_service_instance.send.assert_called_once_with(
#         email="task_user@example.com",
#         subject="Task Subject",
#         message="Task Content"
#     )
#
#
# @patch("app.tasks.send_email_task.EmailService")
# def test_send_email_task_failure(mock_email_service_class):
#     """Тест перехвата ошибки (Exception) внутри задачи Celery."""
#     # Настраиваем мок так, чтобы метод send выбрасывал ошибку
#     mock_service_instance = MagicMock()
#     mock_service_instance.send.side_effect = Exception("SMTP connection timeout")
#     mock_email_service_class.return_value = mock_service_instance
#
#     # Вызываем задачу, ожидая, что она сама обработает ошибку внутри try/except
#     result = send_email_task(
#         email="bad_user@example.com",
#         subject="Fail Subject",
#         message="Fail Content"
#     )
#
#     # Проверяем возвращаемый словарь при ошибке
#     assert result == {
#         "status": "failed",
#         "reason": "SMTP connection timeout",
#     }
#
#     # Проверяем, что вызов метода send действительно состоялся
#     mock_service_instance.send.assert_called_once()
