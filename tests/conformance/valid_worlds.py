"""
Conformance Set: Valid Worlds

Status: Normative

This module defines world declarations
that MUST be accepted by WorldSeed Lint.

Each case:
- explicitly satisfies all applicable axioms,
- may contain 'unknown',
- but violates no normative rule.

Failure to accept these cases
indicates an overly restrictive implementation.
"""

VALID_WORLDS = [
    {
        "version": "1.0.0",
        "profile": "L2",
        "world": {
            "id": "550e8400-e29b-41d4-a716-446655440000"
        },
        "ontology": {
            "entities": ["position"]
        },
        "actions": [
            {
                "name": "move",
                "parameters": {
                    "dx": {
                        "value": "unknown",
                        "unit": "meter",
                        "uncertainty": "unknown",
                        "provenance": "control"
                    }
                },
                "stochastic": False
            }
        ],
        "observers": [
            {
                "name": "camera",
                "operator": "pinhole",
                "boundary": "2D projection",
                "noise": {
                    "value": "unknown",
                    "unit": "pixel",
                    "uncertainty": 1.0,
                    "provenance": "sensor"
                }
            }
        ]
    }
]
