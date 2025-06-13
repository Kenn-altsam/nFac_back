import requests
from celery import shared_task
from sqlalchemy.orm import Session
from src.database import SessionLocal
from src.models.data import WebsiteData

@shared_task
def fetch_and_save():
    # 1) fetch
    resp = requests.get("https://example.com/data.json")
    resp.raise_for_status()
    items = resp.json()

    # 2) save to DB
    db: Session = SessionLocal()
    try:
        for item in items:
            db_obj = WebsiteData(**item)
            db.add(db_obj)
        db.commit()
    finally:
        db.close()
