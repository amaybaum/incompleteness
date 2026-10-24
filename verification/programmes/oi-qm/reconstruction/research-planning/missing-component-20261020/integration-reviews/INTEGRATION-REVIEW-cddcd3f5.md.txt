# Review of 3a8a3188 (parent 2d555f17), PR #885: integration record, evidence retention, #910 at 00e85e74

Reviewer: independent and read-only. I made no push, no GitHub comment, no dispatch and no repository edit. I used
detached throwaway worktrees at 3a8a3188 and at #910's 00e85e74, and removed both afterwards. Paths below are
relative to `verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/`, and #910
paths are relative to `.../native-y-continuation-20261024/`.

## Verdict: REVISE (2 blocking findings, both small text fixes)

The provenance work is accurate and conservative overall. The diff is exactly the four authorized paths. The protected
sections are byte-identical. The retained review matches its expected digest. Every "not held" item I checked is in
fact absent from the repository and from local disk. Every cited #910 SHA resolves and is an ancestor of 00e85e74.

Two statements need fixing. The q7 row loses the conditional, supplied-resource scope that its review attaches. And the
status "report only" is given to three rows whose review report is not retained either.

## A. Scope and integrity: pass

- `git diff --name-status 2d555f17 3a8a3188` shows exactly four paths: `EVIDENCE-RETENTION.md` (A), `INTEGRATION.md`
  (M), `integration-reviews/INTEGRATION-REVIEW-2d555f17.md` (A) and `integration-reviews/SHA256SUMS` (M). No code or
  data file is touched.
- "The question", "Acceptance rule for instrument candidates", "Supplied, not derived" and "Responsibility" are
  byte-identical to the parent (section-by-section sha256 comparison). Only two hunks change: lines 37–63 and 79–84.
- `INTEGRATION-REVIEW-2d555f17.md` has sha256 `c9f1d9a2d8186d02a8ee5ce985cff2c5113fe68a4e66146e263aac7484654bcc`,
  the expected digest. `cmp` against the handoff copy `reviews/review-885-integration-3.md` shows the two files are
  identical. The renaming follows the earlier pairs (`review-885-integration.md` = `INTEGRATION-REVIEW-1907963e.md`,
  `-2` = `-0be12721`, matched by digest).
- `sha256sum -c` results:
  - `integration-reviews/SHA256SUMS`: 6/6 OK;
  - `mc-node9/design/native-instrument/SHA256SUMS`: 6/6 OK;
  - `review/SHA256SUMS`: 14/14 OK.

## B. EVIDENCE-RETENTION.md

**Native instrument, "reproducible here": verified by replay.**
- `instrument_checks.py` reproduces its saved output byte for byte under `python3 -I -B`.
- So do `indep_cher`, `indep_native`, `indep_register` and `coordinator_weight20`.
- `indep_degree_qm.py` needs sympy. It is not stdlib and is absent from the system python. With sympy 1.14.0 it
  matches except for the missing last line, which is the exception `review/README.md` documents.
- `REVIEW.md` has sha256 `bf61c520…` and equals the handoff's `review-885-native-instrument.md`.

**"Not held" claims: verified.**
- I fetched all 254 remote heads, including 19 not previously local.
- I sha256-hashed every blob in the object store (20,925 blobs, 3.4 GB). I looked for every prefix the reports give:
  `3d18fe9c`, `c204e6f6`, `15af0674`, `529185bb`, `88f80567`, `977e8e33`, `2a51fe2a`, `3e47e54e`, `286d9b1c`,
  `9c2a5dcc`, `e50b51f0`, `05ebed2d`, `c0057e95`, `b8286cb1`, `1eb4eb4e`, `0efc7df3`, `39c47fe8`, `c3a9771d` and
  `4a232a48`.
