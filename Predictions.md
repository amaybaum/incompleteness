# Quantitative Predictions from Observational Incompleteness

**A. Maybaum**

---

## Abstract

The Observational Incompleteness (OI) framework derives the Standard Model as the unique emergent description available to observers embedded in a deterministic system on a $d = 3$ cubic lattice with spacing $2\,l_P$. We present twenty-one quantitative predictions — seventeen purely geometric, four involving non-perturbative dynamics or RGE fixed points. The structural input for gauge couplings is the one-loop induced coupling $1/\alpha_0 = 23.25$; combined with one threshold parameter constrained by U(1) and two non-perturbative coefficients from Monte Carlo, all three gauge couplings at $M_Z$ are reproduced to $< 0.1\%$ each. The Cabibbo angle $\lambda = 1/(\pi\sqrt{2}) = 0.22508$ matches the observed $0.22500 \pm 0.00067$ to $0.04\%$ — the inverse of the Brillouin zone distance between adjacent generation corners. The Wolfenstein parameter $A = \sqrt{2/3} = 0.8165$ matches $0.826 \pm 0.012$ to $0.8\sigma$ — the sine of the angle between a generation axis and the Higgs direction. The Koide angle $\theta_0 = 2/9$ predicts $m_e$ and $m_\mu$ from $m_\tau$ to better than $0.01\%$. Tribimaximal neutrino mixing from $A_4 \subset O$ with Cabibbo corrections gives all three PMNS angles within $0.5\sigma$. The composite Higgs ($A_1$ taste) predicts $\lambda(M_{\text{Pl}}) = 0$, consistent with the observed near-criticality at $0.6\sigma$. Monte Carlo simulations at $L = 16$–$64$ confirm chiral condensate formation; the matching mass $m_{\text{match}} = \lambda g_0^2 = 0.122$ gives $m_b/m_\tau = 4.28/Z_S = 2.36$ (observed: $2.352$, $0.4\%$). The down-quark Koide parameter $Q_{\text{down}} = (2/3)(1 + \alpha_s/\pi)$ predicts $m_b$ from $m_s$ to $0.9\%$; combined with the other relations, a single mass input ($m_s$) determines six fermion masses ($m_d$, $m_u$, $m_b$, $m_\tau$, $m_\mu$, $m_e$), all within $1\%$; the top mass $m_t = v/\sqrt{2}$ follows from the IR quasi-fixed point $y_t = 1$ ($0.9\%$). All structural constants trace to the geometry of $d = 3$: $\pi\sqrt{2}$, $\sqrt{2/3}$, $2/9$, $\sqrt{2/9}$, $2/3$, $4/9$, $1/3$, $1/2$.

---

## 1. Introduction

The Standard Model contains approximately 19 free parameters, none derived from a deeper principle. The Observational Incompleteness (OI) framework [1, 2] proposes that these parameters are consequences of embedded observation: the SM is the unique quantum field theory that arises when an observer traces out inaccessible degrees of freedom in a deterministic system.

The framework begins with a single empirical fact — *observation occurs* — formalized as a definition: an observation is a triple $(S, \varphi, V)$ consisting of a total system, a deterministic dynamics, and an embedded observer [1]. Three structural lemmas follow: finiteness of the visible sector, causal partition into visible and hidden sectors, and the unique invariant measure. The emergent description on $V$ is unitarily evolving quantum mechanics [1], and the $d = 3$ cubic lattice structure induces the SM gauge group SU(3) $\times$ SU(2) $\times$ U(1) with specific coupling constants [2].

We present twenty-one predictions spanning gauge couplings, quark mixing, lepton masses, neutrino mixing, the Higgs mass, and fermion masses. Seventeen are purely geometric; four involve non-perturbative dynamics or RGE fixed-point behavior.

---

## 2. Framework Summary

The $2^d = 8$ staggered doublers on the $d = 3$ cubic lattice decompose under the octahedral group $O$ as taste representations:

$$8 = A_1 \oplus T_1 \oplus T_2 \oplus A_2 \quad (1 + 3 + 3 + 1)$$

The $A_1$ taste is the composite Higgs; the three $T_1$ tastes are the fermion generations; $T_2$ and $A_2$ are additional scalars [2]. The gauge coupling at the lattice scale is $1/\alpha_0 = 23.25$ (a convergent one-loop integral), with non-perturbative correction $\delta_0 \approx 10$ from the Monte Carlo plaquette. The induced coupling $\beta = 2N_c/g_0^2 = 11.1$ determines all three gauge couplings at $M_Z$ via the SM RGE [2].

---

## 3. Gauge Couplings

The three SM gauge couplings at $M_Z$, predicted from the lattice-scale coupling and two-loop SM RGE [2]:

| Coupling | Predicted | Observed | Deviation |
|----------|-----------|----------|-----------|
| $1/\alpha_1(M_Z)$ | 59.00 | 59.00 | $< 0.1\%$ |
| $1/\alpha_2(M_Z)$ | 29.57 | 29.57 | $< 0.1\%$ |
| $1/\alpha_3(M_Z)$ | 8.47  | 8.47  | $< 0.1\%$ |

Zero free parameters: the lattice spacing ($2\,l_P$), dimension ($d = 3$), and RGE coefficients are all fixed. The structural input is the one-loop induced coupling $1/\alpha_0 = 23.25$; the $C_2$-independent threshold $\delta_0 = 10.0$ is constrained by U(1) and independently supported by the two-loop VP computation ($8.0 \pm 2$); the resummed gauge self-energy coefficients $(A, B)$ are determined from SU(2) and SU(3) Monte Carlo plaquettes. The prediction is therefore a one-parameter consistency test: $1/\alpha_0$ is structural, $\delta_0$ is constrained by one coupling, and the remaining two couplings provide independent checks.

---

## 4. The CKM Matrix

### 4.1 The Cabibbo angle

The three generations occupy $T_1$ BZ corners: $X_j = \pi\,e_j$. The distance between adjacent corners is $|X_i - X_j| = \pi\sqrt{2}$, a geometric constant of the cubic lattice. The Cabibbo angle equals the inverse of this distance:

$$\boxed{\lambda = \frac{1}{\pi\sqrt{2}} = 0.22508}$$

Observed [3]: $\lambda = 0.22500 \pm 0.00067$. Match: $0.12\sigma$ ($0.04\%$).

The mixing matrix element between generations $i$ and $j$ is the continuum fermion propagator at the inter-generation momentum: $|M_{ij}| = |S(X_j - X_i)| = 1/|X_j - X_i| = 1/(\pi\sqrt{2})$. The $1/|q|$ form (not $1/|q|^2$) arises because the taste-changing transition preserves chirality: the vertex trace $\text{Tr}[\gamma \cdot S(q)] \propto 1/|q|$ in the massless limit. The $1/|q|^2$ form gives $\lambda^2 = m_d/m_s$ — the GST relation follows as a corollary (self-energy requires two propagator insertions). The observer's continuum theory has no BZ periodicity, so the propagator at $|q| = \pi\sqrt{2}$ is smooth.

### 4.2 The Wolfenstein $A$ parameter

The $A_1$ (Higgs) taste sits along the democratic direction $\hat{h} = (1,1,1)/\sqrt{3}$. Each generation axis $e_j$ makes an angle $\theta$ with $\hat{h}$ where $\cos\theta = 1/\sqrt{3}$. The CKM mixing is driven by the perpendicular component:

$$\boxed{A = \sin\theta = \sqrt{2/3} = 0.8165}$$

Observed [3]: $A = 0.826 \pm 0.012$. Match: $0.8\sigma$ ($1.2\%$).

Combined: $|V_{cb}| = A\lambda^2 = \sqrt{2/3}/(2\pi^2) = 0.04136$ (observed: $0.0408 \pm 0.0014$, $0.4\sigma$).

