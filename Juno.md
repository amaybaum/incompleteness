# A Parameter-Free Prediction of the Solar Mixing Angle from Cubic-Group Flavor Structure, Tested by JUNO

**Author:** Alex Maybaum  
**Date:** April 2026  
**Status:** DRAFT PRE-PRINT  
**Classification:** Theoretical Physics / High Energy Physics / Neutrino Phenomenology

---

## Abstract

The first JUNO measurement of reactor neutrino oscillations reports sin²θ₁₂ = 0.3092 ± 0.0087, with the post-JUNO global fit tightening this to sin²θ₁₂ = 0.3085 ± 0.0073. We show that treating the cubic point group O — the symmetry group of three-dimensional space — as the underlying symmetry of the lepton sector yields the prediction sin²θ₁₂ = 1/3 − 1/(4π²) = 0.3080, matching the global fit at 0.07σ, with no parameter fit to the value of sin²θ₁₂. The same construction gives sin²θ₁₃ = 4/(18π²) = 0.02252 and sin²θ₂₃ = 1/2 + 1/(2π²) = 0.5507, each consistent with NuFIT 6.0 within 1.1σ, and forces the exact sum rule 2sin²θ₁₂ + sin²θ₂₃ = 7/6 — a clean discriminator from the TM1 and TM2 patterns currently analyzed against JUNO. The angle predictions follow from a discrete μ-τ parity together with one cubic-group structural relation between the U-even and U-odd components of the second-order perturbation. The Cabibbo angle λ = 1/(π√2) = 0.22508, set by the cubic Brillouin-zone geometry, sets the perturbation scale and matches the observed value to 0.04%. JUNO's design-lifetime precision of ±0.0014 will test the prediction at sub-percent level.

---

## 1. Introduction

Tribimaximal (TBM) mixing [Harrison 2002] predicts the lepton mixing angles sin²θ₁₂ = 1/3, sin²θ₂₃ = 1/2, and sin²θ₁₃ = 0. It was the leading phenomenological description of neutrino oscillation data until Daya Bay measured a nonzero θ₁₃ [Daya Bay 2012]. Since then, modified TBM patterns have been the subject of a substantial literature [King-Luhn 2013; He-Zee 2011; He 2015; Petcov-Titov 2018]. The two best-known modifications preserve one column of the original TBM matrix exactly: TM1 (first column) and TM2 (second column). Each gives a one-parameter family that accommodates the observed θ₁₃ but predicts different values for the other two angles.

The first JUNO results, released in November 2025, sharpen this picture. JUNO reports

**sin²θ₁₂ = 0.3092 ± 0.0087**

from 59.1 days of data [JUNO 2025]. Combining JUNO with all prior solar and reactor results, Capozzi *et al.* [Capozzi 2025] obtain

**sin²θ₁₂ = 0.3085 ± 0.0073**

At this precision, TBM-modification proposals can be discriminated at the few-percent level. He [He 2025] finds that TM2 is excluded at >3.5σ while TM1 remains viable; Zhang reports similar results [Zhang 2025]. Structural assumptions about flavor symmetry are now being tested directly against data.

Most existing TBM-modification proposals start from a discrete *flavor symmetry* — typically A₄, S₄, or a Z₂ residual — postulated as an axiom of the lepton sector. The minimal modifications then preserve one column of the TBM matrix or one residual symmetry of the neutrino mass matrix, yielding one-parameter correlations between angles.

In this paper we take a different starting point: the cubic point group O, which is the symmetry group of three-dimensional space. The subgroup A₄ ⊂ O that generates TBM at zeroth order [Ma-Rajasekaran 2001; Altarelli-Feruglio 2010] is the orientation-preserving subgroup of O. We adopt as a working hypothesis that the three fermion generations transform under O as the triplet irrep T₁. The cubic group then has a natural (3, 2, 1) multiplet structure that matches the three-generation pattern (Sec. 2.1).

