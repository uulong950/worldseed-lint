"""
Profile Rule: L1 — Causal

Enforces:
- All L0 requirements
- Explicit action declarations

Forbidden:
- Observers
"""

def check(context):
    violations = []

    if context.profile == "L1":
        if not context.actions:
            violations.append({
                "rule": "PROFILE-L1-ACTIONS",
                "axiom": "S5",
                "path": "actions",
                "message": "L1 profile requires declared actions."
            })

        if context.observers:
            violations.append({
                "rule": "PROFILE-L1-NO-OBSERVERS",
                "axiom": "S9",
                "path": "observers",
                "message": "L1 profile MUST NOT declare observers."
            })

    return violations
