from .base import BaseAgent
import os
from google import genai

class GeminiAgent(BaseAgent):
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-pro")

    def chat(self, message: str) -> str:
        response = self.model.generate_content(message)
        return response.text