The Cabibbo angle, λ² = 1/(2π²), sets the perturbation scale; it is fixed by a single cubic Brillouin-zone distance (Sec. 2.2). The breaking of TBM is then controlled by a discrete μ-τ parity (the U-parity of S₄ ⊃ A₄) together with one normalization condition (Sec. 3.4). The resulting predictions are:

- **sin²θ₁₂ = 1/3 − 1/(4π²) = 0.3080**
- **sin²θ₁₃ = 4/(18π²) = 0.02252**
- **sin²θ₂₃ = 1/2 + 1/(2π²) = 0.5507**

The prediction for sin²θ₁₂ contains no parameter fit to sin²θ₁₂: the input 1/3 comes from A₄ representation theory, λ² = 1/(2π²) from the cubic Brillouin geometry that also reproduces the Cabibbo angle to 0.04% (Sec. 2.2), and the 1/(4π²) correction from a cubic-group structural relation between U-even and U-odd components of the second-order perturbation (Sec. 3.4) [Maybaum 2026]. The 0.07σ match with the post-JUNO global fit is therefore a test of structural relations fixed before JUNO took data.

The paper is organized as follows. Section 2 sets up the cubic-group structure and derives the perturbation scale. Section 3 computes the deviations from TBM at O(λ²) and derives the sum rule. Section 4 presents the predictions and compares them with JUNO, the post-JUNO global fit, and competing TM1/TM2 patterns. Section 5 covers the remaining angles. Section 6 discusses falsifiability under JUNO's projected long-term precision. Section 7 concludes.

## 2. Cubic-group flavor structure

### 2.1 The cubic group O and its A₄ subgroup

The cubic point group O is the rotation symmetry group of three-dimensional space, the unique finite point group with a six-element generator set {±ê₁, ±ê₂, ±ê₃} — six minimal-length translations corresponding to forward and backward motion along three orthogonal axes. In the lattice realization of the OI framework, this six-element set arises from coupling-degree minimization (K = 2d = 6 for d = 3), and the multiplicities (3, 2, 1) under the action of O on these six directions match the structure of one Standard Model fermion generation (quark triplet, lepton doublet, singlet). The triplet sector T₁ then carries the three generations. We adopt this identification here as a working hypothesis; the detailed argument from coupling-degree minimization to the (3, 2, 1) decomposition of T₁ ⊕ E ⊕ A₁ is given in [Maybaum 2026] (Theorems 6 and 7).

The full octahedral rotation group O has order 24 and is isomorphic to S₄. Its irreducible representations decompose as

**irreps(O) = A₁ ⊕ A₂ ⊕ E ⊕ T₁ ⊕ T₂**

of dimensions 1, 1, 2, 3, 3. The subgroup A₄ ⊂ O keeps {A₁, A₂, E, T₁} but identifies A₂ with A₁, giving the standard A₄ content A ⊕ A' ⊕ A'' ⊕ T of dimensions 1, 1, 1, 3.

We take T₁ as the generation triplet. Realize it by the three Cartesian unit vectors {e₁, e₂, e₃} acted on by the 24 rotations of O. The democratic vector

**ĥ = (1/√3)(e₁ + e₂ + e₃)**

is the only direction fixed by the ℤ₃ cyclic subgroup. The plane perpendicular to ĥ carries the doublet E. This is the geometric origin of TBM: the second column of U_TBM is exactly ĥ, and the first and third columns lie in the plane perpendicular to it, oriented by μ-τ exchange.

### 2.2 The Cabibbo scale from cubic Brillouin geometry

We identify the perturbation parameter λ with the Cabibbo angle. In a lattice realization of the cubic-group flavor structure, the three generations occupy the three T₁ corners of the cubic Brillouin zone at momenta X_j = π·e_j (j = 1, 2, 3). The inter-generation distance in momentum space is

**|X_i − X_j| = π√2 (i ≠ j)**

