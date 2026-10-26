# NP-AVG-1 Stage 0 Layer 2 r4: independent review

**Reviewed object:** `4a4d8bc1`, on top of `a782aa54`, branch `research/np-avg-1-plan-20261026`, PR #935. The review was read-only. All probes ran in scratch, and nothing ran on v8's configuration class. The drafter's uncommitted `FEASIBILITY-AND-REDESIGN.md` was not reviewed.

**Verdict: ACCEPT WITH CHANGES.**
- R1–R6 are applied, the frozen files are unchanged, and every control replays.
- The owner's rulings are encoded faithfully: κ has a rule and no value, κ is never lowered, the reserve is explicit, and the 24 h ceiling is fixed.
- Three findings change the cost picture.
  - **Per-job inequality.** r4 states this inequality wrongly. Under the current index-even shard plan it fails at any κ, because representatives concentrate in a few shards (K1).
  - **Survivor cap.** The cap proposal's concentration assumption is too low (K2).
  - **CI calibration.** The workflow is **not ready to dispatch**: one of its own guard checks can never pass, and the u_cal statistic is not preregistered (CI-1 to CI-4).

## 1. R1–R6, frozen files, replay

- **Frozen files.** `a782aa54..4a4d8bc1` touches only `layer2/**`, `planning/README.md` and `planning/SHA256SUMS`, and the SHA256SUMS change is README's line only. Layer 1 (r5, `STAGE0-PLAN.md`, `LAYER1-FREEZE.md`), `amendments/` and `review/` are byte-unchanged. `sha256sum -c SHA256SUMS` passes on all 333 lines. The committed `review/LAYER2-R3-REVIEW.md` and `LAYER2-REVIEW.md` are byte-identical to my delivered texts.
- **R1.** `rule_T.statement_scope` is E1-T6's text only for "L_A = L_G = 0". The toy `result.json` has outcome "L_A > 0 or L_G > 0", and its rule-T `statement_scope` reads "not applicable (outcome: …)". This is checked by L2-T6, and M_scope_every_outcome is killed.
- **R2.** The v8 survivor cap is a placeholder with no default; the toy profile's 10 is design evidence only. `survivor_gates_incomplete` is in `result.json`, and L2-MRG and L2-PLACEHOLDER check both. Applied.
- **R3.** The new `index_check` gate `index_roundtrip` is VOID in the merge. L2-IDXRUN checks 312 members, and a planted off-by-one fails all 312. Applied.
- **R4.** PO-L2-7's text is as ruled. **R5:** the overhead is labelled as a judgement and is now measured (§4 below). **R6:** §13 item 7 is added. Applied.
- **Replay.** I ran a full `l2run.py design` replay on a scratch copy of the tree at `4a4d8bc1` (11 min).
  - All 24 steps exit 0, except `certificate_toy`, which exits 2 for the expected reason: the scratch copy is not a git repository, so the commit binding fails closed.
  - Self-test: 36/36, including L2-LAUNCH, L2-PLACEHOLDER, L2-IDXRUN and L2-T6.
  - Quick campaign: 51/51 killed.
  - Cross-check: 58 compared, pass.
  - `e1check_replay`: byte-identical (sha `d2297fb7…`).
  - `crosscheck`, `refusal_probe_v8`, `dryrun_v8_plan_no_closure`, `merge_toy`, `planted_survivor_path` and `code_r5_equivalence_quick` outputs are byte-identical to the committed ones.

## 2. The rulings as encoded; L2-LAUNCH

- **No κ value is set anywhere.** `budget.kappa_rule.u_cal` and `u_model`, `reserve_runner_seconds` and the v8 cap are all `OWNER`. `kappa_from_rule` (ceil(u_cal·u_model·10)/10) is the only source of κ, and `launch_decision` never changes it. The ceiling is `runner_hours = 24`, and L2-PLACEHOLDER pins it. The non-fitting outcome is the owner's text ("not undertaken for cost … not lowered to fit").
- **L2-LAUNCH kills both mutants.** M_launch_fit_kappa is killed by `over_total`: a fitted κ of 1.528 would admit the run. M_launch_no_reserve is killed by `reserve_decides`: 73,600 + 13,000 > 86,400, while 73,600 alone would fit. Two gaps remain:
  - **(L-a) Rounding.** The test's κ = 1.25·1.25 = 1.5625 rounds to 1.6 both up and to nearest, so a round-to-nearest mutant survives. Add a case such as 1.21·1.0 → 1.3, and a mutant for it.
  - **(L-b) The per-job input is a mean.** `estimate()` passes `shard_job = (closures + sampled gates + C7 + survivor)/S`, the mean shard, to the job inequality. The heaviest shard is what can time out (K1). No test covers a heterogeneous shard set. Fix the input to the maximum per-shard estimate, and add a case and mutant (heaviest shard over, mean under).

