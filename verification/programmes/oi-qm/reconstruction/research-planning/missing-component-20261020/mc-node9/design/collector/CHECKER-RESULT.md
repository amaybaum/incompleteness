# C-SPH-1 complete-record checker: result

> **Status.** The run executes `CHECKER-PREREG.md`, frozen at `27cbc2d7` (`FREEZE.md`).
> - **Files.** The checker is `record_checker.py`. Its outputs are `record_checker.out`, `record_checker_cells.csv`
>   (one bracket per case) and `record_checker_d1.csv` (one D1 bracket per preparation and protocol).
> - **Run.** Single run of 2207 s on 4 cores. A replay in a separate copy matches byte for byte (see the end).
> - **What it is.** Verification of the implemented model against the frozen allowance, not a certification by
>   review.

## Verdict

**ACCEPT on P\*.**
- **Pool allocation.** All 2,664 cases have hi ≤ 0.01. No case has lo > 0.01, and none is UNDECIDED.
- **Total.** Adding the analytic aperture bound (≤ 0.01) gives a pairwise transcript distance of at most 0.02.
- **Controls.** All are green.

| Family | Cases | Largest hi | Where | Its lo | Cases exactly 0 |
|---|---|---|---|---|---|
| F1 | 2,040 | 8.47·10⁻⁶ | XXX\|R, relation 1 | 4.34·10⁻⁷ | 596 |
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
  - a target relative gap of 1%;
  - 40-digit interval arithmetic.

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

**CSV writer.** The first run wrote the case files without quoting, which split F2 protocol names such as
`X+,X+`. The checker now writes with the csv module. The two files from that run were rewritten by re-splitting
each line from the right, which changes no value. The replay of the fixed checker reproduces them byte for byte.

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

The checker was replayed in a separate copy of `collector/` and `instrument/` (2199 s).
- `record_checker_cells.csv` and `record_checker_d1.csv` are byte-identical to this run's.
- The printed output is identical except for the two wall-clock lines ("integrals done at …" and "elapsed …").
