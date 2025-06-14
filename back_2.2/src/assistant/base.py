class BaseAgent:
    def chat(self, message: str) -> str:
        raise NotImplementedError("Agent must implement chat()")
