
from pydantic import BaseModel, ConfigDict, Field


class SearchQuery(BaseModel):
    model_config = ConfigDict(extra="forbid")

    query: str = Field(min_length=1)
    purpose: str = Field(min_length=1)
    priority: int = Field(ge=1)


class SearchStrategyOutput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    interpreted_objective: str = Field(min_length=1)
    information_dimensions: list[str]
    queries: list[SearchQuery]
    source_types: list[str]
    freshness_filter: str | None = None
    exclusion_criteria: list[str]
    stopping_conditions: list[str]
    unresolved_ambiguities: list[str]