- The only hit is `c0057e95…` (blob `00c6deaf`).
- I also searched history across all refs by file name. `selector_checks.py`, `native_checks.py`, `law_checks.py`,
  `transport_layout.py`, `relay*.py`, `xplane.py`, `t185_sources*`, `run_bundle.py`, `dump_sources.py`,
  `combined-review`, `native-y-review` and the bundle zips are absent.
  - The `exactlp.py` and `indep.py` files that do exist (`mc-node9/design/cards`, `mc-node9/design/emb/review`) are
    unrelated code.
- A hash scan of 213,971 local files under /tmp, /root and /home found no prefix match.

**compiler.py on #910: correct.**
- `parallel_v3/direct_reset/compiler.py` at 00e85e74 has sha256 `c0057e953656e264…daa3`.
- That matches the prefix `NATIVE-SELECTOR-REVIEW.md:50` gives. The wording "has the sha256 prefix the report gives"
  is scoped correctly.

**Verdict wording.** Nothing reads as rewriting a historical verdict. The file says the verdicts "stand as historical
verdicts of their authors".

## C. INTEGRATION.md and #910

**SHAs.**
- Every cited SHA resolves to a commit and is an ancestor of 00e85e74: `1c8c9e5e`, `bf165400`, `5f6786d6`,
  `9b334367`, `8247de45`, `71d29129`, `8daae9f6`, `6db981c1`, `49a391b9`, `3fcaa271`, `5d36a3f6` and `4f240773`.
- 00e85e74 is an ancestor of #910's head `1c91d315`.
- Commit contents match their labels. Each review commit adds the named `review/` directory. Each author SHA equals the
  revision named in its review: six-source `8daae9f6`, q7 `6db981c1`/`49a391b9`, post-Y `9b334367`.
- The report blobs at 00e85e74 were last changed by those commits.

**00e85e74 is the latest #910 commit that retains a review.** The six commits after it add nothing under `review/`:
- `1324d9a8`, `05397c79`, `1b729355` and `8dd2bc32` are contracts and preregistrations;
- `f24a57a7` and `1c91d315` are author results; `native_x_v12/REPORT.md` says "Separate-author review pending".

**#910 evidence.**
- The 298-entry manifest at 00e85e74 verifies.
- The `SHA256SUMS` files in the relevant modules verify, including `outward_v6/CORRECTION-SHA256SUMS`.
- Four review checkers replay byte-identical to their retained outputs: `junction_v4/review`, `six_source_v5/review`,
  `outward_v6/review` and `phase_joint_v10/review`.
- "Reproducible on #910" is therefore supported.

**Six-source sentence: faithful.** It matches `six_source_v5/REPORT.md` §Result and §2 and its review verdict ("ACCEPT,
within the stated endpoint/preparation scope").

**Post-Y row: numerically faithful.** L=R+9, q8, q9, Z, 5:3:2, z jointly fair, success 5/16 and determinant −1/4 match
`phase_joint_v10/REPORT.md`, its review and `CURRENT-HANDOFF.md`. The review cell quotes the verdict exactly. Note N1
covers the omitted scope.

**Obligation-2 addition.** It is acceptable and keeps the reset and the joint law open.

### Blocking

**B1. `INTEGRATION.md:56`: the q7 sentence drops its review's conditional, supplied-resource scope.**

The text says:

> "A corrected depth-seven outward readout gives the native code (0, 0, y) at q7; it is not an arbitrary-input clean
> socket, a reusable interface or a native reset"

The evidence says otherwise in four places:

- **The review's verdict is conditional.** `outward_v6/review/REPORT.md:3` reads: "ACCEPT the conditional native
  clean-readout construction".
- **The result rests on an added initial source.** That source is f=(0,S,S+2d+14) with payload (u,0,u).
  `CORRECTION-REPORT.md` calls it "a supplied initial correlation/readiness resource, not a constructed native
  initializer". The review says "No native initializer for this correlation is supplied or inferred".
- **It also rests on supplied access.** Every earlier q7 prefix is unchanged, and the prefix at R−7 reveals u, so "The
  receiver must remain private until its designated read under the supplied access rule". The 147 inherited fair
  bits and the joint-frontier theorem are not independently closed.
- **The review's list of negatives is longer.** It also excludes "a complete joint-history/access certificate".
  `CHECKPOINT-CHECKS.json:53` gives the same scope: "full joint-record certification ... OPEN".

"Corrected readout" also misdescribes the result. What changed is the initial apparatus preparation (a seed-only
pulse), not the readout. The owner's authorization names it as the "seed-only q7 preparation". As written, the
sentence moves conditional to unconditional, which the claim/evidence rule forbids.

Suggested text: "Conditionally, with an added seed-only initial source (payload (u, 0, u), a supplied initial
correlation) and supplied access, the depth-seven outward readout gives the native code (0, 0, y) at q7. It is not an
arbitrary-input clean socket, a reusable interface, a native reset or a complete joint-history and access law."

