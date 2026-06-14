import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

redis_url = os.getenv("REDIS_URL")

celery_app = Celery(
    "document_analyzer",
    broker=redis_url,
    backend=redis_url,
)

import app.tasks.analyze_doc_task
import app.tasks.send_email_task



# import os
#
# from celery import Celery
# from dotenv import load_dotenv
#
# load_dotenv()
#
# redis_url = os.getenv("REDIS_URL")
#
# celery_app = Celery(
#     "document_analyzer",
#     broker=redis_url,
#     backend=redis_url,
# )

# celery_app.autodiscover_tasks(
#     ["app.tasks"]
# )
# регистрация задач в воркере

# import os
# from celery import Celery
# from dotenv import load_dotenv
#
# load_dotenv()
#
# celery_app = Celery("document_analyzer")
#
# celery_app.conf.result_backend = os.getenv("REDIS_URL")



# celery_app.conf.update(task_always_eager=True)
