# Landing status: the Gate A forward amendment record (PR #1289), r2

Status note for `verification/programmes/oi-qm/reconstruction/drafts/gate-a-amendment-20261114/`,
prepared under item 5 of #1169 comment 6876591512, proposed to land in that directory as `STATUS.md`
and to be listed in its `README.md` contents table (§6 item 9). r1 was reviewed by a non-author
model review, ACCEPT WITH CHANGES, held outside the repository and not posted on GitHub; this
revision, r2, applies its findings and has no review of its own. It is status documentation only:
it is not an authoritative status record until its review is complete, it changes no Gate A
contract and no scientific status, and it authorizes no merge. Where this note and a cited source
differ, the source governs (§A.45 rule 1). Facts below were read 2026-11-14 between 12:10Z and
12:35Z.

## 0. Pins

- **Record.** Branch `research/gate-a-amendment-1169-20261114`, head
  `927915e9923281dae3da9d414fa349ccbb5d8643` (checkout `HEAD` and `git ls-remote origin` agree; the
  PR API reports the same head). Chain: `c3b5f37a` ← `65b0a929` ← `ae2de57a` ← `cea26912` ←
  `eb515150` ← `927915e9`, all single-parent. Sixteen files, 3413 added lines, one new directory; no
  other path differs from `c3b5f37a`.
- **Final text.** `GATE-A-AMEND-r4.md` (blob `32c294c3`, 444 lines) and `OWNER-QUESTIONS-r4.md` (blob
  `2933ec78`); both blobs are identical at `eb515150` and `927915e9`. Line trace and status table:
  `GATE-A-AMEND-r3-TRACE.md` (blob `fd293d60`), which r4 retains unchanged (r4:10–11).
- **Contract addressed.** `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md`, blob
  `d9d92e038a8022e854586101067ce4de9789fdf6` (179 lines, 113 nonblank), at the record's base `c3b5f37a`
  and unchanged at current `main` `dfeec843bec08443b25cffe34d33dc8401c3b604` (the #1283 merge, which
  changes `AGENTS.md` only). `fdc3dd7f`, `9d24914c`, `dc0b333a` and `c3b5f37a`, which r4 §1 cites for
  this blob, are all ancestors of `dfeec843`.
- **Policy form relied on.** `AGENTS.md` at `dfeec843`: §A.42 and §A.46 including item 8. #1283 was
  adopted on #1169 comment 6874035457 (`amaybaum`, 2026-11-14T07:45:39Z: "I adopt #1283 at
  f57e576a"), its merge authorized on #1283 comment 6875009394 (`amaybaum`, 2026-11-14T09:10:38Z),
  and merged 2026-11-14T09:11:18Z as `dfeec843`. Item 8 is therefore in force on `main`.

## 1. Scientific acceptance (what the reviews established)

| Review file | Object reviewed | Verdict | What followed |
| --- | --- | --- | --- |
| `REVIEW-r1.md` | r1 and `NOTES-r1.md` as working text, before any commit; committed unchanged at `65b0a929` | REVISE: one blocking, sixteen should-fix (its header says fourteen; `RESPONSE-r1.md` counts F1–F16) | r2 adds a residual clause and a trace of the 113 nonblank lines of `endpoints.md` |
| `CONFIRM-r2.md` | r2, its trace and `RESPONSE-r1.md`, as working text | ACCEPT WITH CHANGES: K1 (blocking, access closure), K2–K5, N1–N4 | r3, committed with r1, r2 and the reviews at `65b0a929` |
| `CONFIRM-r3.md` | commit `65b0a929` | ACCEPT WITH CHANGES: RC1–RC4 and one owner-questions wording | committed at `ae2de57a`, which also removes the unrecorded owner-confirmation sentence from `README.md` (O1); `cea26912` replaces one word at two places in `CONFIRM-r3.md` and appends a coordinator's note saying so; r4 at `eb515150` |
| `CONFIRM-r4.md` | commit `eb515150` | ACCEPT; no change to r4 or `OWNER-QUESTIONS-r4.md`; one `README.md` correction | `927915e9` adds `CONFIRM-r4.md`, applies its README replacement verbatim with the requested contents row, and changes the README's description of r4 to "The final text of the amendment cycle", which the review did not request |

