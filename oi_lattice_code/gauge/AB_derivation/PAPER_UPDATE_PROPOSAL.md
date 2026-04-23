# Proposed updates to SM.md reflecting the A·B derivation

**Status**: Preliminary first-principles calculation of A·B yielding **48 ± 15%**,
consistent with the fitted value 46.4 at the 4% level (central value) within
the uncertainty budget. This upgrades the A·B parameter from a fitted
retrodiction to a computed (if imprecise) first-principles prediction.

**Recommendation**: Rather than claiming the open task is fully closed, update the
paper's language to reflect a **preliminary derivation at ~15% precision**
with a clear roadmap for tightening. Keeping the caveats intact is important
because:

1. The calculation has methodological approximations (Wilson-plaquette V_3g
   used as leading piece of induced Γ_3; no lattice V_4g corrections;
   FP ghost applied despite framework having no formal gauge fixing).
2. The b_0-capture calibration is from standard QCD, assuming universal
   lattice artifact scaling.
3. N→∞ extrapolation still has ±10% uncertainty.
4. Subleading contributions (F³ from c_F3, lattice V_4g) could shift the
   result by ±10%.

The 4% central-value agreement is *within* the 15% error band, not a
rigorous tight test. It should be presented as a strong consistency check,
not a precision match.

---

## Suggested changes

### Change 1: Bullet about A·ln(1+B·...) (around line 572)

**Current:**

> *A·ln(1+B·C_2 g_0²) with (A, B) = (8.3, 5.59)*: the resummed gauge
> self-energy contribution. [...] In the current formulation, A and B are
> determined by matching to the observed SU(2) and SU(3) couplings at M_Z,
> given the structurally computed 1/α_0 and the empirically fixed δ_0.
> **Deriving (A, B) directly from a two-loop lattice PT computation of the
> C_2-dependent threshold in the induced gauge theory is an open
> computational task — when completed, it would upgrade the SU(2) and SU(3)
> entries from retrodictions to strict first-principles predictions.**

**Proposed replacement for the bolded sentence:**

> A preliminary first-principles derivation of the leading coefficient
> A·B from 2-loop lattice perturbation theory in the induced gauge theory
> gives A·B = 48 ± 15%, consistent with the fitted 46.4 at the level of
> the extrapolation uncertainty (§6.2.1). This upgrades the SU(2) and
> SU(3) entries from retrodictions to first-principles predictions at
> ~15% precision. Separating A from B individually, and reducing the
> precision below 10%, remain open tasks.

### Change 2: In structural constraint (iii), around line 590

**Current (final sentence):**

> The step from 1/(1-Σ) to the logarithm is not derived in the current
> work; the log form should be read as a constrained parameterization
> consistent with the resummation structure, not as a derived result.
> **An explicit two-loop lattice PT derivation in the induced gauge theory
> is an open computational task.**

**Proposed:**

> The step from 1/(1-Σ) to the logarithm is not derived in the current
> work; the log form should be read as a constrained parameterization
> consistent with the resummation structure, not as a derived result.
> The leading coefficient A·B (the `(C_2·g_0²)¹` term in the expansion)
> has been computed from 2-loop lattice PT in the induced gauge theory
> (§6.2.1), giving A·B = 48 ± 15% in agreement with the fitted 46.4.
> Separating A from B requires computing the next-order coefficient and
> is left for future work.

### Change 3: In Status of the rows (around line 614)

**Current:**

> [...] The SU(2) and SU(3) rows are retrodictions, not predictions.
> **Deriving (A, B) directly from a two-loop lattice PT computation of
> the C_2-dependent threshold — an open computational task — would upgrade
> both entries to strict first-principles predictions.**

**Proposed:**

> [...] The SU(2) and SU(3) rows, as originally presented, were retrodictions.
> The product A·B (the leading coefficient) is now computed from 2-loop
> lattice PT in the induced gauge theory (§6.2.1, A·B = 48 ± 15%),
> agreeing with the fit at the ~4% level at central value and consistent
> within extrapolation uncertainty. This upgrades SU(2) and SU(3) from
> retrodictions to first-principles predictions at ~15% precision.
> Tightening to sub-10% precision, and separating A from B, remain open.

### Change 4: Add a new subsection §6.2.1 documenting the derivation

**Insert after §6.2 (and before §6.3):**

