# NOTES-E15 — draft S6 (K2-SCHEMA-1) in the native V3 format: the module, the named hypothesis, the countercontrol

Base L = `9f9f8257`. Node E15 of round 4: a preregistration draft for the K2 schema round, citing the built design
module `EqvK2Schema` (run 38101580750, 22/22 prints standard; NOTES-E11), with `ReachPure` as the named hypothesis and
HO-24's explicit exotic cone for the finite clause as the countercontrol. A draft only: nothing is activated, nothing is
placed under `verification/`.

## S0 (written 2026-10-11T03:08Z, before the probe's first run)

**What E15 is (§A.31).** Closure-mode drafting, not gem-finding. The draft counts if (a) the predicted outputs of its
kernel cells are generated from a measured design run of the frozen statement surface (run 38101580750), (b) the
predicted output of its exact cell is generated from a run of the probe it would freeze, (c) the countercontrol is
recomputed by this thread rather than cited, and (d) the A_miss hypothesis and the named hypothesis are stated exactly
as the module carries them. A discrepancy with HO-24 exposed by the recomputation would be NEW; otherwise the node is
POSITIVE (drafting).

**The draft's decisions (fixed now).**
- Round id `K2-SCHEMA-1`, kind non-sealing; module `OIBridge/K2Schema.lean`, namespace `OIBridge.K2Schema`, a rename of
  `EqvK2Schema` (blob `659ae36c`) with no statement changed; 22 `#print axioms` lines.
- Three cells, each with its own rule: Q-CONE (the dictionary as a linear equivalence with its product law and pairing;
  LOWER, UPPER; `Q3 = dualW Q3`), Q-SCHEMA (`driveWords_preserve`, `pairCone_eq_Q3_of_drive`), Q-EXACT (the frozen
  probe).
- A_miss in the form the module carries: invariance under `actT (rotLin t)` for every `t` and under `actT cycEquiv` (the
  full flow, HO-5). HO-13 item 2's two-rotation clause (`R_z(θ₀)`, `cos θ₀ = 3/5`, and `cycEquiv` only) is recorded as
  the stronger theorem S6 does not formalize (the passage to the flow needs `K` closed, which H3 supplies, and the
  density of `⟨R_z(θ₀)⟩` in the axis circle, neither in the module).
- `ReachPure` is the named hypothesis: a statement about the drive words only, with no OI content, proved in writing
  (NOTES-E10 L4 with Euler angles [L]) and on exact instances; the round neither proves nor assumes it true.
- The countercontrol is HO-24 item 4's cone, recomputed by `experiments/e15_k2s6_probe.py` (decision rule in its
  header): the finite clause leaves a cone `K*` with the products, invariant under `G₃₈₄`, `K* ≠ Q3`, not preserved by
  the flow at `cos t = 3/5`; its self-duality rests on Theorem S′ [W] and is not checked by the round.

**Predictions for the probe (sign, strength, reason).**
- D1 PASS, very high: E10's L2 checked the same four maps (the flow at `cos t = 3/5` through the half-angle unitary,
  the same conjugation as `diag(1, (3 + 4i)/5)`); `(I − i(X + Y + Z))/2` equals E10's `U_J` up to the phase `e^{iπ/4}`
  (scratch check at 03:04Z, recorded in LOG).
