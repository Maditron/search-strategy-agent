from typing import Protocol, runtime_checkable

@runtime_checkable
class LLMProvider(Protocol):
    def generate(self, prompt: str) -> str:
        ...