a fixed geometric constant of the cubic lattice. The leading-order inter-generation mixing matrix element is the continuum fermion propagator at this momentum, |M_ij| = |S(X_j − X_i)| = 1/|X_j − X_i|, where the 1/|q| scaling (rather than 1/|q|²) follows from chirality preservation in the taste-changing vertex (the vertex trace Tr[γ·S(q)] ∝ 1/|q| in the massless limit). Identifying this with the Cabibbo angle gives

**λ = 1/(π√2) = 0.22508**

matching the observed value λ_obs = 0.22500 ± 0.00067 [PDG 2024] to 0.04%. Squaring,

**λ² = 1/(2π²) = 0.05066**

sets the overall scale of O(λ²) corrections. The full derivation of λ = 1/(π√2) from the lattice fermion propagator and the chirality-preservation argument is given in [Maybaum 2026].

A second geometric quantity will appear. The angle between any generation axis e_i and the democratic direction ĥ satisfies e_i · ĥ = 1/√3, so cos²(∠(e_i, ĥ)) = 1/3 and sin²(∠(e_i, ĥ)) = 2/3. We identify the Wolfenstein parameter A with this quantity:

**A = √(2/3) = 0.8165**

agreeing with the PDG value A = 0.826 ± 0.012 at 0.23σ. The combination A² = 2/3 enters the inter-generation projection geometry, and A⁴ = 4/9 appears directly in the deviation Δ₁₃ below.

### 2.3 The PMNS matrix in the Altarelli-Feruglio basis

We work in the Altarelli-Feruglio (AF) basis [Altarelli-Feruglio 2010]. In this basis the neutrino sector realizes TBM exactly (after diagonalization of the seesaw matrix), and all deviations from TBM come from the charged-lepton mass matrix. The PMNS matrix is

**U_PMNS = V_ℓ† · U_TBM**

where V_ℓ is the charged-lepton rotation that diagonalizes M_ℓ M_ℓ†, and

```
            ⎛  √(2/3)   √(1/3)    0      ⎞
U_TBM   =   ⎜ -√(1/6)   √(1/3)  -√(1/2)  ⎟
            ⎝ -√(1/6)   √(1/3)   √(1/2)  ⎠
```

Expanding V_ℓ in λ,

**V_ℓ = exp(λA₁ + λ²A₂ + O(λ³))**

with A₁, A₂ real antisymmetric 3×3 matrices. The remaining task is to determine A₁ and A₂ from the structural ingredients of the cubic geometry.

## 3. U-parity grading and the sum rule

### 3.1 The U-parity generator

In the AF basis, the μ-τ exchange generator U ∈ S₄ acts on the generation indices by exchanging the second and third:

```
        ⎛ 1  0  0 ⎞
U   =   ⎜ 0  0  1 ⎟
        ⎝ 0  1  0 ⎠
```

Conjugation by U defines a ℤ₂ grading on antisymmetric matrices: A is **U-even** if UAU⁻¹ = +A, **U-odd** if UAU⁻¹ = −A. With (E_{ij})_{kl} = δ_{ik}δ_{jl} − δ_{il}δ_{jk}, the decomposition is:

- **U-even**: E₁₂ + E₁₃
- **U-odd**: E₁₂ − E₁₃, E₂₃

The unique U-odd combination antisymmetric in (μ, τ) is E₂₃; the unique U-odd combination relating the first generation to the second/third is E₁₂ − E₁₃.

### 3.2 Determination of A₁

Three conditions fix A₁ uniquely. First, θ₁₃ is zero at TBM zeroth order, but the data require sinθ₁₃ = O(λ); so A₁ must contribute to the (1,3) element of V_ℓ† U_TBM. Second, both Δ₁₂ ≡ sin²θ₁₂ − 1/3 and Δ₂₃ ≡ sin²θ₂₃ − 1/2 are observed to be O(λ²) (not O(λ)), which fixes A₁ up to an overall sign. Third, the coefficient is set by the geometric identity

**sinθ₁₃ = A²λ**

which follows from the projection geometry: each end of an inter-generation mixing vertex projects onto the plane perpendicular to ĥ, contributing a factor sin(∠(e_i, ĥ)) = A, for a total A².

