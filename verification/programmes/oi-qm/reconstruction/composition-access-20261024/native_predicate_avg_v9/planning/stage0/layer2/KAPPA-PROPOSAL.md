# NP-AVG-1 Stage 0, Layer 2: κ, the reserve, the retry allowance and the launch rule (advisory, r5)

**Status: advisory. It sets nothing.** κ's two components, u_cal and u_model, the reserve and the retry
allowance are `OWNER-PLACEHOLDER` values in `l2config`, with no default anywhere in code or
configuration. The v8 profile is refused while any of them is open (`LAYER2-PLAN.md` §3.5, §4.2).
Nothing here ran on v8's configuration class: v8 enters only through the dry run's combinatorics
(counts and the context-size histogram; no context, no closure, no shared-tip, F_G or site-pair count).

**r5 (LAYER2-R4-REVIEW §3–4; the owner's decisions of 2026-10-26).**
- The ceiling is one **campaign ledger**: κ · (calibration + count pass + primary run + mutant campaign +
  retries + execution overhead) + reserve ≤ 24 runner-hours, every job's measured compute time counted,
  failed jobs and retries included (owner). The per-job fixed overhead, r4's largest reserve item, is now
  a cost term, and a retry allowance is a new placeholder.
- **The affordable κ is stated beside the justified κ, never in place of it** (K3); r4's stale "about
  1.18" is removed.
- **u_cal is preregistered as an upper confidence bound** (CI-3; `ci/CI-CALIBRATION-PROPOSAL.md` §4).
- **The per-job statement is corrected** (K1, B4): §c.
- **Measured and modelled numbers are labelled** (B1–B3): §a.

## The owner's rulings (amaybaum, 2026-10-26)

- **κ:** "Approve the proposed method, κ = u_cal × u_model, but not a final numerical value."
- **Calibration:** "Require at least 20 independent timing calibrations on the relevant CI runner
  class."
- **Model uncertainty:** "Retain as an explicitly judgment-based factor, subject to sensitivity
  analysis."
- **Sequencing:** "Approved. Fix κ, the survivor cap, and budget ceiling before any v8 count." G-D and
  O1 are decided after the count, before the full run.
- **Budget ceiling:** "24 hours maximum, including all run overhead, with an explicit reserve." and
  "If the calibrated runtime exceeds 24 hours, the experiment must be reduced through a new reviewed
  design or declared infeasible under this budget — not run with an artificially smaller margin."
- **Its scope:** "Per complete experimental campaign, not per individual run"; "Include calibration,
  count pass, primary run, mutant campaign, retries, and execution overhead"; "The 24-hour ceiling is an
  aggregate compute-runtime budget across the campaign, not a 24-hour wall-clock deadline. Record all
  measured compute time consistently, including failed jobs and retries."
- **Shard imbalance:** "Do not compensate by lowering κ or simply increasing job timeouts."

**The launch rule as implemented** (`l2plan.kappa_from_rule`, `launch_decision`, `campaign_decision`;
L2-LAUNCH, L2-LEDGER):
- κ = u_cal × u_model, rounded up to one decimal; there is no other source of κ. 1.21 × 1.0 gives 1.3
  (the mutant that rounds to nearest is killed).
- Launch iff κ · (the campaign's six components) + reserve ≤ 86,400 runner-seconds, and κ · each job ≤
  its timeout, every shard compared, so the heaviest decides.
- Otherwise "not undertaken for cost: the experiment must be reduced through a new reviewed design or
  declared infeasible under this budget". κ is never lowered and no timeout is raised to fit; mutants
  that lower κ, drop the reserve, use the mean shard, or drop failed jobs from the ledger are killed.

**Sources.** `design/kappa/calibration-repeats.json` (step `kappa_calibration_repeats`),
`design/overhead/overhead.json`, `design/overhead/survivor-cap.json`, `design/subdivision/bounds.json`,
`design/midsize/validation.json` and `design/runs/dryrun_v8_estimate.out`, in `design/RUN-MANIFEST.json`.
Timing data, measured locally on one machine (Python 3.13.16), not on a CI runner.

## (a) The cost model

Every primary-run term is in runner-seconds and includes the `-O` copy (factor 2), as `l2plan.estimate`
computes it; each term's formula is printed in `dryrun.json` under `cost.formulas`. Medians over the 10
local calibrations of the r5 run.

| term | formula (abridged) | v8 estimate (model; local planted calibration) |
| --- | --- | --- |
| closures | 2 · overhead · Σ_m count(m) · (orbits/N) · 2 [t_A(m) + t_G(m)]; **overhead = 2 is an unmeasured judgement** | 58,957 |
| sampled gates | C11 (i), C17, C18 at 1 in 1,000 orbits; C8 at 1 in 100 orbits | 2,364 |
| S1a | bound closures, three streamed reference passes per bound, per-line closures | 537 |
| pre-flight, merge | stated allowances | 900 |
| C7 set 4 (H₁₀₀₀) | (N / 1,000) · (c7_A + c7_G); c7_A = 0.0715 s and c7_G = 0.303 s per record, **model-weighted from planted timings, not measured on records** | about 2,030 |
| **primary run, known terms** | sum of the above | **64,784 (18.0 h)** |
| survivor gates | cap · 764 s (both copies, all shards; includes C7 on set 1) | 6,112 at cap 8; 12,224 at 16 |
| C7 sets 2 and 3 | \|F_G\| · c7_G + (\|I_A\| / 100) · c7_A + (\|I_G\| / 100) · c7_G | **unknown: v8 count not authorized** |

**The other campaign components** (`budget.campaign`; each with its status in the dry run):

| component | planned value (s) | status |
| --- | --- | --- |
| calibration | 220 per launch (20 × 11 s script time) | modelled from the local script time; its jobs' setup is execution overhead |
| count pass | site-pair count about 1; population count about 3,200 | site-pair count: measured on analogues (≤ 0.01 s); population count: measured on the mid-size analogue (about 115 s for 188,125 records), scaled linearly to v8's 5,163,225 records (an assumption) |
| mutant campaign | 3,872 | modelled: rule mutants 1,980 (r3 local measurement, L1 §10) + 44 machinery mutants × one full self-test (43 s locally) |
| retries | owner placeholder | measured retries replace the allowance as they occur; §d proposes a size |
| execution overhead | not computed | jobs (about 62) × the per-job fixed overhead, measured by the CI calibration (CI-5); §c uses 90 s per job as a judgement |

**The unknown inputs.** |F_G|, |I_A| and |I_G| each lie in [0, N], with N = 5,163,225, and
F_G ⊆ I_G. On the toy class they are 42.5 %, 76.5 % and 47.6 % of N; on the mid-size analogue (ball(2),
not v8) 40.1 %, 41.9 % and 40.1 %. Neither is information about v8; both say that F_G is not small on
any class measured. They become known on v8 only through the population count, whose amendment is
unadopted (`AMENDMENT-PROPOSAL-V8-COUNT.md`).

**The model is not validated.**
- **The toy comparison.** The toy dry run predicts a C7 term of about 200 s and a primary total of about
  2,200–2,450 s; all four toy shards ran in about 9 s. Most of the gap is fixed allowances, the survivor
  bound and contexts below the smallest calibrated size. r4 called this "does not transfer to v8"; that
  was an untested explanation (B3).
- **The mid-size analogue (r5, the review's validation step).** On `mid` (v8's slices, n and gate rates;
  ball(2); contexts up to 27), four real shards of the deterministic subdivision took 7.9, 131.6, 18.5
  and 8.5 s against the model's 60.4, 145.5, 62.3 and 110.8 s (single copy): actual/predicted 0.13, 0.90,
  0.30 and 0.08. The model over-predicts three shards by 3 to 13 × and the heaviest by about 10 %,
  and shows a spread between shards (heaviest/mean 1.34) far smaller than the measured one (3.2 × the
  mean of these four). **It is not validated as a per-shard predictor, nor as a total.**
- **The overhead factor.** Configured at 2. Measured locally (`overhead_measure`, toy geometry): 2.87 as
  a ratio of totals on every toy orbit, 2.89 on 120 planted records. Measured on the mid-size analogue at
  contexts of 12–27 (`midsize_validation`): median 2.24, 90th percentile 3.46 over 24 representatives.
  r4 said "the closures term is under-stated by about 45 %"; that applied a toy-geometry measurement to
  v8 sizes, which was unmeasured (B2). At v8-like sizes the measured median is about 12 % above the
  configured 2.
- **Every conclusion below is therefore "under the cost model".** u_model is the explicit place for
  that error. It is not also absorbed by a second factor: the overhead factor stays at its configured
  value, and the measurements are reported beside it.

## (b) The calibration data and u_cal's statistic

**u_cal, as the review defines it,** is the 99th percentile of the ratio between two independent
calibrations. `kappa_calibration.py` computes it over every ordered pair (90 pairs) of 10 local
calibrations (5 normal, 5 `-O`, each in a fresh process), on the v8 estimate's known terms.

| local run of the 10-calibration procedure | σ of log(known terms) | normal-approximation p99, exp(2.326 · √2 · σ) | empirical p99 (= max/min) |
| --- | --- | --- | --- |
| r3 (the review's re-read) | 0.06 | 1.22 | 1.21 |
| r4, interim | 0.082 | 1.31 | 1.29 |
| r4, final | 0.091 | 1.35 | 1.37 |
| r5 (retained) | 0.059 | 1.22 | 1.19 |

**What the table shows.** Four repeats of the same procedure on the same machine give 1.19 to 1.37. With
n = 10 the statistic moves with one slow calibration. The review's simulation puts the estimator's 5–95 %
range at 1.12–1.31 (σ = 0.06) and 1.18–1.50 (σ = 0.09) at n = 10, and still ±6–9 % at n = 20. Hence the
owner's requirement of at least 20 runner-class calibrations, and the r5 rule:

**u_cal, preregistered** (`ci/CI-CALIBRATION-PROPOSAL.md` §4, implemented in `ci/postrun.py`, fixed
before any CI data): u_cal = exp(2.3263 · √2 · s_U), with s_U the one-sided 95 % upper confidence bound on
the standard deviation of the log v8 known terms across all calibrations, by χ² (Wilson–Hilferty), pooled
over CPU models, rounded up to three decimals. The point estimate and the empirical p99 are reported for
information only. At n = 20, s_U ≈ 1.37 s: s = 0.06 would give u_cal ≈ 1.31, s = 0.09 ≈ 1.50.

**The statistic is conservative for the campaign total**, whose many jobs average runner noise, and
about right for a single job's timeout. It is not fitted: it is fixed before the data and can only exceed
the point estimate.

**Other sources of spread** (r5 run): per table entry the median CV is 4–12 %; the `-O` copy against the
normal run has median ratio 1.01, so it is a full duplicate, a deterministic factor 2 inside the estimate,
not part of κ; runner heterogeneity is what the CI calibration measures.

**For the sensitivity analysis only,** u_cal is taken at 1.25 (the review's provisional value) and 1.35.
Neither is proposed as the value.

## (c) Sensitivity: u_model, κ, and the two inequalities

u_model is "an explicitly judgment-based factor, subject to sensitivity analysis" (owner). It covers the
planted-to-record model error (the mid-size validation shows it is large per shard),
including the overhead factor's, and anything else the calibration does not see.

**The campaign inequality.** The campaign's known terms at cap 16 are 84,261 s: the primary run's 64,784,
the survivor term 12,224, calibration 220, the count pass about 3,161 and the mutant campaign 3,872.
With the judged execution overhead (90 s × 62 jobs, 5,580 s) and the proposed retry allowance (2,400 s,
§d) they are 92,241 s. T_max = (86,400 − reserve) / κ, with the proposed reserve of 3,600 s (§d); "room"
is what T_max leaves for C7's sets 2 and 3.

| u_cal | u_model | κ | T_max (s) | room, with overhead and retries (s) | room, known terms only (s) |
| --- | --- | --- | --- | --- | --- |
| 1.25 | 1.0 | 1.3 | 63,692 | −28,548 | −20,568 |
| 1.25 | 1.1 | 1.4 | 59,143 | −33,098 | −25,118 |
| 1.25 | 1.25 | 1.6 | 51,750 | −40,490 | −32,510 |
| 1.25 | 1.4 | 1.8 | 46,000 | −46,240 | −38,260 |
| 1.25 | 1.5 | 1.9 | 43,579 | −48,662 | −40,682 |
| 1.35 | 1.0 | 1.4 | 59,143 | −33,098 | −25,118 |
| 1.35 | 1.1 | 1.5 | 55,200 | −37,040 | −29,060 |
| 1.35 | 1.25 | 1.7 | 48,706 | −43,535 | −35,555 |
| 1.35 | 1.4 | 1.9 | 43,579 | −48,662 | −40,682 |
| 1.35 | 1.5 | 2.1 | 39,429 | −52,812 | −44,832 |

At κ = 1, which the method cannot produce (u_cal > 1), the room is −9,441 s with overhead and retries.

**The affordable κ (a diagnostic, never a candidate for κ).** κ_aff = (86,400 − reserve) / total: the
largest κ the configuration fits under the model. Choosing it would be the "artificially smaller margin"
the owner ruled out.

| configuration (C7 sets 2–3 at 0) | κ_aff |
| --- | --- |
| primary run only, reserve 10,800 (r4's form; the review's figures on r4's calibration: **1.08 at cap 8, 0.99 at cap 16**) | r5 calibration: 1.07 at cap 8, 0.98 at cap 16 |
| the campaign's known terms, reserve 0, no overhead or retries | 1.11 at cap 8, 1.03 at cap 16 |
| the campaign with judged overhead, the proposed retries and reserve | 0.90 at cap 16 |

**The statistically justified κ** is at least 1.3 by the method (u_cal ≥ 1.19 measured locally and its
preregistered bound larger; u_model ≥ 1.0); across the sensitivity range it runs 1.3–2.1. Every affordable
κ above is below 1.3.

**The job inequality, correctly stated** (K1, B4). Both copies of a shard run against its 40 minutes (as
one job, or as two 20-minute replica jobs). Under the model, with the deterministic subdivision:
- the mean shard's closures and sampled gates are 1,916 s, and C7's set 4 adds about 63 s;
- the subdivision's modelled cost spread on the ball(3) analogue makes the heaviest about 1.04 × the mean:
  about 2,050 s before any survivor allowance, which fits only for κ ≤ 1.17;
- the survivor allowance adds c × 24 s: at cap 8 the heaviest is about 2,240 s (κ ≤ 1.07), at cap 16 about
  2,435 s, which **fails at κ = 1**.

So under the model the job inequality fails at every κ the rule can give, before C7's sets 2 and 3, at
32 shards. r4's "not the binding one" compared one replica with the 40-minute combined timeout and was
wrong. Under r4's index-even plan it failed by a factor of about 4 at any κ (LAYER2-R4-REVIEW K1). The
mid-size measurement (actual shard spread 3.2 × against the model's 1.34 ×) says the model understates
the spread. The levers are the per-shard work and the shard count (`FEASIBILITY-AND-REDESIGN.md`), not κ
or the timeouts.

**Consequence, by the owner's ruling.** If the calibrated estimate confirms this, the full Stage-0
campaign "must be reduced through a new reviewed design or declared infeasible under this budget — not
run with an artificially smaller margin". Layer 2 encodes that outcome as "not undertaken for cost".

## (d) Proposed reserve and retry allowance (advisory)

r4 proposed a reserve of 10,800 s made of three judgements. Under the campaign ledger two of them are
cost terms:

| r4 reserve item | r5 |
| --- | --- |
| per-job fixed overhead, about 69 jobs × 1.5 min (6,200 s) | **a ledger term**, execution overhead, measured by the CI calibration (CI-5) |
| one job lost to its timeout (2,400 s) | **the retry allowance**: proposed 2,400 s, one shard job at its timeout. A larger allowance only moves the launch further out of reach; measured retries replace it |
| setup variance and rounding, about 20 % (2,200 s) | **the reserve**: proposed 3,600 s (1 h), for what the ledger does not model (variance of the measured terms between planning and running, the population count's scaling to v8, rounding). A judgement |

The reserve is not a margin on the estimate's error; κ is. The two do not overlap. Neither proposal is
fitted: both can only make the launch harder, and the verdict holds with both at 0 (§c).

## (e) What is not known, and the decision sequence

**Not known:** |F_G|, |I_A|, |I_G| and |E_G| on v8; the representatives per site pair on v8 (the
site-pair count, conditionally approved and not dispatched); the runner-class calibration; the per-job
fixed overhead; the model error on v8 contexts.

**Sequence** (steps 1–5 before any v8 count, by the owner's ruling):
1. **κ's method:** approved.
2. **u_cal:** from the CI calibration by §b's preregistered rule, after the workflow's review and the
   owner's authorization of each launch.
3. **u_model:** a recorded judgement, using §c.
4. **The survivor cap, the reserve and the retry allowance** (`SURVIVOR-CAP-PROPOSAL.md`; §d).
5. **The site-pair count:** after its independent review, with the owner's authorization
   (`SITE-PAIR-COUNT.md`).
6. **The population count:** after the reviewed amendment (`AMENDMENT-PROPOSAL-V8-COUNT.md`) and the
   owner's authorization.
7. **G_D and O1:** after the count, before the full run.
8. **The campaign decision.** Launch iff κ · (the six components) + reserve ≤ 24 h and every job fits.
   Otherwise not undertaken for cost: a new reviewed design, or infeasible under this budget.

**Reproduce.** From `stage0/layer2/`:
- `python3 -I -B design/kappa_calibration.py code design/kappa/calibration-repeats.json` (about
  2.5 minutes);
- `design/overhead_measure.py code design/overhead/overhead.json`;
- `design/midsize_validation.py code design/toyrun/calib.json design/midsize/validation.json` (about
  6 minutes).

Timing output varies between runs and machines.
