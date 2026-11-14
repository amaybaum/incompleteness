# Review: ARP-3 (Q-C2-2) preregistration r14b, an independent review

**Standing.** WIP / UNVERIFIED review note. Model-written. Read-only.
- **What was not done.** No repository, git or GitHub write (one read-only `git fetch` of `origin/main`). No LP,
  simplex or script self-test. No computation on F1, `G_SM` or any OI construction. Q-C2-1's files read only.
- **Ignored.** `review/probes-r14b/`, left by an interrupted reviewer, was not read or used. This review's probes are
  in `review/probes-r14b-rv/`.
- **Freshness check (first step).** `#1169` comments since 2026-11-09 and every pull request updated since then were
  listed through the REST API. No Q-C2-2 revision newer than r14b exists. The latest mentions are status notes:
  - c.6743475622 (2026-11-09T15:09:48Z): "r14b written (`e8f5fcfb`); its review interrupted | Re-run the review";
  - c.6791556736 (2026-11-11T08:56:22Z, Bell-first reset): Q-C2-2 is "parked" pending the Bell-scope paper decision.

  That is a priority fact, not a defect of the draft. It is recorded here because it bears on when, not whether,
  these findings matter.

## Objects (hashes verified)

| object | sha256 |
| --- | --- |
| `preregistration.draft.md` r14b | `e8f5fcfb48ed861b3e2a14f37a6d333e37baafaf722130a7931bb756aca9bed9` ✓ |
| `r14a/preregistration.draft.md` | `d751a127582748093491da416cfb024ac8db319f72b8f3206334abe7d35447ae` ✓ |
| `DECISIONS-QC22-preF.md` (r14b) / `r14a/` copy | `555bf629…ced3` ✓ / `545ce34c…f571` ✓ |
| `DISPOSITIONS-r14b.md` | `927e92959b740c20f3589cabc9641ad0c893252baae6b9dc1ffb3f74480ce44d` |
| `IMPL-DELTA-r14b.md` | `51b74acfa271091d1a798beea2b8df2aa834c94a07ca51cd347f6f438aa2db39` |
| `review/REVIEW-QC22-r14a.md` | `c63ca1cc…1a1361` ✓ |
| `r14bwork/make_r14b.py` / `make_sheet_r14b.py` | `99e9ea77…0290` / `cd4fc4d5…d0d0` |
| Q-C2-1 `preregistration.draft.md` (r14c, read only) | `d4e0fca9…1ef7` |
| `origin/main` `verify.yml`, for the skip check | at `cac5d26441dd33e9348151487e4df7b547195481` |

**Reproduction.** `make_r14b.py` on r14a applies 26 edits and `make_sheet_r14b.py` on the r14a sheet applies 12.
Both outputs are `cmp`-identical to the installed files. Both scripts read one input and write one output. The
`v3-round` and `v3-governed-paths` blocks are equal in r14a and r14b (`review/probes-r14/p01_v3blocks.py`).
The diff r14a→r14b has 148 changed lines, every one traced to a finding in `DISPOSITIONS-r14b.md`.

## Verdict: **REVISE** (three blockers, each cheap)

- **The r14a findings are all disposed, and each fix compares the right object (§1).** Rc1 is fixed by the r14a
  review's route (a), with the residual named, an executor precondition and a self-test.
- **The three blockers below were not in the r14a review.** B1 is the Q-C2-2 copy of Q-C2-1's R14C-B1. That review
  flagged it for Q-C2-2 ("Report it there"), but was written at 14:52Z, after r14b (14:41Z). B2 is the latent defect
  the owner ruled on for Q-C2-1 (c.6784808669). B3 is the activity-pagination trap, on `T0`.
- **Unchanged and sound.** The mathematics, the decision rule, the tokens and the frozen expectations. The owner
  quotes are verbatim: 36 of 36 in *Authority*, plus the sheet's quotes. The 34 `PENDING` fields block `F`. No owner
  option is read as chosen.

## Blockers

### QC22-r14b-B1. `F`'s designation comment is read, but it is not bound to `F` or to the owner

- **The rule** (1670–1673). The comment is read by "its id given as an argument". Its `created_at` and `updated_at`
  must precede "the first execution run's `created_at`", and `order.json` "records its id, author and times".
  - Nothing requires the comment to quote `F`'s full commit id.
  - Nothing requires it to be authored by `amaybaum` with association `OWNER`.
  - So any comment created earlier passes, including an unrelated earlier owner comment.
  - APPROVALS (796–797) tests only the timing case.