The result is

**A₁ = (√2/3)(E₁₂ − E₁₃)**

A₁ is purely U-odd: UA₁U⁻¹ = −A₁. Geometrically, it is a rotation by angle A² = 2/3 around the axis (e₂ + e₃)/√2, reproducing the structural identity above.

### 3.3 Deviations to O(λ²)

Expanding V_ℓ to second order,

**V_ℓ = I + λA₁ + λ²(A₂ + ½A₁²) + O(λ³)**

and writing the most general antisymmetric A₂ as

**A₂ = b₁₂E₁₂ + b₁₃E₁₃ + b₂₃E₂₃**

we compute |U_PMNS,ij|² to O(λ²). The PMNS angles satisfy sin²θ₁₃ = |U_e3|², sin²θ₁₂ cos²θ₁₃ = |U_e2|², and sin²θ₂₃ cos²θ₁₃ = |U_μ3|². The deviations from TBM are:

- **Δ₁₃ = (4/9)λ² = A⁴λ²**
- **Δ₁₂ = −(2/3)(b₁₂ + b₁₃) λ²**
- **Δ₂₃ = b₂₃ λ²**

Three observations follow.

**(i) Δ₁₃ is fully determined by A₁ alone.** The A₂ parameters cancel from |U_e3|² at O(λ²), so sin²θ₁₃ = (4/9)λ² is fixed without reference to A₂. Equivalently, the structural identity sinθ₁₃ = A²λ is exact at O(λ) and receives no O(λ²) correction.

**(ii) The combination b₁₂ − b₁₃ does not enter any of the three angles.** It is identified physically with the CP-violating Dirac phase δ_CP, which the present analysis leaves undetermined.

**(iii) The remaining structure depends on two combinations:** (b₁₂ + b₁₃) controlling Δ₁₂ and b₂₃ controlling Δ₂₃. The first is the U-even, the second the dominant U-odd coefficient of A₂, with b₁₂ − b₁₃ the sub-dominant U-odd combination.

### 3.4 Sum rule and absolute normalization

The deviations depend on two scalar combinations of A₂: (b₁₂ + b₁₃) controlling Δ₁₂, and b₂₃ controlling Δ₂₃. We fix the normalization with two conditions.

**Condition 1 (natural normalization).** Take b₂₃ = 1. This sets A₂ to enter the perturbation series at unit strength relative to λ². It is a labeling convention rather than a physical input — fixing the normalization of the O(λ²) expansion before b₁₂ + b₁₃ is determined.

**Condition 2 (cubic-group structural relation).** Take

**b₂₃ = (4/3)(b₁₂ + b₁₃)**

which with Condition 1 gives b₁₂ + b₁₃ = 3/4. Unlike Condition 1, this is a substantive physical input: it relates the dominant U-odd coefficient of A₂ to the U-even combination through a fixed numerical factor 4/3.

The geometric interpretation is that

**4/3 = 2A² = 2 sin²(∠(e_i, ĥ))**

where A = √(2/3) is the off-democratic projection of any generation axis (Sec. 2.2). The factor decomposes as a *partner-count × per-partner projection*: the U-even combination E₁₂+E₁₃ couples generation e₁ to its two partners {e₂, e₃}, each contributing factor A² from the ĥ-perpendicular projection geometry — total 2 × A² = 4/3. The dominant U-odd combination E₂₃ couples e₂ to its single partner e₃, with no analogous multiplicity, giving relative weight 1. The same projection geometry produces sinθ₁₃ = A²λ at O(λ) via a single-vertex projection (Sec. 3.2). A complete derivation of the structural relation from the lattice Yukawa structure remains an open task; we present it here as a structural relation supported by the geometric argument above and by the broader cubic-lattice framework of [Maybaum 2026].

We treat Condition 2 as a structural input to the present analysis and quote our predictions *conditional* on it. The angle predictions of Sec. 3.5 and the sum rule below thus stand or fall with Condition 2: empirical agreement at 0.07σ on sin²θ₁₂ is, in this sense, a nontrivial test of Condition 2 itself.

