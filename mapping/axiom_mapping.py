"""
Axiom–Rule Mapping Accessor

Status: Normative
Scope: Read-only mapping between axioms and lint rules

Responsibilities:
- Provide a canonical mapping from:
  - Axiom ID → Rule IDs
  - Rule ID → Axiom ID
- Ensure traceability of violations to specification axioms

Normative Requirements:
- Mapping MUST be treated as authoritative.
- Mapping MUST be immutable at runtime.
- Lint rules MUST NOT hardcode axiom semantics
  outside this mapping.

This module introduces NO new semantics.
"""

AXIOM_RULE_MODULES = {
    "S1": "rules.axioms.s1_world_identity",
    "S2": "rules.axioms.s2_state_independence",
    "S3": "rules.axioms.s3_explicit_state",
    "S4": "rules.axioms.s4_no_spontaneous_change",
    "S5": "rules.axioms.s5_action_completeness",
    "S6": "rules.axioms.s6_action_semantics",
    "S7": "rules.axioms.s7_action_determinism",
    "S8": "rules.axioms.s8_observer_non_intervention",
    "S9": "rules.axioms.s9_explicit_observer",
    "S10": "rules.axioms.s10_observer_stability",
    "S11": "rules.axioms.s11_observation_semantics",
    "S12": "rules.axioms.s12_sensing_boundary",
    "S13": "rules.axioms.s13_boundary_respect",
    "S14": "rules.axioms.s14_explicit_irreversibility",
    "S15": "rules.axioms.s15_no_implicit_reconstruction",
    "S16": "rules.axioms.s16_numerical_semantics",
    "S17": "rules.axioms.s17_no_implicit_casting",
    "S18": "rules.axioms.s18_claim_scope",
    "S19": "rules.axioms.s19_distinguishability",
}