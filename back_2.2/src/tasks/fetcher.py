from src.celery_app import celeryy  # ✅ правильный импорт
import requests
from datetime import datetime
from src.db import SessionLocal
from src.models import AILog


@celeryy.task
def fetch_daily_data():
    try:
        print("📦 Fetching products from fakestoreapi.com ...")
        response = requests.get("https://fakestoreapi.com/products")
        products = response.json()

        db = SessionLocal()
        log = AILog(
            agent_name="fakestore_scraper",
            input_text="https://fakestoreapi.com/products",
            output_text=str(products),
            timestamp=datetime.utcnow()
        )
        db.add(log)
        db.commit()
        db.close()

        print(f"✅ Saved {len(products)} products to DB.")
    except Exception as e:
        print("❌ Error fetching data:", e)
