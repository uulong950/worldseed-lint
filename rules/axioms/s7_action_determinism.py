"""
Axiom S7 — Action Determinism Declaration

Rule ID: AXIOM-S7-ACTION-DETERMINISM
Severity: ERROR
Status: Normative

Requirement:
Actions MUST be deterministic unless stochasticity
is explicitly declared.

Violation Conditions:
- Non-repeatable actions without stochastic declaration

Rationale:
Undeclared randomness is hidden noise.
"""

def check(context):
    violations = []

    for name, action in context.actions.items():
        if action.stochastic not in (True, False):
            violations.append({
                "severity": "ERROR",
                "rule": "AXIOM-S7-ACTION-DETERMINISM",
                "axiom": "S7",
                "path": f"actions[{name}].stochastic",
                "message": "Action stochasticity MUST be explicitly declared."
            })

    return violations
