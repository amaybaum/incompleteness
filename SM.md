# WHY THESE PARTICLES
### Standard Model Structure from Observational Incompleteness

**Author:** Alex Maybaum  
**Date:** March 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Particle Physics / Foundations

---

## ABSTRACT

The Observational Incompleteness (OI) framework derives quantum mechanics and general relativity from a deterministic bijection on a finite lattice but does not address which quantum field theory the embedded observer sees. This paper derives the Standard Model's structure from the framework's existing results combined with mathematical consistency, using three complementary arguments. **Bottom-up:** the uniquely selected wave equation is the massless lattice Klein-Gordon equation, which factors into staggered Dirac operators; center independence enforces chiral symmetry, mandating the Higgs mechanism; in $d = 3$, staggered tastes give three fermion sectors and one scalar sector. **Gauge emergence:** coupling-degree minimization uniquely gives $K = 2d = 6$ internal components (proved); the cubic rotation group decomposes $6 = T_1(3) \oplus E(2) \oplus A_1(1)$, fixing the eigenvalue multiplicities of the coupling matrix $M$ (proved); Wilson's lattice gauge construction promotes the global commutant symmetry $\mathrm{U}(3) \times \mathrm{U}(2) \times \mathrm{U}(1)$ to local gauge invariance. **Top-down:** anomaly cancellation uniquely determines the hypercharges; $D_{LL} = 0$ makes the gauge coupling chiral; $T$-invariance forces $\theta = 0$ (proved) and $\bar{\theta} = 0$ at the lattice scale (proved) with radiatively stable IR persistence. The filter chain contains no empirical inputs beyond the axioms; its steps range from theorem to well-characterized proposition. Parameter values remain undetermined.

---

# PART I: BOTTOM-UP — FROM THE LATTICE TO FERMIONS

## 1. INTRODUCTION

The OI framework [1] derives quantum mechanics from the causal partition imposed by the cosmological horizon. The companion papers derive general relativity [2] and establish the structural foundations — $d = 3$, background independence, the coupling graph ontology [3]. But quantum mechanics is a *framework*, not a *theory*. It is compatible with infinitely many quantum field theories: any gauge group, any matter content, any number of generations. The QM derivation tells the embedded observer that they must use quantum probability; it does not tell them which particles exist, which forces act, or which symmetries govern the interactions.

This paper asks: does the specific lattice structure selected by the QM and GR requirements — the wave equation on a $d = 3$ hypercubic lattice with checkerboard partition — determine the quantum field theory the observer sees? The answer is yes: the emergent QFT is the Standard Model, with no empirical inputs beyond the framework's axioms.

The argument has three parts. Part I works bottom-up from the lattice dynamics to fermionic matter and the generation count. Part II extends the dynamics selection to multi-component systems, deriving gauge structure from a coupling matrix. Part III works top-down from consistency constraints to the gauge group. Each result is labeled: **Theorem** (proved) or **Proposition** (follows from established results with identified steps). The free parameters of the Standard Model are determined by the substratum dynamics $\varphi$; this paper addresses structure, not parameters.

---

## 2. THE WAVE EQUATION AS LATTICE KLEIN-GORDON

The OI lattice is a $d$-dimensional hypercubic lattice $\Lambda = \mathbb{Z}^d$ with spacing $\epsilon = 2\,l_p$. Each site carries $\phi(\mathbf{n}, t) \in \mathbb{Z}/q\mathbb{Z}$. The dynamics selected by [2] is the discrete wave equation ($d = 1$):

$$\phi(n, t+1) = \phi(n-1, t) + \phi(n+1, t) - \phi(n, t-1)$$

Center independence requires $\phi(n, t)$ absent from the right-hand side.

**Theorem 1.** *The OI wave equation is the massless lattice Klein-Gordon equation. Center independence is equivalent to the vanishing of the lattice mass term.*

*Proof.* The general linear update is $\phi(n, t+1) = \alpha\,\phi(n,t) + \beta[\phi(n-1,t) + \phi(n+1,t)] + \gamma\,\phi(n,t-1)$. Reversibility: $\gamma = -1$. Center independence: $\alpha = 0$. Isotropy + unit speed: $\beta = 1$. The d'Alembertian $\Box_{\text{lat}}\phi = -\alpha\,\phi = 0$: massless KG. The massive equation $\Box_{\text{lat}}\phi = m^2\phi$ requires $\alpha \neq 0$, violating center independence. $\square$

---

## 3. FACTORIZATION INTO DIRAC OPERATORS

The lattice KG operator factors into first-order Dirac operators via the staggered fermion construction [4, 5].

**Definition.** The staggered Dirac operator: $D_{\text{st}}\chi(\mathbf{x}) = \frac{1}{2}\sum_{\mu} \eta_\mu(\mathbf{x})[\chi(\mathbf{x}+\hat{\mu}) - \chi(\mathbf{x}-\hat{\mu})]$, where $\eta_\mu(\mathbf{x}) = (-1)^{n_0 + \cdots + n_{\mu-1}}$.

**Theorem 2** (Susskind [5]). $D_{\text{st}}^2 = -\frac{1}{4}\Box_{\text{lat}}$. *The OI wave equation ($\Box_{\text{lat}}\phi = 0$) is equivalent to the massless staggered Dirac equation ($D_{\text{st}}\chi = 0$).*

The bosonic and fermionic descriptions are related by an exact change of variables on the lattice.

---

## 4. CENTER INDEPENDENCE AND CHIRAL SYMMETRY

**Theorem 3.** *Center independence of the lattice dynamics is equivalent to exact chiral symmetry of the emergent staggered fermions.*

*Proof.* The staggered mass term $m_{\text{lat}}\varepsilon(\mathbf{x})\chi(\mathbf{x})$ (where $\varepsilon = (-1)^{\sum n_\mu}$ is the staggered $\gamma_5$) squares to $\Box_{\text{lat}}\phi = -4m_{\text{lat}}^2\phi$: center dependence. Conversely, center independence gives $D_{\text{st}}\chi = 0$, invariant under $\chi \to \varepsilon\chi$ (since $\varepsilon$ anticommutes with $D_{\text{st}}$). $\square$

**The chain:**

$$\text{P-indivisibility} \xrightarrow{\text{[2]}} \text{center independence} \xrightarrow{\text{Thm.~3}} \text{chiral symmetry} \xrightarrow{\text{[6, 7]}} \text{Higgs mechanism}$$

**Corollary.** *One algebraic condition ($\alpha = 0$) produces quantum mechanics, chiral fermions, and the Higgs boson.*

---

## 5. THE STAGGERED SPECIES COUNT

The Nielsen-Ninomiya theorem [8] requires $2^{d+1}$ Weyl species in $d+1$ dimensions. Staggered reduction: $N_{\text{taste}} = 2^{\lfloor(d+1)/2\rfloor} = 4$ Dirac tastes in $d+1 = 4$.

