# OBL-RO3-2: mixing of the prime-alphabet linear update on the infinite lattice, r1

**UNREVIEWED.** This is the writer's first draft of the bounded proof unit. It has had no independent
review. No step in it is confirmed until a review records that it is.

## Standing

- **Authorization.** #914 comment 6883249235 (`amaybaum`, 2026-11-14T19:48:13Z), quoted verbatim:
  "I approve, proceed as suggested". Its item 6, quoted verbatim: "I authorize Claude to investigate
  whether the stated prime-alphabet linear update on the infinite lattice is mixing under its uniform
  Haar measure."
  - The comment lists the unit's requirements: verify the Halmos/Rokhlin criteria from primary
    sources; prove or refute the dual-action argument, including its Laurent-polynomial determinant
    step; reconcile the outcome with SM:294; preserve the `p`-adic and finite-dimensional torus
    countercontrols; distinguish Haar invariance, invariance of `referenceState` under the
    implemented dynamics, and physical observer-interface realization; and state precisely what the
    result implies about exact visible return, recurrence-based P-indivisibility and finite dynamical
    factors.
  - Writer: Claude Code. Review: an independent review, then ChatGPT exact-head review.
- **Limits.** Paper-only. No Lean, no simulation, no manuscript change, no new physical premise, no
  merge. The owner: "Keep RO-1 as the primary thread. OBL-RO3-2 is independent and must not delay the
  sector-C specification." "Physical source remains NOT PASSED."
- **Origin.** The question is OBL-RO3-2 of `RO3-INVENTORY-r2.md` §3. The argument was first sketched
  in `REVIEW-r1.md` (M1) as a reviewer reading.
- **Base.** `main` `dfeec843bec08443b25cffe34d33dc8401c3b604`. Lean modules are under
  `verification/lean-mathlib/OIBridge/`; they were read, not built.

### Step labels

- **proved**: a complete argument is given here, on paper, from the stated inputs.
- **conditional[...]**: proved given the bracketed inputs.
- **refuted**: shown false.
- **open**: neither.

Every step is paper-level and unreviewed.

## 0. The question, stated exactly

- **Alphabet.** `F_p = Z/p` with `p` prime, and `α ∈ F_p` with `α ≠ 0`.
- **Lattice.** `Z^d` with `d ≥ 1`.
- **Carrier.** `X = ((F_p)^2)^{Z^d}`, the pair configurations `x = (u, v)` with `u, v : Z^d → F_p`.
  `X` is a compact abelian group under sitewise addition and the product topology.
- **Update.** `F(u, v) = (v, Av − u)`, with `(Av)(n) = α Σ_{j=1}^{d} (v(n + e_j) + v(n − e_j))`. This is the
  second-order form of the posited linear rule: posit-ledger item (vii) at `papers/Main.md:724`, in
  the form of `papers/SM.md:296` written on `Z^d` instead of a torus. In the kernel the second-order
  rule on a general site set is `ruleDynamics` (`SecondOrderDrive.lean:339`), the leap map
  `(p, c) ↦ (c, F(c) − p)`.
- **Measure.** `μ`, the uniform product measure on `X`. Step 1 identifies it with Haar measure.
- **Question.** Is `F` mixing for `μ`? That is, does `μ(E ∩ F^{-n} E') → μ(E) μ(E')` for all
  measurable `E, E'`?

Outside this unit:
- composite `q`;
- the rounded and all other nonlinear rules (`papers/SM.md:294`, :298);
- the gauge-coupled multi-component rule;
- every other invariant measure on `X`.

## 1. The Halmos and Rokhlin criteria: source check

**Result of the check: the primary sources could not be reached, so this unit does not apply them.**

- **Halmos.** P. R. Halmos, "On automorphisms of compact groups", *Bull. Amer. Math. Soc.* **49**
  (1943), 619–624, doi 10.1090/S0002-9904-1943-07995-5.
  - The bibliographic data were confirmed through the Crossref API.
  - The article's text was not reached: the publisher's site returned HTTP 403 to this session.
- **Rokhlin.** The 1949 paper on endomorphisms of compact commutative groups, which the review
  names, was not reached, and its bibliographic data were not confirmed.
  - Crossref returned only a later paper: V. A. Rokhlin, "Metric properties of endomorphisms of
    compact commutative groups", *Amer. Math. Soc. Transl. (2)* **64** (1967), 244–252, doi
    10.1090/trans2/064/08. This is not the 1949 paper, and it was not read either.
  - The Math-Net.Ru archive returned HTTP 403.
