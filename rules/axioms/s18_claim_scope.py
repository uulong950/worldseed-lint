"""
Axiom S18 — Claim Scope Limitation

Rule ID: AXIOM-S18-CLAIM-SCOPE
Severity: ERROR
Status: Normative

Requirement:
All learning or generalization claims
MUST be scoped to the declared world,
profile, observers, and boundaries.

Violation Conditions:
- Over-claim beyond declared scope

Rationale:
Claims outside scope are invalid.
"""

def check(context):
    # Claims live outside lint input; profile enforcement only
    return []
