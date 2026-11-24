from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentInterface,
    AgentSkill,
)


def build_agent_card(base_url: str) -> AgentCard:
    skill = AgentSkill(
        id="design-search-strategy",
        name="Search Strategy Design",
        description=(
            "Transforms an information need and its constraints "
            "into a structured, prioritized, actionable search strategy. "
            "Does not execute searches or retrieve information."
        ),
        tags=[
            "search-strategy",
            "research-planning",
            "query-design",
        ],
        examples=[
            "Design a search strategy for researching "
            "local-first AI agent architectures."
        ],
        input_modes=["application/json"],
        output_modes=["application/json"],
    )

    return AgentCard(
        name="Search Strategy Agent",
        description=(
            "An autonomous agent that designs structured and "
            "prioritized search strategies from information needs."
        ),
        version="0.1.0",
        supported_interfaces=[
            AgentInterface(
                url=f"{base_url.rstrip('/')}/",
                protocol_binding="JSONRPC",
                protocol_version="1.0",
            )
        ],
        capabilities=AgentCapabilities(
            streaming=False,
            push_notifications=False,
        ),
        default_input_modes=["application/json"],
        default_output_modes=["application/json"],
        skills=[skill],
    )
