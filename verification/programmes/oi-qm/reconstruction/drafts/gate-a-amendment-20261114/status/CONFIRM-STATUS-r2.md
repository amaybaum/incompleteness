# Confirmation of STATUS-r2.md (landing-status note for the Gate A amendment record, PR #1289)

**This is a model review of the text at the head below, not an owner decision.** It is a
non-author confirmation, read-only and paper-only: reading, `git` inspection of the record
checkout, grep and API reads, 2026-11-14 about 12:38Z–12:48Z. Nothing was computed on OI models, no
Lean was built, no repository checker was run, no workflow was dispatched, and nothing was edited,
committed, pushed or posted in any checkout or on GitHub. It is not independent mathematical
verification (§A.46 item 8). `S2:n` is line n of `STATUS-r2.md`; `RSP:n` is line n of
`RESPONSE-STATUS-r1.md`; `REV` is `REVIEW-STATUS-r1.md`; `r4:n` is line n of `GATE-A-AMEND-r4.md`.

## Exact head

- Branch `research/gate-a-amendment-1169-20261114`, checkout `HEAD` =
  `120ecb975390695237bf6ed88d96c9d1d3530a34`, equal to `git ls-remote origin` and to the PR #1289
  API head; working tree clean. `main` = `dfeec843bec08443b25cffe34d33dc8401c3b604` (unchanged).
- Under review: `verification/programmes/oi-qm/reconstruction/drafts/gate-a-amendment-20261114/status/STATUS-r2.md`,
  214 lines, SHA-256 `48a7efe32a1faa99114d462f4dc3bdc530e00388625c4ab4e659dd04972921dc` (matches the
  brief and `status/README.md`). Also read: `REVIEW-STATUS-r1.md` (SHA-256 `8ceacc9d…`),
  `RESPONSE-STATUS-r1.md` (`482b9eaf…`), `STATUS-r1.md`, `NOTES-STATUS-r1.md`, `status/README.md`.

## How r2 reads at `120ecb97` (one commit after the head it describes)

`120ecb97` is a single-parent child of `927915e9` (committed 12:38:15Z) that adds six files under
`status/` (934 lines) and changes none of the sixteen record files and nothing outside the record
directory. r2 states that its facts were read between 12:10Z and 12:35Z (S2:10–11), before that
commit existed. Read in that light:

- **Head and files (S2:15–19).** True of the record's content head `927915e9`, false of the
  branch head: the branch now differs from `c3b5f37a` in 22 files (4347 added lines) and two new
  directories; the PR reports 6 commits, 6 ahead and 9 behind. The sixteen-file description stays
  correct for the amendment record proper.
- **Review location (S2:6, S2:163, S2:178).** "held outside the repository and not posted on
  GitHub" / "not in the repository or on GitHub" are false at `120ecb97`: the review of r1 is on the
  branch as `status/REVIEW-STATUS-r1.md`. It is still not on `main` and not posted as a comment, so
  the S2:163 classification "support off `main`" stands.
- **Final commit (S2:179).** "the final commit, which adds this note, does not exist yet" stays true
  in r2's sense (the commit that lands the note as `STATUS.md`), but `120ecb97` does add the note,
  as a draft at another path, so the sentence is now ambiguous.
- **CI (S2:180).** Accurate as a record of run 43588379859 at `927915e9`, and r2's own conclusion
  ("The final head needs its own run") still holds. It is overtaken in two facts: a new
  `pull_request` run exists at `120ecb97`, and the PR's test-merge commit is now `b1355802`, not
  `29dd4cda` (details under check 2).
- **Draft state (S2:182).** "5 ahead" is now 6 ahead.

r2 needs a correction for this, but not in place: `STATUS-r2.md` is preserved by digest in
`status/README.md` as an unreviewed draft, so the corrections belong in the next revision (r3, the
text proposed to land as `STATUS.md`). Changes RC-1 to RC-5 below do this.

## Verdict per check

