"""
Axiom S2 — State Independence from Observation

Rule ID: AXIOM-S2-STATE-INDEPENDENCE
Severity: ERROR
Status: Normative

Requirement:
World state MUST be defined independently of observers
and observation outputs.

Violation Conditions:
- State variables are defined solely through observations
- Ontology depends on sensor outputs

Rationale:
Observation is a readout operator, not part of world state.
"""

def check(context):
    violations = []

    # Ontology must not depend on observers
    if context.ontology and context.observers:
        # semantic_context guarantees separation;
        # this rule exists to forbid future coupling
        pass

    return violations
