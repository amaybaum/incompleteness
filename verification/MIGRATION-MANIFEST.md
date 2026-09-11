# Verification layout - migration manifest

**This file moves nothing.** It records, for every artifact currently at the
`verification/` root, where the mechanical migration will place it, so that the migration
is a reviewable mapping rather than a judgement call made file by file while moving.

Base commit: `e0c0c709620db0d114dbd7061975b6747cb7aabc`. Artifacts classified: **91**
(plus `README.md`, `ROADMAP.md` and this file, which stay at the root). Flagged for owner
decision: **0**.

The machine-readable form is [`migration-manifest.json`](migration-manifest.json); the
migration reads that, not this table. Both are emitted by
`tools/build_migration_manifest.py` from one mapping, and the release gate runs that
script in `--check` mode, so a hand-edit to either generated file fails CI rather than
silently diverging.

## Why the destinations are shaped this way

Preregistration and outcome stay **together**, inside the round that produced them -
`act-07-dilation-choice/preregistration.md` beside `act-07-dilation-choice/result.md` -
rather than being split into global `preregistrations/` and `results/` folders. A reader
arriving at a round should find the freeze, the outcome and any amendments in one place;
that relationship is currently recoverable only by reading filenames.

Amendments sit in an `amendments/` subdirectory of their own round, which keeps the
append-only record legible as a sequence.

**Filenames carrying vocabulary this programme does not use in new prose are preserved
unchanged.** Renaming them would rewrite the historical record of what a round was called
at the time, and the rule governs prose we write, not the names of artifacts already
merged. Those rows are marked below.

## What is NOT moving

`lean/`, `lean-mathlib/` and `coverage/` stay exactly where they are. They are coherent
technical subsystems with their own structure and their own roadmaps; the disorder this
migration addresses is the research-control Markdown around them.

## The mapping

### `archive/superseded/`

| Current | Destination | Note |
| --- | --- | --- |
| `EQUIVALENCE-STRENGTHENING-ROADMAP-2026-09-05.md` | `EQUIVALENCE-STRENGTHENING-ROADMAP-2026-09-05.md` | superseded by COMPLETION-ASSUMPTION-AUDIT.md per its own header; historical filename preserved exactly |

### `audits/foundations/`

| Current | Destination | Note |
| --- | --- | --- |
| `C1C4-MINIMALITY-AUDIT.md` | `C1C4-MINIMALITY-AUDIT.md` | filename carries a term this programme does not use in new prose; the FILENAME is preserved unchanged rather than renamed |
| `C5-DISCOVERY-AUDIT.md` | `c5-discovery-audit.md` |  |
| `COHERENT-CONTINUUM-SOURCE-AUDIT.md` | `coherent-continuum-source-audit.md` |  |
| `DERIVED-Q3-AUDIT.md` | `derived-q3-audit.md` |  |
| `EXEC-SOURCE-AUDIT.md` | `exec-source-audit.md` |  |
| `FLOW-ENDPOINT-AUDIT.md` | `flow-endpoint-audit.md` |  |
| `FLOW-EXTENSION-AUDIT.md` | `flow-extension-audit.md` |  |
| `INVERSE-CLAUSE-AUDIT.md` | `inverse-clause-audit.md` |  |
| `LIFT-AUDIT.md` | `lift-audit.md` |  |
| `LIFT-SOURCE-AUDIT.md` | `lift-source-audit.md` |  |
| `MINIMAL-REPERTOIRE-AUDIT.md` | `MINIMAL-REPERTOIRE-AUDIT.md` | filename carries a term this programme does not use in new prose; the FILENAME is preserved unchanged rather than renamed |
| `OI-CORE-FORWARD-REDUNDANCY.md` | `oi-core-forward-redundancy.md` |  |
| `PAIR-FLOW-EQUIVALENCE-AUDIT.md` | `pair-flow-equivalence-audit.md` |  |
| `PHASE-PROPAGATION-AUDIT.md` | `phase-propagation-audit.md` |  |
| `PHASE-SOURCE-AUDIT.md` | `phase-source-audit.md` |  |
| `POLARIZATION-CLOSURE-AUDIT.md` | `polarization-closure-audit.md` |  |
| `Q3-PROPAGATION-AUDIT.md` | `q3-propagation-audit.md` |  |
| `REAL-PAIR-FLOW-AUDIT.md` | `real-pair-flow-audit.md` |  |
| `SCALAR-CLOSURE-AUDIT.md` | `scalar-closure-audit.md` |  |
| `STATE-MIXING-COUPLING-AUDIT.md` | `state-mixing-coupling-audit.md` |  |

