"""
Module: Report Generator

Status: Normative
Responsibility: Deterministic compliance reporting

This module generates the final validation report
for WorldSeed Lint.

Normative Requirements:
- Each violation MUST include:
  - rule ID,
  - axiom reference,
  - manifest field path,
  - normative explanation.
- Output MUST be deterministic.
- Severity levels MUST NOT be altered or suppressed.

Supported outputs:
- Machine-readable structured format (e.g., JSON)
- Human-readable textual format

This module MUST NOT:
- aggregate away violations,
- suggest fixes,
- or reinterpret rule severity.
"""

def generate_report(violations: list[dict]) -> dict:
    """
    Generate deterministic lint report according to interface.md ABI.
    """
    # Count errors and warnings
    error_count = 0
    warning_count = 0
    blocked_count = 0

    # Determine blocked status
    is_blocked = any(v.get('rule') in ['CLI-IO-ERROR', 'CLI-JSON-ERROR', 'CONSTRUCTION-ERROR'] for v in violations)
    blocked_count = 1 if is_blocked else 0

    # Count errors and warnings
    for v in violations:
        if v.get('severity', 'ERROR') == 'ERROR':
            error_count += 1
        elif v.get('severity') == 'WARNING':
            warning_count += 1

    # Determine verdict
    if blocked_count == 1:
        verdict = "BLOCKED"
        compliance_status = "invalid"  # For backward compatibility
    elif error_count > 0:
        verdict = "NON-COMPLIANT"
        compliance_status = "invalid"  # For backward compatibility
    else:
        verdict = "COMPLIANT"
        compliance_status = "valid"  # For backward compatibility

    # Build summary
    summary = {
        "errors": error_count,
        "warnings": warning_count,
        "blocked": blocked_count
    }

    # Ensure all violations have required fields
    normalized_violations = []
    for v in violations:
        normalized_v = {
            "severity": v.get("severity", "ERROR"),
            "rule": v.get("rule", "UNKNOWN-RULE"),
            "axiom": v.get("axiom", None),
            "path": v.get("path", "unknown"),
            "message": v.get("message", "Unknown violation")
        }
        normalized_violations.append(normalized_v)

    # Sort violations according to §3.2.1: severity_rank (ERROR=0, WARNING=1), then rule, path, message
    normalized_violations.sort(key=lambda v: (
        0 if v["severity"] == "ERROR" else 1,  # severity_rank
        v["rule"],                              # rule (lexicographic ascending)
        v["path"],                              # path (lexicographic ascending)
        v["message"]                            # message (lexicographic ascending)
    ))

    # Ensure verdict-summary consistency according to §6.1
    if verdict == "BLOCKED":
        summary["blocked"] = 1
    else:
        summary["blocked"] = 0

    # Fix compliance mapping according to §4.1.1
    if verdict == "COMPLIANT":
        compliance_status = "valid"
    else:  # NON-COMPLIANT or BLOCKED
        compliance_status = "invalid"

    # Build final report
    report = {
        "verdict": verdict,
        "summary": summary,
        "violations": normalized_violations,
        "compliance": compliance_status  # For backward compatibility
    }

    return report
