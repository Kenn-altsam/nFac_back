from src.celery_app import celery
from src.a2a import run_conversation

@celery.task
def fetch_daily_data():
    # Заглушка под ежедневный парсинг
    print("Fetching daily data...")

@celery.task
def agent_to_agent_chat():
    run_conversation()
