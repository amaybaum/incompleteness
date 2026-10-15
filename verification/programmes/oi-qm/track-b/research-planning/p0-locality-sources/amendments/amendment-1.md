# P0 locality sources — amendment 1: records as registered values (HI-rec)

Committed after one development run and before any recorded run. It adds one cell and does not change the existing
cells, configurations, controls or tokens.

## Why

The development run used script sha256 `01d3581f…` and gave output sha256 `556c4a01…`. It passed every control and
printed `LS-SPLIT`. Since that outcome favours the framework, the reading got a skeptical pass (§A.31) before any run was
recorded. The pass found that `RULES.md` models Lemma 3's "maximal entropy compatible with the observer's records"
(Main.md:62; posit (iv), Main.md:708) only with orbit-level records (E-reg, W5).

An observer's records are registered values at a tick, not orbit labels. For a record `R = {v₁ = a, v₂ = b}` at tick 0:
- the invariant laws compatible with it are those supported on the joint orbits that meet `R`;
- the maximal-entropy one is the uniform law `μ_R` on their union `U(R)`.

Under product dynamics, `U(R)` need not be a product set, because the two regions must meet their records at the same
tick. So `μ_R` can be correlated across an uncoupled cut. The law that predicts forward from the record is
`μ_R(· | R)`, and that law is uniform on the rectangle `R` [W]. The cell tests which of the two the conclusion depends
on.

## The added cell

| cell | positive token | rule |
| --- | --- | --- |
| HI-rec | `LS-HI-REC` | On `U-free(3)`, `U-free(5)` and every `U-edge(3, α, β)`, take every record `(a, b)` of the two regions' visible values at tick 0 with a nonempty record set. The record-conditioned law `μ_R(· ∣ R)` gives product joint visible laws at `t = 0..8` and product one-step kernels at `t = 0..7`, and conditioning on region 2's visible value never changes region 1's visible law |

Supplementary, deciding nothing: the number of records whose unconditioned `μ_R` is not a product on `Conf`.

The reading's conjunction becomes `LS-INS-ALL-PRIORS ∧ LS-HI-DEFAULT ∧ LS-HI-REC ∧ LS-HI-ORBIT-FAILS ∧
LS-HI-PRIOR-FAILS`. It prints `LS-SPLIT` with the sentence of `RULES.md` §6, and the sentence's second clause reads:

> Hidden-sector independence follows from the counting measure, or from Lemma 3's maximal-entropy selection conditioned
> on regional records.

The development run's tokens are not used.
