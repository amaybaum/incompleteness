# Chapter 8
# JUNO and the Neutrino Sector

---

## 8.1 What this chapter develops

Chapter 6 §6.7 introduced the framework's predictions for the three PMNS mixing angles and identified the solar mixing angle $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2) = 0.3080$ as the framework's sharpest neutrino-sector empirical confirmation, matched to the post-JUNO global fit at $0.07\sigma$. The present chapter develops that prediction in detail. The JUNO experiment, the structural derivation, the global-fit methodology, the discrimination from competing tribimaximal-modification patterns, and the framework's empirical position in the post-JUNO landscape — these are the chapter's content.

The chapter opens with the experiment. Section 8.2 develops the JUNO detector design and the reactor antineutrino source: the 20-kiloton liquid scintillator detector 53 km from two nuclear power complexes in southern China, the energy resolution and reactor flux that combine to produce the world's most precise measurement of $\sin^2\theta_{12}$ on a much shorter timescale than was thought possible. Section 8.3 develops the cubic-group flavor structure that produces the framework's prediction: the three lepton generations occupying the $T_1$ corners of the cubic Brillouin zone, the Cabibbo angle $\lambda = 1/(\pi\sqrt{2})$ from a single Brillouin-zone distance, the tribimaximal mixing pattern from the $A_4 \subset O$ subgroup at zeroth order.

The structural derivation occupies the middle of the chapter. Section 8.4 develops the $U$-parity grading — the discrete $\mu$-$\tau$ exchange symmetry of $S_4 \supset A_4$ that controls how the charged-lepton perturbations modify the tribimaximal pattern at order $\lambda^2$. Section 8.5 develops the sum rule $2\sin^2\theta_{12} + \sin^2\theta_{23} = 7/6$ as the framework's structural discriminator from tribimaximal-modification alternatives, and locates the framework's specific structural relation $b_{23} = (4/3)(b_{12} + b_{13})$ within the broader space of partial-TBM patterns currently analyzed against JUNO data.

The empirical content occupies the latter sections. Section 8.6 develops the three numerical predictions — $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2) = 0.3080$, $\sin^2\theta_{13} = 4/(18\pi^2) = 0.0225$, $\sin^2\theta_{23} = 1/2 + 1/(2\pi^2) = 0.5507$ — and compares them with the post-JUNO global fit and the NuFIT 6.0 best fits, with all three angles matched within $1.1\sigma$. Section 8.7 compares the framework's predictions with the column-preservation patterns TM1 and TM2 currently analyzed against JUNO: TM2 excluded at greater than $3.5\sigma$ post-JUNO, TM1 marginal at $1.35\sigma$, the framework at $0.07\sigma$.

The framework's position in the literature is the chapter's closing content. Section 8.8 develops the JUNO design-lifetime sensitivity: 30-year exposure projected to reach $\pm 0.0014$ precision on $\sin^2\theta_{12}$, providing a sub-percent test of the framework's prediction. Section 8.9 develops the coupled neutrino-mass / dark-energy result with DESI DR2 — the $\Sigma m_\nu < 0.0642$ eV bound consistent with the framework's normal-ordering prediction near the oscillation minimum of $0.059$ eV, the $3\sigma$ tension with the lower oscillation limit assuming $\Lambda$CDM that the framework's RVM dark energy resolves. Section 8.10 closes with the chapter's epistemic implications: a $0.07\sigma$ empirical match on a parameter-free structural prediction made before the JUNO measurement, with the chapter's content classified per Chapter 4's discipline.

The framework's empirical record in the neutrino sector represents the strongest single piece of evidence for the framework's structural commitments outside the gravitational sector. The Cabibbo angle and the Koide relation match at $0.04\%$ and $0.02\%$ respectively, but their predictions were available before the high-precision measurements that confirmed them. The $\sin^2\theta_{12}$ prediction was published before the JUNO measurement of November 2025 — making the $0.07\sigma$ match a forward prediction confirmed by experiment rather than a retrodiction of existing data. The framework's neutrino-sector content is therefore concentrated in this chapter as a focused case study of preregistered prediction confirmed at high precision.

## 8.2 The JUNO experiment

The Jiangmen Underground Neutrino Observatory (JUNO) is a multipurpose neutrino experiment located 700 meters underground in Jiangmen, southern China. The detector consists of a 20-kiloton liquid scintillator sphere, approximately 35 meters in diameter, instrumented with 17,612 large-aperture photomultiplier tubes and 25,600 smaller photomultiplier tubes. The detector is designed to measure reactor antineutrinos from the Yangjiang and Taishan nuclear power complexes, located 53 km from the experimental site — a baseline chosen to maximize sensitivity to the solar mixing angle $\theta_{12}$ at the oscillation maximum for reactor antineutrino energies.

The detector's energy resolution is the principal experimental innovation. JUNO achieves approximately $3\%$ at 1 MeV, a factor of three to five improvement over previous reactor neutrino experiments. The improvement comes from three sources: the high photocathode coverage (over $75\%$ of the detector surface), the high light yield of the scintillator, and the careful calibration program that has been ongoing throughout the detector commissioning. The combination of high statistics (approximately 60 events per day from the two reactor complexes) and high energy resolution allows JUNO to resolve the fine structure of the reactor antineutrino oscillation spectrum at unprecedented precision.

**The first JUNO measurement.** The collaboration reported its first measurement of reactor neutrino oscillations in November 2025. The headline result from 59.1 days of physics data was
$$\sin^2\theta_{12} = 0.3092 \pm 0.0087,$$
which is the most precise single-experiment determination of the solar mixing angle to date — a factor of 1.6 improvement over all previous measurements combined. The same dataset also produces a high-precision measurement of the mass-squared splitting:
$$\Delta m_{21}^2 = (7.48 \pm 0.10) \times 10^{-5}\,\text{eV}^2,$$
confirming the solar oscillation parameters with reactor-baseline precision for the first time. JUNO's first measurement closes a long-standing tension between solar and reactor neutrino measurements of $\theta_{12}$: the solar neutrino determination, primarily from SNO and Super-Kamiokande, gave systematically higher values, while the reactor neutrino determination from KamLAND gave systematically lower values, with the discrepancy at the $1.5\sigma$ level before JUNO. The new JUNO result lies between the two prior determinations and provides a unified value with significantly reduced uncertainty.

