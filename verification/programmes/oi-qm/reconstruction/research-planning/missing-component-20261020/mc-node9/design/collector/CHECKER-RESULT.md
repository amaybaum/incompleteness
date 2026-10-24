# C-SPH-1 complete-record checker: result

> **Status.** The run executes `CHECKER-PREREG.md`, frozen at `27cbc2d7` (`FREEZE.md`).
> - **Files.** The checker is `record_checker.py`. Its outputs are `record_checker.out`, `record_checker_cells.csv`
>   (one bracket per case) and `record_checker_d1.csv` (one D1 bracket per preparation and protocol).
> - **What it is.** Verification of the implemented model against the frozen allowance, not a certification by
>   review.
> - **Which run.** The results below are from run 2, the corrective run (2391 s on 4 cores), replayed byte for byte.
>   Run 1 is kept on record (see Runs).

## Runs

**Run 1, at `9ceadbca`.** It is retained in the branch history, and it deviated from the freeze in one respect:
- **Precision.** It used 40-digit arithmetic. The preregistration fixes 50 (§5).

Owner review then found three certification defects in it:
- **Box antiderivative sign.** The helper returned the box integral with sign (−1)^d, for example −0.115 for
  ∫₀^(23/200) 1 du. Within a box every term has the same dimension, so the following absolute value cancelled the
  sign, and the brackets were unaffected.
- **D1 accumulation.** The D1 upper bound was accumulated with nearest rounding.
- **CSV export.** Endpoints were rounded to nearest, so a stored upper endpoint could fall below the computed one.

Run 1's verdict, controls and maxima agree with run 2 at the printed precision.

**Run 2, the corrective run, under the unchanged freeze.** It fixes all four points:
- 50-digit arithmetic;
- correct corner signs in the box antiderivative (new check I3: a positive volume, and agreement with quadrature
  in 1, 2 and 3 dimensions, for the fixed pool and the reference);
- interval accumulation in D1;
- outward export: lo rounded down and hi rounded up to 8 significant digits, with the enclosure checked exactly for
  every row.

It also encloses C6's √2 values exactly, rather than through a decimal string.

## Verdict

**ACCEPT on P\*.**
- **Pool allocation.** All 2,664 cases have hi ≤ 0.01. No case has lo > 0.01, and none is UNDECIDED.
- **Total.** Adding the analytic aperture bound (≤ 0.01) gives a pairwise transcript distance of at most 0.02.
- **Controls.** All are green.

| Family | Cases | Largest hi | Where | Its lo | Cases exactly 0 |
|---|---|---|---|---|---|
| F1 | 2,040 | 8.47·10⁻⁶ | YYY\|R, relation 1 (equal at printed precision to its mirror XXX\|R) | 4.34·10⁻⁷ | 596 |
| F2 | 432 | 1.41·10⁻⁶ | probes R+, R+, relation 6 | 2.98·10⁻⁷ | 172 |
| F3 | 192 | 2.83·10⁻⁷ | Y > R+, relation 6 | 2.04·10⁻⁷ | 112 |

**What the zero cases are.** A case is exactly 0 when no visible station of the record lies in the hidden support
with a nonzero coefficient. The two record laws are then identical.

**Bracket width (hi/lo) on the nonzero cases.**

| Family | Median | 90th percentile | Maximum |
|---|---|---|---|
| F1 | 4.4 | 16.1 | 20.4 |
| F2 | 1.38 | 5.1 | 5.1 |
| F3 | 1.38 | 1.38 | 1.38 |

The wide brackets come from integrals of three and four offsets that reach the per-integral cap. They do not affect
the verdict, which needs only hi ≤ 0.01.

## Controls (all green)

| Control | Result |
|---|---|
| I3 | box antiderivatives: ∫₀^(23/200) 1 du = 0.115; the fixed-pool and reference box integrals agree with quadrature in 1–3 dimensions |
| C1 | read-law derivation: the hemisphere integrals hold symbolically; a grid quadrature agrees to 2.1·10⁻⁴ (numerical evidence) |
| C2 | closed form = particle-level enumeration, symbolic over call times, windows, offsets and q: 56 cases (N ≤ 4, 14 patterns). The merge identity behind log R also holds |
| C3 | relation 5 (identical procedures) has hi = 0 on every protocol |
| C4 | log R_ref = 0 identically (symbolic), and hi ≤ 10⁻³⁰ on every pair and protocol |
| C5 | the herald-history regression through the checker's merge rule gives 151201/16777216 for the fixed pool, and 0 for the Poisson reference |
| C6 | impact-read control: P(E \| Z-mix) = 1/√2 and P(E \| X-mix) = 1 − 1/√2, integrated from the flux law; F3 with a = Z gives lo ≥ 0.3935 > 0.02 for all 8 probes |
| C8 | address exposure: the supports are disjoint and every record mass contains 1, so TV = 1 exactly on all 8 single-probe F2 protocols |

