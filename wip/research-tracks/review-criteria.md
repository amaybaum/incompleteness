# Owner's review criteria for the current equivalence phase (2026-10-16)

## Track A — exact theorem correspondence
- Verify equality of the table actions with #829's specified CNOT and local-action formulas for all k (the finite check at k = 1..4 is a control, not the proof).
- Complete the carrier reindexing to #829's `Fin k`-indexed carriers.
- Recover the two-token theorem without invoking it, directly or through anything that depends on it.
- Keep every physical premise explicit in each bridged statement.

## Track B — local tomography
- #829 already assumes a Pauli-table carrier with local tomography built into its coordinates.
- A countermodel satisfying the product-level premises without local tomography shows only that those premises cannot source the carrier. It does not refute #829's conditional theorem.
- Verify that the alternative system's preparation, readout and reversible dynamics really arise from the claimed OI construction.

## Track C — spectrality versus symmetry
- Freeze the meaning of "symmetric" before drawing conclusions: a symmetric cone (homogeneous, self-dual) is not the same as strong symmetry of reversible transformations on distinguishable frames.
- Keep the common domain explicit: closed convex C, SEP ⊆ C ⊆ maxCone on Herm(4), trace-normalized.
- Distinguish mathematical effects from physically available effects.
- Do not silently import strong symmetry or the quantum cone.
- A positive symmetry theorem would not, by itself, establish complex quantum mechanics or its physical sourcing.

## Boundaries
- No further workflow edits.
- No premature F designations.
- No upgrade of a mathematical representation theorem to physical equivalence.

## Target
An audited sufficiency theorem, paired with a precise inventory of independently sourced and still-assumed physical principles.
