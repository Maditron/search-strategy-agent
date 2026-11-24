# Search Strategy Agent

An independent agent that transforms information needs into structured, relevant, prioritized, and actionable search strategies.

**Version:** 0.1.0
**Protocol:** A2A 1.0

## Responsibility

Given an information objective and its constraints, the agent:

- Interprets the information need.
- Identifies distinct research dimensions.
- Designs complementary search queries.
- Prioritizes queries by expected contribution.
- Recommends suitable source categories.
- Defines practical stopping conditions.
- Identifies unresolved ambiguities.

The agent designs search strategies. It does not execute searches or retrieve information.

## Architecture

The agent is self-contained and independently usable.

Its internal components include:

- **Reasoning:** LLM-powered search strategy design.
- **Skills:** Information decomposition, search-space coverage, query design, prioritization, source selection, and stopping conditions.
- **Provider abstraction:** Replaceable LLM providers.
- **Validation:** Structured input and output validation.
- **Communication:** A2A protocol interface.

Consumers interact with the agent through its published interface and contracts without depending on its internal implementation.

## Design Principles

- One agent, one responsibility.
- Independent and reusable.
- Explicit input and output contracts.
- Encapsulated internal capabilities.
- Replaceable LLM providers.
- Integration-ready, without depending on other agents.

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
- An available LLM provider:
  - Arvan AI API
  - Local Ollama instance

## Installation

Clone the repository and install dependencies:

```bash
git clone <repository-url>
cd search-strategy-agent
uv sync
```

## Configuration

Create a `.env` file in the project root.

### Arvan AI

```dotenv
SEARCH_STRATEGY_PROVIDER=arvan
SEARCH_STRATEGY_HOST=127.0.0.1
SEARCH_STRATEGY_PORT=9999

ARVAN_API_KEY=your-api-key
ARVAN_BASE_URL=your-endpoint-url
ARVAN_MODEL=GPT-5
```

### Ollama

Alternatively, configure a local Ollama instance:

```dotenv
SEARCH_STRATEGY_PROVIDER=ollama
SEARCH_STRATEGY_HOST=127.0.0.1
SEARCH_STRATEGY_PORT=9999

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen3.5:latest
```

Ensure the selected provider is available before starting the agent.

## Running the Agent

Start the A2A server:

```bash
uv run search-strategy-agent
```

The default local endpoint is:

```text
http://127.0.0.1:9999/
```

The Agent Card is available at:

```text
http://127.0.0.1:9999/.well-known/agent-card.json
```

## Example Interaction

The agent accepts an A2A `SendMessage` request containing a JSON data part.

```bash
curl --noproxy '*' -X POST http://127.0.0.1:9999/ \
  -H "Content-Type: application/json" \
  -H "A2A-Version: 1.0" \
  -d '{
    "jsonrpc": "2.0",
    "id": "1",
    "method": "SendMessage",
    "params": {
      "message": {
        "messageId": "example-001",
        "role": "ROLE_USER",
        "parts": [
          {
            "data": {
              "objective": "Research local-first multi-agent architectures",
              "context": "Focus on autonomous agents and interoperability",
              "constraints": [
                "Prioritize technical sources"
              ],
              "preferred_source_types": [
                "academic",
                "technical"
              ],
              "freshness_requirement": "Prioritize 2024 onward"
            },
            "mediaType": "application/json"
          }
        ]
      }
    }
  }'
```

A successful execution returns a completed A2A task containing a `search-strategy` JSON artifact.

## Public Contracts

The public interface is defined independently of the internal implementation.

| Resource | Description |
|---|---|
| `contracts/input.schema.json` | Input JSON Schema |
| `contracts/output.schema.json` | Output JSON Schema |
| `docs/contract.md` | Human-readable public contract |

**Schema standard:** JSON Schema Draft 2020-12.

Consumers should integrate against these published contracts rather than internal Python models or implementation details.

## Current Limitations

- Task state is stored in memory and does not survive server restarts.
- LLM execution is synchronous internally.
- Task cancellation is not supported.
- Authentication and production deployment security are not yet implemented.

## Status

Early development — v0.1.0.

The agent has completed an end-to-end A2A interaction using its published interface.