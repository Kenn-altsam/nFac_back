from celery import Celery
from celery.schedules import crontab

app = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    include=["src.tasks.fetch_data"]
)

app.conf.beat_schedule = {
    "daily-fetch-data": {
        "task": "src.tasks.fetch_data.fetch_and_save",
        "schedule": crontab(hour=0, minute=0),  # every day at midnight UTC
    },
}