At the angle level, this is equivalent to

**2Δ₁₂ + Δ₂₃ = 0**

which is testable directly against data (Sec. 4.3). The combination b₁₂ − b₁₃ remains free; we identify it in Sec. 4.2 with δ_CP. The present analysis therefore predicts all three angles but not δ_CP.

### 3.5 Numerical predictions

Substituting b₂₃ = 1, b₁₂ + b₁₃ = 3/4, and λ² = 1/(2π²):

- **sin²θ₁₂ = 1/3 − 1/(4π²) = 0.30798**
- **sin²θ₁₃ = 4/(18π²) = 0.02252**
- **sin²θ₂₃ = 1/2 + 1/(2π²) = 0.55066**

The first formula for sin²θ₁₃ follows from A² = 2/3 and λ² = 1/(2π²) together with the constraints on A₁; it does not use the normalization conditions on A₂. The other two additionally use Conditions 1 and 2.

## 4. The sin²θ₁₂ prediction

### 4.1 Numerical value and comparison with data

The headline prediction is

> **sin²θ₁₂ = 1/3 − 1/(4π²) = 0.30798**

Comparison with current measurements:

| Source | sin²θ₁₂ | σ from prediction |
|---|---|---|
| This work | 0.30798 | --- |
| JUNO direct | 0.3092 ± 0.0087 | 0.14σ |
| Post-JUNO global | 0.3085 ± 0.0073 | 0.07σ |

The prediction agrees with the post-JUNO global fit at 0.07σ. Both inputs entering the prediction were fixed before JUNO: 1/3 is the A₄ TBM zeroth-order value, and λ² = 1/(2π²) is the squared Cabibbo angle predicted from the same cubic Brillouin geometry that gives λ = 0.22508 (matching observation to 0.04%).

### 4.2 Comparison with column-preservation patterns

The two best-known minimal modifications of TBM preserve one column of U_TBM exactly. Both have been analyzed against JUNO recently [He 2025; Zhang 2025]. Comparison summary:

| Approach | Symmetry origin | sin²θ₁₂ | σ |
|----------|----------------|---------|---|
| TM1 | postulated A₄ flavor | 0.3184 | 1.35σ |
| TM2 | postulated A₄ flavor | 0.3408 | 4.4σ |
| TM3 | postulated; θ₁₃ = 0 | --- | excluded |
| **This work** | **cubic group O of 3D space** | **0.3080** | **0.07σ** |

(Comparing against post-JUNO global fit 0.3085 ± 0.0073. TM1 uses sin²θ₁₂ = 1 − (2/3)/cos²θ₁₃; TM2 uses sin²θ₁₂ = 1/(3cos²θ₁₃); both with sin²θ₁₃ = 0.02195.)

Three differences distinguish the present prediction from TM_n:

**(i) Symmetry origin.** TM1, TM2, and TM3 take a discrete flavor symmetry as an axiom of the lepton sector. The cubic-group prediction here uses A₄ ⊂ O, where O is the symmetry group of three-dimensional space and the three generations transform as the T₁ irrep (Sec. 2.1 working hypothesis).

**(ii) Independence of predictions.** TM1 gives a one-parameter correlation, sin²θ₁₂ = 1 − (2/3)/cos²θ₁₃, fixing θ₁₂ given θ₁₃ but predicting neither separately. The cubic-group analysis predicts all three angles as fixed numerical values, with no parameter common to them (Sec. 3.5).

**(iii) CP violation.** He's surviving pattern predicts sin δ_CP = ±0.998, close to maximal. Here, δ_CP is identified with the only remaining free parameter at O(λ²), namely b₁₂ − b₁₃, which does not enter any of the three angles. The angle predictions therefore stand independently of any value of δ_CP, and the present paper makes no prediction for it.

The bottom line: the cubic-group prediction is closer to the post-JUNO global fit by a factor of about 20 in σ-distance than the best surviving column-preservation pattern, and at the same time makes more falsifiable claims (three independent angles plus the sum rule below).

