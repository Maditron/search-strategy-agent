QUERY_PRIORITIZATION = """
## Skill: Query Prioritization

Assign priorities to search queries according to their expected
contribution to achieving the research objective.

1. Evaluate each query based on its relevance to the objective.
2. Consider its importance to essential information dimensions.
3. Prioritize queries that establish foundational understanding
   or address critical information gaps.
4. Give higher priority to queries likely to provide substantial
   information or resolve important uncertainties.
5. Consider dependencies between queries when determining
   execution order.
6. Give lower priority to supplementary, exploratory, or
   peripheral queries.
7. Avoid assigning equal priority to all queries unless
   their research value is genuinely comparable.

Use integer rankings:
- 1 = highest priority
- Larger numbers = progressively lower priority

Assign unique, sequential rankings where practical.
Priority represents execution importance, not a confidence
or relevance score.

Prioritization should reflect the objective, constraints,
freshness requirements, and overall research strategy.
"""