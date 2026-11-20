# MEAS-Q amendment A02 (before run S-B-long)

Committed after the preregistered runs (`--search`, results in `results.json`) and after post hoc
diagnostic X1 (`checks/posthoc_sb.py`), and before the run S-B-long defined here. It changes no
requirement, bound or decision rule of `PREREG.md` §§2–6, and it does not change the preregistered
verdict, which is computed from `results.json` alone.

**Why.** X1 (not preregistered) re-ran the ten S-B examples stored in `results.json` in Q on
`(ℤ/100)³`, where sites within distance 8 of the box are exact up to `t = 87`. In 7 of 10, DT_A as
defined in §2 holds with `A` = the sites at distance 1–8 from the box (about 1 000 sites). In every
example `H` is at `(c, c)` at `τ₂` but not at every later tick. In the examples where one branch
stays confined (support 2–3 sites) the other grows to about 20 000 sites by `t = 87`. DT_A's
readiness clause is evaluated at the single instant `τ₂`. S-B-long measures how much of S-B's
cross-class DT_s and DT_A rests on that clause.

**Run S-B-long (preregistered here).**
- Sample: every 10th configuration of S-B's selected list, in S-B's order (398 configurations).
- Q itself on `(ℤ/100)³`, background `2^15`, box at offset 40, both carrier branches, horizon 87;
  tracked region `E` = sites at ℓ1-distance 1–8 from the box (exact to `t = 87`).
- For every site `H ∈ E` and every configuration:
  - DT_s (§2), `τ₂ ≤ 27`;
  - DT_A (§2), with `A = E`, persistence 60, `τ₂ ≤ 27`;
  - DT_A^h (held readiness): DT_A, and in addition `W_t(H) = w*` in both branches at every
    `t ∈ [τ₂, τ₂ + 8]`. The 8 ticks are the light-cone time across `A`'s radius.
- Recorded per configuration: whether some `H` meets each task; the two-slice support size of each
  branch at `t = 87`; whether exactly one branch stays within the box (confined) to `t = 87`.

**How it is reported.** The counts are reported beside the preregistered verdict. A DT_A^h
delivery, if any, is re-run with a ledger audit and reported as a candidate for review. It is not
counted by the author as gem (i): S-B-long is a follow-up defined after the preregistered runs.
Compute bound: under 30 minutes (§A.40).
