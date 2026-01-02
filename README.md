# WorldSeed Lint

**Status:** Normative Enforcement Tool  
**Scope:** Validation of WorldSeed world declarations  
**Authority:** WorldSeed Constitution, Axioms, Manifest, Features, Operators

---

## 1. Purpose

WorldSeed Lint is the **authoritative enforcement tool**
for the WorldSeed specification.

Its sole purpose is to determine whether a declared world
is **eligible to claim WorldSeed compliance**.

WorldSeed Lint does not improve data quality,
does not suggest fixes,
and does not evaluate model performance.

---

## 2. Normative Role

WorldSeed Lint is normative.

A world declaration that fails WorldSeed Lint
**MUST NOT** be described as WorldSeed-compliant.

Passing WorldSeed Lint is a **necessary condition**
for any compliance claim.

---

## 3. What WorldSeed Lint Is Not

WorldSeed Lint:

- MUST NOT be treated as a data cleaning tool.
- MUST NOT infer missing information.
- MUST NOT introduce default values.
- MUST NOT provide automatic repairs.
- MUST NOT evaluate learning performance or benchmarks.

Lint exists to **enforce explicitness**, not convenience.

---

## 4. Scope of Validation

WorldSeed Lint validates compliance against:

- the WorldSeed Constitution,
- Axioms S1–S19,
- the Manifest specification,
- declared compliance profiles,
- feature semantics,
- and operator semantics.

WorldSeed Lint enforces **semantic validity**,
not merely structural correctness.

---

## 5. Compliance Semantics

WorldSeed Lint produces a **binary compliance outcome**:

- **Valid** — the world MAY claim WorldSeed compliance.
- **Invalid** — the world MUST NOT claim WorldSeed compliance.

Warnings MAY be reported,
but any ERROR-level violation invalidates compliance.

---

## 6. Relationship to Other Repositories

- `worldseed-spec` defines the authoritative rules.
- `worldseed-lint` enforces those rules.
- `worldseed-sdk` MAY provide convenience utilities,
  but has no authority over compliance.

No implementation, including WorldSeed Lint itself,
may weaken or reinterpret the specification.

---

## 7. Versioning

WorldSeed Lint versions are aligned with
the WorldSeed specification version they enforce.

A lint version MUST clearly declare
which specification version it targets.

---

## 8. Final Statement

WorldSeed does not rely on trust.
It relies on explicit, auditable declarations.

WorldSeed Lint exists to make that audit unavoidable.

---

**End of README**
