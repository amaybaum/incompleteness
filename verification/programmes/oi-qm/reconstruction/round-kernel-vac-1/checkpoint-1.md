# KERNEL-VAC-1 — checkpoint 1: original-predicate defect control

Status: candidate proof, ordinary CI and independent non-author review pending.
This is execution checkpoint **1 of at most 3**, not an E designation or receipt.

Owner execution authorization: [#1359 decision](https://github.com/amaybaum/incompleteness/pull/1359#issuecomment-6951772438).
Frozen F is `0c706277ae7f65ca9c09b91978839003640b07d1`, from D
`d4d0a07091926641dd3ee844807f41dae8a51d89`; the frozen preregistration is
unchanged. The published branch remains `round/kernel-vac-1-1188-20261117`.

The new module `OIBridge/ReadWriteNonvacuity.lean` states the exact compulsory
target `∀ T : FiniteOperationalTheory (Fin 2), ¬ ReadWriteSourced T` as
`OIBridge.ReadWriteNonvacuity.readWriteSourced_fin2_impossible`.
It derives identity availability at extension level one from `readout_avail`,
`readout_is_localLuders` and `availExt_coarse`. The same available channel has
the representative `Complex.I • 1`; its diagonal imaginary part rules out
every exact permutation matrix. The original predicate and implications are
unchanged. The contradiction is specifically on the nonempty `Fin 2 × Fin 1`
carrier; it makes no claim of an empty-carrier contradiction.

The module's root import, census disposition and axiom-report commands are in
the same commit. No local Lean, Mathlib build, numerical research or special
workflow launch was run. Kernel validation belongs to ordinary PR CI.

Unresolved: CI compilation/axioms; independent review; checkpoint 2's sole
`SubstratumInterface.MonomialSource (SubstratumInterfaceAudit.permTheory (Fin 2))`
target for every `n`, including zero, and every matrix representative;
checkpoint 3's citation/registry disposition. No witness or repair success is
claimed by this checkpoint. A failed control requires STOP; an unestablished
witness after a passing control takes the preregistered retirement branch.

Goal: [OI correctness issue #1188](https://github.com/amaybaum/incompleteness/issues/1188).
