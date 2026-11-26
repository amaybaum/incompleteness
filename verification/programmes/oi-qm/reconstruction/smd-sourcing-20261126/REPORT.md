# SMD-SRC-1: physical sourcing of SMD for SM Theorem 5 (#1049, #1217). Report

**WIP / UNVERIFIED. Model-written research record, paper-only. Nothing here is adopted, proposed
for the manuscripts or authorized beyond the investigation's scope. Pending independent non-author
review (PLAN.md §8).**

- **Plan:** PLAN.md in this directory, commit `6a0a11657d55f4e847b7b53cefdd1168aec2e5a1`, committed
  alone before this report.
- **Authorization and Goal link:** as in PLAN.md (owner decision `amaybaum`, #1169 comment
  7200549806, created 2026-11-26T18:30:55Z, item 4; work package WP-2, #1169 comment 7199704501).
- **Pinned main commit [P]:** `a8d4ab969e274dc6ba25cbc6021da909d5aec814`. Quoted SM lines were
  re-read at [P] (SM:136, SM:290–296, SM:312–316, SM:322, SM:340, SM:342, SM:374).
- **Evidence layers.** Theorem P and its lemmas: mathematical derivation on paper ([A]), using
  standard textbook facts named where used. Corollaries P3′ and Pα: conditional on imported
  theorem [I-Stein], stated as recalled and not re-checked against its source (no external access
  was used), and on the stated hypothesis H-αCLT, which no source theorem is yet pinned to. Witness identities: exact rational computation [C]
  (`controls.py`, output `controls-output.txt`). Spreading illustration: floating point, certifies
  nothing.
- Labels as in PLAN.md §0. Premise statuses: proved / conditional / posited / open.

## 0. Outcome

**Per-notion table (PLAN.md §3), on Z = Z^d, M = μI_6, linear offset-free branch:**

| Notion | 0 < abs(μ) < 1 | μ = 0 (boundary) |
| --- | --- | --- |
| K3 (all-moments reading), finite-range dependence, uniformly bounded moments of all orders | POSITIVE (Corollary P3, [A]) | OBSTRUCTION (CC-D) |
| K3′ (fourth-moment reading of K3), finite-range dependence, uniformly bounded fourth moments | POSITIVE, conditional on [I-Stein] (Corollary P3′) | OBSTRUCTION (CC-D) |
| K2, cumulant clustering, uniformly bounded moments of all orders | POSITIVE (Theorem P, [A]) | OBSTRUCTION (CC-D) |
| Kα, strong mixing with summable rate, uniformly bounded 2+δ moments | POSITIVE, conditional on H-αCLT (Corollary Pα), for the distance-indexed α of H-αCLT (§3) | OBSTRUCTION (CC-D) |
| K1, translation mixing, no rate | OPEN (§5) | OBSTRUCTION (CC-D) |
| K0, translation ergodicity | OPEN (§5) | OBSTRUCTION (CC-D) |
| none (stationarity alone), d = 3 | OBSTRUCTION (CC-K); outside §2, recorded as the countercontrol | not examined |

**Generated verdict (PLAN.md §3; all controls green, §9):**
- *On Z^d with 0 < abs(μ) < 1:* "Stationarity and clustering force SMD", with K2 (cumulant
  clustering with uniformly bounded moments of all orders; unconditional, paper proof) and with Kα (strong
  mixing with summable rate and uniformly bounded 2+δ moments, for the distance-indexed α of
  H-αCLT, §3; conditional on H-αCLT). K2 and Kα are not comparable
  as far as checked (§1.2), so both minimal notions are printed. The mechanism gives more than SMD:
  every such state is a centred Gaussian law.
- *On Z^d with 0 < abs(μ) < 1:* no obstruction was found for any notion of §2; K1 and K0 are open
  (§5).
- *At the boundary μ = 0:* "Stationarity and clustering do not force SMD", with K3, the strongest
  notion of §2.
- *Without clustering (d = 3, 0 < abs(μ) < 1):* stationarity with every premise of the fixed set
  does not force SMD (CC-K). This is the Z analogue of unit A's Proposition A.

**What this does not show.** None of L-SDS, K2, Kα or the moment conditions is stated in SM (§8).
The result replaces SMD, an unstated symmetry condition on the state, by unstated conditions on the
state of a different kind: exact stationarity under the same linear map, and summable clustering.
It derives nothing from SM's stated premises, and it is confined to the observer-level linear
offset-free lift on the infinite lattice with 0 < abs(μ) < 1. It says nothing about the Z/q level,
the nonlinear case, μ = 1, or the finite torus T, where unit A's Propositions A and B stand.

## 1. Setting

### 1.1 Notation (unit A §1; lane 2 §4)

- Configuration space X = ((R^6)²)^{Z^d}, points x = (x_n)_n, x_n = (u_n, v_n). A state is a Borel
  probability law ρ on X (product σ-algebra). Its mean m_n = E x_n and second moment
  C(n, m) = E[x_n x_mᵀ] exist under the moment conditions used.
- F = F_s ⊗ I_6, F_s(u, v) = (v, A_s v − u), A_s = (μ/d) Σ_j (T_j + T_j⁻¹): SM:314 at M = μI_6
  with u = φ(t−1), v = φ(t). F is a nearest-neighbour map on X, so F^t is defined on all of X and
  (F^t x)_n depends only on x_m with abs(m − n)_1 ≤ t. L-SDS: F_*ρ = ρ.
- Fourier symbol: a(k) = (2μ/d) Σ_j cos k_j ∈ [−2abs(μ), 2abs(μ)]; F̂_s(k) = [[0, 1], [−1, a(k)]].
  For abs(μ) < 1 its eigenvalues are e^{±iθ(k)}, θ(k) = arccos(a(k)/2) ∈ [θ_−, π − θ_−] with
  θ_− = arccos abs(μ) > 0; θ is real-analytic on T^d, and sin θ(k) ≥ (1 − μ²)^{1/2}.
- J_s: the positive-frequency complex structure, symbol (F̂_s − cos θ)/sin θ ([L2] Theorem 1Z;
  unit A §1). For abs(μ) < 1 the symbol is analytic, so J_s is a convolution with an exponentially
  decaying kernel. R(w) = I ⊗ X + J_s ⊗ Y for w = X + iY ∈ U(6), X and Y real. The internal factor
  carries the real six-link representation of the cubic rotation group O,
  6 = T_1 ⊕ E ⊕ A_1 ([K] `theorem_7`).
- SMD: Stab_{U(6)}(ρ) = Stab_{U(6)}(C), where Stab(ρ) = {w : R(w)_*ρ = ρ} and
  Stab(C) = {w : R(w) C R(w)ᵀ = C} (second moment; as bilinear forms on finitely supported test
  vectors).

### 1.2 Order of the clustering notions (recorded deviation from PLAN.md §2)

PLAN.md §2 lists the notions "from weakest to strongest", to be checked where used. The check gives
a partial order only:
- K3 ⇒ K2 (Lemma K below), K3 ⇒ Kα (α(r) = 0 for r > R), Kα ⇒ K1 ⇒ K0 (for translation-invariant
  states).
- Neither K2 ⇒ Kα nor Kα ⇒ K2 was established; they are treated as incomparable. The verdict
  therefore prints both minimal positive notions (§0).
- **Kα read with the distance-indexed α.** PLAN.md §2 does not fix how the mixing coefficient is
  indexed. The conditional positive (Corollary Pα) covers Kα with α(r) indexed by distance alone,
  over sets of sites of any sizes, as H-αCLT states it (§3); a mixing coefficient restricted by
  set size is not covered.
- **K3 split into its two readings.** PLAN.md §2 defines K3 with "uniformly bounded fourth (or
  all) moments". The report treats the two readings separately: K3 (all moments), for which the
  unconditional positive Corollary P3 holds, and K3′ (fourth moments only), for which the positive
  Corollary P3′ is conditional on [I-Stein]. No other notion was added or redefined.