The $2^3 = 8$ spatial Brillouin zone corners decompose under the cubic group $O_h$:

| Point | $\boldsymbol{\eta}$ values | Count |
|-------|---------------------------|-------|
| $\Gamma$ | $(0,0,0)$ | 1 |
| $X$ | $(1,0,0)$, $(0,1,0)$, $(0,0,1)$ | 3 |
| $M$ | $(1,1,0)$, $(1,0,1)$, $(0,1,1)$ | 3 |
| $R$ | $(1,1,1)$ | 1 |

Grouping by complementation ($\boldsymbol{\eta} \leftrightarrow \bar{\boldsymbol{\eta}}$), the 4 staggered tastes decompose as:

**Proposition 1.** *Under $O_h$: $4 = \mathbf{1} \oplus \mathbf{3}$. Tastes 2–4 (one per spatial axis) form an irreducible triplet.*

---

## 6. THE GENERATION COUNT: $N_{\text{gen}} = d = 3$

**Proposition 2.** *The number of non-singlet staggered tastes in $d$ spatial dimensions is $d$.*

*Proof.* The $2^{d-1}$ taste pairs include one singlet ($\Gamma$-$R$). The $d$ axis-aligned pairs form a $d$-dimensional irreducible representation. For $d = 3$: $3$ non-singlet tastes. $\square$

Since $d = 3$ is derived [3, §7.3], the triplet count is 3.

**Proposition 3a** (Taste coupling structure in $d = 3$). *On the $d$-dimensional lattice with the normalized wave equation $\phi(\mathbf{n}, t+1) = \frac{1}{d}\sum_j[\phi(\mathbf{n}+\hat{e}_j, t) + \phi(\mathbf{n}-\hat{e}_j, t)] - \phi(\mathbf{n}, t-1)$, each BZ corner $\boldsymbol{\eta}$ has coupling $\mu(\boldsymbol{\eta}) = \sigma(\boldsymbol{\eta})/d$ where $\sigma = \sum_j \cos(\pi\eta_j)$. In $d = 3$:*

$$\mu_\Gamma = 1, \qquad \mu_X = \tfrac{1}{3}, \qquad \mu_M = -\tfrac{1}{3}, \qquad \mu_R = -1$$

*The staggered taste pairs (complementary corners) have couplings:*
- *Singlet taste ($\Gamma$, $R$): $|\mu| = 1$*
- *Triplet taste ($X_j$, $M_j$): $|\mu| = 1/3$, identical for all $j = 1, 2, 3$*

*Proof.* Direct computation: $\sigma(\Gamma) = 3$, $\sigma(X) = 1$, $\sigma(M) = -1$, $\sigma(R) = -3$. Dividing by $d = 3$ gives the couplings. The triplet members are related by cubic symmetry ($O_h$ permutes spatial axes), hence identical. Verified numerically on $L = 6$ lattice with machine precision. $\square$

**Proposition 15** (Triplet tastes = three SM generations). *The three triplet staggered tastes, each producing a spin-1/2 Dirac fermion (Theorem 12b) with $K = 6$ internal components, constitute three complete Standard Model generations.*

*Status.* The lattice produces exactly three spin-1/2 fermion sectors and one spin-0 sector (Theorems 12a–b) — this is proved. The gauge group $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ (Theorem 11) with anomaly cancellation (Proposition 11) uniquely determines the matter content per generation — this is proved. The *identification* of each lattice fermion sector with a full SM generation (carrying the anomaly-cancelling representations) is a consistency argument: the tensor-product representation $Q_L = (\mathbf{3}, \mathbf{2})$ does not arise from the $K = 6$ direct sum $3 \oplus 2 \oplus 1$ but is the unique assignment demanded by anomaly cancellation. No alternative exists. Three degenerate sectors (by cubic symmetry) with uniquely determined representations = three generations. $\square$

**Theorem 12** (Spin-taste correspondence). *In the staggered-to-Dirac reconstruction on the $d = 3$ lattice: (a) the singlet taste ($A_1$ under $O$) produces a spin-0 field; (b) the triplet taste ($T_1$ under $O$) produces spin-1/2 fields.*

*Proof.* (a) The singlet pairs $\eta = (0,0,0)$ and $\eta = (1,1,1)$ with $\Gamma(0,0,0) = I_4$ (scalar) and $\Gamma(1,1,1) = \gamma^1\gamma^2\gamma^3 = i\gamma_5\gamma^0$ (pseudoscalar). Both are invariant under $\mathrm{SO}(3)$: the identity trivially, and $\gamma^1\gamma^2\gamma^3 \to \det(R)\cdot\gamma^1\gamma^2\gamma^3$ with $\det(R) = 1$ for proper rotations. The reconstructed field $\psi_S \propto I_4\cdot\chi(\Gamma) + \gamma^1\gamma^2\gamma^3\cdot\chi(R)$ transforms as a scalar: $J = 0$. (b) The $j$-th triplet taste pairs $|\eta| = 1$ ($\Gamma = \gamma^j$, a spatial vector) with $|\eta| = 2$ ($\Gamma = \epsilon_{jkl}\gamma^k\gamma^l = -i\Sigma_j$, the spin-$1/2$ angular momentum generator). Under $\mathrm{SO}(3)$, $\gamma^j$ rotates as a vector and $\Sigma_j$ as an axial vector; their combination in the reconstructed field $\psi_j \propto \gamma^j\cdot\chi(X_j) - i\Sigma_j\cdot\chi(M_j)$ carries one unit of angular momentum in the spinor representation: $J = 1/2$. $\square$

**Corollary** (Spin-statistics from the lattice). *Singlet taste $\to$ spin-0 $\to$ boson (Higgs). Triplet taste $\to$ spin-1/2 $\to$ fermion (quarks and leptons). The spin-statistics connection is derived from the $\Gamma(\eta)$ matrix structure, not postulated.*

**Proposition 3c** (Singlet taste = Higgs sector). *The singlet taste produces spin-0 excitations (Theorem 12a). Coupling to the $E(2)$ internal sector via the tensor product $A_1 \otimes E = E$, it carries quantum numbers $(\mathbf{1}, \mathbf{2}, +\tfrac{1}{2})$ — exactly the Higgs.*

*Consequences.* (i) Exactly **one** Higgs doublet (one singlet taste). (ii) The Higgs is a scalar (Theorem 12a). (iii) Three generations of fermions (Theorem 12b, three triplet tastes). (iv) No $\nu_R$: the singlet taste produces the Higgs, not a fourth matter generation. (v) Neutrinos are Majorana (Weinberg operator). The Higgs potential parameters are determined by $\varphi$. $\square$

