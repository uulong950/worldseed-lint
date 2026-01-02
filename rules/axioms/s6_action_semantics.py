"""
Axiom S6 — Action Semantics

Rule ID: AXIOM-S6-ACTION-SEMANTICS
Severity: ERROR
Status: Normative

Requirement:
Each action MUST declare parameters with explicit
units and provenance.

Violation Conditions:
- Missing unit
- Missing provenance
- Implicit parameter scaling

Rationale:
Action semantics define causal meaning.
"""

def check(context):
    violations = []

    for name, action in context.actions.items():
        for pname, q in action.parameters.items():
            if not q.unit:
                violations.append({
                    "severity": "ERROR",
                    "rule": "AXIOM-S6-ACTION-SEMANTICS",
                    "axiom": "S6",
                    "path": f"actions[{name}].parameters[{pname}].unit",
                    "message": "Action parameter missing unit."
                })
            if q.provenance is None:
                violations.append({
                    "severity": "ERROR",
                    "rule": "AXIOM-S6-ACTION-SEMANTICS",
                    "axiom": "S6",
                    "path": f"actions[{name}].parameters[{pname}].provenance",
                    "message": "Action parameter missing provenance."
                })

    return violations
