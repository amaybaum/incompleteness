# Independent review: NP-AVG-1 Stage 0 Layer 2 r3 (exact commit `47cf942d`), and the κ proposal

**Object.**
- `stage0/layer2/` at `47cf942d1bc53f6192a34b3b6aae779b557807ea`:
  - `LAYER2-PLAN.md` (SHA-256 `62aa38ba…b2f5`, 908 lines), `CHANGES-L2-r3.md`,
    `KAPPA-PROPOSAL.md` (advisory);
  - `code/`;
  - `design/`, with `RUN-MANIFEST`, `runs/`, `toyrun/` and `kappa/`.
- Read against Layer 1 (r5, frozen at `f33d8d63`), erratum E1 in effect (`53786e6e`), and my
  `LAYER2-REVIEW.md`, `E1-ANALYSIS.md` and `E1-RECHECK-r2.md`.

**Read-only. Nothing on v8.** No closure, grant or record enumeration was run on v8. My replay and
probes are in `S/npavg/review-l2r3/`.

## Verdicts

**Layer 2 r3: ACCEPT WITH CHANGES.**
- **Fidelity.** It implements E1 faithfully: C7 per record on sets 1–4 under both conventions,
  closure-free set 2 under G, record-index samples, direct production plus full `s0ref` closures,
  no substitution by representatives, coverage reporting, σ with 2 (d) and its precedence, and 58
  counts.
- **Placeholders.** κ, G_D and O1 have no default. G-D is absent, and v8 is refused.
- **Replay.** Every deterministic output replays.
- **Required changes.** Six bounded changes, R1–R6.
  - One fixes a substantive overstatement: `rule_T.statement_scope` asserts the zero-branch
    geometric fact in runs whose outcome is the other branch, including the committed toy result.
  - One concerns a resource constant, the survivor cap, which acts as an unflagged owner decision.

**The κ proposal: sound in structure, not yet sound in its statistic, and the decision sequence
needs two corrections.**
- **The rule is right:** κ = u_cal × u_model, fixed before the count. u_model is labelled as a
  judgement, and the arithmetic is correct.
- **u_cal uses the wrong statistic** (max/median of single draws). The ratio statistic is
  borderline at 1.2.
- **The infeasibility finding is relative to the model.** It holds only relative to a cost model
  whose largest term carries an unmeasured overhead of 2. The only actual-against-estimate
  comparison available, on the toy class, over-predicts by roughly 20×.
- **Recommendation:** fix a κ *rule* now, before any count, not a tuned value (§6).

## 1. Replay (task 4)

`l2run.py` was re-run on a scratch copy of the planning tree at `47cf942d`: exit 0, 10 minutes.
The code hashes equal `RUN-MANIFEST`.

| step | result against `runs/` |
| --- | --- |
| manifest_verify, l2_selftest, dryrun_v8_plan_no_closure, preflight_toy_quick, mutants_quick, s1a_toy, merge_toy, crosscheck_toy_counts, e1check_replay, code_r5_equivalence_quick, planted_survivor_path, refusal_probe_v8 | **byte-identical** |
| shard_toy_0…3, s1a/shard/result/preflight JSON | equal apart from `commit`, `head`, `tree_clean` and the digests that hash them |
| calibration_planted, dryrun_toy, dryrun_v8_estimate, kappa_calibration_repeats | timing-dependent, as declared |
| certificate_toy | exit 2 in my copy: items 2 and 7 fail on the commit binding, because the copy is not a git repository. This shows the binding fails closed. The committed certificate holds, with HEAD `53786e6e` and `tree_clean = false`, which is the declared commit caveat |

**What the replay confirms.**
- **The self-test:** 34 of 34.
- **The quick campaign:** 47 of 47 killed at their named cases (17 rule, 30 machinery), with the
  unmodified suite clean first. The demonstrations fail C11 only.
- **The 58-count cross-check:** equal, with 36 counts identically zero on the toy class.
- **The E1-check replay:** byte-identical to `e1_check.out` (`d2297fb7…8542`).
- **The commit caveat stands:** the evidence ran on an uncommitted tree at `53786e6e`. It is
  acceptable for design evidence, and the plan's freeze procedure (§14) regenerates it at the freeze
  commit.

