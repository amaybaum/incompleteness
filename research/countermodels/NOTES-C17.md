# NOTES-C17 — Theorem S′ as a design module

Round-4 node C17, opened 2026-10-11T02:46Z (session start), S0 written 2026-10-11T04:28Z (`date -u`). Target, in the
coordinator's words: first the two-defect case (the sufficiency half of C12-P): rank-one defects `d_i = I − c_iP_{h_i}` on
`ℂ⁴`, `c_i ∈ (1, 2]`, nonnegative pairing, (CC) `c₁c₂|⟨h₁|h₂⟩|² ≥ (√(c₁ − 1) + √(c₂ − 1))²` ⇒
`K = (PSD ∩ Z*) + cone Z` closed and self-dual under the trace pairing; then the finite case in general. Compact `Z` is not
asked. One or two dispatches.

Conventions as in NOTES-C11 (Theorem S′) and NOTES-C12 (C12-P). The module is `OIBridge/CmSprime.lean` (namespace
`OIBridge.CmSprime`), written against the kernel at L = `9f9f8257` and Mathlib `v4.33.0`; the working copy is kept under
`lean/` once a run has been made.

## Hypothesis classification (standing rule 1)

Theorem S′, its inequality form and the two-defect case are statements of cone geometry in `Herm(n)`: their hypotheses
(unit vectors, `c ∈ (1, 2]`, pairings, (CC)) are conditions on a finite set of matrices, not premises about OI. No OI
inventory item is used and no introduced hypothesis (H1–H3, A_miss, a finite clause, claim (D), EBF, T) appears. The rows
carry no "introduced" flag. What the theorem changes downstream is the status of the cones built with it (C11.x, C13.5,
C13.7, C15.2, C16.4): their CONDITIONAL on "Theorem S′ [W]" becomes a condition on a design-built statement, and only for
finite `Z` (the circle cones of C13.5, C13.7, C16.4 use S′ for compact `Z`, which this module does not state).

## The module (as dispatched)

Statements (module header, verbatim in substance):

- `theorem_Sprime` — Theorem S′, finite form, on `ℂⁿ` for any finite `n`: `d k = I − c_k h_kh_k†`, `|h_k| = 1`,
  `c_k ∈ (1, 2]`, `c_k < n`, `⟨d_j, d_k⟩ ≥ 0` for all `j, k`, and (CC) in the cap/co-cap form (for every ordered pair
  `j ≠ k` with `⟨d_j, d_k⟩ > 0`, every `v` with `|v|² < c_j|⟨h_j|v⟩|²` has `(c_k − 1)|v|² < c_k|⟨h_k|v⟩|²`). Conclusion:
  `surgery d = dualH (surgery d)` (self-dual inside the Hermitian matrices under `Re tr(AB)`) and `surgery d` closed.
- `theorem_Sprime_C4` — the same on `ℂ⁴` with no hypothesis beyond NOTES-C11's (`c_k < 4` is automatic).
- `theorem_Sprime_ineq` — (CC) in the inequality form `(√(c_j − 1) + √(c_k − 1))² ≤ c_jc_k|⟨h_j|h_k⟩|²`; only the
  implication inequality ⇒ cap ⊆ co-cap (`cap_subset_cocap`) is proved.
- `pr_defect_defect` — `⟨d_j, d_k⟩ = n − c_j − c_k + c_jc_k|⟨h_j|h_k⟩|²` for unit `h_j, h_k`.
- `twoDefect` — C12-P's sufficiency half on `ℂ⁴`: `c_0, c_1 ∈ (1, 2]`, unit `h_0, h_1`, and `⟨d_0, d_1⟩ = 0` or the
  inequality; the pairing's sign is derived from `pr_defect_defect`, not assumed.
- `control_single_defect` — non-vacuity: `I − (3/2)|00⟩⟨00|` satisfies every hypothesis.

Proof architecture (no Hahn–Banach): `farkas_one` (one constraint, by the infimum of ratios), `farkas_finset` (induction
over a finset), `exists_psd_sub` (`(Q ∩ Z*)* ⊆ Q + cone Z`, with the kernel's PSD self-duality
JordanClassification.lean:84 and `OperationalRigidity.psd_trace_mul_nonneg` OperationalRigidity.lean:917),
`exists_qf_add_nonneg` (the local lemma, compactness of the sup-norm unit sphere), `exists_decomp` (a decomposition of least
total weight on the compact feasible set; the factorization `psdFactorization_discharged` BoundaryAudit.lean:100),
`selfDual_of_local` (the engine: `K ⊆ K*` by the four pairings, `K* ⊆ K` by Farkas + least weight + local lemma; closed as a
dual), `bessel_two` (Bessel for two orthogonal vectors, by a residual vector), `qf_defect_pos_of_perp`, `capcocap_real` (the
real core of (CC), by the identity checked in P1 below). Kernel lemmas used besides those three:
JordanClassification.lean:74 (`trace_mul_vecMulVec`), ReferenceSufficiency.lean:373, :381, :394.

## S0 — predictions and decision rules, written before the first run of any C17 script (2026-10-11T04:28Z, `date -u`)

### Preflight `experiments/c17_preflight.py` (exact; sympy and Gaussian rationals)

Checks, each with its control:

1. **P1 the identity of `capcocap_real`.** `K²((K′AG − R′p)² − K′²(1 − G²)(p² − A²)) − [K′(KA − p)(KK′A + K′p − 2KR′pG) +
   p²(KK′G − R − R′)(KK′G + R − R′)] = q₁(K² − 1 − R²) + q₂(K′² − 1 − R′²)` with `q₁ = −p²(K′² − R′²)`, `q₂ = −R²p²`
   (the `linear_combination` certificate as written in the module), as a polynomial identity. Countercontrol: dropping
   `q₂` leaves a nonzero remainder. Predicted: remainder 0; countercontrol nonzero.
2. **P2 `qf_defect`.** `v†(I − chh†)v = |v|² − c|⟨h|v⟩|²` on exact Gaussian-rational instances (`c` rational). Countercontrol:
   `hhᵀ` in place of `hh†` breaks it on a complex `h`. Predicted: holds; countercontrol fails.
3. **P3 `pr_one_defect`, `pr_defect_defect`.** `tr(I − cP_h) = 4 − c` and `tr((I − cP_h)(I − c′P_{h′})) = 4 − c − c′ +
   cc′|⟨h|h′⟩|²` for exact unit `h, h′`. Countercontrol: a non-unit `h` breaks the second. Predicted: holds; countercontrol
   fails.
4. **P4 the residual of `bessel_two`.** For orthogonal `u, x` and any `h`, with `U = |u|²`, `X = |x|²`, `H = |h|²`,
   `a = ⟨u|h⟩`, `b = ⟨x|h⟩`, `w = UXh − Xau − Ubx`: `⟨w|u⟩ = ⟨w|x⟩ = 0`, `⟨w|h⟩ = UXH − X|a|² − U|b|²`,
   `⟨w|w⟩ = UX⟨w|h⟩`, hence `|a|²X + |b|²U ≤ HUX`. Countercontrol: non-orthogonal `u, x` give `⟨w|u⟩ ≠ 0`. Predicted:
   holds on every instance; countercontrol fails.
5. **P5 cap ⊆ co-cap at the threshold.** `c = 5/4`, `c′ = 10/9` (`√(c − 1) = 1/2`, `√(c′ − 1) = 1/3`), threshold
   `s* = 1/2`; `h = e₀`, `h′ ∝ (1, 1, 0, 0)` (`s = s*`, equality in (CC)). Over an exact grid of real and Gaussian-integer
   `v` plus a near-extremal family, every `v` in the open cap of `(c, h)` lies in the open co-cap of `(c′, h′)`.
   Countercontrol: `h″ ∝ (1, 1, 1, 0)` (`s = 1/3 < s*`) has an exact witness in the cap and outside the co-cap.
   Predicted: no violation at `s = s*`; at least one witness at `s = 1/3`.
6. **P6 `capcocap_real` as stated (hypothesis `b ≥ 0` dropped).** On exact rational instances with `c = 1 + r²`,
   `c′ = 1 + r′²` (`r, r′` rational) satisfying the cap, Gram and (CC) hypotheses — `b` of either sign — the conclusion
   `(c′ − 1)V < c′b²` holds. Countercontrol: with (CC) violated, an instance satisfying the cap and Gram hypotheses
   violates the conclusion. Predicted: no counterexample; countercontrol found.
7. **P7 the control's hypotheses.** `I − (3/2)|00⟩⟨00|`: eigenvalue `−1/2`, trace `5/2 > 0`. Countercontrol: `c = 5`
   gives trace `−1 < 0` (the hypothesis `c < n` is load-bearing for `pr 1 d > 0`). Predicted: as stated.

Decision rule (fixed now): `VERDICT C17-PREFLIGHT-OK` iff all seven checks give the predicted outcome, the countercontrols
included. Any other outcome voids the preflight and blocks the dispatch until it is understood; the failed run is kept as
`c17_preflight.run1.{py,out,err}`.

### Design run (CI), at most two dispatches for C17 (the round's third is held back)

Dispatch on `dev-countermodels/c17-sprime`, cut from L with the module and one root import line
(`import OIBridge.CmSprime` after `import OIBridge.RelcSelectC5`).

Decision rule (fixed now): the run is **BUILT** iff, in the Mathlib bridge job log, (i) the Build step succeeds with
`Built OIBridge.CmSprime`; (ii) every one of the module's `#print axioms` lines (78) reports a subset of
`{propext, Classical.choice, Quot.sound}`; (iii) no `sorryAx` anywhere and `lean-axioms` passes. BUILT ⇒ the module's
statements are CONJECTURE [D] (design-built, not certified, no census disposition), which for finite `Z` replaces
Theorem S′'s [W] in the rows that cite it. Not BUILT ⇒ the failing text is kept as `lean/CmSprime.run<id>.lean`, the
error lines are recorded, and one repair dispatch may follow; not BUILT after two dispatches ⇒ C17 is recorded FAILED
(design) with the errors, and S′ stays [W].

Predictions: the build succeeds at the first dispatch (if it does not, the likeliest failure sites are elaboration
details — `rw`/`simp` shapes in `bessel_two`, `capcocap_real`, `exists_qf_add_nonneg`, `exists_decomp` — not the
mathematics); 78 prints, all within the permitted three (several basic lemmas and the definitions may print a strict
subset); the release gate red on `lean-manuscript` (a new module without a census disposition) and possibly on other
registry steps that bind to the module list; no other red step.
