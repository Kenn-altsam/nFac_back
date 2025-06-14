from celery import Celery
import os

celeryy = Celery(
    __name__,
    broker=os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0")
)

celeryy.autodiscover_tasks(['src.tasks'])

from celery.schedules import crontab
celeryy.conf.beat_schedule = {
    "daily-fetch": {
        "task": "src.tasks.fetcher.fetch_daily_data",
        "schedule": crontab(hour=9, minute=0),
    },
}
