"""
Axiom S15 — No Implicit Reconstruction

Rule ID: AXIOM-S15-NO-IMPLICIT-RECONSTRUCTION
Severity: ERROR
Status: Normative

Requirement:
Irreversibly destroyed distinctions
MUST NOT be implicitly reconstructed.

Violation Conditions:
- Recovery of declared lost information

Rationale:
Reconstruction introduces undeclared priors.
"""

def check(context):
    # Enforced via degradation_graph invariants
    return []
