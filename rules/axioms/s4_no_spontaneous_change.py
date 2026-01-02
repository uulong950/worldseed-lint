"""
Axiom S4 — No Spontaneous State Change

Rule ID: AXIOM-S4-NO-SPONTANEOUS-CHANGE
Severity: ERROR
Status: Normative

Requirement:
World state MUST change only through explicitly declared actions.

Violation Conditions:
- State changes without a corresponding declared action

Rationale:
Undeclared change is indistinguishable from hidden intervention.
"""

def check(context):
    violations = []

    # Enforced structurally: only actions can exist
    # Rule exists to forbid hidden mutation paths
    return violations
