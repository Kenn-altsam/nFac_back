from fastapi import FastAPI
from src.api import users  # ✅ путь до users.py
from src import models, database

app = FastAPI()

database.Base.metadata.create_all(bind=database.engine)

app.include_router(users.router)  # ✅ используем router, определённый в users.py
