# Coordinator audit — `research/countermodels`, round 2

Thread head `e6d42cab` (2026-10-10; round-2 commits `d8a1461b` … `e6d42cab`). Base L = `9f9f8257`. Audited: the
round-2 rows of `RESULTS.md` (C7.1 … C7.7 with C7.1f, C7.6f; C8.1 … C8.4; C9.1 … C9.7; C10.1 … C10.3; C2.8r),
`NOTES-C7.md`, `NOTES-C8.md`, `NOTES-C9.md`, `NOTES-C10.md`, `experiments/c7_ebf_wall` (run 2; run 1 kept),
`c7_circle`, `c8_bell_sets`, `c9_omega4`, `c10_b3c_case` (run 2; run 1 kept), the receipts in `inbox/`, the handoff
proposals HP2 and HP3, `LOG.md`. No Lean work this round (no CI run to verify).

## Method

1. **Receipts.** HO-1, HO-2, HO-7 copied verbatim (sha256 `f5a2e0da…`, `13abf306…`, `6931120d…`, each equal to the
   overview file at `62cbb3cf`) and committed at `d8a1461b` with the reliance recorded in `LOG.md` (HO-1 context only;
   HO-2 for the statement of B3.C and its coverage list; HO-7 for the definition of Ω₄ only, every property
   recomputed). The receipts commit also changed the wording of a round-1 LOG entry, restored verbatim at `d70422f6`.
   Protocol satisfied.
2. **Replay.** Five scripts re-run (`python3 -I -B`, cwd `experiments/`): stdout IDENTICAL 5/5
   (`countermodels/REPLAY-LOG.txt`); stderr differs only by the thread's `exit 0` marker line.
3. **Independent check.** `countermodels/indep_checkC2.py` (own table-level code in the ψ-basis conventions of the
   round-1 check; reads nothing; decision rule fixed before the first run): run 1 **7/7 CONFIRMED**, `INDEP-C2-FIXED`,
   replay identical.
   - X0 conventions: the cap vectors `ψ_s` are real, orthonormal, entries `±1/2`; `cos t ψ_1 + sin t ψ_3` is
     maximally entangled for every `t` (symbolic), as is `(3ψ_1 + 4iψ_2)/5`; `d_{ψ_s} = 8 pauliW(z_s)`; Circ is the
     image of the Lorentz cone under the isometry `(t, u) ↦ (t/2)𝟙 + u`, hence self-dual.
   - X1 (C7.1, CC-R): `y_d = (−2, 12, 6, 4)/5` on `∂Circ` with dual ray `(12, −2, 4, 6)/5` (pairing 0, opposite
     deviation); the profile of `v = ψ_2 + ψ_3/2` outside Circ; `c₀ = (−2/5, 7/5, 19/20, 4/5)` interior; `π(y) = y_d`,
     `⟨ψ_2|y|ψ_3⟩ = 1/2`; the corrected slack identity `−Σp/2 − p_s` (symbolic).
   - X2 (C7.4, C7.5): the profile `(25, 9, 9, 1)/44` in `Circ \ O`; `π(w) ∈ Circ`; `tr(w P_v) = −3`;
     `tr(P_u σ·diag) = 1/2` for all 24 coordinate permutations and `⟨diag, σ diag⟩ ∈ {0, 4}`; `π(y5) = (1, 9, 9, 9)`,
     `x†y5x = −12`, PSD at coefficient 6 (eigenvalues 12, 6, 6, 0) and not at 8 (`6 ± 2√13`, 8, 8); the orbit bound
     equals 160 for every permutation.
   - X3 (C7.6): `d_g = Pperp − cos 2t·sz − sin 2t·sx` (symbolic); `y_1, y_2` Hermitian and strictly in `Z_circ*`;
     `tr(y_1 y_2) = −475586012673053754301/30445958586078125000000`, the thread's value, negative; B5's orthonormal
     pairs.
   - X4 (C8.1, C8.2): the witness construction on a line triple of the coordinator's choosing
     (`g₁ = ψ_1`, `g₂ = (4ψ_1 + 3ψ_3)/5`, `g₃ = (3ψ_1 − 4ψ_3)/5`, `e = ψ_2`, `ε = 9/10`): `λ = 19/256`, `⟨y, d_1⟩ = 0`,
     `⟨y, d_2⟩ = 1323/1600`, `⟨y, d_3⟩ = 109/100`, `x†yx = −323/20736`, `⟨d_k, d_1⟩ = 4c_k > 0`; countercontrols
     `ε = 1/2` (`−3/100`) and `Z_F` (all `⟨d_k, d_1⟩ = 0`).
   - X5 (C9.1): `det Hess N = 2304 s²|x|⁶`; the chain-rule identity on a rational instance; `|x|²` of rank 3; the
     rotation `(3/5, 4/5)` and `s ↦ −s` preserve `N`; the shear, the scaling and an `x₁`–`s` rotation do not.
   - X6 (C10.1): the basis `C2(1), C2(−1), |0+⟩, |1−⟩` orthonormal with two Bell and two product members;
     `CNOT = I − 2|1−⟩⟨1−|` diagonal `(1, 1, 1, −1)`; the six weight differences nonzero; `MM† = I/2`; `z` fixed by
     `H₀` and `CNOT`; the slice cone's seven extreme rays equal its seven facet normals (exact enumeration both ways),
     `≠ ℝ⁴₊`; `ℝ⁴₊ ∩ f*` has exactly the six predicted rays; both countercontrols.
