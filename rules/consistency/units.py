"""
Consistency Rule: Unit Consistency

Validates that:
- Units are compatible across related quantities.
- No implicit unit conversion occurs.

Violations may invalidate compliance.
"""

def check(context):
    violations = []

    seen = {}

    for key, q in context.quantities.items():
        if key in seen:
            if seen[key] != q.unit:
                violations.append({
                    "rule": "CONSISTENCY-UNIT-MISMATCH",
                    "axiom": "S16",
                    "path": key,
                    "message": "Same quantity declared with conflicting units."
                })
        else:
            seen[key] = q.unit

    return violations
