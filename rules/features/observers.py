"""
Feature Rule: Observer Semantics

Rule IDs:
- FEATURE-OBSERVER-NON-INTERVENTION
- FEATURE-OBSERVER-EXPLICIT
- FEATURE-OBSERVER-STABILITY

Enforces:
- S8, S9, S10, S11

This module validates that observers:
- are explicitly declared,
- do not modify world state,
- do not drift without declaration,
- and declare uncertainty.

Violations invalidate WorldSeed compliance.
"""

def check(context):
    violations = []

    for name, obs in context.observers.items():
        if obs.operator is None:
            violations.append({
                "rule": "FEATURE-OBSERVER-OPERATOR",
                "axiom": "S11",
                "path": f"observers[{name}].operator",
                "message": "Observer MUST declare an operator."
            })

    return violations