- **Consequence.** The two criteria in the review's sketch are:
  - (H) an automorphism of a compact abelian group is ergodic for Haar measure exactly when the dual
    automorphism has no nontrivial finite orbit;
  - (R) an ergodic automorphism of a compact abelian group is mixing.

  Neither is used here as an external theorem. Steps 3 and 4 prove, for the group `X` of §0, the two
  implications this unit needs:
  - no nonzero periodic dual character ⟹ mixing;
  - a nonzero periodic dual character ⟹ not ergodic.

  They use only the standard facts S1–S3 below. The attribution of (H) and (R) to Halmos and Rokhlin
  stays unverified from primary sources. A reviewer with access should check it, but no step depends
  on it.

**Standard facts used.** These are textbook measure theory and finite Fourier analysis. They are
stated, not re-proved.

- **S1 (characters).** For `ξ` a finitely supported function `Z^d → (F_p)^2`, set
  `⟨ξ, x⟩ = Σ_n (ξ_1(n) u(n) + ξ_2(n) v(n)) ∈ F_p`, a finite sum, and `χ_ξ(x) = ω^{⟨ξ, x⟩}`, where
  `ω = e^{2πi/p}`.
  - The `χ_ξ` are continuous characters of `X`.
  - `∫ χ_ξ dμ = 1` if `ξ = 0` and `0` otherwise.
  - `∫ χ_ξ \bar{χ_η} dμ = [ξ = η]`.

  Both integral identities hold because `χ_ξ` depends on finitely many coordinates, which are
  independent and uniform under `μ`, and a nontrivial character of a finite group sums to zero.
- **S2 (determination).** A Borel probability measure on `X` is determined by its values on cylinder
  sets, equivalently by its Fourier coefficients `∫ χ_ξ`. Haar measure on `X` is the unique
  translation-invariant Borel probability measure.
- **S3 (density).** The linear span of the `χ_ξ` is dense in `L^2(X, μ)`. Cylinder functions are
  dense, and on each finite coordinate block the characters span all functions.

## 2. The dual-action argument, step by step

**Step 1. `μ` is Haar measure on `X`. Proved.**
`μ` is translation-invariant because each coordinate's uniform law is. By S2 it is Haar measure.

**Step 2. `F` is a continuous group automorphism of `X` and preserves `μ`. Proved.**
- `F` is additive.
- Each output coordinate depends on finitely many input coordinates, so `F` is continuous.
- From `(u', v') = F(u, v) = (v, Av − u)` one gets `v = u'` and `u = Au' − v'`. So `F` is bijective
  with continuous inverse `F^{-1}(u', v') = (Au' − v', u')`.
- Invariance: `∫ χ_ξ d(μ ∘ F^{-1}) = ∫ χ_ξ ∘ F dμ = ∫ χ_{Bξ} dμ = [Bξ = 0] = [ξ = 0]`. This uses
  Step 3 and the injectivity of `B` from Step 5. So `μ ∘ F^{-1}` has the Fourier coefficients of `μ`,
  and the two are equal by S2.

**Step 3. The Koopman operator permutes characters through the dual map `B`. Proved.**
- `⟨ξ, F(u, v)⟩ = Σ (ξ_1 v + ξ_2 (Av − u)) = Σ ((−ξ_2) u + (ξ_1 + Aξ_2) v)`.
- The last equality uses `Σ_n ξ_2(n)(Av)(n) = Σ_m (Aξ_2)(m) v(m)`. This holds because `A` is
  convolution with a kernel symmetric under `n ↦ −n`; all sums are finite.
- Define `B(ξ_1, ξ_2) = (−ξ_2, ξ_1 + Aξ_2)`. Then `χ_ξ ∘ F = χ_{Bξ}`, so the Koopman operator
  `Uf = f ∘ F` sends `χ_ξ` to `χ_{Bξ}`.

