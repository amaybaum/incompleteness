# Q-C2-1 (ARP-2-QC21): dispositions of r14c

WIP / UNVERIFIED. Model-written. Drafting record, not a control-plane artifact.

- **Input:** r14b, `preregistration.draft.md`, sha256 `57053e08a18f3357b86ea3956e88bbb1fb7a34c1d14fbd6b169ebbff8d1b65e1`
  (verified before the build; the build script checks it again), with `DISPOSITIONS-r14b.md` (`1703425b…`) and
  `IMPL-DELTA-r14b.md` (`9489f790…`).
- **Output:** `r14cwork/preregistration.r14c.md` (r14c), `r14cwork/IMPL-DELTA-r14c.md`, this file, the build script
  `r14cwork/make_r14c.py`, the diff `r14cwork/r14b-r14c.diff`, and the text check `r14cwork/check_rows_r14c.py`.
  Their sha256s are reported with this file, not in it. No file in `qc21/` outside `r14cwork/` was changed.
- **Work list:** `review/REVIEW-QC21-r14b.md` (`95dcec39762b648139a24626fd20b9b776dc6ceca5f5a0e93374efe0406d4765`),
  REVISE (minor): R14B-B1 to B3, N1–N9. Added by the coordinator: blocker Rc1 of the Q-C2-2 r14a review
  (`../qc22/review/REVIEW-QC22-r14a.md`, `c63ca1cc…`) and its note on host-time records.
- **Wording ported (read only):** Q-C2-2 r14 (`../qc22/r14/preregistration.draft.md`, `9e3ef0c9…`), lines 1538–1541
  (`order.json`), 1006 (arguments), 691–694 (APPROVALS) and 1741 (invariant row); Q-C2-2 r14a
  (`../qc22/preregistration.draft.md`, `d751a127…`) for N10 and the later shared-method changes (§3 below). No Q-C2-2
  file was changed.
- **Authority:** #1169 c.6740078002 (amaybaum, OWNER, 2026-11-09T12:29:10Z): revise the preregistration and plan
  script changes. Not authorized: the design run, the gate tests, `F`, dispatch, any computation.
- **Nothing was run** except text tools: the build script (exact string replacements), `diff`, the review's
  text-only probes `review/probes-r14b/v3_blocks.py` and `review/probes-r14a/control_p_coverage.py`, the row check
  `r14cwork/check_rows_r14c.py`, a line-width check and a phrase scan. One read-only `git` lookup confirmed
  `tools/v3_verifier.py`'s blob at `D` (`681c6737…`, sha256 `fc6545f5…`). No LP, stress test, script self-test or
  computation on any round instance. No repo, git or GitHub write.
- **Build:** `python3 -I r14cwork/make_r14c.py` checks r14b's and IMPL r14b's sha256s, then applies 45 and 11 exact
  replacements, each required to match once.
- **Line numbers** below are r14c's.

## Checks run on r14c (text only)

- **V3 blocks.** The `v3-round` and `v3-governed-paths` blocks are byte-identical to r14b's.
- **Control P's rule.** It catches 37 lines: r14b's 35, plus R10's two placeholders (1719, 1728). The 9 lines it
  skips only name the word, as in r14b.
- **Edit-log rows 109–126.** Each "copied text" fragment occurs in r14b, and each "becomes" fragment occurs in r14c.
  Row 118's "(none; added after S1-BIND)" is a marker, like row 77's.
- **Line width.** No added line is over 120 characters outside tables, apart from the title.
- **Register.** The added lines contain none of "now", "no longer", "formerly", "corrected" or "should not be read".

## 1. Blockers