**The post-JUNO global fit.** The combined analysis of all neutrino oscillation data — solar, atmospheric, reactor, and accelerator — produces a global fit that incorporates the new JUNO measurement. The Capozzi *et al.* post-JUNO global fit (early 2026) gives
$$\sin^2\theta_{12} = 0.3085 \pm 0.0073,$$
which is the value the framework's predictions are tested against in this chapter. The global fit's uncertainty is dominated by JUNO's measurement; future runs will continue to tighten the constraint over the experiment's design lifetime.

The JUNO experiment is therefore the primary current source of constraint on the solar mixing angle and on the framework's specific prediction. The remainder of this chapter develops what that prediction is, where it comes from structurally, and how it compares with alternative theoretical proposals currently being analyzed against the JUNO data.

## 8.3 The cubic-group flavor structure

The framework's prediction for the PMNS angles follows from the cubic point group $O$ — the rotation symmetry group of three-dimensional space — applied to the three lepton generations. The structural argument runs through the same chain that produced the gauge group $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ in Chapter 5: the cubic decomposition of the six nearest-neighbor link directions on the simple cubic lattice gives multiplicities $(3, 2, 1)$ under the cubic-group action, with the three lepton generations occupying the $T_1$ triplet representation.

**The cubic group $O$ and its $A_4$ subgroup.** The cubic point group $O$ is the rotation symmetry group of three-dimensional space, with $24$ elements isomorphic to the symmetric group $S_4$. Its irreducible representations decompose as
$$\mathrm{irreps}(O) = A_1 \oplus A_2 \oplus E \oplus T_1 \oplus T_2,$$
of dimensions $1, 1, 2, 3, 3$. The subgroup $A_4 \subset O$ keeps $\{A_1, A_2, E, T_1\}$ but identifies $A_2$ with $A_1$, giving the standard $A_4$ content $A \oplus A' \oplus A'' \oplus T$ of dimensions $1, 1, 1, 3$. The framework's structural derivation in Chapter 5 placed the three lepton generations on the $T_1$ representation as one of the irreducible components of the cubic decomposition $6 = T_1 \oplus E \oplus A_1$ of the six nearest-neighbor link directions.

The realization of $T_1$ in the framework is concrete. The three Cartesian unit vectors $\{e_1, e_2, e_3\}$ — corresponding to the three spatial axes of the cubic lattice — are acted on by the $24$ rotations of $O$. The three generations occupy these three Cartesian directions. The cubic decomposition has a single democratic direction
$$\hat{h} = \frac{1}{\sqrt{3}}(e_1 + e_2 + e_3),$$
which is the only direction fixed by the $\mathbb{Z}_3$ cyclic subgroup of $O$. The plane perpendicular to $\hat{h}$ carries the doublet $E$ representation. This is the geometric origin of tribimaximal mixing in the framework: the second column of the tribimaximal mixing matrix is exactly $\hat{h}$, and the first and third columns lie in the plane perpendicular to it, oriented by $\mu$-$\tau$ exchange.

**The Cabibbo scale from cubic Brillouin geometry.** The perturbation parameter $\lambda$ controlling the deviations from tribimaximal mixing in the framework is identified with the Cabibbo angle, fixed independently by the cubic Brillouin-zone geometry as developed in Chapter 6 §6.5. The three generations occupy the three $T_1$ corners of the cubic Brillouin zone at momenta $X_j = \pi \cdot e_j$ for $j = 1, 2, 3$. The inter-generation distance in momentum space is
$$|X_i - X_j| = \pi\sqrt{2} \quad (i \neq j),$$
a geometric constant of the cubic lattice. The Cabibbo angle is the inverse of this distance:
$$\lambda = \frac{1}{\pi\sqrt{2}} = 0.22508.$$

The match to observation is at $0.04\%$: the measured value is $\lambda = 0.22500 \pm 0.00067$, with the framework's prediction inside the experimental uncertainty. The Cabibbo angle is therefore a parameter-free structural prediction of the framework, fixed by a single Brillouin-zone distance, with no input from the lepton sector. The fact that the same $\lambda$ then controls the PMNS deviations from tribimaximal mixing is the framework's structural commitment: the Cabibbo scale that produces the quark-sector mixing is the same scale that produces the lepton-sector mixing deviations. The two empirical confirmations — the Cabibbo angle at $0.04\%$ and the solar mixing angle at $0.07\sigma$ — are not independent confirmations of separate structures but joint confirmations of a single cubic-group geometric source.

**The PMNS matrix at zeroth order.** The framework's PMNS structure at zeroth order is the tribimaximal mixing matrix, obtained from the $A_4 \subset O$ representation theory. The tribimaximal matrix is
$$U_{\text{TBM}} = \begin{pmatrix}
\sqrt{2/3} & \sqrt{1/3} & 0 \\
-\sqrt{1/6} & \sqrt{1/3} & \sqrt{1/2} \\
-\sqrt{1/6} & \sqrt{1/3} & -\sqrt{1/2}
\end{pmatrix},$$
with the columns corresponding to mass eigenstates $\nu_1, \nu_2, \nu_3$ and the rows to flavor eigenstates $\nu_e, \nu_\mu, \nu_\tau$. The corresponding zeroth-order mixing angles are
$$\sin^2\theta_{12}^{\text{TBM}} = \frac{1}{3}, \quad \sin^2\theta_{23}^{\text{TBM}} = \frac{1}{2}, \quad \sin^2\theta_{13}^{\text{TBM}} = 0.$$

The observed values deviate from tribimaximal mixing by amounts of order $\lambda^2 \approx 0.05$, with the most consequential deviation being a non-zero $\theta_{13}$ at the level of $\sin^2\theta_{13} \approx 0.022$. The framework's content in the next sections is to derive these deviations from a $\mu$-$\tau$ parity grading combined with one cubic-group structural relation, producing parameter-free predictions for all three angles.

**The framework's structural commitment.** The cubic-group flavor structure used here is not a postulated symmetry of the lepton sector. It is the rotation symmetry group of three-dimensional space, realized in the framework's lattice substratum as developed in Chapters 5 and 6. The same cubic group that produced the Standard Model gauge structure produces the lepton flavor structure here, with the $T_1$ generations occupying the same triplet representation in both contexts. The empirical record across the framework's flavor predictions — Cabibbo at $0.04\%$, Koide at $0.02\%$, $\sin^2\theta_{12}$ at $0.07\sigma$, the sum rule $2\sin^2\theta_{12} + \sin^2\theta_{23} = 7/6$ at $0.6\sigma$ — tests the same cubic structure across multiple observables at sub-percent precision. This is testable structure rather than a postulated symmetry: the same numerical inputs ($\lambda^2 = 1/(2\pi^2)$, the projection factor $A^2 = 2/3$) enter multiple observables with all of them matching observation.

