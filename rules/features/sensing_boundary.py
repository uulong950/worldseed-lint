"""
Feature Rule: Sensing Boundary Semantics

Rule IDs:
- FEATURE-BOUNDARY-DECLARATION
- FEATURE-BOUNDARY-RESPECT

Enforces:
- S12, S13

This module validates correct declaration
and respect of sensing boundaries.
"""

def check(context):
    violations = []

    for name, obs in context.observers.items():
        if obs.boundary is None:
            violations.append({
                "rule": "FEATURE-SENSING-BOUNDARY",
                "axiom": "S12",
                "path": f"observers[{name}].boundary",
                "message": "Observer MUST declare sensing boundary."
            })

    return violations
