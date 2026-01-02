"""
Feature Rule: Numerical Semantics

Rule IDs:
- FEATURE-NUMERICAL-SEMANTICS
- FEATURE-NO-IMPLICIT-CASTING

Enforces:
- S16, S17

This module validates physical meaning
of numerical representations.
"""

def check(context):
    violations = []

    for key, q in context.quantities.items():
        if q.unit is None or q.unit == "":
            violations.append({
                "rule": "FEATURE-NUMERICAL-UNIT",
                "axiom": "S16",
                "path": key,
                "message": "Numerical quantity MUST declare unit."
            })

        if q.uncertainty is None:
            violations.append({
                "rule": "FEATURE-NUMERICAL-UNCERTAINTY",
                "axiom": "S16",
                "path": key,
                "message": "Numerical quantity MUST declare uncertainty."
            })

    return violations
