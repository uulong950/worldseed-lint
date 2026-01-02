"""
Axiom S14 — Explicit Irreversibility

Rule ID: AXIOM-S14-EXPLICIT-IRREVERSIBILITY
Severity: ERROR
Status: Normative

Requirement:
All irreversible operations MUST be explicitly declared.

Violation Conditions:
- Quantization, compression, or projection without declaration

Rationale:
Irreversibility defines degradation.
"""

def check(context):
    # No implicit irreversibility allowed
    return []
