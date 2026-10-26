# NP-AVG-1 Stage 0, Layer 2: κ, the reserve and the launch rule (advisory, r4)

**Status: advisory. It sets nothing.** κ's two components, u_cal and u_model, and the reserve are
`OWNER-PLACEHOLDER` values in `l2config`, with no default anywhere in code or configuration. The v8
profile is refused while any of them is open (`LAYER2-PLAN.md` §3.5, §4.2). Nothing here ran on v8's
configuration class: v8 enters only through the dry run's combinatorics (counts and the context-size
histogram; no context, no closure, no shared-tip or F_G count).

**What changed from r3.** r3 proposed κ = 1.5, with u_cal = 1.2 taken as the max/median of single
local calibrations. The review (`../../review/LAYER2-R3-REVIEW.md` §6) showed that this answers the
wrong question. The relevant statistic is the ratio between two *independent* calibrations: one
produces the estimate, and the run is another draw. That correction raised the provisional value
from 1.5 to about 1.6. **The change comes from the corrected statistic, not from any budget fit.**
The owner has since ruled that κ has an approved method and no numerical value yet, so this document
now gives the method, the current evidence and a sensitivity analysis, not a value.

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
- **The CI calibration:** authorized conditionally, as "a separate, planted-set-only CI timing
  calibration, provided it cannot access v8 and its exact workflow and resource limits are reviewed
  before dispatch. This is not authorization to dispatch the existing full experimental workflow"
  (`ci/CI-CALIBRATION-PROPOSAL.md`).

**The launch rule as implemented** (`l2plan.kappa_from_rule`, `l2plan.launch_decision`; L2-LAUNCH):
- κ = u_cal × u_model, rounded up to one decimal; there is no other source of κ.
- Launch iff κ · total + reserve ≤ 86,400 runner-seconds (24 h) and κ · each job ≤ its timeout.
- Otherwise the decision is "not undertaken for cost: the experiment must be reduced through a new
  reviewed design or declared infeasible under this budget". κ is never lowered to fit; mutants that
  lower κ, or that drop the reserve, are killed.

**Sources.** Every number below is read from `design/kappa/calibration-repeats.json` (step
`kappa_calibration_repeats`), `design/overhead/overhead.json`, `design/overhead/survivor-cap.json` and
`design/runs/dryrun_v8_estimate.out` in `design/RUN-MANIFEST.json`. These are timing data, measured
locally on one machine (Python 3.13.16), not on a CI runner.

## (a) The cost model

Every term is in runner-seconds and includes the `-O` copy (factor 2), as `l2plan.estimate` computes
it. Each term's formula is printed in `dryrun.json` under `cost.formulas`. The values are medians over
the 10 local calibrations.

| term | formula (abridged) | v8 value |
| --- | --- | --- |
| closures | 2 · overhead · Σ_m count(m) · (orbits/N) · 2 [t_A(m) + t_G(m)]; **overhead = 2 is an unmeasured judgement** | 58,235 |
| sampled gates | C11 (i), C17, C18 at 1 in 1,000 orbits; C8 at 1 in 100 orbits | 2,354 |
| S1a | bound closures, three streamed reference passes per bound, per-line closures | 548 |
| pre-flight, merge | stated allowances | 900 |
| C7 set 4 (H₁₀₀₀) | (N / 1,000) · (c7_A + c7_G), with c7_A = 0.0715 s and c7_G = 0.313 s per record | about 1,990 |
| **known terms** | sum of the above | **64,029 (17.8 h)** |
| survivor gates | cap · 767 s (both copies, all shards; includes C7 set 1) | owner's cap: 6,136 at 8, 12,272 at 16 |
| C7 sets 2 and 3 | \|F_G\| · c7_G + (\|I_A\| / 100) · c7_A + (\|I_G\| / 100) · c7_G | **unknown: v8 count not authorized** |

**The unknown inputs.** |F_G|, |I_A| and |I_G| each lie in [0, N], with N = 5,163,225, and
F_G ⊆ I_G. On the toy class they are 42.5 %, 76.5 % and 47.6 % of N, which carries no information
about v8. They become known only through the count-only pass, whose amendment is unadopted
(`AMENDMENT-PROPOSAL-V8-COUNT.md`).