- **Uniformity of moments.** Theorem P, Lemma M and Lemma G use moment bounds uniform in the site
  (sup_n). PLAN.md §2 states uniform bounds for Kα and K3 but says only "finite moments of all
  orders" for K2, and translation invariance is not in the fixed set. K2 is read here with
  uniformly bounded moments of all orders, as Theorem P states; for translation-invariant states
  the two coincide.
- **Two readings of the μ range (PLAN.md §1, §3, §5).** PLAN.md §1 sets the range abs(μ) < 1 "with
  μ = 0 … treated separately as a boundary case"; §3 defines POSITIVE(K) over "the range of §1";
  §5's S2 states no range. Two readings are recorded, and PLAN.md is left unchanged:
  - *R1 (used for the table and the verdict):* μ = 0 and 0 < abs(μ) < 1 are separate ranges, each
    assigned per notion. POSITIVE(K) is claimed on 0 < abs(μ) < 1 only, and S2 is read on that
    range.
  - *R2:* the range of §1 is all of abs(μ) < 1. Then no notion of §2 is POSITIVE on the whole
    range, since ρ_D gives OBSTRUCTION for every notion at μ = 0; the positive results hold on
    0 < abs(μ) < 1 only. S2 is then met through ρ_D.
  The per-range statements of §0 and §7 are true under both readings; only the labelling of S2 and
  of POSITIVE on the full range differs.

## 2. Theorem P (cumulant clustering forces Gaussianity, hence SMD)

**Theorem P [A].** Let d ≥ 1 and 0 < abs(μ) < 1. Let ρ be a law on X with:
1. **L-SDS:** F_*ρ = ρ;
2. **moments:** sup_n E abs(x_n)^r < ∞ for every r;
3. **K2:** for every r ≥ 3,
   K_r := sup_{n_1} Σ_{n_2,…,n_r} max_{α_1…α_r} abs(κ(x_{n_1 α_1}, …, x_{n_r α_r})) < ∞,
   where κ is the joint cumulant and α_j ∈ {1, …, 12} labels components of x_n.

Then ρ is a centred Gaussian law. Consequently ρ satisfies SMD (Lemma G).

No translation, cubic or J-invariance, no TPC and no H-PF is used. The proof has four steps.

### 2.1 Step 1: finite propagation and stationarity [A]

For a finitely supported test function f : Z^d → R^12 put ⟨f, x⟩ = Σ_n f(n)·x_n. Then
⟨f, F^t x⟩ = ⟨f_t, x⟩ with f_t := (F^t)ᵀ f, finitely supported (its support radius grows by at
most t). By L-SDS, ⟨f, x⟩ and ⟨f_t, x⟩ have the same law for every t ∈ N; in particular
κ_r(⟨f, x⟩) = κ_r(⟨f_t, x⟩) for all r and t.

### 2.2 Step 2: the cumulant bound (Lemma C) [A]

**Lemma C.** For finitely supported g and r ≥ 3,
abs(κ_r(⟨g, x⟩)) ≤ 12^{r/2} K_r ‖g‖_∞^{r−2} ‖g‖_2²,
with abs(g(n)) the Euclidean norm on R^12, ‖g‖_∞ = sup_n abs(g(n)), ‖g‖_2² = Σ_n abs(g(n))².

*Proof.* By multilinearity,
κ_r(⟨g, x⟩) = Σ_{n_1…n_r} Σ_{α} g(n_1)_{α_1} ⋯ g(n_r)_{α_r} κ(x_{n_1α_1}, …, x_{n_rα_r}).
Write abs(g(n))_1 = Σ_α abs(g(n)_α) ≤ √12 abs(g(n)). Then
Π_j abs(g(n_j))_1 ≤ ‖g‖_{∞,1}^{r−2} (abs(g(n_1))_1² + abs(g(n_2))_1²)/2. The term with
abs(g(n_1))_1² sums to at most ‖g‖_{2,1}² K_r / 2. Joint cumulants are symmetric in their
arguments, so the term with abs(g(n_2))_1² obeys the same bound with n_2 as the distinguished
site. Converting the 1-norms costs 12^{(r−2)/2} · 12. ∎

### 2.3 Step 3: spreading under the dispersive map (Lemma S) [A]

**Lemma S.** For 0 < abs(μ) < 1 and finitely supported f:
(a) sup_t ‖f_t‖_2 ≤ B ‖f‖_2 with B = 5/(1 − μ²)^{1/2};
(b) ‖f_t‖_∞ → 0 as t → ∞.