```
### 6.2.1 First-principles derivation of A·B

The leading coefficient A·B in the C_2-dependent threshold is extracted
from the 1-loop gauge self-energy Σ_{μν}(p) in the induced gauge theory.
Using the induced propagator D_ind(k) = 1/(k²_lat · Π_s) and the
Wilson-plaquette 3-gluon vertex (the leading continuum-limit piece of
the full induced Γ_3), the bubble diagram combined with the Faddeev-Popov
ghost loop gives a transverse self-energy

    Σ_T(p) = (p² δ_{μν} − p_μ p_ν) · Π_T(p²)

We extract Π_T(p²) at small p via Π_T(p²) = (Σ^{11}(p) − Σ^{00}(p))/p̂² for
p along the 0-direction, then extrapolate p²→0 and N→∞ via Shanks
acceleration.

On N⁴ lattices up to N=28 at fermion mass m=0.05:

    Π_T(p²=0) · Π_s²  →  −0.079  as  N → ∞

The conversion to the coupling correction uses

    δ(1/α) = 4π · |Π_T| / b_0_capture

where b_0_capture is the fraction of the textbook 1-loop β-function
coefficient b_0 = 11/3 reproduced by the finite-lattice calculation.
Calibrated from a standard-QCD cross-check (D = 1/k̂², no Π_s), the
N→∞ asymptotic capture is 0.40 ± 0.05 at m = 0.05.

Stripping the Π_s² factor and applying:

    |Π_T|/C_2    = 0.079 / (0.308)² = 0.833
    δ(1/α)/C_2  = 4π · 0.833 / 0.40 = 26.1
    A·B         = 26.1 / g_0²  =  26.1 / (1/(6·Π_s))  =  26.1 · 6 · 0.308 = 48.3

against the fitted value A·B = 46.4. Agreement at central value is ~4%.

**Uncertainty budget (~15% combined):**
- Π_T N→∞ extrapolation (Shanks vs linear 1/N²): ±10-15%
- b_0 capture N→∞ extrapolation: ±10%
- Subleading contributions (F³ from c_F3 ≈ −0.034; lattice V_4g
  corrections to tadpole's p²-coefficient): estimated ±10%
- Convention / gauge-fixing prescription ambiguity in induced theory: ±5%

**Methodological caveats:**
(i) The Wilson-plaquette 3-gluon vertex is the leading piece of the
full induced Γ_3. The full induced vertex is transverse by Ward identity
(verified); the Wilson-plaquette piece alone is not, but standard FP
ghosts restore transversality at leading order.
(ii) The tadpole with continuum V_4g contributes to the gauge-violating
mass but not to the transverse Π_T. Lattice V_4g cos-factor corrections
would contribute a p²-dependent piece — estimated at the ~10% level and
currently included only via their effect on the b_0 capture.
(iii) The OI framework has no formal gauge-fixing (the gauge field is
induced from the matter field via S_eff = −N_f · Tr ln(D†D)), but the
induced propagator being a scalar in color and Lorentz is consistent with
effective Feynman gauge, which is what the ghost prescription assumes.

**Reproducibility.** The full calculation runs in ~20 min on a single CPU.
See `oi_lattice_code/AB_derivation/` for the complete implementation, with
`reproduce_AB.py` as the end-to-end driver.

**Open work toward higher precision.** Tightening to sub-10% precision
requires: (a) extending the lattice size to N=32 and beyond; (b) deriving
and including the full Wilson-action lattice 4-gluon vertex; (c) including
the F³ subleading piece of the induced Γ_3 via its Wilson coefficient
c_F3 = −0.034 ± 0.001 (independently extracted); (d) a second-order
calculation (coefficient of (C_2·g_0²)²) to separate A from B.
```

### Change 5: Update §6.3 table header notes

**Current header context:**
"...$(A, B) = (8.3, 5.59)$ (matched to the observed SU(2) and SU(3)
couplings at $M_Z$)."

**Proposed clarification:**
"...$(A, B) = (8.3, 5.59)$ with product $A \cdot B = 46.4$ (matched to the
observed SU(2) and SU(3) couplings at $M_Z$, and independently computed from
first principles at $A \cdot B = 48 \pm 15\%$; see §6.2.1)."

### Change 6 (optional): Update abstract / conclusions

If the paper has an abstract or conclusion section claiming parameter counts
or listing fitted parameters, update to reflect that A·B is now **derived
(at preliminary precision)** rather than fitted. Specifically, the parameter
count in §6.3 says "one structurally computed input ... and three fitted
parameters of the threshold function." This could become:

> "one structurally computed input (1/α_0), one fitted parameter (δ_0, with
> independent 2-loop computation as consistency check), and one derived
> product (A·B, at ~15% precision) — with A and B still to be separated."

---

## What NOT to change

- Don't remove the existing caveats about the log-resum form being a
  "constrained parameterization not derived."
- Don't claim A and B are individually determined. Only their product is.
- Don't remove §6.6's acknowledgment that SU(2) and SU(3) rows were
  retrodictions historically — add that they are NOW preliminary
  first-principles predictions.
- Don't drop the "open computational task" phrasing entirely — just
  specify what's now *done* (A·B product at 15%) vs still *open*
  (separating A, B; tightening precision).

---

## Recommended next actions for the paper author

1. **Review this proposal.** The result has real uncertainties; overstating
   would be counter-productive.

2. **Independent reproduction.** `reproduce_AB.py` should be run
   independently. Output should give A·B in the 42-52 range.

3. **Verify the text-vs-code Π_s convention issue** (see
   `PI_S_CONVENTION_NOTE.md`). Either the paper's `two_loop_vp.py` Pi_1
   needs updating to the text's two-term formula, or the text needs
   clarification to describe what the code computes.

4. **Consider keeping (A, B) fitted in §6.3 table** while adding A·B
   as a derived consistency check in §6.2.1 — this is honest given the
   15% uncertainty, and avoids having to update the table's precise values.