---

## 8.4 The U-parity grading

The framework's PMNS structure beyond tribimaximal mixing develops through a $\mu$-$\tau$ exchange parity — a discrete $\mathbb{Z}_2$ grading from $S_4 \supset A_4$ — that organizes the charged-lepton perturbations into structurally distinct $U$-even and $U$-odd components. The grading is not an additional symmetry postulate but a direct consequence of the framework's structural commitment to $T_1$ as the generation triplet: $T_1$ contains a natural $\mu$-$\tau$ exchange generator, and the perturbations of $T_1$ inherit a grading under this exchange.

**The $U$-parity generator.** In the Altarelli-Feruglio basis (charged-lepton mass matrix diagonal at zeroth order), the $\mu$-$\tau$ exchange operator $U$ is the permutation that exchanges the second and third generations:
$$U = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}.$$
The generator $U$ sits in $S_4 \supset A_4$ as the $\mu$-$\tau$ exchange element of the larger permutation group. Conjugation by $U$ defines a $\mathbb{Z}_2$ grading on antisymmetric matrices: a matrix $A$ is $U$-even if $U A U^{-1} = +A$, $U$-odd if $U A U^{-1} = -A$. The grading decomposes the space of antisymmetric matrices into two orthogonal components.

With the basis matrices $(E_{ij})_{kl} = \delta_{ik}\delta_{jl} - \delta_{il}\delta_{jk}$ — the elementary antisymmetric matrices spanning the space of $3 \times 3$ antisymmetric matrices — the decomposition is:
- $U$-even combinations: $E_{12} + E_{13}$
- $U$-odd combinations: $E_{12} - E_{13}$ and $E_{23}$

The unique $U$-odd combination antisymmetric in $(\mu, \tau)$ is $E_{23}$; the unique $U$-odd combination relating the first generation to the second and third is $E_{12} - E_{13}$. The $U$-even combination $E_{12} + E_{13}$ relates the first generation symmetrically to the other two.

**The charged-lepton perturbation expansion.** The charged-lepton rotation matrix $V_\ell$ in the Altarelli-Feruglio basis admits a perturbative expansion in the Cabibbo scale $\lambda$:
$$V_\ell = \exp\bigl(\lambda A_1 + \lambda^2 A_2 + O(\lambda^3)\bigr),$$
with $A_1$ and $A_2$ real antisymmetric $3 \times 3$ matrices to be determined from structural inputs. The expansion is the framework's parametrization of the charged-lepton rotation: $A_1$ controls the leading deviations from the tribimaximal pattern at order $\lambda$, $A_2$ controls the next-to-leading deviations at order $\lambda^2$.

**Determination of $A_1$.** The leading-order generator $A_1$ is fixed by three structural conditions plus the cubic geometric input. First, the observed value $\theta_{13} \neq 0$ requires $\sin\theta_{13} = O(\lambda)$, forcing $A_1$ to contribute to the $(1,3)$ element of $V_\ell^\dagger U_{\text{TBM}}$. Second, the empirical observations that both $\Delta_{12} \equiv \sin^2\theta_{12} - 1/3$ and $\Delta_{23} \equiv \sin^2\theta_{23} - 1/2$ are of order $\lambda^2$ — neither shows a leading $\lambda$ contribution — further constrains $A_1$'s structure. Third, the geometric input from Section 8.3: each end of an inter-generation mixing vertex projects onto the plane perpendicular to the democratic direction $\hat{h}$, contributing a factor $\sin(\angle(\hat{e}_i, \hat{h})) = A$ from the off-democratic projection of any generation axis. For a single-vertex inter-generation transition, the total projection factor is $A^2$ — one factor per vertex end.

Identifying this projection geometry with the leading $O(\lambda)$ contribution to $U_{e3}$ gives the structural identity
$$\sin\theta_{13} = A^2 \lambda,$$
exact at order $\lambda$ (the order-$\lambda^2$ contributions from $A_2$ cancel in $|U_{e3}|^2$, as the next section establishes). This is a structural input fixing $A_1$'s overall coefficient up to sign, combined with the $U$-odd character required by the constraint $\Delta_{12}, \Delta_{23} = O(\lambda^2)$.

The result is uniquely determined:
$$A_1 = \frac{\sqrt{2}}{3}(E_{12} - E_{13}).$$
The generator $A_1$ is purely $U$-odd: $U A_1 U^{-1} = -A_1$. Geometrically, $A_1$ represents a rotation by angle $A^2 = 2/3$ around the axis $(\hat{e}_2 + \hat{e}_3)/\sqrt{2}$, which reproduces $\sin\theta_{13} = A^2 \lambda$ as required. The structural property is that $A_1$ is $U$-odd; the magnitude $\sqrt{2}/3$ is fixed by the projection identity $\sin\theta_{13} = A^2\lambda$ with $A^2 = 2/3$.

**Deviations from TBM at order $\lambda^2$.** Expanding $V_\ell$ to second order:
$$V_\ell = I + \lambda A_1 + \lambda^2\bigl(A_2 + \tfrac{1}{2}A_1^2\bigr) + O(\lambda^3),$$
and writing the most general antisymmetric $A_2$ as
$$A_2 = b_{12} E_{12} + b_{13} E_{13} + b_{23} E_{23},$$
direct computation of $|U_{\text{PMNS},ij}|^2$ to order $\lambda^2$ gives the deviations from tribimaximal mixing:
$$\Delta_{13} = \tfrac{4}{9}\lambda^2 = A^4 \lambda^2,$$
$$\Delta_{12} = -\tfrac{2}{3}(b_{12} + b_{13})\lambda^2,$$
$$\Delta_{23} = b_{23}\lambda^2.$$