## 3. Findings on cost

**K1. The per-job inequality is misstated, and under the index-even shard plan it fails at any κ.**
- **Misstatement.** `KAPPA-PROPOSAL.md` §c and `SURVIVOR-CAP-PROPOSAL.md` §4 compare one replica, about 1,043 s at cap 8 or 1,138 s at cap 16, with the **40-minute combined** timeout, and conclude "not the binding one". The code compares both copies together (about 2,085 s at cap 8 before C7, about 2,147 s with C7 set 4) with 2,400 s. That fails for κ above about 1.12. In the replica form the timeout is 20 min, and it fails at the same κ.
- **Concentration (new, non-v8 analogue probe).** Representatives are lexicographic minima and the index runs singles first, then pairs by (i < j). Representatives therefore pile into a few shards, and closure cost per shard is proportional to representatives. This is visible in the replay: shard 0 took 6 s with 260 reps, shard 3 took 0 s with 30.
  - **Probe.** `review-l2r4/probe/rep_concentration.py` counts reps per shard: C4v about z, `index_of` order, 25 slices, 32 even shards. It is pure combinatorics, and radius 4 is refused.
  - **Controls.** It reproduces the toy's 488 reps and the 260/36/162/30 split exactly.
  - **Heaviest shard against the mean:**

    | region | sites | heaviest shard / mean | top 8 shards' share | empty shards |
    | --- | --- | --- | --- | --- |
    | ball(1), toy | 7 | ×2.9 | 67 % | 15 |
    | ball(2) | 25 | ×3.7 | 70 % | 14 |
    | ball(3) | 63 | ×5.0 | 76 % | 12 |

  - **Consequence at v8's ball(4).** By extrapolation, the heaviest v8 shard is likely ≥ 5× the mean. Its closures alone would be ≈ 5 × 1,890 ≈ 9,500 s against 2,400 s, so it fails at κ = 1 by about 4×. Under the current shard plan the run would most likely be INCOMPLETE by timeout, whatever κ is.
- **Remedy.** Balance shard boundaries by representative count, using prefix counts from this combinatorics. The total and the science stay the same, and the cap model's uniform case becomes exact for reps. It needs v8's reps per index range. That is the same kind of computation as the dry run's Burnside count (region, slices, group; no record, context or closure), but it is a computation on v8's index space, so the owner must say whether the dry run's standing permission covers it (see §7).

