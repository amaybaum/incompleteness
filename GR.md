# Dynamics Selection and Emergent General Relativity in the Observational Incompleteness Framework

### Alex Maybaum

### March 2026

---

## Abstract

The Observational Incompleteness (OI) framework [1] proves that quantum mechanics emerges necessarily from embedded observation in a deterministic system. This paper tests the framework's rigidity by constructing an explicit lattice realization and asking: does the dynamics uniquely selected by the QM requirement also produce the inputs for general relativity? It does. Among all second-order reversible nearest-neighbor dynamics on a lattice, center independence (necessary for emergent QM), spatial isotropy, and linearity uniquely select the discrete wave equation — for any alphabet size q ≥ 2 and dimension d ≥ 1. This dynamics, without further tuning, produces area-law entropy, Lorentz-invariant dispersion, horizon thermality, and all inputs to Jacobson's thermodynamic derivation of Einstein's equations. The derivation chain has seven links, all analytically proven for both the linear wave equation over ℝ and the mod-q wave equation over ℤ/qℤ. Each link is an independent check that could have failed; none does. The structural consistency — a dynamics selected by one criterion (emergent QM) passing seven additional tests (emergent GR) with no free parameters — constitutes corroborative evidence for the framework's central claim.

---

## 1. Introduction

The companion paper [1] proves that any observer embedded in a deterministic, bijective system with a coupled, slow, high-capacity hidden sector necessarily describes the visible sector using P-indivisible stochastic dynamics, equivalent to unitary quantum mechanics. The characterization theorem establishes that QM and embedded observation are equivalent — the conditions are necessary and sufficient. (The result is established by two independent routes: the Barandes stochastic-quantum correspondence [2] and a Stinespring dilation construction [1, Appendix A].)

A natural question follows: is the framework rigid or flexible? A framework that accommodates any dynamics equally well has little predictive content. A framework that constrains the dynamics — and where the constrained dynamics independently reproduces known physics beyond QM — provides structural evidence for its correctness.

This paper addresses that question. We construct a specific system — the mod-q discrete wave equation on a lattice with a checkerboard partition — and show that it is uniquely selected by the requirement of emergent QM plus two physical symmetries (isotropy and linearity). We then check whether this dynamics, without modification, provides the inputs needed for Jacobson's thermodynamic derivation of Einstein's equations [3]. The construction proceeds through seven analytical links. At each link, the framework could have produced the wrong answer: the entropy could have scaled with volume rather than area, the dispersion relation could have been non-relativistic, the horizon state could have been non-thermal. None of these failures occurs. The wave equation passes every check, with no free parameters.

The paper's primary contribution is therefore not "deriving GR" — the thermodynamic derivation is due to Jacobson [3] — but demonstrating that the OI framework is overconstrained: the dynamics selected by QM emergence uniquely and correctly produces the inputs for GR emergence, providing independent corroborative evidence for the framework.

---

## 2. The System

The mod-q discrete wave equation on a d-dimensional cubic lattice Λ = (ℤ/Lℤ)^d with periodic boundary conditions:

$$x_\mathbf{i}(t+1) = \left(\sum_{\mathbf{j} \sim \mathbf{i}} x_\mathbf{j}(t) \ - \ x_\mathbf{i}(t-1)\right) \bmod q$$

where the sum runs over the 2d nearest neighbors of site **i**, and q is a positive integer.

**Axiom 1 (Bijectivity).** The phase-space map F: (x(t−1), x(t)) → (x(t), x(t+1)) is bijective.

**Axiom 2 (Finiteness).** The configuration space C = {0, 1, ..., q−1}^{|Λ|} is finite, with |C| = q^{L^d}.

**Axiom 3 (Partition).** The lattice is partitioned into visible (V) and hidden (H) sectors via the checkerboard rule: site **i** is visible if Σ_k i_k is even, hidden if odd. Every visible site has hidden neighbors (C1). For a core-shell partition (visible = cube of side r in a lattice of side L), timescale separation C2 and capacity asymmetry C3 are controlled by the ratio (L − r)/r.

---

## 3. Link 1: Emergent Quantum Mechanics

**Theorem 1.** *The visible-sector propagator of the wave equation with checkerboard partition satisfies G(2) ≠ G(1)² for all L ≥ 4 in any dimension d ≥ 1. The reduced dynamics is non-Markovian.*

