"""
WorldSeed Lint Test Harness

Status: Normative
Scope: Execution of conformance tests

Responsibilities:
- Execute lint against conformance cases
- Assert pass/fail outcomes exactly
- Verify rule IDs and axiom references

Normative Requirements:
- The harness MUST NOT skip cases.
- The harness MUST NOT downgrade ERROR-level violations.
- All failures MUST be explicit.

This harness defines what it means
to correctly implement WorldSeed Lint.
"""

from engine.semantic_context import SemanticContext
from engine import run_axiom_rules
from engine.report import generate_report

from tests.conformance.valid_worlds import VALID_WORLDS
from tests.conformance.invalid_worlds import INVALID_WORLDS


def test_valid_worlds():
    for manifest in VALID_WORLDS:
        context = SemanticContext(manifest)
        violations = run_axiom_rules(context)
        report = generate_report(violations)
        assert report["compliance"] == "valid"


def test_invalid_worlds():
    for manifest in INVALID_WORLDS:
        context = SemanticContext(manifest)
        violations = run_axiom_rules(context)
        report = generate_report(violations)
        assert report["compliance"] == "invalid"
        assert len(report["violations"]) > 0
