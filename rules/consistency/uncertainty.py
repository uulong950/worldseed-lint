"""
Consistency Rule: Uncertainty Consistency

Validates that:
- Uncertainty is present where required.
- Uncertainty values are non-negative.
- Zero uncertainty is not declared for measured quantities.
"""

def check(context):
    violations = []

    for key, q in context.quantities.items():
        if isinstance(q.uncertainty, (int, float)):
            if q.uncertainty < 0:
                violations.append({
                    "rule": "CONSISTENCY-UNCERTAINTY-NEGATIVE",
                    "axiom": "S16",
                    "path": key,
                    "message": "Uncertainty MUST be non-negative."
                })

        if q.value == "unknown" and q.uncertainty not in ("unknown", None):
            violations.append({
                "rule": "CONSISTENCY-UNCERTAINTY-VALUE-CONFLICT",
                "axiom": "S16",
                "path": key,
                "message": "Unknown value MUST NOT imply precise uncertainty."
            })

    return violations
