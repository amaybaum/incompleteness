# HO-44 (v1) — equivalence → countermodels: a cone invariant under the gate and the full clause is `Q3` given H1 and H3; where an exotic cone must break

**From** `research/equivalence` (round 5, node E19; proposal HP-equivalence-16). **To** `research/countermodels`.
Written by the coordinator from the source thread's committed record; version 1, 2026-10-11. Reading: invariance;
nothing here is certified.

## Statements and labels

1. **Exotic cones must break the full clause.** `blockInvariant_of_drive` (EqvK2Generation.lean:448, design run
   38134245361): invariance under the gate, the flow at every angle and `cycEquiv` gives invariance under the
   block-diagonal `SU(2) × SU(2)`, and then, with H1 and H3, `K = Q3` (HO-43 item 2). So every exotic self-dual cone
   containing the products and invariant under the gate fails invariance under some flow angle or under `cycEquiv` —
   consistent with HO-32 item 4 (`Kk`: the drive flow without `J`) and with the tower's closure, which lacks the cyclic
   permutation (HO-40, HO-42). Label: CONJECTURE (design run).
2. **Theorem S′'s hypotheses for the Clifford chain, checked** (R-E19.1). For `K384`, `K768` and `KC` every hypothesis
   of `theorem_Sprime_ineq` holds exactly (orbit reduction verified on `K384`); `Kk` rests on the compact form, now
   design-built (HO-41, with the closedness remark at [W]). Label: CONJECTURE ([X]); the order 384 of
   `⟨CNOT, 1 ⊗ S, 1 ⊗ U_c⟩` modulo phase confirmed independently by the coordinator (`indep_checkE5.py` Z7).
3. **Tools in design**: `su_euler` (EqvK2Generation.lean:345: every special unitary is `diag(a, ā) R(c, s) diag(b, b̄)`,
   no angles), `rotRe_eq` (`cycMatᴴ diag(c − is, c + is) cycMat = [[c, −s], [s, c]]`), `rtrick` (:382:
   `(1, diag(r̄², r²)) = gate · (1 ⊗ diag(r, r̄)) · gate · (1 ⊗ diag(r̄, r))`), `blockMat_mul`, `conjInv_mul` /
   `conjInv_smul` (conjugation invariance closed under products and unit scalars).

## Evidence

| item | pointer |
|---|---|
| source | `research/equivalence` @ `3a46b811` |
| proposal | `handoff-proposals/HP-equivalence-16-countermodels-generation-tools-where-exotic-cones-must-break.md` (`a3eb5325…`) |
| module | `lean/EqvK2Generation.lean` (`f03c02ee…`), run 38134245361 |
| controls | `experiments/e19_s6_controls.py` (`80787ca1…`), replay identical |
| audit | `research/AUDITS/2026-10-11-round5/AUDIT-EQUIVALENCE-R5.md` |

## What the receiving thread may assume

Items 1–3 at their labels.

## What it may not assume

- that the design statements are certified;
- that a cone surviving the finite-order parts says anything about OI with continuous control.

## Receipt

The receiving thread copies this file into its `inbox/` with a commit naming `HO-44 v1` and records in its `LOG.md`
whether and how it relies on it.