*Proof.* With ĝ(k) = Σ_n g(n) e^{−ik·n}, f̂_t(k) = (F̂(k)ᵀ)^t f̂(k) (a(k) is even, so the symbol
of Fᵀ is F̂(k)ᵀ). F̂_sᵀ has the distinct eigenvalues e^{±iθ}, so
F̂_sᵀ = e^{iθ}P_+ + e^{−iθ}P_−, P_± = ±(F̂_sᵀ − e^{∓iθ})/(2i sin θ), and
f̂_t = e^{itθ}P_+ f̂ + e^{−itθ}P_− f̂ (on the phase-space factor; the internal I_6 is inert).

(a) ‖F̂_sᵀ‖ ≤ (2 + a²)^{1/2} < 3 and sin θ ≥ (1 − μ²)^{1/2} give ‖P_±‖ ≤ 2/(1 − μ²)^{1/2}, so
‖(F̂_sᵀ)^t‖ ≤ B uniformly in k and t; Parseval gives (a).

(b) Each component of f_t is a sum of two terms
h_s(n) = (2π)^{−d} ∫_{T^d} e^{ik·n} e^{isθ(k)} g(k) dk, with s = ±t and g a component of P_± f̂,
real-analytic on T^d. Since ‖h‖_∞ ≤ ‖h‖_4, it suffices that Σ_n abs(h_s(n))^4 → 0. By Parseval
applied to h_s²,
Σ_n abs(h_s(n))^4 = (2π)^{−3d} ∫_{T^{3d}} e^{isΘ(k, k_1, k_2)} G(k, k_1, k_2) dk dk_1 dk_2,
Θ = θ(k_1) + θ(k − k_1) − θ(k_2) − θ(k − k_2), G = g(k_1) g(k − k_1) conj(g(k_2) g(k − k_2)) ∈ L¹.

*Non-degeneracy of Θ.* ∇_{k_1}Θ = ∇θ(k_1) − ∇θ(k − k_1). If it vanished identically, ∇θ would be
constant, hence zero (θ is periodic), so θ, and with it a(k), would be constant: μ = 0. For μ ≠ 0
some partial derivative of Θ is a real-analytic function on the connected torus T^{3d} that is not
identically zero; its zero set is Lebesgue-null (standard fact for real-analytic functions), and
{∇Θ = 0} is contained in it.

*Riemann–Lebesgue through the pushforward.* On the open full-measure set U = {∇Θ ≠ 0}, Θ is a
submersion, so locally Θ is a coordinate function and Θ⁻¹(N) ∩ U is null for every null N ⊂ R
(Fubini in such charts; countably many charts cover U). Hence the complex measure
ν(B) = ∫_{Θ⁻¹(B) ∩ U} G is absolutely continuous on R, ν = ψ ds with ψ ∈ L¹(R), and
∫ e^{isΘ} G = ∫ e^{isy} ψ(y) dy → 0 as abs(s) → ∞ by the classical Riemann–Lebesgue lemma. ∎

*Where μ ≠ 0 is used:* only in the non-degeneracy of Θ. At μ = 0, θ ≡ π/2, F^4 = I, f_t is
4-periodic in t and ‖f_t‖_∞ does not tend to 0. This is the line at which CC-D requires a positive
proof to fail (§4.2; illustrated in `controls-output.txt`, part X, which certifies nothing).

### 2.4 Step 4: Gaussianity and the mean (Lemma M) [A]

For r ≥ 3, Step 1 and Lemmas C and S give
abs(κ_r(⟨f, x⟩)) = abs(κ_r(⟨f_t, x⟩)) ≤ 12^{r/2} K_r B² ‖f‖_2² ‖f_t‖_∞^{r−2} → 0,
so κ_r(⟨f, x⟩) = 0 exactly. All moments of ⟨f, x⟩ therefore coincide with those of the normal law
with the same mean and variance, and the normal law is determined by its moments; so ⟨f, x⟩ is
normal (degenerate if its variance is 0). By the Cramér–Wold device every finite-dimensional
marginal of ρ is jointly Gaussian, and a law on X is determined by its finite-dimensional
marginals. So ρ is Gaussian with mean m and covariance C − mmᵀ.

**Lemma M (the mean vanishes) [A].** m is bounded (moments), and F-stationarity gives Fm = m. A
bounded sequence is a tempered distribution, and in Fourier space (F̂(k) − I) m̂ = 0. Per mode,
det(F̂_s(k) − I) = 2 − a(k) ≥ 2 − 2abs(μ) > 0, so (F̂ − I)⁻¹ has real-analytic entries;
multiplying gives m̂ = 0, so m = 0. (This step holds for every abs(μ) < 1, μ = 0 included.)

### 2.5 Gaussian implies SMD (Lemma G; control CC-G) [A]

**Lemma G.** Let abs(μ) < 1 and let ρ be a centred Gaussian law on X with sup_n E abs(x_n)² < ∞
and covariance C. Then R(w) is defined ρ-almost surely for every w ∈ U(6), and
R(w)_*ρ = ρ if and only if R(w) C R(w)ᵀ = C. Hence Stab(ρ) = Stab(C): SMD holds.

*Proof.*
- *Domain.* J_s has kernel bounded by c e^{−γ abs(n)}. Since Σ_m e^{−γ abs(n − m)} E abs(x_m) < ∞,
  the series (J_s x)_n converges absolutely almost surely, for every n; so R(w)x is defined on a
  full-measure set.
- *The pushforward.* For finitely supported f, ⟨f, R(w)x⟩ = ⟨R(w)ᵀf, x⟩ with R(w)ᵀf exponentially
  decaying; this is the L²(ρ)-limit of finite truncations, hence centred normal with variance
  ⟨R(w)ᵀf, C R(w)ᵀf⟩ (the double sum converges since C is bounded and R(w)ᵀf ∈ ℓ¹). Jointly over
  finitely many f the same holds, so R(w)_*ρ is the centred Gaussian law with covariance form
  f ↦ ⟨f, R(w) C R(w)ᵀ f⟩.
- *Both directions.* Two centred Gaussian laws on X are equal if and only if their covariance
  forms on finitely supported f agree. "If": equal covariance forms give R(w)_*ρ = ρ. "Only if":
  R(w)_*ρ = ρ gives equal second moments. ∎