| finding | change | r14c lines |
| --- | --- | --- |
| **R14B-B1** `F`'s designation is never read | **(i)** C.3's `order.json` rule now carries Q-C2-2 r14's 1538–1541 wording (row 113). The designation comment is read through `issues/comments/{DEC}`, with its id given as an argument. Its `created_at`, and its `updated_at` under the edited-comment rule, precede the first execution run's `created_at`. `order.json` records its id, author and times. **(ii)** C.8 item 9's arguments include `F`'s designation id, and both `order` and `verdict` read comments through the template. **(iii)** Rule (g)'s template note reads "read by `order`, `verdict` and `e-entry`" (row 120). **(iv)** A frozen control, **APPROVAL-ENTRIES**, in C.4 after S1-BIND (row 118). It carries Q-C2-2's 691–694 cases, the `E` entry, `e-entry` ≡ `verdict`, R8's cases under both options, and the R14-N2 cases (§3). It is named APPROVAL-ENTRIES, not APPROVALS, so that no copied control's name reads as a reference to `approvals` (*After the edits*). **(v)** Invariant rows 3752 and 3765 name the read and the control. **(vi)** IMPL: D20 and D21 are corrected, and D29 and D30 are added. **Necessary addition.** C.8 item 9 defines "the first execution run" (3338): the earliest-created run, of any event, whose `head_sha` is a round-branch commit after `F`. Without this definition `order` cannot evaluate the rule | 2462–2465; 3317–3320; 2915–2916; 2728–2738; 3338–3339; 3752; 3765 |
| **R14B-B2** R1 has no admissible value after a red run below `10^5` | R1, its alternative and C.8 item 2 all use the review's wording. After a red design run, the owner **may** fix a positive `S_max` no larger than the red run's, by a recorded decision before another design run. The value is at least `10^5` unless the red run's was at most `10^5`, in which case the same decision removes the floor. Under the alternative, the same rule applies with no floor. Some value is admissible after any red run, the red run's own value included, so neither a red run at `S_max = 1` nor one that was red for another reason forces a value. The `check --freeze` bullet (3165–3168) is unchanged and agrees. IMPL D24 is reworded | 1621–1633; 3222–3226 |
| **R14B-B3** R2's alternative is not implementable | **Form taken: A3 exits 0 at round-branch dispatches and records the red control.** The other form (`always()` on A4–A10 with A3 still exiting 3) fails at `E`: job A, the aggregate and the run would be red, and `E`'s run is `E`'s exact-head attestation (§A.39), which needs every job green. The alternative therefore states four things. **The checker:** the fixture exit rule is keyed on the existing `GITHUB_EVENT_NAME` and `GITHUB_REF` keys, so the checker exits 0 only in a `workflow_dispatch` run on the round branch, and exits 3 as before at the design run, at 6′, in the gate tests and on PR and push runs. **The workflow:** nothing changes beyond A3b's `always()`, which N1 puts in the default, so the splice and W are the default's. **`verdict`:** it reads S1's and `E`'s `arp2-qc21-fixtures` artifacts through the frozen templates, in memory, with the members exactly `["fixtures.json"]`. A red control voids its `for` column. A missing or expired artifact is VOID. **The readings:** C.6, D21's list, C.8 item 14, and the note's token line against `verdict`'s. N1 is done (below). IMPL D36 lists what the alternative would require. It is not implemented | 1634–1664 |

## 2. Nits