**Step 4. The criterion for `X`. Proved, given S1–S3.**
- (a) **If no nonzero `ξ` has `B^n ξ = ξ` for some `n ≥ 1`, then `F` is mixing for `μ`.**
  - Take `ξ ≠ 0`. The vectors `B^n ξ`, `n ≥ 0`, are pairwise distinct: `B^n ξ = B^m ξ` with
    `n > m` gives `B^{n−m} ξ = ξ`, since `B` is injective (Step 5).
  - Hence `⟨U^n χ_ξ, χ_η⟩ = [B^n ξ = η]` is nonzero for at most one `n`. It tends to
    `0 = ∫ χ_ξ · ∫ \bar{χ_η}`.
  - For `ξ = 0` the correlation is constant and equals `∫ χ_0 · ∫ \bar{χ_η}`.
  - So `⟨U^n f, g⟩ → ⟨f, 1⟩⟨1, g⟩` for `f`, `g` in the span of characters.
  - Since `U` is unitary, `|⟨U^n f, g⟩ − ⟨U^n f', g'⟩| ≤ ‖f − f'‖ ‖g‖ + ‖f'‖ ‖g − g'‖` uniformly in
    `n`. With S3 the limit extends to all `f, g ∈ L^2`, which for indicators is mixing.
- (b) **If some `ξ ≠ 0` has `B^n ξ = ξ` with `n ≥ 1`, then `F` is not ergodic.**
  `f = Σ_{k=0}^{n−1} χ_{B^k ξ}`, summed over the distinct elements of the orbit, is `U`-invariant. It
  is orthogonal to the constants and nonzero by S1, so it is a nonconstant invariant `L^2` function.
- (a) and (b) are the two halves of (H) combined with (R), proved here for `X` only.

**Step 5. The dual module and the determinant. Proved.**
- Let `R = F_p[x_1^{±1}, …, x_d^{±1}]`, an integral domain. The map `ξ ↦ Σ_n ξ(n) x^n` identifies
  finitely supported functions `Z^d → F_p` with `R`, and the dual space with `R^2`.
- Translation by `±e_j` becomes multiplication by `x_j^{∓1}`. So `A` becomes multiplication by
  `a = α Σ_j (x_j + x_j^{-1}) ∈ R`, by symmetry of the kernel.
- On column vectors `(ξ_1, ξ_2)`, `B` is the matrix `[[0, −1], [1, a]]` over `R`, with
  `tr B = a` and `det B = 1`.
  - So `B` is invertible over `R`, which gives the injectivity used in Steps 2 and 4.
  - By Cayley–Hamilton, `B^2 = aB − I`.
- Define `D_n = tr(B^n)`. Then `D_0 = 2`, `D_1 = a` and `D_{n+1} = a D_n − D_{n−1}`, from
  `B^{n+1} = aB^n − B^{n−1}`. So `D_n = P_n(a)`, where `P_n ∈ F_p[t]` satisfies `P_0 = 2`, `P_1 = t`
  and `P_{n+1} = t P_n − P_{n−1}`. By induction `P_n` is monic of degree `n` for `n ≥ 1`; `P_2 = t^2 − 2`.
- For a 2 × 2 matrix `M`, `det(M − I) = det M − tr M + 1`. With `M = B^n` and `det B^n = 1`:
  `det(B^n − I) = 2 − P_n(a)`.
- This is the review's determinant identity, with the review's `C_n` and r2's `D_n` both equal to
  `P_n` here.

**Step 6. `2 − P_n(a) ≠ 0` in `R` for every `n ≥ 1`. Proved.**
- Write `R = S[x_1, x_1^{-1}]` with `S = F_p[x_2^{±1}, …, x_d^{±1}]`, a domain; `S = F_p` if `d = 1`.
- In `x_1`, `a = α x_1 + c + α x_1^{-1}`, with `c ∈ S`. Its top term is `α x_1`, with `α ≠ 0`.
- Over a domain the top coefficient of a product is the product of the top coefficients. So `a^k`
  has top term `α^k x_1^k`.
- `2 − P_n(t) = −t^n + Σ_{k<n} c_k t^k` with `c_k ∈ F_p`. So `2 − P_n(a)` has the term
  `−α^n x_1^n`, and every other term has `x_1`-degree at most `n − 1`. It is nonzero.
- Remark. The same conclusion holds for any nonconstant `a ∈ R`.
  - A nonconstant Laurent polynomial is transcendental over `F_p`. If it were algebraic,
    `F_p[a] ⊂ R` would be a finite field, so `a` would be `0` or a unit of finite order.
  - The units of `R` are the monomials `c x^m`, and one of finite order has `m = 0`.
  - The nonzero polynomial `2 − P_n` therefore cannot vanish at `a`.
  - The argument fails exactly when `a` is algebraic over `F_p`, which is the mechanism behind the
    countercontrols in §4.