`927915e9` itself has no review; its changes are `CONFIRM-r4.md` and the three `README.md` changes
above, and `GATE-A-AMEND-r4.md`, `OWNER-QUESTIONS-r4.md` and the trace are unchanged by it.
`CONFIRM-r4.md` states what its acceptance means: "the text is
internally consistent, faithful to its sources and within the authorization. It proves no
obligation, adopts no E or C, and changes no scientific status." Every review describes itself as
non-author and paper-only; `CONFIRM-r3.md` and `CONFIRM-r4.md` also state that they are model
reviews, not independent verification and not owner decisions, and `README.md`:56 states that all
the reviews are non-author model reviews, not independent verification. Under
§A.46 item 8 a model's acceptance is evidence of review, not independent mathematical verification.
No review proves any obligation below.

**Verification status of the record's content (§A.46 item 4).**

| Content | Status | Basis | Verification missing | Accountable Issue | What would resolve it |
| --- | --- | --- | --- | --- | --- |
| Line trace of `endpoints.md` (113 dispositions) and the superseded lines EP:56–59, forward half of EP:157, EP:51 in part | partially verified | coverage checked mechanically and dispositions read by `CONFIRM-r2.md`; preservation confirmed by `CONFIRM-r3.md`, `CONFIRM-r4.md`; model reviews only | an independent line-by-line check of the 113 dispositions against EP | #1169 | a recorded independent check of the trace, or an owner decision accepting the model reviews as the review standard for this record |
| Conditional statements of r4 §5.2 (S⇐ implies I; S⇐ with S-A implies S⇐ᴺ when C is ≃-invariant; a C that is a function of p_M over all of `J_exact(A)` is ≃-invariant) | partially verified | checked by hand in `CONFIRM-r2.md`–`CONFIRM-r4.md`; no independent check | an independent check of the three implications | #1169 | a recorded independent paper check, or a Lean statement of the implications under #914 decision 5 |
| Obligations I, S⇒, S-A, S⇐, S⇐ᴺ, S-J, B, G and the admissibility conditions C-1 to C-5 | exploratory: stated targets, not results | r4 §5, §9: "I, S⇒, S-A, S⇐, S⇐ᴺ, S-J, B and G are open" | none (targets, not results) | none | none |
| r2:248–250 ("S⇒ and S⇐ together give the set equality …") and `OWNER-QUESTIONS-r3.md`:8 ("Question 2 answers itself.") | known-invalid as stated; superseded by r4 and kept as review trail | `CONFIRM-r2.md` K1; `CONFIRM-r3.md` Part C | none (superseded) | none (superseded) | none (superseded) |
| r3:213, :272–273, :339–340, :378, :381 and r2:209, :255, :258, :327, :363 (necessity follows from coverage under C-law; a distinct question only under C-model), and the hand check at `CONFIRM-r2.md`:58 | superseded by r4 §5.2 (RC2); correct only when C is a function of p_M over the whole of `J_exact(A)`, not as general statements; kept as review trail | `CONFIRM-r3.md` §B.3 | none (superseded) | none (superseded) | none (superseded) |