The commit message's "a corrected q7 readout gives (0,0,y)" has the same issue. It is a non-blocking note there, since
history is not rewritten.

## D. Attribution, status labels and rendering

- The 7/30 sentence is now attributed: "as `READ-RESET-REVIEW.md` reports (E1–E3)", which matches
  `READ-RESET-REVIEW.md:60-65`. `EVIDENCE-RETENTION.md:33-35` says no replay from retained material was performed.
- The replay cells now read "reported ... by the coordinating session", and "replay outputs not retained" is stated.
  Neither implies a replay from retained material.
- The native-instrument row stays "reproducible here".
- The table renders with 5 columns. Pandoc gfm gives 51 `<td>`: 9×5 plus the 2×3 responsibility table. Every row has
  6 unescaped pipes.
- I found no self-narration of revision history in the documents.

### Blocking

**B2. "report only" is applied where no review report is retained, which overstates retention.**

Both files define the status as "the review report is retained, but [not the material it ran on]"
(`INTEGRATION.md:43-44`, `EVIDENCE-RETENTION.md:12-13`). Three rows do not meet that definition.

- **Native X: `INTEGRATION.md:53` and `EVIDENCE-RETENTION.md:26`.** The row is labelled "report only (external)".
  Its own "Not held" cell lists "the external review text". My scan found no blob or local file with prefix `2a51fe2a`.
- **Combined handoff (`INTEGRATION.md:54`, `EVIDENCE-RETENTION.md:27`) and native-Y continuation (`INTEGRATION.md:55`,
  `EVIDENCE-RETENTION.md:28`).** The "review" is the coordinating session's replays. No report of them is retained,
  and "Held here" is "—". The only retained trace is the citation of `replay.out` in
  `INTEGRATION-REVIEW-1907963e.md:115` and `:130`.

The owner asked for missing code and outputs to be marked unavailable. These rows need a third status, for example
*not retained (cited only)*. The alternative is a scoped label such as "report only: `INTEGRATION-REVIEW-1907963e.md`
cites the replay outputs, which are not retained" and "not retained: external review text unavailable". Whichever
wording is chosen, the definitions at `INTEGRATION.md:42-45` and `EVIDENCE-RETENTION.md:8-13` should match.

## E. Sensitive data: pass

- The added lines contain no addresses, tokens, URLs, IP addresses, local paths or personal data.
- The only grep hits are "private keys", in the unchanged one-time-pad sentence, and "@q_Y", in the retained review.
- The commit author is `noreply@anthropic.com`.

## Notes (non-blocking)

- **N1. `INTEGRATION.md:57`, post-Y row.** "Conditional on #910's retained native family" carries most of the scope.
  Several of the author's and reviewer's qualifiers are missing:
  - "under the supplied initialization and access assumptions";
  - the stipulated six-bit fair seed bank (a, b, k0, k1, k2, z);
  - that E_phase "is a coordinate comparison, not a newly available physical observer operation";
  - that previous-slice Y access is open;
  - that the terminal read is the candidate's *stipulated* whole-q9 read.

  The author calls the result a "phase-preparation candidate", while obligation 2 (`:82`) says "#910 constructs". I
  recommend adding "under a stipulated fresh seed bank and supplied access" when B1 is fixed.