**The model is not validated** (review §5; plan §3.6).
- **The toy comparison.** The toy dry run predicts a C7 term of 191–229 s and a total of
  2,197–2,453 s, across runs. All four toy shards ran in about 9 s. The over-prediction comes mostly
  from fixed allowances and from contexts smaller than any calibrated size, so it does not transfer
  to v8.
- **The overhead factor.** It is set at 2. Measured locally (`overhead_measure`) as Shard.rep time
  against four bare closures, it is 2.93 on every toy orbit and 2.87 on 120 planted records (medians
  2.9–3.0, 90th percentile about 4). On that evidence the closures term is under-stated by about
  45 %, which would raise the known terms to about 90,000 s.
- **Every conclusion below is therefore "under the cost model".** u_model is the explicit place for
  that error. It is not also absorbed by a second factor: the overhead factor stays at its stated
  value, and the measurement is reported beside it.

## (b) The calibration data and u_cal's statistic

**u_cal, as the review defines it,** is the 99th percentile of the ratio between two independent
calibrations. `kappa_calibration.py` computes it over every ordered pair (90 pairs) of the 10 local
calibrations (5 normal, 5 `-O`, each in a fresh process), on the v8 estimate's known terms.

| local run | σ of log(known terms) | normal-approximation p99 of the ratio, exp(2.326 · √2 · σ) | empirical p99 (= max/min) |
| --- | --- | --- | --- |
| r3 (review's re-read) | 0.06 | 1.22 | 1.21 |
| r4, interim | 0.082 | 1.31 | 1.29 |
| r4, final (retained) | 0.091 | 1.35 | 1.37 |

**What the table shows.** The statistic moves from 1.21 to 1.37 between three local repeats of the
same 10-calibration procedure. With n = 10 on one machine it is not stable enough to fix u_cal. This
is direct support for the owner's requirement of at least 20 calibrations on the runner class. The
CI calibration (`ci/`) is designed to measure it there.

**Other sources of spread** (final run):
- **Per table entry:** the median CV is 4–9 %, and max/median reaches 1.17–1.73.
- **Cache:** pass 1 over the toy records is 0.95–0.96 of passes 2–3 this time (1.04–1.06 in r3), so
  in-process caching effects are a few per cent either way.
- **`-O` duplication:** the paired `-O`/normal ratio has median 1.01, so the `-O` copy is a full
  duplicate. It is a deterministic factor 2 inside the estimate, not part of κ.
- **CI-runner heterogeneity:** not measured. This is what the CI calibration measures.

**For the sensitivity analysis only,** u_cal is taken at two values:
- 1.25, the review's provisional value;
- 1.35, the final local run's normal approximation.

Neither is proposed as the value; the value is to come from the CI calibration.

## (c) Sensitivity analysis: u_model, κ and the launch inequality

u_model is "an explicitly judgment-based factor, subject to sensitivity analysis" (owner). It covers
the planted-to-record model error, including the overhead factor's, and anything else the
calibration does not see. The table gives, for each pair (u_cal, u_model):
- κ, rounded up to one decimal;
- the largest admissible total T_max = (86,400 − reserve) / κ, with the reserve at the proposed
  10,800 s (§d);
- the room left for C7's sets 2 and 3 after the known terms (64,029 s) and the survivor term at a
  cap of 8 or 16.

| u_cal | u_model | κ | T_max (s) | room for C7 sets 2–3, cap 8 (s) | room, cap 16 (s) |
| --- | --- | --- | --- | --- | --- |
| 1.25 | 1.0 | 1.3 | 58,154 | −12,011 | −18,147 |
| 1.25 | 1.1 | 1.4 | 54,000 | −16,165 | −22,301 |
| 1.25 | 1.25 | 1.6 | 47,250 | −22,915 | −29,051 |
| 1.25 | 1.4 | 1.8 | 42,000 | −28,165 | −34,301 |
| 1.25 | 1.5 | 1.9 | 39,789 | −30,376 | −36,512 |
| 1.35 | 1.0 | 1.4 | 54,000 | −16,165 | −22,301 |
| 1.35 | 1.1 | 1.5 | 50,400 | −19,765 | −25,901 |
| 1.35 | 1.25 | 1.7 | 44,471 | −25,694 | −31,830 |
| 1.35 | 1.4 | 1.9 | 39,789 | −30,376 | −36,512 |
| 1.35 | 1.5 | 2.1 | 36,000 | −34,165 | −40,301 |

**What it shows, under the cost model.**
- For every u_model from 1.0 to 1.5, at either u_cal, the known terms and the survivor term already
  exceed T_max, before C7's sets 2 and 3 add anything (and they add |F_G| · 0.313 s). Even κ = 1,
  which the method cannot produce since u_cal > 1, leaves 5,435 s at cap 8 and −701 s at cap 16.
- With the measured overhead (about 2.9 instead of 2), the known terms rise to about 90,000 s, and
  the gap widens.
- **Per job.** As normal and `-O` replicas, a shard job is about 1,043 s (cap 8) or 1,138 s (cap 16)
  before C7. At κ = 1.6 that is 1,669 s and 1,821 s against the 2,400 s timeout; the job inequality is
  not the binding one.

**Consequence, by the owner's ruling.** If the calibrated estimate confirms this, the full Stage-0
run "must be reduced through a new reviewed design or declared infeasible under this budget — not run
with an artificially smaller margin". Layer 2 encodes that outcome as "not undertaken for cost".
Whether to reduce, and how, is the owner's decision. The largest model terms are the closures, which
contain the `-O` duplication (L1 §5b item 7) and the overhead factor. Reducing either is a design
change that needs review, and for item 7 a Layer-1 amendment. Nothing here proposes one.

**What the sensitivity does not settle.** It is conditional on the local calibration and the
unvalidated model. The CI calibration replaces the first. The second is improved only by an authorized
timing sample of real v8 records, which is a v8 computation and not proposed here.

## (d) A proposed reserve (advisory)

The ceiling covers "all run overhead"; the reserve is the explicit term for what the estimate does
not model.

| item | basis | runner-seconds |
| --- | --- | --- |
| per-job fixed overhead | about 69 jobs (owner check, dry run, pre-flight, S1a, 64 shard replicas, merge) × about 1.5 min each for checkout, Python setup and artifact transfer. A judgement; the CI calibration's job durations, read from the host's structured job records, would measure it | about 6,200 |
| one job lost to its timeout | a hung or slow job is cancelled at its timeout and makes the run INCOMPLETE, but its runner time is spent: one 40-minute job | 2,400 |
| setup variance and rounding | about 20 % of the above | about 2,200 |
| **proposed reserve** | rounded | **10,800 (3 h)** |

The reserve is not a margin on the estimate's error; κ is. The two do not overlap. A larger reserve
would only move the launch further out of reach under the current model.

## (e) What is not known, and the decision sequence (the review's §6, with the owner's rulings)

**Not known:**
- |F_G|, |I_A|, |I_G| and |E_G| on v8;
- the representatives per shard on v8 (`SURVIVOR-CAP-PROPOSAL.md`);
- the runner-class calibration;
- the model error on v8 contexts.

**Sequence.** Steps 1–4 come before any v8 count, by the owner's ruling.
1. **κ's method:** approved, κ = u_cal × u_model.
2. **u_cal:** from the CI calibration (at least 20 runner-class calibrations; the 99th percentile of
   the ratio of independent calibrations). This needs the workflow's review, then the owner's
   authorization of its launch.
3. **u_model:** a recorded judgement, using the sensitivity table above.
4. **The survivor cap and the reserve.** The ceiling is fixed at 24 h. Proposals:
   `SURVIVOR-CAP-PROPOSAL.md` and §d above.
5. **The v8 count-only pass:** after the reviewed amendment (`AMENDMENT-PROPOSAL-V8-COUNT.md`) and
   the owner's authorization.
6. **G_D and O1:** after the count, before the full run.
7. **The complete estimate and the launch rule.** Launch iff κ · total + reserve ≤ 24 h and every
   job fits. Otherwise not undertaken for cost: a new reviewed design, or infeasible under this
   budget.

**Reproduce.** From `stage0/layer2/`:
- `python3 -I -B design/kappa_calibration.py code design/kappa/calibration-repeats.json` (about
  2.5 minutes);
- `design/overhead_measure.py code design/overhead/overhead.json`;
- `design/survivor_cap_measure.py code design/kappa/calibration-repeats.json design/overhead/survivor-cap.json`.

Timing output varies between runs and machines.
