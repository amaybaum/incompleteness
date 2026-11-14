# Review of STATUS-r1.md (with NOTES-STATUS-r1.md)

Non-author review, read-only and paper-only: reading, `git` inspection of the record checkout,
`cmp`, grep and public GitHub API reads, 2026-11-14 about 12:20Z–12:45Z. Nothing was computed on
OI models, no Lean was built, no repository checker was run, and nothing was edited, committed,
pushed or posted in any checkout or on GitHub. It is a model review, not independent verification
and not an owner decision. `S:n` is line n of `STATUS-r1.md`; `r4:n` is line n of
`GATE-A-AMEND-r4.md` at `927915e9`.

## Verdict: ACCEPT WITH CHANGES

The four sections are kept apart and the large majority of facts check out at source: the pinned
head, the chain, the file list and blobs, the `endpoints.md` blob and its ancestry, every owner
quotation (exact, with author and time), the absence of any decision adopting
`GATE-A-AMEND-r4.md` as the governing contract, the CI counts, the dependency PRs, and the finding
that the review heads stay reachable from `main` only under a merge commit. Nothing in the note
implies authorization of a merge or reads an unadopted choice as decided. The note does not rely
on `STATUS-INCOMPLETE-DIAGNOSTIC.md`: the only shared text is quotations from the same sources and
table headers.

No finding is blocking. Four are medium and should be applied before the note is published as an
authoritative record: the CI row asserts a merge-commit identity the writer did not check (F1);
merge readiness omits the repository's up-to-date rule, which makes a branch update, and so a new
head, unavoidable (F2); one off-`main` reference used as support is classified as provenance (F3);
and the §A.46 item 8 condition on accountable Issues and remediation plans is shown as met when two
obligations have no accountable Issue and the partially verified content has no remediation plan
(F4). The rest are low.

## Findings

### F1 (medium). The CI row asserts which merge commit the run tested

- **Location.** S:162.
- **Source.** `NOTES-STATUS-r1.md`:66 ("Not checked: Whether run 43588379859 used the merge commit
  `29dd4cda`; the run record names only the head"). Run 43588379859 (API): event `pull_request`,
  `head_sha` `927915e9`, created 11:05:52Z, updated 11:16:17Z; its 27 check runs carry `head_sha`
  `927915e9` and no merge SHA. PR #1289 `merge_commit_sha` `29dd4cda` (parents `dfeec843`,
  `927915e9`, committed 11:05:47Z). `main` has been at `dfeec843` since 09:11:18Z. Compare
  `927915e9...29dd4cda`: the only file difference is `AGENTS.md`. Workflow `verify.yml` at
  `927915e9`: triggers `pull_request`, `push` on `main` only, and `workflow_dispatch`; its checkout
  steps set no `ref`. The skipped job is `Numerical probes / A42 exclusion (${{ matrix.part }})`,
  which runs only on `workflow_dispatch`.
- **Assessment.** That a `pull_request` run tests GitHub's synthetic merge, not the head (§A.39), is
  correct, and "the final head needs its own run" is correct. Naming `29dd4cda` as the tested commit
  is an inference the writer's own notes mark unchecked; the structured record does not name it.
  The row also does not say that a push run cannot occur on this branch (push triggers only `main`)
  or that the skipped job is the dispatch-only job, so "no push or dispatch run" can read as a
  deficiency.
- **Replacement for the S:162 cell "State as read":**

  > at `927915e9`: workflow `verify`, run 43588379859, event `pull_request`, attempt 1,
  > 11:05:52Z–11:16:17Z; 26 jobs success, including the required contexts `Lean kernel check`,
  > `Mathlib bridge` and `Numerical probes`, and 1 skipped (`Numerical probes / A42 exclusion`, which
  > runs only on `workflow_dispatch`). A `pull_request` run tests GitHub's synthetic merge of the
  > head into `main`, not the head itself (§A.39). `main` was at `dfeec843` throughout; the PR's
  > test-merge commit is `29dd4cda` (parents `dfeec843` and `927915e9`, 11:05:47Z), whose tree differs
  > from the head's only in `AGENTS.md`, but the run record names only the head, so which merge
  > commit the run checked out is not recorded. The workflow runs on `push` only for `main`, so no
  > push run exists for this branch; no `workflow_dispatch` run exists, and none is authorized by
  > item 5 of #1169 comment 6876591512. The final head needs its own run.