**Corollary (with TPC).** If, in addition, C = c ⊗ Σ_b κ_b P_b with κ_b pairwise distinct and c
F-invariant and J-Hermitian (the TPC form, reading r2), then Stab(ρ) = U(3)×U(2)×U(1). *Proof:*
identity (★) of §4.1 gives R(w)(c ⊗ S)R(w)ᵀ = c ⊗ S iff wSw† = S, and the unitary commutant of
Σ_b κ_b P_b with distinct values is U(3)×U(2)×U(1). The general TPC form C = Σ_b C_b ⊗ P_b is
[L2] §4.2's scope argument.

## 3. Corollaries for the other notions

**Lemma K (K3 ⇒ K2) [A].** If the σ-algebras of any two sets of sites at distance > R are
independent and sup_n E abs(x_n)^r < ∞ for every r, then K2 holds.
*Proof.* A joint cumulant vanishes when its arguments split into two mutually independent groups.
So κ(x_{n_1α_1}, …, x_{n_rα_r}) = 0 unless {n_1, …, n_r} is connected in the graph joining sites
at distance ≤ R. The number of such r-tuples with n_1 fixed is at most r^{r−2} D^{r−1},
D = (2R + 1)^d (a spanning tree on r labelled vertices with each edge within distance R). Each
cumulant is a polynomial in joint moments of order ≤ r, bounded by Hölder uniformly in the sites.
∎

**Corollary P3 [A].** Theorem P holds with K2 replaced by K3 (all moments).

**Corollary P3′ (conditional on [I-Stein]).** Theorem P holds with K3 and only
sup_n E abs(x_n)^4 < ∞.
- *[I-Stein]* (dependency-neighbourhood normal approximation; Ross, "Fundamentals of Stein's
  method", Probab. Surveys 2011, Theorem 3.5, as recalled): for centred X_1, …, X_N with finite
  fourth moments, σ² = Var Σ X_i > 0, dependency neighbourhoods of size ≤ D and W = Σ X_i/σ,
  d_W(W, Z) ≤ (D²/σ³) Σ E abs(X_i)³ + (√28 D^{3/2}/(√π σ²)) (Σ E X_i⁴)^{1/2}.
- *Use.* X_n = f_t(n)·x_n (m = 0 by Lemma M, which needs only bounded first moments), σ² =
  Var⟨f, x⟩, fixed by Step 1. Σ E abs(X_n)³ ≤ M_3 ‖f_t‖_∞ ‖f_t‖_2² and Σ E X_n⁴ ≤ M_4 ‖f_t‖_∞² ‖f_t‖_2²,
  both → 0 by Lemma S. So ⟨f, x⟩, whose law equals that of ⟨f_t, x⟩, is normal. Cramér–Wold and
  Lemma G conclude.

**Corollary Pα (conditional on H-αCLT).** Theorem P holds with K2 replaced by Kα:
sup_n E abs(x_n)^{2+δ} < ∞ and uniform Rosenblatt mixing α(r) with Σ_r r^{d−1} α(r)^{δ/(2+δ)} < ∞.
- *H-αCLT (a stated hypothesis, not a pinned theorem).* Let α(r) be the uniform strong-mixing
  coefficient indexed by distance alone: the supremum of abs(P(A ∩ B) − P(A)P(B)) over events A, B
  measurable with respect to the variables in two sets of sites, of any sizes, at distance ≥ r.
  H-αCLT states: under sup_n E abs(x_n)^{2+δ} < ∞ and Σ_r r^{d−1} α(r)^{δ/(2+δ)} < ∞, if a_t are
  finitely supported weights with ‖a_t‖_∞ → 0, sup_t ‖a_t‖_2 < ∞ and Var Σ a_t(n)·x_n → σ², then
  Σ a_t(n)·x_n converges in law to N(0, σ²). No specific source theorem is pinned. The Bernstein
  room–corridor argument used by Dudnikova, Komech and Spohn for harmonic crystals (J. Math. Phys.
  44 (2003)) is a candidate source, to be matched, together with its set-size indexing of α, by
  the source check of N3. For d ≥ 2 that indexing decides which theorem applies; mixing
  coefficients restricted by set size would need a different statement. Corollary Pα is
  conditional on H-αCLT as stated here.
- *Use.* As for P3′, with Lemma S supplying the weights. This route uses from the dynamics only
  Lemma S (non-constant θ, uniform gap of e^{±iθ} from ±1). The stronger dispersion conditions of
  the continuous-time literature (conditions on the Hessian of the dispersion relation) serve
  convergence from non-stationary initial states; the stationary question does not need them
  (§6, item 1).

## 4. Witnesses and countercontrols

The internal identities below are certified by exact rational arithmetic in `controls.py`
(checks E8–E18, negative control N5). The spatial ones (F-invariance, J-Hermiticity, positivity, cubic and translation
invariance, finite range) are spot-checked exactly (E1–E7) on small tori (d = 1, L = 5, 6;
d = 2, L = 4; d = 3, L = 3; μ = 1/3, −3/5, 1/3, 1/2), with the negative controls E4 and N1–N4 at each size.
The torus checks spot-check identities proved here in general by symbol calculus; they do not
replace the proofs.

### 4.1 CC-N (non-vacuity): a finite-range Gaussian condensate state on Z

Let c be the operator on the phase-space factor with symbol [[1, a/2], [a/2, 1]], i.e.
c_uu = c_vv = 1, c_uv = c_vu = A_s/2 (range 1). Let C_0 = c ⊗ S_0, S_0 = Σ_b κ_b P_b, κ_b pairwise
distinct and positive, and ρ_0 the centred Gaussian law with covariance C_0.

**Facts [A], spot-checked exactly [C].**
- c = det(Ĝ) Ĝ⁻¹ for the conserved form Ĝ = [[1, −a/2], [−a/2, 1]] of F_s
  (Q(u, v) = abs(u)² + abs(v)² − u·A_s v, the conserved energy of SM:296), with det Ĝ = 1 − a²/4 a
  function of A_s. Hence F c Fᵀ = c (E1).
- D_s c D_sᵀ = (1 − A_s²/4) c, i.e. J_s c J_sᵀ = c: C_0 is J-Hermitian (E2).
- c is positive definite: its symbol has eigenvalues 1 ± a/2 ≥ 1 − abs(μ) > 0 (E3).
- c is translation-invariant, invariant under the hyperoctahedral site action, and of range 1
  (E5–E7). A Gaussian law with range-1 covariance is finite-range dependent (R = 1), so ρ_0 meets
  K3 with all moments, hence K2, Kα, K1 and K0.

**Identity (★) [A].** For any real symmetric internal S and w = X + iY,
R(w)(c ⊗ S)R(w)ᵀ = c ⊗ (XSXᵀ + YSYᵀ) + J_s c ⊗ (YSXᵀ − XSYᵀ),
using J_s c J_sᵀ = c and hence c J_sᵀ = −J_s c. The right side equals c ⊗ S if and only if
wSw† = S: c (symmetric, positive) and J_s c (antisymmetric, nonzero) are linearly independent, and
wSw† = XSXᵀ + YSYᵀ + i(YSXᵀ − XSYᵀ).

So the positive results are not vacuous: they apply to a state realizing Theorem 5's conclusion
with distinct block values (CC-W table in §4.4).

**Consequence for unit A's Proposition B.** ρ_0 is translation-mixing, hence ergodic for the group
generated by F and the translations, and extremal among laws invariant under that group and O; the
identity component of its stabilizer is U(3)×U(2)×U(1), and its block values are distinct. So the
conclusion of unit A's Proposition B, proved on T, fails on Z: on Z an extremal (indeed
finite-range dependent) state realizes Theorem 5's conclusion. Proposition B's obstruction belongs
to the finite torus, where the closure of the dynamics is compact and ergodic laws are orbit
measures.

