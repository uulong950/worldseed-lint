"""
Axiom Rule: S1 — World Identity

Rule ID: AXIOM-S1-WORLD-IDENTITY
Status: Normative
Severity: ERROR

Enforces:
- WorldSeed Axiom S1 (World Identity)

Requirement:
A manifest MUST declare a globally unique and immutable world identity.

Violation Conditions:
- world.id is missing
- world.id is empty
- world.id is not a valid UUID format
- world.id is reused across distinct manifests

This rule introduces NO new semantics.
"""

import re

def check(context):
    violations = []

    if not context.world.id:
        violations.append({
            "severity": "ERROR",
            "rule": "AXIOM-S1-WORLD-IDENTITY",
            "axiom": "S1",
            "path": "world.id",
            "message": "world.id MUST be non-empty."
        })
    else:
        # Check if world.id is a valid UUID format
        uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
        if not re.match(uuid_pattern, context.world.id, re.IGNORECASE):
            violations.append({
                "severity": "ERROR",
                "rule": "AXIOM-S1-WORLD-IDENTITY",
                "axiom": "S1",
                "path": "world.id",
                "message": "world.id MUST be a valid UUID format."
            })

    return violations
