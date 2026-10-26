# NP-AVG-1 Stage 0 Layer 2: changes r2 → r3

r2 is the draft at `4a51c675` (`CHANGES-L2-r2.md`). r3 implements erratum E1
(`../amendments/E1-LAYER1-ERRATUM.md`), in effect under `../LAYER1-FREEZE.md`, in place, as a WIP
draft. The follow-ups E1's drafter listed are in `../amendments/E1-CHANGES-r2.md` ("Layer 2
follow-ups the revision implies"). No frozen file and no part of E1 (including `E1-check/`) is
changed, no workflow file is added, and nothing ran on v8's configuration class: no v8 closure, no
grant for v8, and no shared-tip or F_G count on v8.

## E1 items

| E1 item | edit (code) | edit (plan) | control and mutant |
| --- | --- | --- | --- |
| **E1-F3**, C7's scope | `l2enum`: C7 runs per record on sets 1–4 (`Shard.c7_orbit`, `c7_record`): every member of every orbit, both conventions; R's direct production closure against the full `s0ref` closure in R's own context, and R's carried result against its direct closure; per-set coverage (records checked and failed, orbits touched, sum of their sizes, skipped beyond the cap); the rep-level shared-tip C7 of r2 is removed. `l2plan`: the closure-free predicates (`Space.q0`, `frame`, `in_out`, `c7_flags`; `shared_near`, `g_cone`, `all_tips`) and the record index (`Space.index_of`). `l2config`: `C7_samples` (streams `C7_H100`, `C7_H1000`, rates 100 and 1,000, on both profiles), `C7` (sets, `reference_form = full_s0ref`), `C7_scope = E1-F3`. `l2merge`: sums `C7_scope_coverage` | §3.3, new §3.3a; §4.1 readings; PO-L2-16, PO-L2-17, PO-L2-19, PO-L2-22 | L2-C7COV, L2-SCOPE, L2-INDEX, L2-F1, L2-F2; M_C7_set2_computed (killed at L2-F1), M_C7_carried_only (L2-F2), M_C7_sample_rep_index (L2-C7COV) |
| **E1-F3**, the G-D form | not implemented: the full `s0ref` closure is the only reference form | §3.3a, §4.2 (owner decision `G_D`), §13 item 2 | L2-PLACEHOLDER (reference form, placeholder) |
| **E1 §9**, O1 | E_G is not a check set; it is reported for information on the toy profile | §3.3a, §4.2 | L2-PLACEHOLDER |
| **E1-T1** | `l2s1a`: `L_bound_rule`; `l2merge.rule_T_inputs` reads the L3′ fields; `rule_T.L_reported_L3` is separate | §3.4, §4.2, §8 | L2-T1; M_ruleT_reads_L3 |
| **E1-T2**, σ | `l2s1a`: `L_reference` (case 2 (d), by `l2refcheck.ref_linked_counts`, `s0ref` only), `L_reference_L3_differs`, `fixed_in_log`, `L3prime_within_L3`. `l2merge.sigma` derives σ from those fields, cases 1–4 in order; every holding condition enters the label's reason lists; `rule_T_record` records the outcome beside a non-passing label with no S1b proposal | §3.4, §3.7, §4.3 rewritten to E1-T2, §8; PO-L2-18 | L2-SIGMA (ten conditions), L2-PREC, L2-2D; M_ruleT_ignores_sigma, M_sigma_overrides_label, M_proposal_on_failed_label, M_sigma_no_2d |
| **E1-T3** | `rule_T.cost_clause` from `l2config` | §8 | — |
| **E1-T5** | unchanged code (quantity's cone); reference recomputation added | §4.2, §8 | L2-T5 (toy L3′ bound, L_G = 7); M_LG_tip_reading |
| **E1-T6** | `l2config.rule_T.zero_text`: E1-T6's text verbatim; `rule_T.statement_scope` in every outcome; `wording_status` confirmed with qualification | §8, §4.1 | L2-T6 (verbatim against the erratum) |
| **E1-F6**, 58 counts | `l2analysis.reported_count_keys` (58), `ADDED_E1_F6`; `member_contributions` takes the two flags; `l2enum.Shard.flags`; `l2plan.Space.masking_key`, `masking_class_count`, `masking_equivalent_record`; `l2merge` reports 58. `count_keys()` stays the r5 list of 54, which E1-check part B reads | §3.2, §3.7; PO-L2-5, PO-L2-20, PO-L2-21 | L2-COUNTS, L2-MASK (per record); M_counts_54; `crosscheck_toy_counts` (58) |
| **E1 §9**, κ | `l2config.budget.kappa` and `owner_rulings.kappa` stay OWNER placeholders with no default; the estimate states its reasons | §3.5, §3.6, §4.2 | L2-PLACEHOLDER; M_placeholders_ignored |

## The follow-ups of `E1-CHANGES-r2.md`

| follow-up | where |
| --- | --- |
| replace the C7 scope placeholder with sets 1–4, F_G per record and closure-free, direct production and reference closures per record, per-set raw and orbit coverage, record-index samples on `C7_H100` and `C7_H1000` | §3.3a; `l2enum`, `l2plan`, `l2config` |
| add σ case 2 (d), and record rule T's outcome beside a non-passing run label | §4.3, §8; `l2s1a`, `l2refcheck`, `l2merge` |
| add `rule_T.statement_scope` | §8; `l2config`, `l2merge` |
| have the dry run report \|F_G\| and the C7 cost term | §3.6: on the toy profile (595 records, 283 orbits); on v8 "not computed (requires authorization)", with the C7 term as a formula (§13 item 1) |
| add the self-tests and the computed-closure mutant named in E1 §10 | §10; 14 new self-test cases and 12 new machinery mutants |
| align `LAYER2-PLAN.md` §4.3 with E1-T2 | §4.3 |
| extend the count keys to 58 | `l2analysis`, `l2merge` |

## Other edits

- **Refusal of v8 record enumeration.** `l2plan --shared-tips` is refused for v8 before anything is
  computed; `refuse_v8_enumeration` is the first statement of every enumerating function and of the
  record generator (PO-L2-23; L2-V8COUNTS; `refusal_probe`).
- **Pre-flight `C12_universe`** also requires `l2plan`'s frame, from which C7's closure-free sets are
  selected, to equal the production frame (PO-L2-17).
- **The cost model** (§3.6): C7 per record over sets 1–4 as a formula with coefficients; per-term
  formulas in `dryrun.json`; S1a's term includes the case 2 (d) pass; "not computed" in place of any
  value that needs an uncomputed input; the dry-run schema is `dryrun/2`.
- **Shard schema** `shard/3` (`C7_scope_coverage`).
- **`l2selftest --only`**, and the quick campaign runs each machinery mutant against its named case
  only; the full campaign runs every case.
- **Design evidence**: `crosscheck.py` compares 58 counts (the four added against an independent
  per-record computation with `code-r5/s0ref.py`); `planted_shard.py` checks set-1 C7 and N_ST on
  the planted orbits; `refusal_probe.py` adds the v8 `--shared-tips` refusal; new
  `e1check_replay.py` (E1-check against r3, output identical to `e1_check.out`) and
  `kappa_calibration.py` (timing repeats for `KAPPA-PROPOSAL.md`).
- **`KAPPA-PROPOSAL.md`**: advisory, for the owner; no κ value is written into code or configuration.
