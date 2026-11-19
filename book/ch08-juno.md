# Chapter 8
# JUNO and the Neutrino Sector

***

## 8.1 What this chapter develops

Chapter 6 §6.7 gave the leading solar mixing value $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2) \approx 0.308003$. It is $0.14\sigma$ from direct JUNO and $0.07\sigma$ from the global fit that includes JUNO. This chapter develops the flavor calculation, its assumptions, and the experiment's comparison with it and with other tribimaximal mixing patterns.

The chapter opens with the experiment. Section 8.2 develops the JUNO detector design and the reactor antineutrino source: the 20-kiloton liquid scintillator detector 53 km from two nuclear power complexes in southern China, the energy resolution and reactor flux that combine to produce the world's most precise measurement of $\sin^2\theta_{12}$ on a much shorter timescale than was thought possible. Section 8.3 develops the cubic-group flavor structure that produces the framework's prediction: the three lepton generations occupying the $T_1$ corners of the cubic Brillouin zone, the Cabibbo angle $\lambda = 1/(\pi\sqrt{2})$ from a single Brillouin-zone distance, the tribimaximal mixing pattern from the $A_4 \subset O$ subgroup at zeroth order.

Sections 8.4 and 8.5 develop the $\mu$-$\tau$ exchange grading and the Wilson-coefficient relation $b_{23} = (4/3)(b_{12}+b_{13})$. That relation preserves the tribimaximal sum $2\sin^2\theta_{12} + \sin^2\theta_{23} = 7/6$ through order $\lambda^2$.

Section 8.6 compares the leading values of the three squared mixing angles with JUNO, the post-JUNO global fit, and the cited NuFIT 6.0 fits. Section 8.7 compares the flavor calculation with the TM1 and TM2 patterns. Section 8.8 describes what future precision can test when higher orders are open. Section 8.9 places the separate DESI DR2 neutrino mass bounds in their cosmological models.

## 8.2 The JUNO experiment

The Jiangmen Underground Neutrino Observatory (JUNO) is a multipurpose neutrino experiment located 700 meters underground in Jiangmen, southern China. The detector consists of a 20-kiloton liquid scintillator sphere, approximately 35 meters in diameter, instrumented with 17,612 large-aperture photomultiplier tubes and 25,600 smaller photomultiplier tubes. The detector is designed to measure reactor antineutrinos from the Yangjiang and Taishan nuclear power complexes, located 53 km from the experimental site — a baseline chosen to maximize sensitivity to the solar mixing angle $\theta_{12}$ at the oscillation maximum for reactor antineutrino energies.

The detector's energy resolution is the principal experimental innovation. JUNO achieves approximately $3\%$ at 1 MeV, a factor of three to five improvement over previous reactor neutrino experiments. The improvement comes from three sources: the high photocathode coverage (over $75\%$ of the detector surface), the high light yield of the scintillator, and the careful calibration program that has been ongoing throughout the detector commissioning. The combination of high statistics (approximately 60 events per day from the two reactor complexes) and high energy resolution allows JUNO to resolve the fine structure of the reactor antineutrino oscillation spectrum at unprecedented precision.

