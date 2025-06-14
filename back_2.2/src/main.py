from fastapi import FastAPI
from src.tasks.fetcher import fetch_daily_data, agent_to_agent_chat

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the A2A AI agents system"}

@app.post("/run-daily")
def run_daily():
    fetch_daily_data.delay()
    return {"status": "fetch task started"}

@app.post("/run-a2a")
def run_a2a():
    agent_to_agent_chat.delay()
    return {"status": "a2a conversation started"}
