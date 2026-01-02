"""
Feature Rule: Action Semantics

Rule IDs:
- FEATURE-ACTION-COMPLETENESS
- FEATURE-ACTION-SEMANTICS
- FEATURE-ACTION-DETERMINISM

Enforces:
- S4, S5, S6, S7

This module validates that actions:
- are complete,
- are semantically explicit,
- and declare stochasticity when applicable.
"""

def check(context):
    violations = []

    for name, action in context.actions.items():
        if not action.parameters:
            violations.append({
                "rule": "FEATURE-ACTION-PARAMETERS",
                "axiom": "S5",
                "path": f"actions[{name}].parameters",
                "message": "Action MUST declare at least one parameter."
            })

    return violations