- **"The first execution run"** (1670, 1672, 1865) is not defined.
- **Contrast.** Approval comments must quote the full commit id and the stage, and must pass authorship (1616–1627).
- **Why it blocks.** The invariant rows at 1865 ("`F` designated before the first execution run") and 1900 cite this
  read as their checkpoint. As written, the read does not measure it (§A.41). That checkpoint is the owner's control
  over c.6723329527's "No automatic freezes".
- **Repair.** Port Q-C2-1 r14c's R14C-B1 fix and its N4.
  - The comment's author is `amaybaum`, with association `OWNER`.
  - Its body contains `F`'s full 40-hex id.
  - `order.json` also records the quoted words (§A.42 item 7).
  - Define the first execution run as the earliest-created run, of any event, whose `head_sha` is a commit after
    `F` that descends from `F`. This excludes `F`'s own dispatch and includes the `pull_request` run at S1's push.
  - Add two APPROVALS cases: a designation that does not quote `F`, and one by another author. Mirror both in
    IMPL-DELTA.

### QC22-r14b-B2. The whole-run conclusion rules do not admit the skips that `D`'s `verify.yml` produces

The trap is the one the owner ruled on for Q-C2-1 (c.6784808669). Q-C2-2 has it in two places, and the second is
worse.

- **At the design run and at 6′** (`pull_request` runs).
  - The rule (2159–2160) is "every job and step conclusion in it is `success` … except job B, which is `skipped`".
    It is checked by `check --freeze`, and 2105 and 2150 say the same in prose.
  - On `pull_request` at `cac5d264`, these are `skipped` by their own `if:`
    (`review/probes-r14b-rv/q3_verify_main_ifs.out`; #1218 run 42891278321 showed exactly these three):
    - the job `Numerical probes / A42 exclusion (${{ matrix.part }})` (661);
    - the step `ARP-1-MARC keep the measurements` (732);
    - the step `KTRANS-SEP-2 marker complete reports with an axiom outside the three` (201). It is skipped
      whenever the axiom-report step succeeds.
  - So `check --freeze` cannot pass, and `F` is unobtainable (fail-closed).
- **At S1 and `E`** (decisive dispatches).
  - The rule (1790) is "every job's conclusion is `success`".
  - `D` is `main` after ARP-2's landing. If Q-C2-1's splice is there, its job `probes_arp2qc21_decisive` has the
    job-level `if:` `… && inputs.arp2qc21_decisive == true`, from Q-C2-1 2264. It is therefore `skipped` in every
    Q-C2-2 dispatch.
  - `verdict` would then print VOID at S1 and `E` by construction, after `F`, with no retake.
  - Rounds landed before `D` with a gated job of their own do the same.
- **Precondition 8** ("green on every job", 2259) has the same ambiguity at `F`'s input-less dispatch.
- **Repair (method choice; record it on the decision sheet, since the owner's ruling is scoped to Q-C2-1).**
  - **(a) Mirror c.6784808669 exactly.** Use a keyed expected-conclusion table, built against `D`'s `verify.yml`
    (`PENDING` until `D`), with each keyed `if:` text byte-matched against `D`:
    - the A42 exclusion job, and ARP-1's keep step: `skipped` on `pull_request`, `success` on dispatch;
    - the KTRANS marker: `skipped`, and the axiom-report step `success`. A marker `success` fails;
    - each earlier round's input-gated decisive job, Q-C2-1's job B included: `skipped`;
    - each earlier round's receipt-keyed and dispatch-keyed steps, such as Q-C2-1's A10 and B6: their keyed values;
    - every other job and step: `success`. Every unlisted skip fails;
    - mutation-tested in both directions.
  - **(b) Or narrow the whole-run conditions.** Require the run's own `conclusion` to be `success`, and keep the
    per-step requirements for Q-C2-2's jobs A and B and the aggregate only. A `success` KTRANS marker implies a failed
    axiom-report step, so a failed job and a failed run, and (b) still catches it.
  - Either way, add the cross-round case, an earlier round's gated job `skipped` at S1, to the `verdict` self-test.

### QC22-r14b-B3. `T0` is a hand-filled value with no reader and no checkpoint, on a cursor-paginated endpoint

- **Why `T0` matters.** It bounds set (2) of the enumeration (1676, 1680). So it carries the completeness claim of
  owner requirement 1's "detected and VOID" row (1881).
- **How the text sets it.** Its value is "the `timestamp` of the entry with `after = D` in
  `GET activity?ref=refs/heads/main`" (1745–1746), filled by hand at `PENDING`. Control P checks only that it is
  filled. No `check` mode re-reads it.
  - If the value is later than `D`'s true host time, set (2) silently drops runs created between the two (§A.41).
- **Host facts, read-only, 2026-11-11 (`review/probes-r14b-rv/q2_host.out`).**
  - `activity` is cursor-paginated. Its `Link` header carries `after=<cursor>`, and `page=2` returns the same ids as
    `page=1`. So a `page=N` loop cannot reach an entry past the first page.
  - In this session, `gh api --paginate` follows `Link` URLs of the form `repositories/<id>/…`. The proxy refuses
    those with 403 ("Numeric-ID repository paths … are not supported"), so it exits 1 at page 2, on `activity` and on
    `jobs` alike.
  - A cursor is not an `a_ok` type. So, as frozen (control B (g)), session-run `controls.py` cannot page `activity`
    at all.
- **Repair.**
  - Name the reader of `T0` and its checkpoint. For example, `check --freeze` and each capture re-read `activity`
    for `main` and require exactly one entry with `after = D`, whose `timestamp` is `T0`, recording the read.
  - Specify the paging. Either a run in CI, or an `a_ok` type for the cursor (base64url, bounded length) in a frozen
    `activity?ref=refs/heads/main&per_page=100&after={CURSOR}` template, with a page-array check.
  - Alternatively, admit any `T0` at or before `D`'s host time, which is conservative because set (2) only grows, and
    verify that bound.

## 1. The r14a findings

| r14a finding | fixed? | checked |
| --- | --- | --- |
| **Rc1** | ✓ | See below. |
| **N1** authorization | ✓ | 43–52 and row 205 call it the coordinator's reading. c.6740747027's words match verbatim. |
| **N2** R6 alternative | ✓ | 1946–1949 carries Q-C2-1 r14b's clause and "reviewed revision". The sheet row is corrected and **[R]**. |
| **N3** item 8 dispositions | ✓ | (i) "only as conditions of landing"; (ii) "Applying the choice" names the sites; (iii) "What each option leaves". No option is chosen. The sheet row matches. |
| **N4** off-`main` completeness | ✓ | 842–844 and 281–283 now read as predictions. Rows 211 and 224 are added. |
| **N5** re-establishment route | ✓ | Row 223 and 1557–1559 use a new branch at `E`, added to the policy after closure. No ref is moved (§A.43 item 4). |
| **N6** M-RAY | ✓ | "An extreme row …" (687–689), on both sides. IMPL B6 forbids "first listed row". |
| **N7** | ✓ | 1686 makes no assertion about pre-`D` pushes. |
| **N8** E-ID (iv) | ✓ | 2085–2088 say no condition reads it. IMPL B7 corrects r14a A8. |
| **N9** sheet | ✓ | §0, §1, §2, §6, §7 and §8 are updated. §8's "three rows" is right. |
| §2 residuals; optional items | ✓ | 1900, 790–791, 1847–1848, 857, 647 and 903–907. The re-wrap is whitespace only. |

**Rc1 in detail.**
- **The rule (1752–1756) and IMPL A1 agree.** `review/probes-r14b-rv/q1_nof1.py` implements the rule as written. It
  gives the NOF1 expectation on all 19 cases (800–803, with B4 `success` crossed with every A3/A3b pair).
- **The safety argument is right.** An `if:` without a status function implies `success()`, so A4–A11 are skipped
  with A3. A3b (`always()`) runs `controls.py` only. A1 and A2 start no checker.
- **`verify.yml` has no `concurrency:` block** (`cac5d264`). So no host-side cancel-in-progress can turn A3 into
  `cancelled` on a recorded branch.
- **Precondition 6's clause is corrected consistently.** A design-run A3 timeout is now known before `F` and blocks
  it, instead of voiding the round after `F`.
- **The residual is named, and the executor precondition is frozen (§A.41).**
- **IMPL's local command matches A3 byte for byte,** apart from `$T`.

## 2. Nits

- **N1 (Rc1's "A3 absent" is broader than its argument).**
  - The argument covers two cases: job A never started, or it failed before A3.
  - The predicate also passes a job A that is present, has A1 and A2 `success`, and has no step named A3 (q1, last
    line). That is a renamed step on a recorded-branch commit whose job carries a frozen display name. r14a made
    that a violation through A3b.
  - Restrict "A3 absent" to job A absent, or to a job whose steps after A2 are absent or `skipped` with A1 or A2 not
    `success`. Add that NOF1 case.
- **N2 (pagination mechanics generally; see B3's facts).**
  - "Every page" is required of jobs (1701), artifacts (1799) and deployments (1646). Their frozen templates have no
    page slot, and `--paginate` fails in this session.
  - Either add `&page={DEC}`, or require `total_count ≤ per_page` with a failed capture otherwise.
  - Say how object pages are parsed. Q-C2-1 added `--slurp` (its D5). Without it, object pages are separate JSON
    documents (not verified here, since the proxy refused page 2 first).
- **N3 (design-run residual's consequence, 2142–2144).** "`F` is then not requested" leaves the round with no route.
  - The violation stays in set (2) for this `D`.
  - Say that the remedy is a re-cut from a later `D`, with new recorded-branch names. The incident then predates the
    new `T0`.
- **N4 (decision sheet §0).**
  - "Resolved by c.6740593434" rests on a session-generated comment posted with the owner's credential (the sheet
    says so). It is the coordinator's reading of the option text "You create the Environment, since I can't", whose
    "You" and "I" are the session's.
  - Label it as that reading, as R14a-N1 does for the authorization, and let the owner correct it.
  - Also, "Owner records used … quoted verbatim" now lists a comment that records no owner decision.
- **N5 (optional, executor precondition).** Nothing records that the local run happened. A posted sha256 of the
  local `fixtures.json` per push, on the guiding PR, would give it a checkpoint at no cost.

## 3. Owner decisions, controls, §A.42 item 8, §A.44, register

- **Owner decisions.** 34 unbackticked `PENDING` fields (`review/probes-r14/p02_pending.py`), unchanged from r14a.
  - The two dispositions that need a reviewed revision say so (1949, 1964–1969). So control P alone does not let a
    filled record id stand in for the revision; precondition 4's review does that.
  - No option is selected anywhere.
  - B2's choice should be added to the sheet.
- **Controls are not vacuous.**
  - NOF1 drives both directions.
  - M-RAY now removes extreme rows only, so the mutation is invalid by construction.
  - The F-designation check is the one vacuous checkpoint (B1).
- **§A.42 item 8.**
  - The new references are classified: Q-C2-1 r14b (provenance), DISPOSITIONS-r14b (provenance) and S1's artifact
    (support when read).
  - The local fixture run is a commitment, not a landed claim.
  - `T0`'s activity read is an unclassified host read (B3).
- **§A.44.** Rc1 reads A3's and A3b's conclusions from the jobs API. No condition reads log text.
- **Register.** The 104 added lines contain no §A.32/§A.33 phrase and no unlisted caps token. Outside tables, only
  the title line is over 120 characters.

## 4. What ran (`review/probes-r14b-rv/`; reviewer checks, not evidence)

| file | what |
| --- | --- |
| `r14b.rebuilt.md`, `sheet.rebuilt.md` | the writer's generators on r14a; `cmp`-identical |
| `added.txt` | added lines r14a→r14b (register screen) |
| `q1_nof1.py` / `q1.out` | the rule as written, on synthetic attempt records: 19 NOF1 cases, 0 mismatches; N1's case passes |
| `q2_host.out`, `q2_paged_obj.raw` | read-only `gh api`: activity `page=1` = `page=2`; cursor `Link`; `--paginate` exits 1 (403) at page 2 in this session |
| `q3_verify_main_ifs.out` | `if:` lines of `origin/main`'s `verify.yml` at `cac5d264` |
| `q4_quotes.py` / `q4.out` | 36 Authority quotes checked verbatim against the comments, fetched read-only: 0 missing |
| (reused) `review/probes-r14/p01_v3blocks.py`, `p02_pending.py` | V3 blocks equal; 34 `PENDING` |