**The first JUNO measurement.** The collaboration reported its first measurement of reactor neutrino oscillations in November 2025. The headline result from 59.1 days of physics data was
$$\sin^2\theta_{12} = 0.3092 \pm 0.0087,$$
which is the most precise single-experiment determination of the solar mixing angle to date — a factor of 1.6 improvement over all previous measurements combined. The same dataset also produces a high-precision measurement of the mass-squared splitting:
$$\Delta m_{21}^2 = (7.50 \pm 0.12) \times 10^{-5}\,\text{eV}^2$$
for normal ordering. [JUNO Collaboration](https://arxiv.org/abs/2511.14593)

**The post-JUNO global fit.** Capozzi *et al.* include these JUNO measurements and updated SNO+ data. Their global fit gives
$$\sin^2\theta_{12} = 0.3085 \pm 0.0073,\qquad \Delta m_{21}^2 = (7.48 \pm 0.10) \times 10^{-5}\,\text{eV}^2.$$
The direct and global solar residuals in §8.6 use overlapping data. [Capozzi et al.](https://arxiv.org/abs/2511.21650)

## 8.3 The cubic-group flavor structure

The flavor calculation uses the rotation group $O$ of the simple cubic lattice. Its six nearest-neighbor signed link directions decompose into blocks of dimensions $(3,2,1)$. Chapter 5 relates this decomposition to the gauge group through the stabilizer of a generic equivariant condensate on the single-copy H-link and H-cust branch, with the specified charged action. Within that nearest-neighbor comparison, simple cubic alone supplies the required block pattern. The flavor construction uses $T_1$ for the lepton generations under the carrier and spin conditions of SM §4.7.

**The cubic group $O$ and its $A_4$ subgroup.** The cubic point group $O$ is the rotation symmetry group of three-dimensional space, with $24$ elements isomorphic to the symmetric group $S_4$. Its irreducible representations decompose as
$$\mathrm{irreps}(O) = A_1 \oplus A_2 \oplus E \oplus T_1 \oplus T_2,$$
of dimensions $1, 1, 2, 3, 3$. The subgroup $A_4 \subset O$ keeps $\{A_1, A_2, E, T_1\}$ but identifies $A_2$ with $A_1$, giving the standard $A_4$ content $A \oplus A' \oplus A'' \oplus T$ of dimensions $1, 1, 1, 3$. The framework's structural derivation in Chapter 5 placed the three lepton generations on the $T_1$ representation as one of the irreducible components of the cubic decomposition $6 = T_1 \oplus E \oplus A_1$ of the six nearest-neighbor link directions.

The realization of $T_1$ in the framework is concrete. The three Cartesian unit vectors $\{e_1, e_2, e_3\}$ — corresponding to the three spatial axes of the cubic lattice — are acted on by the $24$ rotations of $O$. The three candidate sectors — the generations, under H-spin' — occupy these three Cartesian directions. The cubic decomposition has a single democratic direction
$$\hat{h} = \frac{1}{\sqrt{3}}(e_1 + e_2 + e_3),$$
which is the only direction fixed by the $\mathbb{Z}_3$ cyclic subgroup of $O$. Its perpendicular plane is the real two-dimensional complement for that cyclic subgroup inside $T_1$. The second column of the tribimaximal mixing matrix is $\hat{h}$. The first and third columns lie in the perpendicular plane, oriented by $\mu$-$\tau$ exchange.

**The Cabibbo scale from cubic Brillouin geometry.** The perturbation parameter $\lambda$ controlling the deviations from tribimaximal mixing in the framework is identified with the Cabibbo angle, fixed independently by the cubic Brillouin-zone geometry as developed in Chapter 6 §6.5. The three generations occupy the three $T_1$ corners of the cubic Brillouin zone at momenta $X_j = \pi \cdot e_j$ for $j = 1, 2, 3$. The inter-generation distance in momentum space is
$$|X_i - X_j| = \pi\sqrt{2} \quad (i \neq j),$$
a geometric constant of the cubic lattice. The Cabibbo angle is the inverse of this distance:
$$\lambda = \frac{1}{\pi\sqrt{2}} = 0.22508.$$

The measured Cabibbo value is $\lambda = 0.22500 \pm 0.00067$, a $0.04\%$ difference. The Brillouin-zone geometry fixes the distance and the chirality argument gives the inverse-momentum power. The algebraic unity of the physically projected taste-changing matrix element and the open emergent dressing of its identification with the Cabibbo angle have the scope of SM §7.1. The lepton calculation uses the same $\lambda$ for the deviations from tribimaximal mixing.

**The PMNS matrix at zeroth order.** The framework's PMNS structure at zeroth order is the tribimaximal mixing matrix, obtained from the $A_4 \subset O$ representation theory. The tribimaximal matrix is
$$U_{\text{TBM}} = \begin{pmatrix}
\sqrt{2/3} & \sqrt{1/3} & 0 \\
-\sqrt{1/6} & \sqrt{1/3} & \sqrt{1/2} \\
-\sqrt{1/6} & \sqrt{1/3} & -\sqrt{1/2}
\end{pmatrix},$$
with the columns corresponding to mass eigenstates $\nu_1, \nu_2, \nu_3$ and the rows to flavor eigenstates $\nu_e, \nu_\mu, \nu_\tau$. The corresponding zeroth-order mixing angles are
$$\sin^2\theta_{12}^{\text{TBM}} = \frac{1}{3}, \quad \sin^2\theta_{23}^{\text{TBM}} = \frac{1}{2}, \quad \sin^2\theta_{13}^{\text{TBM}} = 0.$$

The observed squared angles differ from the tribimaximal values by amounts of order $\lambda^2 \approx 0.05$, including a nonzero $\sin^2\theta_{13} \approx 0.022$. The next sections calculate the leading shifts from the $\mu$-$\tau$ exchange grading, a projection input, and two Wilson-coefficient inputs.

***

## 8.4 The U-parity grading

The $\mu$-$\tau$ exchange gives a $\mathbb{Z}_2$ grading of the charged-lepton perturbations into $U$-even and $U$-odd components.

**The $U$-parity generator.** In the Altarelli-Feruglio basis (charged-lepton mass matrix diagonal at zeroth order), the $\mu$-$\tau$ exchange operator $U$ is the permutation that exchanges the second and third generations:
$$U = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}.$$
The displayed swap has determinant $-1$. Its negative $-U$ is a proper cube rotation with the same conjugation action. This action gives a $\mathbb{Z}_2$ grading on antisymmetric matrices: $A$ is $U$-even when $UAU^{-1}=+A$ and $U$-odd when $UAU^{-1}=-A$.

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
at leading order in $\lambda$. This input fixes $A_1$'s magnitude, while the orders of $\Delta_{12}$ and $\Delta_{23}$ fix its $U$-odd form.

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

The leading squared reactor angle depends only on $A_1$. The real combination $b_{12}-b_{13}$ can contribute to the unsquared reactor amplitude $U_{e3}$ at order $\lambda^2$. Its interference with the leading amplitude can enter $|U_{e3}|^2$ at order $\lambda^3$. The combination drops out of all three squared angles through order $\lambda^2$. At this order the mixing matrix is real and the Dirac Jarlskog invariant vanishes. A physical complex CP phase remains unsourced. The atmospheric shift $\Delta_{23}$ depends on $b_{23}$ alone at this order.

## 8.5 The sum rule and structural relation

The second-order shifts involve two independent combinations of the $A_2$ coefficients. The $U$-even combination $b_{12}+b_{13}$ controls $\Delta_{12}$, and the $U$-odd coefficient $b_{23}$ controls $\Delta_{23}$.

**Condition 1 (normalization input).** Setting $b_{23}=1$ fixes the absolute second-order atmospheric shift with $\lambda$ fixed independently.

**Condition 2 (coefficient relation).** The proposed relation is
$$b_{23} = \tfrac{4}{3}(b_{12} + b_{13}).$$
With Condition 1 it gives $b_{12}+b_{13}=3/4$ and fixes the solar shift as well. Deriving the relation from the underlying dynamics remains open.

**The leading-order sum rule.** Adding the two shifts gives
$$2\Delta_{12} + \Delta_{23} = \bigl(b_{23} - \tfrac{4}{3}(b_{12}+b_{13})\bigr)\lambda^2 + O(\lambda^3).$$
The second-order term vanishes precisely when Condition 2 holds. Thus the sum keeps its tribimaximal value $7/6=2/3+1/2$ through order $\lambda^2$. The expansion allows higher-order terms.

The sum rule itself has a clean cubic-geometric reading: $7/6 = 2/d + 1/(d-1)$ for $d = 3$ generations, with $2/d$ being twice the inverse generation count (the value $\sin^2\theta_{12}^{\text{TBM}} = 1/3$ doubled) and $1/(d-1)$ being the inverse partner count (the value $\sin^2\theta_{23}^{\text{TBM}} = 1/2$ in the doublet sector). For three generations, $2/3 + 1/2 = 7/6$ is forced by the representation theory; the framework's content is that this sum rule is *preserved* at order $\lambda^2$ by the second-order Wilson-coefficient relation.

**The factor $4/3$ as cubic-group identity.** Condition 2's specific numerical coefficient is a genuine cubic-group identity:
$$\frac{4}{3} = 2A^2 = 2 \cdot \frac{C_2(T_1)}{d} = \frac{C_2(T_1)^2}{d},$$
where $A = \sqrt{2/3}$ is the off-democratic projection of any generation axis and $C_2(T_1) = d - 1 = 2$ is the quadratic Casimir of the $T_1$ representation. The identity $A^2 = (d-1)/d = C_2(T_1)/d$ for $d = 3$ is the same representation-theoretic identity from Section 6.5 that produced the Wolfenstein $A$ parameter. The factor $4/3$ thus has an interpretive reading as partner-count × per-partner projection: the $U$-even combination $E_{12} + E_{13}$ couples the first generation to its two partners $\{\hat{e}_2, \hat{e}_3\}$, with the per-partner projection nominally $A^2$. The interpretation is internally consistent but non-directional — the same arithmetic produces the inverse ratio $3/4$ under alternative partner-count assignments. The directional assertion that the $U$-odd coefficient $b_{23}$ is *larger* than the $U$-even coefficient $b_{12}+b_{13}$ by this specific factor is what carries the framework's substantive content beyond the cubic-group identity itself.

**Structural protection of the sum rule by $A_1$ alone.** For $V_\ell=\exp(\lambda A_1)$, direct computation gives $2|U_{e2}|^2+|U_{\mu3}|^2=7/6-(14/27)\lambda^2+O(\lambda^4)$. Dividing by $\cos^2\theta_{13}=1-(4/9)\lambda^2+O(\lambda^4)$ cancels the second-order offset:
$$(2\sin^2\theta_{12}+\sin^2\theta_{23})\bigm|_{A_1\text{ only}}=7/6+O(\lambda^4).$$

Condition 2 makes the sum survive the addition of $A_2$ at order $\lambda^2$.

**Layer status.** The leading reactor angle depends on $A_1$ and inherits the open emergent dressing of the Cabibbo identification. The leading solar and atmospheric values additionally use the normalization $b_{23}=1$ and the Layer 2(b) relation of Condition 2.

**Condition 2 as a Layer 2(b) bijection-specific commitment.** The framework's $b_{23} = (4/3)(b_{12} + b_{13})$ relation has a multi-layer structural status that the four-layer framing of Chapter 4 §4.5 distinguishes precisely:

(i) Under the U-parity grading developed in §8.4, the antisymmetric tensor product $T_1 \wedge T_1$ decomposes into a U-even subspace (spanned by $E_{12} + E_{13}$) and a U-odd subspace (spanned by $E_{12} - E_{13}$ and $E_{23}$). The subspace decomposition is forced by group theory — this is Layer 1 structural.

(ii) The cubic-geometric off-democratic projection $A^2 = 1 - 1/d = 2/3$ for $d = 3$ is forced by inner-product structure on $T_1$ with $\hat{h} = (1, 1, 1)/\sqrt{3}$ as the democratic axis. This is the same $A^2$ that produces the Wolfenstein parameter $A = \sqrt{2/3}$ in the quark sector (Chapter 6 §6.5) — Layer 1 structural.

(iii) The number $4/3=2A^2$ admits a geometric reading. Identifying it with the coefficient ratio requires an underlying amplitude calculation. The specified second-order lattice route is excluded (SM §7.3). The recorded $O(\lambda^3)$ interference route remains open.

(iv) The directional assertion that the $U$-odd amplitude exceeds the $U$-even amplitude by the specific factor of $4/3$, with the labeling fixed by the observed mass hierarchy ($m_e \ll m_\mu \ll m_\tau$ pinning generation 1 = electron), is *Layer 2(b) bijection-specific* content. It depends on the specific bijection $\varphi$ within the equivalence class — the same kind of content as the fermion mass hierarchy itself (Chapter 19 §19.3.1) and CKM/PMNS CP phases.

The solar residual constrains the leading pattern under the stated inputs. The open task is to obtain the required second-order alignment for a candidate bijection. The proposed staggered-Yukawa calculation concerns emergent post-trace-out operators. The specified two-hop route to the alignment is excluded (SM §7.3).

## 8.6 The three numerical predictions

Substituting $\lambda^2=1/(2\pi^2)$ and the coefficient inputs of §8.5 gives the leading values through order $\lambda^2$:
$$\sin^2\theta_{12} = \frac{1}{3} - \frac{1}{4\pi^2} \approx 0.308003,$$
$$\sin^2\theta_{13} = \frac{4}{18\pi^2} \approx 0.02252,$$
$$\sin^2\theta_{23} = \frac{1}{2} + \frac{1}{2\pi^2} \approx 0.5507.$$

The reactor angle uses the $A_1$ projection input and the Cabibbo scale. The solar and atmospheric values additionally use Conditions 1 and 2. The complex CP phase remains open (§8.4).

**Comparison with JUNO, the global fit, and NuFIT 6.0.** The table compares the leading values with the named fits. NuFIT 6.0 entries use normal ordering.

| Angle | Leading value | Observed | Residual |
|-------|---------------|----------|----------|
| $\sin^2\theta_{12}$ | $0.308003$ | $0.3092 \pm 0.0087$ (direct JUNO) | $0.14\sigma$ |
| $\sin^2\theta_{12}$ | $0.308003$ | $0.3085 \pm 0.0073$ (post-JUNO global fit) | $0.07\sigma$ |
| $\sin^2\theta_{23}$ | $0.5507$ | $0.561^{+0.012}_{-0.015}$ (NuFIT 6.0, upper octant) | about $0.7\sigma$ |
| $\sin^2\theta_{13}$ | $0.02252$ | $0.02195 \pm 0.00056$ (NuFIT 6.0) | $1.01\sigma$ |

The global comparison includes the direct JUNO data. Both solar comparisons are retrodictions because the derivation followed the first results, with no parameter fitted to either solar value. The leading solar value uses the TBM pattern and the supplied conditions of §8.5 together with the Cabibbo scale fixed outside the neutrino comparison.

**The sum rule.** With Condition 2 the sum is $7/6+O(\lambda^3)$. Combining the post-JUNO solar and upper-octant atmospheric fits gives $2(0.3085)+0.561=1.178$. Adding the marginal errors in quadrature with zero covariance gives an illustrative uncertainty of about $0.020$, and hence a residual of about $0.6\sigma$ from $7/6$. The result uses the same solar and atmospheric estimates as the individual comparisons.

The remaining sections develop the framework's position in the broader landscape of tribimaximal-modification proposals (Section 8.7), the JUNO design-lifetime sensitivity for testing the $\sin^2\theta_{12}$ prediction at sub-percent precision (Section 8.8), and the coupled neutrino-mass / dark-energy result with DESI DR2 (Section 8.9).

***

## 8.7 Comparison with TM1/TM2 column-preservation patterns

Tribimaximal mixing was the leading phenomenological description of neutrino oscillation data until Daya Bay measured a non-zero $\theta_{13}$ in 2012. Since then, modified tribimaximal patterns have been the subject of a substantial literature, with the two best-known modifications preserving one column of the original tribimaximal matrix exactly: TM1 (first column preserved) and TM2 (second column preserved). Each gives a one-parameter family that accommodates the observed $\theta_{13}$ but predicts different values for the other two angles.

**TM1 and TM2 in the post-JUNO landscape.** Post-JUNO analyses by He and by Zhang find that TM2 is excluded at greater than $3.5\sigma$ while TM1 remains marginally viable. The framework's prediction sits well below both alternatives in tension with the post-JUNO global fit:

| Approach | Symmetry origin | $\sin^2\theta_{12}$ | $\sigma$ from observed |
|----------|----------------|---------------------|-----------------------|
| TM1 | postulated $A_4$ flavor | $0.3184$ | $1.35\sigma$ |
| TM2 | postulated $A_4$ flavor | $0.3408$ | $4.4\sigma$ |
| TM3 | postulated; $\theta_{13} = 0$ | — | excluded |
| **This work (leading)** | **cubic group $O$ of 3D space** | **$0.308003$** | **$0.07\sigma$** |

The comparison uses the post-JUNO global fit $\sin^2\theta_{12}=0.3085\pm0.0073$. TM1 uses $\sin^2\theta_{12}=1-(2/3)/\cos^2\theta_{13}$ and TM2 uses $\sin^2\theta_{12}=1/(3\cos^2\theta_{13})$, both with $\sin^2\theta_{13}=0.02195$.

**Three structural differences distinguish the framework from TM$_n$.**

*Symmetry origin.* The cubic-group calculation uses $A_4\subset O$ on the $T_1$ generation triplet. The simple-cubic link and gauge interpretation carry the conditions of §8.3.

*Mixing angles.* TM1 fixes $\theta_{12}$ given $\theta_{13}$. The cubic-group calculation gives three leading values with the inputs of §8.6. The comparison of precise measurements with those values depends on the higher-order terms.

*CP violation.* The surviving pattern in He’s analysis predicts $\sin\delta_{\text{CP}}=\pm0.998$. The cubic-group mixing matrix is real through order $\lambda^2$. A mechanism for a physical complex phase remains open (§8.4).

**The sum-rule comparison.** Condition 2 gives $2\sin^2\theta_{12}+\sin^2\theta_{23}=7/6+O(\lambda^3)$. The approximate $0.6\sigma$ comparison in §8.6 uses the upper-octant fit. The lower-octant central value $\sin^2\theta_{23}\approx0.455$ gives a sum of about $1.072$. TM1 and TM2 give different mixing correlations. A precise comparison depends on the atmospheric octant and the theory remainder.

## 8.8 JUNO sensitivity and tests of the flavor pattern

The JUNO sensitivity study projects uncertainties on $\sin^2\theta_{12}$ of about $0.0016$ after six years and $0.0010$ after twenty years under its forecast inputs. The comparisons below use an illustrative uncertainty of $0.0014$. [JUNO sensitivity study, Table 6](https://juser.fz-juelich.de/record/911312/files/Abusleme_2022_Chinese_Phys._C_46_123001.pdf)

**The leading solar value and the minimal truncation.** If a model takes $0.308003$ as its complete solar prediction, unchanged direct and global central values would differ from it by about $0.855\sigma$ and $0.355\sigma$, respectively, at the illustrative precision. Higher orders matter to a test of the proposed structure. In the minimal truncation $V_\ell=\exp(\lambda A_1+\lambda^2 A_2)$ with $-0.5\le b_{12}-b_{13}\le1$, the higher orders of that exponential shift $\sin^2\theta_{12}$ by $+0.0032$ to $+0.0044$. Independent terms in the full expansion are open.

**Comparison with TM1 and TM2.** The solar values $0.3184$ and $0.3408$ for TM1 and TM2 are separated from the leading value by about $7.4$ and $23$ times the illustrative uncertainty, respectively. Within the specified minimal truncation the corresponding separations are about $4.3$–$5.1$ and $20$–$21$ times that uncertainty. These are separations between model values on the chosen experimental scale.

**Sensitivity to Condition 2.** At fixed $b_{23}$ and $\lambda$ and ignoring higher orders, a fractional shift $\epsilon$ in $4/3$ changes $\sin^2\theta_{12}$ by $\epsilon\Delta_{23}/2$ to first order, with $\Delta_{23}=1/(2\pi^2)$. A $10\%$ shift gives about $0.0025$, about $29\%$ of the direct first-result uncertainty. The direct, global, and illustrative future solar uncertainties translate to about $34\%$, $29\%$, and $5.5\%$ on the coefficient under these conditions.

**What the measurements test.** Solar data compare directly with a model taking the leading solar value as complete. A test of the proposed cubic-group flavor structure uses the TBM and Cabibbo inputs, the separate normalization and Condition 2, and a controlled higher-order remainder. More precise solar and atmospheric data can test the exact $7/6$ sum as an additional phenomenological commitment. Testing the perturbative Condition 2 uses that correlation through order $\lambda^2$, with the atmospheric octant, covariance as applicable, and theory remainder included. Reactor data test the stated $A_1$ and Cabibbo inputs through the leading squared reactor angle, also subject to higher orders.

## 8.9 DESI DR2 and the neutrino mass bound

The flavor calculation and the cosmological mass bound compare different quantities. The framework heuristically favors a hierarchical normally ordered spectrum on the branch described in SM §8.4.

**The DESI DR2 + CMB bound.** The baseline $\Lambda$CDM fit with degenerate neutrino masses gives
$$\Sigma m_\nu < 0.0642\,\text{eV} \qquad (95\%\,\text{CL}).$$
In the analysis with additional oscillation information, the lightest mass is bounded by $m_l<0.023$ eV and normal ordering is preferred. The approximate normal-ordering minimum, $0.059$ eV, uses measured splittings and a negligible lightest mass, $\Sigma m_\nu^{\min}\simeq\sqrt{\Delta m_{21}^2}+\sqrt{\Delta m_{31}^2}$. The baseline upper limit is compatible with this value. [Elbers et al.](https://doi.org/10.1103/w9pk-xsk7)

**Dependence on the dark-energy model.** The reported tension between the baseline cosmological fit and the oscillation lower limit ranges from $2.7$ to $4.0\sigma$ depending on the statistic. The same study obtains a weaker upper limit, $0.163$ eV, in $w_0w_a$CDM. Bertini *et al.* separately constrain the running-vacuum parameter $\nu$. A joint neutrino-mass fit in the OI Type II model remains open. [Elbers et al.](https://doi.org/10.1103/w9pk-xsk7) · [Bertini et al.](https://arxiv.org/abs/2509.24026)

## 8.10 Chapter close: the framework's empirical record in the neutrino sector

The leading solar value $0.308003$ lies $0.14\sigma$ from direct JUNO and $0.07\sigma$ from the overlapping global fit. The cited reactor and atmospheric comparisons give about $1.01\sigma$ and $0.7\sigma$. The approximate $0.6\sigma$ comparison with the leading sum uses those solar and atmospheric estimates on the upper-octant branch.

The flavor calculation shares the Cabibbo scale and the off-democratic projection with the quark-sector calculations. The solar and atmospheric shifts also require the independent normalization and Condition 2. The observed values constrain the proposed leading flavor pattern, with no parameter fitted to the solar measurements. New precision can test specified flavor models once their higher-order terms are controlled.

The separate cosmological comparison is with an upper bound on the mass sum. The normal-ordering near-minimum value uses measured splittings and the negligible-lightest-mass assumption.

**Forward pointers.** Chapter 9 examines the universality of the framework's structural results and places the fundamental-physics comparisons in the wider theoretical landscape. Part III turns to the cascade through chemistry, life, and intelligence, and Part IV develops applications and forward predictions.

***
