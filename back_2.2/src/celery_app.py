from celery_app import Celery
import os

celery = Celery(
    __name__,
    broker=os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0")
)

celery.autodiscover_tasks(['src.tasks'])

# ⏰ Периодическая задача (если используешь beat)
from celery.schedules import crontab
celery.conf.beat_schedule = {
    "daily-fetch": {
        "task": "src.tasks.fetcher.fetch_daily_data",
        "schedule": crontab(hour=9, minute=0),
    },
}
