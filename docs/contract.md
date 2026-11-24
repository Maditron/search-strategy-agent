# Search Strategy Agent — Public Contract

Version: 0.1.0

## Purpose

Transform an information need into a structured, relevant, prioritized, and actionable search strategy.

The agent designs the search. It does not execute searches or retrieve information.

## Interface

The agent accepts one JSON object and returns one JSON object.

- Input schema: `contracts/input.schema.json`
- Output schema: `contracts/output.schema.json`
- Schema standard: JSON Schema Draft 2020-12

## Input

| Field | Required | Meaning |
|---|---|---|
| objective | Yes | The information need to investigate. |
| context | No | Background needed to interpret the objective. |
| constraints | No | Restrictions and requirements. |
| preferred_source_types | No | Preferred source categories. |
| freshness_requirement | No | Desired information recency. |

The objective must not be empty. Optional fields may be omitted.

## Output

| Field | Meaning |
|---|---|
| interpreted_objective | The agent's interpretation of the information need. |
| information_dimensions | Distinct research dimensions to investigate. |
| queries | Search queries, their purposes, and priorities. |
| source_types | Recommended source categories. |
| freshness_filter | Suggested temporal filter, if applicable. |
| exclusion_criteria | Material that should be excluded. |
| stopping_conditions | Conditions for considering the planned search sufficiently complete. |
| unresolved_ambiguities | Uncertainties that may affect the strategy. |

### Query priority

- Priority is a positive integer.
- `1` means highest priority.
- Lower numbers indicate higher execution priority.
- Priorities express relative ordering, not a relevance score.

## Behavioral expectations

The agent should:

1. Interpret the objective using the supplied context.
2. Decompose it into meaningful information dimensions.
3. Design queries that collectively cover those dimensions.
4. Avoid unnecessary query duplication.
5. Prioritize queries by expected contribution and importance.
6. Recommend source types appropriate to the information need.
7. Respect constraints and freshness requirements.
8. Define practical stopping conditions.
9. Identify unresolved ambiguities rather than silently inventing missing information.

## Scope boundaries

The agent is responsible for search strategy design only.

It does not:

- Execute search queries.
- Browse websites or retrieve documents.
- Verify source credibility.
- Summarize search results.
- Guarantee that the resulting information need has been satisfied.

These responsibilities belong to downstream components.

## Compatibility

Consumers should integrate against the published input and output schemas, not internal implementation details.

Internal implementation changes that preserve these schemas and their documented semantics should not require consumer changes.

Changes to required fields, field meanings, or behavioral guarantees may require a contract version update.