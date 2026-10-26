# NP-AVG-1 Stage 0, Layer 2: a proposal for the launch margin κ (advisory)

**Status: a proposal for the owner. It sets nothing.** κ stays an `OWNER-PLACEHOLDER` in `l2config`,
with no default anywhere in code or configuration, and the v8 profile is refused while it is open
(`LAYER2-PLAN.md` §3.5, §4.2). The owner's answer on κ and S7 so far is "Decide later" (erratum E1
§9). Nothing here ran on v8's configuration class: v8 enters only through the dry run's
combinatorics (counts and the context-size histogram; no context, no closure, no shared-tip or F_G
count).

**The question.** The owner asked for "the proposed κ value and its statistical and computational
justification". The launch rule (`LAYER2-PLAN.md` §3.5; review `LAYER2-REVIEW.md` §6) is:

> launch iff κ · (total estimate) ≤ S7's budget, and κ · (each job's estimate) ≤ that job's timeout,

with S7's budget 24 runner-hours (86,400 runner-seconds) over at most 32 shards, and a 40-minute shard
job timeout (2,400 s). κ is a resource margin for the error of the estimate, fixed with its basis
before the complete estimate is computed.

**Sources.** All numbers below are read from `design/kappa/calibration-repeats.json` (step
`kappa_calibration_repeats` of `design/RUN-MANIFEST.json`; timing data, not deterministic) and
`design/runs/dryrun_v8_estimate.out`. They were measured on one machine (Python 3.13.16), not on a
CI runner.

## (a) The cost model

