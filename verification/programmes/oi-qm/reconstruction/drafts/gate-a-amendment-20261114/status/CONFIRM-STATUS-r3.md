# Focused review of STATUS-r3.md (landing-status note for the Gate A amendment record, PR #1289)

**This is a model review of the text at the head below, not an owner decision.** It is a
non-author, read-only, paper-only review: reading, `git` inspection of the record checkout, grep
and API reads, 2026-11-14 about 12:53Z–13:00Z. Nothing was computed on OI models, no Lean was built,
no checker was run, no workflow was dispatched, and nothing was edited, committed, pushed or posted.
It is not independent mathematical verification (§A.46 item 8). The scope is the five questions
of the request; anything else is optional. `S3:n` is line n of `STATUS-r3.md`.

## Exact head

- Branch `research/gate-a-amendment-1169-20261114`, checkout `HEAD` =
  `acfdbd0fa27b0834047efef760da464efe627198`, equal to `git ls-remote origin` and the PR #1289 API
  head; working tree clean; `main` = `dfeec843bec08443b25cffe34d33dc8401c3b604`.
- `status/STATUS-r3.md`: 247 lines, SHA-256
  `3258dbe231923f7c1604803ecb630a8790e58741951d48020bd600a05d5861ba` (matches the request and
  `status/README.md`). Also read: `status/RESPONSE-CONFIRM-STATUS-r2.md` and `status/README.md`.
  `status/CONFIRM-STATUS-r2.md` on the branch (blob `ff687f78`) has the same SHA-256 as the
  confirmation I wrote (`9c57f4ef…`).
- Chain: `927915e9` ← `120ecb97` ← `b3cc7182` (12:48:53Z, adds the confirmation of r2) ←
  `acfdbd0f` (12:52:54Z, adds r3 and its response, updates `status/README.md`). None changes a
  file outside `status/`. `endpoints.md` still has blob `d9d92e03` at `acfdbd0f`.

## 1. RC-1 to RC-7 and O-1 to O-5: PASS

Every disposition in the response matches the r2→r3 diff:

- **RC-1, RC-3, RC-4, RC-6.** Applied. RC-1 and RC-3 name the review files under `status/`, which
  is correct because they are on the branch. RC-6 keeps "whether r3 needs a confirmation review" in
  §6 item 4, which is right for an unreviewed r3.
- **RC-5, RC-7.** Applied as given.
- **O-1 to O-5.** Applied.
- **RC-2 (modified): right.** It describes the content head `927915e9` separately from the
  commits after it.

