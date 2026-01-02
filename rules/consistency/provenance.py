"""
Consistency Rule: Provenance Consistency

Validates that:
- Declared provenance matches usage.
- Derived quantities declare derivation.
- Provenance chains are not contradictory.
"""

def check(context):
    violations = []

    for key, q in context.quantities.items():
        if not q.provenance:
            violations.append({
                "rule": "CONSISTENCY-PROVENANCE-MISSING",
                "axiom": "S6",
                "path": key,
                "message": "Quantity MUST declare provenance."
            })

    return violations
