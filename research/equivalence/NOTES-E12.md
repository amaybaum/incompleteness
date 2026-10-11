# NOTES-E12 — draft S4's checkpoint `C0`: the repaired `EqvOmega4`, measured

Base L = `9f9f8257`. Draft S4 (`preregistration-drafts/S4-kinf-trans-separation.md`, KTRANS-SEP-1) was marked not ready to
freeze: its one design run (38090924005 on `195dfbee`) failed to build at two terms, and the proof-only repair
`95beab2b` (blob `9030f471`, copied as `lean/EqvOmega4.lean`) was committed and not dispatched. Its invariant table
names the open hazard as checkpoint `C0`: "a design run of the repaired module …, green at the Mathlib bridge build
with all fifteen prints standard, recorded in this file before `F`".

## S0 — predictions and the reading rule (written 2026-10-10T23:52Z, before the dispatch)

**What is dispatched.** `workflow_dispatch` of `verify.yml` on branch `dev-equivalence/omega4`, whose head is
`95beab2b` (checked with `git ls-remote` at 23:51Z): L + `OIBridge/EqvOmega4.lean` (repaired) + one import line in
`OIBridge.lean`. No further repair precedes the dispatch.

**Reading rule (fixed now).** `C0` is **MET** iff the Mathlib bridge job's Build step concludes `success` and each of
the fifteen `#print axioms` lines of `EqvOmega4` reads exactly `[propext, Classical.choice, Quot.sound]` (none with
`sorryAx`). Otherwise `C0` is **NOT MET**: S4 stays not ready, and the failing term is recorded. Read by S4's Q-SEP
rule (the statement surface only — the rule's "at `E`" clause cannot be read on a dev branch), `C0` MET supports
`KTRANS-SEP-SEPARATED` from a measurement; `C0` NOT MET leaves Q-SEP unsupported.

**Predictions (sign, strength, reason).**

- P1 — the Build step succeeds. Strength high (about 0.85). Reason: in run 38090924005 every declaration except the two
  `hsub` terms elaborated, and Lean's error recovery replaced each failing term by a sorry and went on elaborating the
  rest of the two proofs, so any further error in them would have been reported; the repair replaces each term by
  three standard tactic steps (`simp only [Set.mem_setOf_eq] at hv`, `rw [mem_omega4]`, `exact le_of_lt hv`). Residual
  risks: `simp only … at hv` making no progress (it should: `hv : v ∈ {v | …}`), and the dropped simp argument
  `Pi.sub_apply` in `omega4_centrallySymmetric` (the linter reported it unused in run 1, so its removal should be
  neutral).
- P2 — the fifteen prints are standard, none `sorryAx`. Same strength (it follows from P1: no declaration of the
  module uses `sorry` or an added axiom).
- P3 — release gate: `lean-axioms` OK with 5875 named results (L's 5860, from runs 38090116254 and 38091534622, plus the
  fifteen prints), no sorry; every step PASS except `lean-manuscript` (one problem: the unregistered module), since the
  branch is based on L with no `research/` tree.
- P4 — consequently S4's Q-SEP prediction `KTRANS-SEP-SEPARATED` becomes generated from a measurement, and S4 can be
  marked ready for owner review except for the items every draft lists as unmeasured (the predicted execution tree at a
  designated `D`: the module under its predicted name `TransSeparation`, the census family, `controls.py`, the probe
  shard).

**Productivity test (§A.31, fixed now).** E12 is closure-mode checkpointing, not gem-finding. A measurement counts if
it settles `C0` either way; a green build is POSITIVE (it validates the repair and generates S4's last unmeasured
prediction), not NEW; a red build is a hazard exposed (it would have voided a round frozen on the repair).

## The measurement (run 38096511360)

**Dispatch.** `workflow_dispatch` of `verify.yml` on `dev-equivalence/omega4`, run **38096511360** (run number 1860),
created 2026-10-10T23:52:27Z, `head_sha` `95beab2b48ab9a07dac820e1df7d0850828f5bec` (read from the run record).
Mathlib bridge job **114343410536**: Build step `success` (23:52:54–23:55:08Z), Release gate step `failure`
(23:55:08–23:55:55Z).

**Build step (job log).** `⚠ [3642/3644] Built OIBridge.EqvOmega4 (14s)`, warnings only: `Set.mem_setOf_eq` is
deprecated in favour of `Set.mem_ofPred_eq` (lines 158, 219 — the two repaired terms), `push_neg` is deprecated in
favour of `push Not` (line 166), one `unnecessarySeqFocus` lint (line 244). The fifteen prints, `EqvOmega4.lean:530–544`,
each `depends on axioms: [propext, Classical.choice, Quot.sound]`: `omega4_isCompact`, `conv_core`, `omega4_convex`,
`abstract_strict`, `omega4_strictConvex`, `relStrictConvex_omega4`, `singletonFaces_omega4`,
`omega4_interior_nonempty`, `omega4_centrallySymmetric`, `sharpSeed_omega4`, `omega4_drivable`,
`not_affine_eball_omega4`, `not_boundaryTransitive_omega4`, `not_denseBoundaryOrbit_omega4`, `kinfTrans_separation`.
`Build completed successfully (3644 jobs)`.

**Release gate (job log).** Every step PASS except `lean-manuscript` (`FAILED (1 problem(s))`: the unregistered design
module, by construction on a dev branch); `lean-axioms` `OK (5875 named result(s) reported, no sorr…)`; `claims`,
`duplicate`, `voice`, `mirror`, `staleness` PASS; `legacy-records` 303 records in 75 closed namespaces intact;
`v3-receipts` 43 hold.

**Reading by the rule fixed in S0.** Build `success` and the fifteen prints exactly `[propext, Classical.choice,
Quot.sound]`: **`C0` is MET.** P1, P2 and P3 held as predicted, P3 to the count (5875 = 5860 + 15). So S4's Q-SEP
prediction `KTRANS-SEP-SEPARATED` is now generated from a measurement (for the statement surface; the rule's "at `E`"
clause is the round's own), and the separation of K∞-Trans — Ω₄ is compact, convex, with interior, drivable, with a
sharp seed, relatively strictly convex and centrally symmetric, and no body-preserving family on it is boundary
transitive or has a dense boundary orbit — is kernel-checked in a design run: CONJECTURE [D], upgrading the
[W] + [X] evidence of R-E2.5 and the partial [D] of R-E8.3 (those rows are not edited). The module is the file already
kept as `lean/EqvOmega4.lean` (blob `9030f471`, sha256 `505a0784…`, checked equal to the dispatched blob).

**What S4 still lacks (as every draft).** The predicted execution tree at a designated `D` is unmeasured: the module
under its predicted name `TransSeparation` (namespace `OIBridge.TransSeparation`; a rename of the measured text), the
census family, `controls.py`, the probe shard. One optional pre-`F` revision item, warnings only: the two deprecated
names (`Set.mem_setOf_eq`, `push_neg`) could be replaced by `Set.mem_ofPred_eq` and `push Not`; neither affects the
build or a print. S4 is updated accordingly (status line, design table, predicted outputs, invariant row `C0`).

**Classification (§A.31).** POSITIVE: the repair was proof-only and the separation is kernel-checked in a design run;
no NEW finding (E12 is checkpointing). Pressure test of the favourable reading: the design run certifies nothing at L;
the separation says nothing about which bodies OI supplies (S4's non-inference rule), and HO-15 (received this round,
CONDITIONAL) adds that Aut(Ω₄) = O(3) × ℤ₂ with orbits the level sets of `s⁴`, which agrees with the separation and is
not used by it.
