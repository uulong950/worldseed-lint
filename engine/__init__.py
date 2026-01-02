"""
WorldSeed Lint Engine Package

Status: Normative
Scope: Semantic execution core of WorldSeed Lint

This package defines the authoritative execution engine
for enforcing the WorldSeed specification.

Importing this package MUST NOT:
- execute validation,
- mutate state,
- infer missing information,
- or introduce defaults.

All behavior MUST be explicitly invoked by the caller.

Authority:
- WorldSeed Constitution
- WorldSeed Axioms (S1–S19)
- WorldSeed Manifest Specification
- WorldSeed Features and Operators

This package introduces NO new semantics.
"""

import importlib
from mapping.axiom_mapping import AXIOM_RULE_MODULES


def run_axiom_rules(context):
    """
    Execute all axiom rules in canonical order.

    Rules are executed strictly according to axiom mapping.
    """
    violations = []

    for axiom, module_path in AXIOM_RULE_MODULES.items():
        module = importlib.import_module(module_path)
        check_fn = getattr(module, "check")
        violations.extend(check_fn(context))

    return violations