- D2 PASS with order 384: certain (E10 F1's construction, unchanged).
- P1, P2 PASS: very high (elementary instances).
- X1 192 rays, closed; X2 overlaps in `[25/2048, 13/16]`; X3 minimum `85/2048` and H1 at `401/400`: high (HO-24 item 4;
  the coordinator's X3).
- X4 PASS: high (the threshold `1600/160801 ≈ 0.00995` lies below `25/2048 ≈ 0.0122`).
- X5 PASS: certain for `d* ∉ Q3`; high for `dict z* = d*/8` (it holds if HO-24's `T_h` is the table `coordOf P_h`,
  by `dict_coordOf` [D]; the risk is my reading of the source's normalization).
- X6 PASS: high. By hand, the squared overlaps of `R h*` with `h*` and with `(1 ⊗ diag(1, i)) h*` are
  `14800/16384 ≈ 0.903` and `15592/16384 ≈ 0.952`; I expect the maximum over the orbit near 0.95, far below
  `400/401 ≈ 0.9975`.
- X7 384 rays, no product, minimum `5/256`: high (HO-24 item 5).
- R1 PASS: certain (E10's code and instances, copied unchanged).
- XC1, XC2, XC3 fail as stated: high.
- Overall `VERDICT E15-S6-EXACT-LAYER-CONSISTENT`, strength high; the main risk is a coding error in the new
  Gaussian-rational layer, which D1 would expose first.

**Prediction for the node.** S6 drafted with every predicted output generated from a measurement; classification
POSITIVE; no label changes (K2 OPEN; the schema CONDITIONAL on H2, H3, A_miss and `ReachPure`).

## 1. The measurement (probe run 1)

`experiments/e15_k2s6_probe.py` run 1 (started 03:11:06Z, after commit `f7c3668c`; decision rule unchanged): 12/12,
`COUNTER XC1 fails as stated` (at `301/300` the minimal overlap `25/2048` is below the threshold `1200/90601`),
`COUNTER XC2 fails as stated`, `COUNTER XC3 fails as stated`, `VERDICT E15-S6-EXACT-LAYER-CONSISTENT`; replay
byte-identical (py `78cd7c59…`, out `3ee625fe…`). Every S0 prediction held. Measured values: the parsed `cycEquiv` is
`v ↦ (v₂, v₀, v₁)` and the two `rotFun_apply` lines were found; the table group has order 384; the orbit of `h*` has 192
rays, closed under the three lifts; the 18336 squared overlaps lie in `[25/2048, 13/16]`; the minimum normalized
`|det Ψ|²` is `85/2048`; (CC) holds at `401/400` on every pair (threshold `1600/160801`); `⟨h*|d*|h*⟩ = −1/400`;
`dict z* = d*/8` with `T_h` read as `coordOf P_h`; the maximum squared overlap of `R h*` with the 192 rays is
`1949/2048` — exactly the hand value `15592/16384` for the ray of `(1 ⊗ diag(1, i)) h*`, the nearest group rotation —
so `P_{R h*}` lies in `PSD ∩ Z*` and pairs `−1/400` with `R d* R*`; the orbit of `φ₀` has 384 rays, none a product,
minimum normalized `|det Ψ|²` `5/256`.

## 2. The draft

`preregistration-drafts/S6-k2-schema-pair-cone.md` (round id `K2-SCHEMA-1`): the `v3-round` and `v3-governed-paths`
blocks (a draft; nothing activated); the three questions Q-CONE, Q-SCHEMA, Q-EXACT; the frozen surface (the 52
declarations of `EqvK2Schema` in order, renamed `K2Schema`, 22 prints, the census family, the import line); a section
stating `hA` exactly in the full-flow form, HO-13 item 2's two-rotation clause as the stronger theorem not formalized
(with HO-20 item 4's H-level premise and HO-17 item 4's token model at their labels), and `ReachPure` as a named
hypothesis with no OI content; the exact layer (this probe, frozen with two path lines changed); decision rules; the
earned reading and the non-inference rule; the premises not sourced; the ROADMAP wording it would license (row K2, not
applied); controls (S1 with six mutations; S2; S3 with a positive control and a load-bearing control for each of H1,
H2, H3, A_miss and, on the finite side, `ReachPure`; S4; P, W, V, I, C, R, G); the invariant→checkpoint table with `C0`
met by run 38101580750; the design evidence and the predicted outputs generated from the measurements.

## 3. Outcome (§A.31)

- Productivity test met (a)–(d). **POSITIVE** (drafting): every predicted output of the three cells is generated from a
  measurement; the countercontrol is the thread's own recomputation, and every exact value HO-24 items 4–5 state was
  reproduced (no discrepancy, so nothing NEW about HO-24). **ELABORATING**: the non-invariance of HO-24's cone under the
  flow at `cos t = 3/5` is now an exact statement with an explicit witness that needs neither Theorem S′ nor `ReachPure`
  (X6); with S′ it shows the module's theorem false when `hA` is weakened to the finite clause, so the full-flow form is
  load-bearing in the module's own terms.
- Pressure test of the favourable reading ("S6 settles K2's cone"): the theorem is conditional on H2, H3 and A_miss,
  none sourced, and on `ReachPure`, proved only in writing; the countercontrol's self-duality is [W] from another
  thread; nothing here concerns more than two tokens. K2 stays OPEN; no label changes.

## 4. Addendum 3 (04:31Z): the meaning of the necessity direction

A_miss in S6 is cone-preserving admissibility: the invariance of `K` under `actT (rotLin t)` and `actT cycEquiv`.
`Q3_aMiss` gives `Q3 ⇒ A_miss` in that reading only; it says nothing about the operational availability of those
operations through the kernel's protocols, which is the H-level premise (A)/H-OI_g and is not in S6 (a quantum cone with
a restricted set of available transformations has the invariance without the availability). The draft now states
"given H1–H3 and `ReachPure`, `K = Q3` iff A_miss, where A_miss is the invariance of `K` under the flow and `cycEquiv`",
sufficiency witnessed by the schema and necessity by the invariance lemma; its scope section says the equivalence is
between cone-level statements, availability is a separate H-level question S6 does not decide, and A_miss remains an
introduced hypothesis, not a premise at L; its hypothesis table names "A_miss (invariance form, introduced)" and
"(A)/H-OI_g (availability, H-level, not in S6)" as separate rows. The scope paragraph also states the stage-6 record's
reach: (b) is independent of the transferred pair-level premises at L, not shown independent of OI.

## 5. §G built in a design module (reading rule and prediction, written 2026-10-11T04:33Z, before dispatch 1)

`lean/EqvK2Converse.lean` (blob `4add9b8d`, sha256 `240abaf6…`, 234 lines, 9 prints) imports the built `EqvK2Schema`
(blob `659ae36c`, unchanged) and states §G: the split `dict_eq_sum_tensorOf`, `dict_actT`, `tensorOf_conj`, the one-token
lemmas `tokMat_eq`, `phaseMat_conjTranspose`, `homMap_rotLin`, `tokMat_rot`, `cycMat_conjTranspose`, `homMap_cyc`,
`tokMat_cyc`, the two intertwining lemmas `dict_actT_rotLin`, `dict_actT_cyc`, then `Q3_aMiss` and
`pairCone_eq_Q3_iff_drive` with exactly the statements of S6 §G. The forms of the identities were checked exactly
beforehand in a scratch script (design aid in the session scratchpad, not evidence; the evidence for the identities is
`e15_k2s6_probe` D1 and `e10_k2_schema` L2).

**Reading rule (fixed now).** In the dispatch's Mathlib bridge job: **BUILT** iff the Build step succeeds and every
`#print axioms` line of `EqvK2Converse` prints exactly `[propext, Classical.choice, Quot.sound]`; **PARTIAL** iff the
build fails and some of its prints are standard; **NOT BUILT** otherwise. `lean-axioms` must report no `sorry`; the
release gate is expected red at `lean-manuscript` only (no census family); any other red step is recorded and examined.
Only BUILT meets `C0′` and moves R-E15.4 from [W] + [X] to [D].

**Prediction.** Sign: BUILT is more likely than not, strength moderate (about 0.55). The statements are low risk; the
risk is in four proofs written without a local Lean: `tokMat_eq` (full `simp` on Pauli entries, then `ring`), the two
conjugate-transpose lemmas (complex `star` through `simp`), and `tokMat_rot`/`tokMat_cyc` (`Matrix.mul_fin_two`, then
real and imaginary parts and `linarith`). A failure there would leave the three dependent theorems with `sorryAx`
(PARTIAL), with the repair proof-only.