**How to read r3's head and CI statements at `acfdbd0f`.** A revision of this note cannot name the
commit that adds it: every revision committed to the branch moves the head past what it describes.
r3 dates its head statement ("agree at 12:49Z", S3:25) and its CI statement ("in progress at
12:50Z", S3:210). Read as dated facts they are accurate. At `acfdbd0f` they are overtaken in three
places:

- the branch differs from `c3b5f37a` in 25 files (4979 added lines), not 23 (4701);
- the PR reports 8 commits;
- the test-merge commit is `4d0233210ec6183fdb44ce4b8a3cb22fdb48e69f`.

Run 43596656232 at `b3cc7182` was still in progress at 12:55Z (24 success, 1 skipped, 1 in
progress). Run 43596974572 at `acfdbd0f`, event `pull_request`, created 12:53:01Z, was in progress
at 12:55Z.

The substance stands at the new head: every commit after `927915e9` changes only `status/`,
neither head is the final head, and each needs its own run. No required change follows from the
moved head. Optional O-A below makes the dating explicit. The landing text (`STATUS.md`) has to
restate the head and CI at the final head in any case.

## 2. Accountable-Issue mapping: CHANGES REQUIRED (RQ-1)

**#1169 comment 6877532844** (`amaybaum`, OWNER, 2026-11-14T12:52:30Z) now records the approval:
"I approve the following:". It quotes the relayed recommendation, including a four-row table:

- "Bell operational coverage, composites and physical instrument sourcing | #868";
- "Quantum Bell-set selection and Tsirelson bound | #1060";
- "Complex kinematics for full operational QM | #1169, with #914 as the dependency index";
- "Complex structure on the SM six-link carrier | #1217".

It also quotes "#1217 specifically concerns the SM's six-link carrier and cannot discharge the
broader Gate A obligation to physically source complex quantum kinematics" and "I recommend
naming the existing Issues rather than opening duplicates". Its scope section says:

- "It changes no Issue's scope, planning block, tier, readiness or authorization";
- #868 "covers two-wing instruments, not instrument sourcing in general";
- #1060 "covers the Tsirelson bound, not selection of the whole quantum set";
- "Excluding supraquantum correlations other than the Tsirelson bound has no accountable Issue
  named";
- "No CI dispatch, branch update or merge is authorized by this record."

It was posted after r3's reads, which ended at 12:52Z. r3's statement that no GitHub record exists
(S3:74–77, S3:165, S3:192, S3:242–245) is now overtaken and must be corrected (RQ-1). Once the note
quotes the approval with author and time, the approval moves from support off `main` to support on
`main` through quotation (§A.42 item 7), like the other owner comments.

**The split, against the Issue bodies.**

- **#868 for B⇐ and two-wing instruments: fits.** The body asks for the physical source of "the
  joint state/test pairing, validity of the required product tests and the locally tomographic
  composition interface". r3's caveat matches the record's scope section, and the routing of
  general instrument sourcing to #866/#913 matches #1169's body.
- **#1060 for the Tsirelson bound: fits.** Sub-question 2 is quoted exactly.
- **Kinematics under #1169 with #914 as index: fits.** The quotations from #1169's body are exact,
  including the bold "**assumed**".
- **#1217 as related only: fits.** The quotations are exact, and the approval record's own #1217
  sentence agrees.

One point r3 must state (RQ-1): the owner-approved row assigns #1060 to "Quantum Bell-set
selection and Tsirelson bound". The scope section of the same record says #1060's body covers only
the Tsirelson bound, and that excluding the other correlations "has no accountable Issue named".
r3's "no accountable Issue" agrees with the scope section. It does not mention that the approved row
names #1060 for Bell-set selection, so the record diverges internally on that point.

## 3. §A.46 item 8 Issue condition: right conclusion; basis should be stated (RQ-2)

On `main`, §A.46 item 8's fourth condition is: "it has an accountable Issue, a verification status
and, for each verification gap still open, a remediation plan (item 4)". Item 4's remediation plan
names "the accountable Issue" for each claim "whose verification is incomplete".

The record's verification gaps are the two partially verified rows
(S3:65–66), and both name #1169 with a remediation plan. Read strictly, item 8's fourth condition
is therefore met. The open obligations are stated targets, not claims whose verification is
incomplete. The rule that each of them has an accountable Issue is §A.45 rule 6 ("One obligation,
one accountable Issue … A new deferral names its Issue when it is recorded").

r3's "partly met" treats the open obligations as gaps under item 4 as well. That reading is
conservative and keeps the residual as a blocker, which is defensible, but r3 should name its
basis. Otherwise the text implies that item 8 itself fails. I accepted r2's wording of this
condition in my confirmation without making that distinction, so this point is new here.

**Anything else without an Issue?** No obligation in r3's §1 table lacks an Issue apart from the
residual Bell part. Two rows name two Issues without saying which one is accountable: confinement
S-J ("#914 (comment 6875548603); #1169") and exactness ("#914; #1169"). That bears on §A.45 rule 6
and is optional (O-B).

## 4. #914 comment 6877420015: quotation exact apart from one elision; consequence not overstated

Quotations compared with the API text:

- exact: "Yes I approve, proceed as suggested", "Keep r4 unadopted until reconciled with the
  strengthened target.", the reconciliation sentences, "as an explicit mandatory condition of the
  target", the summary sentence on PR #1289, and the #1169 pointer;
- one elision: "Gate A should remain the quantum-sector proof gate." drops the source's opening
  "However," without marking it (optional O-C).

The consequence (S3:150–153) is not overstated. "Until reconciled" makes reconciliation a
precondition of adoption; it is necessary, not sufficient, and "prerequisite" says no more than that.
"Preserving the record on `main` does not perform or replace that reconciliation" is supported by
"its reconciliation with this target is a separate later step". "Four-part target" leaves out the
joint-satisfiability condition, which the comment's summary lists beside the four parts ("now has
four parts and the joint-satisfiability condition"); see optional O-D.

## 5. New claims, status, scope, authorization: one scope discrepancy (RQ-3); no authorization implied

- **B⇒ wording.** r3 states B⇒'s missing proof as "no protocol of `J_Bell` yields supraquantum
  correlations for a member inside C" (S3:87). r4 states B⇒ as "no protocol of `J_Bell(A₁, A₂)` yields
  correlations outside the quantum set" (r4:328–329). That is broader than "supraquantum" usually
  denotes, since it also excludes signalling correlations. r3's residual inherits the narrower
  wording, and the wording came from my confirmation of r2.
- **Other statements.** All other Issue scopes and statuses are quoted from the bodies. r3 adopts
  no C or E, promotes no status, and states no authorization. S3:203–204, the gate rows and §6 keep
  merge, dispatch and branch update as owner decisions. This matches the approval record's "No CI
  dispatch, branch update or merge is authorized by this record".

## Overall verdict: ACCEPT WITH CHANGES

r3 applies the confirmation of r2 faithfully. The required changes add the owner record that
appeared after r3 was written (RQ-1), state the basis of the "partly met" reading (RQ-2), and align
B⇒ with r4 (RQ-3). None is blocking for preservation as a draft.

## Required changes (for r4 of the note)

**RQ-1. The recorded approval.**

Replace S3:74–77 with:

> The Bell and kinematics entries follow the mapping the owner approved, #1169 comment 6877532844
> (`amaybaum`, 2026-11-14T12:52:30Z, quoted in §2). Scopes below are those of each Issue's body as
> read.

In §2, after the bullet ending "readiness and authorization are unchanged." (S3:129), add:

> - **Accountable Issues, #1169 comment 6877532844** (2026-11-14T12:52:30Z): "I approve the
>   following:", covering a relayed recommendation that names "Bell operational coverage, composites
>   and physical instrument sourcing" #868, "Quantum Bell-set selection and Tsirelson bound" #1060,
>   "Complex kinematics for full operational QM" #1169 "with #914 as the dependency index", and
>   "Complex structure on the SM six-link carrier" #1217, which "cannot discharge the broader Gate A
>   obligation to physically source complex quantum kinematics"; and "I would not authorize special
>   dispatch yet. Ordinary CI should be used where possible; if a dispatch is necessary, require a
>   separate explicit owner decision stating the workflow, ref, purpose and permitted skips." The
>   comment's scope section states that it "changes no Issue's scope, planning block, tier, readiness
>   or authorization", that #868 "covers two-wing instruments, not instrument sourcing in general" and
>   #1060 "covers the Tsirelson bound, not selection of the whole quantum set", and that "Excluding
>   supraquantum correlations other than the Tsirelson bound has no accountable Issue named".

In S3:150, replace "(comments through 2026-11-14T12:42:18Z; none later at 12:50Z)" with
"(comments through 2026-11-14T12:52:30Z)", followed by the time of the new read.

Replace S3:192 (the off-`main` row for the approval) with:

> | #1169 comment 6877532844 | the Accountable Issue entries for Bell and kinematics in §1 | quoted in this note with author and time (§2) | none once this note lands with the record |

In the S3:165 cell, replace from "Not met:" to the end with RQ-2's text. Replace §6 item 8
(S3:242–245) with:

> 8. Which Issue is accountable for excluding, inside C, correlations outside the quantum set
>    other than violations of the Tsirelson bound: #1169 comment 6877532844 names #1060 for "Quantum
>    Bell-set selection and Tsirelson bound", while its scope section states that #1060 covers the
>    Tsirelson bound only and that this residual "has no accountable Issue named" (§A.45 rule 6).

**RQ-2. Basis of the item 8 reading (S3:165, from "Not met:").** Replace with:

> Not met under this note's reading, which treats each open obligation of §1 as needing an
> accountable Issue (§A.45 rule 6, with the remediation fields of §A.46 item 4): excluding, inside
> C, correlations outside the quantum set other than violations of the Tsirelson bound has no
> accountable Issue. #1169 comment 6877532844 names #1060 for "Quantum Bell-set selection and
> Tsirelson bound", and its scope section states that this residual "has no accountable Issue
> named". The verification gaps of §1 (the two partially verified rows) each have #1169 and a
> remediation plan. Closing it: an owner record naming an Issue for the residual, or recording it as
> part of #1060's scope (§6 item 8) |

**RQ-3. B⇒ (S3:87, last cell).** Replace "missing: a proof that no protocol of `J_Bell` yields
supraquantum correlations for a member inside C; remediation: for the Tsirelson bound, under
#1060. #1060 names the Tsirelson bound, not selection of the whole quantum correlation set;
exclusion of every other supraquantum correlation inside C has no accountable Issue" with:

> missing: a proof that no protocol of `J_Bell` yields correlations outside the quantum set for a member inside C (r4 §5.2, B⇒); remediation: for the Tsirelson bound, under #1060. #1060's body names the Tsirelson bound, not selection of the whole quantum set; for the rest of the exclusion see §3 and §6 item 8

## Optional suggestions

- **O-A.** S3:23–27: write "branch head as read at 12:49Z" and add "later commits on the branch add
  only files under `status/`". The note then stays true as the head moves.
- **O-B.** Confinement S-J and exactness rows: name one accountable Issue each, with the other as a
  dependency (§A.45 rule 6).
- **O-C.** S3:122: mark the elision ("[However,] Gate A should remain …" or "… Gate A should remain
  …").
- **O-D.** S3:151 and S3:225–226: "the four-part target" → "the strengthened target (four parts and
  the joint-satisfiability condition)".
- **O-E.** S3:86: B⇐'s "missing" cell paraphrases with #868's vocabulary ("product tests"); r4's
  B⇐ asks for an S⇐ witness whose extension to `J_Bell` meets I-1 to I-4 and reproduces T's law on
  the quantum-labelled part. Stating that, with #868's terms as the route, would follow r4 more
  closely.
- **O-F.** S3:212: the bypass-actor sentence could keep "read through the authenticated API", since
  that is the read it rests on.

## What I checked myself, and what I took from the note

Checked: head, clean tree, `ls-remote`, chain and file changes of `b3cc7182` and `acfdbd0f`;
SHA-256 of all `status/` files; the full r2→r3 diff against each disposition; `endpoints.md` blob;
`git diff --stat` from `c3b5f37a` at `b3cc7182` and `acfdbd0f`; r4:314–333 (Bell clause). Read
through the API: #1169 comment 6877532844 in full; newer comments on #1169, #914, #868, #1060 and
#1217 since 12:42:19Z (only 6877532844); runs at `b3cc7182` and `acfdbd0f`; PR #1289 (draft,
`behind`, 8 commits, 0 comments, 0 reviews). From my earlier confirmation: #914 comment 6877420015
in full, and the bodies of #868, #1060, #1169, #914 and #1217. Taken from the note: everything
outside the five questions.
