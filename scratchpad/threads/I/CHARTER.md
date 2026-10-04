# Thread I — Equivalence dependency frontier

## Status and base

- **Base:** `b7af4852b79fa3bfa90e9b5c2eca3aca6890395a` (sealed pre-L3B main / CC-2 landing).
- **Mode:** independent read-only research thread.
- **Relation to L3B:** none. This thread must not read from, write to, or interpret the evolving L3B execution branch or its unsealed outputs.
- **Relation to architectural round 2:** preparatory audit only. It does not start round 2, prove the SELECT composition theorem, or alter any round-2 premise.
- **Write scope:** this `scratchpad/threads/I/` directory only.
- **Forbidden writes:** Lean sources, verification programmes, manuscripts, ROADMAP, workflows, receipts, L3B records, or any certified artifact.

## Mission

Predict the minimum hypothesis package likely required for the full OI ↔ finite-dimensional complex-QM equivalence **before** attempting the final proof, by reconstructing the complete dependency frontier from the sealed corpus at the base above.

The thread is to work backwards from the intended final equivalence and classify every required arrow as one of:

1. **SEALED** — already proved at the base, with exact theorem identifier and source.
2. **ADAPTER** — mathematics is already present but theorem interfaces/types do not compose directly.
3. **LEMMA** — a substantive implication appears to be required but may be provable from existing premises.
4. **UNKNOWN** — implication status is genuinely unresolved and requires a proof-vs-countermodel test.
5. **INDEPENDENT/PREMISE** — a countermodel or sealed no-go shows the conclusion does not follow from the proposed antecedents, so an extra premise (or a stronger antecedent) is required.

Do not collapse **ADAPTER**, **LEMMA**, and **INDEPENDENT/PREMISE** into one category.

## Primary target chain

Reconstruct, using only sealed corpus statements at the base, the strongest justified chain of the form

[
\text{finite OI / observer premises}
\Longrightarrow
\text{finite representation}
\Longrightarrow
\text{selected/completed observable geometry}
\Longrightarrow
\text{3-ball + required effects}
\Longrightarrow
\text{complex composite structure}
\Longrightarrow
\text{full finite-dimensional QM}.
]

The already-established finite bridge (including the fixed-basis representation results) is an input, not something to re-prove.

## Mandatory frontier questions

Audit these separately rather than treating them as one package:

1. **SELECT composition target.** Determine the exact sealed theorem interfaces behind the proposed §4 composition target. In particular, locate and type-check the relevant forms of drivability / drive structure, boundary transitivity / orbit generation, completion, invariant-inner-product or ellipsoid structure, effect generation/sharpness, and energy-observable premises. Classify the missing glue as adapter vs substantive lemma.
2. **LIMCLOSE-C provenance.** Identify exactly what the final chain needs from completion/limit closure and whether the sealed finite hierarchy plus existing completion results already supply it. If not, state the weakest missing implication suitable for a deletion test.
3. **EO provenance.** Identify the exact operational content used under “energy observability” and whether any sealed theorem sources it from earlier observer/operational assumptions. Do not infer sourcing from names or manuscript prose.
4. **ORD∞ / TRANS / V4′.** Separate what each premise contributes, identify redundancy if any, and determine whether any is already a consequence of a stronger sealed drive/orbit hypothesis.
5. **Composite / G layer.** Reconstruct the exact nonlocal reversible/composite assumptions used by the dimension/complexity selector. Distinguish existence, composability, inverse/reversibility, readout, discard, positivity/cone preservation, and local tomography. Incorporate sealed no-go controls as independence evidence where applicable.
6. **Thread-H primitives.** Check whether register attachment, sharp register readout, reversible effect transport, discard, functoriality/composition, or matrix realization are already available under field-neutral names.
7. **Final identification.** State the remaining bridge from the selected GPT/ball/composite structure to the already-proved fixed-basis quantum representation. Distinguish definitional/type identification from new physics.
8. **Reverse direction.** Audit separately which existing constructions show that ordinary finite-dimensional complex QM satisfies the final premise bundle; do not assume the reverse implication is automatic.

## Method

### A. Backward proof plan

Write the desired final theorem as a dependency DAG without attempting proof. For every edge, record:

- antecedent theorem/predicate(s);
- consequent theorem/predicate;
- exact source identifiers;
- whether types line up literally;
- current classification;
- smallest missing statement if not SEALED.

### B. Deletion tests

For every candidate final premise `H`, formulate:

[
\text{all other currently proposed premises} \stackrel{?}{\Longrightarrow} H.
]

Run two conceptual tracks:

- **proof track:** identify an existing theorem or a plausible lemma route;
- **countermodel track:** search sealed controls / known models satisfying the antecedents while violating `H`.

The first decisive result determines whether `H` is derivable or must remain explicit.

### C. Anti-circularity

Every proposed derivation must be checked for dependence on the target itself or on a later equivalent form. In particular, do not source:

- ball geometry from a theorem already assuming the ball;
- EO from a theorem whose proof assumes the ellipsoid/ball conclusion EO is meant to help derive;
- composite richness from a matrix/Hilbert-space realization if the purpose is to derive that realization;
- local tomography from a result whose domain is already the quantum composite.

### D. Evidence bar

A row is **SEALED** only when its exact identifier and statement have been located at the pinned base. Design evidence, manuscript prose, comments, or intended architecture do not count.

A row is **INDEPENDENT/PREMISE** only with an explicit countermodel/no-go or a sealed theorem establishing non-implication. “No theorem found” is only **UNKNOWN**.

## Deliverables

1. `DEPENDENCY.md` — the end-to-end DAG with exact identifiers and classifications.
2. `FRONTIER.md` — only the currently missing arrows, each in minimal theorem form.
3. `DELETION_TESTS.md` — one proof-vs-countermodel test per questionable premise, prioritized by likely impact on the final theorem statement.
4. `MINIMAL_HYPOTHESES.md` — three bundles:
   - **currently sufficient on paper**;
   - **likely reducible**;
   - **currently evidenced independent**.
5. `RESULT.md` — concise verdict: predicted final theorem statement, unresolved premises, and which next lemma/countermodel would maximally reduce uncertainty.

## Priority order

1. Exact SELECT §4 composition interfaces.
2. LIMCLOSE-C.
3. EO.
4. Composite/G-layer provenance and local tomography.
5. Thread-H primitive reconstruction.
6. Final identification and reverse direction.

## Stop / escalation conditions

Stop and flag immediately if any of the following is found:

- an explicit sealed counterexample to the proposed final equivalence under the currently intended premise bundle;
- a circular dependency in the proposed selector/composite chain;
- a supposed SEALED ingredient that cannot be found at the pinned base;
- two “same” premises that are materially inequivalent rather than merely differently typed.

Otherwise the thread remains an audit: no theorem is to be claimed proved merely because the dependency graph appears routine.