**Step 7. No nonzero periodic dual vector. Proved.**
- Suppose `B^n ξ = ξ` with `n ≥ 1`. Multiply `(B^n − I) ξ = 0` by the adjugate of `B^n − I`. This
  gives `δ ξ_1 = δ ξ_2 = 0` with `δ = det(B^n − I) ≠ 0` (Step 6).
- `R` is a domain, so `ξ = 0`.

**Step 8. Conclusion: `F` is mixing for the uniform Haar measure `μ`. Proved, given S1–S3.**
This follows from Steps 4(a) and 7, for every prime `p`, every `α ≠ 0` and every `d ≥ 1`.

**Correction to the earlier sketch.** The review's sketch (`REVIEW-r1.md`, M1) reaches mixing through
ergodicity and (R). Step 4(a) gives mixing directly, so (R) is not needed. The determinant step of the
sketch is confirmed (Steps 5–6). Nothing in the sketch is refuted.

## 3. What the result implies, and what it does not

Throughout, "readout" means a measurable map `π : X → V` into a finite set with at least two cells
`C_a = π^{-1}(a)` of positive measure. A readout through a finite set of sites is an example.

**3.1 Exact visible return. Refuted for every readout, under `μ`. Proved.**
- If `Γ_n = I` for some `n ≥ 1`, then `π ∘ F^n = π` almost everywhere. In the cell-conditioned
  convention this is `measuredGamma_eq_one_iff` (`ObservableMeasureReturn.lean:83`, kernel-only).
- Since `F` preserves `μ`, the exceptional set's preimages are null. By induction
  `π ∘ F^{kn} = π` almost everywhere, so `μ(C_a ∩ F^{-kn} C_a) = μ(C_a)` for every `k`.
- Mixing gives the limit `μ(C_a)^2`. So `μ(C_a) ∈ {0, 1}`, which contradicts two cells of positive
  measure.
- For a readout through finitely many sites, `μ` is the product of the uniform visible law and the
  hidden law, so Main's rooted maps (`papers/Main.md:135`, :141), with an independent root and a
  root-shared hidden prior, coincide with the cell-conditioned ones.
- Mixing also gives `Γ_t(a, j) → μ(C_j)` as `t → ∞`: every row tends to the visible marginal.
- This is the discrete-time, every-positive-time statement that r2 recorded only as context. Main's
  statement is for continuous-time Hamiltonian flows at late times (`papers/Main.md:155`).

**3.2 Microscopic recurrence. Refuted on `X`. Proved.**
- `F^n ≠ id` for every `n ≥ 1`. Otherwise every function would be `F^n`-invariant, contradicting
  Step 8.
- Applied to `F` itself on finitely supported configurations, which form the same module `R^2` with
  matrix `[[0, 1], [−1, a]]` (`tr = a`, `det = 1`), Steps 5–7 show that no nonzero finitely
  supported configuration is periodic.
- Spatially periodic configurations do recur (`papers/SM.md:296`). They form a countable set, which
  has `μ`-measure zero because `μ` has no atoms.

**3.3 Recurrence-based P-indivisibility.**
- **The recurrence route is refuted within this class. Proved.** The class is: this rule, prime `p`,
  `α ≠ 0`, the measure `μ`, any readout. Every recurrence-based result consumes an identity return
  `Γ_n = I`: the one-step theorem through `φ^N = id` (`papers/Main.md:121`); history readback with
  finite recurrence (:135–137); overlap and return (:141–143); the constraint-surface form
  (`papers/GR.md:587`); and the matrix-level kernel theorems (`RecurrenceHorizon.lean:119`;
  `ObservableFactorRecurrence.lean:68`). By 3.1 that hypothesis never holds here.
- **P-indivisibility itself: open.** The result does not show that the rooted family is P-divisible.
  It does not show that the visible process is Markov, or that it lacks C4 conditional memory. A
  proof of P-indivisibility on this carrier would need another mechanism.
- **Unaffected.** The readback lemma and its accessible-window memory (`papers/Main.md:60`, :157).

**3.4 Finite dynamical factors. Refuted: there is no nontrivial one. Proved.**
- Let `ψ : X → Y`, with `Y` finite, satisfy `ψ ∘ F = S ∘ ψ` almost everywhere and `ψ_* μ = ν`.
  Suppose some `y` has `ν(y) ∈ (0, 1)`.
- Set `E = ψ^{-1}(y)`. Then `μ(E ∩ F^{-n} E) = ν({y} ∩ S^{-n}{y})`, which lies in `{0, ν(y)}` for
  every `n`. It cannot converge to `ν(y)^2`, which lies strictly between 0 and `ν(y)`. Contradiction.
