# HP-equivalence-17 — to the coordinator: E20–E22 deferred to round 6, their state (research only; WIP, unverified)

From `research/equivalence`, round 5, by the owner's direction of 10:38Z. No result row exists for E20–E22.

1. **E20** (E16's residual, odd chart dimension ≥ 5 with K∞-Geom): NOTES-E20 S0 and S0-b; probe
   `experiments/e20_odd_bodies.py` runs 1 and 2 kept (`.run1.*`, `.run2.*`), both `VERDICT NOT RENDERED`: the
   positive control's cutting-plane LP (`eball 3`) does not converge in 40 rounds (margin `6.24·10⁻³`, violations of
   order `10⁻²` each round — not the tolerance stall S0-b supposed). Recorded, not concluded: the sector family meets
   the count and fails K∞-Geom exactly; the `(3; 3, 3, 3)` sector gate meets frame, `relT`, `relC` exactly; the `posFwd`
   relaxation's float candidates for `eball 5` and `Ω⋆⁵` violate `posInv` on the pool (the kernel's `d ≠ 5` exclusion
   runs through `posInv`: `gate_corner_symm`, `lor_Minv`). Round 6 needs a converging separation (more rounds or an
   exact positive-control check) before any verdict.
2. **E21** (the infinite-volume passage of the transport form): NOTES-E21 S0 only — the decomposition of `Passage` into
   (P1) uniqueness of extension, (P2) matrix units suffice, (P3) diagonal preservation, (P4) the construction lemma
   `PassageUnits`, with (iii)'s dependence on the maximal abelianness of the diagonal [L] as an assumption-watch
   marker; no module written.
3. **E22** (one dictionary): `lean/EqvOneDictionary.lean` built in design run 38132266383 (10/10 prints standard) —
   §A's two directions between S6's clause and the bridge's `TransferClause` and §C's `transferClause_of_blockInvariant`
   were built because they were queued; their analysis (NOTES-E22) is round 6's. Its §B is part of E19 (R-E19.5).

**May not be assumed:** any E20 or E21 conclusion; that the E22 statements were reviewed as a node.