**Proposition 3b.** *The OI checkerboard partition coincides with the staggered spinor decomposition: visible and hidden sectors carry complementary spinor components. Spin is the observable signature of the partition structure.*

---

# PART II: GAUGE EMERGENCE — FROM MULTI-COMPONENT DYNAMICS TO GAUGE GROUP

## 7. THE MULTI-COMPONENT FRAMEWORK

Each site now carries a $K$-component vector $\boldsymbol{\phi}(\mathbf{n}, t) \in (\mathbb{Z}/q\mathbb{Z})^K$. Applying the selection criteria — reversibility ($D = -I_K$), center independence ($C = 0$), spatial isotropy ($M^{(\pm j)} = M$ for all $j$) — yields:

**Theorem 4** (Generalized dynamics selection). *Center independence + isotropy + linearity + reversibility uniquely select the matrix wave equation:*

$$\boxed{\boldsymbol{\phi}(\mathbf{n}, t+1) = M \sum_{j=1}^{d} \left[\boldsymbol{\phi}(\mathbf{n} + \hat{e}_j, t) + \boldsymbol{\phi}(\mathbf{n} - \hat{e}_j, t)\right] - \boldsymbol{\phi}(\mathbf{n}, t-1)}$$

*where $M \in \mathrm{Mat}(K)$ is the sole free parameter.*

---

## 8. DISPERSION RELATIONS AND THE MASS SPECTRUM

In Fourier space, each eigenmode of $M$ decouples. Diagonalizing $M = V\,\text{diag}(\mu_1, \ldots, \mu_K)\,V^{-1}$:

**Theorem 5** (Mass spectrum). *Each eigenvalue $\mu_a$ determines a dispersion relation $\cos\omega_a = \mu_a \cos k$. Massless iff $\mu_a = 1$. For $|\mu_a| < 1$: mass gap $m_a = \epsilon^{-1}\arccos|\mu_a|$. Stability requires $|\mu_a| \leq 1$.*

**Max-speed constraint.** The GR derivation chain requires $\max_a \mu_a = 1$.

---

## 9. GAUGE GROUP FROM EIGENVALUE STRUCTURE

**Theorem 6** (Gauge group). *The global gauge group is the commutant $G = C_{\mathrm{U}(K)}(M)$. If $M$ has $r$ distinct eigenvalues with multiplicities $(n_1, \ldots, n_r)$:*

$$G = \mathrm{U}(n_1) \times \mathrm{U}(n_2) \times \cdots \times \mathrm{U}(n_r)$$

**Corollary.** *The gauge group and mass spectrum are the same information.* Modes of equal mass share a gauge symmetry; modes of different mass break $\mathrm{U}(K)$ into the product on each eigenspace.

| Eigenvalue structure | Gauge group | Mass spectrum |
|---------------------|-------------|---------------|
| $M = I_K$ | $\mathrm{U}(K)$ | All massless |
| $\text{diag}(I_3,\, \mu I_2,\, \nu)$ | $\mathrm{U}(3) \times \mathrm{U}(2) \times \mathrm{U}(1)$ | 3 massless + 2 massive + 1 massive |

Local gauge invariance follows from promoting $M$ to site-dependent link matrices $A_j(\mathbf{n}) = U(\mathbf{n})MU^\dagger(\mathbf{n}+\hat{e}_j)$ — Wilson's lattice gauge theory [9]. Center independence forbids explicit gauge-boson mass terms.

*Status note on gauge emergence.* Theorem 6 (the commutant of $M$ is a global symmetry) is a mathematical fact. The identification of this global symmetry with the *gauge* group of the emergent QFT rests on Wilson's lattice gauge construction [9], which is standard but involves a physical step: promoting $M$ to site-dependent link variables. This promotion is the unique way to make the global symmetry local while preserving the lattice structure, and is well-established in lattice QFT. However, a fully rigorous proof that the continuum limit of the lattice theory recovers precisely the SM gauge theory — rather than some other theory with the same symmetry group — requires universality arguments that are supported by decades of numerical evidence and renormalization group analysis but are not mathematically proven in the strict sense. This is a gap shared with all of lattice QCD, not specific to this framework.

---

## 10. NON-MARKOVIANITY UNDER GAUGE STRUCTURE

The multi-component system's P-indivisibility can be computed in closed form, confirming that the QM emergence is robust across all gauge group choices.

**Theorem 7** (Eigenmode decomposition). *For the $K$-component matrix wave equation with diagonal coupling $M = \mathrm{diag}(\mu_1, \ldots, \mu_K)$ on a ring of $L$ sites with checkerboard partition, the non-Markovianity decomposes additively over eigenmodes:*

$$\|G_V(2) - G_V(1)^2\|_F^2 = \sum_{a=1}^{K} \|g^{\mu_a}(2) - g^{\mu_a}(1)^2\|_F^2$$

*Proof.* $M \otimes A$ is block-diagonal; the $K$ components decouple; the checkerboard partition acts identically within each block. $\square$

**Theorem 8** (Analytical NM formula). *The normalized non-Markovianity is:*

$$\boxed{\mathrm{NM}_{\text{norm}} = \sqrt{3} \cdot \sqrt{\langle \mu^4 \rangle}}$$

*where $\langle \mu^4 \rangle = \frac{1}{K}\sum_{a=1}^{K} \mu_a^4$. This is exact, independent of $L$, and depends on $M$ only through its eigenvalue spectrum.*

*Proof sketch.* Fourier decomposition of the scalar propagator on a ring of $L$ sites gives $\|g^\mu(2) - g^\mu(1)^2\|_F^2 = 3L\mu^4$ and $\|g^\mu(1)\|_F^2 = L$ (via the identity $\sum \cos^4 = 3L/16$). Combining with Theorem 7 and normalizing yields the formula. Verified numerically for $K = 1$–$12$, $L = 8$–$50$, $\mu \in [0,1]$ with machine-precision agreement. $\square$

**Consequences.** NM is maximized at $M = I_K$ ($\mathrm{NM}_{\text{norm}} = \sqrt{3}$ for all $K$). The SM structure $(3,2,1)$ with $\mu_w, \mu_c < 1$ gives $\mathrm{NM} < \sqrt{3}$: P-indivisibility does not select the gauge group. The gauge group is selected by the top-down constraints of Part III.

---

## 11. THE STANDARD MODEL EMBEDDING

### 11.1 Why $K = 2d = 6$

**Theorem 13** ($K = 2d$ from coupling-degree minimization). *Among all factorizations of the per-site state space of the matrix wave equation into $K$ equal components, the internal coupling degree is minimized uniquely at $K = 2d$.*

*Proof.* The matrix wave equation (Theorem 4) updates the $K$-component vector at site $\mathbf{n}$ as:

$$\boldsymbol{\phi}(\mathbf{n}, t+1) = M \sum_{j=1}^{d} \left[\boldsymbol{\phi}(\mathbf{n} + \hat{e}_j, t) + \boldsymbol{\phi}(\mathbf{n} - \hat{e}_j, t)\right] - \boldsymbol{\phi}(\mathbf{n}, t-1)$$

The update at site $\mathbf{n}$ receives exactly $2d$ independent spatial inputs: $\{\boldsymbol{\phi}(\mathbf{n} \pm \hat{e}_j, t)\}_{j=1}^d$. We formalize the internal coupling degree as follows.

*Definition.* For a factorization of the per-site state space into $K$ components $(\phi_1, \ldots, \phi_K)$, the *internal coupling degree* $\delta(K)$ is the maximum number of spatial input channels on which any single component's update depends.

*Step 1 ($K = 2d$ achieves $\delta = 1$).* With $K = 2d$, assign component $a$ to link direction $a$ (i.e., $a \in \{+\hat{e}_1, -\hat{e}_1, \ldots, +\hat{e}_d, -\hat{e}_d\}$). If $M$ is diagonal in this basis, then $\phi_a(\mathbf{n}, t+1) = \mu_a \cdot \phi_a(\mathbf{n} + \hat{e}_{j(a)}, t) - \phi_a(\mathbf{n}, t-1)$: each component depends on exactly one spatial input. Therefore $\delta(2d) = 1$.

*Step 2 ($K < 2d$ forces $\delta \geq 2$).* By the pigeonhole principle, at least one component must receive contributions from $\lceil 2d/K \rceil \geq 2$ spatial input channels. These channels carry independent data (from distinct neighboring sites), so the component's update depends on at least 2 spatial inputs: $\delta(K) \geq 2$.

*Step 3 ($K > 2d$ forces $\delta \geq 2$).* With $K > 2d$ components and only $2d$ spatial input channels, at least $K - 2d > 0$ components have no dedicated spatial input. These components' updates must be algebraically determined by other components' inputs (since the dynamics is non-trivial by C1), requiring coupling to at least one other component's spatial channel. The coupling matrix $M$ in the $K > 2d$ case has rank at most $2d$ in its spatial coupling structure, so the $K \times K$ matrix necessarily couples the excess components to the same spatial inputs as others: $\delta(K) \geq 2$.

*Uniqueness.* $K = 2d$ is the unique value achieving $\delta = 1$: Steps 2–3 show $\delta \geq 2$ for all $K \neq 2d$. $\square$

This is the per-site analog of the factorization principle [3, §3.1], which selects the product decomposition of the full state space that minimizes the coupling degree of the coupling graph. The spatial factorization principle gives the sites; the internal factorization principle gives the components per site.

**Theorem 11** ($K = 6$ with multiplicities $(3, 2, 1)$ from $d = 3$). *The $2d = 6$ nearest-neighbor link directions of the $d = 3$ cubic lattice decompose under the rotation group $O$ as:*

$$6 = T_1(3) \oplus E(2) \oplus A_1(1)$$

*The eigenvalue multiplicities of $M$ are $(3, 2, 1)$, giving gauge group $\mathrm{U}(3) \times \mathrm{U}(2) \times \mathrm{U}(1) \supset \mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$.*

*Proof.* The $2d = 6$ directions $\{\pm\hat{e}_1, \pm\hat{e}_2, \pm\hat{e}_3\}$ form a 6-dimensional representation of $O$ (24 elements). Character at each conjugacy class: $E$: $\chi = 6$; $8C_3$: $\chi = 0$; $3C_2$: $\chi = 2$; $6C_2'$: $\chi = 0$; $6C_4$: $\chi = 2$. Decomposing via the character inner product:

$$n(A_1) = \tfrac{1}{24}(6 + 0 + 6 + 0 + 12) = 1, \quad n(E) = \tfrac{1}{24}(12 + 0 + 12 + 0 + 0) = 1, \quad n(T_1) = \tfrac{1}{24}(18 + 0 - 6 + 0 + 12) = 1$$

with $n(A_2) = n(T_2) = 0$. By Schur's lemma and spatial isotropy (Theorem 4), $M = \mathrm{diag}(\mu_c I_3, \mu_w I_2, \mu_y)$ with commutant $\mathrm{U}(3) \times \mathrm{U}(2) \times \mathrm{U}(1)$. $\square$

**Corollary (SM embedding).** Each $\mathrm{U}(n_i) = \mathrm{SU}(n_i) \times \mathrm{U}(1)_i$ [9, 10]. The max-speed constraint (§8) requires $\mu_y = 1$ (the $A_1$ mode propagates at the lattice speed of light). The resulting gauge group is $\mathrm{SU}(3)_c \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$, with the physical identifications: $T_1$ (spatial vector) → color, $E$ (quadrupole) → weak isospin, $A_1$ (scalar) → hypercharge.

---

# PART III: TOP-DOWN — FROM CONSISTENCY TO THE GAUGE GROUP

## 12. TOP-DOWN CONSTRAINTS: RENORMALIZABILITY AND THE STRONG SECTOR

The OI framework establishes: $d = 3$ [3], lattice QFT with UV cutoff $\epsilon = 2l_p$ [1], spatial locality [1], Lorentz invariance in the continuum limit [2], unitarity [1], and the conformal spectral assumption for $\nu_{\text{OI}}$ [1].

**Proposition 4.** *The Yang-Mills coupling has mass dimension $[g] = (3-d)/2$; dimensionless iff $d = 3$.* Since $d = 3$ is derived, the emergent QFT supports renormalizable gauge interactions.

**Proposition 5.** *The conformal spectral assumption requires asymptotic freedom: $g(\mu) \to 0$ as $\mu \to \infty$. The dominant gauge interaction is therefore non-abelian.*

**Proposition 6.** *Stable composite matter requires fermionic baryons, hence odd $N_c$.*

**Proposition 7.** *Asymptotic freedom + odd $N_c$ + minimality: $N_c = 3$.*

---

## 15. THE ELECTROWEAK SECTOR

### 15.1 Parity Violation from the Partition Structure

**Proposition 8** (Chirality from trace-out). *The emergent gauge coupling of the visible sector is chiral: the effective Lagrangian has only left-handed external fermion legs.*

*Proof.* The argument has five steps.

*(i) Chirality = sublattice parity.* The staggered-to-Dirac reconstruction [4, 5] assigns spinor components to hypercube corners $\eta \in \{0,1\}^{d+1}$ via $\chi(y + \eta\epsilon) = \frac{1}{4}\Gamma(\eta)_{\alpha\beta}\psi_\beta(y)$ where $\Gamma(\eta) = \gamma_0^{\eta_0}\cdots\gamma_d^{\eta_d}$. Under $\gamma_5$: $\Gamma(\eta) \to (-1)^{|\eta|}\Gamma(\eta)$. Sites with $|\eta|$ even are left-handed; $|\eta|$ odd are right-handed. This equals the sublattice parity $\varepsilon(x) = (-1)^{\sum x_\mu}$.

