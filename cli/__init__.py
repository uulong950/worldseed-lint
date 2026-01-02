"""
WorldSeed Lint CLI Package

Status: Normative
Scope: Command-line interface for invoking WorldSeed Lint

This package defines the authoritative user-facing entry point
for WorldSeed Lint.

The CLI is a thin orchestration layer.
It MUST NOT:
- implement validation logic,
- introduce semantics,
- reinterpret results.

All authority resides in:
- engine/
- rules/
"""