### `audits/manuscript/`

| Current | Destination | Note |
| --- | --- | --- |
| `LEAN-MANUSCRIPT-CENSUS.md` | `lean-manuscript-census.md` |  |
| `OI-N-EXPLORATORY.md` | `oi-n-exploratory.md` |  |
| `OI-N-FREEZE.md` | `oi-n-freeze.md` |  |
| `REPRESENTATION-SECTOR-AUDIT.md` | `representation-sector-audit.md` |  |

### `audits/operational/`

| Current | Destination | Note |
| --- | --- | --- |
| `CENSUS-oi-compatible-theories.md` | `census-oi-compatible-theories.md` |  |
| `COMPLETION-ASSUMPTION-AUDIT.md` | `completion-assumption-audit.md` |  |
| `DENSE-INSTRUMENT-BRIDGE-AUDIT.md` | `dense-instrument-bridge-audit.md` |  |
| `DISCRETE-COMPLETION-AUDIT.md` | `discrete-completion-audit.md` |  |
| `INSTRUMENT-COMPLETION-AUDIT.md` | `instrument-completion-audit.md` |  |
| `INSTRUMENT-MIGRATION-AUDIT.md` | `instrument-migration-audit.md` |  |
| `INSTRUMENT-REALIZATION-AUDIT.md` | `instrument-realization-audit.md` |  |
| `MILESTONE-finite-quantum-instruments.md` | `milestone-finite-quantum-instruments.md` |  |
| `QUASILOCAL-COMPLETION-AUDIT.md` | `quasilocal-completion-audit.md` |  |
| `SOURCING-PROPAGATION-AUDIT.md` | `sourcing-propagation-audit.md` |  |
| `STOCHASTIC-OBSERVER-INTERFACE-AUDIT.md` | `stochastic-observer-interface-audit.md` |  |
| `TYPED-COMPLETION-AUDIT.md` | `typed-completion-audit.md` |  |

### `audits/operational/rooted-observer-family-sourcing/`

| Current | Destination | Note |
| --- | --- | --- |
| `ROOTED-OBSERVER-FAMILY-SOURCING-AUDIT-RESULT.md` | `result.md` |  |
| `ROOTED-OBSERVER-FAMILY-SOURCING-AUDIT.md` | `preregistration.md` |  |

### `audits/physical-realization/`

| Current | Destination | Note |
| --- | --- | --- |
| `CONTINUOUS-TIME-AUDIT.md` | `continuous-time-audit.md` |  |
| `CT3-R2B-Q2-PERIOD-AND-CYCLES.md` | `ct3-r2b-q2-period-and-cycles.md` |  |

### `audits/physical-realization/c4-causal-readback/`

| Current | Destination | Note |
| --- | --- | --- |
| `C4-CAUSAL-READBACK-AUDIT.md` | `preregistration.md` |  |

### `audits/physical-realization/c4-causal-readback/amendments/`

| Current | Destination | Note |
| --- | --- | --- |
| `C4-CAUSAL-READBACK-AUDIT-AMENDMENT-1.md` | `amendment-1.md` |  |
| `C4-CAUSAL-READBACK-AUDIT-AMENDMENT.md` | `amendment.md` |  |

### `audits/physical-realization/concrete-cut/`

| Current | Destination | Note |
| --- | --- | --- |
| `CONCRETE-CUT-AUDIT.md` | `preregistration.md` |  |
| `CONCRETE-CUT-FREEZE.md` | `freeze.md` |  |

### `programmes/hydrodynamics/`

| Current | Destination | Note |
| --- | --- | --- |
| `OI-HYDRODYNAMICS-SINGULARITY-RESEARCH-PROGRAMME.md` | `PROGRAMME.md` |  |