- **N2. `EVIDENCE-RETENTION.md:26-28` understate what #910 holds.**
  - #910 holds `continuation/core.py` (sha256 `b1615592…`). #910's own `continuation/PROVENANCE.json` and
    `REPORT.md:149` call it "byte-for-byte from the accepted native-Y handoff" (977e8e33). No #885 report gives its
    digest, so the claim cannot be cross-checked here.
  - `direct_reset/PROVENANCE.json` names compiler.py's source as the combined handoff
    (`oi_native_x_instrument_v1/compiler.py`). The note that the file is held on #910 therefore applies to the native-X
    and combined rows as well.

  These omissions are conservative, but they are inconsistent with the compiler.py note.
- **N3. `EVIDENCE-RETENTION.md:23`.** "the reviewer's `indep.py` and its mutants": `SELECTOR-RECORD-REVIEW.md:45`
  says the five mutations were of the *author's* checker. Suggested wording: "the reviewer's `indep.py`; the mutants
  of the author's checker".
- **N4. §A.25 mirror.** The PR #885 description (line 11) still says #910 "is currently at `1c8c9e5e`". It should cite
  00e85e74 when next edited. This is outside the commit.
- **N5.** The native-instrument replay needs sympy for `indep_degree_qm.py`. A one-line requirement note beside
  "reproducible here" would make it self-contained.
- **N6.** Gate 1 is not marked closed in either document. The commit message keeps 2d555f17 as the accepted synthesis
  pending review, as instructed.

***

# Re-review of 222f7973 (parent 3a8a3188): fixes for the REVISE of 3a8a3188

Read-only, as before. I used throwaway worktrees at 222f7973 and at #910's 00e85e74, and removed both afterwards.

## Verdict: REVISE (1 blocking finding, a one-line fix)

B1 and B2 are fixed faithfully. N1, N2, N3 and N5 are applied accurately. Scope and integrity hold. One status
inconsistency remains in `EVIDENCE-RETENTION.md`, and it fails check (3).

## (1) B1 and B2: fixed

**B1 (`INTEGRATION.md:58`).** The sentence now reads: "Conditionally, with an added seed-only initial source (a
supplied initial correlation and readiness resource, not a constructed native initializer) and supplied access (the
receiver stays private until its designated read) … not … a complete joint-history and access law". It matches #910
at 00e85e74:
- `outward_v6/CORRECTION-REPORT.md` §1: "a supplied initial correlation/readiness resource, not a constructed native
  initializer";
- `outward_v6/review/REPORT.md:3`: "ACCEPT the conditional native clean-readout construction";
- the same review, under "Access, resources and remaining boundary": "must remain private until its designated read
  under the supplied access rule";
- the same review, l.6–7: "a complete joint-history/access certificate", listed among what the result is not.

"Corrected" is gone.

**B2.** Native X, the combined handoff and the native-Y continuation are now "not retained (cited only)" in both
files (`INTEGRATION.md:55-57`, `EVIDENCE-RETENTION.md:28-30`). The definition is added in both files. The closing
bullet of `EVIDENCE-RETENTION.md` now says neither those reports nor their outputs are retained.

## (2) Notes as applied: accurate

**N1 (`INTEGRATION.md:59`, obligation 2 at `:84`).** The row now has:
- "two-slice phase-preparation candidate", matching `phase_joint_v10/REPORT.md` l.10;
- "supplied initialization and access", matching l.5–6;
- "stipulated six-bit fair seed bank", matching "(a,b,k0,k1,k2,z), six bits … under the stipulated initial
  preparation";
- "coordinate comparison, not an observer operation", matching "a coordinate comparison, not a newly available
  physical observer operation";
- "previous-slice Y access is open", matching the review's "Previous-slice Y access … remain open".

**N2 (`core.py`): verified at 00e85e74.**
- `continuation/PROVENANCE.json` gives `source_handoff_sha256` `977e8e33…` and `core_sha256` `b1615592…`.
- `continuation/core.py` hashes to `b1615592…`.
- `continuation/REPORT.md:149` reads: "The copied `core.py` is byte-for-byte from the accepted native-Y handoff."
- The attribution "per #910's provenance records" is correctly scoped.

