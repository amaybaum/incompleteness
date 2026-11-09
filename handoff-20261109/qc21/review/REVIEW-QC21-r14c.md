# Independent preparation review: Q-C2-1 r14c (ARP-2-QC21)

WIP / UNVERIFIED review note. Model-written. Read-only.

**Verdict: REVISE (minor).** r14c fixes R14B-B2 exactly as scoped and fixes r14b-N1 to N8 correctly. The Rc1 port is
sound. R14B-B1 and R14B-B3 are fixed in substance, but each leaves one gap. R10 carries a wording defect that the
Q-C2-2 r14a review has already found in the text r10 copies. There are three blockers, all cheap:
- **R14C-B1.** `order` checks the times of a comment whose id the executor supplies. Nothing binds that comment to
  `F` or to the owner, so any earlier comment satisfies the check.
- **R14C-B2.** R2's alternative leaves out two frozen rule changes it needs, both in control B's node-form rules.
  IMPL D36 says the guard rules stay as they are under the default, which is wrong.
- **R14C-B3.** R10's narrowing option contradicts itself: it states the checks as "met", yet "makes no claim that
  rests on their content". It also names no sites and says nothing about the token. These are Q-C2-2 r14a review
  N3 (i)–(iii), not ported.

R1 and R3–R9 are ready for the owner as written. R2 needs B2's fix and R10 needs B3's fix.

**Authority.** #1169 c.6740078002 (amaybaum, OWNER, 2026-11-09T12:29:10Z) authorizes r14, the script updates,
ordinary non-scientific self-tests and independent preparation review. It does not authorize the design run, the
gate tests, `F`, dispatch or any scientific computation.

**What this review did.**
- It ran no LP, no simplex, no stress test, no script self-test and no computation on any round instance.
- Its probes are text checks, integer counts, the integer rank of 0/1 read-indicator functions on `F_2^k`, and
  read-only `git`.
- It made no repo, git or GitHub writes, and changed no Q-C2-2 file.
- Its only writes are this file and `review/probes-r14c/`.

## Inputs (verified)

| file | sha256 | check |
| --- | --- | --- |
| r14c `preregistration.draft.md` | `d4e0fca90180400b77f6290eb1c1df305be14a7f86591cecd76337b907651ef7` | matches the brief; equals `r14cwork/preregistration.r14c.md` |
| r14b `r14b/preregistration.draft.md` | `57053e08a18f3357b86ea3956e88bbb1fb7a34c1d14fbd6b169ebbff8d1b65e1` | matches |
| `DISPOSITIONS-r14c.md` | `61cff2885c87495ad19ced5421c34447d2888b3b282e9fcc459f9fe5c9ced43f` | matches; equals the `r14cwork/` copy |
| `IMPL-DELTA-r14c.md` | `80df27b0656e33fefeb63e01f2e7160beb44ccd37fd500486450aeeff5a1682d` | matches; equals the `r14cwork/` copy |
| `review/REVIEW-QC21-r14b.md` | `95dcec39762b648139a24626fd20b9b776dc6ceca5f5a0e93374efe0406d4765` | matches |
| `r14cwork/make_r14c.py` | `6df6b7f2e5f26445a9d1645b5d412cca266db07d13edc60634e63e036d420069` | read in full |
| Q-C2-2 r14 `../qc22/r14/preregistration.draft.md` | `9e3ef0c9…` | the source of rows 113 and 118 |
| Q-C2-2 r14a `../qc22/r14awork/r14a.out.md` | `d751a127…` | the source of the r14a ports |
| `../qc22/review/REVIEW-QC22-r14a.md` | `c63ca1cc125b60419b3fb75950e8c6958dfb30a8bcddd712989c28a0501a1361` | Rc1, and §3 N3 |

**Q-C2-2's file moved during this review.** `../qc22/preregistration.draft.md` was `d751a127…` (r14a) when this
review started. At 14:41 it became `e8f5fcfb…`, which Q-C2-2's own `DISPOSITIONS-r14b.md` (14:44) accounts for as
its r14b. That is the sibling round's writer, in its own directory, so it is not a provenance anomaly here. The r14a
comparisons below use `r14awork/r14a.out.md` (`d751a127…`). Q-C2-2 r14b is unreviewed, and it is cited below only as
a comparison (`probes-r14c/qc22_state.out`).

