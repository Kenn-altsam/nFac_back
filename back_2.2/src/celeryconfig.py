from celery.schedules import crontab

beat_schedule = {
    "daily-fetch": {
        "task": "src.tasks.fetcher.fetch_daily_data",
        "schedule": crontab(hour=9, minute=0),
    },
}
