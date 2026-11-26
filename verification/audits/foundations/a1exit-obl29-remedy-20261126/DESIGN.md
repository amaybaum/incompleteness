# OBL-29 remedy for removal of finding evidence (paper design r2)

## 0. Status, authority, scope and goal link

**Status.** Paper design r2, pending independent review of this revision and an owner decision.
The proposed requirements (ids `R6.OBL29.n`) have no force until adoption. OBL-29 remains an explicit
A1 retirement blocker until a remedy is implemented and independently verified. The interim
procedural guards (AGENTS.md §A.50 item 3 and §A.46 item 6) and adoption alone do not discharge it.

**Authority.** Owner decision (amaybaum, received 2026-11-26T11:44Z, coordinating session; recorded
at #1169 comment 7191104852), item 2, quoted:

> I authorize a separate paper-only remedy design and independent design review.
>
> The design must:
> - Cover every type of post-F change that removes a finding, not just deletion.
> - Identify the underlying correctness failure and derive a general remedy rather than enumerating special cases alone.
> - Distinguish legitimate removal from removal that improperly bypasses an outstanding obligation.
> - Include positive controls, negative controls and adversarial countercases.
> - Assess compatibility with amendment 6 and the existing verification architecture.
>
> Keep the remedy separate from r5. Implementation, adoption and trial execution require separate authorization.
>
> OBL-29 remains an explicit retirement blocker until its remedy is implemented and independently verified. Interim procedural guards do not discharge it.

The owner continued the paper revision and independent review on 2026-11-26 at 12:10Z
(#1169 comment 7191665350, item 2). The direction prefers all-ancestor traversal subject to
independent verification, requires retention of dissent and other discharge-constraining
evidence, requires the complete inventory of affected requirements, and calls for an assessment
of the squash and rebase gap before any acceptance. It also requires distinguishing malformed
historical content from evidence of an obligation and investigating a correction route that
preserves the original finding and its adjudication. Implementation, adoption and trial execution
require separate authorization. The prior draft at `0b06363c8dbb3d2c7e95a6ca7ab22cdc8cc7d234`
received REVISE (#1601 comment 7191637164).

**Base text.** The analysis follows design r6 amendment 6 r5 at
`1f5764572a98b7ae2f306e121e2e410f79c29daf`. Section 5 compares the current amendment 6 proposal,
r10 at `4fee62cff40b1acf52357fa177752f2d5b231dfa` on draft PR #1593. Both versions are off
`main`, verified at `942bd5ea1fd09f4223012b0755bce2d6da07c44a`. The relevant source files lie
under `verification/audits/foundations/a1exit-design-r6-20261125/`. Amendment 6 addresses
whether a resolution still applies. OBL-29 addresses whether finding evidence can disappear
while the obligation it established still applies.

**Goal link (AGENTS.md sec. A.47).** The work serves A1 retirement (#1169) and its blocker OBL-29
(Issue #1598). The design seeks to keep a category-3 finding binding until its obligation is
discharged and states the effects on amendment 6. The squash and rebase gap remains open (§6).

**Scope.** Category-3 findings and the predicates that decide whether their discharges apply.
The second-review clause of R6.REC.6 is in scope for the cited reassessment and its repair's
reconciliation record. Extending the same rule to other record kinds is an owner decision (§5.4).

***

## 1. The failure

### 1.1 What the mechanism computes

Let `S(c)` be the set of regular-file entries `(path, blob)` under `verification/audits/` in the tree
of commit `c`, and let `Det` be the detection function of R6.RECON.35, which maps an entry to the
findings it carries (none, well-formed, form-failed or malformed). Under r5, the findings a run sees
are

    Found(run) = Det(S(M)) ∪ Det(S(F)) ∪ Det(S(REV)) ∪ Det(records the run reads)

where `Det` also excludes every entry under a prefix of the tool-landing class (R6.RECON.35,
"Tool-landing prefixes"). A finding binds a configuration (R6.RECON.26) and is lifted only by a
discharge: the configuration no longer carries any edit the finding binds, or its freeze cites an
applying reassessment that names the finding (R6.RECON.27). Discharges are read from the
configuration at `F` and from records that configuration pins.

### 1.2 The obligation the design states

R6.RECON.26 makes the block an event property: once a finding has been landed, "no reconciliation
record, resolution, supersession, or later commit that reverts or repairs the change clears the
block", and only a discharge lifts it. The owner's lifecycle tables (#1169 comments 7185092393 and
7185562871) say the same: the finding is preserved, the block persists for the frozen plan, and
only reassessment and a revised, frozen plan restore eligibility. Write `Obl(t)` for the set of
findings established up to time `t`. The design requires, for every later check time `t' >= t`:

    (I) Obl(t) ⊆ Obl(t'), and every finding in Obl(t') binds until a discharge lifts it.

### 1.3 The invariant that fails

`Found(run)` is computed from snapshots. `S(M)` is not monotone in time: any later commit can make
`S(M')` lack an entry that `S(M)` held, or hold it at a path, mode or content that `Det` no longer
selects. `S(F)` and `S(REV)` are fixed, but they cover only findings that were present when `F` or
`REV` was made. Requirement (I) is therefore computed from an input that does not satisfy it.

**Failure statement.** The block decision must be monotone in the history of recorded evidence,
but it is evaluated over the current content of the repository, which is not. Every rule that uses
the evidence is affected according to its polarity:

- **Monotone predicates** (true when more evidence exists): the detection of findings. Removing
  evidence makes them false, so a finding is lost.
- **Antitone predicates** can become true as evidence is removed. R6.RECON.27 Keys (b) admits
  `repair: null` when a review's `reviewed` reference names no record the scan finds. Keys (a)
  admits it for a rejected first-kind finding only where no independent reviewer asserts the
  invalidation. Deleting the reviewed reconciliation record or the review that establishes the
  independent assertion can relax these conditions. R6.REC.6 also fails a cited reassessment or a
  repair's reconciliation record when a second review dissents on any item. Deleting that review
  can make the discharge apply.

- **The selector.** `Det` depends on the tool-landing class of the configuration's side-change class
  record. A later configuration, frozen anew, can widen a tool-landing prefix, or pin a blob, so
  that it covers a finding's path. That takes the finding out of detection without touching it.

This covers every change in #1598 that removes already reachable evidence. A finding landed and
removed before `F` can escape all three r5 snapshots. A `REV` record seen once and missing from a
later run likewise escapes r5. Whether the proposed history walk preserves that record depends on
how it reached `main` (§6).

### 1.4 What a removal can change

The decision's inputs are: the set of commits that the run's role commits reach; the object store;
the detection function; and the discharge records the configuration pins. A change that "removes a
finding" must alter at least one of these. It cannot alter commits that are already reachable,
because they are immutable. So it must make some of them unreachable (a history rewrite), lose
objects, change the detection function, or change what is evaluated over the current tree. The
remedy reads reachable history, fixes the selector and fails closed on unreadable required objects.
The coverage argument in §2.3 assumes continued reachability. Section 6 covers evidence that
never becomes reachable through the protected history or is lost through a history rewrite.

***

## 2. The remedy

### 2.1 Requirements

**R6.OBL29.1 The cumulative record set.** For op C with `M`, `R*` contains the regular-file
entries `(path, blob)` (mode `100644` or `100755`) under `verification/audits/` in every tree
reachable through any parent from `M`, `F` and `REV`, when named, together with the records
the run explicitly reads under its existing input rules. For a predicted `M`, scan `M0` and its
ancestors plus the in-memory chain through the predicted `M` (R6.TREE.15 and R6.RECON.21).
`F` and `REV` retain the evidence corresponding to those inputs. `X` and `C` do not root a
walk. Incidental files there are execution-side content, while a proof under §2.3 depends only
on evidence reachable from `M`. The reference `{path, blob_sha256}` identifies an entry
(R6.RECON.29). A byte-identical blob at a second path gives a second reference. Mode does
not enter the identity. Traversal order does not enter the set.

**R6.OBL29.2 Detection over `R*`.** Apply R6.RECON.35 to `R*` and retain the union of
its findings. Class (a) contributes when R6.RECON.26's form rules identify a finding. A
class (b) or (c) entry with an invalidation signal contributes a malformed finding, with
the existing run-level fallback and reviewed `repair: null` route. Without that signal,
a class (b) or (c) entry contributes neither a finding nor a diagnostic solely from history.
The current malformed-record check applies to entries in effective `M` and to records the
run reads, subject to the existing input-admission errors. For a historical-only finding
with a form failure, emit FAIL `record-invalid` on account of that failure while the finding
binds and lacks an applying discharge. After an applying discharge, preserve the finding
and its witness without a FAIL due solely to its historical form. Otherwise a malformed
historical file could still irreversibly fail the run after a reviewed D3 discharge.
Finding identity remains reference plus `item`. R6.RECON.26's binding, lineage and
global matching rules still apply, including its `side_change_commits` condition where
applicable. Finding presence in `R*` alone can therefore differ from binding.

**R6.OBL29.3 Finding and dissent predicates read `R*`.** Evaluate every R6.RECON.26 or
R6.RECON.27 predicate about what the scan finds over the same detection set, including:
- Form (i), whether the reviewed record exists and supplies the author for checking
  independence. A review remains disqualified where the historical reference establishes
  a same-author review.
- Form (iv), whether the finding names an entry. Deleting the named entry does not widen an
  edit binding into a run-level binding or make a valid reassessment of the edit inapplicable.
- Keys (a) and (b), eligibility for `repair: null`, including whether there is an independent
  assertion of the invalidation. Count every review in `R*` that names the exact reference
  and meets the applicable form rule.
- R6.RECON.27's lookup of the finding a cited reassessment names, by original reference and
  `item`.

For the cited reassessment and the repair's reconciliation record wherever its lint is
required for discharge, the R6.REC.6 second-review clause checks every review in `R*` naming
that exact record reference. A second review with a non-`accept` item still fails the
record if the review disappears from current content. Keep the existing admission and
positive review requirements. Any other discharge predicate that becomes easier to satisfy
through removal of finding or dissent evidence must also read the cumulative evidence.

**R6.OBL29.4 Presence-based discharge conditions stay on current content.** Some conditions enable a
discharge only by the presence of evidence. These are read where r5 reads them, because a removal
can only make them fail. They are the repair's commits on `M`'s first-parent chain, the repair's current reconciliation
record entry and accepting non-author review in the scanned set at `M`, and the cited
reassessment and its accepting review through the existing pin and resolution rules
(R6.RECON.27 and R6.RECON.33). Historical acceptance cannot substitute for those inputs.

**R6.OBL29.5 A fixed selector.** For category-3 detection, R6.RECON.35's selection excludes no entry
on the ground of the tool-landing class, including at a path whose blob the class pins. Selection within the traversed trees depends
only on the fixed prefix `verification/audits/`, the regular mode and the entry's bytes.
Explicit input records retain their existing selection. The scanned set of
R6.RECON.2 (d) and (e), which governs which reconciliation records apply, keeps its exclusions
unchanged. A file under a tool-landing prefix that carries a finding binds. R6.TREE.5 still reports
it REVIEW_REQUIRED `side-change-unclassified` when it is unpinned.

**R6.OBL29.6 Removal is never a discharge.** Deletion, rewriting, moving, renaming,
changing mode, replacing with a non-regular entry, prepending or truncating bytes, merge resolution
and supersession do not discharge a finding. A finding in `R*` binds a configuration until
one of the discharges of R6.RECON.26 applies to it, as R6.RECON.27 defines them. Either the
configuration carries no edit the finding binds, or the configuration's freeze cites an applying
reassessment that names the finding's reference and `item`. Each is evaluated with
R6.OBL29.3 and R6.OBL29.4. Missing, unresolvable or non-applying discharge evidence leaves the
block standing.

**R6.OBL29.7 The ancestry walk.** `R*` is computed by one walk through the verified reader
(R6.REC.17). It starts at the roots in R6.OBL29.1, visits each commit reachable through its parsed parents
once (keyed by full id), and ends when no unvisited parent remains, which happens at parentless
commits. It reads parents only from verified commit content. Refs, reflogs, replace refs, grafts,
the `shallow` file and commit-graph files are never consulted. A commit, tree or blob that the walk
needs and that is missing or does not hash to its id is an unresolvable object: ERROR, and no
verdict. A parent absent from a shallow store is one such case. There is no count or depth limit,
so no reachable finding sits beyond a depth bound. The commit traversal visits each reachable
commit and parent edge once. Object reading and tree comparison add work proportional to
the entries examined.
*Equivalent computation (informative).* The tree-derived component of `R*` equals the
parentless commits' full entry sets plus the entries of every other visited tree that differ
from its first parent's tree.
Each entry of a reachable tree is either present in the first parent's tree, which is itself
visited, or new relative to it. Because selection depends only on the entry (R6.OBL29.5), a per-entry
detection cache keyed by `(path, blob)` is exact.

**R6.OBL29.8 Result fields.** Each element of `category3.findings` (R6.RECON.36) gains two fields.
`present_at_M` is a boolean that says whether `M`'s tree holds the finding's reference. `witness` is
the full id of one commit whose tree holds it, chosen deterministically: `M` if present, else
`REV`, else `F`, else the first commit on `M`'s first-parent chain going back from `M`, else the
smallest id among the other commits that supply it, including a verified source commit for
an explicit record input. A predicted `M` uses its computed object id when it is the witness.
A finding with `present_at_M` false that no
discharge lifts appears among the `blocked` elements with FAIL `retirement-blocked`, as any other
finding does. A finding that a discharge lifts appears with the applying reassessment, or with no
blocked element when the configuration carries none of its edits. No new outcome class is
introduced.

**R6.OBL29.9 Status of the blocker.** OBL-29 is discharged only when the remedy is adopted by a
recorded owner decision, implemented in the tool revision, and independently verified, with the
controls of CONTROLS.json holding under the gate (sec. 16 of r6). Procedural guards do not
discharge it.

### 2.2 What the remedy does not add

It needs no new record kind, configuration field, owner-authorization input, epoch constant or
outcome class. It adds no change to R6.RECON.23. The existing discharges (R6.RECON.26, R6.RECON.27)
are the only route out of a block.

### 2.3 Persistence under ancestry extension

Let `M` be an ancestor of a later `M'` under P-1. If `c` is reachable from `M`, it is also
reachable from `M'`. The tree entries of `c` remain the same, and the fixed selector identifies
the same candidate finding evidence. A missing or corrupt required object produces ERROR.
Consequently the `M`-derived part of `R*` is monotone. Changing `F` or `REV` cannot erase
a witness reachable from `M`. Evidence known only through those additional roots or explicit
inputs has a narrower guarantee while it has no witness reachable from `M` (R-1).

For a fixed configuration and applicable side change, removing current files cannot erase a
finding or its reviewed reference witnessed in `M`'s ancestry, change the result of "the scan
finds" for such evidence, or erase a dissent witnessed there. Removing evidence required at
`M` can cause a discharge to fail. The original form, independence and scope rules still
determine whether the persistent evidence establishes a binding finding. For example,
establishing a reviewer's lack of independence can disqualify it. That is a determination
from the evidence, not a consequence of removing it.

A first-parent-only walk needs preservation of `M` on every later first-parent chain. A
foxtrot fast-forward can put `M` on a merge's second-parent path without breaking ancestry
(P-FOXTROT). All-parent traversal therefore proves persistence with the weaker P-1 (§5.6).

### 2.4 Coverage of the change types (consequence of 2.3)

| Change after the finding is recorded | Why it does not lift the finding |
|---|---|
| deletion of the file | the entry is in an earlier reachable tree |
| rewrite: verdict to `accept`, `invalidated` removed, entry removed, `configuration` altered | the old blob is a distinct entry in an earlier tree |
| move or rename, in or out of `verification/audits/`, chains included | the old path's entry persists; each new path is a further entry |
| move under a tool-landing prefix, or a new freeze widening a prefix or pinning the blob | R6.OBL29.5: no tool-landing exclusion in detection |
| mode change `100644` to `100755` | mode is not part of identity; still regular |
| replacement by a symbolic link or a submodule | the regular entry persists in the earlier tree |
| prepended bytes, truncation, re-encoding, invalid bytes | the original blob persists; the altered blob is classed on its own |
| corruption of the stored object | ERROR (R6.OBL29.7), never a pass |
| deletion and re-add with altered content | the original blob persists |
| removal by a two-parent merge resolution | each parent remains reachable, so the parent that carried the evidence is scanned |
| add and remove within a branch that is then merged | covered when the merge preserves that branch history. A squash can discard the intermediate entry and a rebase can change its applicability (§6) |
| record seen in an earlier `REV` and dropped at merge | a merge commit with that `REV` in its ancestry retains it. Squashed, abandoned or superseded `REV` histories require separate assessment (R-1) |
| supersession by a later record | R6.OBL29.6 retains the original and its obligations |
| removal before `F` | an entry already reachable from `M` persists regardless of the freeze |
| deletion of the record that a second-kind review names | Form (i), Form (iv) and Keys (b) still find it in `R*` |
| deletion of review evidence establishing an independent assertion | Keys (a) still counts the review in `R*` |
| deletion of a dissenting second review of a reassessment or its repair record | R6.OBL29.3 preserves the R6.REC.6 lint failure |
| owner-approved evidence removal (AGENTS.md §A.46 item 6 and §A.50 item 3) | R6.OBL29.6 retains the obligation and §A.46 item 6 requires continued reachability of the evidence |
| history rewrite of `main` | R-2 limits the guarantee to P-1 |
| a finding seen only outside the protected history or selector | R-1 and R-7 bound what the scan can recover |

***

## 3. Legitimate and improper removal

**Rule.** Whether a removal is legitimate is decided by whether every obligation the removed content
carried is discharged. The removal event itself decides nothing.
- A removal is **legitimate** when, for each finding in `R*` that the removed content carried, and
  for every configuration it binds, one of the discharges of R6.OBL29.6 applies. The evidence for
  each discharge is defined by R6.RECON.26 and R6.RECON.27. Either the citing configuration's ledger
  carries no edit the finding binds (no id, migrated id or target match). Or the configuration's
  freeze (`records`, kind `reassessment`) cites an `oi-reassessment/1` record whose `finding` names
  the original reference and `item`, with a non-author review, record lint, the re-derivation, the
  verdict `no-effect`, `edit` bound to the configuration's canonical entry, and either a repair (its
  commits on `M`'s first-parent chain, its entry present at `M` with an accepting non-author review)
  or `repair: null` where Keys admits it, with eligibility read over `R*`.
- A removal is **improper** when some finding it carried has no applying discharge for the
  configuration. Then the finding binds, and the run reports FAIL `retirement-blocked` with
  `present_at_M: false`.
- **Fail closed.** A discharge whose evidence is missing, does not resolve, or does not apply does
  not exist. A finding that no discharge lifts binds. The tool never reads an owner approval, a
  commit message, a disposition note or a deletion's justification as discharge evidence
  (R6.STAT.4, R6.PUR.11). A configuration that references a record kind outside R6.RECON.33's table,
  such as an owner-authorization record, is ERROR `CONFIG_INVALID` as now.

**The cases named in the authority.**
- *Reassessment.* Legitimate when an applying reassessment naming the original reference is cited by
  the new freeze. A reassessment naming the rewritten blob, or any reference that carries no
  finding, names no finding in `R*`: it fails R6.RECON.27 (FAIL `record-invalid`) and lifts nothing.
- *Supersession.* Never a discharge (R6.RECON.26). A superseded record may be removed, but its
  findings stay in `R*` until reassessed or the edit leaves the plan.
- *Owner-approved evidence removal* (AGENTS.md sec. A.46 item 6, sec. A.50 item 3). It is legitimate
  as a repository action. It changes no obligation. Sec. A.46 item 6 already requires the original to
  stay reachable in history without rewriting it, which is exactly what `R*` reads. The procedural
  guard and the mechanical rule therefore agree.
- *A finding that was itself record-invalid.* Amendment 6 detects before lint, so such a finding
  binds (form failure). Its removal is legitimate only after an applying reassessment, with
  `repair: null` where Keys (a), (b) or (c) admit it, read over `R*`. A malformed file of class (b)
  or (c) needs one with `item: null` and `edit: null`.
- *A finding by an independent reviewer that later proves mistaken.* The current Keys proposal
  still requires repair and an applying reassessment, or a revised plan to which the finding
  does not bind. Withdrawal or deletion adds no discharge. Section 5.6 evaluates controlled
  correction routes for the owner's decision.

***

## 4. The walk bound and an unreadable history

- **Bound.** The walk covers the commits reachable from the role commits and terminates at
  parentless commits. It runs between explicit commits at one end and the roots at the other, as the
  reference-resolution walk of R6.RECON.33 already does. There is no depth limit. A depth limit would
  put a removal just beyond it out of reach (control N-BOUND-DEPTH).
- **At the boundary.** Each root's whole tree is scanned. An entry present at a root and removed in
  its child is in `R*` (control N-ROOT).
- **Unreadable history.** A missing or unverifiable commit, tree or blob, a shallow store, or a
  pruned object is ERROR. The run produces no verdict, so a PASS is impossible. Replace refs and
  grafts that would hide a commit are not applied.
- **Cost.** One tree comparison per reachable non-root commit and one detection per distinct
  entry, with subtree-hash pruning. The initial reviewer counted 6,021 commits by ancestry
  and 1,205 by first parent at the reviewed `main` snapshot. These counts describe that
  snapshot and do not bound later verification work.

***

## 5. Amendment 6 compatibility and decisions

### 5.1 Resolution validity and the current proposal

R6.RECON.23 tests whether a resolution to a landing-trial finding or a carried site still
applies at the landing. OBL-29 preserves the category-3 finding and the evidence needed to
test its discharge. The r7 resolution-route table and its later refinements in r10 leave
the category-3 detection and reassessment model in R6.RECON.26–.27 in place. The r10
`resolution_validity` field describes a failure to keep a matched trial resolution or
carried site under R6.RECON.23. R6.OBL29.8 adds fields only within `category3.findings`.
The same output requirement and schema document both kinds of data. Amendment 6 r10
still states that the OBL-29 remedy must be implemented and independently verified to
discharge the blocker (§32). This paper proposes the remedy independently of that amendment.

### 5.2 Reassessment and migration records

A reassessment resolves its finding from `R*`, reads the repair entry at `M`, and counts
historical dissent for record lint (R6.OBL29.3–.4). Its keys, item ids, positive review and
freeze citation retain their existing requirements. REASSESS-FORM and REASSESS-KEYS keep
their schema cases. An edit-id migration remains a pinned match route under R6.RECON.28
and establishes no discharge.

The current reference-and-item rule requires a reassessment for each distinct finding
reference created by a rename or rewrite. A byte-identical rename still creates a second
reference. Section 5.6 gives the alternative and its consequences.

### 5.3 The tool-landing prefix

R6.OBL29.5 removes the tool-landing prefix exclusion for detection. Record admission in
R6.RECON.2 (d) and (e) keeps its current selector. P-TL-CLEAN applies the detection rule
over the entire `R*` of predicted `M`, including inherited history and the tool's own
landing paths. It checks for an accidental finding in the fixture. Any genuine finding
there follows the usual binding and discharge rules.

### 5.4 Dissent outside category-3 discharge

R6.OBL29.3 applies the second-review rule to the reassessment and the repair's
reconciliation record when that record's lint affects discharge. Other kinds have the
same deletion vulnerability when their lint reads only snapshots. Proposed R6.OBL29.10
would extend the history rule to all other records governed by R6.REC.6. That affects
record admission beyond this remedy's required category-3 scope. Section 5.6 gives the
scope decision. Presence and uniqueness conditions in R6.RECON.2 (d) and (e) and the
lineage checks in R6.REC.7 still use their prescribed inputs. They determine the record
to evaluate. Where the selected record serves as evidence of a discharge, the historical
dissent requirement still applies.

**R6.OBL29.10 (scope option)** Extend the R6.REC.6 second-review source rule of R6.OBL29.3
to other record kinds when those kinds undergo R6.REC.6 lint.

### 5.5 Requirements affected on adoption

The table records the proposed changes relative to r5 and cross-checks them against the
same requirement locations in r10. They would need a separate amendment on adoption.

| Requirement | Proposed effect |
|---|---|
| R6.RECON.26 | Use `R*` for detection and for each "the scan finds" predicate in Forms (i) and (iv). State that the original finding remains as reachable evidence after a legitimate removal. Preserve the independence, lineage, edit and side-change predicates. |
| R6.RECON.27 | Look up the finding in `R*`, evaluate Keys (a)–(b) and the corresponding Form (iv) basis over `R*`, and count historical dissent in the applicable lint. Keep the current repair entry, positive review and first-parent predicates. |
| R6.RECON.33 | Change its last reference-resolution sentence. The finding comes from `R*`; the repair entry remains in the scan at `M`. The record-kind table and existing resolution anchors retain their scope. |
| R6.RECON.35 | Use the fixed detection selector and limit history-only failures to outstanding finding evidence. Replace the post-`F` removal and tool-landing paragraphs with the proposed detection rule and its reachability conditions. |
| R6.REC.6 | Count second reviews in `R*` for a cited reassessment and for its referenced repair record when its lint is required. Apply the same change to other kinds only if the owner selects R6.OBL29.10. |
| R6.REC.17 | Add the verified all-parent walk to parentless commits as an exception to the explicit-endpoint rule. |
| R6.RECON.36, R6.OUT.18 and the result schema | Add `present_at_M` and `witness` within each `category3.findings` element. |
| OBL-29 (§32) | Record the expanded removal and predicate scope, the remaining coverage gaps, and the adopted, implemented and independently verified remedy required by R6.OBL29.9. The existing r10 discharge text and the earlier r7 wording are compatible with that condition. |

R6.RECON.2 (d) and (e), R6.RECON.23, R6.RECON.28, R6.CFG.1–.8 and R6.TREE.5 can retain
their text. R6.TREE.5's classification check and the category-3 detection check can both
apply to the same file. Existing controls retain their expected outcomes within their
fixtures. RECON-BLOCK still fails when a later run's `REV` omits an already landed finding.
GV5's positive shallow-store case runs `terms` with all its required objects. Each op C
run with `M` needs every object required by the ancestry scan, so that shallow success does
not generalize to op C. Recheck existing op C fixture completeness and the expanded result
schema at any later implementation. CONTROLS.json specifies new expectations and carries
no runners.

### 5.6 Decisions before adoption

| Decision | Alternatives and consequences | Review and owner position |
|---|---|---|
| Ancestry walk | All parents require ordinary ancestry extension and scan more commits. A first-parent walk requires first-parent preservation and would lose the foxtrot witness, even with ordinary ancestry extension. | The reviewer preferred the weaker ancestry premise. The owner prefers all parents subject to independent verification. R6.OBL29.1 uses it for this draft. |
| Reachability after squash, rebase or a `REV` change | A protected landing that preserves the required commit ancestry or independently verifies a replay retaining the relevant evidence and applicability closes specific gaps. Requiring direct `main` evidence before a subsequent run would preserve the current selector and record identity. An independently checked retained evidence record could preserve a finding and its witnesses even where a merge omits the commit, and would require new admission and verification rules. R6.RECON.26's existing land-at-once procedure reduces exposure but cannot establish mechanically that an earlier run saw more than the next run. | The reviewer called for explicit boundaries and cited the land-at-once procedure. The owner requires assessment and has accepted no squash/rebase residual. Section 6 describes the cases. The alternatives remain open. |
| Mistaken independent finding | Current Keys requires a repair and applying reassessment, or a plan that no longer binds. This can exclude otherwise sound work across all matching lineages. A narrowly extended `repair: null` route could require an independently reviewed adjudication attached to the original finding and a new freeze, reusing the reassessment flow. A dedicated adjudication record could carry the original reference and `item`, review, evidence and scope explicitly, with a larger schema and admission change. | The reviewer identified the indefinite liveness cost. The owner favors controlled independent adjudication and asks that it be investigated. Neither route is adopted here. |
| R6.REC.6 beyond reassessment and repair | Apply the required fix only when lint affects a category-3 discharge, or apply R6.OBL29.10 to other kinds too. The latter prevents analogous deletion bypasses and changes unrelated record-admission outcomes, including the effect of mistaken historical dissent. | The reviewer treated the discharge case as a correctness defect and the broader case as a scope choice. |
| Renamed findings | Keep exact reference plus `item` and reassess every reference, or add a tightly checked multi-reference reassessment for byte-identical copies and the same `item`. The latter reduces repeated work and requires checking each path's independence and review location. A blob-and-item identity would change R6.RECON.35 and needs the same review-location analysis. | The reviewer saw a sound route in principle with those interactions accounted for. The draft retains exact identity pending a decision. |

A correction for a mistaken independent finding would need to preserve the original record,
path, blob and item, give the evidence and re-derivation showing why it was mistaken for
the cited target and configuration, and bind the decision to an authorized new freeze. The
adjudicator and accepting reviewer would require verifiable independence from the original
and corrective authors, with unresolved dissent keeping the block. An uncorroborated
withdrawal, a missing original, an altered reference or deletion cannot satisfy these
conditions. A later proposal would need to define who can adjudicate, the exact replay and
evidence requirements, how disagreement is resolved, and whether a decision applies beyond
its cited configuration. The draft's controls retain the current Keys outcome.

***

## 6. Assumptions and limits

- **P-1. Ancestry extends on `main`.** For successive `main` bases `M` and `M'`, `M` is an
  ancestor of `M'`. The active guardrail ruleset requires a PR and bars non-fast-forward
  updates and deletion for its covered default branch, subject to the host's bypass handling.
  The tool sees only verified parents and cannot reconstruct an overwritten history.
- **P-2. Findings need a durable witness.** R6.RECON.26 directs landing a finding on `main`
  by its own commit before a subsequent retirement landing run. A later run can mechanically
  verify only the evidence its inputs and reachable objects supply.
- **P-3. Readable objects.** A missing required object fails closed. A complete store therefore
  governs availability.
- **P-4. Stable detection.** A later tool revision that narrows detection can forget findings.
  R6.STAT.5 and review of revisions govern that change. SCAN-PARSE and the proposed controls
  pin the cases.
- **P-5. Git object ids are collision resistant** (R6.REC.17).

**R-1. Evidence that never becomes reachable from `main`.** Ruleset 21725642 allows merge,
squash and rebase. A merge commit preserves the ancestor it actually merges, including a
file dropped by the merge resolution. A squash keeps the net tree change. It can omit a
finding or dissent added and removed within the branch, even if a prior run saw it. A
rebase rewrites original commit ids. A replay preserving the exact path and blob keeps a
record detectable, but a side-change predicate tied to an old commit id can cease to bind.
A replay omitting or changing the entry may also lack the original reference. Similarly,
an abandoned or force-pushed `REV`, an unmerged branch, a tag-only witness or an uncommitted
finding can escape subsequent runs. The absence of a finding in those runs does not
establish that no earlier run saw it. The risk includes loss of dissent needed to keep
a discharge inapplicable. The land-at-once procedure is an interim safeguard. Acceptance
of the squash/rebase gap and any additional safeguard remain open.

- **R-2. Main history rewrite.** Loss of a commit reachable from a former `M` violates P-1
  and cannot be detected by this walk alone.
- **R-3. Apparent malformed findings.** A historical malformed record without an invalidation
  signal creates no historical failure. The existing class (b)/(c) heuristic conservatively
  treats a record-shape or schema signal together with an invalidation token as finding
  evidence. Stray tokens can mimic that evidence. The r1 reviewer found that unparseable
  versions of amendment 6's EXPECTATIONS.json or this design's CONTROLS.json can meet
  class (c), for example after conflict markers corrupt a JSON-leading file. The reviewed
  run-level D3 reassessment can lift both the outstanding block and its historical-only
  form failure. A file still present at `M` or explicitly read keeps the prescribed lint. The r1
  reviewer reported
  zero class (a), (b) or (c) entries across 6,021 commits of `main` at
  `4bb48cddec206e567639fa863ecce852ddd8350e` and zero in the compared unmerged ancestry
  of r1 and amendment 6 r7. That report is evidence of the earlier review's scope. The
  r2 historical control calls for a fresh independent check at the current exact base.
- **R-4. Rename burden.** Additional exact references can require additional reassessments (§5.6).
- **R-5. Scan cost.** The total cost grows with the reachable graph, tree comparisons and
  distinct entries examined.
- **R-6. Other records.** R6.REC.6's second-review clause can still be relaxed by deletion
  for other kinds unless R6.OBL29.10 is adopted.
- **R-7. Selector boundary.** A file committed only outside `verification/audits/` and never
  explicitly read by the run does not establish a finding via the scan. Moving a previously
  reachable in-scope record out of the prefix still leaves its historical witness.

***

## 7. Reference trace (AGENTS.md sec. A.42 item 8)

| Reference | Use | Classification |
|---|---|---|
| commit `1f5764572a98b7ae2f306e121e2e410f79c29daf` (branch `design/a1-r6-amendment-6`): DESIGN-r6.md, EXPECTATIONS.json, REQUIREMENTS.json, AMENDMENT-6.md | the requirement texts this design amends and cites | support off `main`: the base text is not on `main`; this design lands nothing and is valid only relative to that text |
| amendment 6 r10 at `4fee62cff40b1acf52357fa177752f2d5b231dfa` (#1593) | requirement cross-check and open OBL-29 discharge | support off `main`, treated as a proposal |
| #1169 comment 7191104852 | the authority, quoted in §0 | provenance, quoted with author and time |
| #1169 comment 7191665350 | bounded r2 direction and open owner decisions | provenance, owner and time in §0 |
| #1601 comment 7191637164 and r1 at `0b06363c8dbb3d2c7e95a6ca7ab22cdc8cc7d234` | independent REVISE, reviewed scope and earlier scan | provenance for the reported observations and review |
| repository ruleset 21725642 (guardrail) | host permits merge, squash and rebase, and requires PRs and rejects non-fast-forward updates on the covered default branch | host configuration at the time of the comparison |
| #1169 comments 7185092393 and 7185562871 | the lifecycle tables behind requirement (I) | support off `main`; quoted in r5 sec. 0.4 and 0.5 on the amendment branches |
| Issue #1598 and comment 7191083365; PR #1593 comments 7189446310, 7190255132, 7190966287 | the defect statement and its wider scope | provenance |
| `main` at `942bd5ea1fd09f4223012b0755bce2d6da07c44a` | current governance snapshot, including AGENTS.md §A.52 items 5 and 6 | support on `main` |
