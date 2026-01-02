"""
Feature Rule: Irreversibility Semantics

Rule IDs:
- FEATURE-IRREVERSIBILITY-DECLARED
- FEATURE-NO-IMPLICIT-RECONSTRUCTION

Enforces:
- S14, S15, S19

This module validates that degradation
and irreversibility are explicit and auditable.
"""

def check(context):
    violations = []

    graph = context.degradation_graph
    for edge in graph.edges:
        if edge.irreversible and not edge.destroyed_distinctions:
            violations.append({
                "rule": "FEATURE-IRREVERSIBILITY",
                "axiom": "S14",
                "path": f"degradation[{edge.source}->{edge.target}]",
                "message": "Irreversible operation MUST declare destroyed distinctions."
            })

    return violations
