from celery import Celery
import os

celery = Celery(
    __name__,
    broker=os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0")
)

celery.autodiscover_tasks(['src.tasks'])
celery.config_from_object('src.celeryconfig')