### 1. Dispositions F1–F16: PASS, with one count error (RC-4)

Each disposition in `RESPONSE-STATUS-r1.md` matches the r1→r2 diff, and I checked each finding's
basis at source (list below). F2–F14 and F16 are applied as the review gave them; F4 adds the
clause "naming an accountable Issue for each would close it", and F12 adds the re-check time, both
correct.

- **F1 (modified): right on the merits.** The run record names only the head: run 43588379859 and
  its 27 check runs carry `head_sha` `927915e9` and no merge SHA. `verify.yml` at the head triggers
  `pull_request`, `push` for `main` only, and `workflow_dispatch`; the skipped job has
  `if: ${{ github.event_name == 'workflow_dispatch' }}`. Compare `927915e9...29dd4cda`: `AGENTS.md`
  only. The substitution is the better text. The owner-quoted item 5 says only "Preparation should
  include review of the final commit and CI", and the comment's own summary says item 5 authorizes
  "an exact-head review of the final commit, and CI". Neither says whether a dispatch is included,
  so "none is authorized by item 5" would have read one into an ambiguous record. §A.43 item 4 on
  `main` (a push or draft-PR update "does **not** authorize `workflow_dispatch`") supports the
  wording, and so does §A.40 ("Any special dispatch or launch still requires owner approval
  (§A.43)").
- **F15 (modified): right on the merits.** The review asked for placeholders (`<file name>`,
  `<review file>`, `<commit>`). A note with unresolved placeholders would carry text that is false
  until someone fills it in. The response instead states the proposed path `STATUS.md`, the
  README listing, r1's verdict and that r2 is unreviewed, and lists the r1 review as support off
  `main` closed by landing it with the note. All of this is at S2:3–9, S2:163, S2:178 and S2:200–214.
  The sentence about the review's location was true when written and is overtaken (RC-1, RC-3).
- **Error.** S2:178 says r2 applies the findings "(one in modified form)". The response (RSP:12,
  RSP:26) and `status/README.md` say two (F1, F15). F2 is "applied, with one added fact", not
  modified.

### 2. CI: PASS (no merge-commit coverage claimed); overtaken facts (RC-5)

r2 does not claim coverage of a merge commit. It says a `pull_request` run tests a synthetic merge
(§A.39), names `29dd4cda` only as the PR's test-merge commit at the time, says "which merge commit
the run checked out is not recorded", and requires a run at the final head. Read through the API
by me:

- `927915e9`: 27 check runs, one suite, run 43588379859 (`verify`, `pull_request`, attempt 1,
  11:05:52Z–11:16:17Z), 26 success, 1 skipped (`Numerical probes / A42 exclusion (${{ matrix.part }})`).
  Required contexts `Lean kernel check`, `Mathlib bridge`, `Numerical probes` present and success.
  The only workflow run for that head.
- `120ecb97`: one workflow run, 43595811887 (`verify`, `pull_request`, attempt 1, created
  12:38:22Z, completed success, last updated 12:46:50Z): 27 check runs in one suite, all with
  `head_sha` `120ecb97`, 26 success and 1 skipped (the same dispatch-only job); the required
  contexts `Lean kernel check` (12:39:21Z), `Mathlib bridge` (12:42:39Z) and `Numerical probes`
  (12:46:50Z) success. The PR's `merge_commit_sha` is now
  `b13558029fbcf080885abde6ca77e4d274fe197c` (parents `dfeec843`, `120ecb97`, 12:38:20Z); compare
  `120ecb97...b1355802`: `AGENTS.md` only. The run record again names only the head. No push run and
  no dispatch run at either head.

Neither head is the final head. The branch must still be updated with `main` (check 3), and a run
at the resulting head is still required.

### 3. Gates: PASS on separation; ruleset statement needs correction (RC-6)

r2 keeps completed and outstanding gates apart. S2:176–182 and S2:200–206 list as outstanding the
review of the note, the exact-head review of the final commit, CI at the final head, the owner merge
decision, the draft state and the branch update. S2:138 records that no merge decision exists, and
S2:173–174 that nothing authorizes a merge. The ruleset as I read it (`/rules/branches/main`,
`/rulesets`, `/rulesets/21725642`): ruleset `guardrail`, id 21725642, active, target
`~DEFAULT_BRANCH`. Its rules are `deletion`, `non_fast_forward`, `required_status_checks` (the three
contexts, `strict_required_status_checks_policy: true`) and `pull_request`
(`required_approving_review_count: 0`, `require_code_owner_review: true`, `allowed_merge_methods`
merge, squash, rebase). No `CODEOWNERS` file exists at `dfeec843` or `120ecb97` (root, `.github/`,
`docs/`).

- **Code owners.** r2 states "it also sets `require_code_owner_review`, and `main` has no
  `CODEOWNERS` file" (S2:182). It does not say the requirement is satisfied, but setting the two facts
  side by side invites that inference. The row also omits that the ruleset requires no approving
  review, so the reviews r2 lists as gates are repository-policy requirements (§A.46 item 8), not
  ruleset rules. RC-6 states both facts without inference.
- **Bypass.** "bypass permissions are not visible through the public API" (S2:182) does not match
  my read. Requests in this session go through a proxy that authenticates them, and with that access
  the ruleset record lists `bypass_actors`: one entry, `actor_type` `RepositoryRole`, `actor_id` 5,
  `bypass_mode` `pull_request`. I could not test an unauthenticated read, so the statement may hold
  for anonymous access. As written it is not accurate for the API as read, and the existence of a
  pull-request bypass bears on "Unless bypassed" (S2:182, S2:204).

### 4. Blockers: PASS

S2:137 states the §A.46 item 8 accountable-Issue condition "is not met" for the Bell clause and the
kinematics input. S2:74 and S2:76 give "none named in the record" as their accountable Issue, and
S2:211–212 keeps the question open under §A.45 rule 6 and §A.46 item 4. Remediation entries exist
for both (S2:74, S2:76: what is missing and what would resolve it), so the remaining gap is the
Issue. The two partially verified rows now carry the four remediation fields §A.46 item 4 names
(S2:57–58).

### 5. Accepted contract untouched: PASS

`verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md` has blob
`d9d92e038a8022e854586101067ce4de9789fdf6` at `c3b5f37a`, `fdc3dd7f`, `9d24914c`, `dc0b333a`,
`927915e9`, `120ecb97` and `dfeec843` (179 lines, 113 nonblank). `git diff --name-only
c3b5f37a 120ecb97` touches only the record directory. On `main` the file was last changed at
`fdc3dd7f`.

### 6. Amendment unadopted: PASS; a later owner record must be added (RC-7)

S2:116–118 and S2:123–125 say no record adopts `GATE-A-AMEND-r4.md` as the governing Gate A
contract. That still holds. I read every comment through the paginated API at about 12:40Z: #1169
had 225, the last at 2026-11-14T11:28:20Z (6876591512), and #914 had 67, the last at 11:28:26Z
(6876592679). Re-read at 12:47Z, each has one later comment, both from `amaybaum` (OWNER), posted
after r2's reads ended at 12:35Z:

- **#914 comment 6877420015** (12:42:16Z), "Owner decision recorded: Part 4 of the target, joint
  satisfiability, the derivation ledger, Gate A scope". The owner's words are "Yes I approve,
  proceed as suggested", adopting four items. Item 3 reads: "Keep r4 unadopted until reconciled
  with the strengthened target." and "Gate A should remain the quantum-sector proof gate. It should
  not acquire responsibility for proving the Standard Model, cosmology or black-hole information."
  It also says "satisfying Gate A is necessary for the unified endpoint but insufficient for Part 4",
  and the reconciliation should "preserve the accepted operational obligations and all existing
  negative results". It adopts joint satisfiability "as an explicit mandatory condition of the
  target". Its summary says "The Gate A amendment (PR #1289) stays unadopted; its reconciliation
  with this target is a separate later step."
- **#1169 comment 6877420524** (12:42:18Z), a pointer to it: "This Issue's scope, readiness and
  authorization are unchanged."

So r4 is explicitly kept unadopted by a later owner record. That record adds a condition r2 does
not state: before adoption, r4 is to be reconciled with the four-part target. r2's §2 and §6 item 1
are overtaken on that point. PR #1289 still has 0 issue comments, 0 review comments and 0 reviews.
6876591512 says r4 "is not edited by these answers. It remains the reviewed amendment proposal",
and that adoption of the amended target "requires an explicit owner decision".

### 7. Issue mapping (information only; no change to r2)

- **#868, "Physical source of joint-test validity and composition".** Its stated question is the
  physical source of the joint state/test pairing, product-test validity and the composition
  interface. Its completed T2 unit compares Bell local causality, setting independence, exclusion
  of superquantum correlations and composed experiments. Its next obligation is "one physically
  executing observer-interface map with the pair update/preparer and complete instrument". It fits
  for composites and for the physical sourcing of two-wing preparations and instruments, the
  operational side of B⇐. "Physical instrument sourcing" in general is wider than its body:
  #1169's body routes interaction/access to #866 and reusable instruments to #913. Planning block:
  tier high (provisional); next construction blocked; no next construction authorized.
- **#1060, "BELL-SEL: H-Bell composite closure and Tsirelson selection".** Sub-question 2 ("Does
  OI select the Tsirelson bound among no-signalling correlations?") fits B⇒, the exclusion of
  supraquantum correlations, as a scoped instance inside C. Its body names the Tsirelson bound, not
  selection of the whole quantum correlation set, so "quantum Bell-set selection" goes beyond its
  stated scope unless that is recorded. Sub-question 1 (H-Bell, a graph-family and curvature
  question) is a different obligation. Readiness: blocked on O-K2. Authorization: not authorized.
- **#1169, with #914 as dependency index.** It fits. #1169's body states that the existing
  characterization holds "within an assumed finite-dimensional complex-matrix … setting" and does
  not derive the quantum state space, and that its objective is to "generate or physically source
  the necessary quantum structure". #914 decision 4 (comment 6875046763) allows complex matrices "as
  a conditional mathematical input, not a physical explanation"; #914's title calls it a dependency
  index. Under §A.45 rule 6, #1169 would be the one accountable Issue and #914 the index.
- **#1217, "COMPLEX-CARRIER-1".** It fits as related, not accountable. Its scope is a complex
  structure J on the six-link carrier as a premise of the SM gauge decomposition (parent #1211). It
  states "A complex structure that is mathematically available is not one derived from OI". It does
  not address operational QM kinematics, so it cannot discharge that obligation.
- If the Bell clause goes to two Issues, the note's single Bell row (S2:74) would become two rows
  (B⇐ under #868, B⇒ under #1060), keeping one obligation per accountable Issue (§A.45 rule 6).

## Overall verdict: ACCEPT WITH CHANGES

The four parts of the note stay separate. No status is strengthened, no authorization is implied,
no unadopted choice is read as decided, and no merge-commit coverage is claimed. The open blockers
are stated as blockers. Required changes are needed for four reasons. One count is wrong (RC-4).
The ruleset row's bypass statement does not match the API as read, and its code-owner statement
needs context (RC-6). Statements overtaken by `120ecb97` must be corrected before the note can land
as `STATUS.md` (RC-1 to RC-3, RC-5). A later owner record on #914 must be added to the governance
section (RC-7). None is blocking for the purpose of preserving r2 as a draft.

## Required changes (for r3; `STATUS-r2.md` stays as preserved)

**RC-1. Header, S2:3–11.** Replace with:

> Status note for `verification/programmes/oi-qm/reconstruction/drafts/gate-a-amendment-20261114/`,
> prepared under item 5 of #1169 comment 6876591512, proposed to land in that directory as `STATUS.md`
> and to be listed in its `README.md` contents table (§6 item 9). r1 was reviewed by a non-author
> model review, ACCEPT WITH CHANGES (`status/REVIEW-STATUS-r1.md`, on the record's branch, not on
> `main`); r2 applied its findings (`status/RESPONSE-STATUS-r1.md`) and was confirmed by a non-author
> model review, ACCEPT WITH CHANGES (`CONFIRM-STATUS-r2.md`); this revision, r3, applies that
> confirmation's required changes and has no review of its own. It is status documentation only:
> it is not an authoritative status record until its review is complete, it changes no Gate A
> contract and no scientific status, and it authorizes no merge. Where this note and a cited source
> differ, the source governs (§A.45 rule 1). Facts below were read 2026-11-14 between 12:10Z and
> 12:35Z, except where a later time is stated.

**RC-2. §0 Record pin, S2:15–19.** Replace with:

> - **Record.** Branch `research/gate-a-amendment-1169-20261114`. Content head of the record
>   `927915e9923281dae3da9d414fa349ccbb5d8643`; chain `c3b5f37a` ← `65b0a929` ← `ae2de57a` ←
>   `cea26912` ← `eb515150` ← `927915e9`, all single-parent; sixteen files, 3413 added lines, one new
>   directory. Branch head `120ecb975390695237bf6ed88d96c9d1d3530a34` (checkout `HEAD`,
>   `git ls-remote origin` and the PR API agree), a single-parent child of `927915e9` that adds six
>   files under `status/` (r1 and r2 of this note, the writer's notes, the review of r1, the response
>   and a README with digests; 934 lines) and changes none of the sixteen record files. No path
>   outside the record directory differs from `c3b5f37a` at either head.

**RC-3. §3, off-`main` row S2:163.** Replace with:

> | The non-author review of r1 of this note and the response (`status/REVIEW-STATUS-r1.md`, `status/RESPONSE-STATUS-r1.md`, on the branch at `120ecb97`); the confirmation of r2 (`CONFIRM-STATUS-r2.md`), not on the branch | the review state stated in this note's header and §4 | support off `main` | landing these files with the note (§6 item 9) |

**RC-4. §4, review row S2:178.** Replace the cell "State as read" with:

> r1: non-author model review, ACCEPT WITH CHANGES (four medium, twelve low findings, none blocking), `status/REVIEW-STATUS-r1.md`, on the branch, not on `main`; r2 applies the findings (two in modified form, F1 and F15) and was confirmed by a non-author model review, ACCEPT WITH CHANGES (`CONFIRM-STATUS-r2.md`); r3 applies that confirmation's required changes and has no review of its own

**RC-5. §4, exact-head and CI rows S2:179–180.** Replace the S2:179 cell with:

> none. `927915e9` and `120ecb97` have no exact-head review; neither is the final commit, which is the head that results from adding this note as `STATUS.md` and updating the branch with `main` (row "Draft state and base")

In the S2:180 cell, replace the closing sentence "The final head needs its own run" with:

> At the branch head `120ecb97`: workflow `verify`, run 43595811887, event `pull_request`, attempt 1, 12:38:22Z–12:46:50Z; 26 jobs success, including the required contexts, and 1 skipped (the same dispatch-only job); the PR's test-merge commit is then `b13558029fbcf080885abde6ca77e4d274fe197c` (parents `dfeec843` and `120ecb97`, 12:38:20Z), whose tree differs from the head's only in `AGENTS.md`, and the run record again names only the head. Neither head is the final head, which needs its own run

If r3 is written after a further push, the row records the run at the head then current instead.

**RC-6. §4, draft-state row S2:182, and §6 item 4, S2:200–201.** Replace the S2:182 cell with:

> PR draft (must be marked ready). GitHub reports mergeable, `mergeable_state` `behind` (6 ahead, 9 behind `main`, merge base `c3b5f37a`). The `main` ruleset (`guardrail`, id 21725642, active) requires the status checks `Lean kernel check`, `Mathlib bridge` and `Numerical probes` with branches up to date before merging (`strict_required_status_checks_policy`), blocks deletion and non-fast-forward updates of `main`, and in its pull-request rule allows merge, squash and rebase, requires no approving review (`required_approving_review_count` 0) and sets `require_code_owner_review`. `main` has no `CODEOWNERS` file (root, `.github/`, `docs/`); no code-owner review of this pull request exists, and this note does not determine what that setting requires of it. The reviews listed above are required by §A.46 item 8, not by the ruleset. The ruleset record, read through the authenticated API, lists one bypass actor (repository role id 5, bypass mode `pull_request`); whether it is used is part of the owner merge decision. Unless bypassed, the branch must be updated with `main` before a merge, which creates a new head needing its own exact-head review and CI

Replace §6 item 4 (S2:200–201) with:

> 4. Who performs the ChatGPT exact-head review of the final commit.

**RC-7. §2, later owner record; §6 item 1.** After the pointer bullet (S2:103–105), add:

> - **Part 4 and Gate A scope, #914 comment 6877420015** (2026-11-14T12:42:16Z): "Yes I approve,
>   proceed as suggested", adopting, among four items: "Keep r4 unadopted until reconciled with the
>   strengthened target." and "Gate A should remain the quantum-sector proof gate. It should not
>   acquire responsibility for proving the Standard Model, cosmology or black-hole information."; "The
>   reconciliation should clarify that satisfying Gate A is necessary for the unified endpoint but
>   insufficient for Part 4. It should also preserve the accepted operational obligations and all
>   existing negative results." It also adopts joint satisfiability "as an explicit mandatory
>   condition of the target". Pointer on #1169, comment 6877420524 (12:42:18Z): "This Issue's scope,
>   readiness and authorization are unchanged."

In S2:116, after "`GATE-A-AMEND-r4.md` is not adopted as the governing Gate A contract;", insert
"#914 comment 6877420015 keeps it unadopted "until reconciled with the strengthened target";".
In S2:124–125 replace "(comments through 2026-11-14T11:28:26Z; none later at 12:33Z)" with
"(comments through 2026-11-14T12:42:18Z)", followed by the time of r3's own read. Replace §6 item 1 (S2:195–196) with:

> 1. Whether to adopt r4 as the governing Gate A contract once it is reconciled with the four-part
>    target (#914 comment 6877420015), and whether answers 1–4 and that reconciliation are recorded
>    beside r4 or written into a revised, re-reviewed text.

## Optional suggestions

- **O-1.** S2:59: the exploratory row gives "none" as accountable Issue while the obligations
  table (S2:69–77) names Issues for the same obligations; "see the obligations table" would remove
  the apparent conflict.
- **O-2.** S2:180: cite §A.40 ("Any special dispatch or launch still requires owner approval")
  beside §A.43 item 4.
- **O-3.** S2:173–174: the quotation "It does not authorize the merge, which needs its own owner
  decision" comes from the comment's summary ("What this does and does not change"), not from the
  owner-quoted item 5 text; "#1169 comment 6876591512 states of item 5:" would attribute it exactly.
- **O-4.** §1, GR row (S2:75): the joint-satisfiability condition of #914 comment 6877420015 bears
  on "consistent with E and C"; citing it there would keep the row current. This is optional because
  that record leaves Gate A's scope quantum-only.
- **O-5.** If the coordinator records #868 and #1060 for the Bell clause, split S2:74 by direction
  (check 7). The Bell and kinematics entries at S2:74, S2:76, S2:137 and S2:211–212 then change
  together, and `status/README.md` already anticipates this.

## What I checked myself

- Checkout `HEAD`, clean tree, `git ls-remote` for the branch and `main`; `git show --stat` of
  `120ecb97`; chain and parents `c3b5f37a..120ecb97`; `git diff --stat`/`--name-only` from
  `c3b5f37a` at both heads; blob identity of `GATE-A-AMEND-r4.md`, `OWNER-QUESTIONS-r4.md`,
  `GATE-A-AMEND-r3-TRACE.md`, `README.md` at `927915e9` and `120ecb97`; SHA-256 and line counts of
  the six `status/` files.
- `endpoints.md` blob at seven commits, line counts, last change on `main`; ancestry of
  `fdc3dd7f`, `9d24914c`, `dc0b333a`, `c3b5f37a` (ancestors of `dfeec843`) and `65b0a929`,
  `eb515150` (not ancestors); `git diff c3b5f37a dfeec843`: `AGENTS.md` only; `git grep` at
  `dfeec843` for the record's directory and file names: no hit.
- Full `diff` of `STATUS-r1.md` and `STATUS-r2.md` against each disposition; `REV` in full;
  F5–F9, F13, F14, F16 sources (`REVIEW-r1.md`:3, `CONFIRM-r2.md`:3, :58, `CONFIRM-r3.md`:3–5,
  :34–38, `CONFIRM-r4.md`:3–5, `README.md`:3, :17, :18, :56, r4:7–12, :54–56, :144, :224, :283–284,
  :308–309, :382–383, :410, :428–433, `OWNER-QUESTIONS-r4.md`:44–47, `OWNER-QUESTIONS-r3.md`:8,
  r2:248–250, r3:213, :272–273, :339, :378, :381, `NOTES-r1.md`:33, :58, trace length 101,
  `git diff eb515150 927915e9`, `git diff 65b0a929 ae2de57a -- README.md`,
  `git diff --stat ae2de57a cea26912`); `two-mode-drive.md`:3 and `oi-qm-ext-1/README.md`:26 on
  `main`; EP:29, EP:164; `papers/GR.md`:162.
- `AGENTS.md` at `dfeec843`: §A.46 in full including item 8; §A.43 item 4; §A.40 dispatch
  sentence; §A.45 rule 6.
- `verify.yml` triggers and the dispatch-only job condition; triggers of the other workflows (none
  fires on a push to this branch for these paths).
- API: check runs and workflow runs at both heads; runs 43588379859 and 43595811887; PR #1289
  (state, draft, `mergeable_state`, `merge_commit_sha`, comments, reviews); commits `29dd4cda`,
  `b1355802`; compares `main...120ecb97`, `927915e9...29dd4cda`, `120ecb97...b1355802`; rules for
  `main`, ruleset list and ruleset 21725642; `CODEOWNERS` at three locations; PR #1283 merge facts;
  #1283 comment 6875009394 (author, time).
- Comments read in full: #1169 6876591512, 6875724719, 6703342848; #914 6875046763 (decisions 3,
  4), 6876592679, 6877420015; #1169 6874035457 (author, time, the quoted sentence), 6877420524. All comments on #1169 and
  #914 listed by time. Bodies of #868, #1060, #1217 in full; #1169 body (planning block, scope,
  existing theorem, Gate A–D); #914 body by grep; labels and titles of #868, #1060, #1169, #1217,
  #914, #873.

## What I took from the note without checking

- The amendment's mathematics, the 113-line trace and the reviews' content beyond the passages
  listed above.
- That the coordinating sessions contained the owner wording the comments quote.
- PRs #1287, #1288, #1290 (states, heads, file lists, citations, "no common path") and
  `TARGET-THEOREM-r3.md`:34.
- #873's planning block and #1143 (r2's "selection question on #1143").
- `main` CI at `dfeec843`; `papers/Main.md`:596 beyond its first line; `README.md`:68–73; r4 §1
  quotation checks beyond the comments listed above; `CONFIRM-r4.md` §6 and its O-a to O-e.
- The mapping of GitHub's role id 5 to a named repository role.

## Final reads (12:47Z)

Branch head still `120ecb97`, `main` still `dfeec843`. Run 43595811887 completed success. The PR is
draft and `behind`, test-merge commit `b1355802`, 0 comments, 0 reviews. The two later owner
comments are under check 6.
