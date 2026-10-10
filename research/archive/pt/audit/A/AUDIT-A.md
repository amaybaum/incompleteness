# Coordinator's audit of thread A — PAIR-COMP

Audited: `pt/A/RESULT.md` sha256 `b39eedca031871ef3077ebb4969f1b93d0dea8c2eba5706a02d4566a736727e1` (39 files in `pt/A/`).

## Integrity
- `inputs.manifest.sha256`: OK. `pt/base` HEAD `9f9f8257…`, status clean. Protocol and both amendments unchanged.
- The thread wrote only in `pt/A/` (its own record agrees). No foreign file is present.

## Replays (coordinator, `pt/auditA-replay/`, `python3 -I -B`)
All four certified scripts reproduce their recorded stdout byte for byte, with empty stderr:
- `a1_stage_product`: 25 PASS, `fb03dd86…`;
- `a2_native_closures`: 22 PASS, `ada90286…`;
- `a3_shadow_countermodel`: 14 PASS, `6d2de61e…`;
- `a4_identification`: 12 PASS, `611dc429…`.

A first attempt from a deeper directory failed because the scripts read the base by relative path. That is a harness
location issue, not a script failure; the copy was rerun next to `base/`.

## Independent checks (`indep_checkA.py`, written from the landed definitions; no thread code used)
All CONFIRMED, with countercontrols green:
- `phiW = cnot(prodState xplus z3)`;
- `T_ψ` is a normalized rank-one PSD state;
- `ipW(F, T_ψ) = −1/2`;
- `F ≥ 0` on every product and every `cnot` image of a product over the closed ball. This is an exact reduction:
  pairing `= 1/2 − (1/4)(1 + xᵀMy)` with `M` orthogonal, which is ≥ 0 by Cauchy–Schwarz. Hence `F ∈ dualW(K_gen)`
  and `T_ψ ∉ K_gen`;
- `famI(phiW, phiW, T_ψ/4, F) = −1/8`, so FCC fails for uniform `K_gen` (countercontrol `0 ≥ 0`);
- `N = actT reflY ∘ cnot` sends `prodState xplus z3` to `idW` and then to `chainW`, whose value at the sharp effects is
  `−1/2`;
- for `K_E`: the IE1 witness gives `−2/5` and the FCC witness `−1/2`.

## Written steps reviewed
- **`D_cl` is a valid `DirectedStages` under the landed definitions.** `FiniteStage` (KInfFoundations.lean:63) needs
  only finite sets, a table in `[0, 1]` and a unit equal to 1. `D_cl` has finite stages, inclusion maps and one
  global table, so SC∞ holds.
- **W-A3** (the read-out of `body D_cl` is the `K_cl` slice) is sound. The norming inequality
  `‖Φλ‖∞ ≥ ½‖λ‖₁` gives ℓ¹ limits. The PD-ness of nonzero `λ` parts gives `⊆`. Finite convex combinations of the
  dense `ρ_J` give `⊇`.
- **W-A3.1** (finite rank ⇒ compact read-out ⇒ closed cone) and **W-A4.2** (`D_K` for any closed admissible `K`)
  are sound. So ID and P-STAGE2, as conditions on the theorem's `K_p`, are `hcl` restated relative to `hadm`.
- **Spot check of references:** 11 [K] references, all accurate. The two that first looked like misses are the
  `Composite` structure, whose `lt` field is at :245, and `W`'s docstring at :95–96: "Local tomography is the premise
  this carrier encodes".

## Verdict for integration
- **(A-i):** DERIVED for the constructed systems. Local tomography holds by construction (product labels only) and is
  named.
- **(A-ii), `hcl` for the theorem's `K_p`:** INDEPENDENT of the premises certified at L as stated. Witness: `M_cl`,
  realized as the read-out of a valid infinite-rank `D_cl`. Scope as the thread states it.
- **Exposed hidden assumption:** the closedness content of a completion route is finite rank (compactness) of the pair
  completion, not completion as such and not local tomography.
- **Restatements:** ID, P-STAGE2, twisted self-duality and no-restriction are `hcl` restated relative to the other
  hypotheses.
- **Native closures at the instance:** `SEP`, `K_gen` and `K_E` are closed, but they fail `hgate` or H.
- **Not kernel-checked:** W-A0 (the closure form), which rests on [D] lemmas, and N4.3 (the instance
  characterization), which rests on the written classification and [L]. The Lean in `lean/` is UNBUILT.
