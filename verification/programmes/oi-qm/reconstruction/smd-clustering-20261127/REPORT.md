# SMD-CL-1: sourcing the clustering of Theorem P; K1 and K0 (#1049, #1217). Report

**Revision r2.** Applies findings F1–F11 of the independent review of r1 at `22347bb9` (#1623
comment 7209241804). No r1 result changes; one derivation added (S-2′, for F4); r1 is the earlier state of this file in the
branch history.

**WIP / UNVERIFIED. Model-written research record, paper-only. Nothing here is adopted, proposed
for the manuscripts or authorized beyond the unit's scope. Pending independent non-author review
(PLAN.md §6).**

- **Plan:** PLAN.md in this directory, commit `98172765ce183501d3f9762906a0d1db7ed913ac`, committed
  alone before this report.
- **Authorization and Goal link:** as in PLAN.md (owner decision `amaybaum`, #1169 comment
  7208939261, created 2026-11-27T03:22:49Z, unit 3; work package WP-2).
- **Pinned main commit [P]:** `13c05b4fe666c2e128eed1213874be9b8208982d`. Quoted lines re-read at
  [P]: Main:54, Main:58, Main:60, Main:736; SM:130, SM:226, SM:232, SM:290–296, SM:312–316,
  SM:1225.
- **Evidence layer of every result:** mathematical derivation on paper ([A]) or reasoning ([W]),
  using standard textbook facts named where used. No computation was run; no identity here needed
  one (CC-E vacuous, §7). [S] marks results of SMD-SRC-1's REPORT.md, [U-A] of unit A's REPORT-r3,
  [L2] of lane 2's REPORT-r2.

## 0. Outcome

| Question | Assignment (PLAN.md §2) |
| --- | --- |
| Q1, selected counting measure (Main Lemma 3, posit (iv)) | NOT SOURCED (obstruction), conditional on the bridge reading (B) and Proposition 4b's hypotheses (H): the missing property is distinct block values, not clustering (§1.2) |
| Q1, uniform invariant ensemble on an energy shell (SM:292, SM:1225) | NOT SOURCED under (H′), Proposition 4b's hypotheses with the shell law in place of the counting measure, for the same missing property (§1.2) |
| Q1, record-selected orbit measure or prepared hidden prior μ_H (Main:58, Main:60) | REDUCED: Main and SM supply no derivation of its stationary law or clustering (SM:290, SM:298, SM:1225) |
| Q2, K1 on 0 < abs(μ) < 1 | OPEN, with a sharpened gap (§3) |
| Q3, K0 on 0 < abs(μ) < 1 | OBSTRUCTION: witness ρ_Q, every d ≥ 1, every 0 < abs(μ) < 1 (§2) |
| Q4, [I-Stein] | re-derived (§4); Corollary P3′ of SMD-SRC-1 then rests only on textbook Stein-equation bounds |
| Q4, H-αCLT | unchanged: no source read (no external access); stays a stated hypothesis |

**Generated verdict (controls green; CC-E vacuous: no computation; §7):**
- *Q1:* under (B) and (H), the selected measure supplies no state that meets the fixed set. Its
  observer image is a single mixing phase (and K3 when the observer map Π has finite range), with
  scalar Σ (unit A's Proposition C), so the condensate is neither that image nor a
  translation-ergodic component of it. What is missing is distinct block values, not clustering.
  The energy-shell ensemble is excluded under (H′) for the same reason. For a prepared prior
  or a record-selected orbit, Main and SM supply no derivation of a stationary, clustering observer
  law (SM:290, SM:298, SM:1225). Clustering of the condensate state therefore remains a condition on
  the state; it is not adopted.
- *Q3:* "Stationarity and clustering do not force SMD" holds with K0 on 0 < abs(μ) < 1: a
  translation-ergodic, F-stationary state meeting every premise of the fixed set has stabilizer
  U(3)×U(2)×Z_4 ⊊ U(3)×U(2)×U(1) = Stab(C).
- *Q2:* K1 is open. Any K1 witness must have continuous covariance spectrum, violate K2, and carry
  a non-summable joint cumulant of order ≥ 3 supported on a resonance set of the dispersion (§3).

**What this does not show.** Q1's obstruction is conditional on (B), a reading of the unproved
coarse-graining bridge (SM:232), and on (H), which is load-bearing for it (§7); it says nothing
about states prepared outside the selected measure. Lemma N is a finite-time statement; whether
the conserved averages or the clustering properties survive t → ∞ limits is not shown. Q3's witness is not O-invariant as a law (the fixed set does not require it);
an O-invariant K0 witness is not constructed (N3). No manuscript or premise status changes.

## 1. Q1: sourcing the clustering

### 1.1 What Main and SM specify

- The bijective substratum is a finite representative (Main:60; posit (ii), an open hypothesis),
  with the second-order update x(t+1) = F(x(t)) − x(t−1) over a finite abelian group (posit (xiii);
  linear, posit (vii)); on a finite set it has finite order, φ^L = id (Main:60), and for the exact
  linear rule mod p explicitly F^{p(p^{2m}−1)} = I (SM:296).
- The selected measure is the counting measure, uniform on the product carrier, chosen as the
  maximal-entropy invariant measure (Lemma 3, Main:54; posit (iv)); a realization may instead carry
  its own hidden prior μ_H as a realization datum (Main:58), and on a finite representative the
  selection "among orbits is fixed by maximal entropy compatible with the observer's records"
  (Main:60).
- The observer-level real update of SM:314 "is not identified with the fundamental bijection …
  without the coarse-graining bridge of §4.1" (SM:316), and that bridge "is not proved anywhere in
  this framework" (SM:232). The stationary law of the realized scalar dynamics is open (SM:290,
  SM:298, SM:1225).
