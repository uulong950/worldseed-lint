"""
Profile Rule: L0 — Ontology

Enforces:
- Explicit world identity
- Explicit ontology declaration

Forbidden:
- Actions
- Observers
"""

def check(context):
    violations = []

    if not context.world or not context.ontology:
        violations.append({
            "rule": "PROFILE-L0-ONTOLOGY",
            "axiom": "S1",
            "path": "world / ontology",
            "message": "L0 profile requires world identity and ontology."
        })

    if context.actions or context.observers:
        violations.append({
            "rule": "PROFILE-L0-NO-DYNAMICS",
            "axiom": "S4",
            "path": "actions / observers",
            "message": "L0 profile MUST NOT declare actions or observers."
        })

    return violations