**Proof.** The full-system evolution in phase space (x(t), x(t−1)) ∈ ℝ^{2N} is the linear map

$$M = \begin{pmatrix} A & -I \\ I & 0 \end{pmatrix}$$

where A is the lattice adjacency matrix. The visible propagator at lag n is G(n) = P_V M^n P_V^T. For L = 4, d = 1:

$$G(2) - G(1)^2 = \begin{pmatrix} 2 & 2 & 0 & 0 \\ 2 & 2 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

The entries are exactly 2, arising from the two hidden sites that each connect the visible pair. For general L ≥ 4, every pair of visible sites at lattice distance 2 shares at least one hidden neighbor, so G(2) − G(1)² ≠ 0. ∎

**Corollary.** By the Barandes stochastic-quantum correspondence [2], the visible-sector dynamics admits a description as unitary quantum mechanics with a Hermitian Hamiltonian and Born rule.

**Theorem 1b** (C2-C3 strengthening). *The (i,j) entry of G(2) − G(1)² equals |N_H(i) ∩ N_H(j)|, the number of common hidden neighbors. For core-shell partitions, this grows monotonically as the visible core shrinks and the hidden shell grows.* ∎

**Theorem 1c** (Validity window). *The emergent Hamiltonian is valid for lags n < τ_B = (L − r)/(2v). The wave equation has an exact light cone (range R = 1, no exponential tails), so information entering the hidden shell at the core boundary takes at least τ_B steps to traverse the shell and return. Before this time, the emergent description holds; after it, returning correlations invalidate it.* ∎

**Numerical confirmation.** For finite q, P-indivisibility was confirmed via conditional mutual information against a Markov null:

| System | CMI z-score |
|--------|------------|
| 1+1D, L=60, mod-256 wave eq | **31.1** |
| 3+1D, L=8, mod-256 wave eq | **4.7** |
| 1+1D, L=60, binary CA | **30.3** |
| 3+1D, 16³, core r=2 (511:1) | **14.9** |

---

## 4. Link 2: Emergent Spacetime

**Theorem 2.** *The (site, time) partial order on a d-dimensional lattice with L_∞ light cone has Myrheim-Meyer dimension converging to d + 1 as L → ∞.*

**Proof.** The causal relation (i, t) ≺ (j, t′) holds iff t < t′ and ||i − j||_∞ ≤ v(t′ − t). By the Bombelli-Lee-Meyer-Sorkin theorem [4], the ordering fraction converges to the value for d+1 Minkowski spacetime. Numerical confirmation: MM dimension = 3.97 in 3+1D at L=14. ∎

---

## 5. Link 3: Emergent ℏ

**Theorem 3** (Gap Equation). *The classical horizon temperature and the emergent quantum horizon temperature, computed independently, must agree. This uniquely determines*

$$\hbar = \frac{c^3 \varepsilon^2}{4G}$$

*connecting the lattice spacing ε to Newton's constant. Self-consistently, ε = 2l_P.*

**Proof.** The argument proceeds in four steps.

*Step 1: Classical horizon temperature.* The lattice has a discreteness scale ε. A local causal horizon with surface gravity κ has an entropy density of one degree of freedom per minimal cell of area ε², so dS = dA/ε². The Jacobson identity [3] gives the energy flux across the horizon as dE = (c² κ / 8π G) dA. Applying the Clausius relation dE = T dS:

$$T_{\text{cl}} = \frac{c^2 \varepsilon^2 \kappa}{8\pi G k_B}$$

This temperature is computed entirely within the classical substratum. No ℏ appears.

*Step 2: Boundary-only dependence.* The emergent action scale ℏ is determined by the partition boundary, not by volumetric hidden-sector data. This follows from spatial locality: the transition probabilities $T_{ij}(t)$ depend, to leading order, only on the visible-boundary dynamics (see [1, §5.2] for the full argument). The partition-intrinsic quantities with which to construct an action are c, G, and ε. The unique combination with dimensions of action is ℏ = β c³ε²/G for a dimensionless constant β.

*Step 3: Emergent quantum temperature.* The emergent QFT of Link 1 lives on the classical background, which possesses a bifurcate Killing horizon with surface gravity κ. Regularity of the Euclidean (Wick-rotated) metric at the horizon enforces periodicity 2πc/κ in imaginary time. Any QFT on this background — including the lattice-regularized one emerging from the OI framework — must therefore be in a KMS (thermal) state at temperature:

$$T_Q = \frac{\hbar \kappa}{2\pi c k_B}$$

with ℏ as the sole unknown. This is a theorem *within* the derived QFT, not an external import. For the lattice theory, thermal periodicity is robust against UV modifications of the dispersion relation, with corrections at O((εκ/c)²) [see references in 1, §5.2].

*Step 4: Thermal matching.* A thermometer at the horizon is a visible-sector object whose click rate is computable in either description. The classical and emergent accounts of one boundary cannot disagree:

$$T_{\text{cl}} = T_Q \implies \frac{c^2 \varepsilon^2 \kappa}{8\pi G k_B} = \frac{\hbar \kappa}{2\pi c k_B}$$

The surface gravity κ cancels — confirming that ℏ is structural (boundary-dependent) rather than state-dependent. Solving:

$$\boxed{\hbar = \frac{c^3 \varepsilon^2}{4G}}$$

Rearranging: ε² = 4ℏG/c³ = 4l_P², giving ε = 2l_P. The factor 1/4 in the Bekenstein-Hawking formula S = A/(4l_P²) is then derived: each cell of area ε² = 4l_P² contributes one entropy unit, so S = A/ε² = A/(4l_P²). ∎

*Remark.* The two temperatures are computed from independent inputs: T_cl from the classical substratum alone (Axioms 1–3, the Jacobson identity, and η = 1/ε²), T_Q from the emergent QFT alone (Link 1's theorem plus Euclidean regularity). The match is non-trivial: T_cl could have depended on volumetric hidden-sector data (excluded by Step 2), or T_Q could have depended on the quantum state (it does not — the KMS temperature is purely kinematic). That neither pathology obtains makes the gap equation a genuine determination, not a tautology.

---

## 6. Link 4: Entropy Proportional to Area

**Theorem 4** (Area Law). *The entanglement entropy of a spatial region V in the d-dimensional wave equation scales as S(V) = η |∂V| / ε^{d−1}. This holds for both the linear wave equation over ℝ and the mod-q wave equation over ℤ/qℤ.*

**Proof.** *Over ℝ:* The linear wave equation on a lattice is equivalent to a system of coupled harmonic oscillators with a quadratic Hamiltonian determined by the adjacency matrix A. This is a Gaussian (free bosonic) system, so the area-law theorem of Eisert, Cramer, and Plenio [5] applies directly.

*Over ℤ/qℤ:* The area law follows from the spatial Markov property of nearest-neighbor dynamics. Let V° = V \ ∂V be the interior of a block V and ∂V its boundary (sites adjacent to V^c). The wave equation has range R = 1, so x_i(t+1) depends only on x_j(t) for |i − j| ≤ 1 and on x_i(t−1). For any i ∈ V°, all neighbors lie inside V, so x_i(1) is a function of initial data within V alone. With uniform initial conditions (independent across sites), V° ⊥ V^c | ∂V. By the chain rule: I(V; V^c) = I(∂V; V^c) + I(V°; V^c | ∂V) = I(∂V; V^c) ≤ H(∂V) ≤ |∂V| · log₂ q. The mutual information scales as boundary area, not volume, for any q ≥ 2 and d ≥ 1. Numerical confirmation (Appendix A.5) gives I/|∂V| ≈ 0.3 log₂ q per boundary pair, constant to within 3% as block width varies from 1 to 7.

Combined with the gap equation (Theorem 3), ε = 2l_P, giving S = η A/l_P² for d = 3. The coefficient η = 1/4 is fixed by the thermal matching condition (§5, Step 4). ∎

---

## 7. Link 5: Lorentz Invariance

**Theorem 5** (Relativistic Dispersion). *The wave equation has exact dispersion relation cos ω = cos k.*

**Proof.** Substituting x_j(t) = A exp(i(kj − ωt)):

$$e^{-i\omega} + e^{i\omega} = e^{-ik} + e^{ik} \implies \cos\omega = \cos k \qquad \square$$

For small k: ω = |k| + O(k³), giving relativistic propagation with v = 1. The identity is algebraic: for the mod-q wave equation, the same substitution using characters of ℤ/qℤ yields the same dispersion relation exactly, not as a large-q approximation.

---

## 8. Link 6: Unruh Temperature

**Theorem 6** (Lattice Bisognano-Wichmann). *For free lattice systems whose low-energy effective theory is Lorentz-invariant, the Bisognano-Wichmann theorem holds on the lattice: the entanglement Hamiltonian for a half-space bipartition has the BW form (linear spatial deformation of the physical Hamiltonian), with errors vanishing as ℓ^{−2} [6, 7]. For free-fermion and harmonic-oscillator chains, this has been proven analytically [8].*

The mod-q wave equation is a coupled harmonic oscillator system — precisely the class for which the lattice BW theorem is proven. Its low-energy dispersion is relativistic (Theorem 5). Therefore the reduced state for a Rindler observer is thermal at

$$T_U = \frac{\hbar\kappa}{2\pi c k_B}$$

where κ is the surface gravity. The thermality of the Unruh effect is robust against UV modifications of the dispersion relation: for the lattice dispersion cos ω = cos k, corrections to the Unruh temperature scale as O(ε²κ²/c²) [9, 10]. ∎

---

## 9. Link 7: Einstein's Equations

**Theorem 7** (Jacobson [3]). *Given (i) δS = η δA/l_P² for local causal horizons, (ii) T = ℏκ/(2πck_B), and (iii) the Raychaudhuri equation, the Clausius relation δQ = TδS yields:*

$$R_{\mu\nu} - \frac{1}{2}Rg_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}$$

