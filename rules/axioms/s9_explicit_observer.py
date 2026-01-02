"""
Axiom S9 — Explicit Observer Definition

Rule ID: AXIOM-S9-EXPLICIT-OBSERVER
Severity: ERROR
Status: Normative

Requirement:
All observations MUST be attributable
to explicitly declared observers.

Violation Conditions:
- Observations exist without observer declaration

Rationale:
Implicit observers erase world–measurement boundary.
"""

def check(context):
    violations = []

    if context.profile in ("L2", "L3") and not context.observers:
        violations.append({
            "rule": "AXIOM-S9-EXPLICIT-OBSERVER",
            "axiom": "S9",
            "path": "observers",
            "message": "Profile requires explicit observers."
        })

    return violations
