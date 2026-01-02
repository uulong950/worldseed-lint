"""
Axiom S19 — Distinguishability Preservation

Rule ID: AXIOM-S19-DISTINGUISHABILITY
Severity: ERROR
Status: Normative

Requirement:
All transformations MUST declare
which distinctions are preserved
and which are destroyed.

Violation Conditions:
- Undeclared degradation
- Silent preprocessing

Rationale:
WorldSeed is defined in terms of distinguishability.
"""

def check(context):
    # Enforced structurally via degradation_graph
    return []