- More generally, mixing excludes nonconstant `L^2` eigenfunctions: `⟨U^n f, f⟩ = λ^n ‖f‖^2` does not
  tend to zero.
- So the G-fact route of `RO3-INVENTORY-r2.md` 2.3 is closed for this rule under `μ`.

**3.5 What the result does not imply.**
- Nothing about other invariant measures on `X`. For example, the uniform measure on a spatially
  periodic sector is invariant and periodic.
- Nothing about composite `q`, the rounded or other nonlinear rules, or the gauge-coupled rule.
- Nothing about finite tori or any finite carrier. Every finite-carrier result keeps its scope (§4).
- Nothing about the invariance of `referenceState` beyond §5.
- Nothing about physical realization (§5).
- It is not a quantum realization. It concerns a classical measure-preserving system, and it does
  not discharge EXACT.
- It selects no completion and no prior. The owner's Q11 decision stands: "Do not adopt it as the
  uniquely physical prior or assume its dynamical invariance."

## 4. Reconciliation with SM:294 and the countercontrols

### 4.1 SM:294 and SM:296. Reconciled. Proved.

`papers/SM.md:294` states that the exact linear rule over `Z/q` "is not ergodic on its energy shells".
It conserves further quadratic invariants, and its largest energy shell splits into many cycles
(`papers/SM.md:296`). The result above does not contradict these statements, for three reasons.

- **Different carrier.**
  - SM's statements concern the finite torus `(Z/L)^d`. There the coefficient ring is
    `R_L = F_p[x_j]/(x_j^L − 1)`, which is finite and not a domain, and `a` is algebraic over `F_p`.
  - Step 6 fails there, as it must: SM:296 gives `F^N = I` with `N = p(p^{2m} − 1)`, so
    `B^N − I = 0` and `2 − P_N(a) = 0` in `R_L`.
  - Every dual vector of a finite group has a finite orbit, so Step 4(b) gives non-ergodicity, in
    agreement with SM.
- **The finite tori sit inside `X` as null sets.** The side-`L` torus is the `F`-invariant set of
  configurations periodic under `L e_j`. It has `μ`-measure zero (3.2), and its own uniform measure is
  a different invariant measure on `X`. Mixing under `μ` says nothing about that measure. So mixing on
  `X` does not imply ergodicity on any finite torus.
- **Conserved sums are not functions on `X`.** SM's invariants are finite sums of local densities
  on the torus. On `Z^d` the corresponding sums do not define functions on `X`. By Step 8 every
  `F`-invariant `L^2` function on `X` is constant.

`papers/SM.md:294`'s further remark, that pure linear dynamics is integrable because the real lattice
frequencies are dependent over `Q`, concerns the real-valued linear map. That is a third carrier, and
it is untouched.

### 4.2 Countercontrols

The argument must fail on each of these cases, and it does, at a named step.

| Countercontrol | Source | Where the argument stops | Consistent with source? |
|---|---|---|---|
| `p`-adic ring `(Z_p)^{2L}`, free map, Haar measure | RR: `continuous-substates/README.md:113–121`, :135–137 | Step 5 has no analogue. The dual `(Q_p/Z_p)^{2L}` is a union of finite `B`-invariant subgroups `(p^{-k}Z_p/Z_p)^{2L}`, so every dual vector has a finite orbit, and Step 4(b) gives non-ergodicity | yes: exact return of lowest-digit readouts |
| Finite-dimensional real torus `(R/Z)^{2L}`, free map | RR: `continuous-substates/README.md:92–104` (`M = F^L − I ≠ 0`, `M^2 = 0`) | Step 6: no Laurent variable, and `det(F^L − I) = 0` over `Z`. The readouts `v` with `vM = 0` are nonzero dual vectors fixed by the dual of `F^L` | yes: exact return of the difference readouts |
| Finite torus over `F_p` | `papers/SM.md:296` | Step 6: `a` is algebraic in the finite ring `R_L` | yes (4.1) |
| Constant `a` (`α = 0`) | — | Step 6: `a` is constant. The sitewise map `(u, v) ↦ (v, −u)` has order 4 | yes: periodic, not ergodic |

All four countercontrols stay as stated at their sources. None is changed.

## 5. Three statements kept apart