### 4.3 The sum-rule discriminator

The cubic-group prediction implies

**2sin²θ₁₂ + sin²θ₂₃ = 7/6 = 1.1667**

versus the observed 2(0.3085) + 0.561 = 1.178 ± 0.020 (using the post-JUNO sin²θ₁₂ and the NuFIT 6.0 NO best fit for sin²θ₂₃). The agreement is at 0.6σ. This sum rule is the angle-level statement of b₂₃ = (4/3)(b₁₂ + b₁₃), which is structural in the cubic-group setup. TM1 and TM2 do not produce this combination as an exact sum rule; in TM2, sin²θ₁₂ is determined by θ₁₃ alone with no θ₂₃ correlation. A direct measurement of 2sin²θ₁₂ + sin²θ₂₃ at the 0.005 level is therefore the sharpest data-side test that distinguishes the two classes of TBM modification.

## 5. The remaining angles

### 5.1 sin²θ₁₃

The formula for sin²θ₁₃ is fully derived: at O(λ²) the A₂ parameters cancel from |U_e3|², leaving sin²θ₁₃ = A⁴λ² = 4/(18π²) = 0.02252. The NuFIT 6.0 best fit (normal ordering) is 0.02195 ± 0.00056, agreeing at 1.01σ. Equivalently,

**sinθ₁₃ = A²λ = (2/3) · 1/(π√2) = 0.1500**

giving θ₁₃ = 8.63°, compared with the observed 8.56° ± 0.10°.

### 5.2 sin²θ₂₃

The formula gives sin²θ₂₃ = 1/2 + 1/(2π²) = 0.5507. NuFIT 6.0 (NO) gives sin²θ₂₃ = 0.561⁺⁰·⁰¹²₋₀.₀₁₅, agreeing at 0.74σ. The prediction lies in the second octant, in line with the current global preference. The sum rule 2sin²θ₁₂ + sin²θ₂₃ = 7/6 ties this directly to sin²θ₁₂:

**sin²θ₂₃ = 7/6 − 2sin²θ₁₂**

A ±0.0014 ultimate JUNO error on sin²θ₁₂ then implies a ±0.0028 error on the predicted sin²θ₂₃, comparable to the current direct measurement.

### 5.3 Summary

| Angle | Prediction | Measurement | σ |
|-------|-----------|-------------|---|
| sin²θ₁₂ | 1/3 − 1/(4π²) = 0.3080 | 0.3085 ± 0.0073 | 0.07 |
| sin²θ₁₃ | 4/(18π²) = 0.02252 | 0.02195 ± 0.00056 | 1.01 |
| sin²θ₂₃ | 1/2 + 1/(2π²) = 0.5507 | 0.561⁺⁰·⁰¹²₋₀.₀₁₅ | 0.74 |

All three predictions agree with observation within 1.1σ.

## 6. Falsifiability

The prediction is sharp: λ² = 1/(2π²) is fixed independently by the Cabibbo angle, and the coefficient 1/(4π²) in Δ₁₂ has no adjustable input. Three experimental directions test it.

**Sub-percent precision on sin²θ₁₂.** Over its 30-year design lifetime, JUNO is projected to reach sin²θ₁₂ = 0.3092 ± 0.0014, a 6× improvement over the current first result. At that precision the prediction 0.30798 is tested at 0.86σ (using the JUNO 59-day central value) or 0.36σ (using the post-JUNO global central value). An ultimate JUNO 2σ disagreement with 0.30798 would falsify the prediction.

**The sum rule.** The prediction 2sin²θ₁₂ + sin²θ₂₃ = 7/6 is sharper than either angle alone: it ties JUNO's reactor measurement to the atmospheric measurements at DUNE, T2HK, and Hyper-Kamiokande. As both improve, the sum rule will be tested at the 0.005 level — a sharper test than either side separately.