| finding | change (or refusal) | r14c lines |
| --- | --- | --- |
| **N1** A3b `always()` | Ports Q-C2-2 r14a's N10. A3b gets `if: ${{ always() }}`, with its consequence stated (row 109). The *Common* paragraph is reconciled: `always()` masks nothing, and A3's and job A's conclusions stay `failure` (row 110). M-GUARD (row 117) and control W, both its pinned list (row 124) and its removal self-test (row 125), gain "the marker A3b, or its `if:`". The rule sentence in C.8 item 7 now reads as Q-C2-2's, refined by Rc1 (§4). IMPL D31 | 2236–2240; 2297–2300; 2669; 2962; 2971; 3293–3297 |
| **N2** v3_verifier pin | *Inputs* gains row V3V: blob `681c673734427cb9f316feee09b7c5ffba348004` at `D`, sha256 `fc6545f5…`, confirmed read-only. Rule (h) cites the row. Before control T starts, `check` compares the working-tree file's blob id with the pin at `F`, S1 and `E`, and a mismatch fails DS (row 122). D27 sets `INPUTS` to the pin, and D33 refers to it | 669; 2929–2931 |
| **N3** credential table | Adds "and, under R8's default, at the ratification" | 1508 |
| **N4** edited-ratification self-test with no frozen rule | **Option taken: removed from IMPL**, rather than adding a rule to R8 that the owner has not ruled on. D23's self-test drops "edited ratification". D20 checks time and edit conditions only where the text states them: approval comments, and `F`'s designation (B1). For the designation of `E` and for the ratification it checks authorship and the quoted sha256s only | IMPL D20, D23 |
| **N5** R8 for the owner's sheet | Added to R8 as one sentence: both options rest on a comment under the owner's identity, which is not independent of the session's credential, so they differ in procedure, not in assurance | 1709–1711 |
| **N6** `run_class_*` callers | Rule (g)'s closing bullet (row 121) and C.8 item 8 now read "`derive-run`, `order`, `verdict` and `e-entry`". IMPL D35 needs no script change | 2934; 3306 |
| **N7** R3's alternative under R5 | "each under its caps and budget (R5)" | 1670 |
| **N8** | Record only. No change | — |
| **N9** Q-C2-2 r14a's shared-method changes | Traced item by item in §3. The ported items are rows 109–112, 114–117, 119 and 123, C.7's re-derivation, and R10 | §3 |

## 3. N9: Q-C2-2 r14a's later shared-method changes, traced

| Q-C2-2 r14a item | applies to Q-C2-1? | disposition |
| --- | --- | --- |
| N10, A3b `always()` | yes | Ported as N1 |
| R14-N2, retakes and the `E` entries | yes. Q-C2-1 has host VOID retakes (C.6). r14b's binding required B3 `success` of every entry, which a host-VOID run's entry fails, and a "`dispatch_sha` equals the same commit" condition that is false at `E` for the committed (S1) measurements. It built only one `E` entry | **Ported.** The binding applies to the run that attests at each stage. `dispatch_sha` is checked at S1 only, and B3 binds the input at `E`. A host-VOID entry has its own rule (row 112). The `verdict` condition is the r14a form (row 116). One entry is built per `E`-stage approval comment id. A C.8 item 9 reading makes every "the `E` dispatch's own entry" mean each such entry, with `e-entry` run once per id and R8's ratification covering each. R8 gains a sentence to the same effect. APPROVAL-ENTRIES carries the three r14a cases. IMPL D32 |
| R14-N4, design run and 6′ re-derived from the host | yes. C.7 checked the pinned records only | **Ported** to C.7 (adapted text, no edit row) with the `confirmation-measurements.json` note, which also states where that file comes from; the r14b text did not. Invariant row 1586. IMPL D19, D34 |
| R14-Rb2 narrowings of off-`main` support | yes, for three copied passages | **Ported.** The pre-`D` draft residual no longer rests on PLAN (row 114). The call figure is an estimate that no condition uses (row 115). The git "Why" no longer cites the writer's control and local run (row 119) |
| R14-Rb2 / §7, host-time records (§A.42 item 8) | yes: the final capture's record, the approval entries `verdict` builds for the dispatches at `E`, and, under R8's default, the ratification comment. Q-C2-1 has no Environment, so there are no `E`-stage Environment reads | **New owner ruling R10**, unbackticked PENDING twice: the item and `Record id`. As the coordinator asked, it decides nothing. It states both options, exception or narrowing, and **has no draft default**, which precondition 2's preamble now excepts. The final-capture passage (row 111) and C.8 item 9 say that the disposition is the owner's. They no longer call the final capture's record provenance |
| §5, the M-GUARD label "BYP-1 to BYP-18" | yes: same list | Ported (row 123) |
| R14-N3, artifact names; R14-N6, the binding's record; Rb3 (expiry) | already in Q-C2-1, which is where they came from | No change |
| Rb1, conditional step 1b; GX+R-Y; the frozen construction of the fixtures' completions | no: Q-C2-1 always runs step 1b, and the fixtures differ | No change |
| Rb1 (iv), C-SYM's own enumeration cap `C(E, d − 1) ≤ 10^5` | **undetermined.** Q-C2-1's C-SYM row also says "the caps apply to the fixture as listed, not to its exchanged form". Whether any Q-C2-1 fixture's effect side exceeds `10^5` needs a per-fixture count of `E` and `d`, which this revision did not make | **Not ported; flagged** for the next review. Under the timeout test the work is measured (`W_fix`), so it is a missing bound on the invariant, not a soundness gap |
| N1, E-ID; N7, Environment reads; N5, N11, the 6′ pins; N8 (`ACCESS.md`); N9 (cert_X3); the ledger | no: specific to Q-C2-2 | No change |

