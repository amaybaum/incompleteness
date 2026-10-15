# The Class A Lorentz-invariance-violation item: original preregistration and correction

The preregistered item is the Class A entry *Leading Lorentz-invariance-violation coefficient* of
`papers/Substratum.md` §6.4, under that section's pre-registration commitment. It entered the
manuscript at `69da7913` (2026-06-07). The manuscript is a working draft and carries only its
current statement; the item as preregistered is preserved here verbatim.

## Original preregistration

From `papers/Substratum.md` at `e30c635a` (blob `4e3fc9d0f14355b92d371d29cbe5ce2eec99ec08`),
lines 431–433:

````markdown
- *Leading Lorentz-invariance-violation coefficient.* The cubic-lattice dispersion relation ([SM, §4.4] Theorem 4, generalized to d = 3: $\cos(\omega\epsilon) = \frac{1}{3}\sum_{i=1}^3 \cos(k_i \epsilon)$ for a massless mode) yields standard emergent dispersion $\omega = |k|$ at leading order. Series expansion gives the first correction as a direction-dependent quadratic term $\omega^2 = k^2[1 - 2\delta(\hat k)(k\epsilon)^2 + O((k\epsilon)^4)]$, with $\delta(\hat k) = \frac{1}{24}\sum_i \hat k_i^4 - \frac{1}{72}$ evaluated on the rigid $\mathbb{Z}^3$ representative. The rigid-lattice anisotropy (values $\delta_{[100]} = 1/36$, $\delta_{[110]} = 1/144$, $\delta_{[111]} = 0$ — the dispersion is exactly linear along the body diagonals, $\omega = k/\sqrt{3}$ to all orders) is a *physical, direction-dependent* prediction. Its absolute orientation in space is gauge: generator (iv) of §4 gauges the rigid orientation of the cubic representative. The anisotropy *pattern* — its fourfold $\ell=4$ cubic-harmonic structure and the direction-differences $\delta_{[100]}-\delta_{[111]}$ — is gauge-invariant, since generator (iv) preserves the octahedral structure and does not identify $\mathbb{Z}^3$ with a generic isotropic graph (which lacks the octahedral structure the gauge group requires, [SM §4.5–4.6]). The orientation-averaged coefficient $\langle\delta\rangle = 1/90$ is a direction-summary of this anisotropy, and the framework predicts the emergent dispersion
$$\omega^2 = k^2\left[1 - \frac{4}{45}\left(\frac{E}{M_{\text{Pl}}}\right)^2 + O\left(\left(\frac{E}{M_{\text{Pl}}}\right)^4\right)\right]$$
after using $\epsilon = 2 l_p$ and $k\epsilon = 2 E/M_{\text{Pl}}$. Three structural features: (i) *subluminal*, since $\delta(\hat k) \geq 0$ everywhere on the sphere ($\langle\delta\rangle > 0$ is invariant under orientation-averaging); (ii) *no linear-in-$E/M_{\text{Pl}}$ term*, because the even-parity cosines in the dispersion admit no $\mathcal{O}(k^3)$ contribution — any demonstration of linear LIV at any scale therefore falsifies the framework's substrate-level commitment to the cubic-lattice wave equation; (iii) *specific coefficient* $4/45$, fixed by the cubic-lattice coordination and isotropy-gauge average, not tunable. Current quadratic-LIV bounds from GRB time-of-flight reach only $E_{\text{QG}} \gtrsim 10^6$ GeV (roughly thirteen orders of magnitude below $M_{\text{Pl}}$), so the $4/45$ coefficient is a structural prediction not yet near-term testable at the magnitude level; linear-LIV tests, by contrast, are already at sensitivities where any positive detection falsifies.
````

## Correction (2026-10-15)

**The amplitude carries σ.** The tree-level expansion of the cubic-lattice dispersion is
ω² = k²[1 − 2⟨δ⟩(kε)² + O((kε)⁴)] = k²[1 − (kε)²/45 + O((kε)⁴)], with ⟨δ⟩ = 1/90.

- The preregistered 4/45 came from ε = 2 l_p, which is kε = 2E/M_Pl.
- The gap equation gives ε = 2√σ l_p for an entropy σ per boundary mode ([GR §3.1, §4]), so
  kε = 2√σ E/M_Pl.
- The coefficient of (E/M_Pl)² is therefore 4σ/45. It is 4/45 only at σ = 1, which the framework
  does not determine ([GR §3.1]; under σ ≤ ln q it is unavailable for a single q = 2 mode).

**Classification, amended.**

- **Class A, tree level, under the stated assumptions.** These are: the observer-level
  nearest-neighbor branch and the coarse-graining bridge of [SM §4.1], with the dispersion as
  stated there.
  - The lattice coefficient 1/45 of (kε)², equivalently ⟨δ⟩ = 1/90.
  - The direction-dependent anisotropy with its ℓ = 4 cubic-harmonic pattern. Its directional
    values are δ_[100] = 1/36, δ_[110] = 1/144 and δ_[111] = 0, so their ratios, 4 : 1 : 0, do not
    depend on σ.
  - Subluminality in every direction.
  - The absence of a linear-in-E term.
- **Conditional on σ.** The physical amplitude, the coefficient 4σ/45 of (E/M_Pl)².
  - It is not a parameter-free numerical prediction.
  - A measurement of the amplitude would constrain σ: a measured orientation-averaged
    coefficient c₂ gives σ = 45c₂/4. It would not falsify the coefficient independently.
  - Linear LIV, superluminal propagation in any direction, or an anisotropy pattern other than
    the cubic one would falsify the Class A content whatever σ is.
- **Open.**
  - Protection of the tree-level coefficient in the interacting theory, against radiative
    corrections ([SM §3.1]).
  - The coarse-graining bridge on which the observer-level dispersion rests ([SM §4.1]).

**Where the corrected statement is carried.**

- `papers/Substratum.md` §6.4.
- `papers/SM.md`: §4, and the open-problems paragraph of §8.
- `papers/Explainer.md`.
- `book/ch04-methodology.md`, with its mirror in `book/The-Incompleteness-of-Observation-FULL.md`.
