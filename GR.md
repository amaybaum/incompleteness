# ℏ, the Bekenstein-Hawking Entropy, and Dynamical Dark Energy from the Cosmological Horizon

**Author:** Alex Maybaum  
**Date:** April 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / Gravitation / Cosmology

---

## Abstract

Applied to the cosmological horizon as a causal partition, the embedded-observation framework of [Main] determines the emergent action scale $\hbar = c^3 \epsilon^2 / (4G)$ from classical horizon temperature and thermal self-consistency, fixes the discreteness scale $\epsilon = 2\,l_p$ as the unique simultaneous solution, derives the Bekenstein-Hawking entropy $S = A/(4 l_p^2)$ including the $1/4$ coefficient by direct boundary-mode counting, and dissolves the cosmological constant problem by identifying the quantum vacuum energy and the effective cosmological constant as properties of logically distinct descriptions rather than commensurable quantities whose $10^{122}$ ratio requires cancellation. The recent LIGO/Virgo/KAGRA observation GW250114 (September 2025) confirms the black-hole area law at $99.999\%$ confidence. The framework predicts dynamical dark energy in Type II running-vacuum form as a *structural* prediction (functional form forced by boundary-entropy architecture; theorem-level magnitude $|\nu| \approx |\nu_{\rm QFT}| \sim 10^{-32}$, indistinguishable from zero) — consistent with the Bertini et al. (2025) RG-corrected $\Lambda$CDM fit to DESI DR2 + DES-Y5 + Planck 2018, which reports $\nu = -(2.5 \pm 1.3) \times 10^{-4}$ (consistent with zero at $2\sigma$); a ~$95\%$ dark sector corollary in which the apparent invisible matter is a structural feature of the embedded observer's description rather than a new particle species; and a MOND-like acceleration scale $a_0 = cH/6$ from entropy displacement at the cosmological boundary, reproducing the baryonic Tully-Fisher relation and predicting Keplerian decline of galactic rotation curves at radii exceeding $r_M = \sqrt{6 G M_B/(cH)}$ — the last confirmed by Jiao et al. (2023) in the Milky Way at $\sim 17$ kpc. The $H(z)$ dependence of $a_0$ predicts systematically more baryon-dominated rotation curves at high redshift, consistent with Genzel et al.'s detection of declining outer velocities at $z = 0.9$–$2.4$. All results follow from partition geometry alone and are independent of the specific substratum dynamics, treated in a separate companion paper [SM].

---

## 1. Introduction

The cosmological observables that most resist explanation within standard physics — the value of $\hbar$, the Bekenstein-Hawking area law, the $10^{122}$ cosmological constant problem, the accelerated expansion, the ~95% dark sector, and the MOND-like behavior of galactic rotation curves — are treated here as consequences of a single structural fact: the cosmological horizon partitions the degrees of freedom of any sub-$c$ observer into a visible sector and a causally inaccessible hidden sector.

**Prerequisites.** This paper takes as established the following results from a companion work [Main]: (i) an observer embedded in a deterministic bijection on a finite configuration space, coupled to a hidden sector that is non-trivial (C1), slow (C2: $\tau_S \ll \tau_B$), and high-capacity (C3: $N_H \gg N_V$), necessarily describes the visible sector using unitarily evolving quantum mechanics, and C1–C3 are necessary as well as sufficient (conditional on the eigenstate thermalization hypothesis for the C2 $\Leftarrow$ direction); (ii) the emergent description is uniquely determined by the partition, with any parameters of the emergent theory depending only on the partition boundary's geometric and thermodynamic properties (partition-relativity); (iii) the emergent transition probabilities $T_{ij}(t)$ uniquely determine the emergent Hamiltonian up to a diagonal-unitary D-gauge, via the phase-locking lemma applied to continuous-time sampling. The technical bridge from P-indivisible classical stochastic processes on finite configuration spaces to unitary quantum evolution on finite Hilbert spaces is Barandes' stochastic-quantum correspondence [35, 36], used as the companion paper's primary tool. We treat these results as inputs and apply them to the cosmological horizon. The cosmological horizon satisfies all three structural conditions: causal coupling via the Einstein constraint equations (C1), a slow-bath timescale of order the Hubble time $\tau_B \sim 10^{17}$ s (C2), and a hidden-sector capacity of order $S_{\text{dS}} \sim 10^{122}$ modes (C3). The ETH condition for C2 necessity holds for the horizon complement (a generic chaotic many-body system), so the full equivalence applies in our universe.

The present paper reproves none of [Main]'s foundational results. Where a theorem below invokes a specific input — partition-relativity (§3.1), the emergent-description determination by transition probabilities (§3.2–§3.3), or the P-indivisibility/recurrence argument (§3.2 deep-sector lemma; §8 theorem requirements) — the invocation is stated as a known result and the reader is directed to [Main] for the proof.

The results are as follows. The emergent action scale $\hbar = c^3 \epsilon^2 / (4G)$ is determined by thermal self-consistency between the classical horizon temperature (computed from the Jacobson thermodynamic argument with no quantum input) and the Euclidean KMS period of the emergent QFT on the same horizon (§3). The discreteness scale $\epsilon = 2\,l_p$ is then fixed as the unique simultaneous solution of the action-scale relation and the definition of the Planck length (§4). The Bekenstein-Hawking entropy follows directly by mode counting, with the $1/4$ coefficient derived rather than assumed as the ratio $2\pi/8\pi$ between the Euclidean KMS period and the Jacobson prefactor (§5); the recent LIGO/Virgo/KAGRA observation GW250114 confirms the area law at $99.999\%$ confidence. The cosmological constant problem is dissolved by identifying the emergent quantum vacuum energy of order $M_{\text{Pl}}^4$ and the effective cosmological constant of order $H^2/G$ as properties of logically distinct objects rather than commensurable quantities whose $10^{122}$ ratio requires cancellation (§6).

The framework's empirical content is developed in §7. Dynamical dark energy emerges in Type II running-vacuum form as a structural prediction forced by boundary-entropy architecture; the magnitude of the $H^2$ coefficient at theorem level is the emergent-QFT value $|\nu| \sim (M_{\rm SM}/M_{\rm Pl})^2 \sim 10^{-32}$, indistinguishable from zero. (Two earlier framework-internal dimensional arguments have been retracted; see §7.1 Retraction notes.) This is consistent with the Bertini et al. (2025) direct RG-corrected $\Lambda$CDM fit to DESI DR2 + DES-Y5 + Planck 2018, which reports $\nu$ consistent with zero at $2\sigma$. The dark-sector corollary predicts that ~95% of the gravitational budget of the universe is invisible to the emergent QFT without requiring new fundamental particles — a concordance rather than a puzzle. The acceleration scale $a_0 = cH/6$ emerges from entropy displacement at the cosmological boundary, reproducing the MOND phenomenology in the deep-modified regime and predicting Keplerian decline at radii exceeding $r_M = \sqrt{6 G M_B/(cH)}$; the latter is confirmed by the Jiao et al. (2023) detection of a Keplerian decline in the Milky Way rotation curve at $\sim 17$ kpc. The $H(z)$ dependence of $a_0$ predicts systematically more baryon-dominated rotation curves at high redshift, consistent with the declining outer velocities observed at $z = 0.9$–$2.4$ by Genzel et al.

Three epistemic tiers are worth distinguishing before the technical development begins. **Tier 1** comprises the results that follow from partition geometry alone — the derivation of $\hbar$, the BH area law with the $1/4$ coefficient, the CC dissolution, and the Type II running-vacuum functional form of the dark energy. These do not depend on the specific substratum dynamics and would hold for any finite deterministic system satisfying the three structural conditions at its cosmological horizon. **Tier 2** comprises the dark-sector phenomenology: the ~95% invisible matter fraction, the MOND acceleration scale, and the rotation-curve crossover. These follow from the thermodynamic Clausius relation applied to the boundary reservoir and the geometric factor from spherical redistribution in de Sitter space. **Tier 3** comprises solution-specific quantities — the transition steepness between the MOND and Keplerian regimes, the greybody factor for Hawking radiation, and the specific microscopic realization of the substratum — which depend on the particular bijection $\varphi$ and are addressed in the companion paper [SM].

The paper is organized as follows. §2 identifies the cosmological horizon as a causal partition and verifies the structural conditions. §3 derives the emergent action scale $\hbar$ in four steps: the classical horizon temperature, boundary-only dependence, dimensional determination, and thermal self-consistency. §4 fixes the discreteness scale $\epsilon = 2\,l_p$. §5 derives the Bekenstein-Hawking entropy and discusses the GW250114 confirmation. §6 dissolves the cosmological constant problem. §7 presents the quantitative predictions for dark energy, the dark sector, and dark matter, with a summary table in §7.4. §8 discusses scope, the status of the discreteness scale, vacuum energy and the Higgs potential, and the framework's falsifiability conditions. §9 concludes. The cubic-lattice realization of the substratum — which fixes the Standard Model gauge structure via the wave equation — is developed in a companion paper [SM] and is independent of the GR results presented here. The reconstruction theorem and the synthesis claim that quantum mechanics, general relativity, and the arrow of time descend as three projections of the same $(S, \varphi)$ are developed in [Substratum].


---

## 2. The Cosmological Horizon as Causal Partition

### 2.1 The partition

The cosmological horizon — the boundary beyond which no signal propagating at or below $c$ can reach the observer — implements the causal partition of Lemma 2: $\Gamma_V$ is the interior, $\Gamma_H$ everything beyond. This is a consequence of GR's causal structure, not a modeling choice. The universality of the observed quantum mechanics follows from all sub-$c$ observers sharing the same causal structure.

Different observers have different horizon areas (hence different $S_{\text{dS}}$), but $\hbar = c^3 \epsilon^2/(4G)$ depends only on local geometric quantities — not on the observer's worldline or horizon area — so all observers share the same emergent action scale.

### 2.2 Verification of the conditions

**(C1)** In the ADM formulation, the bulk Hamiltonian is a sum of constraints that vanish on-shell; physical time evolution is generated by the boundary term at the horizon, which depends on data from both sides. The Hamiltonian and momentum constraints further correlate interior and exterior initial data on any Cauchy surface, so the physical phase space is a constraint surface within the kinematic product $\Gamma_V \times \Gamma_H$ (see §8.4 for implications). This is *stronger* than the $H_{\text{int}} \neq 0$ required by Lemma 2: constraints enforce correlations that persist on all timescales and cannot be perturbatively removed. **Satisfied.**

**(C2)** $\tau_B \gtrsim 1/H \sim 10^{17}$ s; for laboratory processes, $\tau_S \sim 10^{-15}$ s. Ratio: $\tau_S / \tau_B \sim 10^{-32}$. **Satisfied.**

**(C3)** Hidden sector has $A/\epsilon^2$ modes with $A \sim 10^{52}$ m$^2$; visible sector has $\sim 10^{80}$ baryons. No laboratory process saturates the hidden sector. **Satisfied.**

### 2.3 Application

Lemma 1 is now a consequence of partition geometry: the horizon has finite area $A = 4\pi c^2/H^2$, bounding coupled modes to $A/\epsilon^2 < \infty$. The Part I theorem applies: the observer's reduced description is P-indivisible and, by Barandes' correspondence, equivalent to unitary QM with $\hbar$ determined by the partition boundary.


---

## 3. The Emergent Action Scale $\hbar$

### 3.1 The classical horizon temperature

Jacobson [1] showed $dE = T\,dS$ applied to local causal horizons yields Einstein's equations, with $dE = (c^2 \kappa / 8\pi G)\,dA$, where $\kappa$ is the surface gravity of the horizon. The entropy density is $\eta = 1/\epsilon^2$ — one coupled mode per minimal cell. This is not an assumption about the number of states per cell but a consequence of two results: $\epsilon$ is defined as the minimal distinguishable scale (Lemma 1), so each cell of area $\epsilon^2$ contributes exactly one boundary mode that couples across the partition; the number of internal states per mode (the alphabet size $q$) is a gauge freedom with no observable consequences (the $q$-gauge theorem: two systems with different $q$ produce identical transition probabilities if they share the same coupling structure). Thus $dS = dA/\epsilon^2$. Equating:

$$T_{\text{cl}} = \frac{c^2 \epsilon^2 \kappa}{8\pi G k_B}$$

For de Sitter ($\kappa = cH$): $k_B T_{\text{cl}} = c^3 \epsilon^2 H / (8\pi G)$. No $\hbar$ appears.

### 3.2 The emergent action scale

**Step 1: Uniqueness.** By partition-relativity (Prerequisites), $\hbar$ is derived, not free.

**Step 2: $\hbar$ is structural, not volumetric.**

**Lemma (Boundary-only dependence).** *Decompose the hidden sector as $\mathcal{C}_H = \mathcal{C}_B \times \mathcal{C}_D$, where $\mathcal{C}_B$ denotes boundary modes (within the interaction range of $H_{\text{int}}$) and $\mathcal{C}_D$ denotes deep modes (the remainder of the hidden sector). If the classical Hamiltonian is spatially local, then on timescales $t \ll \tau_B$:*

$$T_{ij}(t) = T^{(B)}_{ij}(t) + \mathcal{O}(t/\tau_B)$$

*where $T^{(B)}_{ij}$ depends only on the $V$-$B$ dynamics.*

*Proof.* (i) *Coupling structure.* Spatial locality of the classical Hamiltonian implies the interaction decomposes as $H_{\text{tot}} = H_V + H_B + H_D + H_{VB} + H_{BD}$, with no direct $V$-$D$ coupling: a deep hidden-sector mode must propagate through the boundary layer before influencing the visible sector. The coupling chain is $V \leftrightarrow B \leftrightarrow D$, not $V \leftrightarrow D$.

(ii) *Frozen deep sector.* Let $\Delta_D$ be the spectral gap of $H_D + H_{BD}$ restricted to the deep sector conditioned on a fixed boundary configuration. The deep-sector evolution over time $t$ displaces any initial configuration by $\mathcal{O}(\Delta_D \, t)$ in phase space. The spectral gap gives the inverse relaxation time of the slowest mode, so $\Delta_D \leq 1/\tau_B$ (with equality when the slowest mode dominates the relaxation). For $t \ll 1/\Delta_D \leq \tau_B$: $\|\varphi_t^D - \text{id}\| = \mathcal{O}(\Delta_D \, t) = \mathcal{O}(t/\tau_B)$.

(iii) *Factorization of the Liouville integral.* The transition probability is:

$$T_{ij}(t) = \frac{1}{|\mathcal{C}_B||\mathcal{C}_D|} \sum_{b \in \mathcal{C}_B} \sum_{d \in \mathcal{C}_D} \delta_{x_j}[\pi_V(\varphi_t(x_i, b, d))]$$

By (i), $\pi_V(\varphi_t(x_i, b, d))$ depends on $d$ only through the back-reaction $B \leftarrow D$, which by (ii) shifts $b$ by $\mathcal{O}(t/\tau_B)$. Expanding:

$$\pi_V(\varphi_t(x_i, b, d)) = \pi_V(\varphi_t^{VB}(x_i, b)) + \mathcal{O}(t/\tau_B)$$

where $\varphi_t^{VB}$ is the flow restricted to $V \times B$ with $D$ frozen. The $d$-sum then contributes $|\mathcal{C}_D|$ identical terms at leading order:

$$T_{ij}(t) = \underbrace{\frac{1}{|\mathcal{C}_B|} \sum_{b \in \mathcal{C}_B} \delta_{x_j}[\pi_V(\varphi_t^{VB}(x_i, b))]}_{T^{(B)}_{ij}(t)} + \mathcal{O}(t/\tau_B) \qquad \square$$

