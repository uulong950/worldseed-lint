# WorldSeed Lint ABI (Normative)

**Status**: Normative  
**Scope**: Command-line output contract and exit semantics for `worldseed-lint`  
**Authority**: WorldSeed Constitution, Axioms (S1–S19), Lint Rules, Verdict Glossary  

---

## 1. Purpose

This document defines the **stable Application Binary Interface (ABI)**  
for **WorldSeed Lint**.

Any tool, CI pipeline, benchmark, publication, or automated system  
that consumes WorldSeed Lint results **MUST** interpret outputs  
according to this specification.

This document governs:

- output structure
- verdict semantics
- violation representation
- exit code behavior

This document does **NOT** define:

- lint rules
- axiom semantics
- compliance profiles
- semantic comparability verdicts

---

## 2. Invocation Contract

### 2.1 Command Form

```text
worldseed-lint <manifest_path>
```

Exactly one manifest path MUST be provided.

The CLI MUST NOT infer missing arguments.

The CLI MUST NOT introduce default values.

### 2.2 Input Encoding

The manifest MUST be parsed as UTF-8 JSON.

Failure to read or parse input MUST result in a BLOCKED verdict  
and exit code 2.

---

## 3. Output Channel and Determinism

### 3.1 Output Channel

- The CLI MUST emit exactly one JSON object to **STDOUT**.
- STDERR MAY be used for diagnostic messages, but MUST NOT carry the compliance report.

### 3.2 Determinism

- Output MUST be deterministic for identical input.
- The order of `violations[]` MUST be deterministic and **MUST be stable across runs**.

#### 3.2.1 Violation Ordering (Normative)

The `violations[]` array MUST be sorted by the following key:

1. `severity_rank` (ERROR = 0, WARNING = 1)
2. `rule` (lexicographic ascending)
3. `path` (lexicographic ascending)
4. `message` (lexicographic ascending)

No implementation MAY rely on insertion order, dictionary iteration order,
or traversal order to determine violation ordering.

---

## 4. Report Object ABI

### 4.1 Top-Level Object

The output JSON object MUST contain the following fields:

| Field | Type | Required |
|------|------|----------|
| `verdict` | string | YES |
| `summary` | object | YES |
| `violations` | array | YES |

Optional backward-compatibility field:

- `compliance` (`"valid"` / `"invalid"`)

If present, `compliance` MUST be consistent with `verdict`
as defined in §4.1.1.

#### 4.1.1 Legacy Compatibility Field: `compliance` (Normative)

`compliance` is a **legacy** field and exists only for backward compatibility.

- Consumers MUST treat `verdict` as the authoritative field.
- If `compliance` is present, it MUST be derived from `verdict` as follows:

| `verdict` | `compliance` |
|----------|--------------|
| `COMPLIANT` | `valid` |
| `NON-COMPLIANT` | `invalid` |
| `BLOCKED` | `invalid` |

No other mapping is permitted.

---

## 5. Verdict Semantics (Top-Level)

The `verdict` field MUST be exactly one of:

- `COMPLIANT`
- `NON-COMPLIANT`
- `BLOCKED`

### 5.1 COMPLIANT

All WorldSeed axioms applicable to the declared profile are satisfied.

`COMPLIANT` does **NOT** imply:

- correctness
- realism
- usefulness
- endorsement

### 5.2 NON-COMPLIANT

One or more WorldSeed axioms are violated.

`NON-COMPLIANT` is a semantic failure, not a runtime error  
and not a quality judgment.

### 5.3 BLOCKED

Compliance evaluation cannot proceed due to missing, invalid,  
or undeclared mandatory information.

`BLOCKED` is a pre-verdict state, not an axiom violation.

---

## 6. Summary Object

The `summary` object MUST contain:

| Field | Type | Meaning |
|------|------|---------|
| `errors` | integer | Count of ERROR-level violations |
| `warnings` | integer | Count of WARNING-level findings |
| `blocked` | integer | `1` if verdict is BLOCKED, else `0` |

### 6.1 Constraints (Normative)

- If `verdict == "BLOCKED"`, then `summary.blocked MUST equal 1`.
- If `verdict != "BLOCKED"`, then `summary.blocked MUST equal 0`.

Additionally:

- If `verdict == "COMPLIANT"`, then `summary.errors MUST equal 0`.
- If `verdict == "NON-COMPLIANT"`, then `summary.errors MUST be greater than 0`.

No implementation MAY emit an internally inconsistent `(verdict, summary)` pair.

---

## 7. Violations Array

Each element of `violations[]` MUST be an object with the following fields:

