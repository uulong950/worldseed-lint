"""
Profile Rule: L3 — Numerical Semantics

Enforces:
- All L2 requirements
- Numerical type semantics
- Explicit irreversibility
"""

def check(context):
    violations = []

    if context.profile == "L3":
        for key, q in context.quantities.items():
            if q.uncertainty == "unknown":
                violations.append({
                    "rule": "PROFILE-L3-UNCERTAINTY",
                    "axiom": "S16",
                    "path": key,
                    "message": "L3 profile requires explicit numerical uncertainty."
                })

    return violations