| Statement | Status | Grounds |
|---|---|---|
| (i) Haar invariance: `μ ∘ F^{-1} = μ` on `X` | proved | Step 2 |
| (ii-a) Bridge: on diagonal stage elements, `referenceState` equals integration against `μ` | proved on paper, given the kernel statement | `referenceState_stage` (`QuasilocalAlgebra.lean:904`) gives value `\|Conf Λ\|^{-1} tr X` on stage `Λ`. For `X = diag(f)` this is the uniform average of `f` over the configurations of `Λ`, which is `∫ f dμ` for the cylinder function `f`. Needs the instance `ι = Z^d` and site set `(F_p)^2`, as in `ruleDynamics` (`SecondOrderDrive.lean:339`) |
| (ii-b) Invariance of `referenceState` under `heisQ (ruleDynamics)` on diagonal elements | conditional[that `heis` (`QuasilocalAlgebra.lean:999`, through `permOp`, :966) sends a multiplication operator `D_f` to `D_{f ∘ φ^{±1}}`] | given that convention it reduces to (i) by (ii-a). The convention was not checked line by line here |
| (ii-c) Invariance of `referenceState` under `heisQ` on the whole quasilocal algebra, off-diagonal elements included | open | not stated on `main`. (i) does not give it. Candidate routes, unverified: stagewise trace preservation of `transported`; uniqueness of the tracial state on the completion |
| (iii) Realization at the physical observer interface: that physical preparations realize `μ`, that a physical readout is such a `π` with the product structure, and that the physical dynamics is this rule | open | the rule is posit (vii) (`papers/Main.md:724`). The uniform family is the interface's assumed preparation in the kernel (`RegionTower.lean`, header item (3)), not a sourced physical one. The owner: "Physical source remains NOT PASSED" |

(i) holds without (ii) or (iii). The consequences in §3 are statements about the mathematical model
`(X, F, μ)`. They bear on the quasilocal completion only through (ii), and on physics only through
(iii).

## 6. Step summary

| Step | Content | Label |
|---|---|---|
| §1 | Halmos and Rokhlin from primary sources | not reached; not applied |
| 1 | `μ` is Haar measure | proved |
| 2 | `F` is a continuous automorphism and preserves `μ` | proved |
| 3 | `U χ_ξ = χ_{Bξ}`, `B = [[0, −1], [1, a]]` | proved |
| 4(a) | no periodic dual vector ⟹ mixing, on `X` | proved, given S1–S3 |
| 4(b) | periodic dual vector ⟹ not ergodic, on `X` | proved, given S1–S3 |
| 5 | `det(B^n − I) = 2 − P_n(a)`, `P_n` monic of degree `n` | proved |
| 6 | `2 − P_n(a) ≠ 0` for `n ≥ 1`, `α ≠ 0` | proved |
| 7 | no nonzero periodic dual vector | proved |
| 8 | `F` is mixing for `μ` | proved, given S1–S3 |
| 3.1 | no exact visible return for any readout under `μ` | proved |
| 3.2 | `F^n ≠ id`; no nonzero finitely supported periodic configuration | proved |
| 3.3 | recurrence route to P-indivisibility unavailable; P-indivisibility itself | route refuted in the stated class; P-indivisibility open |
| 3.4 | no nontrivial finite dynamical factor | proved |
| 4.1 | compatibility with SM:294 and SM:296 | proved |
| 4.2 | four countercontrols fail at named steps | proved |
| 5 | (i); (ii-a); (ii-b); (ii-c); (iii) | proved; proved; conditional; open; open |

## 7. Bearing on the RO-3 inventory (not applied)

The inventory is not edited by this unit. If an independent review confirms the steps above, then for
the class of §0 (this rule, prime `p`, `α ≠ 0`, measure `μ`):
- the I-meas and I-qloc cells of the inventory's 1.2 would move from open to "refuted within" that
  class;
- the recurrence route of 1.3 would be recorded as unavailable there;
- the G-fact first missing step of 2.3 would be recorded as closed for that rule.

For I-qloc these changes hold only through (ii) of §5. Moving any cell needs its own authorized
revision. EXACT stays open.

## 8. Off-`main` references (AGENTS.md §A.42 item 8)

| Reference | Use | Classification |
|---|---|---|
| #914 comment 6883249235 | authorization and requirements | governance |
| `REVIEW-r1.md`; PR #1303 review 5906337933 | origin of the sketch; nit N3 (separation of (i)–(iii)) | review records; support no claim |
| `RO3-INVENTORY-r2.md` | the question as stated | context |
| Crossref API records for the two cited papers | bibliographic data only | provenance; no step depends on them |