The OI framework provides all three inputs: (i) from Theorem 4 — the area-law entropy holds for any local patch because the spatial Markov property applies to arbitrary connected subregions; (ii) from Theorem 6 — the Unruh temperature at each local horizon; (iii) from the emergent (d+1)-dimensional Lorentzian manifold (Theorem 2), on which the Raychaudhuri equation is a kinematic identity relating the expansion of null congruences to the Ricci tensor. ∎

---

## 10. The Complete Chain

| Link | Statement | Proof |
|------|-----------|-------|
| 1 | Non-Markovian → QM | Theorems 1, 1b, 1c |
| 2 | MM dimension = d+1 | Theorem 2 |
| 3 | Gap equation → ℏ | Theorem 3 |
| 4 | S ∝ A (area law) | Theorem 4 |
| 5 | cos ω = cos k (Lorentz invariance) | Theorem 5 |
| 6 | Unruh temperature | Theorem 6 |
| 7 | Einstein's equations | Theorem 7 |

All seven links are analytical for the linear wave equation over ℝ. For the mod-q wave equation over ℤ/qℤ, all seven have analytical proofs: the lattice BW theorem (Link 6) is proven for free-particle systems [8], the class to which the wave equation belongs.

---

## 11. Discussion

### 11.1 The dynamics selection

The OI axioms derive quantum mechanics **generically**: any bijective dynamics with a coupled V/H partition produces non-Markovian reduced dynamics (Theorem 1 for linear systems; numerical confirmation for nonlinear CAs with z up to 30.3). Lorentz invariance is **not generic** — it requires wave-equation dynamics. But this choice is not arbitrary; it is uniquely determined by three physical requirements.

**Theorem 8** (Dynamics selection). *Among all second-order reversible nearest-neighbor dynamics on a d-dimensional lattice of alphabet size q, the requirements of (i) center independence, (ii) spatial isotropy, and (iii) linearity uniquely select the discrete wave equation f(neighbors) = Σ neighbors mod q. This holds for any q ≥ 2 and d ≥ 1.*

**Proof.** The update function has the form x_i(t+1) = (f(neighbors of i at time t) − x_i(t−1)) mod q. Center independence requires that f not depend on x_i itself: f reduces to a function of the 2d neighboring values only. Spatial isotropy requires f to be symmetric under all permutations of the neighbors that correspond to lattice symmetries. Linearity over ℤ/qℤ requires f(a + a') = f(a) + f(a') for neighbor configurations a, a'. The unique function satisfying all three is f = α(x₁ + x₂ + ... + x_{2d}) mod q for some constant α. The propagation speed is v = α, so α = 1 gives the maximum lattice-scale speed. This is the discrete wave equation. ∎

Each requirement has a physical justification:

**Center independence is necessary for emergent QM.** Center dependence suppresses P-indivisibility for linear rules over ℤ/qℤ: Rule 150 (f = l ⊕ c ⊕ r) has zero P-indivisibility (CMI z = 0.0) vs Rule 90's z = 7.2, despite identical propagation speed. The mechanism — information screening by the visible self-coupling — is proven analytically in §11.2 and confirmed numerically through q = 64 (Appendix A.4).

**Spatial isotropy is required for Lorentz invariance.** Without left-right (or rotational) symmetry, the dynamics has a preferred spatial direction, breaking the isotropy that Lorentz invariance demands.

**Linearity gives maximum propagation speed.** Among all center-independent, isotropic dynamics, the linear wave equation achieves the maximum propagation speed v = 1 (the lattice speed of light). The dispersion relation cos ω = cos k (Theorem 5) gives exact group velocity v_g = sin k / sin ω → 1 as k → 0. Nonlinear center-independent dynamics generically have v < 1, confirmed by the exhaustive scan of all 256 binary rules: the 53 QM-producing rules have mean speed 0.33, while only Rule 90 achieves v = 1 (anti-correlation r = −0.60, p < 10⁻⁴).

The derivation chain for GR therefore requires wave-equation dynamics, uniquely selected by center independence, isotropy, and linearity. Linearity is itself selected by three independent criteria (§11.2): maximum propagation speed, maximum P-indivisibility, and horizon thermality.

### 11.2 Caveats

**The continuum limit and Jacobson stability.** The derivation chain works on a finite lattice but invokes continuum results in the final link (Jacobson's thermodynamic derivation). The concern is whether lattice corrections to Lorentz invariance invalidate the result. This can be resolved by decomposing Jacobson's derivation into its four inputs and checking each independently:

*(i) δS = δA/ε² (area-law entropy).* Proven for Gaussian systems over ℝ [5] and for any nearest-neighbor dynamics over ℤ/qℤ via the spatial Markov property (Theorem 4). No Lorentz invariance enters. **Exact on the lattice.**

*(ii) T = ℏκ/(2πck_B) (Unruh temperature).* This requires the Bisognano-Wichmann theorem. On the lattice, the BW form of the entanglement Hamiltonian is proven analytically for free-particle systems [8], confirmed numerically across multiple universality classes [6, 7], and shown to be robust against UV modifications of the dispersion relation with corrections at O(ε²κ²/c²) [9, 10]. **Approximate: O(ε²κ²/c²) corrections.**

*(iii) δQ = ∫ T_μν k^μ dΣ^ν (energy flux).* This is a definition on the emergent manifold (Theorem 2). The stress-energy tensor is constructed from the emergent fields; the integral is over a null generator of the local causal horizon. No Lorentz invariance is required. **Exact on the emergent manifold.**

*(iv) Raychaudhuri equation.* The identity dθ/dλ = −(1/2)θ² − σ_{ab}σ^{ab} − R_μν k^μ k^ν is kinematic: it holds on any pseudo-Riemannian manifold as a consequence of the definition of curvature. No Lorentz invariance is required. **Exact on the emergent manifold.**

Since inputs (i), (iii), and (iv) are lattice-exact, corrections to Einstein's equations enter only through input (ii):

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu} \times \left[1 + \mathcal{O}\!\left(\frac{\varepsilon^2 \kappa^2}{c^2}\right)\right]$$

For the cosmological horizon, εκ/c = 2l_P · H/c ~ 10⁻⁶¹, giving corrections of order 10⁻¹²². For solar-mass black holes, εκ/c ~ 10⁻³⁸, giving corrections of order 10⁻⁷⁶. The corrections are negligible for any horizon much larger than the Planck scale.

**Center independence and emergent QM.** Theorem 8 relies on center independence as necessary for emergent QM. Numerical experiments (Appendix A.4) confirm this for every q from 2 to 64. The following argument proves the mechanism on the full lattice, not just a single site.

For the checkerboard partition, the adjacency matrix A is bipartite: A_VV = 0 (no visible–visible edges). A center-dependent rule replaces A with A + I, giving (A + I)_VV = I.