### F2 (medium). Merge readiness omits the up-to-date rule and the allowed merge methods

- **Location.** S:164 (row "Draft state and base"); S:181–182 (§6 item 5); S:143 (column "What
  would close a gap").
- **Source.** Public rules API for `main` (`/rules/branches/main`): rule `required_status_checks`
  with `strict_required_status_checks_policy: true` and required contexts `Lean kernel check`,
  `Mathlib bridge`, `Numerical probes`; rule `pull_request` with `allowed_merge_methods` `merge`,
  `squash`, `rebase`. PR #1289: `mergeable_state` `behind`; compare `main...927915e9`: diverged, 5
  ahead, 9 behind, merge base `c3b5f37a`. Bypass permissions are not visible to the public API.
- **Assessment.** Under the strict policy the branch must be brought up to date with `main` before a
  merge (unless bypassed). §6 item 5 presents the update as optional ("whether the branch is
  updated with `main` first"). An update is then the step that creates the final head, besides the
  status-note commit, and its method matters for the review heads: a merge of `main` into the
  branch keeps `65b0a929`–`927915e9` as ancestors; a rebase replaces them. Squash and rebase merges
  are allowed by the ruleset, so a merge commit has to be chosen.
- **Replacement for the S:164 cell:**

  > PR draft (must be marked ready). GitHub reports mergeable, `mergeable_state` `behind` (5 ahead,
  > 9 behind `main`, merge base `c3b5f37a`). The repository ruleset for `main` requires branches to
  > be up to date before merging (`strict_required_status_checks_policy`) and allows merge, squash
  > and rebase; bypass permissions are not visible through the public API. Unless bypassed, the
  > branch must be updated with `main` before a merge, which creates a new head needing review
  > and CI.

- **Replacement for S:181–182 (§6 item 5):**

  > 5. Merge method and branch update. The ruleset allows squash and rebase as well as merge; only
  >    a merge commit keeps the review heads reachable from `main`. The up-to-date rule requires
  >    updating the branch with `main` before a merge unless bypassed; updating by a merge of `main`
  >    into the branch keeps the review heads as ancestors, a rebase does not. Either update creates
  >    a new head needing review and CI.

- **Replacement for the S:143 cell "What would close a gap":**

  > a landing that keeps these commits reachable from `main`: a merge commit, and any branch update
  > by merging `main` into the branch, not by rebase; no squash or rebase merge

### F3 (medium). #1169 comment 6703342848 is used as support but classified as provenance

- **Location.** S:139.
- **Source.** r4:56 ("#1169 c.6703342848 is quoted for an explanation the owner approved
  (§3.2)"); r4:144, the §3.2 requirement row "Hidden machinery need not be quantum (the explanation
  the owner approved: "We do not need the hidden machinery itself to be quantum"); deterministic
  hidden dynamics admissible (the comment's statement)", sourced "#1169 c.6703342848
  (2026-11-07T06:25:11Z)"; r4:430–433 and `OWNER-QUESTIONS-r4.md`:44–47 (recorded positions on
  question 4). API: comment 6703342848, `amaybaum`, OWNER, 2026-11-07T06:25:11Z, reads "The owner
  approved proceeding after the explanation that success means the same predictions across the
  complete agreed experimental interface and that “We do not need the hidden machinery itself to
  be quantum.”" and "Deterministic hidden dynamics and indirect recovery of hidden information are
  admissible." Also r4:54–55, which classifies the three owner comments of r4 §1 as "provenance for
  authority".
- **Assessment.** The §3.2 row is a requirement the record carries, and it uses the comment's
  content: under §A.42 item 8 that is support. The first half is quoted verbatim with time; the
  second half is a paraphrase, so its content is not on `main` as stated. The row of S:139 groups
  this use with trace §2 entries that are provenance; §A.42 item 8 makes "provenance" a finding
  about each reference. Separately, S:137 classifies the three r4 §1 comments as support on `main`
  through quotation, while r4:54 calls them provenance for authority; the note's reading is the more
  careful one, but the difference should be stated.
- **Replacement for S:139** (two rows in place of one):

  > | #1169 comment 6703342848 | r4 §3.2 requirement row (r4:144); owner question 4 (r4:430–433, `OWNER-QUESTIONS-r4.md`:44–47) | support on `main` through quotation with time: "We do not need the hidden machinery itself to be quantum" and "a quantum counterpart for every behavior admitted by the physical OI interface" are verbatim; the clause "deterministic hidden dynamics admissible" paraphrases the comment, whose words (`amaybaum` account, 2026-11-07T06:25:11Z) are "Deterministic hidden dynamics and indirect recovery of hidden information are admissible." | none once this note lands with the record |
  > | #1169 comment 6763928950; #1169 and #1143 bodies; #1169 comment 6703342848 as a trace §2 entry | dependent statements (trace §2), §4.2 | provenance (quoted to identify statements; not support) | none |

- **Addition at the end of the S:137 cell "Classification":** "; r4:54 classifies these comments
  as provenance for authority; this note classifies the quotations as support on `main`, since the
  §3.2 requirements and §5 definitions use their content".

### F4 (medium). The §A.46 item 8 condition on Issues and remediation plans is shown as met

- **Location.** S:123; S:45–52 (verification status table); S:65 and S:67 (Bell and kinematics
  rows).
- **Source.** `AGENTS.md` at `dfeec843`, §A.46 item 4 ("The same record states each such claim's
  remediation plan: the current evidence level, the verification that is missing, the accountable
  Issue, and the evidence or decision that would resolve the gap") and item 8, fourth condition;
  §A.45 rule 6 ("One obligation, one accountable Issue"). S:65 and S:67 give "none named in the
  record" as the accountable Issue.
- **Assessment.** The obligations table states remediation for each open obligation, but two rows
  have no accountable Issue, and the two "partially verified" rows of S:49–50 state an evidence
  level without the missing verification, the accountable Issue or what would resolve the gap. The
  S:123 cell "#1169; status and plans in §1 of this note" reads as if the condition were met.
- **Replacement for the S:123 cell:**

  > #1169 for the record. Verification status: §1. Remediation plans: §1 for each open obligation and
  > for the partially verified content; the Bell clause and the kinematics input have no accountable
  > Issue named in the record or in the owner records read, so this condition is not met for those
  > two items (§6 item 8)

- **Replacement for the S:47 header and S:49–50 rows** (adds two columns):

  > | Content | Status | Basis | Verification missing | Accountable Issue | What would resolve it |
  > | --- | --- | --- | --- | --- | --- |
  > | Line trace of `endpoints.md` (113 dispositions) and the superseded lines EP:56–59, forward half of EP:157, EP:51 in part | partially verified | coverage checked mechanically and dispositions read by `CONFIRM-r2.md`; preservation confirmed by `CONFIRM-r3.md`, `CONFIRM-r4.md`; model reviews only | an independent line-by-line check of the 113 dispositions against EP | #1169 | a recorded independent check of the trace, or an owner decision accepting the model reviews as the review standard for this record |
  > | Conditional statements of r4 §5.2 (S⇐ implies I; S⇐ with S-A implies S⇐ᴺ when C is ≃-invariant; a C that is a function of p_M over all of `J_exact(A)` is ≃-invariant) | partially verified | checked by hand in `CONFIRM-r2.md`–`CONFIRM-r4.md`; no independent check | an independent check of the three implications | #1169 | a recorded independent paper check, or a Lean statement of the implications under #914 decision 5 |

  The remaining two rows of S:51–52 take "none" (targets, not results) and "none (superseded)" in
  the three added columns.
- **Addition to §6, after S:186:**

  > 8. Which Issue is accountable for the Bell clause B and for the kinematics input; the record and
  >    the owner records read name none (§A.45 rule 6; §A.46 item 4).

### F5 (low). Not every review describes itself as the note says

- **Location.** S:40–41.
- **Source.** `REVIEW-r1.md`:3 ("Non-author review, paper-only"); `CONFIRM-r2.md`:3 ("Non-author
  confirmation review ... paper-only"); neither says "model review", "not independent
  verification" or "not an owner decision". `CONFIRM-r3.md`:3–5 and `CONFIRM-r4.md`:3–5 say all
  three. `README.md`:56: "The reviews are non-author model reviews, not independent verification."
- **Replacement for "Every review describes itself as a non-author model review, paper-only, not
  independent verification and not an owner decision.":**

  > Every review describes itself as non-author and paper-only; `CONFIRM-r3.md` and `CONFIRM-r4.md`
  > also state that they are model reviews, not independent verification and not owner decisions,
  > and `README.md`:56 states that all the reviews are non-author model reviews, not independent
  > verification.

### F6 (low). What `927915e9` changed is described incompletely

- **Location.** S:36 (column "What followed"); S:38.
- **Source.** `git diff eb515150 927915e9`: adds `CONFIRM-r4.md` (230 lines) and changes
  `README.md` in three places: line 17, "The current text of the amendment" to "The final text of
  the amendment cycle"; a new contents row at line 20 for `CONFIRM-r4.md`; lines 48–55, the
  replacement of eb515150's lines 47–51. `CONFIRM-r4.md`:194–206 asks for the replacement of lines
  47–51 (given verbatim, and applied verbatim) and "a matching row for `CONFIRM-r4.md`"; it does not
  ask for the line 17 change. `GATE-A-AMEND-r4.md`, `OWNER-QUESTIONS-r4.md` and the trace are
  byte-identical at the two commits.
- **Assessment.** "`927915e9` itself has no review" is correct: `CONFIRM-r4.md` reviewed
  `eb515150`, and nothing reviews `927915e9`. The line 17 change matches `CONFIRM-r4.md`'s verdict
  wording but was not requested and is unreviewed.
- **Replacement for the S:36 cell "What followed":**

  > `927915e9` adds `CONFIRM-r4.md`, applies its README replacement verbatim with the requested
  > contents row, and changes the README's description of r4 to "The final text of the amendment
  > cycle", which the review did not request

- **Replacement for "`927915e9` itself has no review." (S:38):**

  > `927915e9` itself has no review; its changes are `CONFIRM-r4.md` and the three `README.md`
  > changes above, and `GATE-A-AMEND-r4.md`, `OWNER-QUESTIONS-r4.md` and the trace are unchanged by
  > it.

### F7 (low). The CONFIRM-r3 row understates `cea26912` and omits `ae2de57a`

- **Location.** S:35, column "What followed".
- **Source.** `git show ae2de57a`: adds `CONFIRM-r3.md` and removes the README sentence on an
  unrecorded owner confirmation (O1). `git diff ae2de57a cea26912`: one word replaced at two places
  in `CONFIRM-r3.md` and a coordinator's note appended.
- **Replacement:**

  > committed at `ae2de57a`, which also removes the unrecorded owner-confirmation sentence from
  > `README.md` (O1); `cea26912` replaces one word at two places in `CONFIRM-r3.md` and appends a
  > coordinator's note saying so; r4 at `eb515150`

### F8 (low). The superseded necessity statements of r2 and r3 are not listed

- **Location.** S:52.
- **Source.** `CONFIRM-r3.md` §B.3: r3's "If C is a function of the history law, S⇐ implies S⇐ᴺ"
  (r3:272–273, :339–340), "follows from S⇐" (r3:213, :378) and "a distinct question only under
  C-model" (r3:381) "are correct only when C is a function of p_M over the whole of `J_exact(A)`,
  for the same A", and S⇐ᴺ with antecedent M ≡ T is "not the intended option". The same statements
  stand in r2 (r2:209, :255, :258, :327, :363), and `CONFIRM-r2.md`:58 records "Under C-law, S⇐
  implies S⇐ᴺ; this was checked by hand".
- **Assessment.** These lines stay in the landed trail. They are not false under their own scope
  but are superseded as general statements; `OWNER-QUESTIONS-r3.md`:8, listed at S:52, is the same
  claim.
- **Addition after S:52:**

  > | r3:213, :272–273, :339–340, :378, :381 and r2:209, :255, :258, :327, :363 (necessity follows from coverage under C-law; a distinct question only under C-model), and the hand check at `CONFIRM-r2.md`:58 | superseded by r4 §5.2 (RC2); correct only when C is a function of p_M over the whole of `J_exact(A)`, not as general statements; kept as review trail | `CONFIRM-r3.md` §B.3 |

### F9 (low). §5 omits the r4 lines that present the four questions as open

- **Location.** S:169–170.
- **Source.** r4:224 ("which one the target uses is undetermined pending owner decision"), r4:283–284
  ("whether the target includes S-A is owner question 4"), r4:308–309, r4:382–383 (both
  "undetermined pending owner decision"), r4:410 ("Owner questions carried"),
  `OWNER-QUESTIONS-r4.md`:2 ("Decisions the amendment leaves open"); #1169 comment 6876591512
  ("`GATE-A-AMEND-r4.md` is not edited by these answers").
- **Replacement for S:169–170:**

  > - r4:224, :283–284, :308–309, :382–383 and §8 (r4:410), `OWNER-QUESTIONS-r4.md` throughout and
  >   `README.md`:18 present four open owner questions; all four were answered at
  >   2026-11-14T11:28:20Z (#1169 comment 6876591512), which leaves r4 unedited. `README.md`:3 reads
  >   "Work in progress".

### F10 (low). The relation of answers 1 and 3 to r4 is slightly loose, and the paragraph is marked for the reviewer

- **Location.** S:97–102.
- **Source.** Answer 1 (#1169 comment 6876591512): "It should be a physically stated condition, with
  its consequences for experiment families defined explicitly." r4:229 (C-model row) states neither
  requirement; r4:247–248 (C-2) requires physical justification. Answer 3: "The ultimate model must
  accommodate arbitrarily large finite carriers, with the permitted encodings and resource
  requirements stated explicitly." r4:422–425 (§8 item 3) already states the single-model
  commitment "one model whose subsystems realize every carrier A, one E for every A, typed
  subsystem embeddings"; I quantifies over every nonempty finite A (r4:193); resource accounting is
  EP:106, kept.
- **Assessment.** The readings of answers 2 and 4 are correct, and answers 1 and 3 select the options
  the note names. "adds carrier, encoding and resource requirements r4 does not state" overstates
  the addition: what r4 does not state is that encodings and resource requirements be stated
  explicitly for the single model. "for the reviewer to check" is process voice.
- **Replacement for S:97–102:**

  > **Relation of answers 1–4 to r4** (this note's reading; the answers are the source). The answers
  > postdate `927915e9` and are not in the record's text. Answer 1 selects r4's C-model type (r4 §5.2,
  > question 1), not C-law, and adds that C is physically stated with its consequences for experiment
  > families defined explicitly. Answer 2 answers question 2 "no": S⇐ᴺ is not part of the target.
  > Answer 3 takes the single-model reading of question 3 (r4 §8 item 3) as the ultimate target and
  > r4's I (one architecture, one instance per (A, T)) as an intermediate milestone, and requires the
  > permitted encodings and resource requirements of the single model to be stated explicitly, which
  > r4 does not. Answer 4 keeps S-A (question 4, first option).

### F11 (low). The pointer comment is summarized as refining only the sector wording

- **Location.** S:94–95.
- **Source.** #914 comment 6876592679: heading "refinement of the target's sector wording"; body
  "Two of its answers refine the target recorded here in comment 6875548603", the first on C, the
  second "One fixed model, with one common extension E" (the inclusion part); it also restates
  answers 2 and 4.
- **Replacement:**

  > - **Pointer, #914 comment 6876592679** (2026-11-14T11:28:26Z): records on #914 that answers 1 and 3
  >   refine the target of 6875548603 (answer 1 its sector wording, answer 3 its inclusion part) and
  >   restates answers 2 and 4; it adds no decision.

### F12 (low). "What would adopt the amendment text" reads as a rule

- **Location.** S:108–111.
- **Source.** Item 5 of #1169 comment 6876591512: "adoption of the amended target requires an
  explicit owner decision". No source prescribes the form of that decision.
- **Replacement for S:108–111:**

  > **What would adopt the amendment text.** Item 5: "adoption of the amended target requires an
  > explicit owner decision". This note's reading is that such a decision, recorded with author and
  > time, would name the text (file and blob or commit) and state how answers 1–4 apply to it (as
  > recorded decisions beside r4, or through a revised and re-reviewed text). No decision adopting
  > `GATE-A-AMEND-r4.md` or a revision of it is recorded on #1169, #914 or PR #1289 as read
  > (comments through 2026-11-14T11:28:26Z).

### F13 (low). The accepted-head row cites blob identity for a fact recorded elsewhere on `main`

- **Location.** S:140.
- **Source.** Blob `d9d92e03` at `fdc3dd7f`, `9d24914c`, `dc0b333a` (checked). On `main` at
  `dfeec843`: `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-mode-drive.md`:3 ("The
  accepted Gate A contract is `endpoints.md` at `fdc3dd7f…`") and `oi-qm-ext-1/README.md`:26 (links
  #1173 comment 6686122542 as "Gate A").
- **Assessment.** Blob identity shows that the accepted text and the amended text are the same; it
  does not by itself show which head was accepted. Records on `main` state that.
- **Replacement for the S:140 cell "Classification":**

  > support on `main`: the blob `d9d92e03` at `fdc3dd7f`, `9d24914c` and `dc0b333a`, all on `main`, and
  > the acceptance of `endpoints.md` at `fdc3dd7f` stated on `main` in
  > `oi-qm-ext-1/two-mode-drive.md`:3, with `oi-qm-ext-1/README.md`:26 linking the acceptance comment

### F14 (low). Two classes of reference are not traced

- **Location.** §3 table, after S:144.
- **Source.** `NOTES-r1.md`:33 and :58 name #1169 comments 6691915819, 6875057963, 6875553907 and #1173
  comment 6686000116 as read or not read. `CONFIRM-r3.md`:34–38 rests the identity of the text that
  `REVIEW-r1.md` and `CONFIRM-r2.md` read on a `cmp` against uncommitted working copies;
  S:33–34 relies on it ("committed unchanged at `65b0a929`").
- **Addition:**

  > | #1169 comments 6691915819, 6875057963, 6875553907; #1173 comment 6686000116 (`NOTES-r1.md`:33, :58) | the writer's reading list | provenance | none |
  > | Uncommitted working copies read by `REVIEW-r1.md` and `CONFIRM-r2.md` | which text the first two reviews read (S:33–34) | support off `main`: the identity rests on the recorded `cmp` in `CONFIRM-r3.md`:34–38; the copies are not retained | cannot be landed; stated as a limit: the reviewed text of those two reviews is identified by that recorded check |

### F15 (low). The note's own status lines and landing path

- **Location.** S:3–5, S:122, S:160, S:180.
- **Assessment.** These describe the note as unreviewed and the review as not started; on
  acceptance they become stale. The note also does not state the path at which it would land or
  whether `README.md` would list it, which a reader deciding the landing needs.
- **Replacement for S:3–5:**

  > Status note for `verification/programmes/oi-qm/reconstruction/drafts/gate-a-amendment-20261114/`,
  > prepared under item 5 of #1169 comment 6876591512, to land in that directory as `<file name>`.
  > Reviewed by `<review file>` at `<commit>`. It is status documentation only: it changes no

  (the sentence then continues as at S:5–7 from "Gate A contract"). S:122 "tracing in this note,
  unreviewed" becomes "tracing in this note, reviewed by `<review file>`"; S:160 becomes the review's
  state and verdict; S:180 item 4 keeps only the exact-head review.

### F16 (low). Two wordings

- **S:33**, "a 113-line trace": `GATE-A-AMEND-r2-TRACE.md` is 101 lines. Replace with "a trace of the
  113 nonblank lines of `endpoints.md`".
- **S:18**, "which r4 adopts unchanged": "adopts" can be read as an owner act. Replace with "which r4
  retains unchanged (r4:10–11)".
- **S:120**, "for review:": process voice. Replace with "the record holds ... not a theorem; whether
  this meets the condition is not recorded (§6 item 2)".

## Checked against the four points of the brief

1. **Sections kept apart.** Yes. Scientific acceptance (§1): heads and verdicts checked (F5–F8);
   the nine obligations, their source statuses and Issues checked (F4). Governance (§2): every
   quotation exact; no adoption of r4 recorded on #1169 or #914 (all 20 comments since
   2026-11-14T00:00Z listed; none after 11:28:26Z) or on PR #1289 (0 comments, 0 reviews); PR
   #1290's description also lists r4 as "Not adopted" (F10–F12). Preservation (§3): basis correct;
   F3, F13, F14 on classification; the merge-commit finding for `65b0a929` and `eb515150` is correct
   (`git merge-base --is-ancestor` against `dfeec843`: not ancestors), F2 on the update method.
   Merge readiness (§4): F1, F2.
2. **No stronger status, no implied authorization, no unadopted choice read as decided.** None
   found; F12 marks one prescriptive passage as the note's reading.
3. **The final commit.** Correctly unreviewed; contents described incompletely (F6).
4. **Self-containment and register.** No absolute paths; no reliance on the stopped diagnostic
   draft; register neutral apart from F10 and F16; F3 and F14 on tracing.

## What I checked myself

- `git ls-remote origin`: branch head `927915e9923281dae3da9d414fa349ccbb5d8643`, `main`
  `dfeec843bec08443b25cffe34d33dc8401c3b604`; checkout `HEAD` the same, working tree clean.
- Chain and parents of the five commits, authors, messages; `git diff --stat c3b5f37a 927915e9`
  (16 files, 3413 insertions, one directory); blob ids of all sixteen files; `GATE-A-AMEND-r4.md`
  (`32c294c3`, 444 lines), `OWNER-QUESTIONS-r4.md` (`2933ec78`), `GATE-A-AMEND-r3-TRACE.md`
  (`fd293d60`) identical at `eb515150` and `927915e9`.
- `git diff eb515150 927915e9` and `git diff ae2de57a cea26912` in full; `CONFIRM-r4.md` read in full;
  headers of `REVIEW-r1.md`, `CONFIRM-r2.md`, `CONFIRM-r3.md`, `RESPONSE-r1.md`; `CONFIRM-r3.md`
  §B.3; `README.md` in full; r4 §1–§9 read (lines 14–70, 125–158, 160–444); `OWNER-QUESTIONS-r4.md`
  in full; `GATE-A-AMEND-r2.md`:246–251 and the r2/r3 necessity lines; `OWNER-QUESTIONS-r3.md`:8;
  F1–F16 present in `REVIEW-r1.md`.
- `endpoints.md`: blob `d9d92e03` at `c3b5f37a`, `fdc3dd7f`, `9d24914c`, `dc0b333a` and `dfeec843`;
  179 lines, 113 nonblank; EP:29 and EP:164 read; ancestry of the four commits to `dfeec843`; review
  heads not ancestors; `git diff c3b5f37a dfeec843` touches `AGENTS.md` only; `git grep` on `main`
  for the record's directory, file names and PR number: no hit.
- `AGENTS.md` at `dfeec843`: §A.46 in full (items 1–8 and the adoption line); §A.42 and §A.39 as
  quoted.
- `papers/GR.md`:162 and `papers/Main.md`:596, :598 on `main`: quoted content present.
- API: run 43588379859 and its 27 check runs (names, conclusions, `head_sha`); runs for the head (one);
  `main` CI (push run 43579358365, 26 success, 1 skipped); PR #1289 (state, draft, merge commit,
  `mergeable_state`, 0 comments, 0 reviews, description); compare `main...927915e9` and
  `927915e9...29dd4cda`; rules for `main`; absence of a `CODEOWNERS` file on `main`.
- API, full text: #1169 comments 6875724719, 6876591512, 6874035457, 6703342848, 6763928950,
  6686258585, 6875729134; #914 comments 6875046763, 6875548603, 6876592679, 6876304390; #1173 comment
  6686122542; #1283 comment 6875009394. Quotations in the note compared by string match after
  whitespace normalization: all exact. Quotations in r4 §1 compared the same way: all exact apart
  from elisions.
- PRs #1283 (merged 09:11:18Z as `dfeec843`, head `bef57cbf`), #1287 (open, draft, head `755f9bff`),
  #1288 (open, draft, head `485f9a2d`), #1290 (open, draft, head `f5b3ee2d`, created 12:11:34Z,
  description lists r4 as not adopted); file lists of all four: no common path.
  `TARGET-THEOREM-r3.md`:34 and the `README.md` branch list at `755f9bff` (raw content host).
- Issues #873 (open; labels `tier: high`, `tier: provisional`, `readiness: ready`; block
  "Authorization: not authorized"), #1169 (planning block: Codex main writer since 2026-11-09,
  Claude paused; no mention of this record), #914, #1143 (labels and state); #868 title only.
- Text overlap of `STATUS-r1.md` with `STATUS-INCOMPLETE-DIAGNOSTIC.md` (8-word shingles): only
  shared quotations, table headers and one phrase.

## What I took from the note without checking

- The content of the reviews beyond their headers, verdicts and the passages cited above; the
  amendment's mathematics and the 113-line trace were not re-derived or re-checked.
- That the coordinating sessions contained the owner wording the comments quote; only comment texts
  were read.
- The local checks the PR description reports at `927915e9`.
- Whether any record on another branch cites this record, beyond PR #1290's description.
- The planning-status blocks of #914 and #1143 beyond labels; whether any open Issue is the Bell-track
  or kinematics home (F4 leaves this as an owner question).
- Repository bypass permissions for the ruleset (not visible through the public API).