## 2. Fidelity to E1 (task 1)

| E1 requirement | r3 | verdict |
| --- | --- | --- |
| C7 per record on sets 1–4, both conventions (E1-F3) | `Shard.c7_orbit`: every member of every orbit, each convention; `c7_record` computes the member's direct production closure, the full `s0ref` closure in its own context, C0, and carried against direct | faithful |
| set 2 closure-free under G | `l2plan.Space.c7_flags`: F_G from Q⁰ and the frame, with its own cone and tip code; `c7_set2` = (T_G ∩ Surv_G) ∪ F_G; T_A under A | faithful; L2-SCOPE agrees with `s0ref` on every toy record |
| record-index samples | `c7_sampled` on `index_of(member)`, streams `C7_H100` and `C7_H1000`; non-representatives included (L2-C7COV) | faithful (but see R3) |
| full `s0ref` reference; G-D absent | `C7.reference_form = full_s0ref`; no G-D code path exists | faithful |
| no substitution by representatives | `c7_record(m)` uses the member; M_C7_carried_only and M_C7_sample_rep_index killed | faithful |
| coverage reporting, raw and orbit-level | `C7_scope_coverage`: records checked and failed, orbits touched, sum of sizes, skipped beyond cap; equals E1-check part J on the toy class | faithful |
| σ with 2 (d); precedence; rule T beside a non-passing label (E1-T2) | `l2merge.sigma`, `label`, `rule_T_record`; L2-SIGMA, L2-PREC, L2-2D; four mutants killed | faithful |
| E1-T1, T5, T3 | L3′ inputs, with L3 reported; quantity's cone; cost clause "not evaluable" | faithful |
| E1-T6 | `statement_scope` carries the text verbatim | **not faithful in scope** (R1) |
| 58 counts (E1-F6) | `reported_count_keys` (58); merge reports 58; `crosscheck` | faithful |
| rulings in `l2config` | T1, T2, T5, T6, F3 and F6 recorded with E1 wording | faithful |
| κ, G_D, O1: no default | each `OWNER-PLACEHOLDER`; `placeholders()` lists exactly these; `startup` refuses v8 while any remains | faithful |
| v8 start refused | `refusal_probe` replays (9 of 9 entry points and 9 forgeries refused; `--shared-tips` on v8 refused); my lock probe: default, `True`, subclass, duck-typed, malformed and forged-zero-digest grants all refused; `decide()` still accepts fabricated inputs, the documented limit closed by the landing check | faithful |

**R1. `statement_scope` overstates.** E1-T6 defines the *zero branch's* text and says `result.json`
records it under `rule_T.statement_scope`. r3 records that text "in every outcome". The committed
toy `result.json` has outcome "L_A > 0 or L_G > 0" (L_A = 15) together with `statement_scope`:
"No record … has a linked survivor under the specified closure …". In that branch the statement
is not established, and read naively it is asserted. That is a claim/evidence overstatement in a
structured output (Code Review Rules). It is §13 item 5, and E1 does not support this reading.

## 3. Proof obligations (task 2)

