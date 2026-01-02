# Verdict Glossary (Normative)

Status: Normative  
Scope: Semantic meaning of WorldSeed Lint verdicts and severities  
Authority: WorldSeed Constitution, Axioms (S1–S19), Lint Rules  

This document defines the **normative meaning** of all verdicts and
severity levels produced or referenced by WorldSeed Lint.

Any documentation, publication, benchmark, or claim that cites
WorldSeed Lint results **MUST** conform to the definitions in this file.
No alternative or informal reinterpretation of verdict semantics
is permitted.

---

## 1. Verdicts (Top-Level Outcomes)

### NON-COMPLIANT

**Meaning**  
One or more WorldSeed axioms are violated under the declared world.

**Implication**  
The declared world **MUST NOT** be described as WorldSeed-compliant.

**Non-Implication**  
NON-COMPLIANT does **NOT** imply:
- incorrectness of data or models,
- lack of empirical usefulness,
- failure of training or evaluation,
- invalidity outside the WorldSeed framework.

NON-COMPLIANT is a **semantic verdict**, not a performance judgment.

---

### BLOCKED

**Meaning**  
Compliance evaluation cannot proceed due to missing, incomplete,
or undeclared mandatory information.

BLOCKED indicates that the declared world is **insufficiently specified**
to admit a compliance determination.

**Implication**  
No WorldSeed compliance claim **MAY** be made.

**Non-Implication**  
BLOCKED does **NOT** imply:
- violation of an axiom,
- incorrect declaration,
- semantic inconsistency.

BLOCKED is a **pre-verdict state**, not a failure verdict.

---

### COMPLIANT (Implicit)

**Meaning**  
All enforced WorldSeed axioms applicable to the declared profile
are satisfied.

**Implication**  
The world **MAY** claim WorldSeed compliance.

**Non-Implication**  
COMPLIANT does **NOT** imply:
- correctness,
- realism,
- usefulness,
- superior performance,
- endorsement by WorldSeed.

WorldSeed Lint does not assert positive qualities beyond compliance.

---

## 2. Severity Levels

Severity levels describe **rule evaluation results** and are distinct
from top-level verdicts.

### ERROR

**Meaning**  
A mandatory WorldSeed rule is violated.

**Effect**  
Any ERROR-level finding results in a final verdict of NON-COMPLIANT.

**Non-Implication**  
ERROR does **NOT** indicate:
- runtime failure,
- software bug,
- low-quality data or models.

ERROR is a **normative violation**, not a technical one.

---

### WARNING

**Meaning**  
A non-fatal issue affecting clarity, completeness,
or future compatibility.

**Effect**  
WARNING does **NOT** invalidate compliance by itself.

**Non-Implication**  
WARNING does **NOT** relax any WorldSeed requirement.

---

## 3. Semantic Verdicts (Comparability)

Semantic verdicts apply to **claims, comparisons, or interpretations**
made on top of declared worlds.

They may be produced by WorldSeed Runtime tools,
or used normatively in publications and analyses.

---

### NOT COMPARABLE

**Meaning**  
Under the declared information, no well-defined semantic basis exists
to compare the referenced worlds, results, or learning claims.

**Implication**  
Any comparative claim **MUST** be withdrawn,
re-scoped, or restated with additional declarations.

**Non-Implication**  
NOT COMPARABLE does **NOT** imply:
- empirical invalidity,
- experimental failure,
- incorrect conclusions within a single world,
- lack of practical utility.

NOT COMPARABLE concerns **semantic comparability only**.

---

## 4. Relationship Between Verdicts and Rules

- Rule violations (`ERROR`) determine **compliance verdicts**
  (NON-COMPLIANT).
- BLOCKED indicates insufficient declaration prior to rule evaluation.
- Semantic verdicts (e.g., NOT COMPARABLE) operate **above compliance**
  and do not imply axiom violation.

These categories **MUST NOT** be conflated.

---

## 5. Final Statement

WorldSeed Lint does not evaluate performance, quality, usefulness,
or intelligence.

It evaluates the **legitimacy and scope of claims**.

A verdict defines **what may be said**, not **what may be built**.

End of Verdict Glossary.
