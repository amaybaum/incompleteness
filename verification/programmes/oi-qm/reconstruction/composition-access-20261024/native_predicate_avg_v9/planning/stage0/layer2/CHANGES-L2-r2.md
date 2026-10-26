# NP-AVG-1 Stage 0 Layer 2: changes r1 → r2

r1 is the draft at `99a9797e`. Its review is `../../review/LAYER2-REVIEW.md` at `a63db7ba` (ACCEPT
WITH CHANGES). r2 applies L2-R1 to L2-R8 and the accepted part of L2-R9, in place, as a WIP draft.
The owner rulings (T1, T2, T5, F3, κ, F6) are left as `OWNER-PLACEHOLDER` values; no frozen Layer-1
file is changed, no workflow file is added, and nothing ran on v8's class.

| item | edit (code) | edit (plan) | control and mutant |
| --- | --- | --- | --- |
| **L2-R1** witness cap | `l2enum`: the first-100 candidate list is replaced by `Shard.add_witness`, a running minimum by the C16 key with a count of candidates seen; candidates come from every directly closed orbit (survivor, flagged, sampled), each confirmed on direct results. `l2merge.minimal_witness` takes the minimum of the shards' minima | PO-L2-10 restated in the review's words, with "follows from PO-L2-3" struck and the unproved part stated (§9); §3.3 | L2-WIT (300 candidates, random order); mutant `M_witness_first` (keeps the first candidate) |
| **L2-R2** every survivor | `l2enum`: `Shard.ref_gates` and `Shard.member_ref_gates`; on survivor orbits C0, C7, C11 (i), C17 and C18 run on every member, both conventions, with the member's own reference context and direct closure; non-survivor orbits keep the representative's shared-tip and sampled gates | §3.3; new PO-L2-14 (survivor-gate coverage, with what remains assumed) | L2-SURV (planted block orbit: 4 members × 2 conventions); `planted_survivor_path` (16 per gate); mutant `M_survivor_rep_only` |
| **L2-R3** no silent truncation | `l2enum`: survivor cap `survivor_cap_per_shard` (configuration), `survivor_representatives`, `survivor_cap_exceeded`; detail written for every gated survivor representative. `l2merge.residue_complete`: INCOMPLETE unless every shard lists one detail per counted survivor representative and did not exceed the cap | §3.3, §3.7; new PO-L2-15 (residue completeness) | L2-MRG cases `residue_truncated`, `survivor_cap_exceeded`, `residue_complete`; mutant `M_residue_ignored` |
| **L2-R4 a** lock wording | `s0geom`, `s0ref`, `l2auth` docstrings: "no file in the repository other than `l2auth` constructs a grant (static check L2-S1); a grant can be forged in-process, so the lock prevents accidental runs, and the authoritative gate is the CI owner-check job and the post-hoc verification" | §7 | L2-S1 |
| **L2-R4 b** echo | `l2cert.startup` records `ci_run` (`GITHUB_RUN_ID`, attempt, repository, workflow); `preflight.json`, every shard and `result.json` echo the decision, artifact, full owner check and CI run | §5, §7 | (fields; checked by certificate item 6 for v8) |
| **L2-R4 c** landing | new `l2landing.py`: compares the designation re-fetched from the host (`fetched.json`) with the echo; certificate item 6 records the landing check as required for v8 | §6, §7, §11 | L2-LAND (accepts the unchanged designation; refuses another author, a changed body, another comment, a missing line, no CI run, no owner check) |
| **L2-R4 d** digest binding | `s0geom.bind_running_digests` and `_granted`; `s0ref.bind_running_digests`, `RefGrant(commit, code_digest, config_sha256)` and `_ref_granted`; `l2cert.startup` binds after manifest verification; nothing bound → every grant refused; rebinding to other values refused. L2-S1 also checks that only `l2cert` (and the self-test) binds | §2, §7 | L2-GUARD (forged grant refused unbound and bound; rebinding refused); `refusal_probe` runs the review's forgeries as controls (9 of 9 refused); mutant `M_grant_unbound` |
| **L2-R5** commit binding | `l2cert.commits_consistent`: `preflight.json`, `s1a.json` (and `-O`), every shard (and `-O`) and `result.json` record one commit, equal to the authorization's for v8; items 2 and 7 require it; item 7 requires a clean tree for v8. `preflight`, `s1a` and shards record `tree_clean` | §6, §12 (commit caveat); `RUN-MANIFEST` records HEAD and tree state | L2-CERT, including the r1 toy certificate's case (pre-flight at another commit); mutant `M_commits_unbound`. A dev replay with the r1 `preflight.json` (commit `217f7a40`) against r2 files at `a63db7ba` now fails items 2 and 7 |
| **L2-R6** complete estimate | `l2plan.estimate`: terms for closures, sampled gates, the C7 term per candidate scope (from `--shared-tips` when run; always as seconds per percent of representatives), the capped survivor-gate bound, pre-flight, merge and S1a; per-job estimates; `launch_within_budget` computed from the complete estimate under κ, `null` with its reason while κ or the scope is a placeholder | §3.6, §12 | toy dry run carries every term including C7 by scope; v8 estimate states the C7 term as pending |
| **L2-R7** launch margin | `l2config`: `launch_if_estimate_at_most_*` removed; `budget.kappa = OWNER-PLACEHOLDER`, with the rule κ · total ≤ budget and κ · job ≤ timeout | §3.5, §13 (F9) | `l2cert.startup` refuses v8 while κ is a placeholder |
| **L2-R8** S1a L3 bound | `l2refcheck.tipset`, `c17_stream` and `c18_stream` take `near_only`; `l2s1a` reference-checks the L3 bound with near tips and the L3′ bound with near and far tips (schema `s1a/2`) | §3.4, PO-L2-12 | toy S1a: both bounds pass |
| **L2-R9** readings | `l2config.CONFIG['accepted_readings']` (F1, F4, F5, F7, F8, F10, F11, citing the review) and `CONFIG['owner_rulings']` (T1, T2, T5, F3, κ, F6 as placeholders with the reading in force); `result.json` echoes both; `l2cert.startup` refuses v8 while any placeholder remains; the v8 profile's C7 scope is a placeholder, the toy profile keeps the literal reading to exercise the path | §4.1, §4.2, §4.3, §8, §13 | — |

**Other edits.**
- Survivor cap `survivor_cap_per_shard = 10` (configuration, with its basis), and pre-flight and
  merge allowances (300 s each), stated in `l2config`.
- `l2run.py`: calibration runs before the toy dry run, which now carries the complete estimate with
  the shared-tip count; the manifest records HEAD and tree state and the commit caveat.
- Shard schema `shard/2`, S1a schema `s1a/2`.

**Quick mutant campaign.** 17 rule mutants and 18 machinery mutants (13 from r1, plus
`M_witness_first`, `M_survivor_rep_only`, `M_residue_ignored`, `M_commits_unbound` and
`M_grant_unbound`), each with its named case; results in `design/toyrun/mutant-campaign.json`.