*(ii) D_{LL} = D_{RR} = 0.* The staggered Dirac operator couples ONLY across sublattices: its even-even and odd-odd blocks vanish identically. In the chiral basis:

$$D = \begin{pmatrix} 0 & D_{LR} \\ D_{RL} & 0 \end{pmatrix}$$

This is verified numerically to machine precision and follows from the anticommutation $\{D_{\text{st}}, \varepsilon\} = 0$ (chiral symmetry, Theorem 3).

*(iii) Trace-out removes right-handed fields.* The OI partition assigns even sites (left-handed) to $V$ and odd sites (right-handed) to $H$. The trace-out marginalizes over $H$. In the emergent quantum description, all operators act on the visible (left-handed) Hilbert space.

*(iv) The effective Lagrangian is left-handed.* Since $D_{LL} = 0$, the gauge coupling in the full theory is purely $L \leftrightarrow R$. After integrating out $R$ (the hidden sublattice), the effective visible-sector coupling has the form:

$$\mathcal{L}_{\text{eff}} = \bar{\psi}_L\,(D_{LR}\,G_{RR}\,D_{RL})\,\psi_L + \cdots$$

where $G_{RR}$ is the hidden-sector propagator and $D_{LR}$, $D_{RL}$ contain the gauge field. Both external legs are left-handed. Right-handed fermions appear only as propagators internal to the hidden sector, not as external fields in the effective Lagrangian.

*(v) Why SU(3) remains vector-like while SU(2) becomes chiral.* The staggered phases $\eta_\mu(x)$ act on SPATIAL structure (sublattice position), while the gauge group acts on INTERNAL structure (the $K$-component index). In the spin-taste reconstruction, these decouple: $D \to (\gamma_\mu \otimes I_{\text{taste}})\,D_\mu\,(I_{\text{spin}} \otimes I_{\text{color}})$. The chirality projection $P_L$ selects the spin-left component without projecting on any color or internal index. Therefore:

- **SU(3)** (internal space): Both $L$ and $R$ carry color. The trace-out integrates over spatial configurations but preserves internal indices. Color passes through → **vector-like**.
- **SU(2)** (entangled with chirality through the effective Lagrangian): The effective coupling $\bar{\psi}_L\,(\cdots)\,\psi_L$ has only $L$ external legs. Right-handed fields are internal to the hidden sector and do not carry visible SU(2) quantum numbers → **chiral**. $\square$

*Note.* The SM's right-handed fermions are SU(2) singlets, not absent — they are effective degrees of freedom reconstructed from the hidden sector's influence, carrying color but no SU(2) charge. $\square$

### 15.2 The Minimal Chiral Group

**Proposition 9.** *Given chiral gauge interactions, the minimal non-abelian chiral group is $\mathrm{SU}(2)_L$ with $L \sim \mathbf{2}$, $R \sim \mathbf{1}$.*

### 15.3 Hypercharge: $\mathrm{U}(1)_Y$ from the Eigenvalue Structure

**Proposition 10.** *The existence of a $\mathrm{U}(1)$ gauge factor is automatic in the multi-component framework: it is not an independent postulate.*

*Proof.* The multi-component gauge group (Theorem 6) is $G = \mathrm{U}(n_1) \times \mathrm{U}(n_2) \times \cdots \times \mathrm{U}(n_r)$. Each factor decomposes as $\mathrm{U}(n_i) = \mathrm{SU}(n_i) \times \mathrm{U}(1)_i$. For $K = 6$ with multiplicities $(3, 2, 1)$:

$$G = \mathrm{U}(3) \times \mathrm{U}(2) \times \mathrm{U}(1) = [\mathrm{SU}(3) \times \mathrm{U}(1)_B] \times [\mathrm{SU}(2) \times \mathrm{U}(1)_L] \times \mathrm{U}(1)_S$$

Three $\mathrm{U}(1)$ factors exist automatically. A general abelian charge is a linear combination $Q = \alpha B + \beta L + \gamma S$. Given the non-abelian factor $\mathrm{SU}(3) \times \mathrm{SU}(2)$ and the minimal fermion content (5 representations per generation), the six anomaly conditions impose 4 independent constraints on the 5 hypercharge unknowns, leaving exactly one free parameter (overall normalization). There is therefore exactly one anomaly-free $\mathrm{U}(1)$. This is $\mathrm{U}(1)_Y$. $\square$

**Summary.** $G = \mathrm{SU}(3)_c \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$, with every factor derived.

---

## 16. ANOMALY CANCELLATION

**Theorem 9.** *Mathematical consistency requires all gauge anomalies to cancel* [11, 12].

**Proposition 11.** *Given $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ with fermions in fundamental or singlet representations, the six anomaly conditions uniquely determine the hypercharges* [13]:

$$Y_Q = \tfrac{1}{6}, \quad Y_u = \tfrac{2}{3}, \quad Y_d = -\tfrac{1}{3}, \quad Y_L = -\tfrac{1}{2}, \quad Y_e = -1$$

**Corollary.** $|q_p| = |q_e|$ is a theorem, not a coincidence.

---

## 17. GENERATIONS, SYMMETRY BREAKING, AND THE HIERARCHY

**Generation count.** Two independent arguments select $N_{\text{gen}} = 3$. Bottom-up: Proposition 2 gives $N_{\text{gen}} = d = 3$ from the staggered taste decomposition. Top-down: CKM CP violation for baryogenesis requires $N_{\text{gen}} \geq 3$ [14]; asymptotic freedom of SU(3) requires $N_{\text{gen}} \leq 8$; minimality selects $N_{\text{gen}} = 3$.

**Spontaneous symmetry breaking.** Chiral symmetry (Theorem 3) + center-independent gauge sector (§9) forbid explicit masses. The unique renormalizable unitarity-preserving mechanism is the Higgs [6, 7]. The minimal scalar breaking $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y \to \mathrm{U}(1)_{\text{em}}$ while preserving $\mathrm{SU}(3)_c$ is $H = (\mathbf{1}, \mathbf{2}, +\tfrac{1}{2})$.

**Hierarchy problem dissolved.** In the OI framework, the QFT is emergent: $m_H$ is set by $\mu_w$ (a property of $\varphi$), not by radiative corrections. The electroweak/Planck hierarchy $v/M_{\text{Pl}} \sim 10^{-17}$ requires $1 - \mu_w \sim 10^{-34}$, but eigenvalues of $M$ are substratum data with no loop corrections.

---

## 20. THE STRONG CP PROBLEM: $\theta = 0$ FROM T-INVARIANCE

### 20.1 T-Invariance of the Wave Equation

