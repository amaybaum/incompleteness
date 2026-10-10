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
