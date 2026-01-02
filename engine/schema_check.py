"""
Module: Schema Check

Status: Normative
Responsibility: Structural validation of WorldSeed manifests

This module validates a manifest against the authoritative
WorldSeed JSON Schema.

Normative Requirements:
- MUST validate against the declared schema version.
- MUST reject manifests that fail schema validation.
- MUST NOT perform semantic checks.
- MUST NOT infer or repair missing fields.

Schema validity MUST NOT be interpreted as WorldSeed compliance.
"""

import jsonschema

def validate_schema(manifest: dict, schema: dict):
    """
    Validate manifest against JSON Schema.

    This function performs STRUCTURAL validation only.
    Semantic validity is explicitly out of scope.
    """
    jsonschema.validate(instance=manifest, schema=schema)