**δ_CP.** The free parameter b₁₂ − b₁₃ of A₂ does not enter any angle prediction, so the framework is consistent with any δ_CP. Long-baseline measurements at DUNE and Hyper-Kamiokande will determine this remaining parameter directly.

## 7. Conclusion

We have derived sin²θ₁₂ = 1/3 − 1/(4π²) = 0.3080 from cubic-group flavor structure, matching the post-JUNO global fit at 0.07σ with no parameter fit to sin²θ₁₂. The same construction predicts sin²θ₁₃ and sin²θ₂₃ within 1.1σ of the NuFIT 6.0 best fits, and forces the exact sum rule 2sin²θ₁₂ + sin²θ₂₃ = 7/6, which distinguishes the prediction from the TM1, TM2, and TM3 column-preservation patterns. The angle predictions are conditional on the cubic-group structural relation b₂₃ = (4/3)(b₁₂+b₁₃) (Condition 2); the empirical match at 0.07σ on sin²θ₁₂ is, in this sense, a nontrivial test of that relation. The Cabibbo scale λ² = 1/(2π²) entering the prediction is set independently by cubic Brillouin-zone geometry and matches the observed Cabibbo angle to 0.04%.

JUNO's projected long-term precision will test the prediction at sub-percent level over the next decade. Combined with atmospheric measurements at DUNE, T2HK, and Hyper-Kamiokande, this will sharply test the sum rule. A confirmed result at JUNO's ultimate precision would support cubic-group flavor structure as a viable origin of the lepton mixing pattern.

## References

[1] P. F. Harrison, D. H. Perkins, W. G. Scott, "Tri-bimaximal mixing and the neutrino oscillation data," Phys. Lett. B 530, 167 (2002).

[2] F. P. An et al. (Daya Bay), "Observation of electron-antineutrino disappearance at Daya Bay," Phys. Rev. Lett. 108, 171803 (2012).

[3] S. F. King and C. Luhn, "Neutrino mass and mixing with discrete symmetry," Rep. Prog. Phys. 76, 056201 (2013).

[4] X.-G. He and A. Zee, "Minimal modification to tribimaximal mixing," Phys. Rev. D 84, 053004 (2011).

[5] X.-G. He, "TM1 mixing pattern from A₄," Chin. J. Phys. 53, 100101 (2015).

[6] S. T. Petcov and A. V. Titov, "Assessing the viability of A₄, S₄ and A₅ flavour symmetries for description of neutrino mixing," Phys. Rev. D 97, 115045 (2018).

[7] JUNO Collaboration (A. Abusleme et al.), "First measurement of reactor neutrino oscillations at JUNO," arXiv:2511.14593 (2025).

[8] F. Capozzi, E. Lisi, F. Marcone, A. Marrone, A. Palazzo, "Updated bounds on the (1,2) neutrino oscillation parameters after first JUNO results," arXiv:2511.21650 (2025).

[9] X.-G. He, "Modified Tri-bimaximal neutrino mixing confronted by JUNO θ₁₂ measurement," arXiv:2511.15978 (2025).

[10] D. Zhang, "Trimaximal mixing patterns meet the first JUNO result," arXiv:2511.15654 (2025).

[11] E. Ma and G. Rajasekaran, "Softly broken A₄ symmetry for nearly degenerate neutrino masses," Phys. Rev. D 64, 113012 (2001).

[12] G. Altarelli and F. Feruglio, "Discrete flavor symmetries and models of neutrino mixing," Rev. Mod. Phys. 82, 2701 (2010).

[13] S. Navas et al. (Particle Data Group), Phys. Rev. D 110, 030001 (2024).

[14] I. Esteban, M. C. Gonzalez-Garcia, M. Maltoni, T. Schwetz, A. Zhou, "NuFIT 6.0: three-flavour global analyses of neutrino oscillation experiments," JHEP (2024); www.nu-fit.org.

[15] A. Maybaum, *The Incompleteness of Observation* (Zenodo archive, 2026), https://doi.org/10.5281/zenodo.19060318.