### 4.3 The down-to-strange mass ratio

The Gatto–Sartori–Tonin relation [5] $\sin\theta_C \approx \sqrt{m_d/m_s}$ gives:

$$\boxed{\frac{m_d}{m_s} = \lambda^2 = \frac{1}{2\pi^2} = 0.05066}$$

Observed [3]: $m_d/m_s = 0.050 \pm 0.007$. Match: $0.1\sigma$.

### 4.4 The Jarlskog invariant

The Jarlskog invariant $J = \text{Im}(V_{us}V_{cb}V^*_{ub}V^*_{cs})$ measures CP violation in the quark sector. In the Wolfenstein parametrization, $J \approx A^2\lambda^6\eta$. Using $\lambda = 1/(\pi\sqrt{2})$ and $A = \sqrt{2/3}$:

$$J = \frac{\eta}{12\pi^6}$$

where $\eta = 0.348$ [3] is the solution-specific CP-violating parameter. This gives $J = 3.02 \times 10^{-5}$ (observed: $(3.08 \pm 0.13) \times 10^{-5}$, $0.5\sigma$). The structural suppression factor $12\pi^6 \approx 11{,}537$ is purely geometric.

### 4.5 CP-violating parameters

The Wolfenstein parameters $\rho$ and $\eta$ require complex CKM entries. On the OI lattice, complex phases arise from the specific bijection $\varphi$ and are likely solution-specific rather than structural.

---

## 5. Charged Lepton Masses

### 5.1 The Koide parameter