### 4.2 CC-D (dispersion is load-bearing): μ = 0

At μ = 0: A_s = 0, F_s(u, v) = (v, −u), and J_s = F_s (site-local; s_L = 1). With
Φ_n = u_n − iv_n one has Φ_n(Fx) = iΦ_n(x), and R(w) acts site by site as Φ_n ↦ wΦ_n.

**Witness ρ_D.** Sites i.i.d.; at each site, independent blocks, with K, K′, K″ uniform on
{0, 1, 2, 3}, j, j′ uniform on {1, 2, 3}, all independent:
- Φ_{T_1} = (3κ_T)^{1/2} i^K ô_j, with ô_j the orthonormal odd link combinations (a T_1 basis on
  which O acts by signed permutations);
- Φ_E = (2κ_E)^{1/2} i^{K′} ε̂_{j′}, with ε̂_j the three unit vectors at 120° obtained from the even
  combinations s_j minus their mean (O permutes them);
- Φ_{A_1} = κ_A^{1/2} i^{K″} â, with â = (1, …, 1)/√6 the unit vector spanning A_1.

**Checks [A], [C].**
- E[ΦΦ†] = κ_T P_T1 + κ_E P_E + κ_A P_A1, from Σ_j ô_jô_jᵀ = P_T1 and Σ_j ε̂_jε̂_jᵀ = (3/2)P_E
  (E17, unnormalized form); E[ΦΦᵀ] = 0 since E[i^{2K}] = 0. So the site second moment is
  (1/2) I_2 ⊗ S_0, J-Hermitian, of TPC form.
- Invariance under Φ ↦ iΦ (K ↦ K + 1), hence L-SDS. O-invariance: the supports are ρ(g)-invariant
  (E18) and sites are i.i.d.; translation-invariant.
- i.i.d. sites with bounded support: K3 with R = 0 and all moments; hence K2, Kα, K1, K0.
- **SMD fails.** R(w)_*ρ_D = ρ_D forces w to preserve the finite single-site support. The identity
  component of Stab(ρ_D) acts trivially on that finite set, so it fixes each support point; the
  T_1 phase e^{iφ P_T1} moves i^K ô_j unless e^{iφ} = 1. So the T_1 phase circle, which lies in
  Stab(C) = U(3)×U(2)×U(1), is not contained in Stab(ρ_D) (a circle in Stab(ρ_D) would lie in its
  identity component). With Stab(ρ_D) ⊆ Stab(C), Stab(ρ_D) ⊊ Stab(C).

**Line of the positive proof that fails at μ = 0:** only Lemma S(b) (non-degeneracy of Θ). Step 1
and Lemmas C, M and G hold at μ = 0. The positive proof therefore does not prove too much.

### 4.3 CC-K (clustering is load-bearing): an O-orbit mixture on Z^3

Let d = 3, 0 < abs(μ) < 1, c as in §4.1, B = t eᵀ + e tᵀ with t ∈ T_1, e ∈ E nonzero real vectors
(E11), and S = S_0 + εB with ε > 0 small enough that S > 0. The argument below needs only t ≠ 0 and
e ≠ 0. The controls use the unnormalised vectors t = |+e_1⟩ − |−e_1⟩ (abs(t)² = 2) and
e = s_1 − s_2 (abs(e)² = 4) in the link basis (E11), and E15 checks S > 0 for κ = (1, 2, 3) and
ε = 1/10 with that B. For
h ∈ O put S_h = ρ(h)Sρ(h)ᵀ. Let ρ_K be the equal-weight mixture over h ∈ O of the centred
Gaussian laws N(0, c ⊗ S_h) (equal components merged; exactly 12 distinct S_h for the vectors of the controls, E14; at least two for any nonzero t, e).

**Checks [A], [C].**
- Each component is F-stationary (E1), J-Hermitian (E2), translation-invariant and of range 1.
- O acts on X by (g·x)_n = ρ(g)x_{g⁻¹n}; c is invariant under the site action (E5), so g maps
  component h to component gh: ρ_K is O-invariant.
- Second moment: c ⊗ (1/24)Σ_h S_h = c ⊗ S_0, because Σ_h ρ(h)Bρ(h)ᵀ = 0 (E12; Hom_O(T_1, E) = 0).
  So TPC (r2) and distinct on-site values hold, and Stab(C) = U(3)×U(2)×U(1) by (★).
- **No clustering.** Each component is ergodic (range-1 Gaussian). Under component h the empirical
  average of u_n u_nᵀ over growing boxes converges almost surely to S_h. This translation-invariant
  function takes at least two values with positive probability, so ρ_K is not ergodic: K0 fails,
  hence K1, Kα and K3. K2 fails directly: for sites 0 and n at distance > 1, the joint cumulant
  κ(u_{0α}, u_{0β}, u_{nα}, u_{nβ}) equals Var_h((S_h)_{αβ}), which does not decay in n and is
  positive for an entry on which the S_h differ.
