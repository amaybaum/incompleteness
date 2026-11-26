# COMPLEX-CARRIER-1, lane 2: the complex structure J and the real lift. Report

**WIP / UNVERIFIED. Model-written research record, paper-only; pending independent non-author
review. Nothing here is adopted, proposed for the manuscripts or authorized beyond the lane
scope (PLAN.md). Evidence layer of every result below: mathematical derivation on paper. No
computation was run; the post-hold controls of §9 are listed, not run.**

- **Accountable Issue:** #1217; parent #1211; programme #1169. Authorization and Goal link: as in
  PLAN.md (owner decision quoted in #1169 comment 7184425769, amaybaum, 2026-11-26T06:25:53Z).
- **Pinned main commit [P]:** `b6c6b80bbd4a878452e54759cc85f16c9ffb72da`; SM line numbers are at
  [P]. Input labels (P-224, P-292, ...) are those of PLAN.md §1.
- **Unit 1 (U1)** is provenance only (§A.42 item 8: classification "provenance"): every statement
  used below is re-derived here, and no result rests on U1's text or its computations.

## 0. Summary

| Question | Carrier T (torus) | Carrier Z (l²(Z^d)) | Needs b = 0? |
| --- | --- | --- | --- |
| (i) canonicity | Proved: a complex structure commuting with F and tamed by ω exists iff E is positive definite, and is then unique, J = D(−D²)^(−1/2), D = (F − F⁻¹)/2. Cubic commutation and symplecticity are consequences, not hypotheses. Dropping either F-commutation or taming gives counterexamples. | Proved: bounded such J on l² iff E coercive (abs(α μ) < 1/d); closed densely defined such J iff E positive definite (abs(α μ) ≤ 1/d); unique up to restriction to a smaller domain. | Only if J must be linear about the given origin (§2.6) |
| (i') locality | Not addressed beyond the no-go below | Proved: no site-local (ultralocal) tamed complex structure commutes with F for α ≠ 0; the unique J has infinite range | No |
| (ii) null modes at α = 1/d | Proved: J fails there (no tamed commuting complex structure on the null sector, with or without cubic commutation). Stationary states are constrained to the static isotropic subspace (w = 0); with b_A1 ≠ 0 no stationary state exists. Exclusion requires the named hypothesis H-ZM (quotient of the static zero modes), not supplied on main. | Proved: no normalizable null modes; J is closed and unbounded on l². For d ≥ 3 finitely supported vectors lie in its domain and form a core; for d = 1, 2 only under zero-mode constraints. J is bounded on the one-particle space K fixed by (F, ω), which is not l². | Stationarity at α = 1/d on T: yes (b_A1 = 0). Z results: no |
| (iii) Σ | Proved: every F-stationary second moment (any number of modes, correlated, non-Gaussian) is J-Hermitian off the null sector. Disproved beyond that: (a) a cubic-invariant stationary state whose U(6)-stabilizer is strictly smaller than U(3)×U(2)×U(1) while its on-site Σ is block-scalar; (b) block-dependent frequency dressing gives a nonzero anomalous part and stabilizer O(n_b) in the bare U(6). At α = 1/d a zero-mode condensate breaks only a real O(6) on the null sector and leaves U(6) unbroken. | Same as T on the spectral subspaces away from k = 0 (proved); the uniform background lies outside the domain on which the J-phase acts. | J-Hermiticity of the uncentred moment: yes (b = 0), or centre at the fixed point |

**Conclusion (§6).** The real lift sources a unique complex structure J, conditional on the lift
and its linearity: on the non-null sector of T, and on the one-particle space K over Z for
abs(αμ) ≤ 1/d. That J is nonlocal. It does not supply the site-local complex structure of
SM:505 / H-link. Theorem 5's use of it needs a separate bridge premise, named here **H-PF** (§6),
together with the two state conditions found in §4. Result: J itself is sourced; its
identification with Theorem 5's carrier is a separate bridge premise; and the interacting case is a
named open hypothesis.

## 1. Setting, re-derived

**Update.** On a carrier X (T = (Z/L)^d or Z^d) with six components per site, the real lift of
the second-order linear update (P-224, P-312) is, on pairs x = (u, v) = (φ(t−1), φ(t)),

    F(u, v) = (v, A v − u),   A = α Σ_j (T_j + T_j⁻¹) ⊗ M,

with M real symmetric and cubic-equivariant. At the symmetric point M = μ I_6 (the H-cust
kinetic clause; Proposition 4b, P-334). In §2 A is any bounded real symmetric operator unless
stated. The affine variant adds a constant β = (0, b), b ∈ R^6, and cubic equivariance forces b
into the A1 component (b = b_A1).

**Lemma 0.** For A symmetric:
(a) F preserves ω(x, x') = u·v' − v·u'.
(b) F preserves E(x) = u·u + v·v − u·A v (SM:296).
(c) F + F⁻¹ = A ⊗ I_2, where F⁻¹(u, v) = (A u − v, u).
(d) E(x, y) = ω(D x, y) with D = (F − F⁻¹)/2 = F − A/2, that is D(u, v) = (v − A u/2, A v/2 − u).
(e) D² = (A² − 4)/4 ⊗ I_2.

*Proof.*
- (a) ω(Fx, Fx') = v·(A v' − u') − (A v − u)·v' = u·v' − v·u', using A symmetric.
- (b) Direct expansion, as in SM:296.
- (c) Direct.
- (d) ω(D x, y) = u·u' + v·v' − ½(A u·v' + A v·u'). This is symmetric under x ↔ y because A is
  symmetric, and it is the polarization of E.
- (e) D² = (F² − 2 + F⁻²)/4 = ((F + F⁻¹)² − 4)/4.
∎

So E is not an independent datum: given F and ω, E = ½ ω((F − F⁻¹)·, ·). This is the
"matched energy" of the pair (F, ω).

**Mode reduction.** On each eigenspace of A with eigenvalue a, F acts as
f = [[0, 1], [−1, a]] ⊗ I, and E as [[1, −a/2], [−a/2, 1]] ⊗ I. The eigenspace is:
- *elliptic* for abs(a) < 2 (eigenvalues e^{±iθ}, a = 2 cos θ, θ ∈ (0, π); E positive definite);
- *parabolic* for a = ±2 (f = ±(I + N), N² = 0; E semidefinite with kernel ker N);
- *hyperbolic* for abs(a) > 2 (real eigenvalues λ, 1/λ ≠ ±1; E indefinite).

For M = μ I_6 and the nearest-neighbour A, a(k) = 2αμ Σ_j cos k_j. At αμ = 1/d the parabolic
points are k = 0 (a = 2) and k = (π, …, π) (a = −2, present on T for even L, always on Z),
reproducing P-292.

## 2. Question (i): canonicity

### 2.1 Definitions

A *complex structure* is a real linear J with J² = −1. It is *tamed* by ω if ω(Jx, x) > 0 for every
x ≠ 0, and *compatible* if in addition ω(Jx, Jy) = ω(x, y). The *positive-frequency structure* is
J_F, equal to +i on the eigenvectors of F with eigenvalue e^{iθ}, θ ∈ (0, π), and to −i on their
conjugates. Off the parabolic and hyperbolic spectrum:

    J_F = D (−D²)^(−1/2) = (1 − A²/4)^(−1/2) (F − A/2),
    J_F(u, v) = s(A)⁻¹ (v − A u/2, A v/2 − u),   s(A) = (1 − A²/4)^(1/2).

On a mode this is J_F = (f − cos θ)/sin θ, U1's candidate. J_F is a function of F alone.

### 2.2 Theorem 1 (carrier T, or any finite-dimensional carrier with A symmetric)

The following are equivalent:
- (1) E is positive definite, that is spec(A) ⊂ (−2, 2);
- (2) there is a complex structure J commuting with F and tamed by ω.

When they hold, J is unique and equals J_F. Moreover J_F:
- is compatible with ω;
- commutes with every linear map that commutes with F, so with the cubic action, the translations
  and the internal symmetries of M;
- preserves every F-invariant bilinear form;
- satisfies ω(J_F x, y) = E(s(A)⁻¹ x, y).

*(1) ⇒ (2).* By (c), J_F commutes with F. From (d), ω(J_F s x, y) = ω(D x, y) = E(x, y), so
ω(J_F x, x) = E(s⁻¹x, x) > 0. The form (x, y) ↦ E(s⁻¹x, y) is symmetric because s commutes with D
and is E-symmetric, so J_F is compatible. Invariant forms: an F-invariant bilinear form β pairs the
eigenspaces V_λ and V_μ only when λμ = 1. On the unit circle this pairs e^{iθ} with e^{−iθ}, and
J_F acts on them as (i, −i), so β(J_F ·, J_F ·) = β.

*(2) ⇒ (1).* J commutes with F, hence with A ⊗ I_2 = F + F⁻¹, hence with its spectral projections.
Two cases:
- *Hyperbolic eigenspace.* V_λ (λ real, abs(λ) ≠ 1) is ω-isotropic, since
  ω(x, y) = ω(F^n x, F^n y) = λ^{2n} ω(x, y). It is J-invariant, so ω(Jx, x) = 0 on it, which
  contradicts taming.
- *Parabolic eigenspace.* ker(f ∓ I) ⊗ W is J-invariant and isotropic, since ω_0 vanishes on the
  line ker N. This gives the same contradiction.

So the spectrum of A lies in (−2, 2).

*Uniqueness.* Let J commute with F and be tamed. On the complexified eigenspace V_θ (θ ∈ (0, π)),
J = iS with S² = 1, so S is diagonalizable. Take an eigenvector z ∈ V_θ with Sz = σz and set
x = z + z̄. Then ω(z, z) = 0, because V_θ pairs only with V_{−θ}, and so

    ω(Jx, x) = 2iσ ω(z, z̄).

For J_F (σ = 1) this equals E(s⁻¹x, x) > 0, so 2iω(z, z̄) > 0 on all of V_θ: the ω-Krein form is
definite there. An eigenvalue σ = −1 would then violate taming. So S = 1 and J = J_F. ∎

### 2.3 Which conditions uniqueness needs

- **Needed: commutation with F, and taming by ω with its sign.** Two failures show this.
  - *Without taming.* For any frequency eigenspace projection P_θ, J' = J_F(1 − 2P_θ) commutes with
    F, with the cubic action and with translations, preserves ω and E, and is not tamed. On a
    degenerate eigenspace of complex multiplicity m, J_F(P_+ − P_−) gives Grassmannian families for
    any h-orthogonal splitting. "E positive", or "E preserved by J", therefore does not fix J; the
    sign link between ω and J (positive frequency) does.
  - *Without F-commutation.* J_{F'} for any F' = F_{α'} with abs(α'μ) < 1/d is compatible, tamed,
    cubic- and translation-equivariant. So is the ultralocal quarter turn (u, v) ↦ (v, −u), which is
    tamed (ω(J x, x) = u·u + v·v). Neither commutes with F for α' ≠ α, α ≠ 0.
- **Not needed:** cubic commutation and symplectic compatibility. Both follow (Theorem 1).
- **Not an extra hypothesis:** positivity of E. It is equivalent to the existence of a tamed
  commuting J (Theorem 1, (1) ⇔ (2)), and E is fixed by (F, ω) (Lemma 0(d)).
- **Robustness under change of symplectic form (pressure test).** Every F-invariant antisymmetric
  form off the parabolic and hyperbolic spectrum has the form ω_B = ω(B·, ·), with B in the
  commutant of F and ω-self-adjoint, that is J_F-Hermitian (by the pairing argument above). Its
  matched energy is ½ω_B((F − F⁻¹)·, ·) = Q_B (SM:296). The structure tamed by ω_B and commuting
  with F is J_F·sgn(B). Hence **every conserved symplectic form whose matched energy is positive
  definite selects the same J_F.** An indefinite B flips J on B-negative subspaces, and its
  matched energy Q_B is then indefinite. J_F depends on F and on the positive-energy orientation
  only.

### 2.4 Theorem 1Z (carrier Z: l²(Z^d; R^6)²)

A is a bounded self-adjoint convolution operator. ±2 are never eigenvalues: an eigenvector would
need a(k) = ±2 on a set of positive measure, while a(k) = ±2 only at isolated points.

- **(a) Bounded case.** A bounded J on l², commuting with F and tamed (ω(Jx, x) > 0 for x ≠ 0),
  exists iff spec(A) ⊂ (−2, 2), that is E ≥ c‖x‖² (abs(αμ) < 1/d). It is then J_F, which is
  bounded because s(A) ≥ s_0 > 0.
  - *If:* as in Theorem 1.
  - *Only if:* on the spectral subspace of A for a compact I ⊂ (−2, 2), J equals J_F by (c) below,
    and ‖J_F P_I‖ = sup_I s⁻¹ → ∞ as I approaches ±2. So a bounded J forces spec(A) to stay away
    from ±2. A spectral part beyond ±2 is excluded by the isotropy argument of Theorem 1.
- **(b) Closed case.** A closed, densely defined J with F J ⊂ J F, F⁻¹J ⊂ J F⁻¹, J D(J) ⊂ D(J),
  J² = −1 on D(J) and ω(Jx, x) > 0 on D(J)∖{0} exists iff spec(A) ⊂ [−2, 2], that is E positive
  definite (abs(αμ) ≤ 1/d). The maximal one is the multiplication operator J_F(k) on its maximal
  domain. It is closed, and D(J_F²) = D(J_F) because J_F(k)² = −1 pointwise.
- **(c) Uniqueness.** Any J as in (b) commutes with the bounded Borel functions of A. This follows
  for a closed operator commuting with a bounded self-adjoint operator, by strong limits of
  polynomials. So J reduces on each H_I (I ⊂ (−2, 2) compact). There Theorem 1's eigenvector
  argument applies to the spectral (Riesz) subspaces of F for the upper and lower arcs: a vector
  w ≠ 0 with −iJw = −w on the upper arc would violate taming. Hence J = J_F on D(J) ∩ H_I. By
  closedness of J_F, J ⊂ J_F. **J_F is the unique maximal such structure, and every other is a
  restriction of it.**

### 2.5 Proposition 2 (locality trilemma)

Let M = μ I_6 and α ≠ 0. Consider three properties of a complex structure on phase space:
- (a) it is site-local (ultralocal);
- (b) it commutes with F;
- (c) it is cubic-equivariant and tamed by ω.

Any two can hold, never all three. Moreover (a) and (b) together already exclude taming, and also
exclude cubic equivariance.

- *(a)+(c).* The cubic-equivariant tamed ultralocal structures are, on each isotypic block, a
  tamed 2×2 structure on (u, v): one point of the upper half-plane per block. This is an H³
  family, including the quarter turn. It is not canonical.
- *(b)+(c).* J_F, unique (Theorem 1). Its symbol entry s(k)⁻¹ is not a trigonometric polynomial:
  s⁻² = (1 − a²/4)⁻¹ would make 1 − a²/4 a unit of the Laurent ring, that is a monomial, but it is
  real, even and nonconstant. So J_F has infinite range on Z. For abs(αμ) < 1/d the symbol is
  real-analytic, and the decay of J_F's kernel is exponential (Paley–Wiener; derivation-level, not
  proved here in detail). At αμ = 1/d the symbol is singular like abs(k)⁻¹ and the decay is a power
  law.
- *(a)+(b).* Write J = [[P, Q], [R, S]] ⊗ 1_sites with site-independent internal blocks. Then
  JF = FJ gives R = −Q and S = P + AQ. Ultralocality of AQ with α ≠ 0 forces Q = 0, so
  J = diag(P, P) with P² = −1 on R^6. Then x = (u, 0) gives ω(Jx, x) = 0, so J is not tamed. And
  no P commutes with the cubic action, whose commutant on R^6 = T_1 ⊕ E ⊕ A_1 is the real
  block-scalars R³ (Schur, all three real type).
∎

**Consequence.** The complex structure "at a site" on which M acts (SM:505, V_K = C^6) cannot be
both site-local and dynamics-compatible. On configuration space R^6 no cubic-equivariant complex
structure exists at all (Schur). The real lift's J lives on phase space (u, v) and is nonlocal.
This is a hidden assumption in the reading of H-link's V_link ⊗ C^m (SM:362) as a site-level
complex carrier.

### 2.6 b-dependence of (i)

A linear J (origin 0) commuting with the affine map F_b(x) = Fx + β needs Jβ = β, hence β = 0,
since J²β = β would give −β = β. If J is allowed to be centred at a fixed point x* of F_b, the
centred structure x* + J_F(x − x*) commutes with F_b. A fixed point exists:
- iff (A − 2)u = −b is solvable;
- that is, always for abs(αμ) < 1/d;
- and at αμ = 1/d iff b_A1 = 0.
Theorem 1 and Theorem 1Z concern the linear part and do not need b = 0.

### 2.7 Status of (i)

- **T: settled by proof**, conditional on LIN. The conditions are identified: F-commutation plus
  taming are needed; cubic commutation and compatibility are consequences; E-positivity is
  equivalent to existence.
- **Z: settled by proof** for both the bounded and the closed formulations, uniqueness being up to
  restriction.

## 3. Question (ii): null modes at α = 1/d (M = μ I_6, μ = 1)

### 3.1 Carrier T

The null sector is V_null = V_0 ⊕ V_π: the constant mode (12 real dimensions) and, for even L,
the staggered mode (12). It is ω-orthogonal to the rest V_rest and F-invariant.

**Proposition 3 (J fails on the null sector).**
- (a) No complex structure on V_null commutes with F and is tamed by ω. No cubic hypothesis is
  needed. *Proof:* parabolic case of Theorem 1.
- (b) The commutant of F on V_0 is {I⊗X + N⊗Y : X, Y ∈ M_6(R)}. A square root of −1 in it needs
  X² = −1. With cubic commutation X is block-scalar real, so none exists. This re-derives U1's
  statement.
- (c) Without cubic commutation, commuting but untamed complex structures do exist (X any complex
  structure on R^6, Y = 0). U1's no-go therefore rests on cubic commutation, and taming gives the
  stronger, cubic-free no-go of (a).
- (d) The symplectic commutant of F on V_0 is {I⊗X + N⊗Y : X ∈ O(6), XᵀY symmetric}. Its compact
  part is O(6): the null sector carries a real O(6), not U(6).

Consequently the custodial U(6) of SM:130, acting as I⊗X + J_F⊗Y on V_rest, extends to the
whole phase space only by acting on V_null through a separate null-sector symmetry (for example
trivially). It is not a group acting on the six-link carrier at k = 0.

**Proposition 4 (stationarity constrains the null sector; role of b).**
- (a) With b = 0, every F-stationary second moment C (FCFᵀ = C) restricted to V_0 or V_π
  vanishes on the drift directions. *Proof:* in the Jordan basis (x_0, w), F = ±[[1, 1], [0, 1]]
  per component, and FCFᵀ = C forces C_ww = 0 and C_xw = 0. So stationary states are supported on
  the static subspace L_0 = ker N ⊕ ker N', which is ω-isotropic and is the E-null space
  (E((1, 1)) = 0 at a = 2; E((1, −1)) = 0 at a = −2). On L_0, F acts as ±1, ω vanishes, and no
  tamed or compatible J can act.
- (b) With b_A1 ≠ 0, no F_b-stationary probability measure exists on T at α = 1/d.
  *Proof:* w_A = Σ_n (v_n − u_n)·e_A1 obeys w_A ↦ w_A + N b_A1, using Σ_n (Av)_n = 2Σ_n v_n at
  α = 1/d. No probability law on R is invariant under a nonzero translation.

This is the only place in this report where b = 0 is a necessary condition. It is the resonant
uniform A1 locus of #1049 Q-β.

**Proposition 5 (what exclusion requires).** The coisotropic reduction of V by L_0, that is
L_0^{⊥ω}/L_0 = {w = 0}/L_0 ⊕ V_rest, is exactly V_rest, with its unique J (Theorem 1). It is the
composite of two operations:
- the constraint w = 0, which stationarity supplies under b = 0 (Proposition 4);
- the quotient of the E-null static subspace L_0, equivalently taking the energy seminorm as the
  topology, equivalently declaring uniform static shifts (constant, and staggered at period two)
  unobservable.

The constant shift x ↦ x + c(1, 1) commutes with F (and with F_b). Its momentum w is conserved
iff b_A1 = 0. The staggered shift by the eigenvector (1, −1)(−1)^{abs(n)} anticommutes with F, so
only its level 0 is invariant. The second operation is a choice. A corpus-wide search of papers/
at [P] (zero mode, shift symmetry, uniform shift) finds only SM:292's statement that a zero-mode
treatment is required, and no premise supplying it. It is named **H-ZM** (the static zero modes are
gauge: quotiented by the E-null space). It is not adopted here.

**Status of (ii) on T: settled by proof.** The null sector is where J fails. It is constrained by
stationarity, which needs b_A1 = 0. It is excluded only under the named hypothesis H-ZM, which is
not supplied on main.

### 3.2 Carrier Z

**Proposition 6.**
- (a) **No normalizable null modes.** ±2 are not eigenvalues of A on l² (§2.4).
- (b) **Domain.** J_F is closed and unbounded on l². Near k = 0,

      J_F(k) = s_k⁻¹ [[−c_k, 1], [−1, c_k]],  s_k ~ abs(k)/√d,

  and applied to x̂ it equals s_k⁻¹ (v̂ − û)(1, 1) + O(1). Near k = (π, …, π) it equals
  s_k⁻¹ (û + v̂)(1, −1) + O(1). For finitely supported x the singular part is in L² iff
  ∫ abs(k)⁻² d^dk converges near 0, that is d ≥ 3. For d ∈ {1, 2}, x ∈ D(J_F) iff
  Σ_n (v_n − u_n) = 0 and Σ_n (−1)^{abs(n)} (u_n + v_n) = 0 per component. For d ≥ 3 the
  finitely supported vectors form a core: the graph norm is the L² norm for the finite measure
  (1 + ‖J_F(k)‖²) dk, in which trigonometric polynomials are dense.
- (c) **Topology.** J_F preserves every form E(h(A)·, ·) with h > 0, so it is isometric in the
  energy norm. The energy completion H_E identifies near-static uniform vectors with 0, so on Z
  that completion performs the H-ZM quotient. In H_E, however, ω is unbounded. The completion K in
  g(x, y) = ω(J_F x, y) = E(s⁻¹x, y) is the one in which ω and the inner product are both bounded
  and J_F is a compatible isometry: the one-particle (Kähler) space. It is fixed by (F, ω), and
  K ≠ l². For d ≥ 2 finitely supported vectors lie in K; for d = 1, under the momentum constraints
  of (b).
- (d) **IR degeneration.** J_F(k)(1, 1) = tan(θ_k/2)(1, −1) → 0 and
  J_F(k)(1, −1) = −cot(θ_k/2)(1, 1) → ∞ as k → 0. The phase rotation e^{tJ} acts on near-static
  uniform vectors as cos t, not as an isometry.

**Status of (ii) on Z: settled by proof.** The null-mode obstruction of T does not occur:
- there is no normalizable null vector;
- J_F exists, unique (Theorem 1Z), with domain containing all local states for d = 3.

Its price is the domain issue: J_F is unbounded on l², bounded on K, and K is not l². Whether the
physical carrier on Z is K, H_E or l² is a choice. Only K makes J a bounded compatible structure,
so this choice is an assumption, named **H-top**.

**Carrier dependence (exposed).** On every finite torus the obstruction stands. Its absence on
Z^3 is an infinite-volume property of the k = 0 singularity, which is integrable for d ≥ 3. A
statement about J that holds on Z is not transferred to T, and the reverse also fails.

## 4. Question (iii): Σ and the stabilizer

The field map is φ_n = Φ_n(x) = ℓ_n(x) − i ℓ_n(J x), with ℓ_n(x) = u_n (or v_n). This map is
J-linear: Φ_n(Jx) = iΦ_n(x). It is the only way to obtain a C^6-valued field on which the J-phase
acts as multiplication by i. Then:
- Σ_n = E[Φ_n Φ_n†] is Hermitian by construction;
- the content of "J-Hermitian" is the vanishing of the anomalous part S_n = E[Φ_n Φ_nᵀ], which
  equals the vanishing of the J-anti-invariant part C_− = (C − J C Jᵀ)/2 of the phase-space second
  moment C.

### 4.1 Proposition 7 (stationary ⇒ J-Hermitian)

Let C be any second moment stationary under the linear F (FCFᵀ = C). The state may be multi-mode,
correlated, non-product or non-Gaussian.
- **T:** C_− = 0 on V_rest.
- **Z:** P_I C_− P_{I'} = 0 for all compact I, I' ⊂ (−2, 2).

*Proof.*
- **T.** C pairs eigenvalues λ, μ of F only when λμ = 1. A J-anti-invariant pairing would join
  e^{iθ} with e^{iθ'}, θ, θ' ∈ (0, π), and e^{i(θ+θ')} ≠ 1.
- **Z.** On H_I ⊕ H_{I'} with complex structure J_F and inner product g, F is a unitary U whose
  spectrum lies in a compact arc Γ of the open upper half circle. C_− corresponds to a bounded
  antilinear Ā with ĀU = UĀ, hence Ā ψ(U) = ψ̃(U) Ā with ψ̃(z) = conj(ψ(z̄)). Choose ψ continuous,
  equal to 1 on Γ and 0 on its conjugate arc. Then ψ(U) = I and ψ̃(U) = 0, so Ā = 0.
∎

Two facts about Proposition 7:
- **No need for cubic or translation invariance.** It strengthens U1's one-mode product statement
  to all F-stationary states.
- **b-dependence.** With b ≠ 0 and abs(αμ) < 1/d, the uncentred moment C + x*x*ᵀ has a
  J-anti-invariant part, since J_F(1, 1) is not proportional to (1, 1) at k = 0. J-Hermiticity of
  the uncentred Σ therefore needs b = 0, or centring at x*.

### 4.2 Proposition 8 (on-site Σ and its stabilizer)

If the state is in addition invariant under the cubic rotations about the site n, then
Σ_n = 2 ℓ_n C ℓ_nᵀ is real and block-scalar: a P_{T1} + b P_E + c P_{A1}. Its stabilizer in the
U(6) acting through J (u = I⊗X + J_F⊗Y) is U(3)×U(2)×U(1) iff a, b, c are distinct.

*Proof.*
- Since C_− = 0, Re S_n = 0, and Im S_n = ℓ(CJᵀ + JC)ℓᵀ = 0.
- Σ_n − 2ℓCℓᵀ = 2iℓCJᵀℓᵀ is antisymmetric, real-coefficient and cubic-equivariant, hence zero:
  the cubic commutant is the real block-scalars, which are symmetric.
- Schur gives the block form.
∎

**Scope of the full state's symmetry.** If the full second moment has the form
C = Σ_b C_b ⊗ P_b with the C_b pairwise distinct (H-cust's condensate clause stated for the whole
two-point function), its U(6)-stabilizer is exactly U(3)×U(2)×U(1). *Proof:* pick a spatial
vector ψ with pairwise distinct values ⟨ψ, C_b ψ⟩; such ψ exist off three proper quadrics. Then
compare spectral projections.

### 4.3 Counterexample 9 (on-site Σ does not fix the unbroken group)

Take L large on T, or Z. Pick a generic k_0: coordinates distinct, nonzero and not π, so that no
cubic rotation maps k_0 to ±k_0. Let Q = |t⟩⟨e| + |e⟩⟨t|, with t ∈ T_1 and e ∈ E unit vectors.
Set

    C = κ G⁻¹ ⊗ I_6 + ε Σ_{g ∈ O} g (Π_{k_0} G⁻¹ ⊗ Q) g⁻¹,

where:
- G⁻¹ is the inverse J-metric, which is F-invariant;
- Π_{k_0} projects onto the real mode pair {±k_0} (on Z, a smooth bump around it);
- ε is small.

Then:
- C is positive, F-stationary, J-Hermitian, translation-invariant and cubic-invariant;
- on the k_0 subspace it equals κ + εQ internally, so every stabilizing u commutes with Q, and
  e^{iφ P_T1} does not;
- the state's U(6)-stabilizer does not contain U(3)×U(2)×U(1);
- Σ_n is unchanged by the ε term, because the cubic average of an intertwiner T_1 → E vanishes.

So Theorem 5's step from Σ = ⟨φφ†⟩ to the unbroken group needs H-cust's condensate clause on the
full two-point function, not only on the on-site Σ (a hidden ambiguity in SM:342 and SM:374).

### 4.4 Counterexample 10 (dressing: the bare J does not survive block-dependent frequencies)

One mode, bare frequency θ (c = cos θ, s = sin θ). Take the state stationary under a dressed
F' = f(2c') with c' ≠ c, for example the thermal covariance
C = κ'[[1, c'], [c', 1]], κ' = 1/(1 − c'²). With Φ = u − i(v − cu)/s,

    S = E[Φ²] = 2κ'(c' − c) e^{−iθ} / s²  ≠ 0.

In a block of multiplicity n_b, with C = C_b ⊗ I and C_− ≠ 0, the stabilizer in the bare U(n_b)
is O(n_b). *Proof:* writing u = X + iY, invariance requires XXᵀ − YYᵀ = I and XYᵀ + YXᵀ = 0,
because C_− and C_−Jᵀ are linearly independent. With unitarity this gives Y = 0.

Hence, if the blocks are dressed to distinct frequencies, the stationary dressed state's
stabilizer in the bare custodial U(6) is O(3)×O(2)×O(1) on dressed blocks: dimension 4, not 14.
The alternative is to use the dressed J' = ⊕_b J_{θ_b}, which is unique for F' by Theorem 1. Then
the symmetry of F' is only U(3)×U(2)×U(1), and no U(6) exists to be broken.

The anomalous ratio abs(S)/κ' grows like (c' − c)/s². In the massless IR (s ~ abs(k)) a dressing
of order m² gives an order-one anomaly for abs(k) ≲ m.

A sector-common dressing (all blocks at one θ', as SM:338 states for the one-loop term from a
component-local operator) keeps a U(6), with J_{θ'}. So the requirement is H-cust's kinetic clause
holding **for the same linear dynamics under which the condensate state is stationary**.

### 4.5 Proposition 11 (zero-mode condensate at α = 1/d)

- **T.** A uniform (k = 0) condensate at αμ = 1/d lies in V_0. By Proposition 4 its stationary
  part is static, in L_0, where U(6) acts trivially (Proposition 3(d)). A block-scalar static
  zero-mode condensate breaks the null-sector O(6) to O(3)×O(2)×O(1) and leaves U(6) unbroken. It
  cannot produce U(6) → U(3)×U(2)×U(1). For abs(αμ) < 1/d, k = 0 is elliptic and Proposition 8
  applies. On T, a non-macroscopic zero-mode occupation contributes O(1/N) to Σ_n.
- **Z.** A uniform background is not in l², K or H_E (in H_E it is 0). By Proposition 6(d) the
  J-phase degenerates on near-static uniform vectors. So the U(6) is not defined on it.

Which reading Theorem 5 intends is not fixed in SM:340: a local bilinear expectation, or a
macroscopic uniform condensate. Under the first, Propositions 7–8 and Counterexamples 9–10
apply. Under the second at the normalized branch, Proposition 11 gives a negative result.

### 4.6 Interacting (nonlinear) case: named gap

The positive-frequency J is defined by a linear F. For a nonlinear lift (POSIT-MIN D1(c), or the
rounded rule) there is no dynamics-defined J without a chosen linearization. Counterexample 10
shows that the result depends on that choice. Named open hypothesis **H-PF-int**: the interacting
stationary state's two-point function is stationary under one custodially scalar linear map, whose
J is used.

### 4.7 Status of (iii)

On both carriers:
- **proved** for states stationary under the same custodially scalar linear F (Propositions 7–8),
  with H-cust's condensate clause on the full two-point function;
- **disproved** in general beyond that (Counterexamples 9 and 10), and for the zero-mode reading
  at α = 1/d (Proposition 11);
- **open** for the interacting case under the named gap H-PF-int.

## 5. Named assumptions

| Name | Content | Where it enters | Status |
| --- | --- | --- | --- |
| LIN | The lift is linear, by A5 or by the lift-level linearity of POSIT-MIN D1(b) (SM:224, SM:240) | Every result. Lane 1 (#1049) traces A5 consumers, including this route. | Conditional input; not established here |
| LIFT | The real lift itself (U1 B12) exists as the observer-level description | Every result | Not claimed |
| b = 0 | Zero affine offset (b_A1 = 0) | Needed: Proposition 4 (stationarity on T at α = 1/d); J-Hermiticity of the uncentred Σ (§4.1); a linear J about origin 0 (§2.6). Not needed: Theorems 1 and 1Z, Proposition 2, Proposition 6, Counterexamples 9 and 10 | Posit status per #1049 |
| abs(αμ) ≤ 1/d | Elliptic or parabolic spectrum | Theorems 1 and 1Z | Normalization is observer-level (SM:232); no J for abs(αμ) > 1/d |
| H-cust (kinetic) at the stationary dynamics | M scalar for the linear map under which the state is stationary | Existence of U(6) (§4.4) | Proposition 4b supplies it at the bare symmetric point only |
| H-cust (condensate), full two-point form | C = Σ_b C_b ⊗ P_b | Proposition 8 scope; Counterexample 9 | Premise (SM:374); its on-site form is insufficient |
| H-ZM | Static zero modes are gauge (E-null quotient) | Exclusion of the null sector on T (Proposition 5) | Named; not supplied on main; not adopted |
| H-top | The Z carrier is the one-particle space K | J bounded on Z at α = 1/d (Proposition 6) | Named; not adopted |
| H-PF | SM's φ is the J-linear positive-frequency field Φ of the real lift | Theorem 5's use of J (§6) | Named bridge premise; not adopted |
| H-PF-int | As H-PF, for the interacting state | §4.6 | Named open hypothesis |

## 6. Conclusion

1. **J is sourced by the real lift, conditional on LIN and LIFT.**
   - The real lift determines one complex structure: the positive-frequency J_F = D(−D²)^(−1/2).
   - It is the only complex structure that commutes with the update and is tamed by any conserved
     symplectic form with positive matched energy.
   - On T it exists exactly when E is positive definite. At α = 1/d it exists on the non-null
     sector, or on all of phase space after H-ZM.
   - On Z it exists as a closed unbounded operator on l² for abs(αμ) ≤ 1/d, bounded on K.
   - Cubic equivariance and symplectic compatibility are consequences.
   - No real-lift statement here transfers to the fundamental Z/q level.
2. **Theorem 5's complex carrier is not supplied by J alone.**
   - J_F is nonlocal. No site-local complex structure commutes with the update (Proposition 2).
     So SM:505's "complex inner-product structure V_K = C^6" at a site, and H-link's ⊗C^m read
     site-locally, are not this J.
   - Using J in Theorem 5 requires the bridge premise H-PF (SM's φ is the J-linear
     positive-frequency field).
   - It also requires the condensate state to be stationary under the same custodially scalar
     linear map (Counterexample 10), with H-cust's condensate clause on the full two-point function
     (Counterexample 9).
   - It further requires the condensate to be a non-zero-mode object at α = 1/d (Proposition 11).
3. **Under these conditions**, Theorem 5's U(6) → U(3)×U(2)×U(1) holds with the real-lift J,
   on T and on Z (Propositions 7–8).
4. **Overall classification:**
   - **J sourced conditional on the lift** for the structure itself;
   - **separate bridge premise (H-PF)** for its identification with Theorem 5's carrier;
   - **named open hypothesis (H-PF-int)** for the interacting case.
   In the audit vocabulary this is class C (conditional structural), Layer 0, architecture
   emergent (observer-level lift).
5. **Correctness bands unchanged.** This is internal work on the consistency axis (§A.23).

## 7. Productivity verdict

**The fixed test (PLAN.md §6) is met, pending independent review.**
- **Settled questions.** (i) is settled on T and on Z by proof, with the conditions identified.
  (ii) is settled on both carriers. (iii) is proved in a stated class and disproved beyond it by
  two counterexamples. Each is strictly stronger than U1's "candidate off the null modes".
- **Bridge.** J is shown to be a separate bridge for Theorem 5 through H-PF and the locality
  trilemma.
- **Hidden assumptions exposed:**
  - site-locality versus dynamics-compatibility (Proposition 2);
  - the on-site versus full two-point reading of H-cust's condensate clause (Counterexample 9);
  - dressing dependence (Counterexample 10);
  - b_A1 = 0 at the normalized branch (Proposition 4(b));
  - the topology on Z (Proposition 6);
  - taming, not E-positivity, as the selecting condition (§2.3).

**Skepticism applied to the favourable branches.**
- **Uniqueness (Theorem 1).** It was pressure-tested against the non-uniqueness of the conserved
  symplectic form (§2.3, last item). It survives for positive matched energy, and fails, as
  stated, for indefinite ones.
- **Absence of null modes on Z^3 (Proposition 6).** This is paid for by unboundedness on l² and
  by the H-top choice, and it does not transfer to T.
- **Stationary ⇒ J-Hermitian (Proposition 7).** It is narrow: it holds only for stationarity
  under the same linear F, and Counterexample 10 breaks it under dressing.

**Classification of findings (§A.31).**
- New: Proposition 2; Proposition 4; Proposition 5 with H-ZM; Proposition 6; Counterexamples 9
  and 10; Proposition 11.
- Positive: Theorem 1 and its robustness; Proposition 7.
- Elaborating: Proposition 3, which strengthens U1's null-mode no-go to a cubic-free form.

## 8. Open nodes

- **O1.** H-ZM: whether any premise on main makes uniform static shifts (constant, and staggered
  at period two) unobservable for the observer of SM §4.1. Not supplied at [P].
- **O2.** H-PF: the identification of SM's φ with Φ_n, and the choice of ℓ_n. The choice of ℓ_n
  changes Σ_n only within the real block-scalars.
- **O3.** H-PF-int: a dynamics-defined J for the nonlinear lift, and the effect of dressing on it.
- **O4.** Whether H-cust's condensate clause in its full two-point form follows from any stated
  premise.
- **O5.** Whether the nonlocality of J_F (exponential tails for abs(αμ) < 1/d, power law at 1/d)
  is compatible with H-link's physical reading. Proposition 2's decay rates are at the level of a
  derivation sketch.
- **O6.** A pre-condensate M that is not scalar (explicit block splitting) has only
  U(3)×U(2)×U(1) as symmetry. Theorem 5's breaking reading then does not apply. Not pursued.
- **O7.** The relation to the Weil-representation polarization of the per-site phase space (C5
  audit candidate 2, cited in U1). Not addressed.
- **O8.** LIN and LIFT, in lane 1 (#1049) and unit 1's B12. NQ-1059 is not started.

## 9. Post-hold controls (listed, not run)

To be run only after the A1 hold lifts and under an owner authorization covering computation.
- **C1.** Unit 1 exact check C1 (r2 checks script at `820519cf`, off main; provenance). Real
  commutant dimension 3 of the cubic action on R^6; multiplicities (1, 2, 3); stabilizer
  dimensions 4 and 14. Supports Proposition 2's Schur step and §4.2.
- **C2.** Unit 1 exact check C2(a)–(d), same script. J² = −1 and the symplectic commutant u(6) at a
  non-null mode; the stationary product covariance stabilizer; the null-mode obstruction with its
  countercontrol. Supports Theorem 1 at one mode, Proposition 3(b) and Proposition 8.

Proposed exact controls for this report's new claims:
- **X1.** On a small torus with exact algebraic arithmetic: J_F = s(A)⁻¹(F − A/2) satisfies
  J² = −1, [J, F] = 0 and ω(J·, ·) positive definite. Countercontrol: J_F(1 − 2P_θ) is not tamed.
- **X2.** Commutant of (I + N) ⊗ I_6 in sp(12, R): the form I⊗X + N⊗Y with X ∈ O(6) and XᵀY
  symmetric. Countercontrol: an elliptic mode gives u(6).
- **X3.** Jordan-block stationarity forces C_ww = C_xw = 0. Countercontrol: an elliptic mode admits
  C_ww ≠ 0.
- **X4.** Symbolic S = 2κ'(c' − c)e^{−iθ}/s². Countercontrol: c' = c gives 0. Also the stabilizer
  Lie-algebra dimension o(n) under C_− ≠ 0.
- **X5.** Stabilizer dimension in u(6) of κ + εQ (T_1–E mixing) is below 14. Countercontrol:
  block-diagonal distinct values give 14.
- **X6.** Solving JF = FJ for an ultralocal J gives diag(P, P). Countercontrol: a nonlocal J_F.

Each verdict prints only over green controls (§A.29); the decision rule is the statement as
written above.

## 10. Depth-first node log

- **N1 (i).**
  - **N1.1** One elliptic eigenspace: commutant M_m(C); tamed commuting implies J_F. Verdict:
    proved (Theorem 1).
  - **N1.2** Drop each condition: counterexamples (§2.3). Verdict: taming and F-commutation are
    necessary; cubic commutation and compatibility are redundant.
  - **N1.3** Non-elliptic modes: isotropy. Verdict: existence ⇔ E positive definite.
  - **N1.4** Z: spectral reduction; bounded ⇔ coercive E; closed ⇔ positive E. Verdict: proved.
  - **N1.5** Pressure test on ω_B. Verdict: robust for positive matched energy.
  - **N1.6** Locality. Verdict: trilemma (Proposition 2), new.
- **N2 (ii).**
  - **N2.1** Tamed no-go without cubic commutation. Verdict: elaborating (Proposition 3).
  - **N2.2** Stationary implies w = 0. Verdict: new (Proposition 4(a)).
  - **N2.3** b_A1 ≠ 0 implies no stationary state. Verdict: new, linked to #1049 Q-β
    (Proposition 4(b)).
  - **N2.4** Reduction = constraint + E-null quotient. Verdict: H-ZM named (Proposition 5).
  - **N2.5** Z: no eigenvectors; domain thresholds d ≥ 3; K; IR degeneration. Verdict: new
    (Proposition 6).
- **N3 (iii).**
  - **N3.1** Stationary implies J-Hermitian. Verdict: positive (Proposition 7).
  - **N3.2** On-site Σ real block-scalar. Verdict: proved (Proposition 8).
  - **N3.3** Full-state stabilizer. Verdict: counterexample, new (Counterexample 9).
  - **N3.4** Dressing. Verdict: counterexample, new (Counterexample 10).
  - **N3.5** Zero-mode condensate. Verdict: negative, new (Proposition 11).
  - **N3.6** Nonlinear case. Verdict: named gap (§4.6).

**Passes.**
- Pass 1: derivations N1–N3.
- Pass 2: skepticism on favourable branches (N1.5, the Z price, the narrowness of Proposition 7).
  Produced Counterexample 10.
- Pass 3: b and LIN sweep. Produced Proposition 4(b) and §2.6.
- Pass 4: re-check of every displayed equivalence against its two directional proofs (§A.34):
  - Theorem 1 (1) ⇔ (2): §2.2;
  - Theorem 1Z (a) and (b): §2.4, both directions;
  - Proposition 8's "iff a, b, c distinct": stabilizer computation (if) and enlargement when two
    values coincide (only if).
  No new finding. With the stopping rule met for (ii) and (iii) on both carriers, the
  investigation stops here.
