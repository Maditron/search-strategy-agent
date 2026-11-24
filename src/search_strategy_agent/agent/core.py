
import os

from search_strategy_agent.models import (
    SearchStrategyInput,
    SearchStrategyOutput,
)
from search_strategy_agent.providers import (
    ArvanProvider,
    OllamaProvider,
)

from .parser import parse_response
from .prompt import build_prompt


class SearchStrategyAgent:
    def __init__(self):

        provider_name = os.getenv(
            "SEARCH_STRATEGY_PROVIDER",
            "arvan",
        ).lower()

        if provider_name == "arvan":
            self.provider = ArvanProvider(
                api_key=os.environ["ARVAN_API_KEY"],
                base_url=os.environ["ARVAN_BASE_URL"],
                model=os.getenv("ARVAN_MODEL", "GPT-5"),
            )

        elif provider_name == "ollama":
            self.provider = OllamaProvider(
                model=os.getenv("OLLAMA_MODEL", "qwen3.5:latest"),
                base_url=os.getenv(
                    "OLLAMA_BASE_URL",
                    "http://localhost:11434",
                ),
            )

        else:
            raise ValueError(
                f"Unsupported LLM provider: {provider_name}"
            )

    def run(self, data: SearchStrategyInput) -> SearchStrategyOutput:
        prompt = build_prompt(data)
        response = self.provider.generate(prompt)
        return parse_response(response)