Every term is in runner-seconds and includes the `-O` copy (factor 2), as `l2plan.estimate` computes
it (`LAYER2-PLAN.md` §3.6; each term's formula is printed in `dryrun.json` under `cost.formulas`).
t_c(m) and r_c(m) are the calibrated production-closure and full-reference times at m non-fixed
quantities; m̄ = 16 is the mean v8 context size and m_max = 29 the largest (combinatorics).

| term | formula | v8 value (median of 10 calibrations) |
| --- | --- | --- |
| closures | 2 · overhead · Σ_m count(m) · (orbits/N) · 2 [t_A(m) + t_G(m)], overhead = 2 (an unmeasured allowance) | 58,836 |
| sampled gates | 2 · [(1/1,000) · 3 · orbits · (r_A + r_G)(m̄) + (1/100) · orbits · 8 · 2 (t_A + t_G)(m̄)] | 2,504 |
| survivor gates (cap 10 orbits per shard) | 2 · 10 · 32 · 8 · [2 (t_A + t_G) + 4 (r_A + r_G)](m_max); includes C7 on set 1 | 8,069 |
| S1a | 2 · [bound closures + 3 streamed reference passes per bound + per-line closures] | 558 |
| pre-flight, merge | stated allowances, 300 + 2 · 300 | 900 |
| C7, set 4 (H₁₀₀₀) | (N / 1,000) · (c7_A + c7_G) | 1,990 (expected sample size 5,163.2) |
| **known terms** | sum of the above | **72,977 (20.3 h)** |
| C7, set 2 under G | \|F_G\| · c7_G | **unknown** |
| C7, set 3 (I_c ∩ H₁₀₀) | (\|I_A\| / 100) · c7_A + (\|I_G\| / 100) · c7_G | **unknown** |

c7_c = 2 · [t_c(m) + r_c(m)] per record: a direct production closure and a full `s0ref` reference
closure. Median over the 10 calibrations: c7_A = 0.072 s and c7_G = 0.3135 s at the record-weighted
mean context size; 0.157 s and 0.642 s at m_max.

**The unknown inputs.** They need the record space of v8 enumerated, which is not authorized; the
v8 dry run reports each as "not computed (requires authorization)".

| input | what it is | admissible range | the toy class (no information about v8) | how it would be measured |
| --- | --- | --- | --- | --- |
| \|F_G\| | records whose in-frame quantities have a shared near tip | 0 ≤ \|F_G\| ≤ \|I_G\| ≤ N = 5,163,225 | 595 of 1,400 (42.5 %) | `l2plan.c7_populations` (combinatorial, no closure) under an authorization: records and orbits |
| \|I_A\|, \|I_G\| | records whose initial context has a shared near tip under A, G | 0 to N | 1,071 (76.5 %), 667 (47.6 %) | the same enumeration |
| \|Surv_A\|, \|Surv_G\| | survivor records | bounded in a complete run by the cap: at most 10 · 32 · 8 = 2,560 per convention, inside the survivor-gate term | 0 | the run itself; beyond the cap the run is INCOMPLETE |

Structural facts bound where F_G can lie but not its size: two quantities share an e-tip only if
their sites lie on a line parallel to e, so a tie in Q⁰(R) needs two items on a common axis line, or
an item on the port's axis line (the z-axis), with compatible slices; two samples of one item never
share a tip. On the toy class the region lies entirely inside the frame, which favours in-frame ties;
on v8 a sample is in the frame only while |x| + s ≤ 8, so the v8 fraction could be much smaller. No
number is proposed for it.

## (b) The calibration data and the spread

`l2calib.py` was run 10 times in fresh processes, 5 normally and 5 under `-O` (planted quantity sets
of 8 to 40 quantities, 12 sets per size), and the v8 estimate was rebuilt from each calibration.

| quantity | median | CV | max / median | min / median |
| --- | --- | --- | --- | --- |
| known terms of the v8 estimate (10 calibrations) | 72,977 s | 5.8 % | 1.161 | 0.962 |
| closures term | 58,836 s | 6.6 % | 1.182 | 0.963 |
| C7 coefficient for F_G (c7_G) | 0.3135 s | 5.5 % | 1.142 | 0.967 |

Per calibrated size (normal runs only), the CV of a single table entry has a median of 6–11 % and a
maximum of 16–23 %, and max/median reaches 1.45–1.58. The estimate is a sum over sizes, so its spread
is smaller than that of a single entry.

**The sources of the spread.**
- **Runner variance (one machine).** The repeat-to-repeat spread above: CV 5.8 % on the known terms.
  Variance *between* CI runners is not measured: every repeat ran on one machine.
- **Cache.** On every toy record, timed in three passes in one process, pass 1 is 1.04–1.06 times the
  mean of passes 2 and 3 (the in-process eligibility memo and explicit cones); passes 2 and 3 differ
  by 0.8–3.5 %. Each shard job is one process, so this effect is a few per cent at most.
- **`-O` duplication.** The `-O` copy is not faster: the paired `-O`/normal ratio over 180 table
  entries has median 0.994 (CV 16 %, per-entry noise). The `-O` run is therefore a full duplicate,
  a deterministic factor 2 that the estimate already contains; it is not part of κ. Running the two
  copies as separate replica jobs halves each job's time and leaves the total unchanged.
- **Model error, planted sets to real records.** Not measurable without timing real v8 records. On
  the toy class, the measured time of every record's closures against the calibration's prediction
  at its context size is 0.93 (A closures), 0.12 (G closures), 0.06 (A reference) and 0.017 (G
  reference). Toy contexts have at most 8 quantities, below or at the smallest calibrated size, and
  most of their quantities are in the frame, so their G tips are rarely eligible. The direction
  (the planted calibration over-predicts) is suggestive for the G terms but does not transfer to v8.
- **Unmeasured allowances inside the estimate.** The overhead factor 2 on the closures term and the
  pre-flight and merge allowances are stated, not measured.

## (c) A proposed κ, and how the launch inequality plays out

**Proposal: κ = 1.5**, as the product of a measured factor and a stated one:
- **u_cal = 1.2** for calibration spread. Over 10 calibrations the known terms' max/median is 1.161;
  a normal approximation with CV 5.8 % gives 1 + 2.326 · 0.058 = 1.13 at the 99th percentile. 1.2 is
  the empirical maximum rounded up. With n = 10 repeats, the maximum exceeds one further draw with
  probability about n/(n + 1) ≈ 0.91; the rounding adds margin beyond that.
- **u_model = 1.25** for what is not measured: CI-runner heterogeneity and the planted-to-record model
  error. This factor is a judgement, not a statistic. It should be replaced by measurements (§d,
  steps 2 and 5) before launch, and κ recomputed by the same rule: κ = u_cal × u_model, each the
  upper value of its measured ratio, rounded up to one decimal.

κ is a margin on the error of the estimate, not on the size of the workload, so it can be fixed
before |F_G| is known. Fixing it first keeps it from being fitted to the estimate (the review's
condition, `LAYER2-REVIEW.md` §6 item 2).

**The launch inequality under S7's current budget.** With κ = 1.5 the total must be at most
86,400 / 1.5 = 57,600 s. The known terms alone are 72,977 s (median), so **no launch is admitted for
any value of |F_G|, |I_A| or |I_G|, including zero**. The largest κ the current budget admits, with
every unknown input at zero, is 86,400 / 72,977 = 1.18 (median calibration) or 1.02 (the slowest of
the 10 calibrations). The table gives the median estimate for a range of input fractions
f_F = |F_G| / N and (f_IA, f_IG) = (|I_A|, |I_G|) / N; the middle row of each group uses the toy
class's I fractions only as an illustration.

| f_F | (f_IA, f_IG) | C7 beyond set 4 (s) | total (s, h) | largest κ the 24 h budget admits | shard job (s): one job / two replicas | budget needed at κ = 1.5 (h) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | (0, 0) | 0 | 72,977 (20.3) | 1.18 | 2,235 / 1,117 | 30.4 |
| 0 | (0.765, 0.476) | 10,549 | 83,526 (23.2) | 1.03 | 2,564 / 1,282 | 34.8 |
| 0 | (1, 1) | 19,904 | 92,881 (25.8) | 0.93 | 2,857 / 1,428 | 38.7 |
| 0.001 | (0.765, 0.476) | 12,167 | 85,144 (23.7) | 1.01 | 2,615 / 1,308 | 35.5 |
| 0.01 | (0, 0) | 16,187 | 89,164 (24.8) | 0.97 | 2,741 / 1,370 | 37.2 |
| 0.01 | (0.765, 0.476) | 26,735 | 99,712 (27.7) | 0.87 | 3,070 / 1,535 | 41.5 |
| 0.05 | (0.765, 0.476) | 91,482 | 164,459 (45.7) | 0.53 | 5,094 / 2,547 | 68.5 |
| 0.10 | (0.765, 0.476) | 172,416 | 245,393 (68.2) | 0.35 | 7,623 / 3,811 | 102.2 |
| 0.425 (the toy fraction) | (0.765, 0.476) | 698,484 | 771,461 (214.3) | 0.11 | 24,062 / 12,031 | 321.4 |
| 1 (trivial bound) | (1, 1) | about 1.64 million at the mean size; about 3.36 million at m_max | — | — | — | — |

**The job inequality.** A shard job's timeout is 2,400 s. Run as one job holding both copies, the
shard job is 2,235 s with every unknown at zero, so it admits κ ≤ 1.07 only. As two replica jobs
(normal and `-O`), it is 1,117 s, and κ = 1.5 admits a C7 term of up to 64 · 1,600 − 71,513 ≈
30,900 s, about |F_G| ≤ 98,500 records (1.9 % of N) with |I_c| = 0.

**What follows for the owner's decisions.**
- Under S7's 24 runner-hours, the enumeration cannot launch with any κ above about 1.0–1.2, whatever
  |F_G| turns out to be; at κ = 1.5 it needs a budget of at least 30.4 runner-hours plus 1.5 times
  the C7 term. S7's budget is a resource decision of its own, recorded with its reason.
- The shard jobs should run as normal and `-O` replicas (the review's §6 item 3).
- |F_G| decides whether C7's set 2 is affordable. Above about 5 % of N, the full-reference cost of
  set 2 dominates every other term; the Lemma G-D reference form (owner decision G_D) was measured
  at about ten times cheaper per toy record (`E1-ANALYSIS.md` §A3), and the toy proxy above suggests
  that the full G reference on in-frame-heavy records may cost far less than the planted
  calibration predicts. Neither is measured on v8.

## (d) What is not known until an authorized count, and a recommended sequence

**Not known.** |F_G| (records and orbits), |I_A| and |I_G|, hence the C7 term, the total, the shard
job's estimate and the launch decision; the planted-to-record model error on v8 contexts; CI-runner
heterogeneity. |E_G| (owner decision O1) is not known either.

**Recommended sequence**, each step a separate owner decision:
1. **Fix κ now, on calibration grounds only**, before any v8 count exists: κ = 1.5 as proposed, or the
   rule κ = 1.2 × u_model with u_model measured in steps 2 and 5. E1 §9 takes the G-D confirmation
   "together with κ once the dry run reports |F_G|"; the review asks that κ be fixed before the
   corrected estimate. Fixing κ first and G-D after the count satisfies both.
2. **Optionally, measure runner heterogeneity**: an owner-approved CI dispatch of `l2calib.py`
   repeats on the runner class (planted sets only; nothing on v8).
3. **Authorize a combinatorial-only v8 count** of I_A, I_G, F_G and E_G (records and orbits): no
   context, no closure, no grant for the engine. This revision refuses it
   (`l2plan --shared-tips` is refused on v8, PO-L2-23), so it needs a Layer-2 amendment adding a
   grant-gated path for exactly this count, with its own review. Its cost, extrapolated from the toy
   enumeration (about 0.3 ms per record at toy context sizes) and not measured on v8, is of the order
   of one to two single-core hours over 5,163,225 records; it shards like the enumeration.
4. **With |F_G| known**, decide G_D (a cost decision: it does not change any verdict, E1 §9) and O1.
5. **Optionally, measure the model error** with an authorized timing sample of real v8 closures (a v8
   computation, separately authorized), and replace u_model.
6. **Decide S7's budget** as a resource decision, recorded with its reason, then compute the complete
   estimate. Launch iff κ · total ≤ budget and κ · each job ≤ its timeout; otherwise the enumeration is
   reported as not undertaken for cost.

**Reproduce.** `python3 -I -B design/kappa_calibration.py code design/kappa/calibration-repeats.json`
from `stage0/layer2/` (about 2.5 minutes); the tables above are medians over its
`v8_estimate_spread.per_calibration` entries. Timing output varies between runs and machines.
