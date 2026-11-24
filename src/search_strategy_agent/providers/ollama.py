
import httpx

from .base import LLMProvider


class OllamaProvider:
    def __init__(
        self,
        model: str = "qwen3.5:latest",
        base_url: str = "http://localhost:11434",
        timeout: float = 300.0,
    ):
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def generate(self, prompt: str) -> str:
        response = httpx.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            },
            timeout=self.timeout,
            trust_env=False,
        )

        response.raise_for_status()

        return response.json()["response"]
