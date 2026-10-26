# NP-AVG-1 Stage 0 Layer 2: changes r3 → r4

r3 is the draft at `47cf942d`. Its independent review is `../../review/LAYER2-R3-REVIEW.md` at
`a782aa54`: ACCEPT WITH CHANGES, R1–R6, with a corrected statistic for the κ proposal. r4 applies
R1–R6 in place, as a WIP draft, and corrects `KAPPA-PROPOSAL.md` to the review's statistic. No
frozen file, no part of erratum E1 and no review file is changed. No workflow is added, and nothing
ran on v8's configuration class.

| item | edit (code) | edit (plan) | control and mutant |
| --- | --- | --- | --- |
| **R1**, scope of `statement_scope` | `l2merge.rule_T`: E1-T6's text under `statement_scope` only when the outcome is "L_A = L_G = 0"; "not applicable (outcome: …)" for `not_evaluated` and "L_A > 0 or L_G > 0". The toy `result.json` (outcome "L_A > 0 or L_G > 0", toy L_A = 15) is regenerated and no longer carries the statement | §4.1, §5, §8, §10, §13 item 5 | L2-T6 (all three outcomes, direct and through the merge); mutant M_scope_every_outcome (killed at L2-T6) |
| **R2**, the survivor cap | `l2config`: `survivor_cap_per_shard` moves into the profiles: an `OWNER-PLACEHOLDER` for v8, with no default, and 10 for the toy profile; `owner_rulings.survivor_cap` added. `l2enum` reads the profile's cap. `l2plan`: the survivor-gate term reads the owner's cap; on v8 it is "not computed (owner placeholder: the survivor cap)", with its coefficient per unit of cap. `l2merge`: `survivor_gates_incomplete` {flag, shards over the cap} in `result.json`; the 58 counts are reported complete | §3.3, §3.3a, §3.6 term 4, §4.1, §4.2, §5; PO-L2-15 extended; §13 item 4 | L2-MRG (a cap-exceeded run is INCOMPLETE, with 58 counts and the flag); L2-PLACEHOLDER (the v8 cap is a placeholder, and v8 startup is refused at item 1) |
| **R3**, `index_of` checked in-run | `l2enum.Shard.index_check`: `record_at(index_of(m)) == m` for every member whose C7 sample membership is evaluated; new gate `index_roundtrip`, VOID in the merge | §3.3 table, §3.3a; PO-L2-19's status | new L2-IDXRUN (312 members on toy orbits, all pass; a planted off-by-one index fails all 312; the merge gives VOID); mutant M_index_check_off (killed at L2-IDXRUN) |
| **R4**, PO-L2-7 | — | PO-L2-7: "Re-reviewed (`LAYER2-R3-REVIEW.md` §3): valid under E1-T1, E1-T5 and E1-T4's four facts; standing E1-T6's" | — |
| **R5**, cost-model honesty | `l2config`: `gate_overhead_factor_status` labels overhead = 2 as an unmeasured judgement; `l2plan` prints the label in the closures formula and in `cost.overhead_factor`. New `design/overhead_measure.py` (step `overhead_measure`, toy geometry only, bounded): Shard.rep time against four bare closures, on every toy orbit and 120 planted records | §3.6 (overhead labelled; the measurement, about 2.9; "the model is not validated": the toy comparison, a predicted C7 term of 191 s and a known total of about 2,200 s against about 9 s of actual shard time); §12 ("κ above about 1.18 does not fit S7" marked as holding under the cost model) | the measurement is retained in `design/overhead/` (timing data) |
| **R6**, §13 | — | §13 item 7 added (the κ timing, an open owner sequencing decision, with the review's resolution); item 4 marked as an owner decision under R2; item 5 marked fixed by R1 | — |

## The owner's rulings of 2026-10-26 (amaybaum), folded into r4

| ruling | edit |
| --- | --- |
| κ: "Approve the proposed method, κ = u_cal × u_model, but not a final numerical value." | `l2config`: `budget.kappa` is replaced by `budget.kappa_rule` {method, u_cal: OWNER, u_model: OWNER}; `l2plan.kappa_from_rule` (u_cal × u_model, rounded up to one decimal) is the only source of κ. No κ value anywhere |
| calibration: "Require at least 20 independent timing calibrations on the relevant CI runner class." | `ci/calib_aggregate.py` refuses fewer than 20; the proposed workflow runs 20 |
| model uncertainty: "Retain as an explicitly judgment-based factor, subject to sensitivity analysis." | u_model a placeholder; `KAPPA-PROPOSAL.md` §c: the sensitivity table for u_model 1.0–1.5 at u_cal 1.25 and 1.35, with κ and the launch inequality |
| sequencing: "Approved. Fix κ, the survivor cap, and budget ceiling before any v8 count." | §3.5, §4.2; §13 item 7 recorded as decided; G_D and O1 after the count, before the full run |
| survivor cap: "Request a reasoned proposal based on shard distribution, memory consumption, and failure probability; do not use the placeholder 10." | the v8 cap stays a placeholder; new `SURVIVOR-CAP-PROPOSAL.md` (proposes 16) with `design/survivor_cap_measure.py`: memory and time per retained survivor on planted sets, exact uniform-shard and concentration-model P(cap exceeded), cost per unit of cap |
| budget ceiling: "24 hours maximum, including all run overhead, with an explicit reserve." and "If the calibrated runtime exceeds 24 hours, the experiment must be reduced through a new reviewed design or declared infeasible under this budget — not run with an artificially smaller margin." | `l2config`: `budget.runner_hours = 24` (owner-fixed), `budget.reserve_runner_seconds` (OWNER; `KAPPA-PROPOSAL.md` §d proposes 3 h); `l2plan.launch_decision`: launch iff κ · total + reserve ≤ ceiling and every job fits, otherwise "not undertaken for cost"; κ never changed. New self-test L2-LAUNCH; mutants M_launch_fit_kappa and M_launch_no_reserve |
| G-D and O1: decided after the count, before the full run | `owner_rulings.G_D`, `O1`; §4.2 |
| CI calibration, authorized conditionally | new `ci/`: the workflow `np-avg-1-stage0-planted-calibration.yml` (push to a dedicated branch only; 20 calibrations; limits stated), `calib_ci.py` (engine definitions executed from hash-checked sources; no v8-capable name; tripwire, fail closed), `calib_aggregate.py`, `CI-CALIBRATION-PROPOSAL.md` (trigger mechanics and trade-offs, limits, review checklist). Not under `.github/`, not launched. Local check `design/ci_local_check.py` |
| the v8 count-only pass: unauthorized pending its amendment and review | new `AMENDMENT-PROPOSAL-V8-COUNT.md`, unadopted |

## The κ proposal (`KAPPA-PROPOSAL.md`), corrected to `LAYER2-R3-REVIEW.md` §6 and the rulings

- **u_cal's statistic** is now the 99th percentile of the ratio between two independent calibrations.
  `kappa_calibration.py` computes it over every ordered pair of the 10 local calibrations. Three local
  repeats gave 1.21, 1.29 and 1.37 (the last retained). This instability at n = 10 is evidence for the
  owner's requirement of at least 20 runner-class calibrations.
- **The change of the provisional value from r3's 1.5 to about 1.6** came from the corrected statistic,
  not from any budget fit. The owner has since ruled the method only, so no value is proposed.
- **u_model** stays a labelled judgement, with the sensitivity table.
- **The infeasibility finding is conditional on the cost model.** Under it, no u_model in 1.0–1.5 fits
  the ceiling with the proposed reserve, before C7's sets 2 and 3.
- **The decision sequence** is the review's, with the owner's rulings.

## Evidence

`l2run.py` re-run in full (bounded, local): 24 steps, all exit 0, every deterministic step `-O`-identical.
- **Self-test:** 36 cases.
- **Quick campaign:** 51 of 51 killed at their named cases (17 rule, 34 machinery mutants).
- **E1-check replay:** byte-identical to `e1_check.out`.
- **New steps:** `overhead_measure`, `survivor_cap_measure` and `ci_calibration_local_check`.
- `RUN-MANIFEST` is regenerated and records the `ci/` files.