**The build reproduces.**
- `make_r14c.py` reads its inputs from a fixed `BASE`, which now holds r14c, so its sha256 guard refuses to run
  there. The probe copy `probes-r14c/make_r14c.rebased.py` changes only `BASE`, to a directory holding r14b and
  IMPL r14b (diffed: one line).
- Run that way, it applies 45 and 11 edits. Its outputs are byte-identical to r14c (`d4e0fca9…`) and to IMPL r14c
  (`80df27b0…`) (`cmp`).
- A fresh `diff -u` r14b→r14c equals `r14cwork/r14b-r14c.diff` below the header lines.
- `check_rows_r14c.py` finds every fragment of rows 109–126. Row 118's copied-text cell is the marker
  "(none; added after S1-BIND)", which the script reports as missing, as expected.

**The V3 blocks are unchanged.** `v3-round` and `v3-governed-paths` are byte-identical in r14, r14a, r14b and r14c
(`probes-r14c/v3_blocks.out`).

**Control P.** The re-implemented `pending_unbackticked` (`probes-r14c/control_p_coverage_r14c.out`) catches 37
lines: r14b's 35, plus R10's item (1719) and its `Record id` (1728).
- The 9 lines it skips only name the word, as in r14b.
- Every `PENDING` on an added line is caught. The other added uses are lowercase labels ("R10, pending", "pending
  owner ruling R1"), and each points to a caught item.
- No pre-`F` placeholder is uncaught.

**V3V.** Read-only `git`: `fd539e15:tools/v3_verifier.py` is blob `681c6737…`, sha256 `fc6545f5…`, the same on
`origin/main` (`probes-r14c/v3_verifier_blob.out`).

**Register.** The 205 added lines contain none of §A.32/§A.33's history or meta phrases. Their only all-caps tokens
are codes, `VOID`, `VERDICT`, `JSON` and `PENDING`. Outside tables, only the title line is over 120 characters.

## Blockers

**R14C-B1. `F`'s designation comment is read but not bound to `F` or to the owner.**

*What the rule checks* (2462–2465). It reads the comment, given by "its id given as an argument", and checks its
`created_at` and `updated_at` against the first execution run. `order.json` "records its id, author and times".
- The executor supplies the id.
- No condition requires the comment to quote `F`'s full commit id, or to be authored by `amaybaum` with association
  `OWNER`.
- Any comment created before the first execution run passes, an unrelated earlier owner comment included.

*The approval comments, by contrast,* must quote the full commit id and the stage, and pass the authorship check
(C.3, 2422–2433).

*Why it matters.* The invariant rows at 3752 and 3765 cite this read as the checkpoint for "`F` designated before
the first execution run". As written, the read does not measure that (§A.41). This is the residue of R14B-B1: the
comment is now read, but not identified.

*Fix (one sentence and two control cases).* In C.3's `order.json` bullet:
- the comment's author is `amaybaum` with association `OWNER`;
- its body contains `F`'s full 40-hex id;
- `order.json` also records the quoted words (§A.42 item 7).

Add both cases to APPROVAL-ENTRIES: a designation comment that does not quote `F`, and one with another author.
Mirror both in IMPL D29 and D30.

*Q-C2-2.* Its r14 1538–1541, which r14c ports, and its r14b 1670 have the same gap. Report it there; this review
changes no Q-C2-2 file.

**R14C-B2. R2's alternative leaves out two frozen changes it needs.**

The r14b-B3 fix is right in kind. A3 exits 0 only at round-branch dispatches, so job A, the aggregate and the run
stay green, and `E`'s run can still be `E`'s exact-head attestation (§A.39). The other form is rejected for the
right reason: `always()` on A4–A10 would leave job A red at `E`.
- **The key cannot be confused with other runs.**
  - The gate tests are off the round branch (C.7 6″), so they still exit 3.
  - `F`'s dispatch carries no checker and no job (2520–2521), so it is unaffected.
  - Host-VOID retakes at S1 and `E` are round-branch dispatches, so they exit 0, as the alternative intends.

But "each frozen before `F`" lists the checker, the workflow, `verdict` and the readings. It leaves out two frozen
node-form rules that the alternative breaks:
- **`controls.py`, rule (b)** (2842–2844). A `ZipFile` may have only `namelist()` and `read("measurements.json")`
  called on it. `verdict` (and `note`) must call `read("fixtures.json")`. Control B, and the ZIP-1 to ZIP-3 family in
  M-GUARD, are written against the old literal.
- **`qc21_check.py`, control B** (2818–2819). `DISPATCH_EVENT` may be referenced only in `s_mode` and in M-GUARD's
  self-tests. `s_mode(argv, environ)` returns `"fixture"` whenever `--event fixture` is passed, so it cannot report
  whether the run is a round-branch dispatch.
  - The new exit rule needs `GITHUB_EVENT_NAME == DISPATCH_EVENT` and `GITHUB_REF == ROUND_REF`.
  - Either that comparison is a new function of `s_mode`'s, or the B rule admits one more site.
  - `os.environ` already reaches `s_entry` whole (2745–2747), so the "exactly two `os` sites" rule can stand.

IMPL D36 says "The splice, W and M-GUARD stay as under the default". The splice and W do, but control B's two rules
and their M-GUARD variants do not.

*Fix.* Add a fifth bullet, **Control B**, to R2's alternative naming both rule changes, each with an M-GUARD variant:
- reading a third member name must fail B;
- referencing `DISPATCH_EVENT` outside `s_mode` and the new exit-rule function must fail B.

Correct D36 to match. N6 below is optional wording for the same bullet list.

**R14C-B3. R10's narrowing option has the defect the Q-C2-2 r14a review already found.**

R10 (1719–1728) copies Q-C2-2 r14a's 1913–1918 text. The Q-C2-2 r14a review (§3, N3) found three defects in that
text:
- **(i) The narrowing contradicts itself.** "states those checks as halt conditions met before landing, … and makes
  no claim that rests on their content". To state that the checks were *met* is a claim that uses the off-`main`
  records. The narrowing must state them only as conditions of landing: the round lands only if they pass, and the
  record does not say that they passed.
- **(ii) A record id alone changes no text.** Under either option, the passages that assert these properties must
  be revised before `F` and reviewed. In Q-C2-1 they are:
  - C.2 *Its record* (2389–2393) and *Violations* (2394);
  - C.3 *Authorship* (2431–2436);
  - `verdict`'s ratification and entry conditions (2572–2579);
  - C.8 item 9 (3317–3336);
  - the credential-table row (1508);
  - the owner commitments (1512–1514);
  - the invariant rows 1562 and 3765.
- **(iii) Say what each option leaves of the token.** The scientific content, the tokens as replay-matched at `E`,
  is re-established by a dispatch at `E` (§A.42 item 7). The governance claims are left unestablished under an
  exception (§A.46 item 1), and are not claimed under narrowing. Those claims are: every dispatch at `E` was
  approved and ratified, and no unapproved checker-bearing run occurred between `E`'s capture and landing.

Q-C2-2 r14b already uses wording that fixes (i) and (iii) ("only as conditions of landing … It does not state that
they passed"; "What each option leaves of the token"). Port the review's fix, not the r14a text.

The rest of R10 is right:
- the three records;
- "no Environment" (Q-C2-1 has none);
- having no draft default, which precondition 2's preamble excepts;
- two unbackticked `PENDING`s;
- the two sites that say the disposition is the owner's.

## Nits (one line each)

- **N1 (attempts still running at a capture; pre-existing, liveness).** Rule (d) reads `A3_conclusion` and
  `A3b_conclusion`, and nothing in the text handles a recorded-branch attempt that is still `queued` or
  `in_progress` at a capture. An example is the S1 push's `pull_request` run while `check --stage S1` runs. Its
  null A3b is not `success`. Add: "a capture that lists a checker-bearing attempt whose status is not `completed`
  is failed, to be retried", as for rate limits. The same holds in Q-C2-2.
- **N2 (the executor precondition's wording).** Scope it to commits carrying the checker: `F` carries none, so the
  precondition cannot be met there as written. Then add these from Q-C2-2 r14b 1769–1772:
  - "within `timeout-minutes`";
  - "with Python 3.11";
  - "`controls.py fixture-mode-check` exits 0 on its output";
  - "the executor cancels no run on a recorded branch while its job A runs". The residual lists cancellation as a
    violation, so an executor's own cancellation must be excluded.
- **N3 (layout).** The **Residual** bullet (2556–2561) sits in the list governed by "The rule holds exactly when,
  for every such attempt:", so it reads as a fourth condition. Move it below the list, as Q-C2-2 r14b does.
- **N4 (APPROVAL-ENTRIES cases).** Add three cases:
  - the first execution run is chosen across events: a `push` run at a post-`F` commit created before S1's dispatch
    is the reference;
  - a host-VOID entry whose run is not a host VOID by C.6's definition fails;
  - with B1, a designation comment that does not quote `F`, or has another author, fails.

  The definition at 3338 could also say "a descendant of `F` other than `F`", which is decidable with
  `merge-base --is-ancestor`, already admitted.
- **N5 (C-SYM's cap; scope item 3).** No Q-C2-1 fixture needs C-SYM's own cap: every bound is below `10^5` (table
  below). That bound rests on B-CLASS and B-REG being two-bit registers, which only the implementation fixes. The
  text says "a classical register with spanning reads" (1266).
  - A three-bit register with a joint read would give `E ≤ 23`, `d ≤ 8` and `C(23, 7) = 245,157`.
  - Either state the register size in B-CLASS's and B-REG's rows and add one sentence recording the bound, or port
    the cap. The DISPOSITIONS' "missing bound on the invariant" is also too strong. C.1's caps on effects before
    reduction and on `d` already bound the effect-side enumeration, by `C(effects cap, d cap − 1)`.
- **N6 (R2 alternative: `note` and R6).**
  - `note` reading S1's artifact over the network departs from the S1-binding pattern, where `derive-run` records
    and `verdict` re-reads. It also makes control V's regeneration of the note depend on the host. Prefer this:
    `derive-run` on S1's run records the red controls in `evidence/s1-run/results.json`, `note` reads that record,
    and `verdict` re-reads the artifact and compares.
  - Under R2's alternative, an expired fixtures artifact is VOID whatever R6 rules. Say so, so that the owner sees
    how the two rulings interact.
- **N7 (`confirmation-measurements.json`, 3088–3091; shared with Q-C2-2).** "cannot make a perturbed decision pass
  unseen" overstates. A copy equal to S1's committed `fixtures` section makes C-STATELESS pass vacuously, and only a
  comparison that no condition makes would reveal it. Narrow the wording to "would be visible only by comparing the
  copy with 6′'s archive, which no condition does", or bind the copy (which needs B2's `ZipFile` widening).
- **N8 (IMPL).** D31 says "Rule (d) is unchanged", but D39 changes rule (d). Reconcile the two.
- **N9 (status bullet).** "shared-method changes of ARP-3-QC22 r14a are ported (edit rows 109–125)" also covers
  rows 113, 118, 120–122, 124 and 125, which are not r14a ports. The edit-log introduction is accurate; the bullet
  could say "rows 109–125 (the ports among them as the edit log states)".

## Scope item 1: R14B-B1 to B3 and r14b-N1 to N9

**R14B-B1. Ported faithfully, apart from B1 above.**
- Q-C2-2 r14's 1538–1541 wording is at 2462–2465 verbatim, with the reference to C.8 item 9 added.
- C.8 item 9's arguments name `F`'s designation (3317–3320), and rule (g)'s note reads "read by `order`, `verdict`
  and `e-entry`" (2915–2916).
- Invariant rows 3752 and 3765 name the read and the control, and IMPL D29 and D30 add them.

**APPROVAL-ENTRIES vs APPROVALS: sound.** Copied *After the edits* (1977) and precondition 2's item 3 (1441) say
that no copied control "refers to an Environment, `approvals` or `deployments`", meaning the Environment's
`…/approvals` endpoint.
- A copied control named APPROVALS would read, lexically, as such a reference.
- APPROVAL-ENTRIES uses C.3's own heading ("Approval entries"), and its lowercase form does not contain
  "approvals".
- Edit row 118 cites its Q-C2-2 origin.
- A lexical scan for `approvals` would still hit `evidence/approvals.json`. The sentence's meaning (the endpoint) is
  therefore what governs, and the new name does not depend on it.

APPROVAL-ENTRIES carries Q-C2-2's 691–694 cases with association added, the `E` entries, `e-entry` ≡ `verdict`,
R8's cases under both options, and the r14a host-VOID and two-id cases. N4 lists three more cases.

**"The first execution run" (3338–3339): right, and needed.** It is the earliest-created run of any event whose
`head_sha` is a round-branch commit after `F`.
- It excludes `F`'s own attestation dispatch and any run at `F`. Those precede the designation by §A.39, so
  including them would make the check impossible.
- It includes the push and `pull_request` runs at S1, so the designation must precede S1's push itself, which is
  §A.39's order.
- `order` finds the run in its enumeration: post-`F` runs postdate `T0`, so set (2) and set (1) contain them.
- A run at a post-`F` commit made on another branch (for example a branch created from S1) also counts. That is
  conservative.
- See N4 for the self-test case and the "descendant" wording.

**R14B-B2. Fixed.** The new wording is identical in R1, R1's alternative and C.8 item 2 (1624–1633, 3222–3226):
the owner "may" fix a positive `S_max` no larger than the red run's, and the floor holds unless the red run's value
was at most `10^5`.
- `probes-r14c/r1_admissible.py` checks chains of red runs with integers only: `2·10^5 → 10^5+1 → 10^5 → 5·10^4 → 1
  → 1`, `10^6 → 10^5 → 10^5 → 99,999 → 2 → 1`, and `10^5 → 1`.
- After every red run, the admissible set is non-empty and contains the red run's own value, under the default and
  under the alternative.
- A red run for another reason forces nothing.
- C.7's new bullet applies the rule to "a design run that is red for another reason, A5's timeout included".
- The `check --freeze` bullet (3175) and SG-2 (1578) keep "at least `10^5`" with R1's label, which is consistent.
- IMPL D24 matches.

**R14B-B3. Implementable, but under-specified: see B2.** The `verdict` reads are right:
- every listing page;
- exactly one artifact of the name, whose `workflow_run` id and `head_sha` are the run's;
- members exactly `["fixtures.json"]`, read in memory;
- missing, expired or unreadable gives VOID.

The readings are complete for C.6, D21's list and C.8 item 14. "`verdict`'s job-A condition stands as written" is
right, since A3 is `success` under the alternative; its parenthetical then describes the default only.

**r14b-N1 to N9.**
- **N1.** Fixed: A3b `if: ${{ always() }}` (2236–2240), with its consequence stated. The *Common* paragraph is
  reconciled: `always()` masks nothing, and A3 and job A stay `failure`. M-GUARD row 117, W's list (row 124) and W's
  self-test (row 125) carry "or its `if:`". C.8 item 7 is reworded.
- **N2.** Fixed: Inputs row V3V, rule (h) cites it, `check` compares the blob at `F`, S1 and `E` before control T
  starts, and D27 and D33 implement it.
- **N3.** Fixed (1508).
- **N4.** Disposed of correctly, by removal from IMPL (D20, D23). No ruling is invented.
- **N5.** Added to R8 (1709–1711).
- **N6.** Fixed (2934, 3306).
- **N7.** Fixed (1670).
- **N8.** No change, as recorded.
- **N9.** Traced item by item (DISPOSITIONS §3).
  - The R14-N2 port is right:
    - the binding holds for the run that attests at each stage;
    - `dispatch_sha` is checked at S1 only, and at `E` B3 binds the input;
    - a host-VOID entry has its own rule;
    - one entry is built per `E`-stage id.
  - The R14-N4 and Rb2 ports and the BYP label are right, apart from N7.
  - R10 is right in kind, apart from B3.

## Scope item 2: the Rc1 port, the residual, and its authorization

**The rule (2549–2555).** It holds when job B and B4 are absent or `skipped`, and either A3 is absent or `skipped`
or A3b is `success`. It is safe on the frozen splice.
- With A3 skipped, every later step whose `if:` lacks a status function is skipped. That includes A10, whose
  `hashFiles` condition implies `success()`.
- A3b starts only `controls.py`.
- A5 (`--stress`) and A8 (`--self-test`) are skipped as well.

*"Absent" adds no new route.* A non-frozen workflow at a recorded-branch commit could already run a rogue job beside
an intact job A and satisfy the r14b rule. Admitting a missing job A therefore does not widen what such a workflow
can do. The in-tree keys are stated to prevent runs of the frozen splice only (C.2, *Enforcement*).

**A3b `success` (N1's case)** covers a red A3 with complete fixture-mode output.

**The residual (2556–2561)** is an A3 that started and left no fixture-mode output. It stays a violation
(fail-closed), which is right: such an attempt cannot be told from one whose A3 did something else. C.7 6's new
bullet correctly applies it to the design run, and C.8 item 7 and invariant row 1573 follow. See N1–N3.

**The authorization question.**
- **The writer is right in substance.** A local run of A3's command decides the frozen fixtures with the solver.
  That is the design run's A3 run off the runner, not a self-test (`--self-test`). c.6740078002 withholds the design
  run, and its "ordinary non-scientific self-tests" does not clearly reach it. Only the owner can say whether it
  does.
- **No authorization is needed now.**
  - The precondition binds only at a push of a checker-bearing commit to a recorded branch.
  - The first such push is the design branch's.
  - C.8 item 2 already forbids pushing a tree that carries the frozen splice before the design run is authorized.

  So the precondition creates no authorization need before the design-run request. That request should name the
  local A3 runs explicitly, before each push to a recorded branch, S1 and `E` included.
- **A precondition that needs no local run.** This is the Q-C2-2 r14a review's Rc1 option (b): exempt, by
  structured data, an attempt whose tree carries the frozen splice and the pinned checker.
  - Rule (d) would hold for an attempt whose A3 started and left no output when its `head_sha` tree has two things:
    - `verify.yml` equal to control W's expectation, read by `git cat-file` or the trees template, both already
      admitted;
    - the pinned `qc21_check.py` blob at the record path.
  - In such a tree, A3's literal `--event fixture` fixes fixture mode (`s_mode`, M-GUARD), and the guard's
    refusal and counter exclude every decisive builder in job A. So an incomplete A3 cannot have computed F1.
  - This is a structured signal (§A.44): blob ids, not log text.
  - **Caveats to state.**
    - A `pull_request` run executes the synthetic merge. The base held at `D` makes its tree `head_sha`'s (C.7).
    - Events that run the default branch's workflow (`schedule`, `workflow_run`, `issue_comment`) do not have a
      recorded-branch `head_sha`, so they do not arise.
  - It removes the residual for frozen trees, and leaves A3b as the requirement for any other tree.
  - It is a frozen-text design choice for the writer. It needs no owner authorization, and the local run then
    becomes an optional liveness check rather than a frozen precondition.

## Scope item 3: the N9 ports, and C-SYM's cap

The ports are covered in scope item 1. The C-SYM count is in `probes-r14c/csym_counts.py` and its `.out`. It uses
exact generic counting only. `E` is over-counted: every listed outcome effect, plus the unit, plus a complement for
each outcome of a setting with more than two outcomes. `d` is bounded by the lesser of the number of preparations and
the integer rank of the read-indicator functions (unit included), or by the dimension the row states where that is
smaller.

| fixture | outcomes | `E ≤` | `d ≤` | `C(E, d − 1) ≤` |
| --- | --- | --- | --- | --- |
| B-POS, B-STAB, B-WAVE, B-REG | 4 | 5 | 3 | 10 |
| B-S4F; B-RAY-S, -P, -F | 4 | 5 | 3 | 10 |
| B-REG+parity | 6 | 7 | 4 | 35 |
| B-CLASS (two-bit, as implemented) | 8 | 13 | 4 | 286 |
| ZPT | 4 | 9 | 2 | 9 |
| F10 | 2 | 3 | 2 | 3 |
| QM-P's restricted fragment, text's `Ω_c` (3 read bits) | 10 | 19 | 6 | 11,628 |
| QM-P, implementation's product embedding (5 bits) | 10 | 19 | 8 | 50,388 |

- **QM-P's dimension.** Its table has `d ≤ 6` under either embedding. M10's and M20's screen marginals equal
  M00's, and the operator span of `{I, Z_s}⊗{I, X_m}` and `{I, Z_s}⊗{I, Z_m}` has dimension 6. So the second QM-P
  row is a loose bound, and the true bound is 11,628.
- **The conclusion.** Every frozen fixture is far below `10^5`, so not porting C-SYM's own cap is safe for this
  fixture list. N5 covers the register-size caveat and C.1's existing caps.

## Scope item 4: R10 and the R8 additions

- **R10.** The list is right: the final capture's record, the entries built for the dispatches at `E`, and the
  ratification under R8's default. No round tree can hold them. Q `adds only the receipt`, and G13 freezes the
  record directory.
  - `verdict`'s other host reads are subsumed: its enumeration is covered by the final capture, and the `E` run's
    other records are re-established by a dispatch at `E`.
  - The designation of `E` is an owner designation, which the receipt records.
  - The wording needs B3.
- **R8's additions.** "Under either option, where a host VOID at `E` is retaken, each entry … is ratified the same
  way" agrees with C.8 item 9's *Several dispatches at `E`* and with APPROVAL-ENTRIES ("under its alternative, the
  same cases on the designation of `E`"). The N5 sentence matches the credential table.
- **R8 and N4.** D20 and D23 check only authorship and the quoted sha256 for the designation of `E` and for the
  ratification, which is what the text states.

## Scope item 5: a re-read of changed sections and of sections that read a ruling

- **What was re-read.**
  - The changed sections: title and status; *Inputs*; credential table; invariants; precondition 2; edit log;
    C.2–C.5; C.7; C.8 items 2, 7 and 9; the invariant table.
  - The sections that read a ruling:
    - R1: SG-2, C.7 6 and C.8 item 2;
    - R2: rows 104, 107 and 108, D21's list (496), the *Stop rule* and C.8 item 14;
    - R8: C.3, `verdict`, C.8 item 9, the owner commitments and the credential table;
    - R10: C.2 *Its record* and C.8 item 9.
- **New errors.** B1 (the residue of a pre-existing gap inside the port), B2, B3 and N2–N9. N1 is pre-existing.
  The other added text is consistent and in a neutral register.
- **The build** reproduces byte for byte, and the V3 blocks are unchanged.
- **Control P** catches every pre-`F` placeholder, R10's two included.
- **Authorization.** Nothing implies authorization:
  - the authority block (361–386) is unchanged;
  - precondition 7 still says "c.6740078002 authorizes none of them";
  - the executor precondition, R2's alternative and R10 are frozen rules or owner choices, and none starts work.

  The one implication to watch is the local A3 run: it must be authorized with the design run (scope item 2).

## Scope item 6: owner rulings R1–R10

| ruling | ready as written | what must change |
| --- | --- | --- |
| R1 | yes | — |
| R2 | no | B2: add the control-B rule changes (the `ZipFile` read, `DISPATCH_EVENT`) with M-GUARD variants, and correct D36; N6 optional |
| R3 | yes | — |
| R4 | yes | — |
| R5 | yes | — |
| R6 | yes | (N6 notes R2's alternative's interaction) |
| R7 | yes | — |
| R8 | yes | — |
| R9 | yes | — |
| R10 | no | B3: the narrowing as "conditions of landing" only, the sites to revise, and what each option leaves of the token |

## Probes (`review/probes-r14c/`)

| file | what |
| --- | --- |
| `make_r14c.rebased.py`, `base/` | `make_r14c.py` with only `BASE` changed, to r14b and IMPL r14b copies |
| `rebuild-r14c.md`, `rebuild-IMPL-r14c.md` | its outputs, `d4e0fca9…` and `80df27b0…`, byte-identical to the installed files |
| `fresh.diff` | a fresh r14b→r14c diff, equal to `r14cwork/r14b-r14c.diff` below the header |
| `v3_blocks.py` / `.out` | the V3 blocks of r14, r14a and r14b against r14c: identical |
| `control_p_coverage.py`, `control_p_coverage_r14c.out`, `cp_r14b.out` | control P's rule on r14c (37 caught) and r14b (35) |
| `added_lines.txt` | the diff's added lines, for the register and width scans |
| `v3_verifier_blob.out` | `tools/v3_verifier.py` at `fd539e15` and `origin/main`: blob and sha256 (read-only `git`) |
| `r1_admissible.py` / `.out` | R1's admissible sets over chains of red runs (integers only) |
| `csym_counts.py` / `.out` | scope item 3's per-fixture `E`, `d` and `C(E, d − 1)` (counting, and the integer rank of read indicators; no LP) |
| `sites_r14c.out` | the cited lines for B1–B3 and N3–N7 |
| `qc22_state.out` | Q-C2-2's file sha256 during this review, and r14a's |