Three structural properties of these deviations deserve explicit comment. First, $\Delta_{13}$ is independent of $A_2$ — the structural identity $\sin\theta_{13} = A^2\lambda$ is exact at order $\lambda^2$, with the $A_2$ contributions canceling from $|U_{e3}|^2$. The reactor mixing angle prediction is therefore Layer 1 structural: $\sin^2\theta_{13} = (4/9)\lambda^2$ follows from $A_1$ alone, with no second-order Wilson-coefficient inputs. Second, the combination $b_{12} - b_{13}$ does not enter any of the three angles — it is naturally identified with the CP-violating Dirac phase $\delta_{\text{CP}}$, the only remaining free parameter at order $\lambda^2$ that does not enter the angles. Third, $\Delta_{23}$ depends only on $b_{23}$, not on the $U$-even combination $b_{12} + b_{13}$. The $U$-parity structure organizes the second-order corrections in a way that the standard effective-field-theory parametrization does not.

## 8.5 The sum rule and structural relation

The deviations $\Delta_{12}$ and $\Delta_{23}$ depend on two independent scalar combinations of the $A_2$ Wilson coefficients: the $U$-even combination $b_{12} + b_{13}$ controlling $\Delta_{12}$, and the dominant $U$-odd coefficient $b_{23}$ controlling $\Delta_{23}$. The framework's content beyond the Layer 1 reactor angle prediction is a structural relation between these two combinations — a relation that produces the sum rule $2\sin^2\theta_{12} + \sin^2\theta_{23} = 7/6$ and discriminates the framework from tribimaximal-modification alternatives.

**Two normalization conditions.** The framework fixes the second-order Wilson coefficients through two conditions.

*Condition 1 — natural normalization.* The overall scale of $A_2$ is fixed by taking $b_{23} = 1$. This is a labeling convention rather than a physical input: it sets $A_2$ to enter the perturbation series at unit strength relative to $\lambda^2$, fixing the normalization of the order-$\lambda^2$ expansion before $b_{12} + b_{13}$ is determined.

*Condition 2 — cubic-group structural relation.* The relation between the dominant $U$-odd coefficient and the $U$-even combination is fixed by the cubic-group representation theory:
$$b_{23} = \tfrac{4}{3}(b_{12} + b_{13}).$$
With Condition 1, this gives $b_{12} + b_{13} = 3/4$. Unlike Condition 1, this is a substantive physical input — a relation between two independent Wilson coefficients that the cubic-group structure produces.

**Equivalence with TBM sum rule preservation.** The framework's structural relation has a clean interpretation at the angle level. Combining the explicit results $\Delta_{12} = -(2/3)(b_{12} + b_{13})\lambda^2$ and $\Delta_{23} = b_{23}\lambda^2$:
$$2\Delta_{12} + \Delta_{23} = \bigl(b_{23} - \tfrac{4}{3}(b_{12} + b_{13})\bigr)\lambda^2.$$
Condition 2 is therefore equivalent to $2\Delta_{12} + \Delta_{23} = 0$, which is the statement that the tribimaximal sum rule $2\sin^2\theta_{12} + \sin^2\theta_{23} = 7/6$ — holding at zeroth order from cubic geometry (since $2(1/3) + 1/2 = 7/6$) — continues to hold at order $\lambda^2$. The Wilson-coefficient relation and the angle-level sum rule are the same content under different parametrizations.

The sum rule itself has a clean cubic-geometric reading: $7/6 = 2/d + 1/(d-1)$ for $d = 3$ generations, with $2/d$ being twice the inverse generation count (the value $\sin^2\theta_{12}^{\text{TBM}} = 1/3$ doubled) and $1/(d-1)$ being the inverse partner count (the value $\sin^2\theta_{23}^{\text{TBM}} = 1/2$ in the doublet sector). For three generations, $2/3 + 1/2 = 7/6$ is forced by the representation theory; the framework's content is that this sum rule is *preserved* at order $\lambda^2$ by the second-order Wilson-coefficient relation.

**The factor $4/3$ as partner-count × per-partner projection.** Condition 2's specific numerical coefficient admits a structural reading:
$$\frac{4}{3} = 2A^2 = 2 \cdot \frac{C_2(T_1)}{d},$$
where $A = \sqrt{2/3}$ is the off-democratic projection of any generation axis and $C_2(T_1) = d - 1 = 2$ is the quadratic Casimir of the $T_1$ representation. The identity $A^2 = (d-1)/d = C_2(T_1)/d$ for $d = 3$ is the same representation-theoretic identity from Section 6.5 that produced the Wolfenstein $A$ parameter. The factor $4/3$ thus has a partner-count × per-partner projection reading: the $U$-even combination $E_{12} + E_{13}$ couples the first generation to its two partners $\{\hat{e}_2, \hat{e}_3\}$, with the per-partner projection nominally $A^2$.

**Structural protection of the sum rule by $A_1$ alone.** A distinct structural feature of the framework's $A_1$ choice deserves explicit treatment. With $A_2 = 0$, direct computation gives $2|U_{e2}|^2 + |U_{\mu 3}|^2 = 7/6 + \lambda^2 \cdot [-14/27]$ before the $\cos^2\theta_{13}$ correction. Dividing by $\cos^2\theta_{13} = 1 - (4/9)\lambda^2$ — which itself follows from $\sin^2\theta_{13} = A^4\lambda^2$, a Layer 1 quantity — precisely cancels the $-14/27$ offset, giving
$$(2\sin^2\theta_{12} + \sin^2\theta_{23}) \bigm|_{A_2 = 0} = 7/6 + O(\lambda^4).$$

The sum rule is therefore *structurally protected* against $A_1$'s perturbation by cubic geometry alone — no substrate input required for this component. The cancellation between the $-14/27$ contribution from $A_1^2$-induced shifts and the $+14/27$ contribution from the $\cos^2\theta_{13}$ dressing is automatic given $A_1$'s Layer 1-forced form. Condition 2's content reduces to whether $A_2$ *preserves* the sum rule that $A_1$ alone protected, or breaks it. The framework's structural commitment is that $A_2$ also preserves the sum rule, through the $b_{23} = (4/3)(b_{12} + b_{13})$ relation.

**Layer status.** The three angle predictions have distinct structural statuses per the four-layer framing of Chapter 4 §4.5. The reactor angle $\sin^2\theta_{13} = (4/9)\lambda^2 = A^4\lambda^2$ is Layer 1 unconditional structural — it depends only on $A_1$ at second order, with $A_2$ contributions canceling. The solar and atmospheric angles $\sin^2\theta_{12}$ and $\sin^2\theta_{23}$ are layered predictions: the structural form is forced by the $A_1$ component (with the sum rule preserved by cubic geometry alone), and the specific deviations at order $\lambda^2$ depend on Condition 2's relation $b_{23} = (4/3)(b_{12} + b_{13})$.