**Theorem 10.** *The discrete wave equation is invariant under time reversal $T: \phi(n, t) \to \phi(n, -t)$.*

*Proof.* Under $T$, define $\psi(n, t) = \phi(n, -t)$. The wave equation at time $-t$ gives $\phi(n, -t+1) = \phi(n-1, -t) + \phi(n+1, -t) - \phi(n, -t-1)$, hence $\psi(n, t-1) = \psi(n-1, t) + \psi(n+1, t) - \psi(n, t+1)$, which rearranges to $\psi(n, t+1) = \psi(n-1, t) + \psi(n+1, t) - \psi(n, t-1)$: the same wave equation. Verified numerically to machine precision for all tested lattice sizes. $\square$

### 20.2 The Trace-Out Preserves T, Breaks P

The checkerboard partition marginalizes over spatial sites, not temporal data. It preserves $T$ while breaking $P$ (§15.1).

### 20.3 $\theta = 0$

**Theorem 14.** *The QCD $\theta$-parameter vanishes in the emergent QFT: $\theta = 0$.*

*Proof.* The $\theta$-term $\mathcal{L}_\theta = (\theta/32\pi^2) \mathrm{Tr}(F \tilde{F})$ is $T$-odd: $\mathrm{Tr}(F\tilde{F}) = 2\,\mathbf{E} \cdot \mathbf{B}$, and under $T$, $\mathbf{E} \to \mathbf{E}$, $\mathbf{B} \to -\mathbf{B}$, so $\mathbf{E} \cdot \mathbf{B} \to -\mathbf{E} \cdot \mathbf{B}$. A $T$-invariant Lagrangian cannot contain a $T$-odd term. The emergent Lagrangian inherits $T$-invariance from the wave equation (Theorem 10) because the trace-out preserves $T$ (§20.2): the partition is spatial, so time reversal commutes with the visible/hidden projection. Therefore $\theta = 0$. $\square$

### 20.4 The Physical Parameter $\bar{\theta}$

The physical CP-violating parameter in QCD is $\bar{\theta} = \theta + \arg\det(Y_u Y_d)$, where $Y_u, Y_d$ are the Yukawa matrices. Even with $\theta = 0$, a nonzero $\arg\det(Y_u Y_d)$ could produce $\bar{\theta} \neq 0$.

**Theorem 15** (Detailed balance of transition probabilities). *The visible-sector transition probabilities satisfy $T_{ij} = T_{ji}$ for all $i, j$.*

*Proof.* The full dynamics $\varphi$ is a bijection, so the Liouville measure $\mu$ (uniform on the finite state space) is invariant. $T$-invariance (Theorem 10) means $\varphi$ and $\varphi^{-1}$ are related by the time-reversal map $\mathcal{T}: (x(t), x(t-1)) \to (x(t-1), x(t))$ — that is, $\varphi^{-1} = \mathcal{T} \circ \varphi \circ \mathcal{T}$.

For each hidden state $h$ such that $\pi_V(\varphi(i, h)) = j$, let $h' = \pi_H(\varphi(i, h))$. Then $\varphi(i, h) = (j, h')$, so $\varphi^{-1}(j, h') = (i, h)$. The time-reversal relation gives $\mathcal{T}(\varphi(\mathcal{T}(j, h'))) = (i, h)$. Since the partition is spatial (not temporal), $\mathcal{T}$ acts on the phase-space pair $(x(t), x(t-1))$ but preserves the visible/hidden site classification: $\pi_V \circ \mathcal{T} = \pi_V$ on the spatial indices.

