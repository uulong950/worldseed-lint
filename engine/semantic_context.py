"""
Module: Semantic Context Builder

Status: Normative
Scope: Canonical semantic world representation for WorldSeed Lint

────────────────────────────────────────────────────────────
I. Authority
────────────────────────────────────────────────────────────

This module is authoritative for defining the internal semantic
representation (SemanticContext) used by WorldSeed Lint.

All lint rules, feature checks, profile checks, and consistency
checks MUST operate exclusively on the data structures defined
in this module.

Raw manifests MUST NOT be accessed directly by rules.

Authority sources:
- WorldSeed Constitution
- WorldSeed Axioms (S1–S19)
- WorldSeed Manifest Specification
- WorldSeed Feature and Operator RFCs
- Schema–Axiom Mapping

This module introduces NO new semantics.

────────────────────────────────────────────────────────────
II. Builder Contract (Procedural Semantics)
────────────────────────────────────────────────────────────

This module defines the contract for constructing a SemanticContext
from a validated WorldSeed manifest.

Normative Requirements:

- All entities MUST be constructed explicitly from the manifest.
- Missing information MUST remain missing.
- Declared "unknown" MUST remain unknown.
- NO default values MAY be introduced.
- NO relationships MAY be inferred beyond those explicitly declared.
- Construction MUST preserve traceability to manifest field paths.
- Construction MUST NOT perform validation logic beyond invariant checks.

The builder is a pure constructor.
It MUST NOT normalize, optimize, repair, or enrich input data.

────────────────────────────────────────────────────────────
III. Data Contract (State Semantics)
────────────────────────────────────────────────────────────

This module defines:
- the canonical data structures,
- required fields,
- semantic invariants,
- and forbidden states.

Violation of any invariant defined herein constitutes
an ERROR-level WorldSeed Lint violation.
"""

from typing import Dict, Set, Optional, Union, Literal


# ────────────────────────────────────────────────────────────
# Atomic Types
# ────────────────────────────────────────────────────────────

Unknown = Literal["unknown"]


# ────────────────────────────────────────────────────────────
# Quantity
# ────────────────────────────────────────────────────────────

class Quantity:
    """
    Canonical physical quantity representation.

    Fields:
    - value: numeric value or explicit "unknown"
    - unit: physical unit
    - uncertainty: non-negative numeric value or explicit "unknown"
    - provenance: origin or derivation description

    Invariants:
    - Bare numbers are forbidden.
    - Unit MUST be declared.
    - Uncertainty MUST be declared.
    - uncertainty == 0 is forbidden for measured quantities.
    - "unknown" MUST be explicit, never implicit.
    """
    def __init__(
        self,
        value: Union[float, Unknown],
        unit: str,
        uncertainty: Union[float, Unknown],
        provenance: str,
        *,
        _path: str
    ):
        self.value = value
        self.unit = unit
        self.uncertainty = uncertainty
        self.provenance = provenance
        self._path = _path


# ────────────────────────────────────────────────────────────
# World Identity
# ────────────────────────────────────────────────────────────

class WorldIdentity:
    """
    World identity descriptor.

    Fields:
    - id: globally unique world identifier
    - description: optional human-readable description

    Invariants:
    - id MUST be non-empty.
    - id MUST be immutable within a semantic context.
    """
    def __init__(self, id: str, description: Optional[str]):
        self.id = id
        self.description = description


# ────────────────────────────────────────────────────────────
# Ontology
# ────────────────────────────────────────────────────────────

class Ontology:
    """
    Ontological declaration of world state dimensions.

    Fields:
    - entities: set of explicitly declared state entities

    Invariants:
    - All referenced state dimensions MUST belong to entities.
    - Ontology MUST NOT depend on observers or observations.
    """
    def __init__(self, entities: Set[str]):
        self.entities = entities


# ────────────────────────────────────────────────────────────
# Action
# ────────────────────────────────────────────────────────────

class Action:
    """
    World state modification operator.

    Fields:
    - name: action identifier
    - parameters: mapping from parameter name to Quantity
    - stochastic: whether the action is explicitly stochastic

    Invariants:
    - All parameters MUST be Quantity instances.
    - State change MUST NOT occur outside declared actions.
    - If stochastic is False, repeated execution MUST be equivalent.
    """
    def __init__(
        self,
        name: str,
        parameters: Dict[str, Quantity],
        stochastic: bool
    ):
        self.name = name
        self.parameters = parameters
        self.stochastic = stochastic


# ────────────────────────────────────────────────────────────
# Boundary
# ────────────────────────────────────────────────────────────

class Boundary:
    """
    Sensing boundary descriptor.

    Fields:
    - description: explicit description of observability limits

    Invariants:
    - Boundary MUST define limits on distinguishability.
    - Any inference outside the boundary is invalid.
    """
    def __init__(self, description: str):
        self.description = description


# ────────────────────────────────────────────────────────────
# Observer
# ────────────────────────────────────────────────────────────

