
import pytest
from pydantic import ValidationError

from search_strategy_agent.models import SearchQuery, SearchStrategyOutput


def test_valid_search_strategy():
    query = SearchQuery(
        query="AI agent engineer jobs Germany",
        purpose="Find relevant job listings",
        priority=1,
    )

    strategy = SearchStrategyOutput(
        interpreted_objective="Find AI agent engineering jobs in Germany",
        information_dimensions=["Job listings", "Required skills"],
        queries=[query],
        source_types=["LinkedIn", "Company career pages"],
        exclusion_criteria=[],
        stopping_conditions=["All relevant sources have been explored"],
        unresolved_ambiguities=[],
    )

    assert strategy.queries[0].priority == 1


def test_invalid_query_priority():
    with pytest.raises(ValidationError):
        SearchQuery(
            query="AI agent engineer jobs",
            purpose="Find jobs",
            priority=0,
        )