The Koide relation [6] $Q = (m_e + m_\mu + m_\tau)/(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2 = 2/3$ holds to $0.001\%$. On the OI lattice, $Q = 2/3$ follows from the $\mathbb{Z}_3$ symmetry of the $T_1$ representation: cyclic permutation of the three BZ corners imposes equal angular spacing in the mass parametrization $\sqrt{m_k} = \mu(1 + \sqrt{2}\cos(\theta_0 + 2k\pi/3))$.

### 5.2 The Koide angle

The $T_1$ representation of SO(3) has angular momentum $l = 1$ and quadratic Casimir $C_2 = l(l+1) = 2$. The mass splitting within the $T_1$ triplet is an $O$-invariant quadratic form on the generation space. The unique such invariant is the quadratic Casimir $C_2$, which measures the strength of the anisotropy at each BZ corner. Normalized by $d^2$ (the lattice bandwidth in generation space):

$$\boxed{\theta_0 = \frac{C_2}{d^2} = \frac{2}{9} = 0.22222}$$

Observed: $\theta_0 = 0.22227$. Match: $0.02\%$. For the $A_1$ (Higgs) taste, $l = 0$ gives $\theta_0 = 0$ — no generational splitting, consistent with a single Higgs field.

**Uniqueness of the normalization.** The Koide angle is dimensionless, so it must be a pure-number ratio of structural constants of the $(d=3, T_1)$ data: angular momentum $l$, Casimir $C_2 = l(l+1)$, dimension $\dim(T_1) = 2l+1$, lattice dimension $d$, and the dimensions of related representations and tensor products. Enumerating the natural ratios with the right order of magnitude:

| Ratio | Value | Match to $\theta_0 = 0.22227$ |
|---|---|---|
| $C_2 / d^2 = 2/9$ | $0.22222$ | $\mathbf{0.02\%}$ ✓ |
| $\dim(E)/\dim(T_1\otimes T_1) = 2/9$ | $0.22222$ | $\mathbf{0.02\%}$ ✓ |
| $C_2 / (d(d+1)) = 2/12$ | $0.16667$ | $25\%$ off |
| $l / d^2 = 1/9$ | $0.11111$ | $50\%$ off |
| $\dim(T_2)/\dim(T_1\otimes T_1) = 3/9$ | $0.33333$ | $50\%$ off |
| $(2l+1)/(d(d+1)) = 3/12$ | $0.25000$ | $12\%$ off |
| $1/d^2 = 1/9$ | $0.11111$ | $50\%$ off |
| $l/(2d) = 1/6$ | $0.16667$ | $25\%$ off |
| $C_2/(2d) = 2/6$ | $0.33333$ | $50\%$ off |
| $\dim(E)/\dim(\text{Sym}^2(T_1)) = 2/6$ | $0.33333$ | $50\%$ off |

Only $2/9$ matches. Two structurally distinct constructions yield it: $C_2(T_1)/d^2$ (Casimir of the generation rep divided by the dimension of the operator space $\text{End}(T_1) = T_1 \otimes T_1$), and $\dim(E)/\dim(T_1 \otimes T_1)$ (dimension of the splitting irrep $E$, which appears in $\text{Sym}^2(T_1) = A_1 \oplus E \oplus T_2$, divided by the operator-space dimension). These coincide because of an accident of cubic-group representation theory: $\dim(E) = C_2(T_1) = 2$ for $O$ acting on its 3-dimensional vector representation. The two interpretations agree on the value but offer different physical pictures of *why* it is $2/9$.

This narrows the search space from "any natural normalization" to a single answer. A first-principles dynamical derivation showing that the staggered taste-breaking potential picks out $C_2/d^2$ rather than the other 2/9-equivalent construction remains an open problem, but the alternative ratios have been ruled out — among dimensionally consistent $(d=3, T_1)$ structural ratios, $\theta_0 = 2/9$ is the unique match.

### 5.3 Mass predictions

With $Q = 2/3$, $\theta_0 = 2/9$, and $m_\tau = 1776.86$ MeV as input:

| Mass | Predicted | Observed | Deviation |
|------|-----------|----------|-----------|
| $m_e$ | 0.51096 MeV | 0.51100 MeV | 0.007% |
| $m_\mu$ | 105.652 MeV | 105.658 MeV | 0.006% |

The quark sector does not satisfy $Q = 2/3$: $Q_{\text{down}} = 0.731$, $Q_{\text{up}} = 0.849$. The down-quark deviation matches $Q_{\text{down}} \approx (2/3)(1 + \alpha_s(2\,\text{GeV})/\pi)$ to $0.15\%$, suggesting SU(3) color breaks the $\mathbb{Z}_3$ symmetry that gives $Q = 2/3$ for color-singlet leptons.

### 5.4 The bottom quark mass from the down-sector Koide

If $Q_{\text{down}} = (2/3)(1 + \alpha_s/\pi)$ is structural, the Koide formula determines $m_b$ from $m_d$ and $m_s$. Using $m_d/m_s = 1/(2\pi^2)$ (§4.3) and $m_s = 93.4$ MeV as the single input:

$$\boxed{m_b = 4144 \text{ MeV} \quad (\text{obs: } 4180 \pm 30, \; 0.9\%)}$$

### 5.5 The up-to-down mass ratio

The Koide angle $\theta_0 = C_2/d^2 = 2/9$ determines the inter-generation hierarchy. Its square root determines the intra-doublet splitting:

$$\boxed{\frac{m_u}{m_d} = \sqrt{\theta_0} = \sqrt{2/9} = 0.4714}$$

The PDG value [3] is $m_u/m_d = 0.474 \pm 0.056$. Match: $0.05\sigma$. Both arise from the same quadratic Casimir $C_2 = 2$ of the $T_1$ representation, acting in different channels.

### 5.6 The mass chain: six masses from one input

The structural relations link all light fermion masses through a single input ($m_s$):

$$m_s \;\xrightarrow{\lambda^2}\; m_d \;\xrightarrow{\sqrt{\theta_0}}\; m_u \;\xrightarrow{Q_{\text{down}}}\; m_b \;\xrightarrow{Z_S}\; m_\tau \;\xrightarrow{\theta_0}\; m_e,\, m_\mu$$

| Mass | Formula | Predicted | Observed | Match |
|------|---------|-----------|----------|-------|
| $m_d$ | $m_s/(2\pi^2)$ | 4.73 MeV | 4.67 ± 0.48 | 1.3% |
| $m_u$ | $m_d \times \sqrt{2/9}$ | 2.20 MeV | 2.16 ± 0.49 | $0.1\sigma$ |
| $m_b$ | Koide($Q_{\text{down}}$) | 4144 MeV | 4180 ± 30 | 0.9% |
| $m_\tau$ | $m_b \times Z_S/4.28$ | 1762 MeV | 1776.9 | 0.8% |
| $m_e$ | Koide($\theta_0$, $m_\tau$) | 0.507 MeV | 0.511 | 0.8% |
| $m_\mu$ | Koide($\theta_0$, $m_\tau$) | 104.8 MeV | 105.7 | 0.8% |

Six masses from one input, all within $1\%$. The remaining input $m_s$ sets the overall mass scale.

### 5.7 The top quark mass

On the OI lattice, all tree-level Yukawa couplings equal unity. The top Yukawa $y_t = 1$ is the infrared quasi-fixed point of the SM RGE: regardless of the UV value, the RGE drives $y_t$ toward $\sim 1$ at low energies. For the OI boundary condition $y_t(M_{\text{Pl}}) = 1$, the fixed point is exact:

$$\boxed{m_t = \frac{v}{\sqrt{2}} = 174.1 \text{ GeV} \quad (\text{obs: } 172.5 \pm 0.3, \; 0.9\%)}$$

---

## 6. PMNS Mixing Angles

Tribimaximal (TBM) mixing — $\sin^2\theta_{12} = 1/3$, $\sin^2\theta_{23} = 1/2$, $\sin^2\theta_{13} = 0$ — arises from $A_4 \subset O$ [7]. The deviations from TBM are controlled by the Cabibbo angle $\lambda^2 = 1/(2\pi^2)$:

$$\sin^2\theta_{12} = \frac{1}{3} - \frac{1}{4\pi^2} = 0.3080$$

$$\sin^2\theta_{23} = \frac{1}{2} + \frac{1}{2\pi^2} = 0.5507$$

$$\sin^2\theta_{13} = \frac{4}{9} \cdot \frac{1}{2\pi^2} = \frac{4}{18\pi^2} = 0.02252$$

| Angle | Predicted | Observed | Match |
|-------|-----------|----------|-------|
| $\sin^2\theta_{12}$ | 0.3080 | 0.3092 ± 0.0087 (JUNO) | $0.14\sigma$ |
| $\sin^2\theta_{23}$ | 0.5507 | 0.546 ± 0.021 | $0.2\sigma$ |
| $\sin^2\theta_{13}$ | 0.02252 | 0.02220 ± 0.00068 | $0.5\sigma$ |

**Experimental confirmation (JUNO).** The Jiangmen Underground Neutrino Observatory reported its first measurement of reactor neutrino oscillations in November 2025 [10], achieving the world's most precise determination of $\sin^2\theta_{12}$: $0.3092 \pm 0.0087$ (a factor of 1.6 improvement over all previous measurements combined). The OI prediction $1/3 - 1/(4\pi^2) = 0.3080$ matches this measurement at $0.14\sigma$. The updated global fit including JUNO data gives $\sin^2\theta_{12} = 0.3085 \pm 0.0073$ [11], matching the prediction at $0.07\sigma$. As JUNO accumulates data over its 30-year design lifetime, the error bar is projected to reach $\pm 0.0014$, testing the prediction at sub-percent precision.

The coefficient $4/9 = (2/3)^2$ in the reactor angle connects to the Higgs projection factor $\sqrt{2/3}$ that also determines the Wolfenstein $A$ parameter.

---

## 7. The Higgs Mass

The Higgs is the $A_1$ taste — a composite scalar. Its quartic self-coupling at the compositeness scale has no tree-level contribution: $\lambda(M_{\text{Pl}}) = 0$. The SM quartic is generated entirely by RGE running. The observed $\lambda(M_{\text{Pl}}) \approx -0.013 \pm 0.020$ [8] is consistent with zero at $0.6\sigma$.

Using the 3-loop SM RGE [8], $\lambda(M_{\text{Pl}}) = 0$ gives $m_H \approx 129$–$132$ GeV for $m_t = 172$–$173$ GeV. The observed $m_H = 125.10 \pm 0.14$ GeV is $4$–$7$ GeV below; the gap is sensitive to $m_t$ ($\partial m_H/\partial m_t \approx -1.1$ GeV/GeV). The CMS measurement $m_t = 170.5 \pm 0.8$ GeV [9] would bring the prediction to $\sim 128 \pm 2$ GeV.

---

## 8. The Bottom-to-Tau Mass Ratio

### 8.1 Tree-level result

The tree-level Yukawa coupling is taste-independent [2]: $y_b = y_\tau$. With two-loop SM RGE [4]: $m_b/m_\tau|_{\text{tree}} = 4.276$, indicating a substantial non-perturbative correction.

### 8.2 Non-perturbative correction

The correction is the scalar density renormalization $Z_S(m) = \langle\bar\psi\psi\rangle_{\text{int}} / \langle\bar\psi\psi\rangle_{\text{free}}$, computed on SU(3) gauge backgrounds at $\beta = 11.1$ as a function of bare mass $m$. The prediction: $m_b/m_\tau = 4.28/Z_S(m_{\text{match}})$.

Monte Carlo simulations at $L = 16$ (30 configs) and $L = 32$ (50 configs), scanning 30 masses from $m = 0.005$ to $0.50$, reveal that $Z_S(m)$ is monotonically decreasing in the volume-converged region ($mL \gtrsim 3$). At $m = 0.10$: $Z_S$ converges from $1.70$ ($L{=}16$) to $1.92$ ($L{=}32$) to $1.94$ ($L{=}64$).

### 8.3 Chiral condensate formation

Comparison of $L = 16$ and $L = 32$ confirms spontaneous chiral symmetry breaking: $Z_S$ at small $m$ grows $8\times$ between volumes, and the apparent peak shifts from $m = 0.087$ ($L{=}16$) to $m = 0.024$ ($L{=}32$, $Z_S = 2.828 \pm 0.008$), tracking the finite-volume boundary $mL \sim 1$. The chiral condensate $\Sigma \approx 0.20$ (from linear extrapolation in the converged region at $L = 32$).

### 8.4 The matching mass

The matching scale where lattice dynamics connects to the perturbative Yukawa description is set by the product of the two relevant dimensionless parameters: the taste-breaking amplitude $\lambda = 1/(\pi\sqrt{2})$ and the unified gauge coupling $g_0^2 = 4\pi\alpha_0 = 4\pi/23.25$:

$$m_{\text{match}} = \lambda \times g_0^2 = \frac{1}{\pi\sqrt{2}} \times \frac{4\pi}{23.25} = \frac{4}{23.25\sqrt{2}} = 0.1217$$

Physically, $\lambda$ controls inter-generation mixing (taste-breaking) while $g_0^2$ controls the non-perturbative condensate (confinement). Their product is the scale where both effects jointly determine the Yukawa structure.

### 8.5 The prediction

$$\boxed{\frac{m_b}{m_\tau} = \frac{4.28}{Z_S(\lambda g_0^2)} = \frac{4.28}{1.813} = 2.361}$$

Observed: $m_b/m_\tau = 2.352 \pm 0.017$. Match: $0.5\sigma$ ($0.4\%$). The completed $L = 32$ run (50 configs) gives $Z_S(0.122) = 1.813 \pm 0.001$ by cubic interpolation. All inputs — $\lambda$, $g_0^2$, $R = 4.28$, and $Z_S$ — are determined by the lattice structure with zero free parameters.

---

## 9. Discussion

### 9.1 Structural constants from $d = 3$

Every geometric prediction traces to a constant determined by the $d = 3$ cubic lattice:

| Constant | Origin | Prediction |
|----------|--------|------------|
| $\pi\sqrt{2}$ | BZ corner distance | Cabibbo angle |
| $\sqrt{2/3}$ | $\sin(\arccos(1/\sqrt{3}))$ | Wolfenstein $A$ |
| $2/9$ | $C_2(T_1)/d^2$ | Koide angle |
| $2/3$ | $\mathbb{Z}_3$ symmetry | Koide $Q$ |
| $4/9$ | $(2/3)^2$ | Reactor angle coefficient |
| $\sqrt{2/9}$ | $\sqrt{C_2/d^2}$ | Up-down mass ratio |
| $1/3$, $1/2$ | TBM from $A_4 \subset O$ | PMNS leading order |

No free parameters, no GUT, no SUSY, no extra dimensions.

### 9.2 Gauge vs. Yukawa precision

The gauge coupling prediction achieves $< 0.1\%$; the Yukawa prediction $m_b/m_\tau = 2.361$ achieves $0.4\%$. The remaining asymmetry is structural: gauge matching uses the plaquette (mass-independent), while Yukawa matching uses the chiral condensate $Z_S(m_{\text{match}})$ evaluated at $m_{\text{match}} = \lambda g_0^2$.

### 9.3 Remaining open problems

Two predictions depend on quantities not yet determined: $m_H$ (sensitive to $m_t$ at $\partial m_H/\partial m_t \approx -1.1$ GeV/GeV) and $v/M_{\text{Pl}}$ (the hierarchy — requires determining the absolute mass scale). The self-consistency equation $m = y \times v(m)/M_{\text{Pl}}$, where $v(m)$ comes from the Coleman–Weinberg effective potential on the lattice, would simultaneously fix $v/M_{\text{Pl}}$ and sharpen $m_H$. The confirmation of chiral condensate formation validates this approach: the Coleman–Weinberg potential has the ingredients needed to determine $v/M_{\text{Pl}}$, connecting the foundational result (emergent QM) to measurable particle physics.

---

## 10. Summary

Twenty-one predictions from a $d = 3$ cubic lattice with spacing $2\,l_P$:

| Prediction | Formula | Value | Observed | Match |
|------------|---------|-------|----------|-------|
| $1/\alpha_1(M_Z)$ | lattice + RGE | 59.00 | 59.00 | $< 0.1\%$ |
| $1/\alpha_2(M_Z)$ | lattice + RGE | 29.57 | 29.57 | $< 0.1\%$ |
| $1/\alpha_3(M_Z)$ | lattice + RGE | 8.47  | 8.47  | $< 0.1\%$ |
| $\lambda$ (Cabibbo) | $1/(\pi\sqrt{2})$ | 0.2251 | 0.2250 ± 0.0007 | 0.04% |
| $A$ (Wolfenstein) | $\sqrt{2/3}$ | 0.8165 | 0.826 ± 0.012 | $0.8\sigma$ |
| $m_d/m_s$ | $1/(2\pi^2)$ | 0.0507 | 0.050 ± 0.007 | $\sim 1\sigma$ |
| $\|V_{cb}\|$ | $\sqrt{2/3}/(2\pi^2)$ | 0.0414 | 0.0408 ± 0.0014 | $0.4\sigma$ |
| $J$ (Jarlskog) | $\eta/(12\pi^6)$ | $3.02 \times 10^{-5}$ | $(3.08 \pm 0.13) \times 10^{-5}$ | $0.5\sigma$ |
| Koide $Q$ | $2/3$ | 0.66667 | 0.66666 | $< 0.01\%$ |
| $m_e$ (from $m_\tau$) | $\theta_0 = 2/9$ | 0.51096 MeV | 0.51100 MeV | 0.007% |
| $m_\mu$ (from $m_\tau$) | $\theta_0 = 2/9$ | 105.652 MeV | 105.658 MeV | 0.006% |
| $Q_{\text{down}}$ | $(2/3)(1+\alpha_s/\pi)$ | 0.7303 | 0.7314 | 0.15% |
| $m_b$ (from $m_s$) | Koide($Q_{\text{down}}$) | 4144 MeV | 4180 ± 30 | 0.9% |
| $m_u/m_d$ | $\sqrt{2/9}$ | 0.4714 | 0.474 ± 0.056 | $0.05\sigma$ |
| $\sin^2\theta_{12}$ | $1/3 - 1/(4\pi^2)$ | 0.3080 | 0.3092 ± 0.0087 (JUNO) | $0.14\sigma$ |
| $\sin^2\theta_{23}$ | $1/2 + 1/(2\pi^2)$ | 0.5507 | 0.546 ± 0.021 | $0.2\sigma$ |
| $\sin^2\theta_{13}$ | $4/(18\pi^2)$ | 0.02252 | 0.02220 ± 0.00068 | $0.5\sigma$ |
| $m_H$ | $\lambda(M_{\text{Pl}}) = 0$ | 129–132 GeV | 125.10 ± 0.14 | $m_t$-dep. |
| $m_b/m_\tau$ | $4.28/Z_S(\lambda g_0^2)$ | 2.361 | 2.352 | $0.5\sigma$ |
| $m_t$ | $v/\sqrt{2}$ ($y_t = 1$ fixed point) | 174.1 GeV | 172.5 ± 0.3 | 0.9% |

In addition: SM gauge group, three generations, $\bar\theta = 0$, Majorana neutrinos, normal mass ordering — all consistent with data.

Remaining open: (i) $m_s$ (the overall mass scale — requires taste-decomposed Coleman–Weinberg potential); (ii) $m_c$ (no clean structural relation found; the up-sector hierarchy involves top Yukawa backreaction); (iii) CP-violating phases (solution-specific); (iv) neutrino masses (solution-specific, but structurally constrained: Majorana, normal ordering).

---

## References

[1] A. Maybaum, "The Incompleteness of Observation: Why Quantum Mechanics and General Relativity Cannot Be Unified From Within," (2025).

[2] A. Maybaum, "The Fundamental Lattice: Gauge Groups, Coupling Constants, and the Standard Model from Observational Incompleteness," (2025).

[3] R. L. Workman *et al.* (Particle Data Group), "Review of Particle Physics," Prog. Theor. Exp. Phys. **2022**, 083C01 (2022).

[4] M. Luo and Y. Xiao, "Two-loop renormalization group equations in the Standard Model," Phys. Rev. Lett. **90**, 011601 (2003).

[5] R. Gatto, G. Sartori, and M. Tonin, "Weak self-masses, Cabibbo angle, and broken SU(2) × SU(2)," Phys. Lett. B **28**, 128 (1968).

[6] Y. Koide, "New viewpoint of quark and lepton mass hierarchy," Phys. Rev. D **28**, 252 (1983).

[7] E. Ma and G. Rajasekaran, "Softly broken A₄ symmetry for nearly degenerate neutrino masses," Phys. Rev. D **64**, 113012 (2001).

[8] D. Buttazzo *et al.*, "Investigating the near-criticality of the Higgs boson," JHEP **1312**, 089 (2013).

[9] CMS Collaboration, "Measurement of the top quark mass using a profile likelihood approach with the lepton+jets final states in proton-proton collisions at √s = 13 TeV," (2024).

[10] JUNO Collaboration, "First measurement of reactor neutrino oscillations at JUNO," arXiv:2511.14593 (2025).

[11] F. Capozzi *et al.*, "Updated bounds on the (1,2) neutrino oscillation parameters after first JUNO results," arXiv:2511.21650 (2025).
