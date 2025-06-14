from .base import BaseAgent
import openai
import os
from src.config import OPENAI_API_KEY

class OpenAIAgent(BaseAgent):
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def chat(self, message: str) -> str:
        print("🧠 Sending message to OpenAI...")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message}]
        )
        answer = response.choices[0].message.content.strip()
        print(f"✅ OpenAI response received.")
        return answer
