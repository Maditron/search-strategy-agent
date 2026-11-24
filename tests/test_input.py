import pytest
from pydantic import ValidationError

from search_strategy_agent.models.input import SearchStrategyInput


def test_valid_input_with_defaults():
    data = SearchStrategyInput(objective="Find AI engineering jobs")

    assert data.max_queries == 5
    assert data.constraints == []
    assert data.preferred_source_types == []


def test_invalid_input_is_rejected():
    with pytest.raises(ValidationError):
        SearchStrategyInput(objective="", max_queries=0)


def test_unexpected_fields_are_rejected():
    with pytest.raises(ValidationError):
        SearchStrategyInput(
            objective="Find AI engineering jobs",
            unknown_field="unexpected",
        )