| PO | verdict |
| --- | --- |
| PO-L2-7, re-reviewed under E1's fixed readings | **Valid.** Nesting, from L1 §1; PO4 monotonicity with a record-independent G frame, from L1 §2; seed-tip status intrinsic, by PO7; L_A over the L3′ bound (E1-T1); L_G by the quantity's own cone (E1-T5). Every linked survivor of any finite item set over Reg × {−1, …, 23} is counted. Its standing is E1-T6's. The status "Not re-reviewed in r3" should now read "re-reviewed: valid" (R4) |
| PO-L2-13 (extended) | Honestly toy-only for the C7 populations. N and Burnside on v8 are confirmed independently |
| PO-L2-16 (C7 per record) | **Valid by construction:** orbit-once processing (PO-L2-2), every member, both closures for the member itself. The cap exception is stated, and makes the run INCOMPLETE. The "not claimed" clause is correct |
| PO-L2-17 (set 2 closure-free) | **Valid.** The equality is E1's Lemma G-D; closure-freeness holds by construction; the frame is tied to production by pre-flight `C12_universe`. The per-record predicate on v8 is checked only through the frame equality. Acceptable, because `c7_flags` is a third independent implementation, and a disagreement on v8 would surface only as a scope difference, not as a wrong verdict |
| PO-L2-18 (σ) | **Valid by construction.** The certification argument is E1-T2's, with the partition invariant cited |
| PO-L2-19 (`index_of` inverts `record_at`) | **Proved** as a closed form, checked on the toy class only. On v8 a defect would silently change *which* records are sampled, with no failure (R3) |
| PO-L2-20 (per-record masking equivalence) | **Valid** (PO-L2-6's canonical form); brute-force checked on three toy variants |
| PO-L2-21 (four added counts preserved) | **Valid given PO-L2-3.** C8 compares them on directly closed orbits |
| PO-L2-22 (samples deterministic over record indices) | **Valid by construction**, given PO-L2-19 |
| PO-L2-23 (no v8 record enumeration) | **Valid by construction.** L2-V8COUNTS uses a sentinel, so a missing refusal is detected without enumerating |
| PO-L2-14 (survivor coverage) | **Valid as scoped.** A member that would be a survivor under direct closure in a collapsed-representative orbit is reached only by C8's 1-in-100 sample and C7's record-index samples. It is honestly stated |

**The table is complete** for r3's new behaviour, with one gap. No obligation states that the
survivor cap is a resource constant fixed before results (R2).

## 4. The seven ambiguities (task 3)

| # | point | verdict |
| --- | --- | --- |
| 1 | \|F_G\| on v8 needs a record enumeration, which is not authorized | Correct; Layer 2 is right to refuse. E1-F3's checkpoint is met on the toy profile only. **Owner decision:** authorize a combinatorial-only count, which needs a Layer-2 amendment adding a grant-gated count path that imports no engine, with its own review. |
| 2 | the G-D self-test in E1-F3's checkpoint while G-D is non-executing | Acceptable. The equivalence check is E1-check part H, replayed byte-identically in Layer 2's evidence (`e1check_replay`). No amendment needed. |
| 3 | "computed closure" = the carried result for set membership | Acceptable. On every directly closed orbit, and on every C7 scope record, carried against direct is compared and fails VOID, so the reading cannot hide a failure there. The residual is PO-L2-14's, and it is stated. |
| 4 | survivors beyond the cap → INCOMPLETE | **Acceptable as fail-closed, but the cap needs an owner decision (R2).** The cap (10 orbits per shard, about 2,560 records per convention) decides whether a survivor-rich outcome can reach any label other than INCOMPLETE, and it sets the survivor-gate cost term. That makes it a resource constant of the same kind as κ. Layer 2 should not set it. It biases only towards "no result" (never towards collapse), and the 58 counts are still complete. But an INCOMPLETE run must say so explicitly, and must report the complete counts (R2). |
| 5 | `statement_scope` in every outcome | **Not acceptable** (R1). |
| 6 | σ case 1 (a): an output lacking a field σ reads | Acceptable (fail-closed; a malformed output is a missing output). |
| 7 | κ timing: my advice was κ before the complete estimate; E1 §9 has the G-D confirmation "taken together with κ once the dry run reports \|F_G\|" | **A real tension, resolved by an owner sequencing decision.** κ is a margin on the error of the estimate and must not depend on \|F_G\| (otherwise it can be fitted). The G-D confirmation is a cost decision that needs \|F_G\|. The owner should record that κ (or κ's rule, §6) is fixed *before* any v8 count, and that the G-D confirmation follows the count. E1 §9's phrase is in its "open decisions" section, so a recorded owner decision suffices. If the owner prefers the text to match, a one-line append-only E2 does it. |

## 5. The cost model behind both the launch rule and κ

- **The model is consistent with L1 §10's arithmetic.** Its largest term, the closures term of
  about 59–65k s, contains `overhead = 2`, an unmeasured allowance for analysis and member
  attributes.
- **It is untested against any real run of comparable size.** The one actual-against-estimate
  comparison available is the toy run, where the same model predicts a C7 term of 191 s and a
  known total of 2,197 s. All four toy shards, with every gate at rate 1 and C7 on 608 records,
  ran in about 9 s, and the whole toy pipeline in minutes. Toy contexts are small (m ≤ 8), so this
  over-prediction does not transfer to v8. But it does show that the model is not validated in
  either direction.
- **Two consequences:**
  - "S7 cannot admit κ > 1.18" is true *of the model* (86,400 / 72,977 = 1.184; 1.02 at the
    slowest calibration). It is not yet a fact about the run.
  - κ is meant to cover the estimate's error, yet the estimate itself embeds an unmeasured factor
    of 2. κ and `overhead` must not both be judgements stacked on the same unknown.
- **The fix (R5).**
  - Measure `overhead` on planted orbits, as the ratio of shard work to bare closures. This can
    run on the toy and planted profiles, with no v8.
  - Disclose the toy over-prediction in §3.6 and §12.
  - Treat model error explicitly in κ (u_model), not twice.

## 6. The κ proposal (task 5)

**Is u_cal's statistic sound? Partly.**
- **The data** (`design/kappa/calibration-repeats.json`, which I re-read): known terms plus set 4
  over 10 calibrations, median 72,977 s, sample CV 6.1% (5.8% as computed in the file),
  max/median 1.161, min/median 0.962, **max/min 1.206**. The distribution is right-skewed by one
  value (84,718 s, a `-O` run).
- **The relevant quantity.** At launch, *one* calibration on the CI runner produces the estimate,
  and the run itself is a different draw. The ratio actual/estimate is a ratio of two
  approximately independent draws. With the observed spread (log-σ ≈ 0.06), its 99th percentile
  is about e^{2.33·√2·0.06} ≈ 1.22. The empirical analogue is max/min = 1.21.
- **The proposal's statistics answer a different question.** "Max/median 1.161" and "the maximum
  exceeds one further draw with probability 10/11" concern a draw against the median, not a draw
  against another draw. u_cal = 1.2 sits just *below* the ratio statistic.
- **Limits:**
  - n = 10 on one machine;
  - normal and `-O` calibrations are pooled, though the paired `-O` ratio has median 0.994, so
    pooling is defensible;
  - CI-runner variance is not measured.
- **Verdict.** Directionally right, but u_cal should be defined as a stated quantile of the ratio
  of independent calibrations, measured on the runner class with n ≥ 20 (step 2 of the proposal),
  not as max/median of single local draws.

**Is u_model transparent and labelled? Yes.** "This factor is a judgement, not a statistic", with
replacement by measurement proposed. It must not double-count with `overhead = 2` (§5).

**Is the "κ ≤ 1.18 even at zero" finding correct?** Arithmetically yes, relative to the model and
the median calibration. As a statement about the real run it is conditional on the unmeasured
`overhead`, the survivor-cap term at m_max, and the pre-flight and merge allowances (§5). It should
be presented as model-conditional.

**Is the decision sequence sound?** Mostly. Its core is right: κ before any count, never fitted.
Two corrections are needed:
- **S7 is placed last**, after the complete estimate. The budget then becomes whatever the
  estimate needs, which is a fit even when κ is fixed. The owner should declare a
  willingness-to-pay ceiling B_max *before* the count. If κ · total > B_max, the enumeration is
  "not undertaken for cost", unless the owner raises B_max by a recorded resource decision, with κ
  unchanged.
- **The E1 §9 tension** (§4 item 7) must be resolved by a recorded sequencing decision. The survivor
  cap (R2) belongs in the same pre-count decision set.

**What I recommend the owner decide, in order. No decision depends on a v8 number unless it says
so.**
1. **Fix the κ rule now**, not a fitted value: κ = u_cal × u_model, where:
   - u_cal is the 99th percentile of the ratio of two independent calibrations, estimated from
     n ≥ 20 calibrations on the CI runner class, with a provisional value of 1.25 from the local
     data (max/min 1.21, rounded up);
   - u_model is 1.25, an explicit judgement, which may be replaced only by a pre-declared rule from
     an authorized timing sample (step 6), and only *after* `overhead` is measured, so that the two
     are not stacked.
   Under the provisional values κ = 1.25 × 1.25 ≈ 1.6 (1.5625, rounded up to one decimal). That is
   not the drafter's 1.5. The difference comes from the statistic, not from any budget.
2. **Record the sequencing:** κ (rule), the survivor cap and B_max are fixed before any v8 count.
   The G-D confirmation and O1 follow the count. This settles E1 §9's "together with κ" (a recorded
   decision, or a one-line E2).
3. **Set the survivor cap** as a resource constant, with its reason (R2).
4. **Declare B_max**, the willingness-to-pay ceiling in runner-hours, replacing or confirming S7's
   24.
5. **Optional:** authorize the CI calibration dispatch (planted sets only) to measure u_cal on the
   runner class, and measure `overhead` (R5) locally.
6. **Authorize the combinatorial-only v8 count** of I_A, I_G, F_G and E_G, records and orbits,
   through a Layer-2 amendment that adds a grant-gated, engine-free count path, with its own review.
   The import trap I used on the dry run is a suitable control.
7. **With the counts:** decide G_D (cost only; it does not change any verdict) and O1 (coverage).
8. **Optional:** an authorized timing sample of real v8 closures, to replace u_model by its
   pre-declared rule.
9. **Complete estimate.** Launch iff κ · total ≤ B_max and κ · each job ≤ its timeout, with the
   normal and `-O` copies as separate replica jobs. Otherwise "not undertaken for cost".

None of these is tuned to make the budget fit: every margin and ceiling is fixed before the count
it would otherwise be fitted to.

## Required changes (Layer 2 r3)

**R1. Scope of `statement_scope`.** Record E1-T6's text under `rule_T.statement_scope` only when
the outcome is "L_A = L_G = 0". For any other outcome record `statement_scope: "not applicable
(outcome: …)"`, with the zero-branch text, if kept at all, under a field such as
`zero_branch_statement_if_applicable`. Update §4.1, §8 and L2-T6, and regenerate the toy
`result.json`.

**R2. The survivor cap is an owner-set resource constant.**
- Make `survivor_cap_per_shard` an `OWNER-PLACEHOLDER` (v8 profile; the toy profile may keep 10),
  listed with κ, G_D and O1, with no default.
- Add a PO, or extend PO-L2-15, stating that the cap affects only completeness, never a verdict,
  and that a cap-exceeded run is INCOMPLETE with the 58 counts reported complete and flagged
  `survivor_gates_incomplete`.
- Make the cost estimate's survivor-gate term read the owner's cap.

**R3. Verify `index_of` on v8 in-run.** For every record whose C7 sample membership is evaluated
(every member of every processed orbit), assert `record_at(index_of(m)) == m` in the authorized
run. A failure is VOID. The cost is negligible. This turns PO-L2-19 from toy-checked into checked
on v8.

**R4. PO-L2-7 status.** Replace "Not re-reviewed in r3" with "Re-reviewed (LAYER2-R3-REVIEW §3):
valid under E1-T1, E1-T5 and E1-T4's four facts; standing E1-T6".

**R5. Cost-model honesty.**
- In §3.6 and §12, label `overhead = 2` as an unmeasured judgement, and state the toy comparison:
  a predicted C7 term of 191 s and a known total of 2,197 s, against about 9 s of actual shard time
  (small m; no transfer to v8).
- Add a planted-profile measurement of `overhead`.
- Mark "κ ≤ 1.18" in §12 and in `KAPPA-PROPOSAL.md` as "under the cost model".

**R6. §13.** Add item 7, the κ-timing tension with E1 §9, with the resolution in §4. Mark item 4
(the cap) as an owner decision under R2, and item 5 as fixed by R1.

## Owner decisions

1. **The κ rule** (§6 step 1): recommended κ = u_cal × u_model, with u_cal a stated quantile of
   independent-calibration ratios (provisional 1.25) and u_model = 1.25, a labelled judgement.
   Fixed now, before any v8 count.
2. **Sequencing:** κ, the survivor cap and B_max before any count; G_D and O1 after (this resolves
   E1 §9's "together with κ").
3. **The survivor cap** (R2).
4. **B_max**, the budget ceiling, in place of deciding S7 after the estimate.
5. **The combinatorial-only v8 count** and the Layer-2 amendment it needs (§4 item 1).
6. **Later, with the counts:** G_D and O1.
7. **Unchanged:** no v8 execution, no full run, no CI dispatch and no full mutant campaign without
   separate authorization.
