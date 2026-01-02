"""
Axiom S12 — Sensing Boundary Declaration

Rule ID: AXIOM-S12-SENSING-BOUNDARY
Severity: ERROR
Status: Normative

Requirement:
Each observer MUST declare a sensing boundary.

Violation Conditions:
- Missing or implicit boundary

Rationale:
Learning beyond observability is invalid.
"""

def check(context):
    violations = []

    for name, obs in context.observers.items():
        if obs.boundary is None:
            violations.append({
                "severity": "ERROR",
                "rule": "AXIOM-S12-SENSING-BOUNDARY",
                "axiom": "S12",
                "path": f"observers[{name}].boundary",
                "message": "Observer MUST declare sensing boundary."
            })

    return violations
