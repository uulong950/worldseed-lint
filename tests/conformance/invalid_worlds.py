"""
Conformance Set: Invalid Worlds

Status: Normative

This module defines world declarations
that MUST be rejected by WorldSeed Lint.

Each case violates at least one axiom-level rule.

Failure to reject these cases
indicates an under-enforcing implementation.
"""

INVALID_WORLDS = [
    # Missing sensing boundary (S12)
    {
        "version": "1.0.0",
        "profile": "L2",
        "world": {
            "id": "550e8400-e29b-41d4-a716-446655440000"
        },
        "ontology": {
            "entities": ["position"]
        },
        "observers": [
            {
                "name": "camera",
                "operator": "pinhole",
                "noise": {
                    "value": "unknown",
                    "unit": "pixel",
                    "uncertainty": "unknown",
                    "provenance": "sensor"
                }
            }
        ]
    }
]