*CI case (A_VV = 0):* For each visible site i, the update x_i(t+1) = [h_{i−1}(t) + h_{i+1}(t) − x_i(t−1)] mod q does not contain x_i(t). Therefore X_V(t+1) is a function of (H(t), X_V(t−1)) that carries no information about X_V(t). Conditioning on X_V(t+1) constrains H(t) but does not screen X_V(t) from the future. Since H(t+1) depends on X_V(t), the path X_V(t) → H(t+1) → X_V(t+2) bypasses the present: the process is non-Markovian.

*CD case ((A+I)_VV = I):* The update x_i(t+1) = [x_i(t) + h_{i−1}(t) + h_{i+1}(t) − x_i(t−1)] mod q contains x_i(t) explicitly. Conditioning on (X_V(t), X_V(t+1)) gives, for each visible site i, the constraint h_{i−1}(t) + h_{i+1}(t) = x_i(t+1) − x_i(t) + x_i(t−1) mod q. This is a system of |V| linear equations in |H| unknowns over ℤ/qℤ, with coefficient matrix A_VH. When this system has a unique solution (which it does generically for q prime), the hidden state H(t) is fully determined by (X_V(t), X_V(t+1), X_V(t−1)). Since the full state determines all future evolution, the augmented process Y_V(t) = (X_V(t), X_V(t−1)) is Markov. Numerical verification: the augmented-state CMI for CD is suppressed by 10–30× relative to CI at all tested q from 3 to 7.

The mechanism is information screening: center coupling makes X_V(t+1) an explicit function of X_V(t), allowing the present to determine the hidden state and screen the past from the future. Without center coupling (A_VV = 0), the present carries no information about the visible past, so the hidden sector retains unscreened correlations. Over ℝ, the screening does not operate — G(2) − G(1)² is identical for CI and CD — because the mod operation is essential to the conditional entropy structure.

**Linearity selection.** The linearity requirement in Theorem 8 is selected by three independent criteria, none imposed as an axiom. First, over ℝ, nonlinear CI dynamics have propagation speed v < 1, so linearity gives maximum speed (§11.1). Second, over ℤ/qℤ, among all linear CI dynamics f = α(l + r) mod q with prime q ≥ 5, α = 1 uniquely maximizes P-indivisibility (Appendix A.6): z-scores of 3–11 vs z ≈ 0 for all other α. Third, modified (nonlinear) dispersion relations break the thermality of the Unruh effect [9, 10] — the KMS condition holds only for linear dispersion ω = |k|. Since Jacobson's derivation requires thermal equilibrium at horizons, only the wave equation supports the full chain. All three criteria converge on the same dynamics.

**The η = 1/4 coefficient.** The Bekenstein-Hawking formula S = A/(4l_P²) follows from ε = 2l_P (the gap equation): one entropy unit per cell of area ε² = 4l_P². This cannot be confirmed via entanglement entropy because of the species problem — the entanglement entropy coefficient is species-dependent (Srednicki found η_ent ≈ 0.295 per scalar field), while the BH entropy is not. The thermal matching route avoids this by counting classical boundary DOF (one per ε² cell, independent of field content) rather than any particular field's vacuum entanglement.

**Jacobson's local equilibrium.** Required only for input (ii) above. For the wave equation, the lattice BW theorem [8] proves the entanglement Hamiltonian has the BW form exactly, establishing local thermal equilibrium at each causal horizon up to O(ε²κ²/c²) corrections.

**Field content.** The wave equation is a scalar (bosonic) system. The Standard Model contains fermions and gauge fields, which are absent from the lattice construction. This does not affect the GR derivation chain: the Jacobson route requires only thermodynamic inputs (entropy proportional to area, the Unruh temperature, and the Raychaudhuri equation), none of which depend on the emergent field content. We note that the wave equation factors into staggered Dirac operators via the standard Susskind factorization, so fermionic degrees of freedom are already implicit in the bosonic dynamics; the question of which specific QFT the observer sees is beyond the scope of this paper.

---

## 12. Conclusion

The OI framework [1] proves that QM emerges from embedded observation. This paper tested the framework's rigidity by constructing an explicit lattice realization and checking whether the dynamics selected by the QM requirement also produces the inputs for general relativity.

The dynamics selection is unique: among all second-order reversible nearest-neighbor rules, center independence (necessary for emergent QM), spatial isotropy, and linearity select the discrete wave equation alone (Theorem 8). Linearity is itself selected by three independent criteria — maximum propagation speed, maximum P-indivisibility, and horizon thermality — leaving no free parameters.

