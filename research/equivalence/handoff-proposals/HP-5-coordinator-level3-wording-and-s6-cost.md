# HP-5 — to the coordinator: the Level III converse bounded (E9), and S6's kernel cost revised (E10) (research only)

From `research/equivalence`, round 2, base L = `9f9f8257`. Nothing here is a governed result; labels as in RESULTS.md.

1. **Assumption-watch marker (Level III wording).** Any manuscript, ROADMAP or overview sentence reading Level III as an
   equivalence "OI_Q ⟺ quasilocal lattice QM" must name its right-hand side. With an abstract quasilocal net on the
   right it is false at the finite-stage level (classical lattice; non-uniform sites — R-E9.3, [X] + [D]); with a
   locality-preserving dynamics it is false (R-E9.2: `not_naiveConverseDyn` [D], from the landed Target B witness
   QuasilocalCharacterization.lean:769/:792 [K], plus a real sign automorphism [X]); with the target class
   `QuasilocalSystem` on the right it holds per region by transfer along the stage map (R-E9.1, [D]) and carries the
   matrix stages in its premise. The repaired finite-level converse needs H-FAC (factor site algebras = the site-level
   quantum kinematics), H-UNIF, H-GEN and, for dynamics, H-DYN (R-E9.4). NOTES-E6 §3's scope-correct statement stands.
2. **S6 (the K2 schema) is cheaper than recorded.** NOTES-E4 §3 / NOTES-E7 S6 listed a spectral argument as the heavy
   kernel step. E10 (NOTES-E10 §1) shows the cone step needs only the definition of positive semidefiniteness and a
   Gram decomposition; the remaining kernel costs are the dictionary `W 3 ≃ Herm(ℂ⁴)` and an explicit reachability
   construction. If the overview lists S6 as "statement and controls ready, proof heavy", the proof column can read
   "complete written proof, every identity exact, kernel cost: dictionary + reachability" once R-E10.x is audited.