**Remaining scientific obligations.** Status is that at the cited source; none is proved
(#1169 comment 6876591512: "none is proved"). Resolving any of them needs a proof or construction
meeting the evidence standard of #914 decision 5 and, for physical sourcing, a justified mechanism.

| Obligation | Status at source | Accountable Issue | Missing / what would resolve it |
| --- | --- | --- | --- |
| Inclusion I (r4 §5.1), with its remainder outside `J_exact(A)` | open; no M_{A,T} exhibited (r4 §9); ε-realizations of `papers/Main.md`:596 are an approximation target, not I (trace §3) | #1169; target on #914 | construction of one model under I-1 to I-4 and proof of M ≡ T for every T; answer 3 makes one architecture an intermediate milestone and one model the ultimate target; interfaces for type changes and multi-wing protocols still untyped |
| Sector soundness S⇒ and coverage S⇐ (r4 §5.2) | open | #1169 | a stated C, a proof of S⇒ over every member inside C, and S⇐ witnesses; necessity S⇐ᴺ not required (answer 2) |
| Physical justification of C (C-2), with C-1, C-3 to C-5 | open; no C proposed (r4 §5.2) | #1169; selection question on #1143 (r4 §4.2) | a C on the underlying model (answer 1), justified independently of the agreement; adopting one is a new premise under §A.29 and needs its own owner authorization |
| Access closure S-A | open; no counterpart in EP (r4 §7, R5) | #1169 | proof over every member inside C and every performable protocol; required by answer 4 |
| Confinement S-J | open; "not stated in any record read" what it means physically (r4 §7, R3) | #914 (comment 6875548603); #1169 | a physical justification that observation is confined to the sector |
| Bell clause B⇐, B⇒ | open; `J_Bell` untyped (r4 §5.2) | none named in the record; #914 decision 3 makes it a separate, mandatory track | typed two-wing interface; coverage, and exclusion of supraquantum correlations inside C |
| Gravity G-1 to G-3 | open: field equations "remain the Level-G3 target" (`papers/GR.md`:162); coupling and source open | #873 (open; tier high, provisional; authorization "not authorized") | GR from the same substratum and observer, consistent with E and C |
| Kinematics input | complex matrix kinematics given; "its operational derivation is open" (EP:29); #914 decision 4: "Allowed as a conditional mathematical input, not a physical explanation" | none named in the record; decision on #914 | an operational derivation, or disclosure as an import under EP:164 |
| Exactness (I-4; EP:116–123) | exact is the ultimate target, approximation a separate milestone (#914 decision 2); no fixed finite total carrier assumed | #914; #1169 | exact law-equality with a declared carrier or completion policy; answer 3 adds arbitrarily large finite carriers with permitted encodings and resource requirements stated explicitly |

Physical source: "Physical source remains **NOT PASSED**" (#1169 comment 6875724719).

## 2. Governance adoption (what the owner has and has not adopted)

All comments below were posted from the owner's account `amaybaum` (author association OWNER).
Each records owner wording given in a coordinating session and quotes it; this note checks the
comment text, not the session.

- **Target, #914 comment 6875046763** (2026-11-14T09:14:01Z): "I adopt all five decisions and the
  target theorem; preserve r3 now".
- **Three-part target, #914 comment 6875548603** (2026-11-14T09:56:47Z): "To be more precise, OI
  should actually be a superset of QM.  OI should include QM and GR." and "Yes proceed as
  suggested." Inclusion, sector and gravity replace the two-way sentence of 6875046763.
- **Authorization of the amendment, #1169 comment 6875724719** (2026-11-14T10:12:11Z): the owner
  "replied **"I approve"**"; scope a paper-only forward amendment; "Not authorized: merging,
  experimental/simulation/Lean execution, adopting E or C as a physical premise, scientific status
  promotion, changing board priorities or initiating QB5(a)."
- **Five dispositions, #1169 comment 6876591512** (2026-11-14T11:28:20Z): "I adopt all five Gate A
  dispositions". The adopted text, quoted there verbatim:
  > 1. C applies to the underlying model. It should be a physically stated condition, with its consequences for experiment families defined explicitly. This refines the earlier wording on #914. Its physical justification remains an obligation.
  > 2. Require coverage and soundness. Necessity remains an optional future theorem. Models outside C may also reproduce quantum statistics. Membership in C need not characterize every possible quantum realization.
  > 3. Make one model the ultimate target. One fixed model, with one common extension E, must support subsystems realizing every quantum carrier in the agreed scope. Establishing this across one common architecture is an intermediate milestone. The ultimate model must accommodate arbitrarily large finite carriers, with the permitted encodings and resource requirements stated explicitly.
  > 4. Require quantum behaviour for every physically performable experiment within C. This includes accessible preparations, interventions, compositions and complete records under the retained contract. Access closure must prevent a model from qualifying through selected quantum experiments while also permitting stronger-than-quantum experiments.
  > 5. Prepare r4 for preservation on main through the normal gates. The landing-status note should distinguish the reviewed amendment proposal, any subsequently adopted owner decisions, and the remaining scientific obligations. Preparation should include review of the final commit and CI. Preserving this record carries no adoption of a particular C or E, and adoption of the amended target requires an explicit owner decision.
- **Pointer, #914 comment 6876592679** (2026-11-14T11:28:26Z): records on #914 that answers 1 and 3
  refine the target of 6875548603 (answer 1 its sector wording, answer 3 its inclusion part) and
  restates answers 2 and 4; it adds no decision.

**Relation of answers 1–4 to r4** (this note's reading; the answers are the source). The answers
postdate `927915e9` and are not in the record's text. Answer 1 selects r4's C-model type (r4 §5.2,
question 1), not C-law, and adds that C is physically stated with its consequences for experiment
families defined explicitly. Answer 2 answers question 2 "no": S⇐ᴺ is not part of the target.
Answer 3 takes the single-model reading of question 3 (r4 §8 item 3) as the ultimate target and
r4's I (one architecture, one instance per (A, T)) as an intermediate milestone, and requires the
permitted encodings and resource requirements of the single model to be stated explicitly, which
r4 does not. Answer 4 keeps S-A (question 4, first option).

**Not adopted.** `GATE-A-AMEND-r4.md` is not adopted as the governing Gate A contract; it remains
the reviewed amendment proposal, and #1169 comment 6876591512 says it "is not edited by these
answers". No C and no E is proposed or adopted. The accepted contract `endpoints.md` is unchanged.

**What would adopt the amendment text.** Item 5: "adoption of the amended target requires an
explicit owner decision". This note's reading is that such a decision, recorded with author and
time, would name the text (file and blob or commit) and state how answers 1–4 apply to it (as
recorded decisions beside r4, or through a revised and re-reviewed text). No decision adopting
`GATE-A-AMEND-r4.md` or a revision of it is recorded on #1169, #914 or PR #1289 as read (comments
through 2026-11-14T11:28:26Z; none later at 12:33Z).

## 3. Evidence preservation

**Basis.** §A.46 item 2 admits the record only through item 8: no established claim needs it, and
no file on `main` at `dfeec843` cites it (`git grep`). Owner item 5 is the stated rationale for preservation.

| §A.46 item 8 condition | State at `927915e9` |
| --- | --- |
| Substantive, nonredundant result | the record holds a line-by-line amendment of the contract and conditional statements (§1), not a theorem; whether this meets the condition is not recorded (§6 item 2) |
| Scope and evidence limits documented | r4 §9, `README.md`; this note |
| Independent non-author review and a ChatGPT exact-head review; landing checks incl. §A.42 item 8 | non-author model reviews exist (§1); no ChatGPT exact-head review is recorded (PR #1289 has no reviews or comments); tracing in this note, reviewed in r1 by the non-author review; r2 unreviewed |
| Accountable Issue, verification status, remediation plans | #1169 for the record. Verification status: §1. Remediation plans: §1 for each open obligation and for the partially verified content; the Bell clause and the kinematics input have no accountable Issue named in the record or in the owner records read, so this condition is not met for those two items; naming an accountable Issue for each would close it (§6 item 8) |
| Rationale and a separate recorded owner merge decision | rationale: owner item 5; merge decision: none |

**What preservation would mean.** The record's text, review trail and this note become
reproducible from `main`; under item 8 its scoped result is a surviving claim for item 6 and §A.42
item 5 while it remains applicable.
**What it would not mean.** No claim becomes established (§A.46 item 1); evidence layers do not
change; no C or E, no target and no contract change is adopted; nothing in it may serve as a
premise of an established claim without independent validation (§A.46 item 7).

**References off `main` (§A.42 item 8), traced claim by claim.**

| Reference | Claim it is attached to | Classification | What would close a gap |
| --- | --- | --- | --- |
| #914 comments 6875046763, 6875548603; #1169 comment 6875724719 | authority (r4 §1); definitions of §5 and requirements of §3.2 | support on `main` through verbatim quotation with author and time (§A.42 item 7); the comments are provenance for the quotations | none; quotations in r4 §1 re-checked against the API text for this note; r4:54 classifies these comments as provenance for authority; this note classifies the quotations as support on `main`, since the §3.2 requirements and §5 definitions use their content |
| #1169 comments 6876591512, #914 6876592679 | §2 of this note | quoted in this note with author and time | none once this note lands with the record |
| #1169 comment 6703342848 | r4 §3.2 requirement row (r4:144); owner question 4 (r4:430–433, `OWNER-QUESTIONS-r4.md`:44–47) | support on `main` through quotation with time: "We do not need the hidden machinery itself to be quantum" and "a quantum counterpart for every behavior admitted by the physical OI interface" are verbatim; the clause "deterministic hidden dynamics admissible" paraphrases the comment, whose words (`amaybaum` account, 2026-11-07T06:25:11Z) are "Deterministic hidden dynamics and indirect recovery of hidden information are admissible." | none once this note lands with the record |
| #1169 comment 6763928950; #1169 and #1143 bodies; #1169 comment 6703342848 as a trace §2 entry | dependent statements (trace §2), §4.2 | provenance (quoted to identify statements; not support) | none |
| #1169 comment 6686258585; #1173 comment 6686122542 | identity of the accepted Gate A head | support on `main`: the blob `d9d92e03` at `fdc3dd7f`, `9d24914c` and `dc0b333a`, all on `main`, and the acceptance of `endpoints.md` at `fdc3dd7f` stated on `main` in `oi-qm-ext-1/two-mode-drive.md`:3, with `oi-qm-ext-1/README.md`:26 linking the acceptance comment | none |
| Branch `records/target-theorem-914-20261114` at `755f9bff` (PR #1287, open, draft): `TARGET-THEOREM-r3.md`:34, rows T5b ⇒/⇐, `README.md` | r4 §7 R2 "reading, not a definition"; r4 §1 | provenance: R2 rests on EP:43 and EP:110 on `main`; line 34 itself sources its row to EP:33–43 | none for any claim; the citation resolves on `main` only if PR #1287 lands |
| Research branches named in PR #1287's `README.md` (`records/bell-landing-plan-868-20261114`, `records/tune1-landing-plan-1236-20261114`, `research/tune1-step3a-1236-20261113`, `research/tune1-sourcing-1236-20261113`) | none: the PR #1287 lines this record cites do not use them | not referenced by this record | none |
| Review heads `65b0a929`, `eb515150` (and `ae2de57a`, `cea26912`) named in the review files and `README.md` | which text each review read | support off `main` until landing | a landing that keeps these commits reachable from `main`: a merge commit, and any branch update by merging `main` into the branch, not by rebase; no squash or rebase merge |
| Checkout names `wt-mainread`, `wt-target`, `wt-gatea` | where reviewers read | provenance; `README.md`:68–73 maps the first two, and `CONFIRM-r3.md`:8–9 names branch and commit beside `wt-gatea` | none |
| #1169 comments 6691915819, 6875057963, 6875553907; #1173 comment 6686000116 (`NOTES-r1.md`:33, :58) | the writer's reading list | provenance | none |
| Uncommitted working copies read by `REVIEW-r1.md` and `CONFIRM-r2.md` | which text the first two reviews read (§1) | support off `main`: the identity rests on the recorded `cmp` in `CONFIRM-r3.md`:34–38; the copies are not retained | cannot be landed; stated as a limit: the reviewed text of those two reviews is identified by that recorded check |
| CI run 43588379859 (§4) | merge readiness only | provenance (§A.42 item 2) | none |
| The non-author review of r1 of this note, held outside the repository | the review state stated in this note's header and §4 | support off `main` | landing the review file and this note's response with the note (§6 item 9) |

Dependencies: PR #1287 (provenance only, above); PR #1288 (TUNE-1 units, #1236): not cited, no
dependence; PR #1290 (unreviewed triage): created after this record, cites it as "Not adopted",
so the dependence runs from #1290 to this record, not the reverse; #914 and #1169: owner records
quoted above; #873: named as the open G3 coupling question, not used as support. PRs #1287–#1290
add no file at a common path.

## 4. Merge readiness

**Nothing in this note authorizes a merge.** Item 5 of #1169 comment 6876591512 authorizes
preparation only: "It does not authorize the merge, which needs its own owner decision".

| Gate | State as read |
| --- | --- |
| Independent review of this note | r1: non-author model review, ACCEPT WITH CHANGES (four medium, twelve low findings, none blocking), not in the repository or on GitHub; r2 applies the findings (one in modified form) and has no review of its own |
| Exact-head review of the final commit (§A.46 item 8: ChatGPT exact-head review) | none; the final commit, which adds this note, does not exist yet; `927915e9` itself is unreviewed |
| CI at the final head | at `927915e9`: workflow `verify`, run 43588379859, event `pull_request`, attempt 1, 11:05:52Z–11:16:17Z; 26 jobs success, including the required contexts `Lean kernel check`, `Mathlib bridge` and `Numerical probes`, and 1 skipped (`Numerical probes / A42 exclusion`, which runs only on `workflow_dispatch`). A `pull_request` run tests GitHub's synthetic merge of the head into `main`, not the head itself (§A.39). `main` was at `dfeec843` throughout; the PR's test-merge commit is `29dd4cda` (parents `dfeec843` and `927915e9`, 11:05:47Z), whose tree differs from the head's only in `AGENTS.md`, but the run record names only the head, so which merge commit the run checked out is not recorded. The workflow runs on `push` only for `main`, so no push run exists for this branch; no `workflow_dispatch` run exists, and a dispatch needs its own owner authorization (§A.43 item 4). The final head needs its own run |
| Explicit owner merge decision | none recorded |
| Draft state and base | PR draft (must be marked ready). GitHub reports mergeable, `mergeable_state` `behind` (5 ahead, 9 behind `main`, merge base `c3b5f37a`). The repository ruleset for `main` requires branches to be up to date before merging (`strict_required_status_checks_policy`) and allows merge, squash and rebase; it also sets `require_code_owner_review`, and `main` has no `CODEOWNERS` file; bypass permissions are not visible through the public API. Unless bypassed, the branch must be updated with `main` before a merge, which creates a new head needing its own exact-head review and CI |

## 5. Record lines overtaken since they were written

- r4:7–12 describe r4 as "itself unreviewed"; `CONFIRM-r4.md` §6 notes this was accurate when written.
- r4:224, :283–284, :308–309, :382–383 and §8 (r4:410), `OWNER-QUESTIONS-r4.md` throughout and
  `README.md`:18 present four open owner questions; all four were answered at
  2026-11-14T11:28:20Z (#1169 comment 6876591512), which leaves r4 unedited. `README.md`:3 reads
  "Work in progress".
- `CONFIRM-r4.md` optional suggestions O-a to O-e are not applied; O-a would change r4's text.

## 6. Open owner decisions raised by the landing

1. Whether to adopt r4 as the governing Gate A contract, and whether answers 1–4 are recorded beside
   r4 or written into a revised, re-reviewed text.
2. Whether the record meets §A.46 item 8's "substantive, nonredundant result" condition.
3. Whether the §5 lines are corrected in place in `README.md` before landing (r4 and
   `OWNER-QUESTIONS-r4.md` are reviewed text), and whether O-a to O-e are applied.
4. Who performs the ChatGPT exact-head review of the final commit, and whether r2 needs a
   confirmation review.
5. Merge method and branch update. The ruleset allows squash and rebase as well as merge; only
   a merge commit keeps the review heads reachable from `main`. The up-to-date rule requires
   updating the branch with `main` before a merge unless bypassed; updating by a merge of `main`
   into the branch keeps the review heads as ancestors, a rebase does not. Either update creates
   a new head needing review and CI.
6. The #1169 planning-status block, as read, names Codex as main writer since 2026-11-09, records
   Claude as paused, and has no row for this record; comments 6875724719 and 6876591512 name no
   writer. Whether a row and a designated writer are recorded (§A.45 rule 3).
7. Whether PR #1287 lands before, with or after this record.
8. Which Issue is accountable for the Bell clause B and for the kinematics input; the record and
   the owner records read name none (§A.45 rule 6; §A.46 item 4).
9. The note's file name at landing, its listing in `README.md`, and whether this note's review
   and response land with it.
