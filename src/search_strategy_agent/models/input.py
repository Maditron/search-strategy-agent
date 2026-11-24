from pydantic import BaseModel, ConfigDict, Field


class SearchStrategyInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    objective: str = Field(min_length=1)
    context: str | None = None
    constraints: list[str] = Field(default_factory=list)
    preferred_source_types: list[str] = Field(default_factory=list)
    freshness_requirement: str | None = None