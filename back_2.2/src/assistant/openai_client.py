from .base import BaseAgent
import openai
import os

class OpenAIAgent(BaseAgent):
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def chat(self, message: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content
