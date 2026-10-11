# HP-10 — to the coordinator: S4 ready, S6's skeleton kernel-checked in design, and the infinite-volume form of H-DYN (research only)

From `research/equivalence`, round 3 (E12, E11, E14), base L = `9f9f8257`. Nothing here is certified; no preregistration
became a round.

1. **Draft S4 is ready for owner review** (E12, R-E12.1). Its checkpoint `C0` is met: the repaired `EqvOmega4` builds over
   L with all fifteen prints standard (run 38096511360, Mathlib bridge job 114343410536; gate red only at
   `lean-manuscript`, `lean-axioms` 5875). The draft's predicted outputs are now generated from that run. Optional
   pre-`F` edit: two deprecated names (`Set.mem_setOf_eq`, `push_neg`) produce warnings only.
2. **S6's skeleton is kernel-checked in a design run** (E11, R-E11.1–R-E11.3). `EqvK2Schema` (22 prints standard, run
   38101580750, job 114358419270) proves the dictionary `W 3 ≃ₗ[ℝ] Herm(ℂ² ⊗ ℂ²)` with both compatibilities, the cone
   step (LOWER, UPPER, `Q3 = dualW Q3`) and the assembly `pairCone_eq_Q3_of_drive` with L4 isolated as the hypothesis
   `ReachPure`. A preregistration for S6 can now cite a built module (the analogue of S4's `C0`); the theorem remains
   CONDITIONAL on H2, H3, A_miss and `ReachPure`; by HO-10 item 1 (CONJECTURE) a reachability hypothesis of this kind
   can hold only for a repertoire whose compact closure has a non-abelian identity component (the drive words' closure
   contains `SO(3)` on one token, R-E10.x).
3. **Level III, infinite volume** (E14, R-E14.1–R-E14.3; LEDGER row L3-conv). NOTES-E9's H-DYN is a top-stage condition.
   Read at every finite stage of an infinite lattice ("every stage matrix unit to a stage matrix unit") it forces a site
   permutation with relabelings and excludes OI's own interacting dynamics (exact: 48 of 40320 at `N = 3`; the CNOT
   update violates it). The form that works is the transport form — stage matrix units to `{0,1}`-matrices, with
   `LocalityPreserving` for the automorphism and its inverse — which yields a `ReversibleDynamics` and a Target A system
   (written proof). **Marker:** a Level III statement in infinite volume that repairs the dynamical converse must use the
   transport form; like H-DYN it restates (O3) on the stages and derives no dynamics.

**May not be assumed:** that any of these is certified at L; that S4 or an S6 draft has been executed; that the
transport-form passage is kernel-checked.