**K2. The survivor cap: the proposal and its justification.**
- **Scientific justification (sound).** The cap never changes a count or a verdict. Exceeding it gives INCOMPLETE with the 58 counts complete and flagged (R2). So the cap is a resource and risk parameter, not a scientific one, and that holds without any v8 count.
- **Failure probability (model-conditional, understated).** The proposal sets f ≈ 2 as "about the toy class's". At 32 shards the analogues give a heaviest shard of 2.9–5.0× and a top-quarter share of 67–76 % (f ≈ 2.7–3.0 in the proposal's top-quarter model), with a heaviest shard above any f the model allows (f ≤ 4 caps it at 4/32).
  - The Poisson calculation also assumes survivor orbits land independently and in proportion to reps. Survivors come from geometric constraint blocks, and the planted ones were clustered, so clumping makes exceedance more likely.
  - "c = 16 holds under f ≤ 2 with a wide margin" should be restated as conditional on that model. For example, with the heaviest shard at w ≈ 0.157 (ball(3)), X = 64 gives P(> 16 in that shard) of the order of a few %. X = 32 stays small.
  - With rep-balanced shards (K1), the uniform row applies to reps.
- **Measured against modelled.**
  - **Measured on planted toy-geometry orbits up to v8's maximum context of 29:** memory and detail size. "Memory does not bind" stands.
  - **Modelled:** the time per orbit at v8 sizes (24 s per shard) comes from the planted calibration at m_max.
  - **Wrong:** the §4 "fits the job inequality" sentence (K1).
- **The site-pair-level count is a real option, and cheap.** It needs region, slices and group only. ball(3) ran in 1.6 s; v8 would take seconds to minutes. It is exact, and it settles the cap's shard weights and the per-job inequality together. It should be separated from the population count (§7).

**K3. The stale "affordable κ" figure.**
- §3.6 and §12 of `LAYER2-PLAN.md` say "κ above about 1.18 does not fit S7". That figure predates the reserve and the cap.
- Under r4's own rule, before C7 sets 2–3, the largest κ the budget admits is (86,400 − 10,800)/(64,029 + cap·767): **1.08 at cap 8, 0.99 at cap 16**.
- It should be stated explicitly as the **computationally affordable κ under the model**, beside, and never in place of, the statistically justified κ. Every sensitivity row (1.3–2.1) lies above it.

## 4. KAPPA-PROPOSAL.md

- **u_cal statistic: correct.** It is the 99th percentile of the ratio of two independent calibrations, with the r3 max/median withdrawn. At n = 10, "empirical p99" equals max/min exactly (the 90th of 90 ordered pairs), as the table says.
- **The drift 1.21 → 1.29 → 1.37 is ordinary n = 10 sampling noise.** My simulation (`probe/ucal_sim.py`, lognormal) gives a 5–95 % range for the estimator of:

  | n | σ = 0.06 | σ = 0.09 |
  | --- | --- | --- |
  | 10 | 1.12–1.31 | 1.18–1.50 |
  | 20 | 1.15–1.28 | 1.23–1.46 |

  - At n = 20 the point estimate is still ±6–9 %. u_cal should therefore be preregistered as an upper confidence bound, or the point estimate's error assigned to u_model explicitly, before the data are seen (CI-3).
  - The ratio-of-two statistic is conservative for the total, because many jobs average runner noise, and about right for a single job. Say so, so that nobody reads it as fitted.
- **The u_model sensitivity table is correct.** I recomputed T_max and room for all 10 rows, plus the κ = 1 line, and they match. It shows infeasibility at every u_model from 1.0 to 1.5 without choosing one. Good.
- **The reserve (3 h) is reasoned, not fitted.**
  - Its three items are judgements and are labelled as such.
  - It cannot have been fitted to pass, because it only makes fitting harder, and infeasibility holds even with a reserve of 0 at κ ≥ 1.3: 1.3 × 70,165 > 86,400.
  - One improvement: the per-job fixed overhead (6,200 s) is a cost, not a margin. The CI calibration can measure it (CI-5).
- **Blurs between measured and modelled numbers, to fix:**
  - **(B1)** The §a column "v8 value" should read "v8 estimate (model; local planted calibration)". The C7 per-record figures 0.0715 s and 0.313 s are model-weighted from planted timings, not measured on records.
  - **(B2)** "the closures term is under-stated by about 45 %" applies a toy-geometry measurement of the overhead (2.9) to v8 sizes. That transfer is unmeasured.
  - **(B3)** "the over-prediction … does not transfer to v8" is an untested explanation and should be labelled as one.
  - **(B4)** The per-job sentence (K1).

## 5. The infeasibility finding

- **Sound, conditional on the model.** At every κ the method can produce (≥ 1.3 in the table), the known terms plus the survivor term already exceed T_max before C7 sets 2–3.
- **Sets 2–3 are probably the largest term.** At |F_G| equal to 1 % of N they add about 16,000 s, and the trivial bound is about 1.6 × 10⁶ s.
- **K1 adds an infeasibility that does not depend on κ:** the per-job inequality under the current shard plan.

**Cheap non-v8 validation, in increasing cost:**
1. **The concentration probe (done, K1).**
2. **The toy per-shard times.** These are already in the run logs, and they scale with reps.
3. **A mid-size analogue design profile** (dim 3, ball(2) or ball(3), tlast 23, with (n, port) ≠ v8's key, so the content-keyed guard admits it, and contexts spanning v8's 8–29 range). Run the dry-run estimate and 2–4 real shards, bounded locally or in CI, and compare predicted with actual for:
   - the closures term;
   - the overhead at v8-like sizes;
   - the C7 cost per record;
   - the per-shard skew.

   This is the validation that u_model currently stands in for. It touches no v8 object.

**Owner distinction 4: can 24 h accommodate the scientifically justified configuration?** Under the model, no. r4 correctly does not lower κ, and it proposes no redesign. The owner now asks for one, and the drafter's separate file is outside this review.

Redesign levers for that design to weigh, none of which lowers κ:
- (i) representative-balanced shards, which is necessary in any case;
- (ii) the `-O` full duplicate, L1 §5b item 7, a factor of 2 on almost every term (a Layer-1 amendment);
- (iii) C7 set 2 on F_G, where Lemma G-D is the proof-backed route the owner has conditionally approved;
- (iv) engineering of the gate overhead (2.9×);
- (v) the budget itself.

Three readings in r4 need the owner's explicit confirmation, because "including all run overhead" could be read either way:
- the full mutant campaign is outside the 24 h;
- the count pass is outside the 24 h;
- the CI calibration is outside the 24 h.

## 6. CI calibration (`layer2/ci/`): pre-dispatch review

**v8 isolation: holds, with the basis stated correctly.**
- I ran `calib_ci.py` under an audit hook (`probe/calib_audit.py`). It opens exactly itself, `LAYER2-MANIFEST.json`, `l2calib.py`, `s0geom.py`, `s0ref.py` and `l2refcheck.py`, and imports no project module.
- Extraction is a whitelist of 19 names, and an exact-set check makes `Setup`, `V8`, the grants and the record functions impossible to define. The transcription of `l2calib.py` is faithful, with the same seed, pool, frame and sizes.
- The extracted `closure` has no guard. So isolation rests on the reviewed, pinned 150-line script, which builds only planted sets, and not on the engine's v8 lock. The tripwire is a backstop for objects, not for raw tuples, and should be described that way.
- `FORBIDDEN` omits `V8_KEY`, `V8_REF` and `NO_V8`. This is harmless, because extraction is whitelist-based, but checklist item 1's "covers every v8-capable name" is not literally true. Add them.

**Trigger.**
- `verify.yml` (push to main; pull_request) and `hidden-sector-replay.yml` (main only) do not fire.
- `bg2-orientation-design.yml` and `bridge-compatibility-research.yml` have push triggers on **any branch**, filtered only by path. For a new branch GitHub diffs against the parent of the earliest pushed commit. One commit on main's head that adds only the new workflow and the NP-AVG-1 planning paths matches neither filter; those paths do not exist on `origin/main`, so they are all new. A push of more than 1,000 commits, or a diff timeout, runs path-filtered workflows unconditionally.
- So the branch must be **exactly one commit on the live main head**. Re-check at launch against live main (my `origin/main` is from 2026-10-24), and open no PR. Neither path-triggered workflow is a governed launch, but they must not fire.

**Limits.** These are acceptable:
- `permissions: contents: read`;
- `persist-credentials: false`;
- no secrets;
- 20 jobs at `max-parallel` 4;
- timeouts of 5, 15 and 5 min, so a worst case of 310 runner-min;
- a concurrency group that does not cancel;
- 30-day artifacts, retained under §A.42 before the κ decision lands.

**Must change before dispatch:**
- **CI-1 (blocker): the guard can never pass.** `PIN_WORKFLOW` hashes the workflow file, which contains `PIN_WORKFLOW`'s own value. A file cannot contain its own SHA-256, so the guard always fails. The comment says "without this line's value", but the command does not strip it. Either hash a normalized copy (the value blanked by `sed`) or drop the self-pin.
  - In any case, every pin lives in the pushed commit, so the pins detect accidental drift, not substitution. The binding is the owner's authorization naming the exact head SHA plus the reviewer's recorded tree. Add a post-run check that the run's `head_sha` equals the authorized SHA, retained with the result.
- **CI-2 (blocker): pins are still unfilled.** Fill `PIN_CALIB_CI`, `PIN_CALIB_AGGREGATE` and `PIN_MANIFEST`, and pin `checkout`, `setup-python`, `upload-artifact` and `download-artifact` to commit SHAs (`download-artifact` ≥ v4.1 for `merge-multiple`). Confirm that `setup-python` provides 3.13.16; if not, the job fails, which is safe but wastes the launch.
- **CI-3 (blocker, preregistration): the u_cal statistic is not fixed.** `calib_aggregate.py` prints three candidates (empirical p99, normal p99, max/min) and does not say which one is u_cal. The governing rule requires the decision rule to be fixed before the data. Freeze, before dispatch:
  - the statistic, whether a point estimate or an upper confidence bound (§4);
  - whether it is computed on the unweighted aggregate or the v8-weighted one, which differ;
  - what happens with heterogeneous runners: for example, all CPU models pooled, or a bimodal result taken as VOID.
- **CI-4: record the runner's CPU model.** `platform.platform()` does not give it; read `/proc/cpuinfo` model name. Without it, nobody can tell whether 20 jobs sampled the hosted fleet's CPU mix.
- **CI-5 (recommended): record wall-clock start and end per calibration.** With the host's job records, job duration minus script time measures the reserve's per-job fixed overhead, which is now a judgement.
- **CI-6 (recommended): temporal independence.** All 20 jobs run within minutes of each other, so time-of-day variation is not sampled. Either authorize two launches at different times (each a separate launch, since each push is one) or state this in u_model.
- **CI-7 (optional):** `aggregate` with `if: always()` would print a VOID with a count when some job fails, instead of being skipped.

## 7. AMENDMENT-PROPOSAL-V8-COUNT.md (design only, not adopted)

**Isolation from the engine is adequately designed.**
- It reuses the dry run's engine-free path, which my earlier import trap verified, and adds a distinct `V8CountGrant` with its own scope string and designation line.
- Each grant is refused by the other's entry points.
- The controls cover the import trap, toy equivalence (I_A 1,071, I_G 667, F_G 595 in 283 orbits, E_G 12), the sentinel, determinism and the landing check.

**Additions needed:**
- **(A1) A mutant on the engine side.** Add a mutant in which the engine's `_guard` accepts a `V8CountGrant`, for example through a subclass or the same digests, and require `V8CountGrant` not to subclass `V8Grant`. The current list mutates only the count side.
- **(A2) Split off the representatives-per-shard count.** It needs no Q⁰, frame or predicate, only region, slices and group. Proposing it separately, or as a dry-run extension, would let the owner rule on it before the cap is fixed. Both K1 and K2 need it, and the owner's sequencing otherwise forbids it until after the cap.
- **(A3) Cross-check at larger sizes.** The count rests on `l2plan`'s independent reimplementation of Q⁰, frame and tips, which is checked only at toy sizes (contexts of 8 or fewer). G_D and O1 will rest on its v8 numbers. Cross-check it against the engine-based populations on the mid-size analogue (§5 item 3) before the v8 count.
- **(A4) Measure the count's cost.** Its cost (1–2 core-hours) is extrapolated from toy timings by an assumed linear scaling. Time it on the analogue to set the count's timeouts from a measurement.

## 8. The owner's four distinctions in r4

| distinction | kept? | where it blurs |
| --- | --- | --- |
| statistically justified κ vs affordable κ | mostly: no κ value; never lowered | the stale "1.18" (K3); the affordable κ (1.08 / 0.99) is not stated as such |
| the proposed cap vs its scientific justification | the benign-failure argument is sound | P(exceeded) rests on an understated f and on independence (K2); the "fits the job inequality" sentence is wrong (K1) |
| measured costs vs unmeasured assumptions | overhead, reserve and u_model labelled as judgements; the model labelled unvalidated | B1–B4 (§4) |
| can 24 h hold the justified configuration | correctly "no, under the model", with κ not lowered | no redesign yet (now requested); K1 adds a κ-independent per-job infeasibility; the three budget-scope readings need confirming (§5) |

## 9. Required changes (r5)

1. **K1 and L-b:** correct the per-job statements in `KAPPA-PROPOSAL.md` and `SURVIVOR-CAP-PROPOSAL.md`. Make the per-job input to `launch_decision` the heaviest shard, and add a test and mutant. Record representative-balanced sharding as a redesign item.
2. **K2:** restate the cap's failure probabilities as conditional on the model, using the analogue concentration (or the exact count, if authorized). Keep the benign-failure justification separate.
3. **K3, B1–B4:** add an explicit affordable-κ line, remove the stale 1.18, and fix the measured/modelled labels.
4. **L-a:** add the rounding case and its mutant.
5. **CI-1 to CI-4 before any dispatch;** CI-5 and CI-6 recommended. Then a short pre-dispatch re-check of the exact branch commit (tree, pins, live-main triggers) before the owner authorizes the push.
6. **A1–A4** in the amendment design before its review.

**Probes** (scratch, retained for the drafter):
- `review-l2r4/probe/rep_concentration.py`
- `review-l2r4/probe/calib_audit.py`
- `review-l2r4/probe/ucal_sim.py`
- `review-l2r4/replay.log`
