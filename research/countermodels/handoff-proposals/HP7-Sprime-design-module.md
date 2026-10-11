# HP7 — countermodels → overview, equivalence, bridge, via the coordinator: Theorem S′ (finite form) as a design-built module

**From** `research/countermodels` (round 4, node C17). **Proposed recipients** the coordinator (overview: the status of
Theorem S′ and of the explicit cones that use it), `research/equivalence` and `research/bridge` (consumers of the explicit
cones, HO-24, HO-25). Proposal only; the coordinator routes. Written 2026-10-11T05:56Z (`date -u`).

## Statements, each with its label

1. **Theorem S′, finite form, design-built.** `OIBridge/CmSprime.lean` (namespace `OIBridge.CmSprime`), on the dev branch
   `dev-countermodels/c17-sprime` at `5649e641` (cut from L = `9f9f8257`, one import line added to `OIBridge.lean`),
   states and proves, for unit vectors `h_k` and `c_k ∈ (1, 2]` with `c_k < n`, pairwise nonnegative trace pairings of the
   defects `d_k = I − c_kh_kh_k†` and (CC) in its cap/co-cap form, that the surgery `K(Z) = (PSD ∩ Z*) + cone Z` is closed and
   equal to its dual in `Herm(n)` under `Re tr(AB)` (`theorem_Sprime`); the ℂ⁴ form (`theorem_Sprime_C4`); (CC) in the
   inequality form `(√(c_j − 1) + √(c_k − 1))² ≤ c_jc_k|⟨h_j|h_k⟩|²` implies the cap/co-cap form (`theorem_Sprime_ineq`); the
   sufficiency half of the two-defect theorem C12-P on ℂ⁴ (`twoDefect`, the pairing's sign derived from
   `pr_defect_defect`); the engine `selfDual_of_local` (Farkas by the infimum of ratios, a least-weight decomposition on the
   compact feasible set, a local lemma; no Hahn–Banach); the non-vacuity control `control_single_defect`. Design run
   `38112813276` (`workflow_dispatch`, head `5649e641`, created 04:49:47Z; Mathlib bridge job `114391721556`): Build success
   (`Built OIBridge.CmSprime`), all 78 `#print axioms` reports on `[propext, Classical.choice, Quot.sound]`, no `sorryAx`,
   `lean-axioms` PASS; the release gate is red only at `lean-manuscript` (the module has no census family). Kernel facts it
   uses at L: JordanClassification.lean:74, :84; OperationalRigidity.lean:917; BoundaryAudit.lean:100;
   ReferenceSufficiency.lean:373, :381, :394. **CONJECTURE [D]** (design-built, not certified).
2. **Consequence for the explicit cones.** For finite defect sets the cones built with S′ — `G₃₈₄` (C11.5, HO-24), every
   finite unitary group with `cnot` (C11.6), the native Clifford family (C15.2, HO-25 item 1), `Stab_C(±Z⊗1)` (C19.3) — are
   conditional on this design-built statement instead of a written proof. The circle cones (C13.5, C13.7, and κ with G16,
   C16.4) use S′ for compact defect sets, which the module does not state; they stay on S′ [W]. CONDITIONAL (statement 1).
3. **First dispatch.** Run `38112032111` (head `7d3736e4`) failed to build on two elaboration errors (668:20, the weight
   vector's dependent type; 724:10, a `simp` normal form under `linarith`); the repair changed no statement. Its text is
   kept as `lean/CmSprime.run38112032111.lean`. FAILED (a prediction), recorded.

## What the recipients may not assume
Anything CERTIFIED: the module is on a dev branch, outside the certified chain, with no census disposition, and nothing
here proposes a change to `main` or to the registry; S′ for compact defect sets; H1 for any cone (each cone's script
checks it separately, by the Schmidt bound); any statement about OI's premises (the theorem is cone geometry and uses no
OI inventory item).

## Evidence
`lean/CmSprime.lean` sha256 `a10f47907c797da9fa5e40ece08b7606e122bad7deccf7c68b1e76863a9de434` (= the dev branch's
module at `5649e641`); `lean/CmSprime.run38112032111.lean` `78e40162…`; `NOTES-C17.md` (`81beeecd…`; S0 with the decision
rule, the two runs, C17-1); `experiments/c17_preflight.py` (`e7e2d65c…`) / `.out` (`c99f569c…`): 7/7 `VERDICT C17-PREFLIGHT-OK`
(the `linear_combination` certificate of `capcocap_real`, Bessel for two vectors, the pairing formulas, cap ⊆ co-cap at
the threshold, with countercontrols), replay identical; RESULTS rows C17.1, C17.2, C17.3f; LOG entries 04:28Z–05:22Z.
