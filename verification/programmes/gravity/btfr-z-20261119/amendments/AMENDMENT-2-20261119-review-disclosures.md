# BTFR-z amendment 2 (2026-11-19): disclosures and sensitivity analyses added at review

**Status of this amendment.** `PREREG.md` (commit `7b51814046c351b0060eb9413dc4d985f08b91b1`) is
frozen and is not edited. This amendment answers the non-author review of `9b1d609f` (#1429 comment
7025329707, REVISE). It was written after the result was known and changes no existing number, rule,
prediction, budget or verdict label. The analyses below are added to `scripts/btfr_z.py`, which
writes them into `results.json` (key `sensitivity_review`, `U2_rule`, and the full-σ power fields of
`controls.C3.const`) and into `RESULT.md`. None of them is preregistered, and none enters a verdict.
The `robustness_gas` key of `9b1d609f` is replaced by `sensitivity_review.margins`, whose z = 2
column reproduces its z~2.3 values; its z~0.9 alternative (+0.55 and +0.36 dex) is not carried over.

## F1. The departure from the planning statistic

- **What the planning rule said.** The G3-SCOPE planning map (#873 comment 7022640763, posted
  2026-11-19T21:25Z, before PREREG) proposed for U2: "fit the zero-point offset at fixed v_flat,
  slope 4; prediction log[H₀/H(z)], null 0". That is an anchored offset, a T1-type statistic.
- **What PREREG did instead.** PREREG §5 made T2 = b(z~2.3) − b(z~0.9) the headline. PREREG §0
  discloses that the published zero-points were known when T2 was chosen. It does **not** disclose
  that this choice departed from the planning statistic. This amendment records that departure.
- **The outcome under the planning statistic** (slope 4, anchored to SPARC, scored with the T1 σ_O
  and the PREREG §7 thresholds; values in `RESULT.md`):
  - OI-asym is consistent in both bins (z = 1.86 at z~0.9, 0.91 at z~2.3).
  - Constant-a₀ MOND is excluded at z~0.9 (z = 3.19) and consistent at z~2.3.

  The choice of statistic therefore decides which model is disfavoured. `RESULT.md` reports this
  outcome in its own summary paragraph directly beside the T2 summary, and in a table under the
  verdict list.
- **Why T2 stays the headline.** T2's justification is structural and independent of the outcome.
  It is the only statistic in which the anchor-common systematics cancel, including the mismatch
  between V_f at z = 0 and v_circ,max at high z (σ_vdef = 0.073 and 0.075 dex in the two bins).
- **The identity.** T2 ≡ T1(z~2.3) − T1(z~0.9) identically, since both use the same anchor and slope.
  OI's two T1 residuals (−0.234 and +0.262 dex) have opposite signs. T1 being "consistent" reflects
  anchor-common terms that cancel in T2, and is not evidence against T2. `RESULT.md` now states this.
  It replaces the earlier line, which presented differing T1 and T2 verdicts as though they stood in
  opposition.

## F2. Sensitivity to the gas and SED allowances

The preregistered T2 gas term allows 0.10 dex of differential error in the z~2.3 scaling-relation
gas masses. `RESULT.md` now reports three things.

- **Margins to both thresholds.** The forward-model exclusion clears z = 3 by 0.034 dex in T2. That
  is a coherent −0.06 dex change in the z~2.3 gas masses. Reaching z = 2 would take 0.151 dex in T2,
  or −0.34 dex in gas; that figure is kept in the table but no longer stands alone. The asymptotic exclusion clears z = 3 by
  0.146 dex in T2, or −0.32 dex in gas.
- **z-scores under alternative allowances:**

  | Allowance | OI forward model | OI asymptotic |
  |---|---|---|
  | 0.15 dex differential gas (PREREG's own per-bin T1 value) | 2.92 | 3.77 |
  | 0.15 dex per bin, independent | 2.74 | 3.54 |
  | 0.20 dex differential gas | 2.56 | 3.31 |
  | 0.15 dex gas + 0.10 dex epoch-dependent SED | 2.73 | 3.53 |

- **Stellar-mass-only cross-check, with no gas recipe.** Stellar T2 = +0.019 ± 0.065 (statistical),
  σ = 0.102 with the non-gas terms. Against the baryonic OI predictions this gives z ≥ 2.14 (forward
  model) and z ≥ 3.24 (asymptotic). These are lower bounds because the observed gas fraction rises
  from z~0.9 to z~2.3.

These replace the earlier single "−0.34 dex to reach z = 2" framing. The tension does not depend on
the gas recipe; the forward-model exclusion does.

## F3. Power with the full error budget

PREREG asked for power computed with the statistical σ only (96.2%). That figure overstates the
power of the preregistered test, which uses the full σ_O. With constant a₀ as the truth, statistical
scatter about it, and the full σ_O in the test, the probability of excluding OI-asym is 27% and of
excluding the OI forward model 1% (Gaussian). The 500 C3 mocks, scored the same way, give 30.2% and
0.8%. The mocks inject into the fitted linear model with Gaussian errors at the observed
velocities and redshifts. They do not model the sample selection: the z~0.9 galaxies lie about 1.6×
above the main sequence, while the z~2.3 galaxies lie on it. C3 therefore tests the fitter, not
selection bias.

## The ΛCDM comparison

The ΛCDM row is the naive analytic halo scaling. OI's prediction is forward-modelled for baryon
dominance; the halo scaling's is not, so the comparison is asymmetric. Its "excluded" label does not
test ΛCDM galaxy formation. `RESULT.md` now says so.

## Summary wording

The preregistered verdict labels are unchanged. The summary in `RESULT.md` reads:

> In strong tension with, and excluded under the preregistered error budget by, the KMOS³D T2
> statistic (4.25σ asymptotic / 3.29σ forward-modelled); the forward-model exclusion is marginal to
> the gas-mass allowance, and the evidence rests on one sample with inferred masses throughout. This
> falls short of a robust exclusion.

The review rounded the two z-values to 4.3σ and 3.3σ; `RESULT.md` prints them to two decimals from
`results.json`. A second summary paragraph beside it states the U2-rule outcome (F1).

**Goal link (§A.47).** Unchanged from `PREREG.md`. This amendment corrects how the existing result is
presented.
