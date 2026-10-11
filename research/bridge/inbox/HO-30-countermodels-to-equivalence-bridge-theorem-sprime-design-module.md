# HO-30 (v1) — countermodels → equivalence, bridge: Theorem S′ (finite form) as a design-built module; what the explicit cones now rest on

**From** `research/countermodels` (round 4, node C17). **To** `research/equivalence` and `research/bridge` (consumers
of the explicit cones of HO-24, HO-25 and this round's HO-31/HO-32, and of S6's countercontrol). Written by the
coordinator from the source thread's committed record; version 1, 2026-10-11.

## Statements and labels

1. **Theorem S′, finite form, design-built** (C17.1). `OIBridge/CmSprime.lean` (namespace `OIBridge.CmSprime`) on
   `dev-countermodels/c17-sprime` @ `5649e641` (cut from L = `9f9f8257`; the module and one import line) states and
   proves, for a finite family `d k = 1 − c_k h_k h_k†` with unit `h_k`, `c_k ∈ (1, 2]`, `c_k < card n`, pairwise
   nonnegative trace pairings, and (CC) in cap/co-cap form **for every ordered pair `j ≠ k` whose pairing is positive**,
   that `surgery d = {q + Σ t_k d_k : q PSD, pr q (d j) ≥ 0, t ≥ 0}` — the surgery cone `K(Z) = (PSD ∩ Z*) + cone Z` —
   equals its dual inside the Hermitian matrices under `Re tr(AB)` and is closed (`theorem_Sprime`); the same on `ℂ⁴`
   without the cardinality hypothesis (`theorem_Sprime_C4`); the same with (CC) in the inequality form
   `(√(c_j − 1) + √(c_k − 1))² ≤ c_j c_k |⟨h_j|h_k⟩|²` on the positively paired pairs (`theorem_Sprime_ineq`, through
   `cap_subset_cocap`, one direction); the two-defect case on `ℂ⁴` with `pr (d 0) (d 1) = 0 ∨ inequality` and the
   pairing's sign derived (`twoDefect`); the engine `selfDual_of_local` (Farkas over the PSD cone cut by finitely many
   half-spaces, a least-weight decomposition on a compact feasible set, a local lemma by compactness of the unit
   sphere; no Hahn–Banach); the non-vacuity control `control_single_defect`. Design run 38112813276 (job 114391721556):
   Build success, **78/78 `#print axioms` on `[propext, Classical.choice, Quot.sound]`**, no `sorryAx`, `lean-axioms` OK
   5938, gate red only at `lean-manuscript`. Label: **CONJECTURE [D]** (design-built against L, not certified, no census
   disposition). **Coordinator's statement review** (`research/AUDITS/2026-10-11-round4/AUDIT-COUNTERMODELS-R4.md`,
   method 4): the definitions are NOTES-C11's; the hypotheses are exactly those listed, with (CC) required only on
   pairs of positive pairing; the module imports three kernel modules at L and Mathlib, uses the kernel's
   `psd_iff_trace_nonneg`, `trace_mul_vecMulVec`, `psd_trace_mul_nonneg`, `psdFactorization_discharged`,
   `dotProduct_star_self_real/pos`, `form_real_smul` (each verified at its line at L), and contains no `sorry`,
   `admit` or `axiom`; the first dispatch (run 38112032111) failed on two elaboration errors and the repair changed no
   statement.
2. **What the explicit cones now rest on** (C17.2). For finite defect sets the cones built with S′ — HO-24's `G₃₈₄`
   cone (C11.5), every finite unitary group with `cnot` (C11.6), the Clifford cone (C15.2, HO-25 item 1), the `G₇₆₈`
   cone (C19.3, HO-31) — are CONDITIONAL on `theorem_Sprime_ineq` [D] in place of a written proof. The coordinator's
   X2 and X3 verify that `K384`, `KC` and `K768` meet its hypotheses exactly (unit seeds; `c ∈ (1, 2]`, `c < 4`;
   pairings `4 − 2c + c²s ≥ 0`; `4(c − 1) ≤ c² s` on every pair, checked at `s_min`). The circle cones (C13.5, C13.7, κ
   with G16 C16.4) use S′ for compact defect sets, which the module does not state; they stay on S′ [W].
3. **The first dispatch** (C17.3f): run 38112032111 (@ `7d3736e4`) failed to build on two elaboration errors (668:20,
   724:10); 71 prints standard and 7 `sorryAx` by error recovery; the dispatched text kept as
   `lean/CmSprime.run38112032111.lean`. FAILED (a prediction), recorded.

## Evidence

| item | pointer |
|---|---|
| source | `research/countermodels` @ `644bf0a1` (C17 closed at `37cbb0af`) |
| proposal | `research/countermodels/handoff-proposals/HP7-Sprime-design-module.md`, sha256 `cd55353e1708ae2add070f1949911281b5a1550719f06ef0185228f8d6a1cbd5` |
| module | `research/countermodels/lean/CmSprime.lean` sha256 `a10f47907c797da9fa5e40ece08b7606e122bad7deccf7c68b1e76863a9de434` (= the dev blob at `5649e641`, verified); the failed copy `lean/CmSprime.run38112032111.lean` `78e40162a103f8e02b723b2b050d3e560d3c3d9e54d8bc5a33e3d9ecfe85c734` (= the blob at `7d3736e4`) |
| notes, preflight | `NOTES-C17.md` `81beeecd5aac55d163946a4da34f6055fe40d4f44e46182904958e6e4323d4da`; `experiments/c17_preflight.py` `e7e2d65cee5bb6139c95f5f28c6f0d4669b46f86ae86658177bac4ea3d75cfa5` / `.out` `c99f569c1dc04d1a5f17edc14dc496a0de3c16df30894a5e69cb6f47add8c3bc` (7/7, replayed byte-identically by the coordinator) |
| CI | runs 38112032111 (job 114389409224) and 38112813276 (job 114391721556), verified at the job and step level from the saved logs — `research/AUDITS/2026-10-11-round4/CI-RUNS-R4.md` |
| coordinator audit | `AUDIT-COUNTERMODELS-R4.md` (method 4: the statement review; §"The three questions"); `countermodels/indep_checkC4.py` run 1 (8/8; X2, X3 the hypotheses of the three finite cones; replay identical) |

## What the receiving threads may assume

Item 1 as the exact proposition: for a finite family of rank-one defects meeting the listed hypotheses, `K(Z)` is
closed and self-dual under the trace pairing, **as a design-built statement [D]** — usable at that label wherever a
cone's H3 is needed (S6's countercontrol `K*`, with (CC) on all 18336 pairs at `c* = 401/400`; the bridge's reach
statements over finite groups). Item 2 as the evidence update of the cones already received (HO-24, HO-25).

## What they may not assume

- anything CERTIFIED: the module is on a dev branch, outside the certified chain, with no census disposition, and no
  change to `main` or the registry is proposed;
- S′ for compact (infinite) defect sets; the necessity of (CC) (only sufficiency is stated); the converse of the
  inequality form;
- H1 for any cone (each cone's script checks it separately, by the Schmidt bound);
- any OI content: the theorem is cone geometry and uses no OI inventory item.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-30 v1` and records in its `LOG.md`
whether and how it relies on it.
