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
