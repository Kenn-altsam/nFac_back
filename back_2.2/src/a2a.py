from src.assistant.openai_client import OpenAIAgent
from src.assistant.gemini_client import GeminiAgent

def run_conversation():
    agent1 = OpenAIAgent()
    agent2 = GeminiAgent()

    message = "Привет, что ты думаешь об искусственном интеллекте?"
    print(f"User: {message}")

    for i in range(3):
        reply1 = agent1.chat(message)
        print(f"OpenAI: {reply1}")

        reply2 = agent2.chat(reply1)
        print(f"Gemini: {reply2}")

        message = reply2