- At M = μI the substratum dynamics, the threshold and the selected measure commute with the signed
  permutations of the six components (SM:130), whence the observer image of the selected measure
  has Σ_n = c·I_6 (unit A Proposition C [U-A], under Proposition 4b's hypotheses).

### 1.2 Results

**S-1 (what the selected measure supplies) [A].** On the lattice model the carrier is
((Z/q)²)^{sites}, and the uniform probability on it is the product of uniform site laws: sites are
independent, i.e. K3 with R = 0 and all moments bounded, at the substratum level, on every finite
torus. It is invariant under every bijection of the carrier, hence under the exact rule. The
infinite-volume version, the product Haar probability on ((Z/q)²)^{Z^d}, is invariant under the
infinite-volume second-order rule, a continuous group automorphism with inverse
(u′, v′) ↦ (Au′ − v′, u′). At the observer level, under (B), its image is translation-mixing for
any Π (S-2), and K3 when Π has finite range (a finite-range factor of an independent field is
finite-range dependent). This is CC-S's required statement of what is supplied: clustering is
available; distinct block values are not (S-2).

**S-2 (the selected measure cannot be the condensate state, nor a component of it) [A],
conditional on:**
- **(B)** the observer-level configuration is the image of the infinite-volume substratum
  configuration under a measurable, translation-equivariant map Π (the form a coarse-graining bridge
  takes; the bridge itself is unproved, SM:232), and
- **(H)** Proposition 4b's hypotheses, under which the observer image is invariant under the signed
  permutations B_6 (SM:130; unit A Proposition C).

*Statement.* Under (B) and (H), the observer image ρ_sel = Π_*(Haar) is translation-mixing, has
Σ_n = c·I_6, and is not a nontrivial mixture of translation-invariant laws. Hence no
translation-invariant state with distinct block values is ρ_sel or an ergodic component of it.

*Proof.* The product measure is a Bernoulli action of Z^d by translations, hence mixing; a factor
of a mixing action is mixing (correlations of Π-pulled-back observables are correlations of the
Bernoulli action). So ρ_sel is mixing, hence ergodic, hence extremal among translation-invariant
laws: it has no nontrivial decomposition into translation-invariant laws, in particular none into
broken (non-B_6-symmetric) ergodic components. Its Σ is scalar by (H). ∎

So the spontaneous-breaking reading of the condensate (SM:136: "spontaneous breaking of a
dynamical symmetry by that condensate") cannot be realized by decomposing the selected measure's
observer image: that image is already a single mixing phase, and it is symmetric.

The new content of S-2 beyond unit A's Proposition C (scalar Σ, row H5) is the extremality step:
the condensate is not an ergodic component of the selected image.

**S-2′ (the energy-shell ensemble) [A], conditional on (H′).** (H′) is Proposition 4b's
hypotheses with the shell law in place of the counting measure. (B) is not used: the shell is a
finite object, and S-2′ concerns its observer image on the finite representative. SM:292 and SM:1225 name a
further candidate invariant law: the uniform ensemble on an invariant finite energy shell. At
M = μI the conserved E of SM:296 is a sum over the six decoupled components and is invariant under
their signed permutations B_6, so the shell and its uniform law are B_6-invariant; under (H) the
argument of unit A's Proposition C gives scalar Σ for its observer image, and distinct block values
fail. Its extremality is a separate question (the shell law is not a product measure) and is not
needed for the assignment: NOT SOURCED under (H′).

**S-3 (no Gaussianization at the substratum level) [A].** On every finite representative the exact
rule has finite order L. For any finitely supported linear functional f of the Z/q-valued
configuration, f∘F^t is L-periodic in t, so the spreading step of Theorem P (Lemma S [S]) has no
substratum counterpart, and any orbit-uniform law is stationary. This is the substratum analogue of
SMD-SRC-1's countercontrol ρ_D at μ = 0 [S]: stationarity under a finite-order map imposes no
Gaussianity. Theorem P's mechanism therefore lives only on the observer-level real lift, which
requires the bridge.

**Lemma N (linear dynamics does not create ergodicity) [A].** On Z^d, any μ, let ρ_0 be a
translation-invariant law on X = ((R^6)²)^{Z^d} with sup_n E abs(x_n)² < ∞. Let
e_n(x) = abs(u_n)² + abs(v_n)² − u_n·(Av)_n, the density of the conserved form of F (SM:296), and
Ē(x) = lim_N abs(Λ_N)⁻¹ Σ_{n∈Λ_N} e_n(x) over cubes Λ_N, which exists ρ_0-a.s. and in L¹ (ergodic
theorem for Z^d actions). Then Ē∘F = Ē ρ_0-a.s.; so the law of Ē is the same under F^t_*ρ_0 for every finite t, and if
Ē is non-degenerate under ρ_0, no F^t_*ρ_0 (t finite) is translation-ergodic.

*Scope.* The ergodicity statement at finite t also follows directly from F being a
translation-equivariant measurable bijection of X (inverse as in S-1): F^t_*ρ_0 is
translation-ergodic iff ρ_0 is. Lemma N adds an explicit conserved invariant Ē. Ē is not weakly
continuous, and whether Ē, or any clustering property, survives t → ∞ limits (where
Gaussianization or mixing could arise) is not shown. For an F-stationary state, Q1's object,
nothing evolves, and Lemma N says nothing about how such a state is selected.

*Proof.* q_Λ(x) := Σ_{n∈Λ} (e_n(Fx) − e_n(x)) is a quadratic form in x of finite range. For x
supported at distance > 3 from Λ^c, Fx is supported in Λ and q_Λ(x) = Q(Fx) − Q(x) = 0 by
conservation; for x supported far outside Λ, q_Λ(x) = 0. By polarization and locality the kernel of
q_Λ vanishes except on pairs of sites within distance 4 of ∂Λ, so
E abs(q_Λ) ≤ C abs(∂Λ) sup_n E abs(x_n)², and q_{Λ_N}/abs(Λ_N) → 0 in L¹. Passing to a subsequence,
Ē(Fx) = Ē(x) a.s. Ē is translation-invariant, so a non-degenerate Ē rules out ergodicity. ∎

The same holds for each of the infinitely many local conserved densities of the linear rule
(Q_B, P_C of SM:296). Positive direction, for contrast: finite-range dependence with range R is
carried by F^t to range R + 2t (finite propagation), so at each finite time K3 is inherited from
the preparation, with a range that grows. At finite times, in both directions, the clustering of an
evolved state is inherited from its preparation; limits t → ∞ are not covered.

**Q1 assignment.**
- Selected counting measure: NOT SOURCED, by S-2, conditional on (B) and (H); the missing property
  is distinct block values. CC-S: S-1 states what it does supply (K3 at the substratum level; mixing,
  and K3 for finite-range Π, at the observer level).
- Energy-shell ensemble: NOT SOURCED under (H′), by S-2′.
- Record-selected orbit measure, or a prepared μ_H: REDUCED. The basis is that Main and SM supply
  no derivation of its stationary law or clustering: the stationary law of the realized dynamics is
  recorded as open (SM:290, SM:298, SM:1225). S-3 and Lemma N (finite t) are consistent with this
  and do not by themselves establish it. Whether an orbit or prior compatible with
  records yields an F-stationary, K2-clustering observer law with distinct block values is that
  open question.

## 2. Q3 (K0): OBSTRUCTION

### 2.1 Phase-locked plane waves

For k ∈ T^d with θ(k) = arccos(a(k)/2) as in [S] §1.1, put E_k(n) = (e^{iθ(k)} e^{ik·n}, e^{ik·n})
∈ ℂ². Then [A]:
- F_s E_k = e^{−iθ(k)} E_k (from a = λ + λ⁻¹ with λ = e^{iθ});
- J_s E_k = −i E_k, since J_s has symbol (F̂_s − cos θ)/sin θ ([S] §1.1; unit A §1);
- translation by m multiplies E_k by e^{ik·m}.

So for c ∈ ℂ the real configuration Re(c E_k) evolves by c ↦ c e^{−iθ(k)}, translates by
c ↦ c e^{ik·m}, and R(e^{iγ}) = cos γ + J_s sin γ acts by c ↦ c e^{−iγ}.

### 2.2 The resonant quartet

Fix d ≥ 1, 0 < abs(μ) < 1, and s = 1, r = √2 (so that π, s, r are rationally independent: π is
transcendental and 1, √2 are independent over Q). Let
k_j = (κ_j, π/2, …, π/2) with κ = (π/2 + s, π/2 − s, π/2 + r, π/2 − r).
- a(k_j) = (2μ/d) cos κ_j, since cos(π/2) = 0. Hence θ(k_1) + θ(k_2) = arccos(−x) + arccos(x) = π
  with x = (μ/d) sin s, and likewise θ(k_3) + θ(k_4) = π. So Σ_j θ(k_j) = 2π: the quartet is
  resonant. Also Σ_j k_j ≡ 0 (first coordinate 2π, others 2π).
- **Relation lattice.** Λ = {m ∈ Z^4 : m·(k_j)_i ∈ 2πZ for every coordinate i}. From the
  coordinates i ≥ 2, (π/2)Σm ∈ 2πZ. From i = 1, (π/2)Σm + s(m_1 − m_2) + r(m_3 − m_4) ∈ 2πZ, and
  rational independence gives m_1 = m_2, m_3 = m_4. So Λ = {(a, a, b, b) : a + b even}.
- **Phase group.** H = Λ^⊥ ⊂ T^4. By Kronecker's theorem the closure of the subgroup generated by
  the translation shifts ((k_j)_i)_j is H.
- **F-shift.** m·θ = (a + b)π ∈ 2πZ for every m ∈ Λ, so (−θ(k_j))_j ∈ H.
- **A_1 phase.** γ(1, 1, 1, 1) ∈ H iff (2a + 2b)γ ∈ 2πZ for all (a, b) with a + b even, iff
  4γ ∈ 2πZ.

Let ψ = (ψ_j) be Haar-distributed on a coset ψ^0 + H, β_j > 0, â the unit vector of A_1, and
y = Σ_j β_j Re(e^{iψ_j} E_{k_j}) ⊗ â.

### 2.3 The witness ρ_Q

Let g ~ ρ_0 (SMD-SRC-1's finite-range Gaussian state, covariance c ⊗ Σ_b κ_b P_b [S] §4.1),
independent of y, and ρ_Q the law of x = g + y. Choose κ_b and β so that the on-site block values
below are distinct.

**Properties [A].**
1. *F-stationary and translation-invariant.* Translations and F shift ψ by elements of H, which
   preserve Haar on ψ^0 + H; g is stationary and invariant [S].
2. *Translation-ergodic (K0).* The translation action on ψ^0 + H is a rotation by a dense subgroup
   of H, so Haar on the coset is ergodic. g is mixing. A product of a weakly mixing and an ergodic
   action is ergodic, and x is a factor of (g, y).
3. *Not mixing (K1 fails), not K2.* y has pure point spectrum and non-decaying covariance. ρ_Q is
   translation-invariant and non-Gaussian (⟨f, y⟩ is bounded and non-constant, so by Cramér's
   decomposition theorem ⟨f, x⟩ is not normal), so K2 fails by Theorem P [S] (CC-M).
4. *Moments and mean.* All moments are uniformly bounded; E y = 0 because each ψ_j is marginally
   uniform on the coset (e_j ∉ Λ).
5. *Second moment.* E[e^{i m·ψ}] = e^{i m·ψ^0} if m ∈ Λ and 0 otherwise. The vectors e_j ± e_l
   (j ≠ l) and 2e_j are not in Λ, so all cross-mode and anomalous terms vanish:
   C_y = Σ_j (β_j²/2) Re(E_{k_j} E_{k_j}†) ⊗ P_A1, J-Hermitian (each term is invariant under the
   phase rotation that J generates).
6. *Fixed set.* C = κ_T c ⊗ P_T1 + κ_E c ⊗ P_E + (κ_A c + C_y^{sp}) ⊗ P_A1 has the TPC form (r2)
   with pairwise distinct block operators; Σ_n is block-scalar with values 2κ_T, 2κ_E and
   2κ_A + Σ_j β_j² (Σ_n = 2ℓ_n C ℓ_nᵀ with the u-component; the u-entry of E_{k_j} has modulus 1),
   distinct by choice; H-PF by construction; F = F_s ⊗ I_6 gives
   the kinetic clause; linear offset-free branch, mean 0.
7. *Stab(C) = U(3)×U(2)×U(1).* "⊆" is [L2] §4.2's scope argument for the TPC form with distinct
   block operators. "⊇": a block-diagonal w acts on the T_1 and E blocks by (★) [S] §4.1, and on the
   A_1 block by cos γ + J sin γ, which preserves the J-Hermitian C_{A_1}.
8. **SMD fails.** Let w ∈ Stab(ρ_Q). Then w ∈ Stab(C), so w is block-diagonal and R(w) preserves
   C_0, hence the law of g (Lemma G [S]). The characteristic functionals satisfy
   χ_x = χ_g χ_y with χ_g > 0, so R(w) preserves the law of y. On y, R(w) acts by the A_1 phase,
   ψ ↦ ψ − γ(1, 1, 1, 1). Distinct frequencies make ψ a function of the configuration y (finite
   exponential sums with distinct frequencies are linearly independent), so the law of y determines
   the coset, and the shifted coset equals ψ^0 + H iff 4γ ∈ 2πZ (§2.2). Directly: the moment
   E[e^{i(ψ_1+ψ_2+ψ_3+ψ_4)}] = e^{i(1,1,1,1)·ψ^0} ≠ 0, since (1, 1, 1, 1) ∈ Λ, and the A_1 phase
   multiplies it by e^{−4iγ}. Hence Stab(ρ_Q) = U(3)×U(2)×Z_4 ⊊ Stab(C).

### 2.4 CC-R (the resonance and the locking are load-bearing)

- If Σ_j θ(k_j) ∉ 2πZ while Σ_j k_j ≡ 0, the F-shift (−θ_j) has (1,1,1,1)·(−θ) ∉ 2πZ, so F moves
  the coset ψ^0 + H to a different coset: L-SDS fails.
- If the locking is removed (Haar on the full torus T^4), every phase rotation preserves the law,
  the U(1)-breaking moment vanishes, and Stab(ρ) = Stab(C).
- Under K1 the mechanism is unavailable: mixing excludes atoms of the covariance spectrum (§3,
  Lemma A).

### 2.5 Why the discrete part sits in A_1 (Lemma A) [A]

**Lemma A.** Let ρ be translation-ergodic with finite second moments, and M its 12×12 matrix
spectral measure (C(n) = ∫ e^{ik·n} M(dk)). Then each atom M({k}) has rank ≤ 1. If ρ is
translation-mixing, M has no atoms.

*Proof.* The atom is the Gram matrix of the projections of the x_{0,α} onto the eigenspace of the
translation action on L²(ρ) with character k. For an ergodic action that eigenspace has dimension
≤ 1 (for eigenfunctions f, g with the same character, f/g, defined where g ≠ 0 and |g| constant,
is invariant), so all projections are multiples of one vector. For a centred law (the fixed set
supplies mean 0), mixing gives C(n) → 0, and by
Wiener's lemma (Cesàro mean of abs(C(n))² equals the sum of squared atom masses) there are no
atoms. ∎

**Corollary.** Under K0 and TPC (r2), M = Σ_b M_b ⊗ P_b, and an atom has rank
Σ_b rank(M_b({k}))·dim b ≤ 1: only the A_1 block can carry atoms; the T_1 and E blocks have
continuous spectrum. So any discrete-spectrum mechanism for SMD failure under K0 with TPC acts in
A_1, as ρ_Q does.

## 3. Q2 (K1): OPEN, with a sharpened gap

**Lemma R (cumulants live on resonance sets) [A].** Let ρ be translation-invariant and F-stationary
with uniformly bounded moments of order r, on 0 < abs(μ) < 1. Write x = x^+ + x^− with
x^± = P_± x (the eigenprojections of F̂, convolution operators with analytic symbols [S] Lemma S),
and let κ̂_ε (ε ∈ {+, −}^r) be the Fourier transform, a tempered distribution, of the joint
cumulant of (x^{ε_1}_{n_1}, …, x^{ε_r}_{n_r}). Then
supp κ̂_ε ⊆ {Σ_j k_j ≡ 0} ∩ {Σ_j ε_j θ(k_j) ∈ 2πZ}.
*Proof.* Translation invariance gives the first factor. F-stationarity gives
κ̂_ε = e^{−iΣ_j ε_j θ(k_j)} κ̂_ε, and (1 − e^{−iΘ_ε}) is smooth, so κ̂_ε vanishes off its zero
set. ∎

**Corollary T (CC-T, reproduces Theorem P for translation-invariant states) [A].** Under K2, κ̂_ε
restricted to the momentum constraint is a continuous function of (k_2, …, k_r). For r ≥ 3,
Θ_ε(−Σ_{j≥2} ε-signed k_j, k_2, …) is real-analytic and non-constant (if ∇_{k_2} vanished
identically, ∇θ would be constant, since k_3 varies the other argument independently, so μ = 0),
so each level set Θ_ε = 2πℓ is null; a continuous function vanishing almost everywhere vanishes.
So all cumulants of order ≥ 3 vanish, and ρ is Gaussian, as Theorem P [S] states. CC-T green.

**What K1 leaves.** A K1 witness, if one exists, with uniformly bounded moments of all orders
(needed for the cumulant statements below), must:
- have no covariance atoms (Lemma A), so the phase-locking mechanism of §2 is unavailable;
- violate K2 (Theorem P [S]);
- carry a nonzero joint cumulant of order ≥ 3 whose Fourier transform is a singular distribution
  supported on a resonance set {Σ_j k_j ≡ 0, Σ_j ε_j θ(k_j) ∈ 2πZ} (Lemma R), and, to violate SMD,
  one with Σ_j ε_j ≠ 0 on the relevant blocks or otherwise not invariant under some w ∈ Stab(C).

**Routes tried, none successful [W].**
- Random wave vectors along the resonant family of §2.2: the frequencies are recoverable from the
  configuration, so they form a non-trivial translation-invariant random variable: not ergodic.
- Superpositions of independent quartets: either the frequencies are again recoverable (not
  ergodic), or, with vanishing amplitudes, the CLT removes the locked moment in the limit.
- Equivariant nonlinear factors of a Gaussian state: the kernel must sit on a resonance set, a null
  set; with a non-singular input spectrum the output variance diverges (as recorded in [S] §5).

**Precise gap.** Whether a translation-mixing, F-stationary law on 0 < abs(μ) < 1 exists with a
nonzero singular resonant cumulant of order ≥ 3; and if so, one meeting the fixed set and violating
SMD.

## 4. Q4: the imports

**[I-Stein] re-derived [A], modulo the textbook Stein-equation bounds.** Let X_1, …, X_N be centred
with finite fourth moments, σ² = Var Σ X_i > 0, W = Σ X_i/σ, and dependency neighbourhoods
N_i ∋ i of size ≤ D, symmetric (j ∈ N_i ⇔ i ∈ N_j, so that each index lies in at most D
neighbourhoods), such that, for index sets I, I′ with I′ disjoint from ∪_{i∈I} N_i, the families
(X_i)_{i∈I} and (X_j)_{j∈I′} are independent (finite-range dependence with balls of radius R gives
this, D = (2R+1)^d). Then
d_W(W, Z) ≤ (D²/σ³) Σ_i E abs(X_i)³ + (4/√π)(D^{3/2}/σ²) (Σ_i E X_i⁴)^{1/2}.
- *Input (textbook):* for 1-Lipschitz h, the Stein solution f_h of f′(w) − w f(w) = h(w) − E h(Z)
  satisfies ‖f_h′‖ ≤ (2/π)^{1/2} and ‖f_h″‖ ≤ 2, so d_W(W, Z) ≤ sup |E[f′(W) − W f(W)]| over such f.
- *Decomposition.* With Δ_i = σ⁻¹ Σ_{j∈N_i} X_j and W_i = W − Δ_i, independence gives
  E[X_i f(W_i)] = 0, so E[W f(W)] = σ⁻¹ Σ_i E[X_i (f(W) − f(W_i))], and
  E[f′(W) − W f(W)] = E[f′(W)(1 − T)] − σ⁻¹ Σ_i E[X_i (f(W) − f(W_i) − Δ_i f′(W))],
  T = σ⁻¹ Σ_i X_i Δ_i, E T = 1 (since E X_i X_j = 0 for j ∉ N_i).
- *Second term.* abs(f(W) − f(W_i) − Δ_i f′(W)) ≤ ‖f″‖ Δ_i²/2, so it is at most
  σ⁻³ Σ_i Σ_{j,k∈N_i} E abs(X_i X_j X_k) ≤ σ⁻³ D² Σ_i E abs(X_i)³ (AM–GM on triple products; each
  index occurs in at most D² triples in each slot).
- *First term.* At most ‖f′‖ (Var T)^{1/2}. Cov(X_iX_j, X_kX_l) = 0 unless {k, l} meets
  N_i ∪ N_j; each nonzero covariance is at most (1/2) Σ of the four fourth moments (AM–GM), and
  each index occurs in at most 4D³ nonzero terms per slot, so Var T ≤ 8 D³ σ⁻⁴ Σ_i E X_i⁴.
  Multiplying by (2/π)^{1/2} gives the stated second term.

The constants differ from Ross's Theorem 3.5 as recalled in [S]; only convergence to 0 is used, and
the use in [S] Corollary P3′ goes through unchanged (Σ E abs(X_n)³ ≤ M_3 ‖f_t‖_∞ ‖f_t‖_2² and
Σ E X_n⁴ ≤ M_4 ‖f_t‖_∞² ‖f_t‖_2²). Corollary P3′ thus rests on this derivation and the textbook
Stein-equation bounds, not on an unchecked recollection of a published constant.

**H-αCLT unchanged.** No source was read (no external access, §A.50 item 4). It remains a stated
hypothesis with the distance-indexed α ([S] §3); Corollary Pα stays conditional on it.

## 5. Witness check (CC-W) for ρ_Q

| Item | ρ_Q |
| --- | --- |
| H-link m = 1; carrier T_1 ⊕ E ⊕ A_1 | ✓ |
| H-cust kinetic clause (F commutes with every R(w)) | ✓ |
| O-equivariant Σ_n, distinct values | ✓ (§2.3 item 6) |
| linear offset-free branch; mean 0 | ✓ |
| H-PF (φ := Φ) | ✓ |
| TPC (r2) | ✓ (item 6) |
| J-Hermitian second moment | ✓ (item 5) |
| translation invariance | ✓; O-invariance of the law not claimed (not in the fixed set) |
| L-SDS | ✓ (item 1) |
| K3 / K2 / Kα / K1 / K0 | ✗ / ✗ / ✗ / ✗ / ✓ |
| SMD | ✗ (item 8) |

## 6. Consequences, stated with conditions

- **For #1217.** SMD-SRC-1 replaced SMD (on Z, 0 < abs(μ) < 1) by L-SDS with K2. This unit finds
  that the specified substratum supplies no state meeting the fixed set: under (B) and (H) the
  selected measure's observer image is a single mixing phase with scalar Σ, so the condensate is
  neither that image nor an ergodic component of it (S-2), and, under (H′), the energy-shell
  ensemble has scalar Σ (S-2′); the missing property is distinct block values. For prepared priors and
  record-selected orbits, Main and SM supply no derivation (SM:290, SM:298, SM:1225). The clustering
  condition of the condensate state is therefore a condition on the state, like SMD; it is not adopted, and whether to state it is the owner's
  decision (§A.29, §A.50 item 6). Clustering cannot be weakened to ergodicity: K0 does not suffice
  (ρ_Q).
- **For #1049.** No bearing beyond SMD-SRC-1's.
- **Finding for routing (#1217).** SMD-SRC-1's mutable status records (REPORT.md §14 and
  PRESERVATION.md) list Corollary P3′ as conditional on the recalled [I-Stein]. After review of §4
  here, they could record P3′ as resting on this re-derivation and the textbook Stein-equation
  bounds. Listed, not edited.
- **For the SSB reading (SM:136).** Under (B) and (H) the condensate is not an ergodic component of
  the selected measure's observer image (S-2). A spontaneously broken condensate, if realized,
  must come from a non-selected preparation or record-selected orbit.

## 7. Controls

| Control | Result | Status |
| --- | --- | --- |
| CC-W | §5 for ρ_Q | green |
| CC-R | §2.4: breaking the resonance breaks L-SDS; removing the locking restores SMD | green |
| CC-M | ρ_Q violates K2 and K1; Lemma A and Lemma R do not apply positively to ρ_K (non-ergodic) or ρ_D (μ = 0) of [S] | green |
| CC-T | Corollary T reproduces Theorem P for translation-invariant states | green |
| CC-S | S-1 states what the selected measure supplies: K3 at the substratum level; under (B), mixing at the observer level, and K3 for finite-range Π. The missing property is distinct block values (S-2), so "not sourced" is not a relabelling of absent clustering. S-2 names its conditional inputs (B) and (H) | green |
| CC-E | no identity in this report required computation; every identity is exact algebra (§2.2) | vacuous, recorded |
| CC-P | quoted lines re-read at [P] | green |

**Pressure test (§A.31).** No result here favours the framework: Q1 is an obstruction or a
reduction, Q3 an obstruction. The obstruction S-2 was tested against its inputs: without (B) the
observer law is not defined from the substratum at all. (H) is load-bearing for the NOT SOURCED
assignment: without it the selected image may itself have distinct block values, and the
assignment fails. Mixing and extremality would still exclude a decomposition of the image into
broken components, but that alone leaves the image itself as a candidate.

## 8. Productivity (PLAN.md §4)

Met through G1 (Q1 assigned NOT SOURCED and REDUCED, with conditional inputs and bases named), G2
(OBSTRUCTION for K0) and G3 ([I-Stein] re-derived).

| Class | Findings |
| --- | --- |
| NEW | ρ_Q (K0 does not force SMD); the extremality step of S-2 (under (B), the selected measure's observer image is a single mixing phase, so the condensate is not an ergodic component of it) |
| POSITIVE | Corollary T (independent proof of Theorem P for translation-invariant states); the re-derivation of [I-Stein] |
| ELABORATING | Lemma A and its corollary; Lemma R; S-1; S-2′; S-3; Lemma N (finite t); the K1 gap |
| CONFIRMING | S-2's scalar-Σ part (unit A's Proposition C) |

## 9. Open nodes

- **N1 (K1).** The gap of §3.
- **N2 (bridge).** Q1 is conditional on (B); the coarse-graining bridge (SM:232) is unproved.
- **N3 (O-invariant K0 witness).** The cubic orbit of the quartet adds frequency relations (for
  example, the four vectors obtained from k by the diagonal rotations diag(±1, ±1, ±1) of
  determinant 1 sum to 0), which change the relation lattice; not pursued.
- **N4 (prepared states).** Whether a record-selected orbit or a prepared μ_H yields an F-stationary
  K2 observer law with distinct values: SM's open stationary-law obligation.
- **N5 (H-αCLT).** Source not read.
- **N6 (μ = 1).** As in [S].

## 10. Off-`main` references (§A.42 item 8)

| Reference | Classification |
| --- | --- |
| #1169 comments 7208939261 (authority), 7199704501 (WP-2) | provenance: authority records, quoted with author and time; no result uses them |
| commit `98172765` (PLAN.md) and the commit adding this report | support on `main` only once merged without squash (plan-before-report order); not before |
| SMD-SRC-1 (`../smd-sourcing-20261126/`), unit A (`../theorem5-premise-ledger-20261126/`), lane 2 (`../complex-carrier-20261126/`) | support on `main` at [P] |
| Main and SM line citations | support on `main` at [P] |
| textbook facts (Kronecker; Wiener's lemma; ergodic theorem; Cramér's decomposition theorem; Bernoulli actions are mixing and factors inherit mixing; Stein-equation bounds) | standard results, cited by name |
| #1049, #1217 | provenance: accountability |
| Ross's Theorem 3.5 "as recalled in [S]" (§4) | provenance: named only for comparison of constants; no result uses it |
| PR #1612 ("landed via #1612", PLAN.md chronology disclosure) | provenance: names how SMD-SRC-1 reached `main`; the content used is SMD-SRC-1 on `main` |
| #1623 comment 7209241804 (review of r1) | provenance: evidence of review; no result uses it |

Support off `main`: none.

## 11. Verification status and remediation (§A.46 item 4)

**This table authorizes no work.**

| Claim | Status | Missing | Issue | What would resolve it |
| --- | --- | --- | --- | --- |
| S-1, S-3 | model-reviewed (r1 review) | independent non-model review | #1217 | a recorded review |
| S-2 | model-reviewed (r1 review); conditional on (B) and (H) | independent non-model review | #1217 | a recorded review |
| S-2′ | model-reviewed (r2 delta review on #1623); conditional on (H′), Proposition 4b's hypotheses with the shell law in place of the counting measure | independent non-model review; (H′) not established here | #1217 | a recorded review; a check of Proposition 4b's hypotheses for the shell law |
| Conditional input (B) | a reading of the coarse-graining bridge, which is unproved (SM:232); not adopted | a proof of the bridge in the form (B), or a bridge of another form | #1217 | a proof, or an owner decision on the reading |
| Conditional input (H) | Proposition 4b's hypotheses (SM:334–336, as unit A carries them); not established here | as recorded in unit A | #1217 | as recorded in unit A |
| Q1 REDUCED assignment | rests on the absence of a derivation in Main and SM (SM:290, SM:298, SM:1225) | a derivation or refutation of a stationary clustering observer law with distinct values from a prepared prior or record-selected orbit | #1217 | either |
| Lemma N (finite t) | model-reviewed (r1 review) | review; the t → ∞ question is not addressed | #1217 | a recorded review; a separate result for limits |
| ρ_Q (K0 obstruction) | model-reviewed (r1 review) | independent non-model review; optionally a non-model check of the relation-lattice computation | #1217 | a recorded review |
| Lemmas A, R; Corollary T | model-reviewed (r1 review) | independent non-model review | #1217 | a recorded review |
| [I-Stein] re-derivation | model-reviewed (r1 review); uses textbook Stein-equation bounds | independent non-model review | #1217 | a recorded review |
| K1 (§3) | open | a proof or a witness | #1217 | either |
| N3, an O-invariant K0 witness | open; ρ_Q is not O-invariant as a law (not required by the fixed set) | a construction with the cubic orbit's relation lattice, or a proof that none exists | #1217 | either |
| H-αCLT | stated hypothesis, no source | a source check or a proof | #1217 | a pinned theorem or a proof |

## 12. Node log and stopping

- **Pass 1.** Q1 sources read; S-1, S-2, S-3.
- **Pass 2.** Lemma N; Q1 assignment.
- **Pass 3.** Lemma A; the quartet construction, relation lattice and ρ_Q; CC-R.
- **Pass 4.** Lemma R, Corollary T; K1 routes. No NEW finding.
- **Pass 5.** [I-Stein] re-derivation. No NEW finding.
- **Pass 6.** §A.34 check (Lemma A one direction; S-2's "not a component" from extremality; ρ_Q's
  "iff 4γ ∈ 2πZ", both directions); claim/evidence check of §0 and §6. No NEW finding.
- **r2.** Review findings F1–F11 applied: Q1 verdict reworded (the missing property is distinct
  block values); S-2′ added; Lemma N scoped to finite t and reclassified; routing and tracing lines
  added. No r1 result changes; one derivation added (S-2′, for F4).

The first stopping condition holds: every question is assigned and the controls have run. Passes
4–6 are three consecutive passes with no NEW finding. No result needed a premise outside the fixed
set and the stated conditional inputs.