- **SMD fails [A].** Finite mixtures of centred Gaussian laws with distinct covariances are
  identifiable: on a finite set of sites on which the distinct covariances restrict to distinct
  quadratic forms q_h, an equality Σ_h p_h e^{−q_h(f)/2} = Σ_h p′_h e^{−q′_h(f)/2} for all f,
  evaluated along s f_0 with f_0 off finitely many proper quadrics and using the linear
  independence of e^{−λs²} for distinct λ, matches the components on an open set of f_0, hence as
  polynomials. So R(w) ∈ Stab(ρ_K) if and only if R(w) permutes the components (R(w) invertible
  keeps them distinct). The identity component of Stab(ρ_K) acts trivially on this finite set, so
  by (★) it satisfies wSw† = S. For w_φ = e^{iφP_T1}, w_φBw_φ† = e^{iφ} t eᵀ + e^{−iφ} e tᵀ ≠ B unless
  e^{iφ} = 1 (E13), while w_φ commutes with S_0. So the T_1 phase circle lies in Stab(C) and is not
  contained in Stab(ρ_K). Since every symmetry of a law preserves its second moment,
  Stab(ρ_K) ⊆ Stab(C) always; hence Stab(ρ_K) ⊊ Stab(C).

ρ_K meets L-SDS and every premise of the fixed set and violates SMD, on Z^3. It is the Z analogue of
unit A's Proposition A (built here from finite-range components and an O-orbit rather than from
Counterexample 9's mode-pair term), and it shows that the clustering hypothesis of Theorem P cannot
be dropped.

### 4.4 CC-W (witness check)

| Item | ρ_0 (§4.1) | ρ_D (§4.2, μ = 0) | ρ_K (§4.3, d = 3) |
| --- | --- | --- | --- |
| H-link, m = 1; carrier T_1 ⊕ E ⊕ A_1 | ✓ | ✓ | ✓ |
| H-cust kinetic clause (F commutes with every R(w); unit A Lemma 1) | ✓ | ✓ (F = R(i)) | ✓ |
| O-equivariant Σ_n with distinct values | ✓ (2S_0, [L2] Prop. 8) | ✓ (S_0) | ✓ (2S_0) |
| linear offset-free branch; mean 0 | ✓ | ✓ | ✓ |
| H-PF (φ := Φ, as the fixed set requires) | ✓ | ✓ | ✓ |
| TPC (r2): full second moment Σ_b C_b ⊗ P_b | ✓ | ✓ | ✓ |
| J-Hermitian second moment | ✓ (E2) | ✓ | ✓ (E2) |
| translation invariance; O-invariance | ✓ (E5, E6) | ✓ (E18) | ✓ (E5, E12) |
| L-SDS | ✓ (E1) | ✓ | ✓ (E1) |
| K3 / K2 / Kα / K1 / K0 | ✓ / ✓ / ✓ / ✓ / ✓ | ✓ / ✓ / ✓ / ✓ / ✓ | ✗ / ✗ / ✗ / ✗ / ✗ |
| SMD | ✓ (Lemma G) | ✗ | ✗ |

## 5. K1 and K0: open

**Positive route.** Steps 1, 3 and 4 hold under K1 with finite moments; Step 2 (Lemma C) is the
only step that uses summability. Without a summability or rate condition, smallness of ‖f_t‖_∞ does
not by itself give normality of weighted sums: strictly stationary strongly mixing sequences with
finite variance whose partial sums are not asymptotically normal are known (recalled, not used).
The extra constraint here, exact invariance of the law under F for all t, is not exploited by any
argument found.

**Obstruction routes tried, none successful.**
1. *Mixtures* are not ergodic when their components are distinct ergodic laws (§4.3), so they
   cannot witness K0 or K1.
2. *Singular spectrum on a level set.* For a field whose spectral measure is carried by
   {θ = θ_0} (d ≥ 2), F acts as the fixed rotation R(e^{iθ_0}), so stationarity reduces to
   invariance under that phase. A non-Gaussian, phase-invariant, translation-mixing field with that
   spectral support is needed. Harmonizable infinitely divisible fields ∫ e^{ik·n} M(dk) with M
   carried by the level set are the natural candidates; their Lévy measure is carried by plane
   waves, whose modulus does not decay, so by the Lévy-measure criterion for mixing of infinitely
   divisible processes (Rosiński and Żak, as recalled [I]) they are not mixing. Not pursued
   further.
3. *Equivariant nonlinear factors of a Gaussian state.* A translation- and F-equivariant cubic map
   needs a kernel carried by the four-wave resonance set
   θ(k_1) + θ(k_2) = θ(k_3) + θ(k_1 + k_2 − k_3), a null set; with a non-singular input spectrum
   the output variance diverges, and the trivial resonances reduce, by the law of large numbers in
   a mixing state, to linear maps. No construction was found.

**Precise gap.** Whether there exists a law on X, with 0 < abs(μ) < 1, that is F-invariant,
translation-mixing (or only ergodic), with finite moments, and not Gaussian; and if so, whether one
exists that also meets the fixed set and violates SMD. Any such law violates K2 (Theorem P) and,
conditionally on H-αCLT, Kα.

## 6. Premise audit of the infinite-lattice route (the successor assessment's request)

| # | Hypothesis | Where used | Status | Load-bearing? |
| --- | --- | --- | --- | --- |
| 1 | Dispersion: θ non-constant (μ ≠ 0) | Lemma S(b) | proved for μ ≠ 0 (§2.3) | yes: CC-D (μ = 0). Only non-constancy is used; no Hessian condition |
| 2 | Uniform gap from ±1: abs(μ) < 1 | Lemma S(a) (bounded P_±); Lemma M (2 − a > 0); Lemma G (exponential J_s kernel) | branch range, stated (SM:322; unit A §1) | not tested at μ = 1; open node N2 |
| 3 | Exact stationarity under the same F for all t (L-SDS) | Step 1 | not stated in SM (unit A, O2) | yes: without it nothing ties the law to the dynamics; [L2] Counterexample 10 shows that dressing already breaks the J-Hermiticity step |
| 4 | Finite propagation (nearest-neighbour F) | Step 1: f_t finitely supported | stated (SM:314) | convenience; an exponentially local update would need a convergence argument |
| 5 | Linear, offset-free update | Step 1 (linearity of ⟨f, F^t x⟩); Lemma M | stated branch premise (SM:312–316) | with an offset the mean is x* ≠ 0, Stab(ρ) = Stab(C − x*x*ᵀ) ∩ Stab(x*) for a Gaussian law, and the second-moment form of SMD is a different condition; not pursued (outside the fixed set) |
| 6 | Clustering: K2 (or Kα, conditional) | Lemma C | not stated in SM (grep "cluster" in papers/SM.md at [P]: no relevant hit) | yes: CC-K |
| 7 | Moments: all orders (K2, K3), fourth (P3′), 2+δ (Pα) | Lemma C; imports | not stated | the weaker forms are conditional on imports |
| 8 | The state lives on configuration space X, not on ℓ²(Z^d) or K | throughout; Lemma G's domain of R(w) | [L2]'s Z carriers (ℓ², H_E, K) are one-particle spaces; a translation-invariant state is not carried by them | R(w) is defined ρ-a.s. through J_s's exponential kernel when abs(μ) < 1; at μ = 1, J is unbounded on ℓ² ([L2] Proposition 6) and this step is open |
| 9 | Translation, cubic and J-invariance; TPC; H-PF | not used by Theorem P | — | TPC and distinct values are used only to identify Stab(C) |