### `programmes/oi-qm/`

| Current | Destination | Note |
| --- | --- | --- |
| `OI-QM-RESEARCH-PROGRAMME.md` | `PROGRAMME.md` | the programme spine; a thin README.md index is added beside it |

### `programmes/oi-qm/amendments/`

| Current | Destination | Note |
| --- | --- | --- |
| `OI-QM-RESEARCH-PROGRAMME-AMENDMENT-1.md` | `amendment-1.md` |  |
| `OI-QM-RESEARCH-PROGRAMME-AMENDMENT-2.md` | `amendment-2.md` |  |

### `programmes/oi-qm/track-b/`

| Current | Destination | Note |
| --- | --- | --- |
| `BARANDES-REPRESENTATION-FREEDOM-SCOPING.md` | `representation-freedom-scoping.md` | a scoping note, not an act |

### `programmes/oi-qm/track-b/act-01-indivisibility/`

| Current | Destination | Note |
| --- | --- | --- |
| `BARANDES-INDIVISIBILITY-BRIDGE-AUDIT-RESULT.md` | `result.md` |  |
| `BARANDES-INDIVISIBILITY-BRIDGE-AUDIT.md` | `preregistration.md` |  |

### `programmes/oi-qm/track-b/act-01-indivisibility/amendments/`

| Current | Destination | Note |
| --- | --- | --- |
| `BARANDES-INDIVISIBILITY-BRIDGE-AUDIT-AMENDMENT-3.md` | `amendment-3.md` | amendments 1 and 2 are not separate root files; confirm during migration |

### `programmes/oi-qm/track-b/act-02-transpose-bridge/`

| Current | Destination | Note |
| --- | --- | --- |
| `BARANDES-TRANSPOSE-BRIDGE-PREREGISTRATION.md` | `preregistration.md` |  |
| `BARANDES-TRANSPOSE-BRIDGE-RESULT.md` | `result.md` |  |

### `programmes/oi-qm/track-b/act-03-candidate-selection/`

| Current | Destination | Note |
| --- | --- | --- |
| `BARANDES-CANDIDATE-SELECTION-PREREGISTRATION.md` | `preregistration.md` |  |
| `BARANDES-CANDIDATE-SELECTION-RESULT.md` | `result.md` |  |

### `programmes/oi-qm/track-b/act-04-dilation-mapping/`

| Current | Destination | Note |
| --- | --- | --- |
| `BARANDES-DILATION-MAPPING-PREREGISTRATION.md` | `preregistration.md` |  |
| `BARANDES-DILATION-MAPPING-RESULT.md` | `result.md` |  |

### `programmes/oi-qm/track-b/act-05-source-a-candidate/`

| Current | Destination | Note |
| --- | --- | --- |
| `BARANDES-SOURCE-A-CANDIDATE-PREREGISTRATION.md` | `preregistration.md` |  |
| `BARANDES-SOURCE-A-CANDIDATE-RESULT.md` | `result.md` |  |

### `programmes/oi-qm/track-b/act-06-tuple-instantiation/`

| Current | Destination | Note |
| --- | --- | --- |
| `BARANDES-TUPLE-INSTANTIATION-PREREGISTRATION.md` | `preregistration.md` |  |
| `BARANDES-TUPLE-INSTANTIATION-RESULT.md` | `result.md` |  |

### `programmes/oi-qm/track-b/act-07-dilation-choice/`

| Current | Destination | Note |
| --- | --- | --- |
| `BARANDES-DILATION-CHOICE-PREREGISTRATION.md` | `preregistration.md` |  |
| `BARANDES-DILATION-CHOICE-RESULT.md` | `result.md` |  |

### `programmes/oi-qm/track-b/boundary-audit/`

| Current | Destination | Note |
| --- | --- | --- |
| `BARANDES-BOUNDARY-AUDIT-RESULT.md` | `result.md` |  |
| `BARANDES-BOUNDARY-AUDIT.md` | `preregistration.md` |  |

### `programmes/oi-qm/track-i/arc-b-rooted-classification/`