4. **Written proofs read.** Theorem C7-D (the Haar-average step `⟨e, π(e)⟩ = ∫⟨e, ge⟩ dg = 0 ⇒ e = 0` by continuity at
   the identity; the extreme-ray decomposition; `y_d` extreme in Circ): sound. Lemma C8-L (`K(Z)* = cl(Q3 + cone Z) ∩ Z*`;
   `μ = 0` forced by `⟨q, d_1⟩ ≥ 0`; (L4) on `O₁`): sound. C9.1's unique-factorization step (`s²|x|⁶ = det(A)² ℓ² Q³`
   with `|x|²`, `Q` irreducible quadratics and `s`, `ℓ` linear): sound. C10.2's self-positive seed (orbit of eigenlines
   with no product vector; `c = min(2, 1/m)`): sound, CONDITIONAL on EBF as labelled.
5. **Kernel citations.** 4/4 new citations resolve at L (`cite_check_r2b.out`), including TransitiveBody.lean:602
   `exists_affine_image_eq_eball` and DenseOrbit.lean:174 `exists_affine_image_eq_eball_of_dense` (C9.3, CERTIFIED).

## Findings by row

| row | thread label | audit |
|---|---|---|
| C7.1, C7.1f | CONDITIONAL (W1); FAILED (kept) | accepted; X1 |
| C7.2, C7.3 | CONDITIONAL (W2) | accepted; proof read (method 4) |
| C7.4 | CONDITIONAL (EBF [A]; W3) | accepted; X2 (`P_v`, `w` lie in `C₀*` directly: PSD against `A`, and `π` lands in Circ = Circ*) |
| C7.5 | CONDITIONAL (EBF [A]; W4) | accepted; X2 |
| C7.6, C7.6f | CONDITIONAL (W5); FAILED (kept) | accepted; X3 reproduces the exact certificate |
| C7.7, C2.8r | OPEN | accepted |
| C8.1 | CONDITIONAL ([W]) | accepted; proof read |
| C8.2 | CONDITIONAL | accepted; X4 on a coordinator-chosen instance. Precision: NOTES-C8's countercontrol "for `Z_F` (L1) is unsatisfiable" reads better as "`Z_F` has no non-orthogonal partner, so the lemma's `y` would be `vv†`, PSD, and (L3) cannot hold"; conclusion unchanged |
| C8.3 | OPEN | accepted |
| C8.4 | CONJECTURE (C8-C) | accepted at its label |
| C9.1, C9.2 | CONDITIONAL | accepted; X5; the orbit description follows from C9.1 |
| C9.3 | CERTIFIED | verified at L |
| C9.4, C9.5, C9.6, C9.7 | CONDITIONAL | accepted; `c* ≡ 1` on `C¹` boundaries is the uniqueness of the supporting hyperplane ([W], read) |
| C10.1 | CONDITIONAL (X's single-defect characterization [A]) | accepted; X6 |
| C10.2 | CONDITIONAL (EBF [A]) | accepted; proof read |
| C10.3 | OPEN | accepted; HO-10 (bridge B7-1/B7-2) reaches this residual at CONJECTURE + (D) level, which the thread may receive |

**Label changes: none.**

## Recorded for the overview

- The EBF wall has a structural explanation: for a slice with property (N) — Circ has it, the reversed simplex R does
  not — the non-PSD extreme rays cannot all be torus-fixed (Theorem C7-D), so no surgery with fixed defects is self-dual
  with slice Circ; the full Bell-circle surgery and its κ-invariant copy fail with an exact certificate. The fibres of
  the slice map over Circ and over the simplex are not singletons (CONDITIONAL on EBF).
- Non-orthogonal Bell-type sets: every triple with a non-orthogonal pair, every finite set on one Bell circle, and the
  `W^⊥` class give non-self-dual surgeries (Theorem C8); Conjecture C8-C (self-dual iff pairwise orthogonal).
- Ω₄: `Aut(Ω₄) = O(3) × ℤ₂`, orbits = level sets of `s⁴`; the facial invariant's single-system analogue `c*` is
  constant on smooth bodies and cannot see the non-transitivity (assumption-watch marker for K∞-Trans, routed as
  HO-15); Ω₄'s cone is self-dual for no inner product.
- B3.C from the cone side: an explicit exotic cone for a case HO-2 listed as open, with the eigenline-orbit mechanism
  (routed as HO-16).
- Thread deviations disclosed (estimate-based clock times in the S0 headers and script headers, corrected by a
  provenance note with the file modification times, order S0 → script → run intact; two first runs kept) — noted, no
  action.
