import json

from pydantic import ValidationError

from search_strategy_agent.models import SearchStrategyOutput


class ResponseParsingError(Exception):
    pass


def parse_response(response: str) -> SearchStrategyOutput:
    try:
        data = json.loads(response)
        return SearchStrategyOutput.model_validate(data)

    except (json.JSONDecodeError, ValidationError) as exc:
        raise ResponseParsingError(
            "LLM response could not be parsed into a valid SearchStrategyOutput."
        ) from exc