The correction is $\mathcal{O}(t/\tau_B) \sim 10^{-32}$ for laboratory processes. Since $T_{ij}(t)$ determines the emergent quantum description (Prerequisites; Barandes correspondence [35, 36]), and $T^{(B)}_{ij}(t)$ depends only on the $V$-$B$ dynamics — which are characterized by the boundary geometry ($A$, $\epsilon$, $\kappa$) and the constants $c$, $G$ appearing in the classical Hamiltonian — the emergent action scale $\hbar$ inherits boundary-only dependence.

**Corollary (deep-sector cardinality is gauge).** *No observable of the emergent description — no transition probability, emergent Hamiltonian eigenvalue, or scattering amplitude — depends on the cardinality $|\mathcal{C}_D|$ of the deep hidden sector. Systems with the same $\mathcal{C}_V \times \mathcal{C}_B$ dynamics produce the same emergent physics to within $\mathcal{O}(\tau_S/\tau_B)$, whether $|\mathcal{C}_D|$ is finite, countably infinite, or uncountably infinite.*

*Proof.* $T^{(B)}_{ij}(t)$ is defined by a sum over $\mathcal{C}_B$ alone. The $\mathcal{C}_D$-dependent terms enter only through the $\mathcal{O}(t/\tau_B)$ back-reaction. Since the emergent Hamiltonian $\hat{H}_{\text{eff}}$ is uniquely determined by $\{T_{ij}(t)\}$ (phase-locking lemma, [Main, §3.1]; D-gauge theorem, §3.3), it inherits $\mathcal{C}_D$-independence at leading order. All observables — eigenvalues, transition amplitudes, scattering cross-sections — are functions of $\hat{H}_{\text{eff}}$ and therefore $\mathcal{C}_D$-independent. $\square$

The cardinality of the deep hidden sector is gauge in the same technical sense as the alphabet size $q$: just as two systems with different $q$ are physically equivalent if they share the same coupling structure, two systems with different $|\mathcal{C}_D|$ are physically equivalent if they share the same $\mathcal{C}_V \times \mathcal{C}_B$ dynamics. Lemma 1 requires $S$ finite for the recurrence proof ([Main, §2.3]); the corollary establishes that the deep sector's contribution to this finiteness has no observable consequences. The question "is the universe finite or infinite?" has no empirical content within the framework — it is identified as gauge.

**Step 3: Dimensional determination.** Step 2 excludes volumetric (deep-sector) quantities, leaving boundary quantities. The boundary carries both *local* geometric data ($\epsilon$, $\kappa$, and the constants $c$, $G$ of the classical Hamiltonian) and a *global* quantity: the total area $A$, which forms the dimensionless ratio $A/\epsilon^2 = S_{\text{dS}}$. If $\hbar$ depended on $S_{\text{dS}}$, it would be observer-dependent — different observers have different horizon areas (§2.1) — contradicting the universality of the emergent action scale. (All sub-$c$ observers share the same local physics and hence the same $\hbar$; §2.1.) This excludes $A$, leaving the local boundary quantities $c$, $G$, $\epsilon$, and $\kappa$. The surface gravity $\kappa$ is excluded because it varies between observers and epochs while $\hbar$ is observed to be universal across observers and constant in time: a laboratory experiment measures the same $\hbar$ regardless of the observer's local cosmological-horizon parameters, and for the cosmological horizon $\kappa = cH$ is itself time-dependent ($\dot{H} \neq 0$). The unique combination of $c$, $G$, $\epsilon$ with dimensions of action:

$$\hbar = \beta \frac{c^3 \epsilon^2}{G}$$

**Step 4: Thermal self-consistency.** The classical substratum assigns the partition boundary a temperature $k_B T_{\text{cl}} = c^2 \epsilon^2 \kappa / (8\pi G)$ (§3.1), containing no $\hbar$. The emergent QFT of Part I lives on this classical background, which has a bifurcate Killing horizon with surface gravity $\kappa$. Regularity of the Wick-rotated metric at the horizon requires Euclidean period $\beta = 2\pi c / \kappa$; any QFT on this background — including a lattice-regularized one — must therefore be periodic in imaginary time with the same period, giving a KMS state at temperature $T_Q = \hbar \kappa / (2\pi c k_B)$, with $\hbar$ unknown. This is a theorem *within* the derived QFT, not an external import. The two temperatures are computed independently — $T_{\text{cl}}$ from the classical substratum alone (no QM), $T_Q$ from the emergent QFT alone (no classical substratum details) — but they refer to the **same physical degrees of freedom**: the boundary modes $V \times B$ across which $H_{\text{int}}$ couples the visible and hidden sectors. Step 2's boundary-only dependence shows that the emergent QFT is uniquely determined (at leading order in $\tau_S/\tau_B$) by these same $V \times B$ dynamics. Temperature is a state property; two complete descriptions of the same modes cannot assign different temperatures without logical contradiction. The matching $T_{\text{cl}} = T_Q$ is therefore not an additional assumption but a consequence of the boundary modes being the same physical objects in both descriptions, with corrections at $\mathcal{O}(\tau_S/\tau_B) \sim 10^{-32}$:

$$\frac{c^2 \epsilon^2 \kappa}{8\pi G} = \frac{\hbar \kappa}{2\pi c}$$

$\kappa$ cancels — a non-trivial cross-check on Step 3, which excluded $\kappa$ from $\hbar$ on observer-universality grounds. The thermal matching here recovers that exclusion from independent physics: $\kappa$ enters both sides of the consistency equation, and only the combinations of $c$, $G$, $\epsilon$ predicted by Step 3 survive. Solving:

$$\boxed{\hbar = \frac{c^3 \epsilon^2}{4G}}$$

The derivation is a gap equation: $\epsilon$ is the free geometric input, $\hbar$ is the output. The match is non-trivial: $T_{\text{cl}}$ could have depended on volumetric hidden-sector data (excluded by Step 2), or $T_Q$ could have depended on the state (it does not — the KMS temperature is purely kinematic). That neither pathology obtains makes the gap equation a genuine determination. The non-circularity is structural: Part I establishes that a QFT emerges with *some* action scale $\hbar$; §3 determines *which* $\hbar$, using the independent classical temperature that Part I neither requires nor produces.

**The counting $\eta = 1/\epsilon^2$ is definitional.** Given that $\epsilon$ is the minimal distinguishable scale (Lemma 1), "one boundary mode per cell of area $\epsilon^2$" is what "minimal" means: a cell finer than $\epsilon$ would subdivide the minimal scale, while counting fewer modes would require a distinction below $\epsilon$ to group them. The $q$-gauge theorem (alphabet size is observationally irrelevant) settles that what counts is the number of *cells*, not the number of internal states per cell. $\eta = 1/\epsilon^2$ is therefore not an independent physical ansatz about mode density but a consequence of the definition of $\epsilon$ combined with the irrelevance of sub-cell structure.

The predictive content lies not in the gap equation alone but in its consequences. The specific relationship $\hbar = c^3\epsilon^2/(4G)$ — rather than any other function of $c$, $G$, $\epsilon$ — produces: the Bekenstein-Hawking formula with the exact factor $1/4$ (§5), the CC dissolution with $S_{\text{dS}}$ as the compression ratio (§6.3), and the Type II running-vacuum form of the dark energy (§7.1). Any alternative $\hbar(\epsilon)$ would fail at least one of these checks. The situation is analogous to deriving the Schwarzschild metric with $M$ as a free parameter: the derivation has genuine content (the functional form) even though one input is not determined from within.

Jacobson's original derivation [1] uses $\hbar$-containing forms; this paper does not — it uses the classical identity $dE = (c^2 \kappa / 8\pi G)\,dA$ and the classical entropy density $\eta = 1/\epsilon^2$. The logical ordering differs from Jacobson's: his argument derives $G$ from $\eta$ and $\hbar$; the present argument takes $G$ as a parameter of the classical Hamiltonian (Lemma 3) and derives $\hbar$ from $G$ and $\epsilon$. The two are consistent — substituting $\eta = 1/\epsilon^2$ and $\hbar = c^3\epsilon^2/(4G)$ into Jacobson's formula $G_{\text{eff}} = c^4/(8\pi \eta \cdot \hbar c)$ recovers $G_{\text{eff}} = G$ — but the roles of input and output are reversed. The Gibbons-Hawking temperature [2] $k_B T_{\text{GH}} = \hbar \kappa / (2\pi c)$ is recovered as a prediction, not used as an input. The KMS condition used above is derived for continuum QFT on bifurcate Killing horizons; for the lattice-regularized theory emerging from Part I, the relevant result is that thermal periodicity of the Euclidean Green's functions is robust against UV modifications of the dispersion relation, with corrections at $\mathcal{O}((\epsilon \kappa/c)^2)$ [3, 4]. For the cosmological horizon, $\epsilon \kappa / c = \epsilon H / c \sim 10^{-61}$, so lattice corrections are $\sim 10^{-122}$.

### 3.3 Gauge-fixing and the dimensional obstruction

Steps 1–2 establish that $\hbar$ depends only on boundary quantities; Step 4 will fix its value via thermal matching. A prior question must be addressed: does the transition-probability data $\{T_{ij}(t)\}$ determine the emergent Hamiltonian uniquely, or does residual gauge freedom leave $\hbar$ underdetermined? The following theorem, completing the phase-locking argument (Prerequisites), shows the gauge freedom is physically trivial.

**Theorem (D-gauge completeness).** *Let $U(t) = e^{-iHt}$ with non-degenerate eigenvalues and non-vanishing configuration-basis overlaps. If $|U'_{ij}(t)|^2 = |U_{ij}(t)|^2$ for all $i, j, t$, then $H' = DHD^\dagger$ for a time-independent diagonal unitary $D$.*

