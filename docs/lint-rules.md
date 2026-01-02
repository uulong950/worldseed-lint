# WorldSeed Lint Rules

**RFC-Style Normative Rule Set**

**Status**: Normative  
**Scope**: Enforcement of WorldSeed Axioms (S1–S19)  
**Authority**: WorldSeed Constitution, Axioms, Manifest, Features, Operators

---

## 1. Terminology

The key words **“MUST”**, **“MUST NOT”**, **“REQUIRED”**, **“SHALL”**, **“SHALL NOT”**, **“SHOULD”**, **“SHOULD NOT”**, and **“MAY”** in this document are to be interpreted as described in [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119) and [RFC 8174](https://datatracker.ietf.org/doc/html/rfc8174).

- All rules in this document are **ERROR-level** unless explicitly stated otherwise.
- Violation of any rule defined herein **invalidates WorldSeed compliance**.

---

## 2. Rule Structure

Each rule specifies:

- **Rule ID** — globally unique identifier  
- **Enforces** — corresponding WorldSeed axiom(s)  
- **Requirement** — normative condition  
- **Violation Condition** — when the rule MUST trigger  
- **Lint Outcome** — compliance effect

---

## 3. Axiom Rules

### RULE AXIOM-S1-WORLD-ID

- **Enforces**: S1 (World Identity)  
- **Requirement**: A manifest MUST declare a globally unique and immutable `world.id`.  
- **Violation Condition**:  
  - `world.id` is missing, empty, or reused across distinct manifests.  
- **Lint Outcome**: ERROR — WorldSeed compliance invalid.

---

### RULE AXIOM-S2-STATE-INDEPENDENCE

- **Enforces**: S2 (State Independence from Observation)  
- **Requirement**: World state MUST be declared independently of observers and observations.  
- **Violation Condition**:  
  - State variables are defined solely via observer outputs.  
  - Ontology depends on observation artifacts.  
- **Lint Outcome**: ERROR.

---

### RULE AXIOM-S3-EXPLICIT-STATE

- **Enforces**: S3 (Explicit State Declaration)  
- **Requirement**: All world state dimensions relevant to learning MUST be explicitly declared.  
- **Violation Condition**:  
  - Undeclared state dimensions are referenced or implied.  
- **Lint Outcome**: ERROR.

---

### RULE AXIOM-S4-NO-SPONTANEOUS-CHANGE

- **Enforces**: S4 (No Spontaneous State Change)  
- **Requirement**: World state MUST change only through explicitly declared actions.  
- **Violation Condition**:  
  - State change occurs without a corresponding declared action.  
- **Lint Outcome**: ERROR.

---

### RULE AXIOM-S5-ACTION-COMPLETENESS

- **Enforces**: S5 (Action Completeness)  
- **Requirement**: All admissible state-modifying actions MUST be declared.  
- **Violation Condition**:  
  - Hidden, manual, or implicit actions affect world state.  
- **Lint Outcome**: ERROR.

---

### RULE AXIOM-S6-ACTION-SEMANTICS

- **Enforces**: S6 (Action Semantics)  
- **Requirement**: Each action MUST declare parameters with explicit units and provenance.  
- **Violation Condition**:  
  - Action parameters lack units.  
  - Provenance is missing or implicit.  
- **Lint Outcome**: ERROR.

---

### RULE AXIOM-S7-ACTION-DETERMINISM

- **Enforces**: S7 (Action Determinism Declaration)  
- **Requirement**: Actions MUST be deterministic unless stochasticity is explicitly declared.  
- **Violation Condition**:  
  - Non-repeatable actions are not marked stochastic.  
  - Randomness is undeclared.  
- **Lint Outcome**: ERROR.

---

### RULE AXIOM-S8-OBSERVER-NON-INTERVENTION

- **Enforces**: S8 (Observer Non-Intervention)  
- **Requirement**: Observers MUST NOT modify world state.  
- **Violation Condition**:  
  - Observer operation causes or implies state change.  
- **Lint Outcome**: ERROR.

---

### RULE AXIOM-S9-EXPLICIT-OBSERVER

- **Enforces**: S9 (Explicit Observer Definition)  
- **Requirement**: All observations MUST be attributable to explicitly declared observers.  
- **Violation Condition**:  
  - Observations exist without an associated observer definition.  
- **Lint Outcome**: ERROR.

---

### RULE AXIOM-S10-OBSERVER-STABILITY

- **Enforces**: S10 (Observer Stability)  
- **Requirement**: Observer parameters MUST remain fixed unless explicitly changed via actions.  
- **Violation Condition**:  
  - Observer drift, recalibration, or mutation occurs without declaration.  
- **Lint Outcome**: ERROR.

---

### RULE AXIOM-S11-OBSERVATION-SEMANTICS

- **Enforces**: S11 (Observation Operator Semantics)  
- **Requirement**: Each observer MUST declare its observation operator and uncertainty.  
- **Violation Condition**:  
  - Missing operator definition.  
  - Missing noise or uncertainty declaration.  
- **Lint Outcome**: ERROR.

---

### RULE AXIOM-S12-SENSING-BOUNDARY

- **Enforces**: S12 (Sensing Boundary Declaration)  
- **Requirement**: Each observer MUST declare a sensing boundary.  
- **Violation Condition**:  
  - Boundary is missing, implicit, or undefined.  
- **Lint Outcome**: ERROR.

---

### RULE AXIOM-S13-BOUNDARY-RESPECT

- **Enforces**: S13 (Boundary Respect)  
- **Requirement**: Distinctions outside the declared sensing boundary MUST be treated as inaccessible.  
- **Violation Condition**:  
  - Claims, features, or inferences rely on information beyond the boundary.  
- **Lint Outcome**: ERROR.

---

### RULE AXIOM-S14-EXPLICIT-IRREVERSIBILITY

- **Enforces**: S14 (Explicit Irreversibility)  
- **Requirement**: All irreversible operations MUST be explicitly declared.  
- **Violation Condition**:  
  - Quantization, compression, clipping, or projection occurs without declaration.  
- **Lint Outcome**: ERROR.

---

### RULE AXIOM-S15-NO-IMPLICIT-RECONSTRUCTION

- **Enforces**: S15 (No Implicit Reconstruction)  
- **Requirement**: Irreversibly destroyed distinctions MUST NOT be implicitly reconstructed.  
- **Violation Condition**:  
  - Attempt to recover or infer irreversibly lost information without declared priors.  
- **Lint Outcome**: ERROR.

---

### RULE AXIOM-S16-NUMERICAL-SEMANTICS

- **Enforces**: S16 (Numerical Type Semantics)  
- **Requirement**: All numerical values MUST carry explicit physical semantics.  
- **Violation Condition**:  
  - Bare numbers appear without unit or uncertainty.  
- **Lint Outcome**: ERROR.

---

### RULE AXIOM-S17-NO-IMPLICIT-CASTING

- **Enforces**: S17 (No Implicit Casting)  
- **Requirement**: Numerical type casting MUST NOT be implicit.  
- **Violation Condition**:  
  - Normalization, scaling, or type conversion occurs without declaration.  
- **Lint Outcome**: ERROR.

---

### RULE AXIOM-S18-CLAIM-SCOPE

- **Enforces**: S18 (Claim Scope Limitation)  
- **Requirement**: All claims MUST be scoped to the declared world, profile, observers, and boundaries.  
- **Violation Condition**:  
  - Declared profile exceeds satisfied requirements.  
  - Claims exceed manifest scope.  
- **Lint Outcome**: ERROR.

---

### RULE AXIOM-S19-DISTINGUISHABILITY

- **Enforces**: S19 (Distinguishability Preservation)  
- **Requirement**: All transformations MUST declare which distinctions are preserved and which are destroyed.  
- **Violation Condition**:  
  - Data transformations lack declared degradation semantics.  
- **Lint Outcome**: ERROR.

---

## 4. Compliance Determination

- A manifest MUST satisfy all rules applicable to its declared profile.  
- Failure of **any** rule defined in this document **invalidates WorldSeed compliance**.  
- There is **no partial pass** for axiom rules.

---

## 5. Final Statement

> **WorldSeed-Lint does not evaluate performance, quality, or usefulness.**  
> It evaluates **legitimacy of claims**.

A world that violates these rules  
**MUST NOT** be described as a **WorldSeed-compliant world**.

---

*End of WorldSeed Lint Rules (S1–S19)*