| Field      | Type           | Required |
|------------|----------------|----------|
| `severity` | string         | YES      |
| `rule`     | string         | YES      |
| `axiom`    | string or null | YES      |
| `path`     | string         | YES      |
| `message`  | string         | YES      |

### 7.1 Severity

`severity` MUST be one of:

- `ERROR`
- `WARNING`

Unless explicitly stated otherwise in `lint-rules.md`,  
all rule violations MUST be reported as `ERROR`.

### 7.2 Rule and Axiom

- `rule` MUST be a globally unique rule identifier.
- `axiom` MUST reference the corresponding axiom (e.g., `S12`),  
  or be `null` for `BLOCKED` or invocation-level failures.

### 7.3 Path

`path` MUST identify the manifest field responsible  
for the violation.

The path MUST be traceable and deterministic.

---

## 8. BLOCKED Conditions (Normative)

The verdict `BLOCKED` MUST be produced when and only when  
compliance evaluation cannot proceed.

This includes, but is not limited to:

- **Invocation or IO failure**
  - file not found
  - permission denied
  - JSON parse error
- **Schema validation failure**
  - manifest does not conform to the declared schema version
- **Unresolvable entry conditions**
  - missing or unsupported version
  - missing or unknown profile
- **Semantic context construction failure**
  - mandatory entry fields missing such that no canonical  
    semantic context can be constructed

### 8.1 Prohibition

`BLOCKED` MUST NOT be used to avoid reporting semantic violations  
that can be evaluated.

For example:

> Missing actions under a profile that requires actions  
> MUST yield `NON-COMPLIANT` with `ERROR` violations,  
> not `BLOCKED`.

---

## 9. Verdict Derivation Rules

The final verdict MUST be derived as follows:

- If `summary.blocked == 1` → `verdict = "BLOCKED"`
- Else if `summary.errors > 0` → `verdict = "NON-COMPLIANT"`
- Else → `verdict = "COMPLIANT"`

Any `ERROR`-level violation MUST imply  
`verdict = "NON-COMPLIANT"`, unless `BLOCKED` applies.

---

## 10. Exit Code Semantics

The CLI exit code MUST reflect the top-level verdict:

| Exit Code | Meaning |
|----------|---------|
| `0` | COMPLIANT |
| `1` | NON-COMPLIANT |
| `2` | BLOCKED or invocation/IO failure |

### 10.1 Emission Requirement on Failure (Normative)

On invocation/IO failure (e.g., missing file, parse error):

- the CLI MUST attempt to emit a `BLOCKED` report to STDOUT,
  conforming to this ABI, whenever possible;
- then exit with code `2`.

The CLI MUST NOT exit without emitting a report unless the process
cannot write to STDOUT at all.

---

## 11. Compatibility and Versioning (Recommended)

The report MAY include the following optional fields:

- `report_version`
- `spec_version`
- `lint_version`

If present, these fields MUST be accurate and MUST NOT  
affect verdict derivation.

No new verdict terms MAY be introduced without updating  
`docs/verdicts.md` and bumping the specification version.

---

## 12. Non-Scope: Semantic Comparability Verdicts

The following verdicts are explicitly out of scope  
for WorldSeed Lint:

- `NOT COMPARABLE`

Such verdicts apply only to runtime or analytical layers  
above compliance checking and MUST NOT be emitted  
by `worldseed-lint`.

---

## 13. Example Outputs

### 13.1 NON-COMPLIANT (Ordering Example)

```json
{
  "verdict": "NON-COMPLIANT",
  "summary": { "errors": 3, "warnings": 0, "blocked": 0 },
  "violations": [
    {
      "severity": "ERROR",
      "rule": "AXIOM-S11-OBSERVATION-SEMANTICS",
      "axiom": "S11",
      "path": "observers[camera].noise.uncertainty",
      "message": "Observer uncertainty MUST NOT be implicit."
    },
    {
      "severity": "ERROR",
      "rule": "AXIOM-S12-SENSING-BOUNDARY",
      "axiom": "S12",
      "path": "observers[camera].boundary",
      "message": "Observer MUST declare sensing boundary."
    },
    {
      "severity": "ERROR",
      "rule": "AXIOM-S5-ACTION-COMPLETENESS",
      "axiom": "S5",
      "path": "actions",
      "message": "Profile requires at least one declared action."
    }
  ],
  "compliance": "invalid"
}

---

## 14. Final Statement

WorldSeed Lint does not evaluate performance,  
quality, usefulness, or intelligence.

It evaluates what may be claimed.

This ABI defines the boundary between  
semantic legitimacy and everything else.