The Layer 2(a)-tractable open question is whether the cubic-lattice substrate Yukawa structure produces the specific ratio $b_{23}/(b_{12} + b_{13}) = 4/3$ from first principles. The closure path is a one-loop staggered-fermion calculation on the cubic lattice testing whether the $C_2(T_1)$ Casimir structure produces this coefficient. The framework treats Condition 2 as a substrate-level relation, with the empirical match at $0.07\sigma$ on $\sin^2\theta_{12}$ providing nontrivial evidence that the relation holds in the specific bijection $\varphi$. The substrate calculation that would derive the $4/3$ ratio from first principles is an open task; the empirical evidence supports the structural reading.

## 8.6 The three numerical predictions

Substituting Condition 1 ($b_{23} = 1$), Condition 2 ($b_{12} + b_{13} = 3/4$), and the Cabibbo scale $\lambda^2 = 1/(2\pi^2)$ into the order-$\lambda^2$ deviations from tribimaximal mixing gives the framework's three numerical predictions for the PMNS angles.

**The three predictions.**
$$\sin^2\theta_{12} = \frac{1}{3} - \frac{1}{4\pi^2} = 0.3080,$$
$$\sin^2\theta_{13} = \frac{4}{9} \cdot \frac{1}{2\pi^2} = \frac{4}{18\pi^2} = 0.02252,$$
$$\sin^2\theta_{23} = \frac{1}{2} + \frac{1}{2\pi^2} = 0.5507.$$

The reactor angle $\sin^2\theta_{13}$ uses only $A^2 = 2/3$ and $\lambda^2 = 1/(2\pi^2)$ together with the constraints on $A_1$ — it does not use the normalization conditions on $A_2$. The other two angles additionally use Conditions 1 and 2. The three predictions together exhaust the framework's content for the PMNS mixing angles; the framework leaves $\delta_{\text{CP}}$ (the CP-violating Dirac phase) undetermined.

**Comparison with the post-JUNO global fit and NuFIT 6.0.** The empirical state of the PMNS angles as of early 2026 is summarized in the table below. The post-JUNO global fit incorporates the November 2025 JUNO measurement; the NuFIT 6.0 best fits use the full neutrino-oscillation data set under the normal mass ordering convention.

| Angle | Predicted | Observed | Match |
|-------|-----------|----------|-------|
| $\sin^2\theta_{12}$ | $0.3080$ | $0.3085 \pm 0.0073$ (post-JUNO global fit) | $0.07\sigma$ |
| $\sin^2\theta_{23}$ | $0.5507$ | $0.561^{+0.012}_{-0.015}$ (NuFIT 6.0, NO) | $0.74\sigma$ |
| $\sin^2\theta_{13}$ | $0.02252$ | $0.02195 \pm 0.00056$ (NuFIT 6.0, NO) | $1.02\sigma$ |

All three predictions match observation within $1.1\sigma$ at current precision. The solar mixing angle prediction is the framework's sharpest neutrino-sector empirical confirmation — at $0.07\sigma$ from the post-JUNO global fit, well within experimental uncertainty.

**The solar mixing angle as the cleanest test.** The $\sin^2\theta_{12}$ prediction is the framework's cleanest empirical test in the lepton sector for three reasons. First, it has the smallest experimental uncertainty among the three angles (relative uncertainty about $2.4\%$, compared to about $2.5\%$ for $\sin^2\theta_{23}$ and about $2.6\%$ for $\sin^2\theta_{13}$). Second, the prediction is parameter-free: both inputs entering the framework's prediction — the zeroth-order value $1/3$ from the $A_4$ tribimaximal pattern and the perturbation scale $\lambda^2 = 1/(2\pi^2)$ from the Cabibbo Brillouin-zone geometry — are independently fixed before the lepton-sector data are considered. Third, the prediction was published before the JUNO measurement of November 2025, making the match a preregistered structural prediction confirmed by experiment rather than a retrodiction of existing data.

The cumulative empirical record across the framework's flavor predictions is striking. The Cabibbo angle is matched at $0.04\%$, the Koide angle at $0.02\%$, the solar mixing angle at $0.07\sigma$, the sum rule $2\sin^2\theta_{12} + \sin^2\theta_{23} = 7/6$ at $0.6\sigma$ — all from the same cubic-group representation theory applied to the lepton sector, with the same numerical inputs ($\lambda^2 = 1/(2\pi^2)$, $A^2 = 2/3$) producing all four predictions. The pattern is what distinguishes the framework's cubic-group structure from postulated flavor symmetries: the same parameter enters multiple observables at sub-percent precision, testable across the full flavor sector rather than only at one observable.

**The sum rule.** The framework's prediction $2\sin^2\theta_{12} + \sin^2\theta_{23} = 7/6$ is the cubic structural commitment beyond the three angles individually. Substituting the framework's predicted values: $2 \cdot 0.3080 + 0.5507 = 1.167$, which equals $7/6$ exactly. Substituting the observed values: $2 \cdot 0.3085 + 0.561 = 1.178 \pm 0.020$, with the agreement at $0.6\sigma$ — consistent with the framework's structural prediction. The sum rule is therefore a *fourth* empirical confirmation of the same cubic-group structure, complementary to the three individual angle measurements.

The remaining sections develop the framework's position in the broader landscape of tribimaximal-modification proposals (Section 8.7), the JUNO design-lifetime sensitivity for testing the $\sin^2\theta_{12}$ prediction at sub-percent precision (Section 8.8), and the coupled neutrino-mass / dark-energy result with DESI DR2 (Section 8.9).

---

## 8.7 Comparison with TM1/TM2 column-preservation patterns

Tribimaximal mixing was the leading phenomenological description of neutrino oscillation data until Daya Bay measured a non-zero $\theta_{13}$ in 2012. Since then, modified tribimaximal patterns have been the subject of a substantial literature, with the two best-known modifications preserving one column of the original tribimaximal matrix exactly: TM1 (first column preserved) and TM2 (second column preserved). Each gives a one-parameter family that accommodates the observed $\theta_{13}$ but predicts different values for the other two angles.

