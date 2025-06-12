from celery import Celery

celery_app = Celery(
    "nfac",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)
celery_app.conf.timezone = "UTC"

# Autodiscover tasks in the 'src' package
celery_app.autodiscover_tasks(['src'])