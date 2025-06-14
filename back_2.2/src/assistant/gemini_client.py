from .base import BaseAgent
import os
import google.generativeai as genai

class GeminiAgent(BaseAgent):
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("❌ GEMINI_API_KEY not found in environment variables.")
        
        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel("gemini-2.0-flash")
        except Exception as e:
            print("❌ Error initializing Gemini:", e)
            raise

    def chat(self, message: str) -> str:
        print("🧠 Sending message to Gemini...")
        response = self.model.generate_content(message)
        print(f"✅ Gemini response received.")
        return response.text.strip()

