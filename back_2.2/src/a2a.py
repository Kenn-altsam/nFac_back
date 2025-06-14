from assistant.openai_client import OpenAIAgent
from assistant.gemini_client import GeminiAgent
from dotenv import load_dotenv

load_dotenv()

def run_conversation():
    agent1 = OpenAIAgent()
    agent2 = GeminiAgent()

    message = input("Enter your message: ")
    print(f"User: {message}")

    for i in range(3):
        reply1 = agent1.chat(message)
        print(f"OpenAI: {reply1}")

        reply2 = agent2.chat(reply1)
        print(f"Gemini: {reply2}")

        message = reply2

if __name__ == "__main__":
    run_conversation()