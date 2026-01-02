"""
Axiom S5 — Action Completeness

Rule ID: AXIOM-S5-ACTION-COMPLETENESS
Severity: ERROR
Status: Normative

Requirement:
All admissible actions that modify world state
MUST be explicitly declared.

Violation Conditions:
- Hidden or manual actions affect world state

Rationale:
Incomplete action declaration breaks causal accounting.
"""

def check(context):
    violations = []

    if context.profile in ("L1", "L2", "L3") and not context.actions:
        violations.append({
            "severity": "ERROR",
            "rule": "AXIOM-S5-ACTION-COMPLETENESS",
            "axiom": "S5",
            "path": "actions",
            "message": "Profile requires at least one declared action."
        })

    return violations
