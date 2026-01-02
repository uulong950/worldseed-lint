"""
WorldSeed Lint Command-Line Interface

Status: Normative
Scope: Invocation and orchestration only

Responsibilities:
- Parse command-line arguments
- Load manifest(s)
- Invoke engine in the correct order
- Emit reports

Normative Requirements:
- The CLI MUST NOT alter lint outcomes.
- The CLI MUST NOT suppress ERROR-level violations.
- The CLI MUST NOT introduce defaults or inferred flags.
- Exit codes MUST reflect compliance status.

Exit Semantics:
- Exit code 0: Valid WorldSeed compliance
- Exit code 1: Invalid WorldSeed compliance
- Exit code 2: Invocation or IO error

The CLI is not a policy engine.
"""

import json
import sys

from engine.semantic_context import SemanticContext
from engine import run_axiom_rules
from engine.report import generate_report


def main():
    if len(sys.argv) != 2:
        print("Usage: worldseed-lint <manifest.json>")
        sys.exit(2)

    try:
        with open(sys.argv[1]) as f:
            manifest = json.load(f)
    except (FileNotFoundError, PermissionError) as e:
        violations = [{
            "severity": "ERROR",
            "rule": "CLI-IO-ERROR",
            "axiom": None,
            "path": sys.argv[1],
            "message": f"Failed to read manifest: {str(e)}"
        }]
        report = generate_report(violations)
        print(json.dumps(report, indent=2))
        sys.exit(2)
    except json.JSONDecodeError as e:
        violations = [{
            "severity": "ERROR",
            "rule": "CLI-JSON-ERROR",
            "axiom": None,
            "path": sys.argv[1],
            "message": f"Invalid JSON in manifest: {str(e)}"
        }]
        report = generate_report(violations)
        print(json.dumps(report, indent=2))
        sys.exit(2)

    try:
        # Semantic context construction (pure builder)
        context = SemanticContext(manifest)
    except ValueError as e:
        # Convert construction errors to violations
        violations = [{
            "severity": "ERROR",
            "rule": "CONSTRUCTION-ERROR",
            "axiom": None,
            "path": "manifest",
            "message": str(e)
        }]
        report = generate_report(violations)
        print(json.dumps(report, indent=2))
        sys.exit(2)

    # Rule execution
    violations = run_axiom_rules(context)

    # Reporting
    report = generate_report(violations)
    print(json.dumps(report, indent=2))

    # Determine exit code according to interface.md ABI
    if report["verdict"] == "COMPLIANT":
        sys.exit(0)
    elif report["verdict"] == "NON-COMPLIANT":
        sys.exit(1)
    else:  # BLOCKED
        sys.exit(2)


if __name__ == "__main__":
    main()