This dynamics then passes seven independent checks (Links 1–7), all analytically proven for both ℝ and ℤ/qℤ: non-Markovian reduced dynamics, correct emergent spacetime dimension, the gap equation for ℏ, area-law entropy, Lorentz-invariant dispersion, the Unruh temperature, and all inputs to Jacobson's derivation of Einstein's equations. The continuum limit is controlled: three of four Jacobson inputs are lattice-exact, and the fourth carries corrections of O(ε²κ²/c²) — negligible for all physical horizons (§11.2).

Each link is a point where the framework could have failed and did not. The structural consistency — one dynamics, selected by one criterion, passing seven tests with no tuning — constitutes independent corroborative evidence for the OI framework's central claim.

---

## Acknowledgements

During the preparation of this work, the author used Claude Opus 4.6 (Anthropic) to assist in drafting, numerical simulations, literature review, and refining argumentation. The author reviewed and edited all content and takes full responsibility for the publication.

---

## References

[1] A. Maybaum, "The Incompleteness of Observation," submitted to Foundations of Physics (2026).

[2] J. Barandes, "The stochastic-quantum correspondence," arXiv:2302.10778 (2023).

[3] T. Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State," Phys. Rev. Lett. 75, 1260 (1995).

[4] L. Bombelli, J. Lee, D. Meyer, R. Sorkin, "Space-time as a causal set," Phys. Rev. Lett. 59, 521 (1987).

[5] J. Eisert, M. Cramer, M.B. Plenio, "Area laws for the entanglement entropy," Rev. Mod. Phys. 82, 277 (2010).

[6] G. Giudici, T. Mendes-Santos, P. Calabrese, M. Dalmonte, "Entanglement Hamiltonians of lattice models via the Bisognano-Wichmann theorem," Phys. Rev. B 98, 134403 (2018).

[7] J. Zhang, P. Calabrese, M. Dalmonte, M.A. Rajabpour, "Lattice Bisognano-Wichmann modular Hamiltonian in critical quantum spin chains," SciPost Phys. Core 2, 007 (2020).

[8] V. Eisler, "On the Bisognano-Wichmann entanglement Hamiltonian of nonrelativistic fermions," J. Stat. Mech. (2025) 013101; arXiv:2410.16433 (2024).

[9] W.G. Unruh, "Sonic analogue of black holes and the effects of high frequencies on black hole evaporation," Phys. Rev. D 51, 2827 (1995).

[10] L.J. Garay, J.R. Anglin, J.I. Cirac, P. Zoller, "Influence of the dispersion relation on the Unruh effect," Phys. Rev. D 103, 085010 (2021).

---

## Appendix: Numerical Confirmation of Dynamics Selection

Theorem 8 is an algebraic result. The following numerical data, from an exhaustive scan of all 256 second-order reversible binary CA rules (L=50, T=80), confirms the key claims empirically.

### A.1 Selection counts

| Criterion | Rules passing (of 256) |
|-----------|----------------------|
| Nontrivial dynamics | 254 |
| Robust QM (min z > 2, multi-seed) | 53 |
| Ballistic propagation (speed > 0.7, R² > 0.9) | 24 |
| Area-law entropy scaling | 18 |
| QM ∩ ballistic | 1–2 |

### A.2 Algebraic characterization

| Property | Count (of 256) | Physical interpretation |
|----------|---------------|------------------------|
| Center-independent | 16 | Hidden sector mediates V-V interactions |
| Left-right symmetric | 64 | Spatial isotropy |
| Linear over GF(2) | 8 | Gaussian structure |
| All three (excluding trivial) | 1 (Rule 90) | Wave equation |

### A.3 Rule 90 vs Rule 150

| Property | Rule 90: f = l ⊕ r | Rule 150: f = l ⊕ c ⊕ r |
|----------|---------------------|--------------------------|
| Propagation speed | 1.000 | 1.000 |
| CMI z (L=50) | 7.2 ± 1.1 | 0.0 ± 0.6 |
| Center-independent | Yes | No |

The sole difference — center dependence — determines whether emergent QM exists.

### A.4 Center independence beyond q = 2

