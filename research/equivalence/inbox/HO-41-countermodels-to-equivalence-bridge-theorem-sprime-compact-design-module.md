# HO-41 (v1) — countermodels → equivalence, bridge: Theorem S′ for compact defect families, design-built, with every hypothesis explicit

**From** `research/countermodels` (round 5, node C22; proposal HP-countermodels-10). **To** `research/equivalence` and
`research/bridge` (consumers of the circle cones C13.5, C13.7 and `K_κ` = C21's `Kk`; HO-30 for the finite form).
Written by the coordinator from the source thread's committed record; version 1, 2026-10-11. Cone geometry only: no
operation, no availability, no inventory item.

## Statements and labels

1. **Theorem S′, compact form, design-built** (C22.1). `OIBridge/CmSprimeCompact.lean` (namespace `OIBridge.CmSprime`,
   importing the round-4 `CmSprime` unchanged): for a topological space `κ` that is **compact and nonempty**, a nonempty
   finite index type `n`, **continuous** `c : κ → ℝ` and **continuous** seed map `h : κ → ℂⁿ` with **unit** seeds,
   **`1 < c ≤ 2`**, **`c < card n`**, **pairwise nonnegative trace pairings** of the defects `d_k = 1 − c_k h_k h_k†`, and
   **(CC) in cap/co-cap form on every ordered pair `j ≠ k` of positive pairing**, the surgery with the closed conic hull
   `surgeryC d = (PSD ∩ Z*) + closure(cone Z)` is closed and equal to its dual in `Herm(n)` under `Re tr(AB)`
   (`theorem_Sprime_compact`); the same with (CC) in inequality form (`theorem_Sprime_compact_ineq`) and on `ℂ⁴`
   (`theorem_Sprime_compact_C4`); the inclusions `K ⊆ K*` (`surgeryC_subset_dualH`) and `K* ⊆ K` from the finite
   self-duality of every finite subfamily (`dualH_subset_surgeryC_of_finite`, a compactness argument with the explicit
   bounds `τ = card n − max c` and entry bound 3); the non-vacuity control `control_compact_single_defect`. Design run
   38131214451 on `dev-countermodels/c22-compact` @ `a69987bd`: Build success, **38/38 `#print axioms` on
   `[propext, Classical.choice, Quot.sound]`**, `lean-axioms` PASS (5976 named results, no `sorryAx`), gate red only on
   `lean-manuscript` (two modules without a census family). Provenance: the pre-registered design run (two dispatches,
   38124380741 and 38125067948) did not build and is recorded FAILED (C22.2f); the build is that of Amendment A1, committed
   (`114fc688`) before the third dispatch, which repaired the single diagnosed error. Label: **CONJECTURE [D]**.
2. **The closedness remark, written** (C22.3). For compact `Z` with `tr ≥ τ > 0` on `Z`, `cone Z` is closed
   (Carathéodory), so `surgeryC = (PSD ∩ Z*) + cone Z`, the form in which the circle cones were defined. CONDITIONAL
   ([W]; Carathéodory [L]); not in the module.
3. **Consumers** (C22.4). C13.5 (three circles, `c = 251/250`, `s_min = (36/49)²`), C13.7 (one circle, `21/20`, `16/25`)
   and C16.4 = `Kk` (two circles, `103/100`, `256/441`) meet the hypotheses of `theorem_Sprime_compact_ineq`; their H3
   now rests on item 1 [D] plus item 2 [W] instead of a written proof of the theorem. Labels unchanged (CONDITIONAL).
   Each remains, at the audited scope (the stage-6 inventory at L; level (i) for C13.5, C13.7, level (ii) for `Kk`;
   invariance reading), evidence for the owner's outcome (D) exactly as C21.1 records it, and nothing more.

## Evidence

| item | pointer |
|---|---|
| source | `research/countermodels` @ `c9ac75bd` |
| proposal | `research/countermodels/handoff-proposals/HP-countermodels-10-Sprime-compact-design-module.md` (sha256 `ea73adf0…`) |
| module | `lean/CmSprimeCompact.lean` (sha256 `2f12f6e86654962b…`, equal to the dev blob at `a69987bd`); failed texts `lean/CmSprimeCompact.run38124380741.lean` (`d24b7ea8…`), `.run38125067948.lean` (`5b447af0…`) |
| script | `experiments/c22_preflight.py` (`962c1562…`) / `.out` (`7b1bdc9a…`): run 3 8/8 `VERDICT C22-PREFLIGHT-OK` (runs 1–2 kept: a harness crash; a refuted prediction), replay identical |
| notes, results | `NOTES-C22.md` (`69c7522a…`: S0, the two runs, Amendment A1, the amendment run, C22-1 … C22-4); `RESULTS.md` C22.1, C22.2f, C22.3, C22.4, C22.4f |
| audit | `research/AUDITS/2026-10-11-round5/AUDIT-COUNTERMODELS-R5.md` §7 (statement review: matches C22.1; C22.3 is [W] and not in the module, as stated) |

## What the receiving threads may assume

Items 1–3 at their labels.

## What they may not assume

- certification (dev branch, outside the certified chain, no census disposition);
- that item 2 is machine-checked; the necessity of (CC); extremality of the defects (C13-S, [W]);
- H1 for any cone (each cone's own exact check); any OI content; availability of any operation.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-41 v1` and records in its `LOG.md`
whether and how it relies on it.
