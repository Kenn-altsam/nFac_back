from fastapi import FastAPI
from src.api import users  # ✅ путь до users.py
from src import models, database
from fastapi import FastAPI
from .tasks import print_hello

app = FastAPI()

database.Base.metadata.create_all(bind=database.engine)

app.include_router(users.router)  # ✅ используем router, определённый в users.py

@app.get("/run-task/")
def run_task():
    result = print_hello.delay()
    return {"task_id": result.id}
