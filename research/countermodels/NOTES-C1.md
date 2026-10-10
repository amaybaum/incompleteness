# NOTES-C1 — the two unreassessed stage-3 cones, row by row

Node C1 of `README.md`. Base L = `9f9f8257`; branch `research/countermodels`. Evidence levels: [K] certified at L
(file:line), [D] design module, [W] written argument (here), [X] exact computation (here, `experiments/`), [A] audited
archived record, [U] unsourced. Conventions as in the charter (W 3 tables, `ipW` the entrywise sum, `z_s`, `cnot` the
kernel's signed permutation, `pauliW` a construction/comparison tool only).

## 1. The objects

- `K_F2 = K({F, cnot F}) = (Q3 ∩ {F, cnot F}*) + cone{F, cnot F}` with `F = z_(−1,−1)`; `cnot F = z_(1,1)` [X D2]. Stage 3:
  U's `K_F2`, X's `K({F, cnot F})` (X's `e_(1,1)` is `z_(−1,−1)`: X writes `e_s = E00/2 − T_s/4 = z_(−s)`).
- `K(e_c) = (Q3 ∩ e_c*) + ℝ₊ e_c`, `e_c = E00 + c(E13 − E22)`, `c ∈ (1/2, 1]` (X's family; `e_1 = E0`, so `K(e_1) = K(E0)`).
  `pauliW(e_c) = (I + c(X⊗Z − Y⊗Y))/4`, spectrum `(1 + 2c)/4, (1 − 2c)/4, 1/4, 1/4` [X EC-C3].

## 2. Scripts and runs

| script | role | runs | final | replay |
|---|---|---|---|---|
| `c1_cones.py` | exact checks D0–D2, C1–C10, T, Q3 controls, CC1–CC5 on both cones (71 checks) | 2 | run 2: 71/71, `VERDICT C1-CONES-EXACT` | see LOG |
| `c1_rows.py` | the 199-row tables C1-F2, C1-EC against R6's A1/A2 reference rows | 2 | run 2: `OUTCOME COVERING-CONFIRMED` | see LOG |

Kept failed runs:
- `c1_cones.run1.*` (69/70, `NO VERDICT`): F2-C7 failed. My rule searched only the images of the defects under
  `actT reflY`; for `K_F2` both images are pure states inside `K_F2` (spectrum `{0, 1/4}`, pairing `1/8` with both
  defects — record line F2-C7r of run 2), so the search was silent. The kernel theorem
  `no_candidateCone_cnot_reflY` (K2Guard.lean:143) moves every `cnot`-invariant candidate cone through its own chain;
  run 2 checks that chain on each cone: `phiW = cnot prodState(xplus, z3) ∈ K` (H1–H2), `actT reflY phiW = idW`,
  `ipW(idW, cnot prodState(−e1, −e3)) = −2` with `cnot prodState(−e1, −e3) ∈ K` (H1–H2). Same run-2 amendment: the EC
  FCC check was strengthened to every `c` by evaluating, symbolically in `c`, the tuple that run 1's record lines had
  located (value `1 − 2c`); disclosed in the header as found from run 1.
- `c1_rows.run1.*` (control 2 failed): my parser read only `CHECK` lines, while `c1_cones.out` prints its
  countercontrols as `COUNTERCONTROL` lines (the I3.144 row cites CC5). Harness error; run 2 accepts a cited
  countercontrol id when `c1_cones.out` reports `0 failed`.

Pre-run edits of `c1_cones.py` (before run 1, recorded here): sparse evaluation of `table`, an exact Fraction interval
cover in place of a sympy one, orthonormalized bases and a systematic Gaussian-integer generator for the T faces,
the transpose added to CC4 so that CC4 is not vacuous for `K(e_c)`.

## 3. Results

### 3.1 The row tables (`c1_rows.out`, Tables C1-F2 and C1-EC)
Both cones receive, row by row, the verdict of R6's reference rows for K(E0)/K(Z_F): **118 SATISFIES, 13 FAILS,
68 NOT REACHED**, with every K-dependent verdict backed by a PASS line of `c1_cones.out` and every K-independent verdict
carried from R6's anchor (kernel line or bridge statement). EXCLUDED-BY-L: none. Every FAILS row is a hypothesis
(do-not-assume items I3.137, I3.142, I3.144, I3.150–I3.153, I3.155, I3.165; [D] four-token hypotheses I3.133, I3.135;
PT-record candidates I3.160, I3.161) — never a theorem or definition at L.

### 3.2 What the exact checks establish ([X], `c1_cones.out`)
- H1 by symbolic SOS identities over the whole ball (EC symbolic in `c`: `I − MᵀM = diag(1, 1 − c², 1 − c²) ⪰ 0`);
  H2 at level (i); the SD1/SD2/Theorem-S certificates (one simple negative eigenvalue `−a`, all others `≥ a`; for
  `K_F2` orthogonal defects and the one-violation identity `Σ_s ⟨ψ_s|Q|ψ_s⟩ = tr Q` over the orthonormal cap basis);
  `K ≠ Q3`; the `maxCone` bound; the slice.
- Level (ii) fails for both: `actT rot3(π)` moves `K_F2` (−1/2), `actC rot3(π)` moves `K(e_c)` for every `c`.
- (b) family: on `K_F2` every listed control map and target map has a witness except `actC rot3(π)`, `actT nflip`
  (both permute `{F, cnot F}`) and the transpose; on `K(e_c)` every listed one-token map has a witness valid for
  **every** `c ∈ (1/2, 1]` (exact interval cover), SWAP at `c ∈ {5/8, 3/4, 1}` only (record).
- Uniform FCC fails: `K_F2` min −1/2; `K(e_c)`: `famI = 1 − 2c < 0` at one tuple, for every `c`.
- T invariant `c(x) = dim span{y ∈ K : ipW(x, y) = 0}`: `c(F) = 15`, `c(P00) = 9` in `K_F2`; `c(e_c) = 15`,
  `c(P00) = 9` at `c ∈ {5/8, 3/4, 1}`. With [A] Y6 (automorphisms of a self-dual cone preserve `c` on extreme rays), T
  fails for both cones.

### 3.3 Written arguments ([W])
- **W1 (H3 for `K_F2`).** T6 §3.3's proof for `K(Z_F)` uses only: the defects are Bell-type with orthonormal cap
  vectors, `tr pauliW(z) > 0`, and the correction lemma for one defect. Each step holds verbatim for any subset of
  `Z_F`; for `{F, cnot F}` it gives `K_F2 = K_F2*`. Independent of, and agreeing with, U's Theorem S and X's SD2 [A].
- **W2 (H3 for `K(e_c)`).** X's characterization [A, AUDIT-X]: `K(e)` is self-dual iff `e` has exactly one negative
  eigenvalue `λ₁` and `λ₂ ≥ −λ₁`; here `λ₁ = (1 − 2c)/4`, `λ₂ = 1/4`, so exactly `c ∈ (1/2, 1]` (CC1, CC2 confirm both
  ends).
- **W3 (the defects are extreme rays).** In `K_F2`: if `F = k₁ + k₂`, `kᵢ = qᵢ + λᵢF + μᵢ cnot F`, pairing with `cnot F`
  (orthogonal to `F`, pairing ≥ 0 with every `qᵢ`) forces `μᵢ = 0` and `⟨qᵢ, cnot F⟩ = 0`; then `(1 − Σλᵢ)F = Σqᵢ ⪰ 0`
  with `F ∉ Q3` forces `Σλᵢ = 1`, `qᵢ = 0`. In `K(e_c)` the same with one defect.
- **W4 (`c(defect) = 15` for every `c`).** `K ∩ e_c^⊥ ⊇ {vv† : v†Av = 0}` with `A = pauliW(e_c)` (one negative, three
  positive eigenvalues). If a Hermitian `Y` has `v†Yv = 0` on the null cone `{v†Av = 0}`, then `Y ∈ ℝA`: the null cone is
  the real quadric of a nondegenerate form of signature (6, 2) on ℝ⁸, irreducible, so a quadratic form vanishing on it is
  a multiple of `A`. Hence the span is the hyperplane `A^⊥` (dimension 15). The instances `c ∈ {5/8, 3/4, 1}` are [X].
  The same argument gives `c(F) = 15` in `K_F2` (computed exactly).
- **W5 (`c(P00) ≤ 9`).** `ipW(P00, z) > 0` for every defect `z` (1/4 for `F`, `cnot F`; 1 for `e_c`), so `y = q + Σλz ∈ K`
  with `ipW(y, P00) = 0` has `λ = 0` and `q ⪰ 0` with `⟨00|q|00⟩ = 0`, i.e. `q|00⟩ = 0`: `y ∈ Herm(|00⟩^⊥)`, dimension 9
  [X: kernel dimension 9]. Equality by 9 independent members [X].
- **W6 (the family is genuinely one-parameter).** For `1/2 < c′ < c ≤ 1` a pure table `w` with
  `−1/c′ ≤ ⟨X⊗Z − Y⊗Y⟩_w < −1/c` lies in `K(e_c′)` and has `ipW(e_c, w) = 1 + c⟨·⟩_w < 0`; so `e_c ∉ K(e_c′) = K(e_c′)*`
  and `K(e_c) ≠ K(e_c′)`. (Stage 3 did not claim distinctness.)

## 4. The covering argument of AUDIT-R §4

AUDIT-R §4 item 1: every pair-level item at L that reaches a cone constrains the gate on products, the effects, the
single-token slices, the `maxCone` bound or the operation `actT reflY`; R6's A3 argument applies to any closed self-dual
`cnot`-invariant cone `K ⊇ SEP`; where stage 3 establishes H1–H3 for `K({F, cnot F})` and `K(e_c)`, the same 199-item
table applies.

**Verdict: CONFIRMED, with one sharpening.**
- Confirmed: no item at L excludes either cone (EXCLUDED-BY-L empty); every SATISFIES and NOT REACHED row of the reference
  holds for both; 157 rows are K-independent (def, thm, gate, inh, d4s, nr, hmg) and carry over as the argument says; the
  42 K-dependent rows (cone 12, kthm 1, b1 13, dna 9, d4f 2, d4v 3, cand 2) are checked exactly (list in `c1_rows.out`).
- Sharpening: the argument, as stated, yields R6's **A3** table, in which T (I3.161) is UNDECIDED; it does not decide T
  for these two cones. The extreme-ray computation here decides it: T FAILS for both (`c = 15` on the defect, `9` on
  `P00`), so the tables equal A1/A2 (13 FAILS), not A3.
- The FAILS rows other than T are covered by the argument through cited theorems (R6 A3: the stage-4 theorem
  "(b_min) with H1–H3 forces Q3" [A], the [D] contrapositive for FCC, stage 3/4's homogeneity theorem [W + L]); here they
  are also witnessed exactly (every (b) form on both tokens; FCC by an explicit tuple for every `c`).

## 5. Gem classification (§A.31)

- CONFIRMING: R6/AUDIT-R's classification extends to the two cones; no item at L excludes them.
- ELABORATING: T decided for both cones; FCC violation `1 − 2c` exact for the whole family; witnesses for every (b) form
  valid for every `c`; the family `K(e_c)` is one-parameter (W6).
- Record (BORDERLINE): `actT reflY` maps each defect of `K_F2` to a pure state inside `K_F2`; the K2Guard obstruction
  moves `K_F2` only through the kernel's own `phiW → idW` chain, not by moving a defect (unlike K(E0), K(Z_F)).
- No NEW structural blind spot. The one process lesson (assumption-watch): a "witness search over images of the
  defects" is not a faithful test of non-invariance; the K2Guard chain is.

## 6. What is not claimed

No kernel statement; nothing about EXOTIC-E alternatives; the T verdict for `K(e_c)` at `c ∉ {5/8, 3/4, 1}` rests on W4
[W]; FCC and KT4Core are [D] hypotheses; no realization claim. Bands unchanged (consistency-axis work).
