# Q-C2-2 (ARP-3-QC22): dispositions of r14b

WIP / UNVERIFIED. Model-written. Drafting record, not a control-plane artifact.

- **Input.** r14a, `preregistration.draft.md`, sha256 `d751a127582748093491da416cfb024ac8db319f72b8f3206334abe7d35447ae`,
  kept unchanged in `r14a/` with its companions: `ACCESS.md` r14a (`8fb9016e…6b0b`), `DISPOSITIONS-r14a.md`
  (`595dd2c8…1338`), `IMPL-DELTA-r14a.md` (`76a21032…0418`) and `DECISIONS-QC22-preF.md` (`545ce34c…f571`).
- **Work list.** `review/REVIEW-QC22-r14a.md` (`c63ca1cc125b60419b3fb75950e8c6958dfb30a8bcddd712989c28a0501a1361`),
  verdict REVISE: blocker Rc1, nits N1–N9, the §2 residuals and the optional items.
- **Output.** r14b `preregistration.draft.md` (2267 lines), `IMPL-DELTA-r14b.md`, and `DECISIONS-QC22-preF.md`
  updated. `ACCESS.md` is unchanged (r14a): no finding concerns it. The sha256s are reported with this file, not in it.
- **Authority.** #1169 c.6740747027 (amaybaum, 2026-11-09T13:04:10Z) records the owner's choice: "Fix B1–B6 and the
  nits, reusing Q-C2-1's repaired wording, then run a further independent review. Paper-only. No F, design run, gate
  tests or Environment changes. Q-C2-2 stays behind Q-C2-1." It authorized r14 and a further review. That it covers
  r14a, r14b and their reviews, as fix-and-review iterations until the preregistration is ready, is the coordinator's
  reading, not the owner's words (R14a-N1). r14b's header says so.
- **How r14b was made.** `python3 -I r14bwork/make_r14b.py r14a/preregistration.draft.md <out>` checks r14a's sha256,
  then applies 26 exact replacements, each required to match once. Its output `r14bwork/r14b.out.md` is identical to
  the installed file. Diff: `r14bwork/r14a-r14b.diff`. The decision sheet is built the same way by
  `r14bwork/make_sheet_r14b.py` (12 replacements, input sha256 checked; diff `r14bwork/sheet-r14a-r14b.diff`).
  `IMPL-DELTA-r14b.md` and this file were written by hand.
- **What was run.** Text checks only:
  - the review's `review/probes-r14/p01_v3blocks.py` on r14a against r14b: both V3 blocks equal, so the
    governed-paths digest is unchanged;
  - `review/probes-r14/p02_pending.py` on r14b: 34 unbackticked `PENDING`, as in r14a;
  - `r14bwork/s4_screen.py`, the review's `p05` screen with its section bounds found by heading: 0 S4 hits in the
    printed sections (Frozen texts to the S4 list, and ADA), r14a and r14b alike;
  - every added line outside tables is at most 120 characters wide, the title excepted;
  - two owner-record comments, c.6740593434 and c.6740747027, read through the API (read only).

  No LP, simplex, script self-test or computation on any OI construction. No repo, git or GitHub write. Q-C2-1's files
  were read only.
- **Wording reused from Q-C2-1 r14b** (`../qc21/preregistration.draft.md`, `57053e08…`): R6's alternative clause (its
  1653–1657) for N2, and M-RAY's "an extreme row removed under a fabricated certificate" (its 3403–3404) for N6.
  Q-C2-1 r14b has no wording for Rc1's case, so Rc1's text was written here. During this work the Q-C2-1 drafter
  installed r14c as `../qc21/preregistration.draft.md` (`d4e0fca9…`, 14:37:35Z; r14b kept in `../qc21/r14b/`). Read
  afterwards, r14c takes the same route for its copy of the rule (its C.3 lines 2552–2560 and C.8 item 7): A3 absent or
  `skipped`, a named residual and a local-run executor precondition. r14b's precondition is the stricter of the two: it
  also requires completion within `timeout-minutes`, `fixture-mode-check` exiting 0, and no cancellation by the
  executor.
- **Line numbers** below are r14b's.

## 1. Blocker

| finding | disposition | r14b location |
| --- | --- | --- |
| **Rc1** an A3 that leaves no fixture output voids the round, including a case the text provides for | **Fixed by the review's route (a), with the residual named and backed.** (i) **The rule** holds when job B and B4 are absent or `skipped` and **either A3 is absent or `skipped`, or A3b is `success`**. `order.json` already records `A3_conclusion`. (ii) **Why the exemption is safe** is stated: A1 and A2 start no checker; every later step whose `if:` has no status function implies `success()` and is skipped with A3 (A5, A8, A10, A11); A3b, the one `always()` step, runs `controls.py` only. So a pre-A3 failure (checkout, `setup-python`, runner) or a job A that never started is no longer a violation, at S1's and `E`'s `pull_request` runs or anywhere else. (iii) **The residual**, an A3 that ran or was cancelled and left no fixture-mode output (timeout, crash), stays a violation, since it cannot be told from an A3 that computed F1; it is named as a residual. (iv) **Executor precondition** (§A.41): no commit carrying the checker becomes a recorded branch's head unless A3's command, run locally on that tree with Python 3.11, completed within `timeout-minutes` and `fixture-mode-check` exits 0 on its output; and the executor cancels no run on a recorded branch while job A runs. (v) **Precondition 6's clause corrected**: a design-run fixture undecided within the job timeout is an A3 timeout and so a violation; its run time is established locally first under the precondition; a fixture found undecided locally, or a design-run A3 exiting 3 with complete fixture output, leads to revision before `F`; a design-run A3 that still times out, crashes or is cancelled is the residual, known before `F`, and `F` is then not requested. (vi) **Checkpoints**: new self-test NOF1 (the rule on synthetic attempt records, both directions); a new invariant row; A3b's description says the rule reads A3's own conclusion when A3 is skipped | 1755–1772; 1379–1380; 800–803; 1885; 2136–2145 |