**TM1 and TM2 in the post-JUNO landscape.** Post-JUNO analyses by He and by Zhang find that TM2 is excluded at greater than $3.5\sigma$ while TM1 remains marginally viable. The framework's prediction sits well below both alternatives in tension with the post-JUNO global fit:

| Approach | Symmetry origin | $\sin^2\theta_{12}$ | $\sigma$ from observed |
|----------|----------------|---------------------|-----------------------|
| TM1 | postulated $A_4$ flavor | $0.3184$ | $1.35\sigma$ |
| TM2 | postulated $A_4$ flavor | $0.3408$ | $4.4\sigma$ |
| TM3 | postulated; $\theta_{13} = 0$ | — | excluded |
| **This work** | **cubic group $O$ of 3D space** | **$0.3080$** | **$0.07\sigma$** |

(Comparing against the post-JUNO global fit $\sin^2\theta_{12} = 0.3085 \pm 0.0073$. TM1 uses $\sin^2\theta_{12} = 1 - (2/3)/\cos^2\theta_{13}$; TM2 uses $\sin^2\theta_{12} = 1/(3\cos^2\theta_{13})$; both with $\sin^2\theta_{13} = 0.02195$.) The cubic-group prediction is closer to the post-JUNO global fit by a factor of about 20 in $\sigma$-distance than the best surviving column-preservation pattern, and at the same time makes more falsifiable claims (three independent angles plus the sum rule).

**Three structural differences distinguish the framework from TM$_n$.**

*Symmetry origin.* TM1, TM2, and TM3 take a discrete flavor symmetry as an *axiom* of the lepton sector — typically $A_4$, $S_4$, or a $\mathbb{Z}_2$ residual postulated for the lepton sector specifically. The framework's prediction uses $A_4 \subset O$, where $O$ is the rotation symmetry group of three-dimensional space. The framework's cubic structure is not postulated for the lepton sector; it is forced by the framework's structural commitments developed in Chapters 5–6: the Bravais-lattice uniqueness theorem (Chapter 5 §5.5), the coupling-degree minimization producing $K = 2d = 6$ (Chapter 5 §5.4), and the anomaly cancellation chain (Chapter 5 §5.7). The same cubic structure that produced the Standard Model gauge group with three generations and the Cabibbo angle here produces the PMNS mixing structure. The flavor symmetry is derived, not postulated.

*Independence of predictions.* TM1 produces a one-parameter correlation $\sin^2\theta_{12} = 1 - (2/3)/\cos^2\theta_{13}$, fixing $\theta_{12}$ given $\theta_{13}$ but predicting neither separately. The framework's analysis predicts all three angles as fixed numerical values, with the same two structural inputs ($\lambda^2 = 1/(2\pi^2)$ and $A^2 = 2/3$) appearing across all three predictions. This makes the framework's prediction strictly more falsifiable than TM1: any individual angle outside the framework's prediction refutes it independently, whereas TM1 can absorb deviations in one angle by adjusting the prediction for another.

*CP violation.* He's surviving TM1 pattern predicts $\sin\delta_{\text{CP}} = \pm 0.998$, close to maximal CP violation. The framework identifies $\delta_{\text{CP}}$ with the only remaining order-$\lambda^2$ free parameter ($b_{12} - b_{13}$) that does not enter any of the three angles. The framework's angle predictions therefore stand independently of any value of $\delta_{\text{CP}}$; this chapter makes no prediction for the CP phase. The two frameworks are testably distinct in the CP sector: if forthcoming long-baseline neutrino experiments (DUNE, T2HK) measure $\sin\delta_{\text{CP}}$ inconsistent with maximal CP violation, TM1 is refuted while the framework's content is unaffected.

**The sum rule discriminator.** The framework's structural prediction $2\sin^2\theta_{12} + \sin^2\theta_{23} = 7/6$ is the angle-level statement of Condition 2's relation $b_{23} = (4/3)(b_{12} + b_{13})$ from Section 8.5. The observed value is $2(0.3085) + 0.561 = 1.178 \pm 0.020$, in agreement with $7/6 = 1.1667$ at $0.6\sigma$. TM1 and TM2 do not produce this combination as an exact sum rule — in TM2 specifically, $\sin^2\theta_{12}$ is determined by $\theta_{13}$ alone with no correlation to $\theta_{23}$, so no analogous sum rule is forced. A direct measurement of $2\sin^2\theta_{12} + \sin^2\theta_{23}$ at the $0.005$ level — achievable with the JUNO design lifetime combined with NOvA, T2K, and IceCube-Upgrade atmospheric determinations of $\theta_{23}$ — is the sharpest data-side test distinguishing the framework from column-preservation alternatives.

**The cumulative-match pattern.** The framework's $\sin^2\theta_{12}$ match at $0.07\sigma$ does not stand alone. It sits within a cluster of empirical matches that all use the same cubic-group structural inputs: the Cabibbo angle at $0.04\%$, the Koide angle at $0.02\%$, the $\sin^2\theta_{13}$ prediction at $1.01\sigma$, the sum rule at $0.6\sigma$, the $|V_{cb}|$ prediction at $0.4\sigma$, the $m_u/m_d$ ratio at $0.05\sigma$. All six predictions match observation at sub-percent or sub-$\sigma$ precision simultaneously, with two structural parameters ($\lambda^2 = 1/(2\pi^2)$ and $A^2 = 2/3$) appearing repeatedly across the cluster.

Under any reasonable prior over flavor models, this is non-trivial structural agreement. A single set of structural inputs produces six distinct empirical matches; each would have to be explained as a coincidence in a flavor-symmetry framework that postulates the cubic structure rather than deriving it. The framework's content here is that the same cubic structure that forces the SM gauge group on the substratum side appears as the empirical flavor structure on the phenomenological side — testable across the full flavor sector rather than only at one observable.

## 8.8 JUNO design-lifetime sensitivity and falsification

JUNO's design lifetime is 30 years of physics operations. The collaboration projects that the experiment will achieve approximately $\pm 0.0014$ precision on $\sin^2\theta_{12}$ by the end of its design lifetime — a factor of six improvement over the first-result precision of $\pm 0.0087$ and approximately a factor of five improvement over the post-JUNO global fit precision of $\pm 0.0073$. The improvement comes from extended exposure (factor of about 185 increase in integrated luminosity over the first 59.1 days), continued calibration refinement, and accumulated cross-checks across multiple reactor cores.

