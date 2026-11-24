import httpx

from .base import LLMProvider


class ArvanProvider:
    def __init__(
        self,
        api_key: str,
        base_url: str,
        model: str = "GPT-5",
        timeout: float = 120.0,
    ):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout

    def generate(self, prompt: str) -> str:
        response = httpx.post(
            f"{self.base_url}/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": self.model,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
            },
            timeout=self.timeout,
            trust_env=False,
        )

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]