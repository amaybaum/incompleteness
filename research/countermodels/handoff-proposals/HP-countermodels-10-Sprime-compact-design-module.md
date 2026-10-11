# HP-countermodels-10 — countermodels → overview, equivalence, bridge, via the coordinator: Theorem S′ for compact defect families, design-built, with every hypothesis explicit

**From** `research/countermodels` (round 5, node C22). **Proposed recipients** the coordinator (overview: the status of
Theorem S′ and of the circle cones that rest on it), `research/equivalence` and `research/bridge` (consumers of the circle
cones C13.5, C13.7 and `K_κ` = C21's `Kk`; HO-30 for the finite form). Proposal only; the coordinator routes. Written
2026-10-11T10:45Z (`date -u`).

## Statements, each with its label

1. **Theorem S′, compact form, design-built** (C22.1). `OIBridge/CmSprimeCompact.lean` (namespace `OIBridge.CmSprime`,
   importing the round-4 `CmSprime` unchanged) states and proves: for a topological space `κ` that is **compact** and
   **nonempty**, a nonempty finite index type `n`, **continuous** `c : κ → ℝ` and **continuous** seed map `h : κ → ℂⁿ` with
   **unit** seeds, **`1 < c ≤ 2`**, **`c < card n`**, **pairwise nonnegative trace pairings** of the defects
   `d_k = 1 − c_k h_kh_k†`, and **(CC) in cap/co-cap form on every ordered pair `j ≠ k` of positive pairing**, the surgery with
   the **closed** conic hull `surgeryC d = (PSD ∩ Z*) + closure(cone Z)` is closed and equal to its dual in `Herm(n)` under
   `Re tr(AB)` (`theorem_Sprime_compact`); the same with (CC) in inequality form (`theorem_Sprime_compact_ineq`) and on
   `ℂ⁴` (`theorem_Sprime_compact_C4`); the inclusions `K ⊆ K*` (`surgeryC_subset_dualH`) and `K* ⊆ K` from the finite
   self-duality of every finite subfamily (`dualH_subset_surgeryC_of_finite`); the estimate
   `|Re tr(qM)| ≤ ε · card n · tr q` for `q ⪰ 0`, `max |M_ij| ≤ ε` (`abs_pr_le`); the non-vacuity control
   `control_compact_single_defect`. Design run `38131214451` on `dev-countermodels/c22-compact` @ `a69987bd` (cut from L =
   `9f9f8257`; the two modules and two import lines): Build success (`Built OIBridge.CmSprimeCompact`), **38/38 `#print
   axioms` on `[propext, Classical.choice, Quot.sound]`**, `lean-axioms` PASS (5976 named results, no `sorryAx`), gate red
   only at `lean-manuscript` (the two modules have no census family). **Provenance:** C22's pre-registered design run (two
   dispatches, runs `38124380741`, `38125067948`) did not build (elaboration details; texts kept) and is recorded FAILED
   (C22.2f); the build is that of Amendment A1, written and committed (`114fc688`) before the third dispatch, which repaired
   the single diagnosed error. Label: **CONJECTURE [D]** (design-built, not certified).
2. **What needed a new argument** (C22-2). The finite engine of `CmSprime` is reused as a black box on finite ε-nets of the
   compact family; the new steps are the pairing estimate, the shift `y + ηI ∈ (K_F)*` for `η ≥ ε · card n · tr(y)/τ`
   (`τ = n − max c`), and the limit in compact entry boxes. Farkas over a compact family, a separation theorem and
   Carathéodory are not used. [D] as parts of the built module.
3. **The closedness remark, written** (C22.3). For compact `Z` with `tr ≥ τ > 0` on `Z`, `cone Z` is closed (Carathéodory),
   so `surgeryC = (PSD ∩ Z*) + cone Z` — the form in which the circle cones were defined. CONDITIONAL ([W]; Carathéodory [L]).
   Not machine-checked.
4. **Consumers** (C22.4). C13.5 (three circles, `c = 251/250`, `s_min = (36/49)²`), C13.7 (one circle, `21/20`, `16/25`) and
   C16.4 = `Kk` (two circles, `103/100`, `256/441`) meet the hypotheses of `theorem_Sprime_compact_ineq` (compact injectively
   parametrized circles, continuous unit seeds, positive pairings, `c²s_min ≥ 4(c − 1)`); their H3 now rests on statement 1
   [D] plus statement 3 [W] instead of a written proof of the theorem; labels unchanged (CONDITIONAL). Each remains, at the
   audited scope (the stage-6 inventory at L; level (i) for C13.5, C13.7; level (ii) for `Kk`; reading invariance), evidence
   for the owner's outcome (D) exactly as C21.1 records it, and nothing more.

## What the recipients may not assume
Anything CERTIFIED (dev branch, outside the certified chain, no census disposition; no change to `main` or the registry is
proposed); that statement 3 is machine-checked; the necessity of (CC); extremality of the defects (C13-S, [W]); H1 for any
cone (each cone's own exact check); any OI content (cone geometry; no inventory item used); availability of any operation.

## Evidence
`lean/CmSprimeCompact.lean` sha256 `2f12f6e86654962bc8845f6f0311b80c616cc2104d5ace6179f21212eccffc65` (= the dev blob at
`a69987bd`); failed texts `lean/CmSprimeCompact.run38124380741.lean` (`d24b7ea8…`), `.run38125067948.lean` (`5b447af0…`);
`NOTES-C22.md` (`69c7522a…`: S0, the two runs, Amendment A1, the amendment run, C22-1 … C22-4); `experiments/c22_preflight.py`
(`962c1562…`) / `.out` (`7b1bdc9a…`): run 3 8/8 `VERDICT C22-PREFLIGHT-OK` (runs 1–2 kept: a harness crash; a refuted
prediction), replay identical; RESULTS C22.1, C22.2f, C22.3, C22.4, C22.4f; LOG 07:50Z–10:22Z.
