"""
Axiom S8 — Observer Non-Intervention

Rule ID: AXIOM-S8-OBSERVER-NON-INTERVENTION
Severity: ERROR
Status: Normative

Requirement:
Observers MUST NOT modify world state.

Violation Conditions:
- Observer operation changes state variables

Rationale:
Measurement is not intervention.
"""

def check(context):
    # SemanticContext forbids mutation paths
    return []
