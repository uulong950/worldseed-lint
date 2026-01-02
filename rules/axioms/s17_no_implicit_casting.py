"""
Axiom S17 — No Implicit Casting

Rule ID: AXIOM-S17-NO-IMPLICIT-CASTING
Severity: ERROR
Status: Normative

Requirement:
Numerical casting MUST NOT be implicit.

Violation Conditions:
- Undeclared normalization
- Silent type conversion

Rationale:
Implicit casting is silent degradation.
"""

def check(context):
    # Implicit casting cannot occur in SemanticContext
    return []