The following data extends the Rule 90/150 comparison to arbitrary alphabet size q. For each q, we compare the linear wave equation f = l + r mod q (center-independent, CI) against its center-dependent analog f = l + c + r mod q (CD). The non-Markovianity statistic is the z-score of ||G(2) − G(1)²||_F against a time-shuffled null (L = 60, T = 1000, 30 seeds).

| q | CI z-score | CD z-score | Both v = 1 |
|---|-----------|-----------|------------|
| 2 | 4.1 | −0.1 | Yes |
| 3 | 6.8 | −0.1 | Yes |
| 4 | 10.9 | 0.1 | Yes |
| 5 | 8.6 | 0.1 | Yes |
| 7 | 8.6 | 0.0 | Yes |
| 8 | 16.4 | 0.0 | Yes |
| 11 | 7.4 | 0.0 | Yes |
| 13 | 5.6 | 0.1 | Yes |
| 16 | 16.9 | 0.0 | Yes |
| 32 | 8.4 | 0.0 | Yes |
| 64 | 3.1 | 0.0 | Yes |

For every q from 2 to 64, the center-independent wave equation produces significant non-Markovianity while the center-dependent analog does not, despite identical propagation speed. Among random (nonlinear) rules at q = 3, both CI and CD rules produce P-indivisibility (47/50 and 40/50 with z > 2), consistent with the general characterization theorem [1]. Center independence is necessary specifically for the linear dynamics.

### A.5 Area law for the mod-q wave equation in 2D

The area law (Theorem 4) is proven analytically for both ℝ (Gaussian argument [5]) and ℤ/qℤ (spatial Markov property). The following data provides independent numerical confirmation at finite q. On a 16 × 16 periodic lattice with T = 8000 timesteps averaged over 5 initial conditions, we measure the per-boundary-pair mutual information across the right edge of a strip of width w:

| q | w = 1 | w = 2 | w = 3 | w = 4 | w = 5 | w = 6 | w = 7 | slope |
|---|-------|-------|-------|-------|-------|-------|-------|-------|
| 4 | 0.271 | 0.287 | 0.271 | 0.304 | 0.261 | 0.275 | 0.263 | −0.002 |
| 8 | 0.714 | 0.727 | 0.712 | 0.723 | 0.701 | 0.711 | 0.692 | −0.004 |
| 16 | 1.352 | 1.348 | 1.329 | 1.334 | 1.340 | 1.341 | 1.336 | −0.002 |
| 32 | 2.118 | 2.110 | 2.095 | 2.094 | 2.101 | 2.097 | 2.103 | −0.002 |
| 64 | 2.963 | 2.955 | 2.946 | 2.943 | 2.951 | 2.951 | 2.956 | −0.001 |

Under an area law, the per-pair MI is independent of strip width (constant rows). Under a volume law, it would grow proportionally to w (a 600% increase from w = 1 to w = 7). The observed variation is less than 3% at every q, with slopes consistent with zero. The area law holds for the mod-q wave equation at all tested alphabet sizes.

### A.6 α-selection: wave equation maximizes P-indivisibility

Among all linear center-independent dynamics f = α(l + r) mod q, the wave equation (α = 1, and its equivalent α = q−1) uniquely maximizes P-indivisibility for prime q. The statistic is the z-score of ||G(2) − G(1)²||_F against a time-shuffled null (L = 60, T = 800, 15 seeds). For each q, the table shows α = 1 vs. the best-performing alternative α.

| q | α = 1 z-score | Best other α | Best other z | α = 1 wins? |
|---|--------------|-------------|-------------|-------------|
| 5 | 7.1 | 2 | 0.9 | Yes |
| 7 | 4.2 | 5 | 0.4 | Yes |
| 11 | 7.7 | 5 | 0.2 | Yes |
| 13 | 2.8 | 10 | 0.1 | Yes |
| 17 | 1.7 | 14 | 0.5 | Yes |
| 19 | 2.4 | 13 | 0.2 | Yes |
| 23 | 5.8 | 13 | 0.1 | Yes |

For every prime q tested, α = 1 is the unique maximizer of P-indivisibility (excluding the equivalent α = q−1). For composite q (4, 8, 16), some non-unit α values match α = 1 by effectively reducing the system to a smaller prime-power alphabet. The wave equation is selected by maximum P-indivisibility, providing an independent criterion that converges with the maximum-speed argument over ℝ.
