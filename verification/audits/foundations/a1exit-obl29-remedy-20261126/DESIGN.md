# OBL-29 remedy for removal of finding evidence (paper design r6)

## 0. Status, authority, scope and goal link

**Status.** Paper design r6, pending independent review of this revision and an owner decision.
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
received REVISE (#1601 comment 7191637164). R3 addressed the r2 review (#1601 comment 7192414933). This revision clarifies the lineage dependency raised by the focused REVISE on r3 at
`36d9071cac29075e2b57db11a17031760dbfd836` (#1601 comment 7192615596). R4 preserved
predecessor-review evidence. The focused REVISE on r4 at
`dd1ca3bc40ffe822928986bba9b8a5d67e8a91b9` (#1601 comment 7192760996) identifies
a competing successor seen through a changing post-freeze scan. The r5 review at
`c11e8d4aa82aa46f0557513d476c6fd5e4f03576` accepted that correction for the same
frozen inputs and found two re-freeze bypasses (#1601 comment 7192888727).

**R6 authority.** Owner amaybaum, recorded on 2026-11-26 at 13:22 UTC (#1169 comment
7193274406), authorized this bounded paper revision and independent review:

> - Re-freezing does not discharge a qualified adverse witness where the new freeze relies on the same disputed repair.
> - Clearance requires corrected evidence or independently reviewed, properly authorized adjudication that substantively resolves the witness.
> - Preserve the original adverse evidence, its provenance and the full adjudication history.
> - Repeated execution with the same frozen inputs must not administratively erase unresolved adverse evidence.
> - Squash and rebase risk is not accepted without demonstrating equivalent evidence custody and lineage preservation.

The decision calls for return of the exact revision for adoption. OBL-29 adoption,
implementation, trial execution and merge remain outside this paper revision.

**Base text.** Amendment 6 r5 at `1f5764572a98b7ae2f306e121e2e410f79c29daf`
establishes the original defect analysis. The operative comparison is Amendment 6
r13 at `5ad8837521de0a26734266a64f91548fd3dcff1e`, adopted by the owner as the tool
contract (#1593 comment 7193277489). Its PR remains open and unmerged into verified
`main` at `942bd5ea1fd09f4223012b0755bce2d6da07c44a`. See
`verification/audits/foundations/a1exit-design-r6-20261125/`. Amendment 6 addresses
whether a resolution still applies. OBL-29 addresses whether evidence can disappear
while the obligation it established still applies.

**Goal link (AGENTS.md sec. A.47).** The work serves A1 retirement (#1169) and its blocker OBL-29
(Issue #1598). The design seeks to keep a category-3 finding binding until its obligation is
discharged and states the effects on amendment 6. The squash and rebase gap remains open (§6).

**Scope.** Category-3 findings and the predicates that decide whether their discharges apply.
Historical review lint under R6.REC.6 is mandatory for a cited reassessment, its cited
repair's reconciliation record and any predecessor whose review an existing discharge
condition requires. The proposed R6.REC.7 addition retains competing-successor evidence
from the mutable scan only where it first qualifies under an existing discharge check.
The retention rule follows the disputed repair through later runs and freezes (§2.2).
Section 5.4 lists the separate scope choices.

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
Apply ordinary malformed-nonfinding lint to the current snapshot with its existing selector,
including the tool-landing prefix exclusion for unreferenced ambient entries at `M`. Explicitly
read records still undergo the applicable input and lint checks. Widening finding detection
does not widen this ordinary malformed-nonfinding lint (R6.OBL29.5). For a historical-only finding
with a form failure, emit FAIL `record-invalid` on account of that failure while the finding
binds and lacks an applying discharge. After an applying discharge, preserve the finding
and its witness without a FAIL due solely to its historical form. Otherwise a malformed
historical file could still irreversibly fail the run after a reviewed D3 discharge.
Finding identity remains reference plus `item`. Where R6.RECON.26 requires that `M`
contain one of the entry's `side_change_commits`, its exact commit id must equal `M` or
be an ancestor of `M` through any verified parent. First-parent ancestry alone would lose
applicability during a foxtrot fast-forward even though the finding remains reachable.
The lineage, edit and global matching rules retain their scope. This ancestry test affects
category-3 applicability only. The repair-commit test and the reconciliation condition RC1
still use first-parent histories (R6.RECON.27 and R6.RECON.4).

**R6.OBL29.3 Finding lookups and historical review lint read `R*`.** Evaluate every
R6.RECON.26 or R6.RECON.27 predicate about what the scan finds over the same detection set,
including:
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

**Direct review checks.** Apply R6.REC.6 to the cited reassessment `A`. For a non-null
repair, find the exact reconciliation record `Q` and its cited entry in the scanned
set of `M` and require its same-directory accepting non-author review at `M`
(R6.OBL29.4). In both cases check every eligible ordinary review in `R*` naming the
record's exact `{path, blob_sha256}`. The repair-review check applies the R6.REC.6 item,
verdict, form and reviewer rules to those exact-reference reviews of `Q`, including
complete, unduplicated coverage of `Q`'s required item ids. A review with a non-`accept`
verdict, an omitted item or a duplicate fails the discharge even if the review has left
the current tree and another eligible review accepts every item. A review of a
reconciliation record qualifies for this check only in that record's reconciliation
directory (R6.RECON.1, R6.RECON.35). A review elsewhere can still carry a category-3
finding. Historical review evidence cannot supply the current or pinned accepting
review. A repair entry selected solely from `M` does not acquire a new R6.REC.7
lineage check or anchor through that selection.

**Existing lineage checks.** `A` retains its R6.REC.7 check. In a chain run the
configuration cites `A` and its review under the existing frozen input rules, and
R6.RECON.33 resolves predecessor references at `F` or on its first-parent chain.
Under existing harness admission (R6.RECON.21), the pinned record is read from its
verified source commit for record lint, and R6.RECON.33 resolves references from the
named `REV` or, without `REV`, from that verified source. When `Q` is independently
admitted by an existing route which requires R6.REC.7 for its use in the discharge,
that route supplies the lineage check and its original anchor. Preserve
R6.RECON.2 (d)'s `REV` presence and competing-successor checks where that route
applies and the R6.RECON.33 reference-resolution rules. The addition below affects
only negative evidence contributed by the mutable scan to a discharge check. A required exact predecessor reference unresolvable
from its prescribed anchor fails `record-invalid`. An unreadable required Git object
is ERROR through R6.REC.17.

**Predecessor reviews.** For each existing R6.REC.7 check whose result is required for a
discharge, follow every required `supersedes` hop using that check's existing inputs.
At each exact predecessor apply its required review checks with the eligible reviews
from `R*`, preserving the normal review roles, item sets, location, independence and
positive review sources. Include a widening review where the original check requires
one. Failure of any required predecessor review keeps the discharge inapplicable.
Cumulative review evidence supplements the existing negative review checks.
Predecessor references and required positive reviews still use their prescribed inputs.

**Qualifying competing successors from the mutable scan.** In an existing R6.REC.7
check required for a discharge, consider each exact successor-to-predecessor edge
`U → P` already resolved under the prescribed lineage anchor. The fixed view at
`F`, the current scan of any admitted `REV` and the admitted records continue to
be checked as prescribed. A lineage check is in scope for the additional evidence
when its admission mode includes the R6.RECON.2 (d) scan in the ambiguity check
on runs that admit a post-freeze reconciliation record. The rule depends on the
admission mode, even if the particular run has no optional `REV` or no drifted
path to reconcile through it. For such a check, count a durable record `S` in the
`M`-derived portion of `R*` if both conditions hold.

- Its eligible regular entry would be selected by R6.RECON.2 (d) if read in that
  scan under the same configuration and tool-landing and plan-directory exclusions.
  Apply the reconciliation-record selector to the historical entry, including
  the `oi-reconciliation/2` schema. File presence in the broader category-3
  detector alone is insufficient.
- Its exact `{path, blob_sha256}` differs from `U`'s. It names the same exact `P`
  in `supersedes` and qualifies as a competing successor of that kind, schema and
  lineage under R6.REC.7. An independent review or admission of `S` is unnecessary
  where the live R6.RECON.2 (d) scan itself would have counted it. Count an exact
  reference once across its witnesses.

The additional evidence tests ambiguity only on the already operative edge.
It is FAIL `record-invalid` for the cited discharge, leaving the finding blocked
under R6.RECON.27. Use this check even if a subsequent run omits optional `REV`
while the same discharge edge and its immutable inputs remain operative. Since
it is based on exact eligible witnesses in `M`'s ancestry, it does not require
proving that a previous run observed `S`. A qualified sibling already in the
protected history can therefore matter on the first use of the edge. If an old `REV` was the only source
of `S` and never became reachable from `M`, changing or omitting `REV` can
still lose that evidence (R-1). An unreadable object that the required ancestry
walk needs still gives ERROR.

Qualification uses the configuration and admitted lineage inputs under which the
competing successor is found. Section 2.2 governs its retention and clearance across
later runs. A repair used solely through the entry lookup at `M` has no new lineage
check from that lookup. A previously qualified witness can still constrain that
repair if the lookup later becomes its only route. These checks add no positive
review, predecessor, lineage anchor or admitted record.

**R6.OBL29.4 Presence-based discharge conditions stay on current content.** Some conditions enable a
discharge only by the presence of evidence. These are read where r5 reads them, because a removal
can only make them fail. They are the repair's commits on `M`'s first-parent chain, the repair's current reconciliation
record entry and accepting non-author review in the scanned set at `M`, and the cited
reassessment and its accepting review through the existing pin and resolution rules
(R6.RECON.27 and R6.RECON.33). Historical acceptance cannot substitute for those inputs.

**R6.OBL29.5 A fixed selector for category 3.** Finding detection and its cumulative evidence
lookups do not exclude an entry because it is under a tool-landing prefix or its blob is
pinned by that class. Tree selection uses the fixed prefix `verification/audits/`, the
regular mode and the file's bytes. The location rule for particular cited reviews in
R6.OBL29.3 still applies. R6.RECON.2 (d) and (e) retain the existing admission selector.
The ordinary malformed-nonfinding check at `M` retains its tool-landing exclusion, unless
the file is explicitly read under another input rule. A finding under that prefix binds
if applicable. An unclassified side change still gives REVIEW_REQUIRED
`side-change-unclassified` under R6.TREE.5.

**R6.OBL29.6 Removal is never a discharge.** Deletion, rewriting, moving, renaming,
changing mode, replacing with a non-regular entry, prepending or truncating bytes, merge resolution
and supersession do not discharge a finding. A finding in `R*` that binds a configuration
continues to bind until a discharge under R6.RECON.26 and R6.RECON.27 applies. Either the
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
`present_at_M` is true exactly when the effective `M` tree holds the finding's original
path and blob SHA-256 at an eligible regular mode (100644 or 100755). A same-path symlink
or gitlink does not qualify, even if its entry names the same object id. `witness` is the
full id of a commit whose tree has the same eligible entry, chosen deterministically from
`M`, `REV`, `F`, then the newest on `M`'s first-parent chain, then the smallest full id
among the other commits that supply it, including verified sources of explicit record
inputs. Skip any candidate without an eligible regular entry. A predicted `M` uses its
computed object id when it is the witness.
A finding that binds and lacks an applying discharge appears in `blocked` with FAIL
`retirement-blocked`, whether or not it is present at `M`. A finding that a discharge lifts appears with the applying reassessment, or with no
blocked element when the configuration carries none of its edits. No new outcome class is
introduced.

**R6.OBL29.9 Status of the blocker.** OBL-29 is discharged only when the remedy is adopted by a
recorded owner decision, implemented in the tool revision, and independently verified, with the
controls of CONTROLS.json holding under the gate (sec. 16 of r6). Procedural guards do not
discharge it.

### 2.2 Retention and clearance across freezes

**Original qualification.** Retain an adverse review or competing successor only
if R6.OBL29.3 qualifies it for an existing discharge check. A retained witness names
the original
configuration and freeze by exact reference and verified commit, the applicable
mode and selector, the proposed reassessment and original finding reference and
item, the exact repair record and entry path, the repair commits, the exact
operative edge `U → P` where applicable, the exact adverse review or competing
successor `S`, and the full Git objects and admitted inputs needed to re-establish
the relationship. Include the exact
`M`/source tree and, if qualification depends on it, the exact `REV` and its
admission evidence. For a lineage witness, check that the original positive route
made the edge operative, and that the adverse review or `S` met the original
eligibility, location and exact-reference conditions. The existence of an eligible
pair in history alone gives no witness for a frozen discharge that never made the
lineage check operative. No earlier execution
verdict is required when qualification is independently reproducible from the
original inputs and authorized scope.

**Same disputed repair.** The negative evidence follows use of the same repair
basis. The match holds if the proposed discharge relies on the same reconciliation
blob and entry path, including a byte-identical copy elsewhere, on the same exact
disputed edge, or on an entry for the same repair path supported by an overlapping
set of exact repair commits. Preserve the original path-plus-blob references
for lookup and audit. A freeze id, selector, pin, review root, new record id or
different spelling of a reference is never a clearance key. When the candidate
still seeks to discharge the original finding for that repair path but uses
different identities, the independent verification must establish a substantive
replacement basis or resolve the retained witness. Changing every identifier supplies
no such verification. The rule does not attach a dispute to unrelated repair
entries on the strength of a matching schema, lineage label or shared path alone.
Any correction or adjudication has only its independently verified scope.

**Custody and lookup.** Discover the applicable witnesses and their subsequent
dispositions from verified custody reachable from protected `main`, starting at
effective `M`. Verify completeness for the discharge from an independently verified starting
inventory and the retained sequence of authorized freezes, operative repair inputs,
original witness sources and later dispositions. Each successor inventory carries
all earlier evidence and accounts for each newly authorized context relevant to
the disputed basis.
Use the historic configuration and its original selector to check each older
witness. A current run's list of positive inputs may omit an old pin or `REV`
but cannot serve as the list of negative witnesses. Before returning an applying
discharge, verify the custody starting point and coverage for the repair under
consideration. An empty result from incomplete custody gives no evidence that
there was no dispute. Missing required custody or unresolved eligibility leaves
the cited discharge inapplicable (FAIL `record-invalid` and `retirement-blocked`);
a required unreadable or unverifiable Git object still gives ERROR. Custody
preserves original bytes, paths, objects, lineage, authorization provenance and
the entire sequence of reviews, corrections and adjudications. It supplies evidence
for verification and no positive repair authority. The custody format, bootstrap
record and mapping to admitted inputs must be fixed and independently verified
before implementation may rely on them.

**Substantive clearance.** A retained witness keeps the same disputed basis
inapplicable until every applicable witness is accounted for through one of these
routes.

1. **Independently verified corrected evidence.** Preserve the witness and identify
   the exact defect and previous and replacement evidence. Verify under the
   applicable existing record route either that the original witness was
   objectively inapplicable in its original context, or that a replacement repair
   has an independently established unambiguous basis that no longer relies on the
   disputed evidence. In the second case check the actual repair, current entry,
   reviews and lineage of the replacement, with a new freeze where required.
   A deletion, new selector, missing pin or assertion that the conflict was fixed
   supplies no correction.
2. **Properly authorized and independently reviewed adjudication.** Retain both
   successor references, their predecessor, the affected repair entry and original
   finding, and all source and subsequent decision records. The adjudication must
   state and substantiate why the evidence supports a particular disposition for
   this disputed basis, and its effect on each witness in scope. Verify the
   authorization and the review under the approved evidence route and require any
   freeze that route calls for. The technical reviewer independently re-derives
   the grounds from the retained evidence and is independent of the disputed and
   corrective authors. An approval, withdrawal or rehearing decision alone
   provides no substantive resolution. Missing or contradictory effective
   dispositions keep the affected witness unresolved.

A clearance addresses only the exact lineage objection within its verified scope.
Other live lineage conflicts and independent admission checks continue to apply.
If the old conflict still appears in a live check, a policy permitting use of that
same disputed edge would need to say how the live check recognizes the clearance
for the exact witness. An applying reassessment is still required wherever
R6.RECON.26–.27 require one, including its ordinary positive review, current repair
evidence, applicable commits and freeze. This paper specifies the conditions of
a usable adjudication and creates no admitted record kind, override or tool input
for it. If the required authority or its inspectable admission route is absent,
the dispute remains unresolved. The same rule applies on repeated runs with the
same frozen inputs. A plan with none of the bound edits uses the existing
R6.RECON.26 route.

### 2.3 Persistence under ancestry extension

Let `M` be an ancestor of a later `M'` under P-1. If `c` is reachable from `M`, it is also
reachable from `M'`. The tree entries of `c` remain the same, and the fixed selector identifies
the same candidate finding evidence. A missing or corrupt required object produces ERROR.
Consequently the `M`-derived part of `R*` is monotone. Changing `F` or `REV` cannot erase
a witness reachable from `M`. Evidence known only through those additional roots or explicit
inputs has a narrower guarantee while it has no witness reachable from `M` (R-1).

For a fixed configuration, a side-change id that was reachable from `M` remains reachable
from `M'`, including if it stops being on the first-parent chain. Removing current files
cannot erase a finding, an exact reviewed reference used by Form (i), Form (iv) or Keys,
or an eligible review constraining a discharge, including a required review of any
predecessor under the existing lineage check, if that evidence has a durable witness
in `M`'s ancestry. With the same immutable lineage inputs and operative edge,
a qualifying competing successor stays in the additional negative set even if
the live `REV` changes or is omitted. A later freeze that still uses the same
disputed repair must consult the verified custody under §2.2. Changing the selector
or dropping an operative pin leaves original qualification intact. Removing evidence required at
`M` can cause a discharge to fail. The original form, independence and scope rules still
determine whether the persistent evidence establishes a binding finding. For example,
establishing a reviewer's lack of independence can disqualify it. That is a determination
from the evidence, not a consequence of removing it.

A first-parent-only walk needs preservation of `M` on every later first-parent chain. A
foxtrot fast-forward can put `M` on a merge's second-parent path without breaking ancestry
(P-FOXTROT). The same graph can move the finding's applicable side-change commit off the
first-parent chain (N-FOXTROT-SIDE-COMMIT). All-parent selection and applicability preserve
both under the weaker P-1 (§5.6).

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
| deletion of a dissenting review of a reassessment, its repair record or an operative predecessor | R6.OBL29.3 preserves the review failure without changing the lineage anchor |
| deletion of a qualifying sibling successor visible through a post-freeze scan | the durable witness still conflicts on the same already-operative discharge edge, including on a run that omits optional `REV` |
| re-freeze covering the old sibling path with a tool-landing exclusion or dropping the operative repair pin | the original qualification is reproduced from verified custody for the same disputed repair (§2.2) |
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
  the new freeze. A reassessment naming a rewritten blob that does not carry the original
  finding cannot lift the original. A reference and item naming no finding in `R*` fail
  R6.RECON.27 (FAIL `record-invalid`).
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

### 5.1 Resolution validity and the adopted baseline

R6.RECON.23 tests whether a resolution to a landing-trial finding or a carried site still
applies at the landing. OBL-29 preserves the category-3 finding and the evidence needed to
test its discharge. The r7 resolution-route table and its later refinements in r13 leave
the category-3 detection and reassessment model in R6.RECON.26–.27 in place. The r13
`resolution_validity` field describes a failure to keep a matched trial resolution or
carried site under R6.RECON.23. R6.OBL29.8 adds fields only within `category3.findings`.
The same output requirement and schema document both kinds of data. Amendment 6 r13
adds exact retained-result and fixture-input checks in R6.RECON.36 and RECON-ENUM.
Those reconciled-state placement controls stay in force. Section 32 still requires
implementation and independent verification of the OBL-29 remedy to discharge
the blocker. This paper proposes that remedy separately from the adopted contract.

### 5.2 Reassessment and migration records

A reassessment resolves its finding from `R*`, reads the repair entry at `M` and counts
historical reviews for the discharge, including operative predecessor reviews
(R6.OBL29.3–.4). Its keys, item ids, positive review and freeze citation retain their
existing requirements. REASSESS-FORM and REASSESS-KEYS keep their schema cases.
An edit-id migration remains a pinned match route under R6.RECON.28.

Consider an applying reassessment `A` citing repair `Q`, where `Q` supersedes `P`.
Initially the direct reviews of `A` and `Q` and the required review of `P` all accept.
If `Q` already undergoes an operative lineage check for this discharge, an eligible
dissent of `P` that lands on `main` makes that check fail. Removing the dissent from the
next tree leaves it in `R*`, so the same check still prevents the discharge. The same
rule applies along `A`'s own required predecessor chain. If the repair lookup is the
only use of `Q`, there is no operative lineage check on `P` through that lookup.
The direct `Q` review condition still applies and retains any eligible dissent of `Q`.

The same discharge can fail for a different reason. Keep `A`, pinned `Q`, `P` and
their accepting reviews fixed. Land an eligible sibling `S → P` on `main`. An
unrelated valid record read from `REV1` makes the mutable scan visible to R6.REC.7.
The scan sees `S` and rejects the existing `Q → P` edge as ambiguous. Delete `S`
and rebuild the unrelated valid `REV2` on the later `M`. The old live-scan check
could now pass. Under the proposed rule, the earlier `main` tree still witnesses
`S` for that edge. The conflict therefore still prevents the discharge. `Q` itself
is not admitted through the unrelated `REV`. If a later freeze keeps `Q` but
excludes `S`'s path or removes `Q`'s configuration pin, look up the qualified
witness under the original freeze and continue to reject that disputed basis
until a substantive clearance is verified.

The current reference-and-item rule requires a reassessment for each distinct finding
reference created by a rename or rewrite. A byte-identical rename still creates a second
reference. Section 5.6 gives the alternative and its consequences.

### 5.3 The tool-landing prefix

R6.OBL29.5 removes the tool-landing prefix exclusion for category-3 detection and evidence
lookups. Record admission in R6.RECON.2 (d) and (e), and ordinary current malformed-nonfinding
lint, retain the existing exclusion. P-TL-CLEAN specifies the category-3 check over all of `R*` for the predicted-`M` run, including history
and the tool's own landing paths. P-TL-MALFORMED-NONFINDING checks the distinction in the
current tree. A genuine finding follows the usual binding and
discharge rules.

R6.EVID.8 and its runners distinguish reads from the representative candidate and the
declared comparison inputs from the category-3 record scan. The first group continues
to satisfy `scanned_paths_within` over the existing ledgered, corpus, `H..M` and
drifted-candidate scope. For the category-3 scan, record the source commit or predicted
step, path and blob and verify that each tree-derived record read comes from a named
R6.OBL29.1 root or its verified history, under `verification/audits/`. An explicitly
read record must be traceable to its admitted input and verified source. Reading a
candidate path as part of its original representative comparison cannot make it part of
the category-3 scan. Both checks are required for a representative op C control. The record-source check covers verified reads even when a
record contributes no finding to the result.

### 5.4 Dissent outside category-3 discharge

R6.OBL29.3 covers direct discharge records and the review dependencies of any
lineage check already required for their use. Other records can have the same
deletion vulnerability when their lint reads only snapshots. Proposed R6.OBL29.10
would extend historical review lint to those other records. The competing-successor
addition is limited to operative discharge edges and the mutable reconciliation
scan. Full lineage admission for repairs selected solely from `M`, or extending
historical ambiguity to unrelated lineages or admission generally, would require a
separate decision. Other R6.RECON.2 and R6.REC.7 checks use their existing inputs.

**R6.OBL29.10 (scope option)** Extend R6.OBL29.3's historical sources for R6.REC.6 review
lint to records outside category-3 discharge when those records undergo that lint.

### 5.5 Requirements affected on adoption

The table records the proposed changes relative to r5 and cross-checks them against the
same requirement locations in adopted r13. They would need a separate amendment on OBL-29 adoption.

| Requirement | Proposed effect |
|---|---|
| R6.RECON.26 | Use `R*` for detection and for each "the scan finds" predicate in Forms (i) and (iv). State that the original finding remains as reachable evidence after a legitimate removal. Preserve the independence, lineage and edit predicates. Define "contains" for the exact side-change commit id as reachability through any verified parent. |
| R6.RECON.27 | Look up the finding in `R*` and evaluate Keys (a)–(b) and the Form (iv) basis there. Keep the reassessment lineage check, preserve current repair entry, positive review and first-parent predicates, and apply R6.OBL29.3 to reviews and competing-successor evidence and require verified custody and clearance under §2.2. |
| R6.RECON.33 | Change its last reference-resolution sentence. The finding comes from `R*`; the repair entry remains in the scan at `M`. The record-kind table and existing resolution anchors retain their scope. |
| R6.RECON.35 | Use the fixed category-3 selector and the historical diagnostic rule. Preserve the existing tool-landing exclusion for ordinary current malformed-nonfinding lint and the same-directory reconciliation-review requirement. |
| R6.REC.6 | Apply review lint using the eligible exact-reference reviews in `R*` of either direct discharge record and of predecessors in existing operative lineage checks. Defective reviews remain material after deletion. Extend historical review sources to other records only if the owner chooses R6.OBL29.10. |
| R6.REC.7 | Preserve existing lineage anchors and positive inputs. Carry eligible predecessor reviews and the scoped negative evidence of competing successors into an operative discharge check under R6.OBL29.3. A repair lookup alone does not trigger lineage admission. Retained original qualification still applies when the same disputed basis is reused. |
| R6.REC.17 | Add the verified all-parent walk to parentless commits as an exception to the explicit-endpoint rule. Verify retained custody objects without substituting them for the run’s ordinary admission anchors. |
| R6.RECON.36, R6.OUT.18 and the result schema | Add `present_at_M` and `witness` within each `category3.findings` element. Both require a regular entry of the exact reference. The r13 requirement to retain and independently check RECON-ENUM placement evidence remains in force. |
| R6.EVID.8 and N10, N11, RT-L2, RT-O9-L2 | Keep `scanned_paths_within` for the existing representative comparison and add a separately verified category-3 read domain tied to the prescribed roots and input records (§5.3). Update those expectation rows and runners on adoption. |
| REASSESS-FORM | Change the missing-finding case to absence of the cited reference and item from `R*`. A valid historical witness suffices for this lookup. Preserve the current repair-entry and review conditions. |
| OBL-29 (§32) | Record the expanded removal and predicate scope, the remaining coverage gaps, and the adopted, implemented and independently verified remedy required by R6.OBL29.9. The existing r13 discharge text and the earlier r7 wording are compatible with that condition. |

R6.RECON.2 (d) and (e), R6.RECON.23, R6.RECON.28, R6.CFG.1–.8 and R6.TREE.5 can retain
their text. R6.TREE.5's classification check and the category-3 detection check can both
apply to the same file. The inventory names the affected control predicates and fixture
wording. RECON-BLOCK still fails when a later run's `REV` omits an already landed finding.
GV5's positive shallow-store case runs `terms` with all its required objects. Each op C
run with `M` needs every object required by the ancestry scan, so that shallow success does
not generalize to op C. Recheck existing op C fixture completeness and the expanded result
schema at any later implementation. CONTROLS.json specifies new expectations and carries
no runners.

### 5.6 Decisions before adoption

| Decision | Alternatives and consequences | Review and owner position |
|---|---|---|
| Ancestry walk | All parents require ordinary ancestry extension and scan more commits. A first-parent walk requires first-parent preservation and would lose the foxtrot witness, even with ordinary ancestry extension. | The reviewer preferred the weaker ancestry premise. The owner prefers all parents subject to independent verification. R6.OBL29.1 uses it for this draft. |
| Reachability after squash, rebase or a `REV` change | An ancestry-preserving landing retains exact witness commits. A verified replay would need to retain each exact reference and item, the referenced records and reviews used by Forms, Keys and historical lint, and the applicable side-change ids. Equal end trees cannot establish this. An explicit retained-evidence record could address a missing witness with new admission and verification rules. Extending the land-at-once procedure to all obligation and discharge evidence before another run could reduce exposure, but would need a way to establish completeness. | The owner requires demonstrable equivalent custody and lineage before squash/rebase risk could be accepted. Section 6 describes the remaining gap. No specific equivalence mechanism or risk acceptance is authorized here. |
| Mistaken independent finding | Current Keys requires a repair and applying reassessment, or a plan that no longer binds. This can exclude otherwise sound work across all matching lineages. A narrowly extended `repair: null` route could require an independently reviewed adjudication attached to the original finding and a new freeze, reusing the reassessment flow. A dedicated adjudication record could carry the original reference and `item`, review, evidence and scope explicitly, with a larger schema and admission change. | The r2 reviewer favored a narrow D3 extension with independent adjudication and a new freeze. The owner favors controlled adjudication and asks that it be investigated. Both routes remain proposals. |
| R6.REC.6 outside discharge checks | Use historical review evidence for discharge and its existing predecessor dependencies, or extend it to unrelated records under R6.OBL29.10. The latter prevents analogous deletion bypasses and changes unrelated admission outcomes. | The reviewer treated the discharge case as a correctness defect and the broader case as a scope choice. |
| R6.REC.7 scope | Qualify competition under the original approved configuration and retain it for the same disputed repair across later runs or freezes. Preserve existing lineage routes, anchors and positive authority. | The owner requires durable eligibility for a qualified witness against the same repair. Full lineage admission for a repair selected solely from `M` and general historical ambiguity checks remain separate choices. |
| Resolving a retained lineage conflict | The proposed clearance routes require independently verified corrected evidence or properly authorized and independently reviewed substantive adjudication. Both preserve the original witness and full decision history. | The owner set the clearance policy. Approval of the exact design and of any new adjudication admission mechanism is separate. |
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
- **P-2. Persistence requires durable witnesses for all relevant evidence.** This includes
  the original finding and item, the exact record and entry looked up by Form (i), Form (iv)
  or Keys, the reviews needed to establish or constrain a discharge at direct records or operative
  predecessors, competing successors of operative edges and the exact side-change commit ids. R6.RECON.26 directs landing a finding on `main` by its own
  commit before a subsequent retirement landing run. That direction does not ensure that
  all those related inputs, including dissent which carries no finding, acquire witnesses
  reachable from `main`. For positive discharge inputs, durable history is supplemental to
  the current and pinned requirements. Equivalence across a squash or rebase would have
  to preserve and independently replay the original qualification context, exact reference
  and applicability, each operative edge and the complete clearance history (§2.2).
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
B-REBASE-SIDE-COMMIT isolates this in a synthetic topic graph. A replay omitting or
changing an entry can also lose the exact reference or a required associated review. Similarly,
an abandoned or force-pushed `REV`, an unmerged branch, a tag-only witness or an uncommitted
finding can escape subsequent runs. The absence of a finding in those runs does not
establish that no earlier run saw it. If an old `REV` was the only source of an
eligible review, reviewed reference or competing successor, a later history
walk alone can miss it. Dropping optional `REV` cannot erase a witness already
durably retained. If custody of a relevant prior scope cannot be established,
§2.2 leaves discharge inapplicable. An earlier accepted result or a new freeze
cannot substitute for the missing history. The existing land-at-once procedure addresses only the
finding itself. Acceptance of the squash/rebase gap and any additional safeguard
remain open.

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
  paper control calls for a fresh independent check at the current exact base. It remains unverified.
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
| Amendment 6 r13 at `5ad8837521de0a26734266a64f91548fd3dcff1e` and #1593 comment 7193277489 | adopted tool contract and OBL-29 blocker | source off `main`, design adoption recorded, integration pending |
| #1169 comment 7191104852 | the authority, quoted in §0 | provenance, quoted with author and time |
| #1169 comment 7191665350 | bounded r2 direction and open owner decisions | provenance, owner and time in §0 |
| #1601 comment 7191637164 and r1 at `0b06363c8dbb3d2c7e95a6ca7ab22cdc8cc7d234` | independent REVISE, reviewed scope and earlier scan | provenance for the reported observations and review |
| #1601 r2 at `1a067396370ecbd36acd1c35aec79c674de4f8e3` and its independent REVISE (comment 7192414933) | r3 review inputs | provenance for the correction scope |
| #1601 r3 at `36d9071cac29075e2b57db11a17031760dbfd836` and its independent REVISE (comment 7192615596) | r4 lineage correction | provenance for the correction scope |
| #1601 r4 at `dd1ca3bc40ffe822928986bba9b8a5d67e8a91b9` and its focused REVISE (comment 7192760996) | r5 mutable-scan correction | provenance for the correction scope |
| #1601 r5 at `c11e8d4aa82aa46f0557513d476c6fd5e4f03576` and #1601 comment 7192888727 | accepted same-freeze correction and re-freeze bypasses | provenance for the correction scope |
| #1169 comment 7193274406 | r6 owner policy and scope | provenance, author and time quoted in §0 |
| repository ruleset 21725642 (guardrail) | host permits merge, squash and rebase, and requires PRs and rejects non-fast-forward updates on the covered default branch | host configuration at the time of the comparison |
| #1169 comments 7185092393 and 7185562871 | the lifecycle tables behind requirement (I) | support off `main`; quoted in r5 sec. 0.4 and 0.5 on the amendment branches |
| Issue #1598 and comment 7191083365; PR #1593 comments 7189446310, 7190255132, 7190966287 | the defect statement and its wider scope | provenance |
| `main` at `942bd5ea1fd09f4223012b0755bce2d6da07c44a` | current governance snapshot, including AGENTS.md §A.52 items 5 and 6 | support on `main` |