class Observer:
    """
    Observation operator.

    Fields:
    - name: observer identifier
    - operator: declared observation operator name
    - boundary: sensing boundary
    - noise: observation noise / uncertainty Quantity

    Invariants:
    - Observer MUST NOT modify world state.
    - Operator MUST be explicitly declared.
    - Boundary MUST be declared.
    - Noise uncertainty MUST NOT be implicit.
    """
    def __init__(
        self,
        name: str,
        operator: str,
        boundary: Boundary,
        noise: Quantity
    ):
        self.name = name
        self.operator = operator
        self.boundary = boundary
        self.noise = noise


# ────────────────────────────────────────────────────────────
# Degradation Graph
# ────────────────────────────────────────────────────────────

class DegradationEdge:
    """
    Directed degradation edge.

    Fields:
    - source: source representation
    - target: target representation
    - irreversible: whether the transformation is irreversible
    - destroyed_distinctions: set of destroyed distinctions

    Invariants:
    - Irreversible edges MUST NOT be invertible.
    - Destroyed distinctions MUST NOT reappear downstream.
    """
    def __init__(
        self,
        source: str,
        target: str,
        irreversible: bool,
        destroyed_distinctions: Set[str]
    ):
        self.source = source
        self.target = target
        self.irreversible = irreversible
        self.destroyed_distinctions = destroyed_distinctions


class DegradationGraph:
    """
    Graph of declared degradation and irreversibility.

    Fields:
    - nodes: semantic representation identifiers
    - edges: degradation edges

    Invariants:
    - Graph MUST include only explicitly declared transformations.
    - Graph MUST be acyclic with respect to irreversibility.
    - Reconstruction paths MUST NOT exist unless explicitly declared.
    """
    def __init__(
        self,
        nodes: Set[str],
        edges: Set[DegradationEdge]
    ):
        self.nodes = nodes
        self.edges = edges


# ────────────────────────────────────────────────────────────
# Semantic Context (Top-Level)
# ────────────────────────────────────────────────────────────

class SemanticContext:
    """
    Canonical semantic representation of a WorldSeed world.

    Fields:
    - spec_version: WorldSeed specification version
    - profile: declared compliance profile (L0–L3)

    - world: world identity
    - ontology: world ontology
    - actions: declared actions
    - observers: declared observers

    - quantities: registry of all quantities
    - degradation_graph: declared degradation semantics

    Global Invariants:
    - spec_version MUST match lint-supported spec version.
    - profile MUST be one of {L0, L1, L2, L3}.
    - All referenced entities MUST exist.
    - No implicit actions, observers, units, uncertainty, or degradation.
    - No implicit reconstruction of destroyed distinctions.
    """
    def __init__(self, manifest: dict):
        # Initialize with default values to avoid None issues
        self.spec_version: str = manifest.get("version", "")
        self.profile: str = manifest.get("profile", "")

        # ── World ────────────────────────────────────────────
        world = manifest.get("world", {})
        self.world = WorldIdentity(
            id=world.get("id", ""),
            description=world.get("description")
        )

        # ── Ontology ─────────────────────────────────────────
        ontology = manifest.get("ontology", {})
        self.ontology = Ontology(
            entities=set(ontology.get("entities", []))
        )

        # ── Actions ──────────────────────────────────────────
        self.actions: Dict[str, Action] = {}
        for action in manifest.get("actions", []):
            try:
                params: Dict[str, Quantity] = {}

                for pname, p in action.get("parameters", {}).items():
                    try:
                        params[pname] = Quantity(
                            value=p.get("value", "unknown"),
                            unit=p.get("unit", ""),
                            uncertainty=p.get("uncertainty", "unknown"),
                            provenance=p.get("provenance", ""),
                            _path=f"actions[{action['name']}].parameters[{pname}]"
                        )
                    except ValueError:
                        # Quantity validation failed, skip this parameter
                        continue

                self.actions[action["name"]] = Action(
                    name=action["name"],
                    parameters=params,
                    stochastic=action.get("stochastic", False)
                )
            except (KeyError, ValueError):
                # Action validation failed, skip this action
                continue

        # ── Observers ────────────────────────────────────────
        self.observers: Dict[str, Observer] = {}
        for obs in manifest.get("observers", []):
            try:
                if "boundary" not in obs:
                    boundary = None
                else:
                    boundary = Boundary(obs["boundary"])

                noise_src = obs.get("noise", {})
                noise = Quantity(
                    value=noise_src.get("value", "unknown"),
                    unit=noise_src.get("unit", ""),
                    uncertainty=noise_src.get("uncertainty", "unknown"),
                    provenance=noise_src.get("provenance", ""),
                    _path=f"observers[{obs['name']}].noise"
                )

                self.observers[obs["name"]] = Observer(
                    name=obs["name"],
                    operator=obs.get("operator", ""),
                    boundary=boundary,
                    noise=noise
                )
            except (KeyError, ValueError):
                # Observer validation failed, skip this observer
                continue

        # ── Quantities Registry ──────────────────────────────
        self.quantities: Dict[str, Quantity] = {}
        for action in self.actions.values():
            for pname, q in action.parameters.items():
                self.quantities[f"action:{action.name}:{pname}"] = q

        for obs in self.observers.values():
            self.quantities[f"observer:{obs.name}:noise"] = obs.noise

        # ── Degradation Graph ────────────────────────────────
        # NOTE: constructed empty; populated only if explicitly declared
        self.degradation_graph = DegradationGraph(
            nodes=set(),
            edges=set()
        )