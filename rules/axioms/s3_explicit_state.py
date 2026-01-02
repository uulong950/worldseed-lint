"""
Axiom S3 — Explicit State Declaration

Rule ID: AXIOM-S3-EXPLICIT-STATE
Severity: ERROR
Status: Normative

Requirement:
All world state dimensions relevant to learning
MUST be explicitly declared.

Violation Conditions:
- Undeclared state dimensions are referenced or implied

Rationale:
Implicit state collapses distinguishability.
"""

def check(context):
    violations = []

    if not context.ontology.entities:
        violations.append({
            "severity": "ERROR",
            "rule": "AXIOM-S3-EXPLICIT-STATE",
            "axiom": "S3",
            "path": "ontology.entities",
            "message": "Ontology MUST declare at least one state entity."
        })

    return violations
