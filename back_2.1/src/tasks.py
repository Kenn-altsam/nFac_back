from .celery_app import celery_app

@celery_app.task
def print_hello():
    print("Hello from Celery!")
    return "Hello!"