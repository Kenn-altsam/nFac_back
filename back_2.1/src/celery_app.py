from celery import Celery
from src import tasks

celery_app = Celery(
    "nfac",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",  # Можно убрать backend, если не нужен результат
)

celery_app.conf.timezone = "UTC"
celery_app.conf.beat_schedule = {
    "print-every-10-seconds": {
        "task": "src.tasks.print_hello",
        "schedule": 10.0,  # каждые 10 секунд
    },
}