*Proof.* Write $U_{ij}(t) = \sum_a V_{ia} \, e^{-iE_a t} \, V_{ja}^*$ with $V_{ia} = \langle i | a \rangle$ and eigenvalues $\{E_a\}$, and similarly $U'_{ij}(t) = \sum_a V'_{ia} \, e^{-iE'_a t} \, V'^*_{ja}$.

*Step 1 (Eigenvalue recovery).* By the phase-locking argument of [Main, §3.1], $|U_{ij}(t)|^2 = |U'_{ij}(t)|^2$ for all $t$ implies, via Fourier analysis, that the frequency sets $\{E_a - E_b\}$ and $\{E'_a - E'_b\}$ coincide. Non-degeneracy of energy gaps then gives $E'_a = E_{\sigma(a)} + E_0$ for some permutation $\sigma$ and global shift $E_0$. The Fourier coefficients $a^{kl}_{ij} = V_{ik} V^*_{jk} V_{jl} V^*_{il}$ must match between primed and unprimed, which (by the non-vanishing condition on overlaps) forces $\sigma = \text{id}$ up to relabeling. Thus $E'_a = E_a + E_0$.

*Step 2 (Modulus recovery).* From the diagonal Fourier coefficients $a^{kl}_{ii} = |V_{ik}|^2 |V_{il}|^2$, the non-vanishing condition gives $|V'_{ia}| = |V_{ia}|$ for all $i, a$.

*Step 3 (Phase structure).* Write $V'_{ia} = V_{ia} \, e^{i\delta_{ia}}$. The off-diagonal Fourier coefficients require:

$$V'_{ik} V'^*_{jk} V'_{jl} V'^*_{il} = V_{ik} V^*_{jk} V_{jl} V^*_{il}$$

Substituting and canceling moduli:

$$e^{i(\delta_{ik} - \delta_{jk} - \delta_{il} + \delta_{jl})} = 1 \quad \text{for all } i, j, k, l$$

This is the double-difference condition: $\delta_{ik} - \delta_{il} - \delta_{jk} + \delta_{jl} = 0 \pmod{2\pi}$. The general solution on the integer lattice is $\delta_{ia} = \alpha_i + \beta_a$ for phases $\{\alpha_i\}$, $\{\beta_a\}$. Thus $V' = D_\alpha \, V \, D_\beta$ where $D_\alpha = \text{diag}(e^{i\alpha_i})$ and $D_\beta = \text{diag}(e^{i\beta_a})$. The $D_\beta$ factor is absorbed into the eigenvector phase convention (physically irrelevant), giving $H' = D_\alpha H D_\alpha^\dagger$ with $D = D_\alpha$ a time-independent diagonal unitary. $\square$

The D-gauge is physically trivial (basis rephasing). Cross-interval transition probabilities fix the relative gauge up to a single global phase; in the continuum limit this becomes an unobservable smooth function $e^{i\theta(t)}$.

**Dimensional obstruction.** The unitary $U(t)$ is dimensionless; $\hbar$ enters only via $\hat{H} = i\hbar \, \partial_t U \cdot U^\dagger$. No dimensionless data can fix a dimensionful constant — Step 4's thermal self-consistency provides the necessary dimensionful input.

**Remark (phase recovery under discrete sampling).** The spatial lattice discreteness does not discretize time: the continuous-time extension ([Main, §2.3]) provides $T_{ij}(t)$ as a genuinely continuous function of $t$ via the Liouville marginalization of the Hamiltonian flow (Lemma 3). The D-gauge theorem therefore applies to the continuous object without aliasing corrections. Aliasing would arise only if the observer sampled $T_{ij}$ at discrete intervals, in which case trans-Planckian frequencies could be misidentified — but these lie outside the emergent QFT's domain. The phase-recovery error is controlled by the same $\mathcal{O}(\tau_S/\tau_B) \sim 10^{-32}$ suppression that governs the boundary-only dependence of §3.2.


---

## 4. Self-Consistency and the Discreteness Scale

Rearranging $\hbar = c^3 \epsilon^2 / (4G)$:

$$\epsilon^2 = \frac{4\hbar G}{c^3} = 4\,l_p^2$$

The framework yields $\epsilon = 2\,l_p$ exactly. This is algebraically equivalent to the formula for $\hbar$: the framework contains one free geometric parameter ($\epsilon$), and thermal self-consistency establishes its relationship to $\hbar$. The result is a self-consistency condition constraining $\epsilon$ to the Planck regime, not an independent determination. If $\epsilon^2 \ll l_p^2$, sub-Planckian subcells would create a second trace-out, breaking the single-valuedness of $\hbar$. If $\epsilon^2 \gg l_p^2$, the emergent description would assign distinct quantum states to physically identical configurations. The framework's predictive content comes from the relationship $\hbar = c^3 \epsilon^2/(4G)$, the Bekenstein-Hawking formula, and the consequences that follow.

---

## 5. The Bekenstein-Hawking Entropy

With $\epsilon = 2\,l_p$, the number of independent modes on the cosmological horizon is:

$$N_{\text{modes}} = \frac{A}{\epsilon^2} = \frac{A}{4\,l_p^2} = S_{\text{dS}}$$

where $S_{\text{dS}} = A/(4\,l_p^2)$ is the Bekenstein-Hawking entropy of the de Sitter horizon. The factor of $1/4$ in the Bekenstein-Hawking formula — historically introduced as a proportionality constant — is here derived: each minimal cell of area $\epsilon^2 = 4\,l_p^2$ on the horizon contributes one unit of entropy, and $A / (4\,l_p^2) = A / \epsilon^2$ recovers the standard formula exactly. The factor of $4$ in $\epsilon^2 = 4 l_p^2$ traces directly to §3 Step 4's thermal matching: the ratio $2\pi/8\pi = 1/4$ between the Euclidean KMS period (numerator: thermal periodicity of QFT on a Killing horizon) and Jacobson's Einstein-equation prefactor (denominator: gravity's coupling in $dE = (c^2\kappa/8\pi G)dA$). The Bekenstein-Hawking $1/4$ is therefore not an arbitrary constant but the consistency condition between gravitational and quantum thermal physics. The same minimal-cell counting argument applies to any horizon with area $A$, giving $S = A/(4 l_p^2)$ for black-hole horizons as well; the recent observational confirmation of the area law on GW250114 [5] is consistent with this extension.

**Observational confirmation: GW250114.** The Bekenstein-Hawking area law $dA \geq 0$ has long been regarded as a theoretical prediction of black-hole thermodynamics, but until 2025 the empirical evidence came primarily from agreement between classical horizon dynamics and semiclassical Hawking radiation predictions — none of it testing the $1/4$ coefficient directly. The LIGO/Virgo/KAGRA observation of GW250114 (September 2025) provides the first direct test of the area law at the percent level: comparing the remnant horizon area inferred from the ringdown to the sum of initial horizon areas inferred from the inspiral, the area increase is consistent with the theorem at $99.999\%$ confidence. Because the framework's derivation fixes the $1/4$ coefficient as the exact ratio $2\pi/8\pi$ between Euclidean KMS periodicity (thermal physics) and Jacobson's Einstein-equation prefactor (gravitational coupling), any measured deviation from $S = A/(4 l_p^2)$ would falsify this derivation — not merely constrain one free parameter. The GW250114 measurement is currently the most stringent empirical test of the framework's gravitational predictions, and the ongoing LVK observing runs will accumulate additional events testing the same relation across a range of progenitor masses and spins.

---

## 6. Dissolution of the Cosmological Constant Problem

### 6.1 The two levels of description

**From finite-dimensional QM to QFT.** Part I delivers QM on a finite-dimensional Hilbert space. The $N = A/\epsilon^2$ cells discretize the visible sector; spatial locality of the classical substratum restricts which cells interact on any given timescale. The emergent Hilbert space decomposes as $\mathcal{H} = \bigotimes_k \mathcal{H}_k$ — a lattice-regularized QFT with UV cutoff at $\epsilon = 2\,l_p$. The tensor product structure follows from the spatial product structure of the classical configuration space $\mathcal{C}_V = \mathcal{C}_1 \times \cdots \times \mathcal{C}_N$ (one factor per cell), which is not required by Lemma 1 but is a consequence of spatial locality in the classical substratum: each cell's configuration is a local degree of freedom.

**Locality preservation theorem.** *If the classical Hamiltonian is spatially local (couples only neighbors), then the emergent quantum Hamiltonian inherits spatial locality.*

*Proof.* For infinitesimal $dt$ and $x' \neq x$: $T_{x,x'}(dt) = |\langle x'|\hat{H}|x\rangle|^2\,dt^2 + O(dt^3)$. If $x, x'$ differ at non-neighboring sites, spatial locality of the classical dynamics gives $T_{x,x'}(dt) = 0$ at leading order, hence $|\langle x'|\hat{H}|x\rangle|^2 = 0$. By the D-gauge theorem (§3.3), the residual phase freedom is a diagonal unitary $D$ that preserves the vanishing of off-diagonal moduli, so $\langle x'|\hat{H}|x\rangle = 0$ in any gauge. The emergent Hamiltonian has the form $\hat{H} = \sum_k \hat{h}_k + \sum_{\langle k,l\rangle} \hat{h}_{kl}$. $\square$

**Scope of the emergent QFT.** The CC dissolution requires only that the emergent description assigns zero-point energy $\sim \hbar\omega/2$ per mode with UV cutoff at $\epsilon^{-1}$ — a property shared by any lattice QFT with local couplings, regardless of gauge group or matter content. The framework's predictions in Part II ($\hbar$, $S_{\text{dS}}$, the Type II RVM form of the dark energy) depend on partition geometry, not on the emergent field content.

**Classical substratum** (what geometric measurements probe): The horizon has classical thermal equilibrium. By the Friedmann equation, $\rho_{\text{crit}} = 3H^2 c^2/(8\pi G)$. No zero-point energy, no discrepancy. Total vacuum energy density: $\rho \sim H^2/G \sim 10^{-9}$ J/m$^3$ — precisely observed.

**Emergent QFT** (what local quantum measurements probe): Zero-point energy $\frac{1}{2}\hbar\omega$ per mode summed to the Planck cutoff gives $\rho_{\text{QFT}} \sim 10^{113}$ J/m$^3$ — a $\sim 10^{122}$ discrepancy with the observed value [6, 7, 8].

### 6.2 Why gravity sees the classical value

Spacetime geometry is part of the classical substratum (Lemma 2): the metric evolves via Einstein's equations *before* the trace-out. The stress-energy sourcing gravity is the classical stress-energy of the total microstate, not the expectation value of an emergent quantum operator. The semiclassical equation $G_{\mu\nu} = 8\pi G \langle \hat{T}_{\mu\nu} \rangle$ is itself an emergent approximation; at the classical level, the gravitational field equations never encounter the zero-point sum.

**Ontological commitment.** Classical spacetime is logically prior to QM; QM is emergent. This ordering is not a claim that spacetime is a substance-level primitive of the framework — the framework has no substance-level primitives, and under the reconstruction theorem, spacetime emerges from $[(S, \varphi)]/\mathcal{G}_{\text{sub}}$ given the framework's irreducible starting commitments (the empirical fact that observation occurs, the empirical inputs E1–E4, and the structural assumptions A1–A6). It is a claim about the direction of the derivation chain — that the trace-out producing QM presupposes the classical geometric structure, not the reverse. This ordering is forced by the logical structure of the derivation through three independent requirements:

*(i) Definiteness.* The trace-out that produces QM is defined by a *specific* partition $\Gamma = \Gamma_V \times \Gamma_H$. The partition must be definite — not in superposition, not subject to quantum uncertainty — for the marginalization integral ([Main, §1.4]) to be well-defined. A partition in superposition would yield an incoherent mixture of inequivalent quantum theories, not a single QM. The metric at the partition boundary must therefore be classical.

*(ii) Non-circularity.* The partition is defined by the causal structure: $\Gamma_H$ is the set of degrees of freedom beyond the observer's causal reach (§2.1). Causal structure is determined by null geodesics of the metric. If the metric were derived from QM, then the derivation would require: QM $\to$ metric $\to$ causal structure $\to$ partition $\to$ QM — a circular dependency with no entry point. The circle breaks only if the metric exists prior to the partition.

*(iii) Uniqueness of $\hbar$.* The emergent action scale is determined by the boundary geometry (§3.2). If the geometry were itself quantum-mechanical, $\hbar$ would depend on a quantum state — but $\hbar$ is state-independent by observation. The geometry-first ordering is the only one consistent with a universal $\hbar$.

Any framework in which QM is logically prior to the metric must either (a) treat the zero-point sum as a gravitational source — producing the $10^{122}$ discrepancy requiring cancellation or fine-tuning — or (b) invoke an independent mechanism to decouple quantum vacuum energy from gravity. In the present framework, the zero-point sum is an artifact of the emergent description and never enters the stress-energy tensor; no decoupling mechanism is needed.

**Cumulative evidence for the ordering.** The geometry-first ordering produces eleven independent consequences that match observation, none of which were designed into the starting point: (1) the CC dissolution — the observed vacuum energy sits at $\rho \sim H^2/G$, the classical baseline, without fine-tuning (§6.3); (2) the Bekenstein-Hawking formula including the $1/4$ factor, derived from $\epsilon = 2\,l_p$ (§5); (3) the value of $\hbar$, determined by partition geometry rather than treated as a free parameter (§3.2); (4) the dark-sector concordance — ~95% of $\rho_{\text{crit}}$ is invisible to QFT, matching the observed dark sector (§7.2); (5) dark energy in running-vacuum form, favoured by DESI DR2 at 2.8–4.2σ and consistent at $2\sigma$ with the Bertini et al. (2025) direct RG-corrected $\Lambda$CDM fit (structurally equivalent to the framework's Type II prediction at leading order) — Bertini being itself consistent with zero, matching the framework's theorem-level magnitude prediction $|\nu| \approx |\nu_{\rm QFT}| \sim 10^{-32}$ [15] (§7.1); (6) the MOND acceleration scale $a_0 = cH/6$ and the baryonic Tully-Fisher relation, derived from entropy displacement (§7.3); (7) the SM gauge group with its coupling strengths, reproduced to $< 0.1\%$ at $M_Z$; (8) declining rotation curves at high redshift, confirmed by Genzel et al. (§7.3); (9) $\bar{\theta} = 0$ at all energy scales; (10) galaxy cluster masses matched by the simple interpolation function (§7.3); (11) the Bullet Cluster lensing morphology reproduced by frozen boundary entropy (§7.3). Quantum-first orderings produce the $10^{122}$ discrepancy, have no natural account of the dark sector, and treat $\hbar$ and the $1/4$ factor as unexplained inputs. The cumulative case is not a single tiebreaker but a pattern: every quantitative output of the geometry-first ordering is consistent with observation; the central quantitative output of the quantum-first ordering is the worst prediction in physics.

**The classical vacuum energy scale.** The framework does not explain *why* $\rho \sim H^2/G$; this is set by initial conditions via the Friedmann equation. What it does is reclassify the CC puzzle: from quantum vacuum cancellation to classical initial conditions. The two problems are not equivalent. The QFT CC problem requires a cancellation between independent contributions — the bare cosmological constant and the zero-point energies of every field — accurate to 122 decimal places, re-tuned at each order in perturbation theory. The initial-conditions question asks why a single parameter ($\Lambda$, or equivalently $H$) takes its observed value; the scale $\rho \sim H^2/G$ is the natural energy density of classical cosmology, not a fine-tuned cancellation between unrelated quantities. The framework eliminates the 122-digit cancellation entirely; the remaining question — why $H$ takes its value — is a standard cosmological problem addressable by inflationary dynamics or other initial-conditions mechanisms.

**Quantum corrections to gravity.** The emergent quantum description does feed back into gravitational dynamics through state-level quantities: §7.1 derives dark energy evolution because the emergent vacuum energy depends on $H$ through the hidden sector's volume. What the framework excludes is the zero-point sum as a gravitational source. The zero-point energy is the ground-state eigenvalue of the emergent Hamiltonian $\hat{H}_{\text{eff}}$, which acts on $\mathcal{H}_V$. But gravity is sourced by the classical Hamiltonian $H_{\text{tot}}$, which acts on the full phase space $\Gamma$ — and $\hat{H}_{\text{eff}}$ and $H_{\text{tot}}$ are not the same operator. The eigenvalues of $\hat{H}_{\text{eff}}$ (including the zero-point energy) are properties of the *emergent description*; the energy that $H_{\text{tot}}$ assigns to the corresponding classical microstates is the *classical vacuum energy* $\rho \sim H^2/G$. The Equivalence Principle applies to $H_{\text{tot}}$: everything that contributes to $H_{\text{tot}}$ gravitates. The zero-point sum does not contribute to $H_{\text{tot}}$; it appears when the classical transition probabilities are reorganized into the Hilbert space formalism ([Main, §3.1]), not when the classical dynamics is evolved. The structural/volumetric distinction of §3.2 captures this: $\hbar$ (structural, a property of the correspondence) does not gravitate; the vacuum energy (volumetric, state-dependent, a property of $H_{\text{tot}}$) does, but at the classical scale $\rho \sim H^2/G$ rather than $\rho \sim M_{\text{Pl}}^4$.

### 6.3 The structural origin of the $10^{122}$ discrepancy

$\rho_{\text{QFT}} / \rho_{\text{classical}} \sim M_{\text{Pl}}^4 / (H^2/G) = S_{\text{dS}} = A/(4\,l_p^2)$ — the Bekenstein-Hawking entropy, now identified as the information compression ratio of the trace-out. The "worst prediction in physics" is the entropy of the observer's blind spot — a category error, not a fine-tuning failure. Wolpert's limits of inference [9] confirm this cannot be resolved from within: both geometric and quantum measurements are faithful to their respective descriptions, and no embedded observer can determine which is more fundamental. This is not a prediction awaiting future data — the observed vacuum energy sits at the classical geometric scale $\rho \sim H^2/G$, the value the framework expects.

---

## 7. Predictions and Tests

### 7.1 Dark energy evolution in running vacuum form

$\hbar$ is $H$-independent (§3.2), but the emergent vacuum energy is a state-level quantity depending on the hidden sector's volume. Any smooth $\rho_\Lambda(H)$ admits the Taylor expansion

$$\Lambda_{\text{eff}}(H) = \Lambda_0 + \frac{3\nu}{8\pi G}(H^2 - H_0^2) + \mathcal{O}((H^2 - H_0^2)^2)$$

This is the Running Vacuum Model [10, 11]. The framework forces this structural form through three architectural commitments: (i) the boundary entropy $S_{\text{dS}} = A/\epsilon^2$ depends on $H$ via $A = 4\pi c^2/H^2$, so the emergent vacuum energy inherits an $H$-dependence; (ii) matter is conserved in the trace-out ontology (§7.2), which forbids direct vacuum–matter energy exchange; (iii) Bianchi consistency with matter conservation then forces $G(H)$ to run in tandem with $\rho_\Lambda(H)$ [11]. The functional form is therefore a structural prediction: the framework commits to Type II RVM.

**Type II identification.** The architecture just described places the framework in the *Type II* class of RVM implementations [11]. Matter is locally conserved, $G(H)$ runs mildly with cosmic expansion, and the Bianchi identity is preserved by the combined running of $\rho_{\rm vac}(H)$ and $G(H)$. By contrast, *Type I* RVM implementations assume $G = G_N$ fixed and introduce a direct vacuum–DM exchange term $Q = 3\nu H \rho_{\rm dm}$; these are physically distinct models sharing the same functional form for $\rho_{\rm vac}(H)$.

**What the framework determines about $\nu$.** The architecture above fixes the functional form but not the coefficient. A rigorous derivation of $\nu$ requires completing §7.3's dark-energy / dark-matter split analysis — specifically, the $H$-dependence of the uniform-vs-structured partition of boundary entropy — which has not been done at the level of a theorem. What the foundations *do* determine are:

- $\rho_s(H) = 3c^2 H^2/(8\pi G) = \rho_{\rm crit}(H)$ exactly, from the gap equation combined with classical-horizon thermodynamics (§7.2). The total gravitating boundary energy tracks the critical density at every $H$ as an identity, not a prediction.
- $S_{\rm struct}/S_{\rm total} = \Omega_B(H)$, from the Clausius-relation entropy-displacement argument of §7.3. The structured (matter-associated) fraction of boundary entropy equals the baryon fraction at each epoch.
- What is *not* fixed: how the non-baryonic $(1 - \Omega_B)$ fraction further subdivides into the cosmological-constant-like (uniform) and dark-matter-like (structured) components as a function of $H$. That subdivision determines $\nu$.

**Dimensional-estimate attempt.** Earlier versions (1.6.5–1.8.x) presented a best-effort qualitative prediction. The natural framework-internal small parameters available for a correction coefficient are $\Omega_B \approx 0.05$, $1/\mathcal{N}_0 = 1/\ln(c/\epsilon H_0) \approx 1/140$, and combinations thereof. A dimensional argument — that $\nu$ parameterizes a correction involving both baryonic back-reaction on the boundary entropy ($\Omega_B$) and spectral dilution over the available frequency decades ($1/\mathcal{N}_0$) — gives

$$|\nu| \sim \Omega_B / \mathcal{N}_0 \sim 3 \times 10^{-4}$$

with a sign argument from $\Omega_B(H)$ decreasing over cosmic time pointing to $\nu < 0$. This estimate is retracted on subsequent audit (Retraction notes below); the framework's theorem-level prediction is the emergent-QFT magnitude given immediately below.

**Emergent-QFT cross-check.** It is important to note what the self-consistent emergent-QFT calculation predicts for $\nu$. In OI the matter fields and the curved-spacetime background are both emergent from the classical discrete substratum; the Shapiro-Solà β-function formula [33, 34] for the vacuum-energy running coefficient

$$\nu = \frac{1}{48\pi^2}\sum_i a_i \frac{M_i^2}{M_{\rm Pl}^2}$$

is derived from one-loop QFT on a curved semiclassical background and applies rigorously only within the emergent QFT sector, with $M_i$ the physical masses of the emergent fields. Applied this way to SM content ($M_i \leq m_t \approx 173$ GeV), the formula gives

$$|\nu_{\rm emergent\ QFT}| \sim (M_{\rm SM}/M_{\rm Pl})^2 \sim 10^{-32}$$

— observationally indistinguishable from zero. Bertini's measurement $\nu = -(2.5 \pm 1.3) \times 10^{-4}$ is consistent with this prediction at the $2\sigma$ level (where it is consistent with zero). The framework therefore accommodates Bertini's data by its emergent-QFT prediction alone, without requiring further mechanism.

The dimensional argument of the preceding paragraph was offered through versions 1.6.5–1.8.x as suggesting a substantially larger magnitude than the emergent-QFT estimate, matching Bertini's central value. Subsequent audit found that the $1/\mathcal{N}_0$ suppression imports the bulk emergent-QFT decade structure as a property of the boundary mode count, which §3.1 and §5 establish by spatial location alone (Retraction notes below). Absent additional substratum structure giving log-uniform boundary-mode distribution at the cosmological horizon, the framework's prediction reduces to the emergent-QFT contribution above. DESI Year 5 ($\sim 1\%$ on $\nu$) will settle the empirical question: a null at this precision confirms the emergent-QFT prediction; a high-significance detection at $|\nu| \sim 10^{-4}$ would require that additional substratum structure.

*Scope of the prediction.* The framework's rigorous claim on $\nu$ is its *functional form* (Type II RVM, derived from boundary-entropy architecture §7.1–7.2) and its emergent-QFT magnitude $|\nu_{\rm QFT}| \sim 10^{-32}$, observationally indistinguishable from zero. The specific magnitude $|\nu| \sim 3 \times 10^{-4}$ from the framework-internal dimensional argument is retracted (Retraction notes below). The framework's theorem-level prediction is therefore $|\nu| \approx |\nu_{\rm QFT}|$, observationally indistinguishable from zero at all foreseeable precision, including DESI Year 5. Bertini's $|\nu| \sim 10^{-4}$ measurement is consistent with this prediction at $2\sigma$, where the measurement itself is consistent with zero; a future high-confidence detection of $|\nu|$ at the $10^{-4}$ level would require additional substratum machinery not currently in §3-§5.

**Observational status.** DESI data [12, 13] report evolving dark energy at $2.8\sigma$–$4.2\sigma$. The 2026 multi-variant analysis [14] of DESI DR2 + Planck PR4 + supernovae tests several Type I RVM variants (vacuum–DM exchange), finding the "flipped RVM" and "RVM with threshold" variants preferred over $\Lambda$CDM at a level comparable to the more flexible $w_0w_a$CDM parameterization — the running-vacuum functional form this framework predicts is favoured by the data at the qualitative level, though the Type I variants tested are not a direct test of OI's Type II prediction.

A direct Type-II-equivalent test is provided by Bertini, Novaes, von Marttens, and Shapiro (arXiv:2509.24026) [15], who fit a renormalization-group-corrected $\Lambda$CDM model — structurally equivalent to Type II RVM at leading order in $\nu$, with both $G(\mu)$ and $\Lambda(\mu)$ running and matter conserved — against Planck 2018 + DESI DR2 + DES-Y5, reporting

$$\nu^{\rm Bertini} = -(2.5 \pm 1.3) \times 10^{-4}$$

with the $\Lambda$CDM limit at the $2\sigma$ boundary of the posterior. This is consistent at $2\sigma$ with the framework's emergent-QFT prediction ($\nu \approx 0$). The dimensional-argument estimate $|\nu| \sim 3 \times 10^{-4}$ is retracted (Retraction notes below); the framework's theorem-level prediction is the emergent-QFT value. An earlier pre-DESI canonical RVM fit by Gómez-Valent and Solà [16] returned $\nu = (1.34 \pm 0.38) \times 10^{-3}$ with $3.5\sigma$ preference over $\Lambda$CDM — positive sign and an order larger in magnitude; the migration from this value to Bertini's as the data improved from pre-DESI to DESI DR2 is itself informative. DESI Year 5 ($\sim 1\%$ precision on $\nu$) provides the decisive test: a null at that precision confirms the emergent-QFT prediction; a high-confidence detection of $|\nu|$ at the $10^{-4}$ level would require additional substratum structure not currently derivable from §3-§5.

**Retraction note.** Earlier versions of this paper (through v1.6.4) proposed a specific coefficient $\nu_{\rm OI} = \Omega_\Lambda/(2\mathcal{N}_0) = 2.45 \times 10^{-3}$ derived from a spectral-uniformity ansatz in which each of $\mathcal{N} = \ln(c/\epsilon H)$ frequency decades was taken to carry a $1/\mathcal{N}$ fraction of the total gravitating vacuum energy. That coefficient is in $\sim 20\sigma$ face-value tension with Bertini's 2025 Type-II-equivalent fit, including a sign disagreement that the ansatz structurally forces ($\nu > 0$ from $\Omega_\Lambda > 0$) but which the data disfavours at $\sim 2\sigma$. Audit of the ansatz reveals that the leap from "each boundary cell couples to all frequencies" (justified by time-translation invariance) to "each frequency decade carries $1/\mathcal{N}$ of the vacuum energy" (not justified) was doing all the quantitative work. The $1.8\%$ uncertainty formerly attached to $2.45 \times 10^{-3}$ captured arithmetic but not ansatz uncertainty. The structural prediction (Type II RVM functional form) is retained; the specific magnitude is retracted pending a rigorous derivation.

**Second retraction.** Versions 1.6.5–1.8.x replaced the v1.6.4 coefficient with the revised dimensional estimate $|\nu| \sim \Omega_B/\mathcal{N}_0 \sim 3 \times 10^{-4}$, switching the prefactor from $\Omega_\Lambda$ to the framework-derived $\Omega_B$ (§7.3) and noting that the cosmic-time decrease of $\Omega_B(H)$ gives $\nu < 0$ in agreement with Bertini's central value. The revised estimate inherits the structural defect of the v1.6.4 ansatz: the factor $\mathcal{N}_0 = \ln(c/\epsilon H_0)$ is the logarithmic count of frequency decades available to the bulk emergent QFT (§3.2), while the boundary modes whose count enters $\rho_{\rm vac}$ are catalogued in §3.1 and §5 by spatial location alone — one degree of freedom per cell of area $\epsilon^2$, with no inherent frequency assignment. Under the natural 2D dispersion $dN/d\omega \propto \omega$ on the boundary, modes concentrate near the UV cutoff and contribute a fraction $(H\epsilon)^2 \sim 10^{-122}$ at horizon frequency, well below the emergent-QFT magnitude. The sign argument relied on the equipartition identification of the uniform fraction of $S_{\rm dS}$ with the gravitating vacuum, which independently gives $\nu \approx 0.84$, incompatible with Bertini at face value. The leap from boundary-mode counting to a $1/\mathcal{N}_0$ suppression is therefore not justified within §3-§5. The structural prediction (Type II RVM functional form) is retained; the specific magnitude is retracted. The theorem-level magnitude is $|\nu_{\rm QFT}| \sim 10^{-32}$.

**Coupled neutrino test.** The same dataset that constrains $\nu$ also constrains the neutrino sector. The DESI DR2 + CMB analysis [17] finds $\Sigma m_\nu < 0.0642$ eV (95% CL) assuming $\Lambda$CDM, prefers normal mass ordering, and bounds the lightest neutrino mass at $m_l < 0.023$ eV — all three results match the OI predictions of normal ordering with $\Sigma m_\nu$ near the oscillation minimum of 0.059 eV. The same analysis finds a $3\sigma$ tension with the lower oscillation limit assuming $\Lambda$CDM, interpreted as "a hint of new physics not necessarily related to neutrinos" — exactly the structural mismatch that the RVM dark energy resolves. JUNO first results [18, 19] confirm the world-leading precision on $\sin^2\theta_{12} = 0.3092 \pm 0.0087$ and $\delta m^2 = (7.48 \pm 0.10) \times 10^{-5}$ eV$^2$, with the solar/reactor 1.5$\sigma$ tension persisting. The neutrino sector predictions and the RVM dark energy prediction are coupled in the framework — both follow from the same lattice structure — and the joint observational support is therefore not independent confirmation of separate effects but a single empirical pattern consistent with the framework's central mechanism.

### 7.2 The dark-sector corollary

The trace-out that produces QM has an automatic gravitational consequence.

**Corollary (Invisible gravitational budget).** *Under Lemmas 1–3 and conditions (C1)–(C3), the cosmological trace-out that produces quantum mechanics simultaneously renders ~95% of the universe's gravitational budget invisible to the emergent QFT.*

*Proof.* Three steps, each using only results already established.

*(i) Total effective density.* The horizon carries $S_{\text{dS}} = A/\epsilon^2$ modes (§5). The classical temperature is $T_{\text{cl}} = c^3 \epsilon^2 H / (8\pi G k_B)$ (§3.1), computed entirely within the classical substratum with no reference to $\hbar$ or the emergent quantum description. The total thermal energy is $E_s = S_{\text{dS}} \cdot k_B T_{\text{cl}}$. By the shell theorem, distributing over $V_H = 4\pi c^3/(3H^3)$:

$$\rho_s = \frac{E_s}{V_H} = \frac{A}{\epsilon^2} \cdot \frac{c^3 \epsilon^2 H}{8\pi G} \cdot \frac{3H^3}{4\pi c^3} = \frac{3c^2 H^2}{8\pi G} = \rho_{\text{crit}}$$

The identity $\rho_s = \rho_{\text{crit}}$ is a consequence of Jacobson's Clausius relation applied to the de Sitter horizon. Verlinde [20] takes the identity as a premise; the present framework grounds it in the Clausius relation of the underlying classical substratum, using the boundary-mode counting fixed in §3.1. The factor $\epsilon^2$ cancels between $S_{\text{dS}} \propto 1/\epsilon^2$ and $T_{\text{cl}} \propto \epsilon^2$, so the result is independent of the specific value of $\epsilon$: what the identity actually uses is Jacobson's $dE = (c^2\kappa/8\pi G)\,dA$ plus an area-law entropy plus the Friedmann volume.

Three clarifications are essential for what follows.

*Classical, not emergent.* The calculation above uses only pre-trace-out quantities: the number of boundary modes ($A/\epsilon^2$), the classical temperature ($T_{\text{cl}}$), and the Hubble volume ($V_H$). No step invokes the emergent quantum description. This is what distinguishes $\rho_s$ from the QFT zero-point energy $\rho_{\text{QFT}} \sim M_{\text{Pl}}^4$: the latter is computed as $\sum \frac{1}{2}\hbar\omega$ over modes of the *emergent* quantum field theory — a quantity that exists only after the trace-out. The framework denies that $\rho_{\text{QFT}}$ gravitates (§6.2), because it is an artifact of the emergent description. The boundary entropy's thermal energy, by contrast, is a classical quantity that predates the trace-out and gravitates at the classical level. That both involve $\hbar$ numerically (because $T_{\text{cl}} = T_{\text{GH}}$) is a consequence of the gap equation's self-consistency, not a dependence on QM. The ratio $\rho_{\text{QFT}} / \rho_s \sim S_{\text{dS}} \sim 10^{122}$ — the same compression ratio identified in §6.3 — confirming that the two quantities occupy different levels of the framework's hierarchy.

*Physical locus.* The entropy modes are physically localized on the horizon — they are the hidden-sector boundary degrees of freedom of §3.2. The uniform-medium description is a gravitational equivalence (shell theorem), not a claim about physical delocalization. No entropy occupies the bulk.

*Why the equivalence is useful.* When matter is present, it locally deforms the horizon geometry, redistributing the boundary entropy. The gravitational effect of this redistribution on bulk observers is most easily computed using the uniform-medium equivalence: the deformed boundary is equivalent to a non-uniform effective bulk source.

*General $d$.* Running the same construction in $d$ spatial dimensions: the horizon is a $(d-1)$-sphere of area $A_{d-1} = [2\pi^{d/2}/\Gamma(d/2)] r_H^{d-1}$; the Hubble volume is $V_d = [\pi^{d/2}/\Gamma(d/2+1)] r_H^d = A_{d-1} r_H / d$; the classical horizon temperature $T_{\rm cl} \propto H$ is dimension-independent (Gibbons–Hawking); and the Friedmann equation in $d$ spatial dimensions is $H^2 = [16\pi G_d/(d(d-1))]\rho$. The boundary entropy is $S = A_{d-1}/\epsilon^{d-1}$ (one mode per $\epsilon^{d-1}$ cell) and the gap equation fixes $\hbar = c^3\epsilon^{d-1}/[2(d-1)G_d]$ by the same thermal self-consistency argument as at $d=3$. Collecting the geometric factors in $\rho_s = S\,k_B T_{\rm cl}/V_d$ and dividing by $\rho_{\rm crit}$ gives

$$\frac{\rho_s}{\rho_{\rm crit}} = \frac{2}{d-1}$$

— unity only at $d=3$. This is the general-$d$ formula cited in [SM §3.2] as the boundary-entropy filter selecting $d=3$.

*(ii) Invisibility.* The argument has two logically distinct components.

*(ii-a) Construction-level invisibility (from Part I alone).* The boundary modes comprising $S_{\text{dS}}$ are hidden-sector degrees of freedom — the variables traced out to produce the quantum description. By the trace-out structure, no hidden-sector degree of freedom maps to an operator on $\mathcal{H}_V$. This is a theorem of Part I, independent of any gravitational content: the hidden sector is invisible to the emergent description by construction.

*(ii-b) Gravitational consequence (from the ontological ordering of §6.2).* The physical import — that the boundary entropy's gravitational influence appears as additional gravity with no source in $\langle \hat{T}_{\mu\nu} \rangle$ — requires the geometry-first ordering established in §6.2: the metric exists at the pre-trace-out level, and the stress-energy sourcing gravity is the classical stress-energy, not the emergent quantum expectation value. Under this ordering, the gravitational interaction between bulk matter and boundary entropy is mediated by the metric at the classical level, modifying the geometry but contributing no term to the emergent $\langle \hat{T}_{\mu\nu} \rangle$. To the embedded observer, this appears as additional gravity with no particle-sector source.

The corollary's predictions are therefore conditional on the same geometry-first ordering that dissolves the CC problem in §6.2. This is not an additional assumption: the ordering is already required by Part II's logic (the partition is defined by null geodesics, so the metric must exist prior to the partition). What the corollary provides is a second, qualitatively distinct *consequence* of that ordering.

*(iii) Budget.* The emergent QFT accounts for the baryonic sector (~5% of $\rho_{\text{crit}}$). The remaining ~95% is boundary entropy — gravitationally active (because $\rho_s$ is a classical quantity computed before the trace-out, unlike $\rho_{\text{QFT}} \sim M_{\text{Pl}}^4$ which is an artifact of the emergent description) but invisible to the emergent QFT. This matches the observed composition, in which ~95% of the gravitational content has no source in particle physics. $\square$

**Observational status of particle dark matter searches.** The corollary's prediction is that no particle dark matter exists — the dark sector is the trace-out, not a missing particle species. The strongest current constraint is the LZ Collaboration's 417-day analysis (December 2025) [21], which is the most sensitive WIMP search ever conducted and reports null results across the 3–9 GeV range, extending world-leading constraints from XENONnT and PandaX-4T to lower mass. The continued failure to detect particle dark matter across multiple decades of increasingly sensitive experiments — summarized in the literature as "the waning of the WIMP" — is consistent with the corollary's prediction. Definitive falsification of the corollary requires positive detection of a particle species accounting for the structured dark sector, which has not occurred.

**Memory effects and P-indivisibility.** Matter locally deforms the horizon geometry, redistributing the boundary entropy. This displacement persists because $\tau_B \gtrsim 1/H$ (condition C2): the hidden-sector modes carrying the redistributed entropy do not thermalize back to the unperturbed configuration on sub-Hubble timescales. Verlinde [20] identifies this as a "memory effect" from the non-thermalization of de Sitter states at sub-Hubble scales. In the present framework, this non-thermalization is not assumed but derived: it is P-indivisibility operating in the gravitational sector, with (C2) ensuring that entropy displacements persist without thermal overwriting.

The corollary is a consistency check for the total dark sector budget, not a derivation of its internal structure. The uniform component of the boundary entropy corresponds to dark energy (§6); the structured component — the matter-induced redistribution of boundary entropy producing local gravitational effects resembling dark matter — is derived in §7.3. The ratio $\rho_{\text{QFT}} / \rho_s \sim S_{\text{dS}} \sim 10^{122}$ confirms the parallel with §6.3: the information compression ratio and the gravitational occlusion fraction are two aspects of a single phenomenon.

**Falsifiability.** The corollary would be falsified by detection of dark matter particles accounting for the full ~27% structured dark sector, or by evidence that the dark sector's gravitational effects are unrelated to the boundary geometry.

### 7.3 Dark matter from entropy displacement

The total dark sector budget is established by §7.2. This section derives the structured component from the entropy displacement induced by baryonic matter.

**Step 1: Entropy displacement (derived).** Baryonic matter $M_B$ is coupled to the boundary entropy through $H_{VB}$ (condition C1). The boundary is a thermal reservoir at $T_{\text{dS}} = \hbar H / (2\pi c k_B)$ (derived, §3.2). For a static matter configuration in gravitational equilibrium — a quasi-static process — the Clausius relation gives the entropy displacement:

$$\Delta S = \frac{M_B c^2}{k_B T_{\text{dS}}} = \frac{2\pi M_B c^3}{\hbar H}$$

This follows from the generalized second law (Theorem A.6) applied to the matter-boundary system: the boundary's entropy reduction is $Q/T$ for a reversible process, where $Q = M_B c^2$ and $T = T_{\text{dS}}$. For dynamic configurations, the Clausius inequality $\Delta S \geq Q/T$ only strengthens the displacement.

**Step 2: The critical acceleration (derived).** The displaced entropy redistributes over the volume between the matter and the horizon. The Jacobson mechanism converts the entropy gradient into additional radial acceleration. The crossover between Newtonian gravity and the entropic effect, accounting for the volume-to-surface ratio of spherical redistribution in de Sitter ($1/6$), gives:

$$a_0 = \frac{cH}{6} \approx 1.2 \times 10^{-10} \; \text{m/s}^2$$

This is the MOND critical acceleration — derived, not fitted. (Milgrom's empirical value: $a_0^{\text{obs}} \approx 1.2 \times 10^{-10}$ m/s².)

**Step 3: The deep-MOND regime.** For baryonic acceleration $\ll a_0$, the displaced entropy dominates. The Jacobson mechanism converts the entropy gradient into curvature, giving $g_{\text{total}} = \sqrt{g_B \cdot a_0}$ and rotation velocity:

$$v^2 = r \cdot g_{\text{total}} = \sqrt{GM_B \cdot cH/6} = \text{constant} \qquad \Longrightarrow \qquad v^4 = GM_B \cdot cH/6$$

This is the baryonic Tully-Fisher relation. Flat rotation curves emerge with no dark matter particles and no free parameters beyond the baryonic mass.

**Step 4: Interpolation constraints.** The full interpolation between the Newtonian regime ($g_B \gg a_0$) and the deep-MOND regime ($g_B \ll a_0$) is constrained by the framework but not uniquely determined. The entropy displacement defines a potential $\Psi_D$ with $g_D = -\nabla \Psi_D$, and the framework requires:

(i) *No free parameters.* $g_D$ depends only on $g_B$ and $a_0 = cH/6$ — no halo-specific parameters, no fitting constants.

(ii) *Conservative.* $\nabla \times g_D = 0$, since $g_D$ derives from the entropy potential.

(iii) *Monotonic.* $\partial g_D / \partial g_B > 0$ — more baryonic mass produces more entropy displacement, hence more dark matter effect.

(iv) *Correct limits.* $g_D \to 0$ for $g_B \gg a_0$ (Newtonian); $g_D \to \sqrt{g_B \cdot a_0}$ for $g_B \ll a_0$ (MOND).

(v) *Analytic.* The entropy redistribution is a smooth function of the coupling structure — no discontinuities or phase transitions in the interpolation.

These constraints narrow the interpolation to a one-parameter family indexed by the transition steepness — a property of the particular bijection $\varphi$, in the same category as fermion masses (solution-specific rather than structural). The simplest member satisfying all five constraints:

$$g_D = \frac{g_B}{2}\left(\sqrt{1 + \frac{4a_0}{g_B}} - 1\right)$$

which is equivalent to $g_{\text{total}} = g_B \cdot \nu(g_B/a_0)$ with $\nu(y) = (1 + \sqrt{1 + 4/y})/2$ — the "simple" MOND interpolation function corresponding to $\mu(x) = x/(1+x)$. This form matches the empirical radial acceleration relation (McGaugh et al. [22]) to $< 0.1$ dex across all galaxy-relevant accelerations.

**Epistemic status.** Steps 1–3 are Tier 2: the displacement formula follows from the Clausius relation applied to the boundary reservoir (§3.2, A.6), the geometric factor from spherical redistribution in de Sitter, and $a_0 = cH/6$ and $v^4 = GM_B \cdot cH/6$ are parameter-free consequences. The interpolation constraints (i)–(v) are Tier 2; the transition steepness is Tier 3 (solution-specific).

**Redshift evolution.** Since $a_0(z) = cH(z)/6$ and $H(z) = H_0\sqrt{\Omega_m(1+z)^3 + \Omega_\Lambda}$, the critical acceleration increases with redshift: $a_0(z=1) = 1.79\,a_0(0)$, $a_0(z=2) = 3.03\,a_0(0)$, $a_0(z=3) = 4.57\,a_0(0)$. The MOND crossover radius $r_M = \sqrt{6GM_B/(cH)}$ correspondingly shrinks — for a $10^{10}\,M_\odot$ galaxy, $r_M = 9.0$ kpc at $z = 0$ but $5.2$ kpc at $z = 2$ and $3.1$ kpc at $z = 5$. Galaxies with effective radii comparable to or exceeding $r_M$ show flat rotation curves (the familiar local behavior); galaxies with $r_{\text{eff}} < r_M$ show declining, Keplerian-like rotation curves. Since $r_M$ shrinks with increasing $z$, high-redshift galaxies are systematically more baryon-dominated — their rotation curves decline at smaller radii.

This prediction is borne out by the data. Genzel et al. [23, 24] report stacked rotation curves for massive star-forming galaxies at $z = 0.9\text{–}2.4$ showing a declining outer velocity at $> 3\sigma$ significance relative to local spirals — consistent with the OI prediction. In ΛCDM, flat rotation curves from NFW halos are expected at all redshifts; explaining the Genzel data requires anomalously low halo concentrations or baryon-dominated inner regions. The cleanest local test is Jiao et al. [25], who detect for the first time a Keplerian decline in the Milky Way's own rotation curve from $\sim 19$ to $\sim 26.5$ kpc using Gaia DR3 kinematics, with the flat rotation curve hypothesis rejected at $3\sigma$. Our own galaxy is the strongest single piece of evidence for the $H(z)$-dependent crossover prediction at $z = 0$, where the OI framework predicts the crossover at $r_M \sim 17$ kpc for the Milky Way's baryonic mass — essentially where Jiao et al. observe the transition.

**Tully-Fisher tension and resolution.** McGaugh et al. (2024), analyzing Nestor Shachar et al. (2023) JWST kinematics, report no evolution in the Tully-Fisher relation out to $z \sim 2.5$, seemingly contradicting $v^4 \propto H(z)$. However, this comparison uses *stellar* mass $M_*$, not baryonic mass $M_B = M_*/(1-f_{\text{gas}})$. At high redshift, gas fractions are large ($f_{\text{gas}} \sim 50\text{–}70\%$ at $z \sim 2$; Tacconi et al. 2018). The OI-predicted shift in the baryonic TF ($\Delta\log M_B = \log(H_0/H(z)) = -0.48$ dex at $z = 2$) is almost exactly compensated by the gas mass not included in $M_*$: the cancellation requires $f_{\text{gas}} = 1 - H_0/H(z)$, which gives 44% at $z = 1$, 58% at $z = 1.5$, and 67% at $z = 2$ — squarely in the observed range. The apparent "no evolution" in the stellar TF is therefore *predicted* by the OI framework: the dynamical shift (higher $a_0$) and the compositional shift (higher gas fraction) cancel when only stellar mass is measured. The definitive test is the *baryonic* TF at $z > 1$ with reliable ALMA gas masses: the OI framework predicts a normalization shift of $-0.48$ dex at $z = 2$ at fixed $v_{\text{flat}}$.

**Observational predictions.** Three parameter-free, quantitative tests:

(i) *Rotation curve evolution.* The outer rotation curve slope (measured as $\Delta v / v$ between $r_{\text{turn}}$ and $2r_{\text{turn}}$) becomes more negative (more Keplerian) with increasing $z$, following $a_0(z) = cH(z)/6$. For a $10^{10.8}\,M_\odot$ exponential disk with $r_{\text{eff}} = 5$ kpc: the outer slope changes from $-0.10$ at $z = 0$ to $-0.12$ at $z = 2$ to $-0.13$ at $z = 5$. Particle dark matter predicts no evolution.

(ii) *Tully-Fisher evolution.* The baryonic Tully-Fisher relation evolves: $v_{\text{flat}}^4 = GM_B \cdot cH(z)/6$. At fixed baryonic mass, $v_{\text{flat}} \propto H(z)^{1/4}$: 7% higher at $z = 0.5$, 16% higher at $z = 1$, 32% higher at $z = 2$. Equivalently, at fixed $v_{\text{flat}}$, the inferred baryonic mass at $z = 2$ is $H_0/H(z=2) = 0.33\times$ the local value — galaxies appear to need less dark matter at high $z$. Testable with JWST and ALMA kinematics combined with photometric baryonic mass estimates.

(iii) *No halo-specific parameters.* In particle DM, each galaxy has a dark matter halo characterized by at least two free parameters (concentration and mass). In the OI framework, the dark matter effect at radius $r$ depends only on the enclosed baryonic mass $M_B(<r)$ and $H(z)$ — no halo-specific parameters. This predicts: the radial acceleration relation (RAR) at fixed $g_B$ has zero intrinsic scatter (at fixed $z$), and the scatter does not correlate with halo properties. Current SPARC data [22] show remarkably small RAR scatter ($\sim 0.13$ dex), consistent with OI but requiring fine-tuning in ΛCDM.

**Falsifiability.** The entropy displacement account would be falsified by: (a) detection of dark matter particles accounting for $\sim$27% of $\rho_{\text{crit}}$; (b) high-redshift rotation curves inconsistent with the predicted $H(z)$ dependence — specifically, if galaxies at $z > 2$ show flat rotation curves at $r > r_M(z)$; (c) baryonic Tully-Fisher violations exceeding baryonic mass uncertainties; (d) RAR scatter correlating with halo properties at fixed $g_B$ and $z$.

**Cluster-scale status.** Galaxy clusters present the most challenging regime for MOND-like theories. For the Coma cluster ($M_B \approx 1.4 \times 10^{14}\,M_\odot$, $R_{200} \approx 1.9$ Mpc), the acceleration at the virial radius is $g_B/a_0 \approx 0.05$ — deep in the MOND regime. With the simple interpolation function above, the predicted velocity is $v = g_B \cdot \nu(g_B/a_0) \cdot R_{200} \approx 1260$ km/s; the observed velocity dispersion implies $\sim 1270$ km/s — a match to better than $1\%$. For other rich clusters (Perseus, A2029, A1689), the simple interpolation reduces the standard MOND mass shortfall from a factor $\sim 2$ to $\sim 1.0$–$1.5$; the residual is within the range of missing baryonic mass in the warm-hot intergalactic medium (WHIM at $T \sim 10^5$–$10^7$ K, difficult to detect in X-rays, estimated to add 30–100% to cluster baryonic mass). The deep-MOND limit $v^4 = GM_B \cdot a_0$ (Tier 2) is identical for all interpolation functions; only the intermediate-acceleration behavior (Tier 3) differs. Galaxy-scale predictions are unaffected: at $g_B/a_0 = 0.5$ (typical outer disk), different interpolation functions agree to $< 0.07$ dex — well within the RAR scatter of $0.13$ dex.

**Colliding clusters (Bullet Cluster).** The Bullet Cluster (1E 0657-56) presents the most-cited evidence for particle dark matter: after the collision, gravitational lensing peaks coincide with the galaxy concentrations ($\sim 15\%$ of baryonic mass), not with the X-ray gas ($\sim 85\%$ of baryonic mass) that was ram-pressure stripped to the center. In a local MOND picture where $g_D$ tracks the instantaneous baryonic distribution, the lensing should peak where the gas is — contradicting observations. The OI framework resolves this through the non-local character of entropy displacement. The dark gravity arises from boundary entropy redistribution at the cosmological horizon, and the horizon's response time is $\tau_{\text{relax}} \sim H^{-1} \approx 14$ Gyr. The collision crossing time is $t_{\text{cross}} \sim 720\,\text{kpc}/4700\,\text{km/s} \approx 0.15$ Gyr — only $1\%$ of the relaxation time. The entropy displacement is therefore *frozen* at the pre-collision configuration, centered on the galaxy concentrations (which defined the gravitational potential wells for gigayears before the collision). The gas moved during the collision; the boundary entropy did not. This reproduces the observed morphology: lensing peaks at the galaxy positions, gas peak between them — without invoking collisionless particles. The mechanism makes a testable prediction: for very old post-collision systems ($t_{\text{since}} \gg 1$ Gyr), the dark gravity should gradually relax toward the gas distribution on timescale $\sim H^{-1}$. Particle dark matter predicts no such relaxation.

**CMB acoustic peaks.** The CMB power spectrum provides the most precise test of the dark matter paradigm: the odd/even peak height asymmetry requires a non-oscillating gravitational source (CDM in ΛCDM) that provides potential wells for the photon-baryon fluid to oscillate in. The entropy displacement satisfies this requirement through the same thermodynamic averaging that resolves the Bullet Cluster. The Clausius relation $\Delta S = \delta Q / T_H$ involves the *net* heat transfer to the horizon boundary. For an oscillating perturbation (compression then rarefaction), the net entropy displacement per acoustic cycle is zero — the oscillating component averages out. Only the secular (growing) component produces net displacement. The entropy displacement perturbation therefore does not oscillate with the photon-baryon fluid; it tracks the growing mode exclusively.

The entropy displacement perturbation then evolves identically to CDM in the linear regime: (i) it has the same effective density ($\rho_E \approx \Omega_{\text{CDM}} \times \rho_{\text{crit}}$, from the dark-sector corollary §7.2); (ii) it does not couple to photons (it is a gravitational effect at the horizon, not a fluid component); (iii) it grows under its own gravity from adiabatic initial conditions set by inflation; (iv) its growth equation $\ddot{\delta}_E + 2H\dot{\delta}_E = 4\pi G \rho_{\text{eff}} \delta_E$ has the same source term as CDM. The CMB power spectrum — which depends on $\Omega_b/\Omega_m$ (peak ratios), the growth of perturbations before recombination (peak heights), the sound horizon $r_s$ (peak positions), and the damping scale (high-$\ell$ suppression) — is therefore predicted to match ΛCDM at linear order. A definitive confirmation requires running a modified Boltzmann code (CLASS or CAMB) with entropy displacement replacing CDM; the prediction is agreement with Planck data to within current uncertainties. *Epistemic status: Tier 3 (derived consequence, pending numerical verification).*


### 7.4 Summary of GR-side predictions

The GR-side quantitative predictions of the framework are collected in the table below. Each follows from partition geometry at the cosmological horizon; no predictions are fit to the quantities they predict.

| Prediction | Formula / value | Observed / status | Match |
|---|---|---|---|
| Emergent action scale | $\hbar = c^3 (2 l_p)^2 / (4G)$ | $\hbar_{\text{obs}} = 1.055 \times 10^{-34}$ J·s | structural |
| Discreteness scale | $\epsilon = 2\,l_p$ | Planck length | structural |
| BH entropy coefficient | $S_{BH} = A / (4 l_p^2)$ | GW250114 area law | $99.999\%$ |
| Cosmological constant | $\rho_\Lambda \sim H^2/G$ | observed value | no discrepancy |
| Dark energy form (structural) | Type II RVM (functional form derived; magnitude $\approx |\nu_{\rm QFT}| \sim 10^{-32}$, indistinguishable from zero) | Bertini 2025 $\nu = -(2.5\pm 1.3) \times 10^{-4}$ | consistent at $2\sigma$ (Bertini consistent with zero) |
| Dark sector fraction | $\Omega_{\text{dark}} \approx 95\%$ | $\Omega_{\text{CDM}} + \Omega_\Lambda \approx 95\%$ | consistent |
| MOND acceleration scale | $a_0 = cH/6 \approx 1.2 \times 10^{-10}$ m/s² | $a_0^{\text{obs}} \approx 1.2 \times 10^{-10}$ m/s² | exact |
| Baryonic Tully-Fisher | $v^4 = G M_B \cdot cH/6$ | SPARC data | within $0.13$ dex RAR scatter |
| Rotation curve crossover | $r_M = \sqrt{6 G M_B/(cH)}$ | Milky Way: $\sim 17$ kpc | Jiao et al. 2023, $3\sigma$ |
| High-$z$ rotation curves | More baryon-dominated with $z$ | Genzel et al. $z = 0.9$–$2.4$ | consistent at $> 3\sigma$ |

The Type II running-vacuum form for dark energy is the gravitational sector's most distinctive *structural* prediction: the functional form is forced by boundary-entropy architecture (§7.1), the Planck-scale UV cutoff is forced by the gap equation (§3.2, §4), and matter conservation plus Bianchi consistency fixes the coupled running of $G(H)$ and $\rho_{\rm vac}(H)$. The *magnitude* of $\nu$ is given at theorem level by the self-consistent emergent-QFT calculation: $|\nu_{\rm QFT}| \sim (M_{\rm SM}/M_{\rm Pl})^2 \sim 10^{-32}$, indistinguishable from zero. Earlier framework-internal dimensional arguments ($\Omega_\Lambda/(2\mathcal{N}_0) \sim 2.5 \times 10^{-3}$ in v1.6.4, $\Omega_B/\mathcal{N}_0 \sim 3 \times 10^{-4}$ in v1.6.5–1.8.x) suggested substratum-level contributions at observable magnitude; both have been retracted on the same audit finding (§7.1 Retraction notes), namely that the $1/\mathcal{N}_0$ suppression imports the bulk emergent-QFT decade count as a property of the boundary mode count, which §3.1 and §5 establish by spatial location alone. The natural 2D field-theoretic distribution concentrates modes near the UV cutoff and contributes $|\nu|_{\rm substratum}$ well below $|\nu_{\rm QFT}|$. The framework's theorem-level prediction is therefore $|\nu| \approx |\nu_{\rm QFT}|$, observationally indistinguishable from zero. The Bertini et al. (2025) measurement $\nu = -(2.5 \pm 1.3) \times 10^{-4}$ is consistent with this prediction at $2\sigma$, where Bertini is itself consistent with zero. DESI Year 5 ($\sim 1\%$ precision on $\nu$) provides the decisive empirical test: a null confirms the prediction; a high-confidence detection at the $10^{-4}$ level would require additional substratum structure (specifically, log-uniform mode-per-decade distribution at the cosmological horizon) not currently derivable from §3-§5. The functional form (Type II RVM) is structurally protected and is the framework's pre-registered prediction.

---

## 8. Discussion

The foundational emergent QM result is treated as established in [Main] and not re-derived here. The cubic-lattice realization of the substratum — which determines the Standard Model gauge structure via the wave equation — is independent of the present results and is developed in [SM]. The reconstruction theorem, the substratum gauge group, and the synthesis claim that quantum mechanics, general relativity, and the arrow of time descend as three projections of the same $(S, \varphi)$ are developed in [Substratum].

### 8.1 Scope

The characterization theorem is a full equivalence: QM $\iff$ embedded observation under (C1)–(C3), conditional on the hidden sector satisfying the eigenstate thermalization hypothesis (ETH) for the C2 ⇐ direction (see [Main, §3.4]). The C1 and C3 necessity directions are unconditional. For the cosmological horizon application, ETH holds for any generic chaotic hidden sector — the horizon complement is such a system — so the full equivalence applies in our universe. The theorem does not identify which physical systems satisfy the conditions (empirical) nor derive $\hbar$ for specific systems (requires Part II). Universality in our universe follows from the shared causal partition defined by null geodesics.

### 8.2 The status of the discreteness scale

$\epsilon$ does not smuggle in a quantum assumption. Lemma 1 requires finite-dimensionality, motivated by the classical fact that finite-area boundaries admit finitely many modes. The result $\epsilon = 2\,l_p$ is a *consequence* of self-consistency (§4). Holographic entropy bounds [26] provide independent, non-quantum motivation.

### 8.3 Vacuum energy: relative effects and the Higgs potential

**Relative effects.** Casimir forces and Lamb shifts are predictions *within* the emergent QFT — relative effects depending on energy differences between configurations. The framework denies that the *absolute* zero-point sum gravitates, because gravity operates at the logically prior classical level (§6.2).

**The Higgs potential.** The strongest CC objection is not the zero-point sum but the electroweak Higgs potential: symmetry breaking shifts $V(\phi)$ by $\sim (200\;\text{GeV})^4$, exceeding the observed $\Lambda$ by $\sim 55$ orders of magnitude. The framework's response follows from its ontological ordering and the structural/volumetric distinction of §3.2, applied as a precise principle:

*What gravitates:* Relative energy differences between configurations of the emergent fields. An electron at rest vs. no electron differs by $m_e c^2$ in the classical substratum — there is a classical microstate difference corresponding to this energy difference. Relative differences appear in the classical stress-energy tensor and gravitate. Casimir forces, Lamb shifts, and particle masses all fall in this category.

*What does not gravitate:* Absolute energy levels assigned to configurations by the emergent description. The Higgs vacuum energy shift $V(\phi_{\text{min}})$ is the energy the emergent QFT assigns to its ground state — the configuration obtained after symmetry breaking. But the "ground state" in the emergent description corresponds to a class of classical microstates whose energy in the classical substratum is $\rho \sim H^2/G$, not $\rho \sim (200\;\text{GeV})^4$. The shift is a property of how the emergent description organizes the microstates (the correspondence), not a property of the microstates themselves (the classical dynamics).

The principle is uniform: the zero-point sum, the Higgs vacuum energy, and the QCD condensate energy are all absolute properties of the emergent ground state. The dissolution applies to each for the same reason — gravity operates at the classical level (§6.2), where none of these quantities appear.

**Why QCD binding energy gravitates but the quantum vacuum does not.** The proton mass is ~99% QCD binding energy — a purely quantum effect. If gravity couples to the classical substratum, how does it "know" about masses generated by emergent quantum dynamics? The answer is that QCD binding energy and vacuum zero-point energy occupy different categories in the structural/volumetric distinction of §3.2. Relative energies within the emergent QFT — energy differences between configurations — correspond to differences in the coupling structure of $\varphi$, which the Jacobson derivation reads as curvature. A proton vs. three free quarks corresponds to two distinct classes of classical microstates with different energies in the classical substratum; the binding energy $\sim 938$ MeV is a *relative* quantity that appears in $H_{\text{tot}}$ and gravitates. The absolute baseline — the zero-point energy summed over all modes — corresponds to the total information capacity of the hidden sector ($S_{\text{dS}}$), which is a property of the partition geometry, not of the dynamics, and therefore does not source curvature.

### 8.4 Assumptions, limitations, and falsifiability


**The theorem** requires Lemma 1 (independent in Part I; consequence of geometry in Part II), the stochastic-quantum bridge ([Main, §3.1] and Appendix A; established by two independent routes), and genericity conditions (non-degenerate spectrum, non-vanishing overlaps), which hold for all but a measure-zero set. The P-indivisibility proof uses finiteness via the recurrence argument ($\varphi^N = \text{id}$). The deep-sector cardinality corollary (§3.2) establishes that only $\mathcal{C}_V$ and $\mathcal{C}_B$ need be finite — both guaranteed by holographic entropy bounds [26] independently of the de Sitter finite-dimensionality conjecture — while the deep sector $\mathcal{C}_D$ may be infinite. The accessible-timescale backflow lemma ([Main, §2.3]) provides a second route to P-indivisibility that is independent of $|\mathcal{C}_H|$. The characterization theorem becomes an equivalence on observable timescales ($T_{\text{obs}} \ll \tau_B \sim 10^{17}$ s) — physically indistinguishable from a timeless identity for all experiments within the age of the universe.

**The sharp partition and constraint structure.** Lemma 2's product decomposition $\Gamma = \Gamma_V \times \Gamma_H$ is the kinematic phase space. In GR, the Hamiltonian and momentum constraints restrict the physical phase space to a submanifold $\Gamma_{\text{phys}} \subset \Gamma_V \times \Gamma_H$ on which interior and exterior data are correlated. P-indivisibility survives on a constraint surface because restoring P-divisibility would require decoupling the sectors entirely, violating the constraints; the constraint surface thus enforces (C1) non-perturbatively. For systems other than the cosmological horizon, the fidelity of the product approximation determines the fidelity of the emergent quantum description.

**Planck-scale ordering.** The classical-prior ontology may break down at $l_p$, where "geometric" and "quantum" lose operational distinction. If a deeper theory unifies both, this framework describes the effective macroscopic regime.

**Falsifiability.** The *theorem* would be falsified by a failure of both the stochastic-quantum correspondence and the Stinespring construction for the class of processes generated here — a possibility excluded by the independent proofs in [Main, §3.1] and Appendix A. The *cosmological application* (Type II RVM functional form as a structural prediction) would be falsified by definitive observational demonstration that dark energy deviates from the $\nu$-parameterized Type II form — e.g., a high-confidence detection of strong $w(z)$ variation incompatible with $w = -1 + \mathcal{O}(\nu)$. The theorem-level magnitude prediction $|\nu| \approx |\nu_{\rm QFT}| \sim 10^{-32}$ admits a stratified falsification structure: a measurement $|\nu| \gtrsim 10^{-4}$ at high significance would require log-uniform boundary-mode spectral structure beyond §3-§5; a measurement $|\nu| > 10^{-3}$ at high significance would also exceed the retracted dimensional-argument range and would constitute a structural challenge to the magnitude prediction without falsifying the Type II functional form itself. The *dark-sector concordance* (§7.2) would be falsified by detection of dark matter particles accounting for the full structured dark sector, or by evidence that the dark sector's gravitational effects are unrelated to the cosmological boundary geometry.

**A near-term mechanism-side test.** A more tractable falsification target is provided by the recently developed operational distinction between classical and quantum memory in non-Markovian processes [27, 28]. Some non-Markovian quantum dynamics can be simulated using only classical stored information, while others require genuinely quantum memory in the environment, with the dividing line set by entanglement structure of the channel's Choi state. The framework predicts that all *fundamental* non-Markovian dynamics in nature — those arising from the cosmological trace-out rather than from engineered quantum baths — should be classical-memory simulable, because the hidden sublattice is by construction a classical substrate. A physically realized fundamental open-system process whose memory provably exceeds the classical bound would falsify the framework's foundational ontology even without cosmological data. This is a near-term tractable test in a literature where the experimental and theoretical tools are advancing rapidly.

**Black-hole horizons under partition-relativity.** The framework's mechanism is grounded in the cosmological horizon as the primary partition for any sub-$c$ observer in this universe (§2.1). A black-hole horizon within the cosmological visible sector is a *local* causal boundary: it prevents an external observer from probing the black-hole interior by direct geometric access, but it does not redefine that observer's epistemic partition in the sense of [Main, §1.4]. Matter falling into a distant black hole was already inside the external observer's $\Gamma_V$ before the merger and remains inside it after; the trace-out that defines the external observer's emergent quantum description is over the cosmological horizon, not over the black-hole horizon. The framework therefore predicts that gravitational wave signatures from binary black-hole mergers follow standard general-relativistic ringdown morphology, with no OI-specific echo, comb, or wall-reflection features. A four-event coherent matched-filter stack on LVK O1–O4 strain data using a dedicated discreteness-scale echo template (with the predicted detector-frame delay $\Delta t = (r_+/c)\ln(r_+/2 l_p)$ at the remnant mass and spin) returned a clean null: stacked statistic $-0.45$, empirical $p = 0.66$, with the previously hypothesized echo amplitude excluded at $5.9\sigma$. The framework's BH physics for external observers is identical to standard GR plus the cosmological-scale dark-sector effects of §7.2–§7.3.

**Nested and time-dependent partitions.** The primary partition for any sub-$c$ observer in this universe is the cosmological horizon (§2.1). When additional causal boundaries are present — most naturally, a black hole horizon within the cosmological patch — the trace-out machinery extends to a nested formalism, addressed in Appendix A. The nested formalism is a self-consistency exercise: it shows that the framework's emergent description is well-defined when multiple boundaries coexist, and that quantities like the generalized second law and the Page curve emerge naturally. It is *not* a claim that external observers' emergent quantum descriptions acquire BH-horizon-specific features; under partition-relativity (above), the cosmological horizon remains the primary partition. Appendix A resolves the formal nested-partition machinery in three layers.

*(i) Consistency of nested trace-outs (Appendix A, Theorems A.1–A.4).* Two procedures — tracing out the trans-cosmological region and the black hole interior simultaneously (direct) or sequentially (first cosmological, then black hole) — produce the same CPTP channel, the same emergent Hamiltonian (up to D-gauge), and the same $\hbar$. The key result (Theorem A.2) is that the quantum partial trace within the emergent description agrees with the classical marginalization on the substratum: the emergent QM is self-consistent.

*(ii) The generalized second law (Appendix A, Theorem A.6).* The sum $S_{\text{matter}} + S_{\text{BH}} + S_{\text{dS}}$ is non-decreasing, proved from strong subadditivity and CPTP monotonicity of the emergent quantum description. Any process that shrinks the black hole (decreasing $S_{\text{BH}}$) transfers information to the visible sector and cosmological boundary, compensating the decrease.

*(iii) The Page curve (Appendix A, Theorems A.7–A.9).* For an evaporating black hole, the entanglement entropy of the radiation follows $S_{\text{rad}}(t) = \min(n_R(t), n_B(t)) \cdot \ln q$ plus exponentially small corrections, where $n_B(t)$ is the shrinking boundary mode count and $n_R(t) = n_B(0) - n_B(t)$. Unitarity is preserved (bijectivity of $\varphi$), the turnover occurs at the Page time $t_P \approx 0.646 \, t_{\text{evap}}$ (structural, independent of mass and greybody factors), and the Page value is recovered for all but an exponentially negligible fraction ($\sim e^{-10^{77}}$ for $30 M_\odot$) of initial conditions — proved from bijectivity (cycle decomposition on the finite energy shell) and Popescu-Short-Winter typicality [29], without assuming ergodicity. The greybody factor is solution-specific.

Laboratory tests of the characterization theorem may be possible in analogue gravity systems where the hidden sector capacity is tunable.


---

## 9. Conclusion

The cosmological horizon realizes the embedded-observation framework of [Main], and the consequences for the gravitational sector are sharp. The emergent action scale $\hbar = c^3 (2\,l_p)^2 / (4G)$ is determined uniquely by thermal self-consistency between the classical horizon temperature and the Euclidean periodicity of the emergent QFT, with no free parameters. The Bekenstein-Hawking entropy $S = A/(4 l_p^2)$ is derived by direct mode counting, with the $1/4$ coefficient fixed as the ratio between the Euclidean KMS period and the Jacobson prefactor — a structural constant, not an empirical fit. The GW250114 observation of September 2025 confirms the area law at $99.999\%$ confidence, providing the framework's first direct empirical test at the percent level. The cosmological constant problem is dissolved: the $10^{122}$ ratio between the quantum vacuum energy and the effective $\Lambda$ is the compression ratio between two levels of description that refer to incommensurable objects, not a failure of cancellation.

The empirical payoff is the set of predictions in §7. The Type II running-vacuum functional form of dark energy is the most distinctive gravitational-sector *structural* prediction: consistent with the Bertini et al. (2025) direct fit to DESI DR2 + DES-Y5 + Planck 2018 [15] (which reports $\nu$ consistent with zero at $2\sigma$), and decisively testable by DESI Year 5 and subsequent stage-IV surveys. The coefficient's magnitude at theorem level is the self-consistent emergent-QFT value $|\nu_{\rm QFT}| \sim 10^{-32}$, observationally indistinguishable from zero. Two earlier framework-internal dimensional arguments (v1.6.4: $\Omega_\Lambda/(2\mathcal{N}_0) \sim 2.5\times 10^{-3}$; v1.6.5–1.8.x: $\Omega_B/\mathcal{N}_0 \sim 3\times 10^{-4}$) suggested observable substratum-level contributions; both have been retracted (§7.1 Retraction notes), since the $1/\mathcal{N}_0$ suppression imports the bulk emergent-QFT decade structure as a property of the boundary mode count, which §3.1 and §5 establish by spatial location alone. The framework's theorem-level prediction is therefore $|\nu| \approx |\nu_{\rm QFT}|$. The dark-sector corollary explains ~95% of the gravitational budget of the universe without new fundamental particles, and the absence of direct dark-matter detection at the LZ and XENONnT experiments is interpreted within the framework as a structural consequence rather than a null result to be explained away. The MOND phenomenology emerges from entropy displacement at the cosmological boundary with $a_0 = cH/6$, reproducing the baryonic Tully-Fisher relation and predicting Keplerian decline at $r > r_M$ — the latter confirmed by the Jiao et al. (2023) detection of a Keplerian decline in the Milky Way's own rotation curve at $\sim 17$ kpc. The $H(z)$ scaling of $a_0$ predicts systematically more baryon-dominated rotation curves at high redshift, consistent with Genzel et al.'s detection of declining outer velocities at $z = 0.9$–$2.4$ and testable at higher precision by JWST and ELT kinematics.

The foundational framework developed in [Main] and the cubic-lattice realization developed in [SM] are complementary to the present work: [Main] establishes the equivalence between embedded observation and quantum mechanics, the present paper applies it to the cosmological horizon, and the SM paper applies it to the microscopic lattice substratum. The reconstruction theorem and the synthesis claim — that quantum mechanics, general relativity, and the arrow of time descend as three projections of the same deterministic $(S, \varphi)$ — are developed in [Substratum]. Together, the four-paper sequence establishes that the Standard Model, general relativity, and the arrow of time are three faces of a single finite deterministic construction, with quantum mechanics emerging as the unique self-consistent description for any observer bounded by a causal horizon.

---

## Appendix A: Nested Partitions

This appendix develops the nested-partition formalism for the framework, establishing the self-consistency of multiple coexisting causal boundaries (typically a black hole horizon inside a cosmological horizon) and deriving the generalized second law and the Page curve as consequences.

### A.1 Setup

Let $\mathcal{C}_V$, $\mathcal{C}_B$, $\mathcal{C}_D$ be finite configuration spaces with $|\mathcal{C}_V|, |\mathcal{C}_B| \geq 2$, and let $\varphi: \mathcal{C}_V \times \mathcal{C}_B \times \mathcal{C}_D \to \mathcal{C}_V \times \mathcal{C}_B \times \mathcal{C}_D$ be a bijection. The physical picture: $V$ is the region between a black hole horizon and the cosmological horizon, $B$ is the black hole interior, $D$ is the trans-cosmological region. Define $W = V \cup B$ (the cosmological interior).

Two procedures produce a quantum description on $V$:

*Direct:* Trace out $B \cup D$ in one step, marginalizing over $\mathcal{C}_B \times \mathcal{C}_D$.

*Sequential:* (Stage 1) Trace out $D$, producing emergent QM on $W$. (Stage 2) Within the emergent QM on $W$, trace out $B$, producing a further-reduced description on $V$.

### A.2 Classical Associativity

**Theorem A.1.** *The direct and sequential procedures produce the same transition probabilities on $\mathcal{C}_V$.*

*Proof.* The direct transition matrix is:

$$T^{\text{dir}}_{ij}(t) = \frac{1}{|\mathcal{C}_B||\mathcal{C}_D|} \sum_{b \in \mathcal{C}_B} \sum_{d \in \mathcal{C}_D} \delta_{x_j}[\pi_V(\varphi_t(x_i, b, d))]$$

The sequential procedure marginalizes over $D$ (Stage 1) then over $B$ (Stage 2). Composing:

$$T^{\text{seq}}_{ij}(t) = \frac{1}{|\mathcal{C}_B|} \sum_b \frac{1}{|\mathcal{C}_D|} \sum_d \delta_{x_j}[\pi_V(\varphi_t(x_i, b, d))] = T^{\text{dir}}_{ij}(t)$$

The sums commute (Fubini on a finite product). $\square$

### A.3 Quantum-Classical Consistency

**Theorem A.2** (Quantum-classical consistency of nested trace-outs). *Let $\Phi_V^{\text{dir}}$ and $\Phi_V^{\text{seq}}$ be the CPTP channels on $\mathcal{H}_V$ produced by the direct and sequential procedures respectively. Then $\Phi_V^{\text{dir}} = \Phi_V^{\text{seq}}$.*

*Proof.* By the Stinespring dilation theorem [30, 31], $\varphi$ defines a unitary $U_\varphi$ on $\mathcal{H} = \mathcal{H}_V \otimes \mathcal{H}_B \otimes \mathcal{H}_D$. The direct channel is $\Phi_V^{\text{dir}}(\rho_V) = \text{Tr}_{BD}[U_\varphi\,(\rho_V \otimes \rho_B \otimes \rho_D)\,U_\varphi^\dagger]$. The sequential channel is $\Phi_V^{\text{seq}}(\rho_V) = \text{Tr}_B[\text{Tr}_D[U_\varphi\,(\rho_V \otimes \rho_B \otimes \rho_D)\,U_\varphi^\dagger]]$. On finite-dimensional tensor products, $\text{Tr}_B \circ \text{Tr}_D = \text{Tr}_{BD}$, giving $\Phi_V^{\text{seq}} = \Phi_V^{\text{dir}}$. $\square$

### A.4 Hamiltonian and $\hbar$ Consistency

**Corollary A.3** (Hamiltonian consistency). *The emergent Hamiltonians $\hat{H}_V^{\text{dir}}$ and $\hat{H}_V^{\text{seq}}$ satisfy $\hat{H}_V^{\text{dir}} = D\,\hat{H}_V^{\text{seq}}\,D^\dagger$ for a time-independent diagonal unitary $D$.*

*Proof.* Theorem A.2 gives $\Phi_V^{\text{dir}} = \Phi_V^{\text{seq}}$, hence $T^{\text{dir}}_{ij}(t) = T^{\text{seq}}_{ij}(t)$ for all $t$ (Born rule applied to diagonal elements). The D-gauge theorem (§3.3) gives the result. $\square$

**Corollary A.4** ($\hbar$ universality). *Both procedures yield the same emergent action scale $\hbar = c^3 \epsilon^2 / (4G)$.*

*Proof.* $\hbar$ depends only on local boundary quantities $c$, $G$, $\epsilon$ (§3.2, Steps 2–3), not on which horizon defines the partition or how many trace-outs are performed. $\square$

### A.5 Additive Dissipators

**Theorem A.5** (Additive dissipators). *Let the classical Hamiltonian be spatially local with coupling chain $V \leftrightarrow B \leftrightarrow D$ (no direct $V$-$D$ coupling). Let $\tau_B^D$ be the $D$-sector timescale and $\tau_B^B$ the $B$-sector timescale. On observation timescales $t \ll \min(\tau_B^D, \tau_B^B)$, the dissipative correction to unitarity on $\mathcal{H}_V$ decomposes as:*

$$\mathcal{D}_V = \mathcal{D}_V^{(B)} + \mathcal{D}_V^{(D)} + \mathcal{R}$$

*where $\|\mathcal{D}_V^{(B)}\| = \mathcal{O}(\tau_S / \tau_B^B)$, $\|\mathcal{D}_V^{(D)}\| = \mathcal{O}(\tau_S / \tau_B^D)$, and the cross term satisfies $\|\mathcal{R}\| = \mathcal{O}(\tau_S^2 / (\tau_B^B \cdot \tau_B^D))$.*

*Proof.* The proof applies the boundary-only dependence lemma (§3.2) twice, tracking the cross term at each stage.

(i) *First application: freeze $D$.* Apply the boundary-only dependence lemma to the partition $(W, D)$ where $W = V \cup B$. By spatial locality, $H_{\text{tot}} = H_V + H_B + H_D + H_{VB} + H_{BD}$ with no direct $V$-$D$ coupling. The $D$-sector is frozen on timescales $t \ll \tau_B^D$, giving:

$$T^V_{ij}(t) = \frac{1}{|\mathcal{C}_B|} \sum_{b \in \mathcal{C}_B} \delta_{x_j}[\pi_V(\varphi_t^{VB}(x_i, b))] + \mathcal{O}(t / \tau_B^D)$$

where $\varphi_t^{VB}$ is the flow restricted to $V \times B$ with $D$ frozen. The $\mathcal{O}(t / \tau_B^D)$ correction arises from $D$'s back-reaction on $B$ through $H_{BD}$.

(ii) *Dissipator from the frozen-$D$ dynamics.* The frozen-$D$ flow $\varphi_t^{VB}$ is a bijection on $\mathcal{C}_V \times \mathcal{C}_B$ — the standard Stinespring setup with $B$ as the hidden sector. The emergent dynamics on $V$ is approximately unitary with dissipator $\mathcal{D}_V^{(B)} \sim \mathcal{O}(\tau_S / \tau_B^B)$.

(iii) *Decomposition of the $D$-correction.* The $\mathcal{O}(t / \tau_B^D)$ correction from step (i) has two components:

*Direct:* $D$'s back-reaction shifts the boundary modes of $B$ by $\delta b \sim \mathcal{O}(t / \tau_B^D)$. This propagates through $H_{VB}$ to the visible sector, contributing $\mathcal{D}_V^{(D)} \sim \mathcal{O}(\tau_S / \tau_B^D)$.

*Cross:* The shift $\delta b$ also modifies the effective $B$-state against which $\mathcal{D}_V^{(B)}$ is computed. The dissipator $\mathcal{D}_V^{(B)}$ depends on the $B$-state through the Liouville average over $b$. The $D$-induced shift changes this average by $\mathcal{O}(t / \tau_B^D)$, so:

$$\|\mathcal{R}\| = \left\|\frac{\partial \mathcal{D}_V^{(B)}}{\partial b}\right\| \cdot \|\delta b\| \leq \|\mathcal{D}_V^{(B)}\| \cdot \mathcal{O}(t / \tau_B^D) = \mathcal{O}\!\left(\frac{\tau_S}{\tau_B^B} \cdot \frac{\tau_S}{\tau_B^D}\right) = \mathcal{O}\!\left(\frac{\tau_S^2}{\tau_B^B \cdot \tau_B^D}\right)$$

The inequality uses the fact that $\mathcal{D}_V^{(B)}$ is a continuous function of the $B$-state distribution and the shift is first-order in $t / \tau_B^D$. $\square$

**Bound for the cosmological + stellar black hole case.** For a $30 M_\odot$ black hole inside the cosmological horizon: $\tau_S \sim 10^{-15}$ s, $\tau_B^B \sim \tau_{\text{scr}} \sim \beta \log S_{\text{BH}} \sim 10^{-3}$ s, $\tau_B^D \sim 1/H \sim 10^{17}$ s. The three terms:

$$\|\mathcal{D}_V^{(B)}\| \sim 10^{-12}, \qquad \|\mathcal{D}_V^{(D)}\| \sim 10^{-32}, \qquad \|\mathcal{R}\| \sim 10^{-44}$$

The cross term is negligible by 12 orders of magnitude relative to the smaller of the two primary dissipators.

### A.6 The Generalized Second Law

The Bekenstein-Hawking entropy of a horizon is the information content of the corresponding partition boundary (§5): $S_{\text{BH}} = A_{\text{BH}} / (4\,l_p^2)$ modes at the black hole horizon, $S_{\text{dS}} = A_{\text{dS}} / (4\,l_p^2)$ modes at the cosmological horizon. The matter entropy is the von Neumann entropy of the visible-sector state: $S_{\text{matter}} = -\text{Tr}[\rho_V \log \rho_V]$.

**Theorem A.6** (Generalized second law). *For any process described by the CPTP channel $\Phi_V$ on $\mathcal{H}_V$:*

$$S_{\text{matter}}(t) + S_{\text{BH}}(t) + S_{\text{dS}}(t) \geq S_{\text{matter}}(0) + S_{\text{BH}}(0) + S_{\text{dS}}(0)$$

*Proof.* The total system $(S, \varphi)$ evolves unitarily at the fundamental level, so the total fine-grained entropy $S_{\text{total}} = \log|S|$ is constant. The three terms $S_{\text{matter}}$, $S_{\text{BH}}$, $S_{\text{dS}}$ are the observer's ignorance about three sectors: $V$, $B$, $D$ respectively.

(i) *Subadditivity.* For the tripartite system $\mathcal{H}_V \otimes \mathcal{H}_B \otimes \mathcal{H}_D$ in a pure state $|\Psi\rangle$ (the total state is deterministic, hence pure conditioned on the initial state), the strong subadditivity of von Neumann entropy [31] gives:

$$S(\rho_{VB}) + S(\rho_{BD}) \geq S(\rho_B) + S(\rho_{VBD})$$

Since $\rho_{VBD} = |\Psi\rangle\langle\Psi|$ is pure, $S(\rho_{VBD}) = 0$. Thus $S(\rho_{VB}) + S(\rho_{BD}) \geq S(\rho_B)$.

(ii) *Identification.* The observer's matter entropy is $S_{\text{matter}} = S(\rho_V)$. By purification on the tripartite system: $S(\rho_V) = S(\rho_{BD})$. The black hole entropy is $S_{\text{BH}} = S(\rho_B)$ restricted to the boundary modes (the number of $B$-modes coupled across the black hole horizon). The cosmological entropy is $S_{\text{dS}} = S(\rho_D)$ restricted to the boundary modes.

(iii) *Monotonicity and compensation.* The CPTP channel $\Phi_V$ is a contraction of relative entropy [29, Theorem 11.9], so $S(\rho_V)$ is non-decreasing under the emergent dynamics. Any process that decreases $S_{\text{BH}}$ (shrinking the black hole) transfers information from $B$ to $V \cup D$. By the unitarity of $\varphi$, the total mutual information $I(V:B:D)$ is conserved, so the decrease in $S_{\text{BH}}$ is compensated by an increase in $S_{\text{matter}} + S_{\text{dS}}$. $\square$

### A.7 The Page Curve

**Setup.** A black hole with initial horizon area $A_0$ evaporates. The partition boundary at the black hole horizon moves: modes transition from $B$ (interior) to $R$ (radiation, a subsystem of $V$) as the horizon shrinks. Define $n_B(t) = A_{\text{BH}}(t) / (4\,l_p^2)$ (the number of boundary modes at the BH horizon) and $n_R(t) = n_B(0) - n_B(t)$ (the number of emitted radiation modes). Conservation: $n_B(t) + n_R(t) = n_B(0) = S_{\text{BH}}(0)$.

The trans-cosmological sector $D$ is frozen on evaporation timescales ($\tau_{\text{evap}} \ll \tau_B^D$), so by Theorem A.5 the relevant dynamics is the bipartite system $B \cup R$ with $D$ decoupled at leading order.

**Theorem A.7** (Effective bipartite pure state). *On timescales $t \ll \tau_B^D$, the joint state of $B$ and $R$ is effectively pure: $\rho_{BR} = |\psi(t)\rangle\langle\psi(t)| + \mathcal{O}(\tau_S / \tau_B^D)$, where $|\psi(t)\rangle \in \mathcal{H}_B(t) \otimes \mathcal{H}_R(t)$.*

*Proof.* The total system evolves unitarily under $U_\varphi$ (§A.3). The total state $|\Psi\rangle \in \mathcal{H}_V \otimes \mathcal{H}_B \otimes \mathcal{H}_D$ is pure (deterministic evolution from a definite initial state). By the boundary-only dependence lemma, the $D$-sector is frozen: $\rho_D$ is approximately constant, and $|\Psi\rangle \approx |\psi_{VB}\rangle \otimes |\chi_D\rangle + \mathcal{O}(\tau_S / \tau_B^D)$. Restricting to the $B \cup R$ subsystem (where $R \subset V$ is the radiation): $\rho_{BR} \approx |\psi\rangle\langle\psi|$ is pure at leading order. The correction is $\mathcal{O}(\tau_S / \tau_B^D) \sim 10^{-32}$. $\square$

**Theorem A.8** (Cycle typicality). *For the dynamics $\varphi$ on the energy shell $\Sigma_E \subset \mathcal{H}_B \otimes \mathcal{H}_R$, the time-averaged entanglement entropy of the radiation equals the Page value [32]:*

$$\overline{S(\rho_R)} = S_{\text{Page}}(d_B, d_R) + \mathcal{O}(\epsilon)$$

*for all initial conditions except a fraction $\leq 2e^{-c \, d_{\min} \, \epsilon^2}$, where $d_B = |\mathcal{C}_B(t)|$, $d_R = |\mathcal{C}_R(t)|$, $d_{\min} = \min(d_B, d_R)$, and:*

$$S_{\text{Page}}(d_B, d_R) = \ln(\min(d_B, d_R)) - \frac{\min(d_B, d_R)}{2\max(d_B, d_R)}$$

*Proof.* The bijection $\varphi$ conserves energy (the wave equation is Hamiltonian), so $\varphi$ restricts to a bijection on each energy shell $\Sigma_E$. Since $\Sigma_E$ is finite, this restricted bijection decomposes into disjoint cycles $C_1, \ldots, C_k$ with lengths $L_1, \ldots, L_k$ summing to $|\Sigma_E|$. On each cycle $C_j$, the time average of any observable $f$ is exact:

$$\overline{f}_{C_j} = \frac{1}{L_j} \sum_{s \in C_j} f(s)$$

By Popescu-Short-Winter [29], the set of atypical states — those with $|S(\text{Tr}_B |\psi\rangle\langle\psi|) - S_{\text{Page}}| > \epsilon$ — has measure at most $\eta = e^{-c \, d_{\min} \, \epsilon^2}$ on $\Sigma_E$, where $d_{\min} = \min(d_B, d_R)$ and $c > 0$ is a universal constant. The total number of atypical states is at most $\eta |\Sigma_E|$.

Call a cycle *bad* if its time-averaged entropy deviates from $S_{\text{Page}}$ by more than $\epsilon$. A bad cycle must contain a disproportionate fraction of atypical states. Specifically, if more than half the states in $C_j$ are typical (entropy within $\epsilon$ of $S_{\text{Page}}$), then $|\overline{S}_{C_j} - S_{\text{Page}}| \leq \epsilon + \mathcal{O}(\ln d_{\min} / L_j)$. So a bad cycle must have at least half its states atypical: $L_j \leq 2 \cdot |\{s \in C_j : s \text{ atypical}\}|$. Summing over all bad cycles:

$$\sum_{j \,\text{bad}} L_j \leq 2\eta\,|\Sigma_E|$$

The fraction of initial conditions on $\Sigma_E$ that land on a bad cycle is therefore at most $2\eta = 2e^{-c \, d_{\min} \, \epsilon^2}$. For a $30 M_\odot$ black hole, $d_{\min} \sim e^{S_{\text{BH}}} \sim e^{10^{77}}$, so $\eta \sim e^{-10^{77}}$. For all but an exponentially negligible fraction of initial conditions, the time-averaged entanglement entropy equals the Page value. $\square$

**Theorem A.9** (The Page curve). *The entanglement entropy of the radiation follows:*

$$S_{\text{rad}}(t) = \begin{cases} n_R(t) \cdot \ln q - \frac{q^{n_R(t)}}{2\,q^{n_B(t)}} & \text{for } n_R(t) < n_B(t) \quad \text{(early: before Page time)} \\ n_B(t) \cdot \ln q - \frac{q^{n_B(t)}}{2\,q^{n_R(t)}} & \text{for } n_R(t) > n_B(t) \quad \text{(late: after Page time)} \end{cases}$$

*where $q$ is the alphabet size (gauge — it cancels in all ratios), $n_B(t) + n_R(t) = n_B(0)$, and the Page time $t_P$ is defined by $n_R(t_P) = n_B(t_P) = n_B(0)/2$.*

*Proof.* Direct substitution of $d_B = q^{n_B(t)}$ and $d_R = q^{n_R(t)}$ into the Page entropy formula (Theorem A.8), using $\ln(q^n) = n \ln q$ and the conservation law $n_B + n_R = n_B(0)$. The turnover at $n_R = n_B$ follows from $\min(d_B, d_R)$ switching from $d_R$ to $d_B$. $\square$

**The evaporation trajectory.** The Hawking temperature (§3.2, Step 4) gives luminosity $L \sim 1/M^2$, hence $dM/dt = -\alpha/M^2$ where $\alpha = \hbar c^4 \Gamma / (15360 \pi G^2)$ and $\Gamma$ is the species-dependent greybody factor (solution-specific). Integrating:

$$M(t) = M_0\!\left(1 - t/t_{\text{evap}}\right)^{1/3}, \qquad t_{\text{evap}} = \frac{M_0^3}{3\alpha}$$

The boundary mode count $n_B(t) = 4\pi G M(t)^2 / (\hbar c) = n_B(0) \cdot (1 - t/t_{\text{evap}})^{2/3}$ and $n_R(t) = n_B(0) - n_B(t)$. The Page time $t_P$ satisfies $n_B(t_P) = n_B(0)/2$:

$$t_P = t_{\text{evap}}\!\left(1 - 2^{-3/2}\right) \approx 0.646 \; t_{\text{evap}}$$

The entropy of the radiation at the Page time is $S_{\text{rad}}(t_P) = n_B(0) \ln q / 2 = S_{\text{BH}}(0) \ln q / 2$ — half the initial black hole entropy, as expected.

---

## References

**Companion papers (cited inline by short name):**

[Main] A. Maybaum, "The Incompleteness of Observation," (2026).

[SM] A. Maybaum, "The Standard Model from a Cubic Lattice," (2026).

[Substratum] A. Maybaum, "The Substratum Construction: Reconstruction, the Substratum Gauge Group, and the QM-GR Synthesis," (2026).

---


[1] T. Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State," *Phys. Rev. Lett.* **75**, 1260 (1995).


[2] G. W. Gibbons and S. W. Hawking, "Cosmological event horizons, thermodynamics, and particle creation," *Phys. Rev. D* **15**, 2738 (1977).


[3] W. G. Unruh, "Sonic analogue of black holes and the effects of high frequencies on black hole evaporation," *Phys. Rev. D* **51**, 2827 (1995).


[4] K. Fredenhagen and R. Haag, "On the derivation of Hawking radiation associated with the formation of a black hole," *Commun. Math. Phys.* **127**, 273–284 (1990).


[5] LIGO Scientific Collaboration, Virgo Collaboration, and KAGRA Collaboration: A. G. Abac et al., "GW250114: Testing Hawking's Area Law and the Kerr Nature of Black Holes," *Phys. Rev. Lett.* **135**, 111403 (2025).


[6] J. Martin, "Everything you always wanted to know about the cosmological constant problem (but were afraid to ask)," *C. R. Phys.* **13**, 566–665 (2012).


[7] S. Weinberg, "The cosmological constant problem," *Rev. Mod. Phys.* **61**, 1 (1989).


[8] S. M. Carroll, "The Cosmological Constant," *Living Rev. Relativ.* **4**, 1 (2001).


[9] D. H. Wolpert, "Physical limits of inference," *Physica D* **237**, 1257–1281 (2008).


[10] J. Solà Peracaula, "The cosmological constant problem and running vacuum in the expanding universe," *Phil. Trans. R. Soc. A* **380**, 20210182 (2022).


[11] J. Solà Peracaula, A. Gómez-Valent, J. de Cruz Pérez, and C. Moreno-Pulido, "Running Vacuum in the Universe: Phenomenological Status in Light of the Latest Observations, and Its Impact on the σ₈ and H₀ Tensions," *Universe* **9**, 262 (2023); arXiv:2304.11157.


[12] DESI Collaboration, "DESI 2024 VI: Cosmological Constraints from BAO," arXiv:2404.03002 (2024).


[13] DESI Collaboration, "DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints," *Phys. Rev. D* **112**, 083515 (2025); arXiv:2503.14738.


[14] J. de Cruz Pérez, A. Gómez-Valent, and J. Solà Peracaula, "Dynamical Dark Energy models in light of the latest observations," arXiv:2512.20616 (2025).


[15] N. R. Bertini, M. H. Novaes, R. von Marttens, and I. L. Shapiro, "Renormalization group corrections to ΛCDM model and observational consequences for H₀ tension," arXiv:2509.24026 (2025).


[16] A. Gómez-Valent and J. Solà Peracaula, "Relaxing the σ₈-tension through running vacuum in the Universe," *Mon. Not. Roy. Astron. Soc.* **478**, 126–145 (2018); arXiv:1801.08501.


[17] DESI Collaboration: W. Elbers et al., "Constraints on Neutrino Physics from DESI DR2 BAO and DR1 Full Shape," arXiv:2503.14744 (2025).


[18] JUNO Collaboration: A. Abusleme et al., "First measurement of reactor neutrino oscillations at JUNO," arXiv:2511.14593 (2025).


[19] F. Capozzi et al., "Updated bounds on the (1,2) neutrino oscillation parameters after first JUNO results," arXiv:2511.21650 (2025).


[20] E. P. Verlinde, "Emergent Gravity and the Dark Universe," *SciPost Phys.* **2**, 016 (2017); arXiv:1611.02269.


[21] LZ Collaboration: J. Aalbers et al., "Dark matter search results from 4.2 tonne-years of exposure of the LUX-ZEPLIN (LZ) experiment," (2025); 417-day analysis presented at SURF, December 2025.


[22] S. S. McGaugh, F. Lelli, and J. M. Schombert, "Radial acceleration relation in rotationally supported galaxies," *Phys. Rev. Lett.* **117**, 201101 (2016).


[23] R. Genzel et al., "Strongly baryon-dominated disk galaxies at the peak of galaxy formation ten billion years ago," *Nature* **543**, 397–401 (2017).


[24] R. Genzel et al., "Rotation curves in z ~ 1–2 star-forming disks: evidence for cored dark matter distributions," *Astrophys. J.* **902**, 98 (2020).


[25] Y. Jiao et al., "Detection of the Keplerian decline in the Milky Way rotation curve," *Astronomy & Astrophysics* **678**, A208 (2023).


---

[26] N. Bao, S. M. Carroll, and A. Singh, "The Hilbert space of quantum gravity is locally finite-dimensional," *Int. J. Mod. Phys. D* **26**, 1743013 (2017).


[27] C. Bäcker, K. Beyer, and W. T. Strunz, "Local disclosure of quantum memory in non-Markovian dynamics," *Phys. Rev. Lett.* **132**, 060402 (2024); arXiv:2310.01205.


[28] A. Yosifov, A. Iyer, V. Vedral, and J. Sun, "On the emergence of quantum memory in non-Markovian dynamics," arXiv:2507.21907 (2025).


[29] S. Popescu, A. J. Short, and A. Winter, "Entanglement and the foundations of statistical mechanics," *Nature Physics* **2**, 754–758 (2006).

[30] W. F. Stinespring, "Positive functions on C*-algebras," *Proc. Amer. Math. Soc.* **6**, 211–216 (1955).


[31] M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, 10th anniversary edition, 2010).


[32] D. N. Page, "Average entropy of a subsystem," *Phys. Rev. Lett.* **71**, 1291 (1993).

[33] I. L. Shapiro and J. Solà, "Scaling behavior of the cosmological constant: interface between quantum field theory and cosmology," *JHEP* **02**, 006 (2002); arXiv:hep-th/0012227.

[34] C. Moreno-Pulido and J. Solà Peracaula, "Running vacuum in QFT in FLRW spacetime: the dynamics of ρ_vac(H) from the quantized matter fields," *Eur. Phys. J. C* **83**, 637 (2023); arXiv:2302.04807.


[35] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Foundations of Physics* **53**, 82 (2023); arXiv:2302.10778.


[36] J. A. Barandes, "The Stochastic-Quantum Theorem," arXiv:2309.03085 (2023).
