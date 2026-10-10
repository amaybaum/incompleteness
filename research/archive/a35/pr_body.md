## A35 — the Diţă hulls of the product-embedded stratum: control plane (merge-held)

A native round under `AGENTS.md` §A.39, drafted from `D = 100bb1e86931fa769a200e9b117f4f9fb0a745b9` (A34 landed and certified). This pull request carries the preregistration alone; `F` is not designated, and nothing lands until the round's receipt holds.

**What is frozen.** Fifteen propositions and the corollary in `OIBridge/DitaHull.lean` (all elaborate: run 36308085118 and run 36309156707, three jobs green; countercontrol run 36308759834 red at exactly one planted error): the column and row Diţă constructions realizable for every choice of flat unitary factors and unit twist phases; both hulls contain the stratum; the cross-ratio identity of product tuples; act 34's properness witness as the exact column relabelling of `F₄(i) ⊗ F₄(i)` (off the stratum, on the locus); a twisted point and the second real class of order sixteen off the stratum; a non-product relabelling carrying a stratum point off the stratum inside its isometry class; the product relabellings and conjugation preserving the column hull with the transpose exchanging the hulls; the twist phases entering the feature vector injectively modulo the gauges, so the hull through one point is infinite and no finite set of maps identifies it.

**The exact-computation layer.** The frozen probe `verification/lean/dita_defect_probe.py` (blob `0570327f3a89927e803f3d6b68fdb5142c766b08`, wired into the probes job) replays by integer and Gaussian-rational arithmetic: the defect strata 105 / 73 / 57 at the fourth-root stratum points, 49 at a rational stratum point and at the twisted point, 17 on the generic hull, 105 at both real classes; the hull tangent rank 26 against the defect 49 at the stratum point; a twenty-point census of hull classes off the Kronecker locus by exact invariants; the matrix-induced subgroup of act 33's group (order 2304, index 16); two stabilizers.

**The open modulus**, recorded and not decided: whether every realizable class sufficiently near the stratum lies in some relabelled Diţă hull. Its frozen countercontrol is `26 ≠ 49`.

Labels: `A35-DITA-STRATIFIED` / `A35-NOT-DITA-STRATIFIED` / `A35-UNDECIDED`. Controls `controls.py` (blob `52009e086a3079b8c3bf50621d6f68d8f35c7530`, self-test: 3 rows, 8 duality mutations, 74 mutation controls) is held off the repository until stage 1.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01XEQMD5kRhaU9WyeZt6dmM1
