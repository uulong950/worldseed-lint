"""
Profile Rule: L2 — Sensing

Enforces:
- All L1 requirements
- Explicit observers
- Explicit sensing boundaries
- Uncertainty declaration
"""

def check(context):
    violations = []

    if context.profile == "L2":
        if not context.observers:
            violations.append({
                "rule": "PROFILE-L2-OBSERVERS",
                "axiom": "S9",
                "path": "observers",
                "message": "L2 profile requires observers."
            })

        for name, obs in context.observers.items():
            if obs.boundary is None:
                violations.append({
                    "rule": "PROFILE-L2-BOUNDARY",
                    "axiom": "S12",
                    "path": f"observers[{name}].boundary",
                    "message": "L2 observers MUST declare sensing boundary."
                })

    return violations