## 2. Nits

| finding | disposition | r14b location |
| --- | --- | --- |
| **N1** r14a's authorization stated as the owner's | **Fixed.** "under the same authorization" removed from the r14 bullet. A new header bullet says c.6740747027 authorized r14 and a further review, and that its covering r14a, r14b and their reviews is the coordinating session's reading, not the owner's words. The off-`main` row for owner comments says the same | 43–52; 205 |
| **N2** R6 alternative; sheet row wrong | **Fixed.** The alternative gains Q-C2-1 r14b's clause: "the committed measurements are then bound to the approved computation by B6's replay at `E` only, not to S1's output", and states that no frozen text renders the limitation, so the alternative is applied by a reviewed revision before `F`. Sheet row corrected (B6 at `E` binds to `E`'s recomputation; the record at `E` holds S1's artifact identity and archive `digest`, not a content comparison) and the alternative marked **[R]** | 1943–1949; sheet §5 |
| **N3** the fourth new `PENDING` item | **Fixed, (i)–(iii) and the revision step.** (i) Narrowing now states the checks **only as conditions of landing** (the round lands only if they pass), not that they passed. (ii) **"Applying the choice"**: filling the record id changes no text; the chosen option is applied before `F` by a reviewed revision (item 4) that revises the named sites: control N's stage reads, *Its record*, *Where the entries are*, the invariant rows on F1's computation, owner requirements 1–3, the Environment at S1 and `E`, and designations and approvals, and the off-`main` row on these records. (iii) **"What each option leaves of the token"**: F1's verdict, replay-matched at `E`, is re-established from `main` by a dispatch at `E` under either option; the governance claims are left not established under an exception (§A.46 item 1) and are not claimed under narrowing. No option is chosen. Sheet row updated, both options **[R]** | 1950–1969; sheet §5 |
| **N4** off-`main` table completeness | **Fixed.** *What infeasibility licenses*' "`r_S ≤ 6` against 36 reads" is marked as the paper prediction that the round measures (and re-wrapped from 165 characters). *The question*'s Consequence becomes "(predicted). If (a) holds in F1, as the paper analysis predicts, …". Row `ACCESS.md` §5/§6 now lists both sites. A row is added for S1's measurements artifact, with *Retention*'s classification (support when read, provenance after expiry; enduring support `E`'s committed measurements, the binding's record and a dispatch at `E`) | 842–844; 281–283; 211; 224 |
| **N5** row 216's route | **Fixed; the route chosen:** after Q-C2-2 closes, the owner adds a branch at `E` to the deployment-branch policy, dispatches on it with the input true and `arp3qc22_sha` `E`, and approves its review. Not chosen: moving the round or gate-test branch to `E`, a non-fast-forward ref movement (§A.43 item 4). Stated in the row and in *After merging to `main`*'s re-establishment bullet | 223; 1557–1559 |
| **N6** M-RAY's "its first row" | **Fixed, Q-C2-1 r14b's wording** "an extreme row removed under a fabricated certificate", applied to both sides ("each with an extreme effect row" for C-SYM) | 686–689 |
| **N7** "which is the writer's statement" | **Fixed:** "This round does not check whether such a draft exists." No assertion about pushes before `D` remains | 1686 |
| **N8** what the identity under (iv) is for | **Fixed.** Under (iv) the session's identity and its permissions are recorded to show which identity dispatches and whether it can edit the Environment; no condition reads it (B3b and the `review` check use `amaybaum`, authorship requires `amaybaum`, `prevent_self_review` enforces the dispatcher rule on the host). Sheet row and `IMPL-DELTA-r14b.md` B7 (correcting r14a's A8) updated | 2083–2088 |
| **N9** drafting records | **Fixed in the sheet.** §0 now shows ENV-CREATE as resolved by c.6740593434 (quoted with author and time; it is a comment generated by the coordinating session and posted with the owner's credential, which the sheet says): the owner creates the Environment and 2a stands. Two consequences that rested on §0's earlier reading are corrected (§1's and §2's "since I can't" sentences), §6's ENV-CREATE bullet is removed, and §7's pointer reads "The owner creates it (§0)". New §8 lists exactly the rows added: r14a added three (expired S1 artifact, §A.42 item 8 dispositions, the identity E-ID adds), precondition 4's row was already there at r14, and r14b adds none. `DISPOSITIONS-r14a.md`'s "four rows" is corrected in §5 below | sheet §0, §1, §2, §6, §7, §8 |

## 3. Residuals (review §2) and optional items (review §4)

| item | disposition | r14b location |
| --- | --- | --- |
| invariant row: "the `E` entry in `verdict`" singular | "the entries `verdict` builds, one per `E`-stage approval comment id" | 1900 |
| unlabelled R6-type default: stop rule, S1-BIND's "no artifact" | both labelled "for an expired or deleted artifact, draft default, pending the owner's ruling in precondition 2" | 1847–1848; 790–791 |
| common clause "(reproduced in this round as CC-F0 …)" | "(decided in this round as CC-F0, with its model verified)"; S4 screen clean | 857 |
| G's configuration space | fixed as H3's eight configurations `(z, x, η)`, point reads on all eight, matching "H3's block B alone". The review's `p03` shows the same verdicts on either space; `p03`'s G row (8 points) gives `n = 4`, `d = 3`, `E = 10`, `C(E, d − 1) = 45`, within every cap | 647 |
| line 886, 152 characters | re-wrapped (whitespace only), with the break before "Per herald block" so that no placeholder is split | 903–907 |

## 4. Changes not traced directly to a single finding

1. **Header**: title r14b; the r14a review-history bullet (housekeeping).
2. **Off-`main` table**: the drafts row adds r14a and `DISPOSITIONS-r14b.md`; the Q-C2-1 row adds r14b (`57053e08…`) as the
   source of the reused wording (provenance; §A.42 item 8).
3. **Decision sheet**: the "Updated for preregistration r14b" bullet; c.6740593434 added to its owner-records list; §6's
   "decided before the revision that fixes B1–B6" corrected to "before the candidate revision presented for `F`", since
   r14–r14b were made without those decisions (a stale statement found while removing §6's ENV-CREATE bullet).

## 5. Choices, refusals and divergences

- **No refusals.** Every finding is applied as the review specifies.
- **Rc1 route.** (a), not (b). (b) would exempt only trees carrying the pinned blob and frozen splice, leaving the
  design branch, which precedes the pins, exposed, which is precondition 6's case. (a) removes the pre-A3 cases
  everywhere, and the precondition covers the design branch's A3 timeout.
- **Rc1, precondition 6.** The review offered "violation, with run time established locally first" or "the rule exempts
  it". The first is taken: an A3 that ran and left nothing cannot be told from one that computed F1, on a design tree as
  anywhere. The consequence for a design-run residual (it is known before `F`, and `F` is not requested) follows from
  the rule and the stop rule; it is stated, not a new owner choice.
- **Owner decisions.** None decided. No new `PENDING` field; 34 remain. Two existing ones now say that their choice
  needs a reviewed revision (the expired-artifact alternative; either §A.42 item 8 option).
- **Same trap in Q-C2-1** (review, Rc1): Q-C2-1 r14b's C.8 item 7 carries the r14a form of the rule. Its r14c,
  installed during this work, fixes it the same way (see *Wording reused* above). Not changed here.

## 6. Errors in `DISPOSITIONS-r14a.md` (kept unchanged as a record; corrected here)

- Its "four rows added to `DECISIONS-QC22-preF.md`" (header and §3 item 5): r14a added three. Precondition 4's row was
  already in r14's sheet (N9).
- Its header's "The same scope covers this review's findings" states as the owner's what is the coordinator's reading
  (N1).
- `IMPL-DELTA-r14a.md` A8 names B3b and the `review` check as users of the identity under (iv); that holds under (i)
  only (N8). Corrected in `IMPL-DELTA-r14b.md` B7.

## 7. Owner `PENDING` items after r14b (34 unbackticked fields; control P refuses `F` until all are filled)

- **Owner decisions:**
  - precondition 2's record id (O-7, O-1–O-3, audit incorporation, F1+R-S scope, floating-point basis, paired
    completions);
  - Q12's record id;
  - the expired-S1-artifact ruling, record id (the alternative needs a reviewed revision);
  - the §A.42 item 8 dispositions, record id (either option needs a reviewed revision);
  - 2a's commitments record id and the round and gate-test branch names;
  - 2b's record id (E-READ, E-ID, E-BIND);
  - the identity E-ID adds;
  - precondition 3 (the preparation-side guard);
  - precondition 4's confirmation or correction of its reading.
- **Waiting on sequence** (ARP-2 landing; "No F before Q-C2-1's results"): `D`; precondition 1's record ids and
  disposition; the splice anchors; `T0`; the drift check's extension to `D`.
- **Waiting on authorized runs** (none authorized): the two scripts' blobs and sha256s; the design run's
  `design-run.json` pin, run id, step ids, `t_5`, `σ`, `W_fix`, `W_stress`, `t_810` and the budgets; the `stress.json`
  pin; 6′'s run id and `confirmation-run.json` pin; the `gate-tests.json` pin; the `env-pin.json` pin.