## 7. Decision rule applied (PLAN.md §3)

- POSITIVE(K2): Theorem P, [A]; CC-N green (ρ_0), CC-E green. POSITIVE(K3): Corollary P3.
- POSITIVE(K3′), POSITIVE(Kα): conditional positives, on [I-Stein] and H-αCLT respectively.
- OBSTRUCTION: none found on 0 < abs(μ) < 1 for any notion of §2. At μ = 0, OBSTRUCTION(K3) by ρ_D, hence
  for every notion of §2 that K3 implies (K3′, K2, Kα, K1, K0).
- OPEN(K1), OPEN(K0) on 0 < abs(μ) < 1, with the gap of §5.
- No positive and obstruction for the same notion on the same range of μ.
- The verdict sentences of §0 are generated from this list.

## 8. Consequences, stated with conditions

**For #1217.** In unit A's ledger, step P2d ("Stab(state) = Stab(C)") is classified U, Dv given
SMD. On Z^d with 0 < abs(μ) < 1 on the linear offset-free branch, P2d is Dv given L-SDS and K2 (or
K3; or, conditionally, Kα), by Theorem P and Lemma G. SMD is thereby not derived from SM's stated
premises: L-SDS and the clustering and moment conditions are not stated in SM (unit A O2; §6,
items 3, 6, 7). Whether to state any of them is an owner decision (§A.29, §A.50 item 6); this
report proposes nothing. With TPC (r2) and distinct values, the stabilizer is then exactly
U(3)×U(2)×U(1) (Corollary of Lemma G). The number of unstated state conditions for layer Φ on Z is
unchanged (SMD is traded for a clustering condition); the clustering condition has an explicit
failure mode (non-summable truncated correlations, §4.3), and ρ_0 shows it compatible with
Theorem 5's conclusion.

**For #1049.** No bearing on the b = 0 dependence beyond §6 item 5: the positive result needs the
offset-free branch through Lemma M and through SMD's second-moment form.

**For unit A's O3.** O3 asked whether spatial clustering plus stationarity under the linear F
implies SMD on Z. On 0 < abs(μ) < 1: yes for K2 and K3; conditionally for Kα and K3′; open for K1
and K0; no without clustering. Unit A's Proposition B does not transfer to Z (§4.1).

## 9. Controls

| Control | Result | Status |
| --- | --- | --- |
| CC-N | ρ_0 meets K3 (hence K2, Kα), L-SDS and the fixed set, with distinct values (§4.1, §4.4) | green |
| CC-K | ρ_K meets L-SDS and the fixed set, fails every notion of §2, violates SMD (§4.3, §4.4) | green |
| CC-D | ρ_D at μ = 0 meets K3, L-SDS and the fixed set and violates SMD; the positive proof fails only at Lemma S(b) (§4.2) | green |
| CC-G | Lemma G re-derives SMD for centred Gaussian states, both directions, with the a.s. domain of R(w) | green |
| CC-E | `python3 -I controls.py`: exact checks E1–E18 and negative controls N1–N5 (56 PASS lines: 4 tori × 11, plus E8–E18 and N5); exit status 0. Negative controls: E4 (identity covariance fails E1); N1 (off-diagonal weight A/3 fails E1 and E2); N2 ([[1, 3A], [3A, 1]] fails E3); N3 (a one-site bump fails E5 and E6); N4 ([[1, A²], [A², 1]] fails E7); N5 (ε = 10 fails E15) | green |
| CC-X | part X of `controls-output.txt`: ‖f_t‖_∞ and ‖f_t‖_4 decrease for μ = 0.5, 0.9 (d = 1, 2) and stay at 1 for μ = 0; ‖f_t‖_2 stays bounded. Illustration only | n/a (certifies nothing) |
| CC-W | itemized table §4.4 for ρ_0, ρ_D and ρ_K | green |
| CC-P | quoted lines re-read at [P] | green |

**Reproduction recipe.** At the commit adding this report, run `python3 -I controls.py` in this
directory (Python ≥ 3.8; NumPy only for part X). Expected: every exact line `PASS`, final line
`EXACT CHECKS: ALL PASS`, exit status 0. The recorded output is `controls-output.txt`. Part X is
floating point and not part of the expected result.

**Pressure test of the favourable branch (§A.31).** Theorem P was tested against μ = 0 (it fails
at the identified line only), a non-clustering state (ρ_K, excluded exactly by K2), a nonzero mean
(excluded on the branch by Lemma M; with an offset, outside the fixed set, §6 item 5), and against
proving too much (it does not apply at μ = 0, without clustering, or at μ = 1). Its non-vacuity is
ρ_0. What it does not show is stated in §0.

## 10. Productivity verdict (PLAN.md §5)

**Met through S1 and S3.**
- S1: POSITIVE(K2) with CC-N, CC-D and CC-E green.
- S3: the premise audit of §6 identifies the load-bearing hypotheses, with countercontrols for
  dispersion (CC-D) and clustering (CC-K), and records that the route needs only non-constancy of
  the dispersion relation, not Hessian conditions.
- S2: not met under reading R1 of §1.2 (no obstruction found under K1 or stronger on
  0 < abs(μ) < 1). Under reading R2 it is met through the μ = 0 obstruction ρ_D, which meets K3 and
  hence K1; that obstruction lies at the uncoupled boundary point, and CC-D requires it in any case.

