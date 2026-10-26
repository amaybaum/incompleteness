# NP-AVG-1 Stage 0 Layer 2: changes r4 → r5

r4 is the draft at `4a4d8bc1`. Its independent review is `../../review/LAYER2-R4-REVIEW.md` at
`bc042a61` (probes in `../../review/toy-l2r4/`): ACCEPT WITH CHANGES. r5 applies it in place, as a WIP
draft, with the owner's decisions of 2026-10-26 (amaybaum) on the three questions the review collected
and on the shard imbalance. No frozen file, no part of erratum E1 and no review file is changed. No
workflow is placed under `.github/`, nothing is pushed to a trigger branch, and nothing ran on v8's
configuration class. The site-pair count on v8's index space is implemented, refuses v8 without its own
authorization, and is not dispatched.

## The review's items

| item | edit (code) | edit (documents) | control and mutant |
| --- | --- | --- | --- |
| **K1**, the per-job inequality | `l2plan`: the shard plan is the deterministic subdivision by representative rank (`site_pair_counts`, `RepIndex`, `subdivision_cuts`, `shard_of`, `plan_from_cuts`, `plan_accounting`, `dry_shard_plan`); `shard_context_weights` gives each shard's modelled closure cost; the dry run prints the plan's kind, accounting and representatives per shard, and on v8 without a count file the index-even plan as a diagnostic. `l2cert` item 7 refuses a dry-run plan that is not the profile's subdivision or fails its accounting; `l2merge` refuses a shard whose representatives differ from the plan's. `l2config`: `shard_plan` per profile | `LAYER2-PLAN.md` §3.5, PO-L2-1, PO-L2-25, §10; `KAPPA-PROPOSAL.md` §c and `SURVIVOR-CAP-PROPOSAL.md` §4 corrected (both copies against 40 minutes; the κ-independent failure); `FEASIBILITY-AND-REDESIGN.md` §2 | L2-SHARDPLAN, L2-SPLIT (new); L2-ORB on the subdivision's plan; `subdivision_bounds` (new step); mutants M_subdiv_drop_record, M_subdiv_dup_record, M_count_inpair_order |
| **L-b**, the per-job input | `l2plan.launch_decision` compares every element of a per-shard list; `estimate` passes the per-shard list (`per_shard_jobs`, the shared terms split by modelled shard cost, the survivor allowance per shard whole), and reports `shard_job_bounds` (the mean shard's known terms, a lower bound under any plan) | §3.5, PO-L2-24 | L2-LAUNCH: heaviest over, mean under; the per-shard split; mutant M_launch_mean_shard |
| **K2**, the cap | `design/survivor_cap_derive.py` (new step `survivor_cap_derive`): exact P(INCOMPLETE by the cap) under the subdivision's exact representative balance, with clustering b as a parameter; the derived cap c*(X, b, α); resources by cap | `SURVIVOR-CAP-PROPOSAL.md` (r5): derived, model-conditional; keeps 16 within a stated envelope, with 24 as the α = 1 % alternative | — |
| **K3**, the stale "1.18" | — | removed from `LAYER2-PLAN.md` §3.6 and §12; the affordable κ stated beside the justified κ in `KAPPA-PROPOSAL.md`, `FEASIBILITY-AND-REDESIGN.md` and §12 | — |
| **L-a**, rounding | — | §3.5 | L2-LAUNCH: 1.21 × 1.0 → 1.3; mutant M_kappa_round_nearest |
| **u_cal (CI-3)** | `ci/postrun.py` (new): u_cal = exp(2.3263 · √2 · s_U), s_U the one-sided 95 % upper confidence bound on the standard deviation of the log v8 known terms (χ², Wilson–Hilferty), pooled over CPU models | `ci/CI-CALIBRATION-PROPOSAL.md` §4; `KAPPA-PROPOSAL.md` §b | `ci_calibration_local_check` (postrun on a synthetic launch) |
| **B1–B4** | — | `KAPPA-PROPOSAL.md` §a (B1: "v8 estimate (model; local planted calibration)"; the C7 per-record figures model-weighted), §a (B2: the overhead transfer to v8 sizes unmeasured; the mid-size measurement), §a (B3: an untested explanation, now tested on the analogue), §c (B4); `LAYER2-PLAN.md` §3.6 | — |
| **CI-1** | workflow: `PIN_WORKFLOW` dropped; `calib_ci.py` records the run identity; `postrun.py` checks the run's `head_sha` and every calibration's `GITHUB_SHA` and `GITHUB_RUN_ID` against the owner-named SHA | `ci/CI-CALIBRATION-PROPOSAL.md` §2 | `ci_calibration_local_check` (no self-pin; postrun VOID on another SHA) |
| **CI-2** | the three file pins filled from this tree; the four actions pinned to commit SHAs | §3 (what `git ls-remote` and the versions manifest confirmed on 2026-10-26, and what cannot be confirmed offline) | `ci_calibration_local_check` (pins equal the files' SHA-256; every action pinned to 40 hex) |
| **CI-4** | `calib_ci.py` records the CPU model from `/proc/cpuinfo`; the aggregator reports per model | §5 | `ci_calibration_local_check` |
| **CI-5** | `calib_ci.py` records the script's wall-clock start and end; `postrun.py` reports the per-job fixed overhead from the host's job records | §5; `l2config` `budget.campaign.per_job_fixed_overhead_seconds` | `ci_calibration_local_check` |
| **CI-6** | `postrun.py` pools several launches | §5: two launches six hours apart proposed, or the time of day in u_model | — |
| **CI-7** | `aggregate` under `always()` and the guard's success; the download step may find nothing; the aggregator prints VOID with the number found, and refuses calibrations from two commits | §5 | `ci_calibration_local_check` |
| **isolation** | `FORBIDDEN` adds `V8_KEY`, `V8_REF`, `NO_V8`; the script's own key constant renamed `TRIPWIRE_KEY` | `calib_ci.py` docstring; proposal §1: isolation rests on the pinned script; the tripwire catches objects, not raw tuples | `ci_calibration_local_check` |
| **trigger** | — | proposal §2: the two path-filtered any-branch workflows; exactly one commit on the live `main` head, no PR, re-checked at launch | — |
| **A1–A4** | — | `AMENDMENT-PROPOSAL-V8-COUNT.md`: the engine-side mutant and no subclassing (A1); the representatives per shard split off as the site-pair count (A2); A3 and A4 measured on the mid-size analogue | `midsize_validation` (new step) |
| **validation step** | `l2config`: design-only profile `mid` (v8's dim, n, slices, sources and rates; ball(2); port (0, 0, −2)). `design/midsize_validation.py` (new step): the dry run at 128 shards, four real shards against the model's per-shard prediction, the overhead at mid sizes, A3, A4 | `LAYER2-PLAN.md` §3.6, §12; `FEASIBILITY-AND-REDESIGN.md` §3 | — |
| **feasibility** | — | `FEASIBILITY-AND-REDESIGN.md` (r5): the campaign ledger, K1's κ-independent failure, the review's levers (i)–(v), D1 no longer an escape | — |

## The owner's decisions of 2026-10-26 (amaybaum), folded into r5

| decision | edit |
| --- | --- |
| 24-hour ceiling: "Per complete experimental campaign, not per individual run" | `l2config` `budget.ceiling_status`, `owner_rulings.budget_ceiling.scope_ruling`; `LAYER2-PLAN.md` §3.5 |
| included costs: "Include calibration, count pass, primary run, mutant campaign, retries, and execution overhead"; "Record all measured compute time consistently, including failed jobs and retries." | `l2config` `budget.ceiling_scope`, `budget.campaign` (planned values with their status), the new placeholder `retry_allowance_runner_seconds`; `l2plan.ledger_spent`, `campaign_decision`, `campaign_components`; the estimate's launch decision is on the campaign total. New self-test L2-LEDGER; mutant M_ledger_skip_failed |
| v8 site-pair count: conditionally approved as a separate, strictly count-only diagnostic, after review of its exact implementation; not yet authorized to dispatch | new `code/l2sitepairs.py` (the algorithm and permitted outputs in its docstring; import, data-flow and stream guards; its own authorization; resource limits) and `SITE-PAIR-COUNT.md`; `l2plan` reads its file on v8 (`--site-pair-counts`), checked against N, Burnside and the module's digest. New self-test L2-COUNTONLY; mutants M_count_guard_off, M_count_validate_lax, M_count_v8_unrefused, M_count_drop_pair; `refusal_probe` (command line; forged file) |
| shard imbalance: "a genuine design blocker … investigate deterministic subdivision of heavy site pairs into smaller shards, maintaining exact accounting and reproducibility" | K1 above |
| the survivor cap from "a justified resource and completeness analysis" | K2 above |

## A finding made while implementing

The first version of the in-pair rule compared only the sorted site pairs of the group images. That is
wrong when an element carries j to i and i to another site a: the image's first site is then i, and its
slices decide before its second site. The correct rule requires t1 ≤ t2 when a > j and t1 < t2 when
a < j; the first version gave "all" and "none" for these pairs. The error showed on ball(3) (the t1 < t2
case occurs once among its 1,953 site pairs); on the toy and ball(1) the first version agreed with the
canonical-image test at every index. Burnside's equality
held on ball(3) despite the error; the canonical-image check of every site pair at four slice pairs (now
in L2-SHARDPLAN and `subdivision_bounds`) caught it. The rule and both checks are in r5; the mutant
M_count_inpair_order reintroduces part of the error and is killed.