## 4. Found via the Q-C2-2 r14a review (Rc1), with its §A.42 note

**Rc1.** The trap is in Q-C2-1 r14b.
- Its no-unapproved-F1 rule requires A3b `success` for every non-dispatch checker-bearing attempt at a
  recorded-branch commit.
- The design branch is a recorded branch, and the design run decides the fixtures under no budget, so an A3 timeout
  or crash there is a violation. It is found at S1's capture, after `F`.
- R1's lowering rule explicitly contemplates "another design run" after a red one.
- A failure before A3 (checkout, setup or the runner) on any recorded-branch run is also a violation. Once A3b runs
  `always()`, it fails on the missing file.

**Fix, in the review's structure:**
- **(i) The rule** (row 126) holds when A3 is absent or `skipped`, or when A3b is `success`. This is safe on the
  frozen splice: with A3 skipped, every default-gated step is skipped, and A3b starts only `controls.py`.
- **(ii) The named residual** (row 126). An A3 that started and left no fixture-mode output is still a violation
  (fail-closed). It carries a frozen executor precondition: no push to a recorded branch unless A3's command, run
  locally on that tree, completes with fixture-mode output. Its limits are stated: a runner fault during A3, and an A3
  that completes locally but times out on the runner.
- **(iii) Precondition 6's equivalent.** C.7 6 gains a bullet: a design-run A3 that starts and leaves no output voids
  the round, so the executor precondition applies before the design branch is pushed. A design run that is red for
  another reason, A5's timeout included, is not a violation, and R1's lowering rule applies to it.
- **(iv)** C.8 item 7 and invariant row 1573 follow.
- **(v)** IMPL D39.

**The local run in (ii) is a fixture-mode run of the checker. It needs the same authorization as the design run,
and c.6740078002 does not give it.**

**The §A.42 item 8 note:** handled as R10 (§3).

## 5. Changes not traced directly to a finding; noticed, not changed

- **Housekeeping:**
  - the title and the r14c status bullet;
  - the row ranges in the edit-log introduction and the C.8 introduction (rows 109–126);
  - the QC22 *Inputs* row, which now cites Q-C2-2 r14a (`d751a127…`) as provenance for the rows it supplied;
  - "the owner's rulings R1 to R10" and invariant row 1576.
- **The `r14b/` directory.** The status bullet says "r14b is kept in `r14b/`", following the earlier bullets. That
  directory does not exist yet. It must be created, holding r14b, when the files are moved into place.
- **Noticed, not changed:**
  - **C-SYM's effect-side enumeration bound** (§3).
  - **"the first execution run" in Q-C2-2.** Q-C2-2 r14 uses the term without defining it. Q-C2-1 r14c defines it
    in C.8 item 9; Q-C2-2 may need the same.

## 6. Refusals

- None of the requested fixes was refused.
- **Owner choices: none decided.**
  - R1–R10 are unbackticked PENDING.
  - R1–R9 each carry a labelled draft default and a self-contained alternative.
  - R10 carries the two options and no default.
- No value of `S_max`, of any cap, budget or pin, or of `T0` is entered.

## 7. Owner rulings, precondition 2 (1617–1728)

Each ruling is PENDING. The coordinator's report restates R1 and R2 and lists the other wording changes: R3 (N7), R8
(N5 and the retake sentence) and R10 (new).
