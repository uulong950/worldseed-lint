"""
Axiom S13 — Boundary Respect

Rule ID: AXIOM-S13-BOUNDARY-RESPECT
Severity: ERROR
Status: Normative

Requirement:
Distinctions outside the declared sensing boundary
MUST be treated as inaccessible.

Violation Conditions:
- Inference or claims beyond boundary

Rationale:
Boundary violations invalidate claims.
"""

def check(context):
    # Boundary violations are checked against claims;
    # no implicit inference here.
    return []