**N2 (`compiler.py` and the combined bundle).** The link is indirect.
- `parallel_v3/direct_reset/PROVENANCE.json` names `baseline/OI_combined_handoff_2026-10-24_v1/…/compiler.py`.
- The archive name is tied to `88f80567` only through `transport_audit_v1/PROVENANCE.json` (`combined_handoff_sha256`
  with `combined_handoff/workspace/…` paths).
- "Per #910's provenance records" is still a fair attribution.

**N3.** The cell now reads "the mutated copies of the author's checker that the review ran", matching
`SELECTOR-RECORD-REVIEW.md:45`.

**N5.** The cell now reads "reproducible here (`review/indep_degree_qm.py` needs SymPy)", which is correct.

## (3) Status definitions: one inconsistency (blocking)

**R1. The status definitions in `EVIDENCE-RETENTION.md` do not cover the statuses its table uses.**
- `:8` still says "Two statuses are distinguished:", but three bullets follow (`:10-15`). This is a stale count
  (§A.30).
- The #910 row (`:31`) uses the status "reproducible on #910". That status is not defined in this file.
- `INTEGRATION.md:42-46` defines four statuses, the fourth being "*on #910*", and its #910 rows use "on #910".

Fix:
- change "Two" to "Four";
- add a bullet defining "reproducible on #910": the reviewed material and the review checkers are on #910's branch.
  INTEGRATION.md abbreviates it as *on #910*. Alternatively, use the same label in both files.

Every other row follows its definition:
- the native instrument is "reproducible here";
- the selector-record, native-selector and read-reset rows are "report only", and each report is in
  `integration-reviews/`;
- the native-X, combined and continuation rows are "not retained (cited only)".

## (4) Scope and integrity: pass

- `git diff --name-status 3a8a3188 222f7973` shows only `INTEGRATION.md` and `EVIDENCE-RETENTION.md`.
- "The question", "Acceptance rule for instrument candidates", "Supplied, not derived" and "Responsibility" are
  byte-identical to 2d555f17.
- `integration-reviews/SHA256SUMS` verifies 6/6. Since 2d555f17 that directory has gained only the review file and
  its sum line.
- The tables render with 5 columns (pandoc gfm: 51 and 40 `<td>`).

## (5) New overclaims: none

Every edit adds a qualifier or narrows a status. No claim is strengthened. No sensitive data is added.

***

# Narrow check of cddcd3f5 (parent 222f7973): R1

## Verdict: ACCEPT

- **The diff touches one file.** `git diff --name-status 222f7973 cddcd3f5` lists only `EVIDENCE-RETENTION.md`.
- **The hunks are only the R1 fix:**
  - "Two statuses are distinguished:" becomes "Four statuses are distinguished, the same as in `INTEGRATION.md`:";
  - the third bullet's final full stop becomes a semicolon;
  - a fourth bullet is added: "**on #910**: the material, with #910's own retained reviews and checkers, is held on
    #910's branch";
  - in the #910 row, "reproducible on #910" becomes "on #910".
- **The four definitions match `INTEGRATION.md:42-46`.** They are reproducible here, report only, not retained (cited
  only) and on #910.
  - "On #910" in `EVIDENCE-RETENTION.md` adds that #910's reviews and checkers are held there. That is consistent with
    INTEGRATION.md's definition and is true: four of #910's review checkers replayed byte-identical at 00e85e74.
- **Every row in both files uses one of the four labels.**
  - INTEGRATION.md: reproducible here ×1, report only ×3, not retained (cited only) ×3, on #910 ×2.
  - EVIDENCE-RETENTION.md: the same, except one on #910 row.
  - The only addition anywhere is the native-instrument row's parenthetical "(`review/indep_degree_qm.py` needs
    SymPy)", unchanged since 222f7973.
- **Nothing else changed.**

Read-only check: I read the commit from the object store with `git show`/`git diff` and created no worktree. I made
no push, comment, edit or dispatch.
