"""
Axiom S11 — Observation Operator Semantics

Rule ID: AXIOM-S11-OBSERVATION-SEMANTICS
Severity: ERROR
Status: Normative

Requirement:
Each observer MUST declare its observation operator
and associated uncertainty.

Violation Conditions:
- Missing operator definition
- Missing noise or uncertainty

Rationale:
Observation without semantics is undefined.
"""

def check(context):
    violations = []

    for name, obs in context.observers.items():
        if not obs.operator:
            violations.append({
                "severity": "ERROR",
                "rule": "AXIOM-S11-OBSERVATION-SEMANTICS",
                "axiom": "S11",
                "path": f"observers[{name}].operator",
                "message": "Observer operator MUST be declared."
            })

        if obs.noise.uncertainty == "unknown":
            violations.append({
                "severity": "ERROR",
                "rule": "AXIOM-S11-OBSERVATION-SEMANTICS",
                "axiom": "S11",
                "path": f"observers[{name}].noise.uncertainty",
                "message": "Observer uncertainty MUST NOT be implicit."
            })

    return violations