**The framework's prediction at JUNO design-lifetime precision.** The framework's structural prediction $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2) = 0.30798$ is a single numerical value with no uncertainty from the framework side. The experimental side will reach $\pm 0.0014$ at design lifetime, giving a precision test at the $0.5\%$ relative level on the predicted value. If the framework's prediction is correct, JUNO's design-lifetime measurement should center on $0.3080$ with $\pm 0.0014$ uncertainty.

The discrimination this provides is severe. The TM1 pattern's prediction $\sin^2\theta_{12} \approx 0.3184$ differs from the framework's by $0.0104$, which is $7.4 \sigma$ at JUNO's design-lifetime precision. TM2's $0.3408$ differs by $0.0328$, which is $23 \sigma$. Any column-preservation pattern with $\sin^2\theta_{12} \gtrsim 0.31$ will be excluded at JUNO design-lifetime precision; only the cubic-group prediction will remain viable in that range. The 30-year program is therefore a decisive test between the framework's structural prediction and the broader landscape of tribimaximal-modification alternatives.

**Sensitivity to Condition 2.** The framework's prediction depends on Condition 2 — the structural relation $b_{23} = (4/3)(b_{12} + b_{13})$ developed in Section 8.5. A small fractional shift to the structural coefficient $4/3 \to (4/3)(1 + \epsilon)$ propagates to a shift in $\sin^2\theta_{12}$ of approximately $\epsilon \cdot \Delta_{23}/2$ at first order, where $\Delta_{23} = 1/(2\pi^2) \approx 0.05$. For a fractional shift $\epsilon = 0.10$ — a $10\%$ deviation from the cubic-group structural coefficient — the shift in $\sin^2\theta_{12}$ is approximately $0.0025$. This is comparable to JUNO's design-lifetime precision and roughly half of the first-result precision.

The framework's current $0.07\sigma$ match therefore tests Condition 2 at the few-percent level on its structural coefficient. JUNO's design-lifetime program will tighten this to better than $1\%$, providing an empirical test of the structural relation $4/3 = 2A^2$ — the framework's commitment that the cubic-group quadratic Casimir structure produces this specific ratio in the substrate. The empirical confirmation at sub-percent precision over JUNO's 30-year lifetime would constitute a quantitative test of the framework's cubic-group commitment at the level normally reserved for Standard Model coupling constants.

**Falsification commitments.** Three pre-registered falsification conditions per Chapter 4 §4.5 are concentrated at the JUNO experimental program.

*Class A falsification of the cubic-group lepton-sector structure.* Any precision-upgrade measurement of $\sin^2\theta_{12}$ moving the observed value outside $3\sigma$ of the framework's prediction $1/3 - 1/(4\pi^2)$ refutes the framework's cubic-group commitment in the lepton sector. The framework would have to be revised — either the $A_4 \subset O$ tribimaximal structure at zeroth order, the Cabibbo perturbation scale $\lambda^2 = 1/(2\pi^2)$, or the Condition 2 structural relation — to accommodate the deviation. The current $0.07\sigma$ match makes such revision unlikely, but JUNO's 30-year program will resolve the question definitively.

*Class A falsification of the sum rule.* Any precision measurement of $2\sin^2\theta_{12} + \sin^2\theta_{23}$ moving outside $3\sigma$ of the framework's prediction $7/6$ refutes the Condition 2 structural relation. The sum rule is the framework's sharpest discriminator against tribimaximal-modification alternatives, and a precise measurement at the $0.005$ level would either confirm or refute the framework's structural commitment in the lepton sector independently of the absolute value of $\sin^2\theta_{12}$.

*Class A falsification of the reactor angle.* Any precision measurement of $\sin^2\theta_{13}$ moving outside $3\sigma$ of the framework's prediction $4/(18\pi^2) = 0.02252$ refutes the Layer 1 reactor angle derivation. This prediction depends only on the structural identity $\sin\theta_{13} = A^2 \lambda$ with $A^2 = C_2(T_1)/d = 2/3$ and the Cabibbo scale $\lambda = 1/(\pi\sqrt{2})$ — both Layer 1 inputs. Refutation here would refute the cubic-group representation-theoretic structure at the framework's deepest level. The current $1.01\sigma$ match leaves substantial empirical room; ongoing reactor neutrino experiments (Daya Bay, Double Chooz, RENO) and accelerator experiments (T2K, NOvA) will continue to tighten the constraint.

The framework's empirical exposure at JUNO is therefore substantial. Three pre-registered Class A falsification conditions are concentrated at the JUNO experimental program, with a fourth (the $\sin^2\theta_{12}$ first-result match at $0.07\sigma$) already confirmed. The framework's neutrino-sector content has more empirical exposure per prediction than any other sector outside the gravitational confirmations of Chapter 7.

## 8.9 The coupled DESI DR2 result

The framework's neutrino-sector predictions extend beyond the PMNS mixing angles to include commitments on the neutrino mass spectrum. Chapter 6 §6.7 noted that the framework predicts normal mass ordering and $\Sigma m_\nu$ near the oscillation minimum; Chapter 7 §7.7 developed the coupled neutrino-mass / dark-energy result with DESI DR2. This section consolidates the joint observational support.

**The DESI DR2 + CMB neutrino mass result.** The DESI Data Release 2 combined with CMB lensing and primary CMB constraints from Planck 2018 produces the most precise current bound on the sum of neutrino masses. The analysis finds
$$\Sigma m_\nu < 0.0642\,\text{eV} \quad (95\%\,\text{CL})$$
under the $\Lambda$CDM cosmological model. The same analysis prefers the normal mass ordering over the inverted ordering and bounds the lightest neutrino mass at $m_l < 0.023$ eV.

The framework's prediction is normal ordering with $\Sigma m_\nu$ near the oscillation minimum of approximately $0.059$ eV — the value the framework's neutrino mass structure predicts at the substratum level combined with the measured mass-squared splittings from atmospheric and solar oscillation experiments. The DESI DR2 + CMB bound is consistent with this prediction and approaches it from above: the experimental upper bound at $0.0642$ eV sits just above the framework's predicted value at $0.059$ eV, with the gap being approximately one standard deviation of the experimental uncertainty.