| Class | Findings |
| --- | --- |
| NEW | Theorem P (K2 clustering and exact stationarity under the dispersive linear lift give a centred Gaussian law, hence SMD, on Z^d, 0 < abs(μ) < 1); ρ_0 and the failure of unit A's Proposition B on Z (§4.1); ρ_K, the Z analogue of Proposition A (§4.3) |
| POSITIVE | Lemma G (SMD for Gaussian states, with the a.s. domain of R(w)); the audit result that only non-constancy of θ is used |
| ELABORATING | Corollaries P3, P3′, Pα; CC-D; the K1/K0 routes of §5 |
| CONFIRMING | unit A's CC3; [L2] Proposition 7's J-Hermiticity, met by ρ_0 |

## 11. Open nodes

- **N1 (K1, K0).** The gap of §5.
- **N2 (μ = 1).** At the massless point the zero mode makes P_± unbounded near k = 0 (Lemma S(a)
  fails), the mean argument loses 2 − a > 0 at k = 0, and J is unbounded ([L2] Proposition 6);
  depends on unit C's H-ZM / H-top. Not pursued.
- **N3 (imports).** [I-Stein] is recalled, not re-checked against its source; Corollary P3′ is
  conditional on it. H-αCLT is a stated hypothesis with no pinned source theorem; Corollary Pα is
  conditional on it until a specific theorem, with its indexing of α, is matched to it.
- **N4 (offset).** The b ≠ 0 case (§6 item 5) is outside the fixed set.
- **N5 (source of K2 and L-SDS).** Whether the observer-level law obtained from the substratum by
  trace-out is exactly stationary under F and K2-clustering is not addressed. SM:290 and SM:298
  record the stationary law of the realized dynamics as open.
- **N6 (T).** On the finite torus, a uniform-in-L clustering notion for families of states, and its
  relation to unit A's Propositions A and B, is not formulated.

## 12. Findings for routing (listed, not edited)

1. **Unit A REPORT-r3 §2 (row P2d) and §9 (O3); unit A PRESERVATION.md §2–§3.** On Z,
   0 < abs(μ) < 1, P2d is derived given L-SDS and K2 (Theorem P); Proposition B's statement fails
   on Z (§4.1); a Proposition A analogue holds on Z without clustering (§4.3). A mutable record
   citing unit A could carry this after review. Route: #1217.
2. **SM:340–344.** The state step of Theorem 5's physical reading can be conditioned on
   stationarity under the same linear map plus summable clustering instead of an unnamed symmetry
   condition on the state. Recorded only; no wording proposed. Route: #1217.
3. **SM:290 (Gaussian limit).** For the observer-level real linear lift on Z^d with
   0 < abs(μ) < 1, every exactly stationary K2-clustering law is Gaussian (Theorem P). This bears on
   the Gaussian-limit part of SM:290's open obligation only for that lift, not for the realized Z/q
   map or the rounded rule. Route: #1217, for the owner to judge relevance.

## 13. Off-`main` references (§A.42 item 8)

| Reference | Classification |
| --- | --- |
| #1169 comments 7200549806, 7199704501 (authority), 7191949320 (successor assessment) | provenance: authority and planning records quoted with author and time; no result uses them |
| commit `6a0a1165` (PLAN.md) and the commit adding this report | support on `main` only once merged without squash (the plan-before-report order is part of the record); not before |
| unit A's record (`../theorem5-premise-ledger-20261126/`), lane 2's record (`../complex-carrier-20261126/`) | support on `main` at [P] |
| kernel `theorem_7` | support on `main`; statement read, not built |
| [I-Stein], Rosiński–Żak; the candidate source of H-αCLT (Dudnikova, Komech and Spohn) | external literature, recalled; Corollary P3′ is conditional on [I-Stein]; Corollary Pα is conditional on the stated hypothesis H-αCLT, not on a pinned source; Rosiński–Żak is used only in an unsuccessful route (§5) |
| #1049, #1217 | provenance: accountability and routing |

Support off `main`: none.

## 14. Verification status and remediation (§A.46 item 4)

**This table authorizes no work.**

| Claim | Status | Missing | Issue | What would resolve it |
| --- | --- | --- | --- | --- |
| Theorem P; Lemmas C, S, M, G, K | unreviewed paper proof | independent review; a non-model check of Lemma S(b) (the pushforward Riemann–Lebesgue step and the analytic non-degeneracy) | #1217 | a recorded review; optionally a Lean formalization of Lemmas C and S |
| Corollaries P3′, Pα | conditional on [I-Stein] and on the stated hypothesis H-αCLT | a check of [I-Stein] against its source; a specific source theorem for H-αCLT | #1217 | a recorded source check; a pinned theorem or a proof of H-αCLT |
| Witnesses ρ_0, ρ_D, ρ_K | unreviewed; identities exact-checked on small tori [C] | review of the general symbol-calculus proofs and of the identifiability step | #1217 | a recorded review |
| §5 (K1, K0) | open | a proof or a counterexample | #1217 | either |
| §6 audit | unreviewed | review | #1217 | a recorded review |

## 15. Node log

- **Pass 1.** Setting; Lemma G (CC-G); ρ_0 (CC-N) by the adj(Ĝ) device; identity (★).
- **Pass 2.** Theorem P: Step 1 (finite propagation), Lemma S by the ℓ⁴ and pushforward
  Riemann–Lebesgue argument, Lemma C, Lemma M; the μ ≠ 0 line identified.
- **Pass 3.** Countercontrols ρ_D (μ = 0) and ρ_K (O-orbit mixture); identifiability; Proposition B
  on Z.
- **Pass 4.** Corollaries P3, P3′, Pα; partial order of the notions (§1.2); K1/K0 routes (§5). No
  NEW finding.
- **Pass 5.** Premise audit (§6) and exact controls (`controls.py`). No NEW finding.
- **Pass 6.** §A.34 re-check: Lemma G's equivalence, both directions; (★)'s "if and only if", both
  directions; identifiability, both directions. Claim/evidence re-check of §0 and §8. No NEW
  finding.

**Stopping (PLAN.md §6).** The first condition holds: every notion of §2 is assigned (POSITIVE,
conditional POSITIVE, OBSTRUCTION at μ = 0, or OPEN with the gap of §5), and the controls have run.
Passes 4–6 are also three consecutive passes with no NEW finding. No result needed a premise
outside the fixed set and the notion under test.