**Implementation checks.**
- **Cancellation identity.** Σ_w d_w r_w = 0 holds exactly on every branch.
- **Record masses.** For every preparation and protocol, the interval of total record mass contains 1, so the branch
  enumeration is complete.

## Diagnostic D1 and completion

- **D1 (reported, not a gate).**
  - The largest hi(TV(fixed pool, Poisson reference)) over the 7 preparation procedures and 444 protocols is
    1.06·10⁻⁶. The largest lower bracket is 7.0·10⁻⁷.
  - The coupling bound mΛ²/N = 4.94·10⁻³ is about 4,600 times larger. It holds, and on P\* it is very conservative.
- **Completion probability.**
  - F1: between 0.9999846 and 1.
  - F2 and F3: always complete.
  - The fixed-pool and Poisson ranges agree at the printed precision.

## Work limits

| Measure | Used | Frozen limit |
|---|---|---|
| Box evaluations, largest single case | 143,663 | 10⁶ |
| Box evaluations, whole run | 1,669,352 | 5·10⁸ |

- **What the run total covers.** The 7,703 distinct fixed-pool integrals. The reference integrals vanish
  identically.
- **Choices made within the limits:**
  - a cap of 400 evaluations per integral;
  - a target relative gap of 1%.
- **Precision.** Interval arithmetic at 50 digits, as frozen.

## Implementation choices within the frozen specification

**Integration method.** The frozen method is interval arithmetic plus adaptive box bisection, with monotone bounds.
- **Variables.** Bisection runs over the individual herald offsets.
- **Sign-certified boxes.** On a box where the sign of Σ_w d_w r_w (R_w − 1) is certified, the box integral is
  computed exactly in closed form. Each term is a product of iterated antiderivatives, evaluated in interval
  arithmetic. The closed form agrees with plain quadrature to 16 digits on a test box.
- **Other boxes** contribute [|∫ g|, max|g|·volume]. The maximum comes from monotone pieces of each station
  density and of log R. For log R this is
  log κ − h₂ log(1 − qS₁) − h₁ log(1 − qS₂) + (N − h₁ − h₂) log(1 − ε).
- **Lower bound.** Each branch also contributes the exact |∫ (p₁ − p₂)|, from closed-form pattern probabilities.
  The larger of the two lower values is kept.

**Order of operations.** Hidden station choices are marginalized before the absolute value is taken (§5).

**D1's upper bound.** It telescopes over stations:
∫|ΠA − ΠB| ≤ Σ_s Π_{t<s} ∫A_t · ∫|A_s − B_s| · Π_{t>s} ∫B_t, on disjoint variables. Each ∫|A_s − B_s| is a
one-dimensional certified integral.

**CSV writer.**
- **Quoting.** The checker writes with the csv module, so F2 protocol names such as `X+,X+` are quoted.
- **Outward rounding.** Each endpoint is rounded outward from the computed binary value to 8 significant digits.
- **Exactness of the check.** The enclosure check compares exact rationals.

## What this establishes, and the stop point

**Established.** The implemented finite-pool model meets the frozen allowance on P\*, with:
- the frozen schedule;
- continuous timestamps;
- exact station history;
- the analytic read law.

The measured distances are 10⁻⁷ to 10⁻⁵, three to four orders of magnitude below the allocation. This is
consistent with Theorem C, which covers every admissible protocol analytically.

**Not established:**
- a finite microscopic realization;
- exact equivalence;
- any OI derivation of isotropy, independent pools, routing or the access restrictions;
- composites.

**Stop point.** Per the owner's rule, numerical refinement of C-SPH-1 stops here. The next question is which of its
essential assumptions OI actually supplies.

## Replay

Run 2 was replayed in a separate copy of `collector/` and `instrument/`.
- `record_checker_cells.csv` and `record_checker_d1.csv` are byte-identical.
- The printed output is identical except for its two wall-clock lines.

## Owner acceptance

> I accept the repair at a7b9674a for the bounded numerical checkpoint. […] The checkpoint can now close with its
> stated scope: bounded approximate equivalence for the specified apparatus and protocols, conditional on its
> resource and access assumptions. Numerical refinement should stop here.

Owner, 2026-10-22, relayed in the coordinating session. **The numerical checkpoint for C-SPH-1 is closed.**
