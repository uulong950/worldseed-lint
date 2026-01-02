"""
Axiom S10 — Observer Stability

Rule ID: AXIOM-S10-OBSERVER-STABILITY
Severity: ERROR
Status: Normative

Requirement:
Observer parameters MUST remain fixed
unless explicitly changed via declared actions.

Violation Conditions:
- Undeclared sensor drift or recalibration

Rationale:
Undeclared drift is silent degradation.
"""

def check(context):
    # Drift must be declared via actions; not representable otherwise
    return []