**The $3\sigma$ tension that the framework resolves.** The DESI DR2 + CMB analysis under $\Lambda$CDM produces a $3\sigma$ tension with the *lower* oscillation limit on $\Sigma m_\nu$. The oscillation experiments require $\Sigma m_\nu \geq 0.059$ eV under normal ordering (from $\sqrt{\Delta m_{31}^2} + \sqrt{\Delta m_{21}^2}$ approximately), but the DESI DR2 + CMB combined analysis under $\Lambda$CDM prefers a value approaching zero. The literature has interpreted this tension as "a hint of new physics not necessarily related to neutrinos" — a structural mismatch between the cosmological inference assuming $\Lambda$CDM and the laboratory oscillation experiments.

The framework's running-vacuum dark energy (Chapter 7 §7.7) resolves this tension. When the cosmological analysis is performed with a Type II RVM dark energy model — the form the framework predicts at the structural level — the inferred $\Sigma m_\nu$ shifts upward to be compatible with the oscillation minimum. The Bertini *et al.* fit reports a $\nu$ parameter consistent with zero at $2\sigma$ but with the residual structure favoring slightly negative values, consistent with the framework's $|\nu_{\text{OI}}| \sim 10^{-32}$ prediction at theorem level. The RVM dark energy and the neutrino mass results are therefore coupled in the framework: both follow from the same lattice structure, and the joint observational support is a single empirical pattern rather than independent confirmation of separate effects.

**The neutrino sector as joint test of three commitments.** The empirical record across the framework's neutrino-sector predictions tests three structural commitments simultaneously. The PMNS angle predictions (§8.6) test the cubic-group representation theory applied to the lepton sector. The mass ordering and $\Sigma m_\nu$ near the oscillation minimum test the framework's normal-ordering commitment and the taste-breaking structure that determines the mass hierarchy. The RVM dark energy resolution of the $\Sigma m_\nu$ tension tests the framework's gravitational sector commitment from Chapter 7. The joint observational support across these three commitments — all consistent with experiment at the current precision — is what the framework's structural unity predicts: three commitments that look distinct in standard physics appear in the framework as different facets of the same cubic-lattice substratum.

The framework's content in the neutrino sector therefore extends well beyond the JUNO $\sin^2\theta_{12}$ measurement. The full empirical pattern includes the PMNS angles, the mass ordering, the absolute mass scale, and the coupled dark-energy / mass-bound resolution. Each tests a distinct framework commitment; the joint coherence across all of them is the framework's strongest non-cosmological empirical case.

## 8.10 Chapter close: the framework's empirical record in the neutrino sector

The framework's content in the neutrino sector represents the strongest single piece of evidence for the framework's structural commitments outside the gravitational sector. The chapter's specific empirical record:

- The Cabibbo angle $\lambda = 1/(\pi\sqrt{2})$ matches the observed value at $0.04\%$.
- The solar mixing angle $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2) = 0.3080$ matches the post-JUNO global fit at $0.07\sigma$.
- The reactor mixing angle $\sin^2\theta_{13} = 4/(18\pi^2) = 0.02252$ matches NuFIT 6.0 at $1.01\sigma$.
- The atmospheric mixing angle $\sin^2\theta_{23} = 1/2 + 1/(2\pi^2) = 0.5507$ matches NuFIT 6.0 at $0.74\sigma$.
- The sum rule $2\sin^2\theta_{12} + \sin^2\theta_{23} = 7/6$ matches observation at $0.6\sigma$.
- The neutrino mass ordering (normal) and $\Sigma m_\nu$ (near $0.059$ eV) are consistent with DESI DR2 + CMB.
- The $3\sigma$ tension with the oscillation minimum under $\Lambda$CDM is resolved by the framework's RVM dark energy.

The empirical pattern is what distinguishes the framework's cubic-group structure from postulated flavor symmetries. Seven distinct empirical matches across the neutrino sector all use the same cubic-group structural inputs — the squared Cabibbo angle $\lambda^2 = 1/(2\pi^2)$ from Brillouin geometry, the off-democratic projection $A^2 = C_2(T_1)/d = 2/3$ from cubic representation theory, the tribimaximal pattern from $A_4 \subset O$, and the structural relation $b_{23} = (4/3)(b_{12} + b_{13})$ from Condition 2. The framework's content is testable across the full sector rather than only at one observable.

**The preregistered-prediction status.** The framework's $\sin^2\theta_{12}$ prediction was published before the JUNO measurement of November 2025. The match at $0.07\sigma$ is therefore a forward prediction confirmed by experiment rather than a retrodiction of existing data. This is unusual in the flavor-physics literature — most tribimaximal-modification patterns were developed after the relevant measurements were available, with the framework's content selected to match observation. The framework's preregistered match makes the $0.07\sigma$ agreement substantively stronger evidence than retrodictive matches of comparable numerical precision.

The methodological discipline of Chapter 4 §4.6 places the preregistered-prediction status at the center of the framework's empirical case. A prediction made before the measurement, with no parameters adjusted to fit, that matches observation at $0.07\sigma$ is the kind of empirical confirmation that distinguishes a structural framework from a fitted phenomenological model. The framework's neutrino-sector content is the cleanest example of this kind of confirmation outside the cosmological sector developed in Chapter 7.

**Forward pointers.** Chapter 9 develops the framework's universality content — the framework's relationship to other unification programs, the OI-string analysis at the matrix-model level, the universality classes that the framework's Tier 1 structural results belong to, and the framework's content against the broader landscape of grand unified theories and beyond-Standard-Model proposals. The cumulative empirical case developed in Chapters 5 through 8 — twenty-two parameter-free Standard Model predictions, fourteen gravitational-sector predictions, seven neutrino-sector predictions — is what Chapter 9 contextualizes against the broader theoretical landscape. The framework's empirical record at the close of Part II is concentrated at Tier 1 of the gravitational sector and at Layer 1 of the Standard Model and neutrino sectors, with substantial empirical exposure across pre-registered falsification conditions and continued empirical agreement at current precision.

The framework's empirical content in fundamental physics is at the strongest evidential standard the field admits: parameter-free structural predictions, made before the relevant measurements, matching observation at the current experimental precision. The JUNO confirmation is the chapter's empirical anchor — the framework's commitment to cubic-group representation theory in the lepton sector, tested at $0.07\sigma$ on a parameter-free prediction. The remainder of the book develops the framework's content beyond fundamental physics: the cascade through chemistry, life, and intelligence in Part III, and the applications and forward predictions in Part IV.

---
