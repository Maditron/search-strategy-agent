
import os

import uvicorn
from dotenv import load_dotenv
from starlette.applications import Starlette

from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.routes import (
    create_agent_card_routes,
    create_jsonrpc_routes,
)
from a2a.server.tasks import InMemoryTaskStore

from .agent_card import build_agent_card
from .executor import SearchStrategyAgentExecutor


def create_app(host: str, port: int) -> Starlette:
    base_url = f"http://{host}:{port}"
    agent_card = build_agent_card(base_url)

    request_handler = DefaultRequestHandler(
        agent_executor=SearchStrategyAgentExecutor(),
        task_store=InMemoryTaskStore(),
        agent_card=agent_card,
    )

    routes = [
        *create_agent_card_routes(agent_card),
        *create_jsonrpc_routes(request_handler, "/"),
    ]

    return Starlette(routes=routes)


def main() -> None:
    load_dotenv()

    host = os.getenv("SEARCH_STRATEGY_HOST", "127.0.0.1")
    port = int(os.getenv("SEARCH_STRATEGY_PORT", "9999"))

    app = create_app(host, port)
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