| Current | Destination | Note |
| --- | --- | --- |
| `OI-ROOTED-CLASSIFICATION-AUDIT.md` | `preregistration.md` |  |
| `OI-ROOTED-CLASSIFICATION-RESULT.md` | `result.md` |  |

### `programmes/oi-qm/track-i/arc-c-quantum-representation/`

| Current | Destination | Note |
| --- | --- | --- |
| `OI-QUANTUM-REPRESENTATION-AUDIT.md` | `preregistration.md` |  |
| `OI-QUANTUM-REPRESENTATION-RESULT.md` | `result.md` |  |

### `programmes/oi-qm/track-i/arc-c-quantum-representation/amendments/`

| Current | Destination | Note |
| --- | --- | --- |
| `OI-QUANTUM-REPRESENTATION-AUDIT-AMENDMENT-1.md` | `amendment-1.md` |  |

### `programmes/oi-qm/track-i/arc-d-operational-sourcing/`

| Current | Destination | Note |
| --- | --- | --- |
| `OI-OPERATIONAL-SOURCING-AUDIT.md` | `preregistration.md` |  |
| `OI-OPERATIONAL-SOURCING-RESULT.md` | `result.md` |  |

### `programmes/oi-qm/track-i/arc-d-operational-sourcing/amendments/`

| Current | Destination | Note |
| --- | --- | --- |
| `OI-OPERATIONAL-SOURCING-AUDIT-AMENDMENT-1.md` | `amendment-1.md` |  |

### `programmes/oi-qm/track-i/causal-readback-discovery/`

| Current | Destination | Note |
| --- | --- | --- |
| `CAUSAL-READBACK-DISCOVERY-AUDIT.md` | `preregistration.md` |  |
| `CAUSAL-READBACK-DISCOVERY-RESULT.md` | `result.md` |  |

### `programmes/oi-qm/track-i/causal-readback-discovery/amendments/`

| Current | Destination | Note |
| --- | --- | --- |
| `CAUSAL-READBACK-DISCOVERY-AMENDMENT-1.md` | `amendment-1.md` |  |
| `CAUSAL-READBACK-DISCOVERY-RESULT-AMENDMENT-1.md` | `result-amendment-1.md` |  |

### `programmes/oi-qm/track-i/recurrence-scaling/`

| Current | Destination | Note |
| --- | --- | --- |
| `RECURRENCE-SCALING-AUDIT.md` | `preregistration.md` |  |
| `RECURRENCE-SCALING-RESULT.md` | `result.md` |  |

### `programmes/oi-qm/track-i/recurrence-tightness/`

| Current | Destination | Note |
| --- | --- | --- |
| `RECURRENCE-TIGHTNESS-AUDIT.md` | `preregistration.md` |  |
| `RECURRENCE-TIGHTNESS-RESULT.md` | `result.md` |  |

### `programmes/oi-qm/track-i/recurrence-tightness/amendments/`

| Current | Destination | Note |
| --- | --- | --- |
| `RECURRENCE-TIGHTNESS-AUDIT-AMENDMENT-1.md` | `amendment-1.md` |  |

### `programmes/substratum/`

| Current | Destination | Note |
| --- | --- | --- |
| `FROZEN-SUBSTRATUM-SOURCING-AUDIT.md` | `frozen-sourcing-audit.md` |  |
| `MANUSCRIPT-AXIOM-AUDIT.md` | `manuscript-axiom-audit.md` | the A1-A6 audit; the A6 roadmap row points here |
| `PRIMITIVE-SOURCE-AUDIT.md` | `primitive-source-audit.md` |  |
| `ROUTE-B-AUDIT.md` | `route-b-audit.md` | Route B of the substratum programme; unrelated to OI-QM Track B |
| `SUBSTRATUM-INTERFACE-AUDIT.md` | `interface-audit.md` |  |
| `SUBSTRATUM-SOURCE-AUDIT.md` | `source-audit.md` |  |

## Placement rule

New audits, preregistrations and results go under a programme or audit directory, never at
the `verification/` root (AGENTS.md §A.36). `tools/artifact_placement_check.py` enforces
this in the release gate, treating this manifest as the grandfather list: any **new**
root-level `verification/*.md` that is not in it fails.
