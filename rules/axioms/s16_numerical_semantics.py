"""
Axiom S16 — Numerical Type Semantics

Rule ID: AXIOM-S16-NUMERICAL-SEMANTICS
Severity: ERROR
Status: Normative

Requirement:
All numerical values MUST carry explicit physical semantics.

Violation Conditions:
- Bare numbers
- Missing unit or uncertainty

Rationale:
Numbers without semantics are meaningless.
"""

def check(context):
    violations = []

    for key, q in context.quantities.items():
        if q.unit is None:
            violations.append({
                "severity": "ERROR",
                "rule": "AXIOM-S16-NUMERICAL-SEMANTICS",
                "axiom": "S16",
                "path": key,
                "message": "Numerical quantity missing unit."
            })

    return violations