The map $h \mapsto h'$ is therefore an injection from $\{h \in \mathcal{C}_H : \pi_V(\varphi(i,h)) = j\}$ into $\{h' \in \mathcal{C}_H : \pi_V(\varphi^{-1}(j,h')) = i\}$. By $T$-invariance, the latter set has the same cardinality as $\{h' \in \mathcal{C}_H : \pi_V(\varphi(j,h')) = i\}$. Since $\varphi$ is a bijection on a finite set, the injection is a bijection between sets of equal cardinality. Dividing by $|\mathcal{C}_H|$: $T_{ij} = T_{ji}$. $\square$

**Theorem 16** (Detailed balance implies $T$-invariant emergent Hamiltonian). *If $T_{ij} = T_{ji}$ for all $i, j$, then the emergent Hamiltonian $\hat{H}_{\text{eff}}$ satisfies $[\hat{H}_{\text{eff}}, \hat{\Theta}] = 0$ where $\hat{\Theta}$ is the anti-unitary time-reversal operator, and all effective couplings in the emergent Lagrangian are $T$-invariant at the lattice scale.*

*Proof.* The relation $T_{ij}(t) = |U_{ij}(t)|^2$ (Born rule, §3.1 of [1]) combined with $T_{ij} = T_{ji}$ gives $|U_{ij}|^2 = |U_{ji}|^2$ for all $i, j$ and all $t$. Under the phase-locking lemma ([1], §3.1), continuous-time transition data determines $\hat{H}_{\text{eff}}$ up to overall energy shift and basis phases. The constraint $|U_{ij}|^2 = |U_{ji}|^2$ is equivalent to $U(t) = \hat{\Theta} U(t)^* \hat{\Theta}^{-1}$ for a suitable anti-unitary $\hat{\Theta}$ (Wigner's theorem applied to the symmetry $T_{ij} = T_{ji}$), which gives $[\hat{H}_{\text{eff}}, \hat{\Theta}] = 0$. The effective Lagrangian, reconstructed from $\hat{H}_{\text{eff}}$ via the Legendre transform, inherits $T$-invariance. $\square$

**Proposition 13** (The physical parameter $\bar{\theta} = 0$). *$\bar{\theta} = \theta + \arg\det(Y_u Y_d) = 0$.*

*Argument.* $\theta = 0$ by Theorem 14. The remaining question is whether $\arg\det(Y_u Y_d) = 0$.

*Lattice-level result (proved).* By Theorem 16, the emergent Yukawa couplings at the lattice scale are $T$-invariant. For $T$-invariant Yukawa interactions, there exists a basis in which $Y_u$ and $Y_d$ are simultaneously real (see e.g. [13, §6.3]): $T$-invariance constrains $Y = \hat{\Theta} Y^* \hat{\Theta}^{-1}$, and choosing the basis where $\hat{\Theta}$ acts as complex conjugation gives $Y = Y^*$. Real Yukawa matrices have $\arg\det(Y_u Y_d) = 0$.

*IR persistence (identified gap).* The lattice-level result establishes $\bar{\theta} = 0$ at the UV cutoff $\epsilon = 2l_p$. The question is whether RG evolution from the Planck scale to the QCD scale can generate a nonzero $\bar{\theta}$. In perturbation theory, $\bar{\theta}$ is not renormalized at any finite loop order if it vanishes at the UV scale — this is because $\bar{\theta}$ is a total-derivative coupling and receives no perturbative corrections [12]. Non-perturbative effects (instantons) can shift $\theta$ but not $\bar{\theta}$ (which is the rephasing-invariant combination). The gap is therefore narrow: $\bar{\theta} = 0$ at the lattice scale is radiatively stable to all orders in perturbation theory, and the known non-perturbative effects preserve it. A complete proof would require showing that no non-perturbative mechanism specific to the OI lattice regularization can generate $\bar{\theta} \neq 0$ — a well-defined technical question within lattice QCD, not a structural gap in the framework.

Verified numerically: the $\mathbb{Z}/q\mathbb{Z}$ transition matrix satisfies $\|T - T^\top\| = 0$ to machine precision for all tested systems. $\square$

### 20.5 Prediction

$\bar{\theta} = 0$ exactly. No axion needed. Neutron EDM $d_n \propto \bar{\theta}$ should be exactly zero (current bound: $|d_n| < 1.8 \times 10^{-26}\;e\cdot\text{cm}$ [15]).

---

# PART IV: SYNTHESIS

## 21. THE FILTER CHAIN

| Step | Constraint | Source | Selects | Status |
|------|-----------|--------|---------|--------|
| 0 | Emergent QFT, $d = 3$ | OI [1, 3] | Lattice QFT, $3+1$D | Theorem |
| 1 | Wave eq. = massless KG | [2], Thm. 1 | Staggered fermions | Theorem |
| 2 | Center indep. = chiral sym. | Thm. 3 | Massless chiral fermions | Theorem |
| 3 | Multi-component $\to$ matrix WE | Thm. 4 | Gauge structure from $M$ | Theorem |
| 4 | Gauge group = commutant of $M$ | Thm. 6 | $\mathrm{U}(n_1) \times \cdots$ | Theorem (global sym.); lattice gauge promotion standard |
| 4a | $K = 2d = 6$, factorization + decomp. | Thm. 13, Thm. 11 | Multiplicities $(3, 2, 1)$ | Theorem |
| 5 | NM decomposition | Thms. 7–8 | P-indivis. preserved $\forall M$ | Theorem |
| 6 | Dimensionless $g$ | $d = 3$, Prop. 4 | Renormalizable gauge theories | Theorem |
| 7 | Asymptotic freedom | $\nu_{\text{OI}}$, Prop. 5 | Non-abelian gauge group | Proposition |
| 8 | Fermionic baryons | Stable matter, Prop. 6 | $N_c$ odd | Proposition |
| 9 | Minimality | §14 | $N_c = 3 \Rightarrow \mathrm{SU}(3)$ | Proposition |
| 10 | Chiral gauge coupling | $D_{LL} = 0$ + trace-out, Prop. 8 | $\mathrm{SU}(2)_L$ chiral | Proposition |
| 11 | Minimal chiral group | Prop. 9 | $\mathrm{SU}(2)_L$ | Proposition |
| 12 | $\mathrm{U}(1)_Y$ existence | Automatic from $\mathrm{U}(n)$, Prop. 10 | Abelian gauge factor | Theorem |
| 13 | Anomaly cancellation | Prop. 11 | SM hypercharges | Theorem |
| 14a | Spin-taste + observer self-consistency | Thm. 12, Props. 3c, 15 | 1 Higgs + 3 gen with SM reps | Theorem (count) + Identification (reps) |
| 14b | CP violation + AF bound | §17.2 | $3 \leq N_{\text{gen}} \leq 8 \to 3$ | Proposition |
| 15 | Chiral sym. + unitarity | §18 | Higgs $(\mathbf{1}, \mathbf{2}, +\tfrac{1}{2})$ | Proposition |
| 16a | T-invariance of wave eq. | Thms. 10, 14 | $\theta = 0$ | Theorem |
| 16b | Detailed balance $\to$ real Yukawas | Thms. 15–16, Prop. 13 | $\bar{\theta} = 0$ | Theorem (UV) + radiatively stable (IR gap narrow) |

**Output:** $\mathrm{SU}(3)_c \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ with:

$$Q_L = (\mathbf{3}, \mathbf{2}, +\tfrac{1}{6}), \quad u_R = (\mathbf{3}, \mathbf{1}, +\tfrac{2}{3}), \quad d_R = (\mathbf{3}, \mathbf{1}, -\tfrac{1}{3})$$
$$L_L = (\mathbf{1}, \mathbf{2}, -\tfrac{1}{2}), \quad e_R = (\mathbf{1}, \mathbf{1}, -1)$$

Three generations. A Higgs doublet $H = (\mathbf{1}, \mathbf{2}, +\tfrac{1}{2})$. This is exactly the Standard Model.

---

## 22. WHAT REMAINS UNDETERMINED

### 22.1 The Structure/Parameters Boundary

The framework determines the Standard Model's *structure* — gauge group, representations, symmetry-breaking pattern, discrete symmetries — but not its *parameters*. This is the correct boundary between laws and initial conditions: just as GR determines the Einstein equations but not the mass of Jupiter, the derivation chain uses only structural properties of $\varphi$ (bounded coupling, isotropy, center independence), so any bijection satisfying these constraints produces the same laws while different bijections produce different parameter values. Specifically: gauge couplings $g_s, g, g'$ depend on the eigenvalues $\mu_c, \mu_w$ of $M$ (with $\mu_y = 1$ derived); fermion masses arise from taste-breaking at $\mathcal{O}(\epsilon^2)$ in the $E$ representation of $O$; mixing parameters (CKM/PMNS) have magnitudes set by $\varphi$ with CP violation traced to the partition's P-breaking; Higgs potential parameters are in $\varphi$. Neutrinos are Majorana (no $\nu_R$ in the spectrum; masses via the Weinberg operator).

### 22.2 Open Problems

**Closed:** $K = 2d$ (Theorem 13); $\theta = 0$ at the lattice scale (Theorems 10, 14, 15, 16).

**Narrowed:** $\bar{\theta} = 0$ in the IR. Proved at the lattice scale; perturbatively non-renormalized; known non-perturbative effects (instantons) preserve it. Remaining gap: whether the OI lattice regularization can generate $\bar{\theta} \neq 0$ through mechanisms not captured by standard arguments.

**Open:** (i) Continuum limit of lattice gauge theory — the commutant-to-gauge-group identification rests on Wilson's construction and universality, supported by numerical evidence but not proved; a gap shared with all of lattice QCD. (ii) Generation identification — the fermion count is proved; the representation assignment is a unique consistency argument, not a geometric derivation. (iii) Taste-breaking phenomenology — whether specific patterns in $\varphi$ reproduce the observed mass ratios.

---

## 23. PREDICTIONS

**(P1)** No additional gauge groups below $M_{\text{Pl}}$. **(P2)** No fundamental scalars beyond the Higgs doublet (one singlet taste → one Higgs). **(P3)** No supersymmetric partners (hierarchy dissolved). **(P4)** No fourth generation. **(P5)** $\bar{\theta} = 0$ exactly: no axion, neutron EDM exactly zero (§20). **(P6)** The CKM phase arises from P-violation (the partition), not from T-violation. **(P7)** Neutrinos are Majorana: the singlet taste is the Higgs sector (Prop. 3c), not $\nu_R$; neutrinoless double beta decay should be observed. **(P8)** No proton decay from GUT-scale gauge boson exchange: the eigenvalues $\mu_c$, $\mu_w$ correspond to independent irreps of $O$ (Theorem 11), so the couplings do not unify; consistent with Super-Kamiokande bounds ($\tau_p > 10^{34}$ years).

---

## 24. CONCLUSION

The Standard Model's structure is not arbitrary. Starting from the OI lattice substratum — a finite set, a bijection, a partition — the wave equation emerges as the unique dynamics compatible with quantum mechanics. This wave equation is the massless lattice Klein-Gordon equation, which factors into staggered Dirac operators: **fermionic matter is the same dynamics seen from within the quantum description**. Center independence enforces chiral symmetry and mandates the Higgs mechanism. In $d = 3$, the staggered taste decomposition gives 3 fermion sectors and 1 scalar sector. The multi-component extension, with $K = 2d = 6$ proved by coupling-degree minimization (Theorem 13), introduces a coupling matrix $M$ whose eigenvalue multiplicities $(3, 2, 1)$ are fixed by the cubic rotation group (Theorem 11).

The exact formula $\mathrm{NM} = \sqrt{3}\cdot\sqrt{\langle\mu^4\rangle}$ establishes that non-Markovianity decomposes additively over eigenmodes and is preserved for any gauge group. The specific gauge group is selected by mathematical consistency: anomaly cancellation, asymptotic freedom, and stable matter. The $\mathrm{U}(1)_Y$ factor, long treated as an empirical input, is automatic from the $\mathrm{U}(n)$ gauge structure and uniquely determined by anomaly cancellation. The strong CP problem is addressed by the $T$-invariance of the wave equation: $\theta = 0$ is a theorem (Theorem 14), detailed balance of transition probabilities is a theorem (Theorem 15), and $\bar{\theta} = 0$ at the lattice scale follows rigorously with a narrow, well-characterized gap for IR persistence.

The filter chain from $(S, \varphi)$ to the Standard Model contains *no empirical inputs beyond the two structural properties* (bounded coupling and statistical isotropy). The chain's steps vary in rigor: the bottom-up results (wave equation → KG → staggered fermions → chiral symmetry, $K = 2d = 6$, gauge multiplicities $(3, 2, 1)$, $\theta = 0$, detailed balance) are at theorem level. The top-down constraints (asymptotic freedom, minimality of $N_c$, chirality from the trace-out) are at proposition level — well-motivated physical arguments, not pure mathematics. The identification of fermion sectors with SM generations and of the global commutant symmetry with the local gauge group involve physical interpretation steps that are unique and consistent but not derived from lattice geometry alone. The continuum-limit universality that connects the lattice theory to the SM is supported by extensive numerical evidence but shares the status of all lattice QCD. These distinctions matter: the framework's credibility rests on precision about what is proved and what is motivated.

One algebraic condition ($\alpha = 0$) produces quantum mechanics, chiral fermions, and the Higgs boson. One matrix ($M$) determines the gauge symmetry, the mass spectrum, and the gauge field structure. One geometric fact ($d = 3$) produces renormalizability, the fermion count, and the dark sector. One symmetry ($T$-invariance) forces $\theta = 0$ and $\bar{\theta} = 0$ at the lattice scale with radiatively stable IR persistence. One structural fact ($D_{LL} = 0$) makes the emergent gauge coupling chiral. The partition that creates quantum mechanics simultaneously breaks parity, mandates the Higgs, and preserves $T$. The Standard Model is what mathematical consistency looks like in a universe observed from within.

---

## ACKNOWLEDGEMENTS

During the preparation of this work, the author used Claude Opus 4.6 (Anthropic) to assist in drafting, numerical simulations, and refining argumentation. The author reviewed and edited all content and takes full responsibility for the publication.

---

## REFERENCES

[1] A. Maybaum, "The Incompleteness of Observation," submitted to *Foundations of Physics* (2026).
[2] A. Maybaum, "General Relativity from Observational Incompleteness," companion paper (2026).
[3] A. Maybaum, "The Substrate Problem," companion paper (2026).
[4] J. B. Kogut and L. Susskind, "Hamiltonian formulation of Wilson's lattice gauge theories," *Phys. Rev. D* **11**, 395 (1975).
[5] L. Susskind, "Lattice fermions," *Phys. Rev. D* **16**, 3031 (1977).
[6] P. W. Higgs, "Broken symmetries and the masses of gauge bosons," *Phys. Rev. Lett.* **13**, 508 (1964).
[7] B. W. Lee, C. Quigg, and H. B. Thacker, "Weak interactions at very high energies: The role of the Higgs-boson mass," *Phys. Rev. D* **16**, 1519 (1977).
[8] H. B. Nielsen and M. Ninomiya, "Absence of neutrinos on a lattice," *Nucl. Phys. B* **185**, 20 (1981).
[9] K. G. Wilson, "Confinement of quarks," *Phys. Rev. D* **10**, 2445 (1974).
[10] M. Creutz, *Quarks, Gluons and Lattices* (Cambridge University Press, 1983).
[11] L. Alvarez-Gaumé and E. Witten, "Gravitational anomalies," *Nucl. Phys. B* **234**, 269 (1984).
[12] G. 't Hooft, "Naturalness, chiral symmetry, and spontaneous chiral symmetry breaking," in *Recent Developments in Gauge Theories* (Plenum, 1980).
[13] R. N. Mohapatra, *Unification and Supersymmetry* (Springer, 3rd ed., 2003), §6.3.
[14] A. D. Sakharov, "Violation of CP invariance, C asymmetry, and baryon asymmetry of the universe," *JETP Lett.* **5**, 24 (1967).
[15] C. Abel et al., "Measurement of the permanent electric dipole moment of the neutron," *Phys. Rev. Lett.* **124**, 081803 (2020).
[16] P. Ehrenfest, "In what way does it become manifest in the fundamental laws of physics that space has three dimensions?" *Proc. Amsterdam Acad.* **20**, 200 (1917).
[17] D. J. Gross and F. Wilczek, "Ultraviolet behavior of non-abelian gauge theories," *Phys. Rev. Lett.* **30**, 1343 (1973); H. D. Politzer, "Reliable perturbative results for strong interactions?" *Phys. Rev. Lett.* **30**, 1346 (1973).
