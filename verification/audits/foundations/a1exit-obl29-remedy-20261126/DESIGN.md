# OBL-29 remedy: removal of a landed finding record (paper design)

## 0. Status, authority, scope and goal link

**Status.** Paper design. Not implemented, not reviewed, not adopted. It changes no requirement,
control expectation or tool behaviour in force, and it changes no text of amendment 6. Its
requirements (ids `R6.OBL29.n`) are proposals for the owner's decision after independent design
review. OBL-29 stays an explicit blocker on the A1 retirement execution until a remedy is
implemented and independently verified. Adopting this design does not discharge it, and neither do
the interim procedural guards (AGENTS.md sec. A.50 item 3, sec. A.46 item 6).

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

The same record frames the question: "Has a finding disappeared legitimately, or has its removal
bypassed an outstanding obligation?" Amendment 6 r5 answers a separate question: "Does a finding
that still exists retain a valid resolution?"

**Base text.** The design is written against design r6 as amended by amendments 1 to 6, at amendment
6 r5, commit `1f5764572a98b7ae2f306e121e2e410f79c29daf` (branch `design/a1-r6-amendment-6`,
directory `verification/audits/foundations/a1exit-design-r6-20261125/`). `main` at `9e52be1e` holds
design r6 as landed in round 6 only. Amendments 1 to 6 are not on `main`: they exist on the branches
`design/a1-r6-amendment-1` to `design/a1-r6-amendment-6`. Every requirement cited here (R6.RECON.26,
R6.RECON.27, R6.RECON.35, R6.REC.17 and others) is cited at its r5 text. The reference trace is in
sec. 7.

**Goal link (AGENTS.md sec. A.47).** The work serves A1 retirement (#1169) and its blocker OBL-29
(Issue #1598). It decides whether a design exists under which no change can make a landed
category-3 finding stop binding a plan unless a discharge the design defines lifts it, and what that
design requires of amendment 6. It decides no scientific question.

**Scope.** Category-3 findings (R6.RECON.26) and the predicates that decide their discharge. One
instance of the same failure outside category 3 is identified (sec. 5.4). It is left to the owner
whether that instance belongs to OBL-29.

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
- **Antitone predicates** (true when evidence is absent) that relax a discharge. Removing evidence
  makes them true, so a discharge becomes easier. r5 has two. R6.RECON.27 Keys (b) allows
  `repair: null` for a review whose `reviewed` "names no record the scan finds". Keys (a) allows
  `repair: null` for a first-kind finding whose entry's non-author review rejects, "only where no
  independent reviewer asserts the invalidation". Deleting the reconciliation record that an
  independent review names, or deleting an accepting review, turns a finding that needs a repair
  into one that does not.
- **The selector.** `Det` depends on the tool-landing class of the configuration's side-change class
  record. A later configuration, frozen anew, can widen a tool-landing prefix, or pin a blob, so
  that it covers a finding's path. That takes the finding out of detection without touching it.

This one statement accounts for every case listed in OBL-29 and #1598. It also shows that the
failure is not limited to post-`F` changes. A finding that lands after `H` and is removed before
`F` is in none of `S(M)`, `S(F)` and `S(REV)`. A post-freeze record admitted through `REV` that
reaches `main` by a merge whose resolution drops it was seen by one run and is lost to every later
run that names a different `REV`.

### 1.4 What a removal can change

The decision's inputs are: the set of commits that the run's role commits reach; the object store;
the detection function; and the discharge records the configuration pins. A change that "removes a
finding" must alter at least one of these. It cannot alter commits that are already reachable,
because they are immutable. So it must make some of them unreachable (a history rewrite), lose
objects, change the detection function, or change what is evaluated over the current tree. The
remedy therefore reads the reachable history instead of the current tree. It fixes the selector,
and it fails closed on lost objects. A history rewrite is the residual left to the host (sec. 6).
The proof is in sec. 2.3. The taxonomy in sec. 2.4 is a consequence of it, not its basis.

***

## 2. The remedy

### 2.1 Requirements

**R6.OBL29.1 The cumulative record set.** For a run, let the role commits be `M`, `F`, `REV` (when
named), `X` and `C`, and `M0` together with the in-memory chain to the predicted `M` (R6.TREE.15)
on a predicted run. `R*` is the set of regular-file entries `(path, blob)` (mode `100644` or
`100755`) under `verification/audits/` in the tree of any commit reachable, through any parent, from
a role commit, together with the records the run reads. An entry's identity is its reference
`{path, blob_sha256}` (R6.RECON.29): mode is not part of it, and a byte-identical blob at two paths
gives two entries. `R*` is a set, so its content does not depend on traversal order.

**R6.OBL29.2 Detection over `R*`.** Category-3 detection (R6.RECON.26, R6.RECON.35) applies the
classes of R6.RECON.35 to every entry of `R*`. The run's findings are the union. Everything else
about a finding is unchanged: its identity (reference and `item`, R6.RECON.27 Keys), its form rules
(R6.RECON.26 (i) to (vi)), and its binding, lineage and global matches. A finding carried by an
entry that is not in `M`'s tree binds exactly as one that is. No absence of an entry from `M`, `F`
or `REV`, and no later state of its path, takes a finding out of the run.

**R6.OBL29.3 Absence-based predicates read `R*`.** A predicate qualifies here if two things hold. It
lifts, narrows or relaxes a block or a discharge condition. And it can become true when an entry is
removed. Every such predicate is evaluated over `R*`, never over a single tree. In r5 these are:
- R6.RECON.26 Form of a finding (i): "a review whose `reviewed` names no record the scan finds". It
  decides whether the review's independence is evaluated, and through that whether Keys (b)
  applies;
- R6.RECON.27 Keys (a) and (b): eligibility for `repair: null`, including "no independent reviewer
  asserts the invalidation", with every review record in `R*` that names the record's reference
  counted.

An absence-based predicate that only widens a block is left as r5 states it, because a removal that
makes it true makes the run stricter. Form of a finding (iv), "the finding names no entry the scan
finds", is one: it binds at run level. For the same set of findings to be both bound and
dischargeable, R6.RECON.27's condition "the named finding is a finding the scan of R6.RECON.26
finds" reads the findings of `R*`, and a reassessment's `finding` is resolved from `R*`.

**R6.OBL29.4 Presence-based discharge conditions stay on current content.** Some conditions enable a
discharge only by the presence of evidence. These are read where r5 reads them, because a removal
can only make them fail. They are the repair's commits on `M`'s first-parent chain, the repair's
reconciliation record entry in `M`'s tree with an accepting non-author review, and the reassessment
pinned by the citing configuration (R6.RECON.27). A discharge can never be read from `R*` alone.

**R6.OBL29.5 A fixed selector.** For category-3 detection, R6.RECON.35's selection excludes no entry
on the ground of the tool-landing class, whether by prefix or by pin. Selection depends only on the
fixed prefix `verification/audits/`, the regular mode and the entry's bytes. The scanned set of
R6.RECON.2 (d) and (e), which governs which reconciliation records apply, keeps its exclusions
unchanged. A file under a tool-landing prefix that carries a finding binds. R6.TREE.5 still reports
it REVIEW_REQUIRED `side-change-unclassified` when it is unpinned.

**R6.OBL29.6 Removal is never a discharge.** No change to the repository lifts a finding in `R*`:
not a deletion, rewrite, move, rename, mode change, replacement by a non-regular entry, prepended or
truncated bytes, a merge resolution, or supersession. A finding in `R*` binds a configuration until
one of the discharges of R6.RECON.26 applies to it, as R6.RECON.27 defines them. Either the
configuration carries no edit the finding binds, or the configuration's freeze cites an applying
reassessment that names the finding's reference and `item`. Each is evaluated with
R6.OBL29.3 and R6.OBL29.4. Missing, unresolvable or non-applying discharge evidence leaves the
block standing.

**R6.OBL29.7 The ancestry walk.** `R*` is computed by one walk through the verified reader
(R6.REC.17). It starts at the role commits, visits each commit reachable through its parsed parents
once (keyed by full id), and ends when no unvisited parent remains, which happens at parentless
commits. It reads parents only from verified commit content. Refs, reflogs, replace refs, grafts,
the `shallow` file and commit-graph files are never consulted. A commit, tree or blob that the walk
needs and that is missing or does not hash to its id is an unresolvable object: ERROR, and no
verdict. A parent absent from a shallow store is one such case. There is no count or depth limit,
so no finding sits beyond a bound. The walk is linear in the number of reachable commits.
*Equivalent computation (informative).* `R*` equals the root commits' full entry sets, together with,
for each other reachable commit, the entries of its tree that differ from its first parent's tree.
Each entry of a reachable tree is either present in the first parent's tree, which is itself
visited, or new relative to it. Because selection depends only on the entry (R6.OBL29.5), a per-entry
detection cache keyed by `(path, blob)` is exact.

**R6.OBL29.8 Result fields.** Each element of `category3.findings` (R6.RECON.36) gains two fields.
`present_at_M` is a boolean that says whether `M`'s tree holds the finding's reference. `witness` is
the full id of one commit whose tree holds it, chosen deterministically: `M` if present, else
`REV`, else `F`, else the first commit on `M`'s first-parent chain going back from `M`, else the
smallest id among the reachable commits that hold it. A finding with `present_at_M` false that no
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

### 2.3 Why it covers every removal

*Claim.* Assume host protection of `main` (P-1, sec. 6), a complete object store, and an unchanged
detection function. Let `e = (p, b)` be a regular entry under `verification/audits/` in the tree of
a commit `c` that a role commit of a run reaches, and let `φ = Det(e)`. Then `φ` is among the run's
findings and binds until a discharge lifts it, whatever commits follow `c`.

*Argument.* `e ∈ R*` by R6.OBL29.1. `Det(e)` depends only on `p`'s prefix, the regular mode and `b`'s
bytes (R6.OBL29.5), and none of these depends on any later commit. A later commit cannot alter `c`,
its tree or `b`, since objects are immutable and the reader verifies them. It cannot make `c`
unreachable from `M` once `c` is an ancestor of the `main` commit taken as `M`: for every later `M'`
on `main`, `M` is an ancestor of `M'` by P-1. A missing object stops the run with ERROR
(R6.OBL29.7). Therefore `φ` is detected, and by R6.OBL29.6 it binds until a discharge applies. The
antitone predicates of R6.OBL29.3 are evaluated over `R*`, which by the same argument never loses an
entry. So no removal makes them true. The presence-based conditions of R6.OBL29.4 can only fail when
content is removed.

*Monotonicity.* Under P-1, if `M` is an ancestor of `M'`, then every entry reachable from `M` is
reachable from `M'`. The findings that `main`'s history carries therefore never decrease along
`main`, and requirement (I) holds.

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
| removal by a merge resolution, through either parent | the parent that held it is reachable |
| add and remove within a branch that is then merged | the intermediate commit is reachable |
| a post-freeze record seen in one run's `REV`, dropped when `REV` is merged | `REV` is reachable once merged |
| supersession by a later record | R6.RECON.26 already: supersession never clears; with R6.OBL29.6 the old record need not stay |
| removal before `F` | the walk does not depend on `F`; the entry is reachable from `M` |
| deletion of the record that a second-kind review names (to reach Keys (b)) | R6.OBL29.3: the record is found in `R*` |
| deletion of an accepting review of a first-kind entry (to reach Keys (a)) | R6.OBL29.3: the accepting review is in `R*` |
| owner-approved evidence removal (AGENTS.md sec. A.46 item 6, sec. A.50 item 3) | R6.OBL29.6: removal is not a discharge; sec. A.46 item 6 keeps the original reachable |
| history rewrite of `main` (force-push) | not covered: residual R-2, relies on P-1 |
| a finding that was never committed, or only to a commit no role commit reaches | not a removal: residual R-1 |

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
- *A finding by an independent reviewer that later proves mistaken.* Under r5 Keys it needs a repair,
  or a revised plan without the edit. Deleting the file was the interim route (AMENDMENT-6.md,
  remarks on review finding 9). The remedy closes that route. Whether a recorded withdrawal by the
  same reviewer, or a further independent review that rejects the finding, should make `repair:
  null` admissible is an owner point (sec. 5.5). The remedy is correct without it and fails closed.

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
- **Cost.** One tree diff per reachable commit, restricted to `verification/audits/`, plus one
  detection per distinct entry. Deterministic and cacheable by object id (R6.REC.17, caching).

***

## 5. Interactions with amendment 6 r5 and the verification architecture

### 5.1 Amendment 6 r5 (R6.RECON.23, identity and validity)

R6.RECON.23 compares landing-trial findings (op D and postconditions) at the landing and at `X`, and
it decides whether a matched finding keeps its resolution. That is a different object, the term
finding of the reconciled-state trial, and a different question. The remedy does not change
R6.RECON.23. The two remedies apply one principle to two layers. Identity and validity are separate:
- For a category-3 finding, identity is its reference and `item`, and it persists in `R*`.
- Validity of a lift is the applying discharge.
- A file's presence is neither.

R6.RECON.23's resolving records (context adjudications, HP adjudications, hit classifications, allow
rules) are pinned at `F` by reference and resolved by the history search of R6.RECON.33. Their
removal from `main` already changes nothing. The remedy gives findings the same footing.

### 5.2 Reassessment and migration records

- Reassessment (R6.RECON.27): the finding is resolved from `R*`, and the repair entry from `M`
  (R6.OBL29.3, R6.OBL29.4). Keys (a) and (b) eligibility is read over `R*`. With that change, the
  reassessment schema, its item ids and its review are unchanged (REASSESS-FORM, REASSESS-KEYS keep
  their cases).
- Migration (R6.RECON.28): pinned by the configuration, resolved by reference, and it only adds
  edits. The remedy does not touch it.
- Rename burden. One reassessment lifts only the finding it names. A finding file that is renamed
  or rewritten in place therefore leaves one finding per distinct reference in `R*`, and each needs
  its reassessment. This follows from R6.RECON.35's identity rule ("two byte-identical files at two
  paths are two records"). It adds work, never a bypass (sec. 5.5).

### 5.3 The tool-landing prefix

r5 excludes tool-landing prefixes from detection, which is a selector that a later freeze can widen.
R6.OBL29.5 removes the exclusion for detection only. The scanned set of R6.RECON.2 (d) and (e)
keeps it. Consequence: the tool's own landing paths under `verification/audits/` must carry nothing
that R6.RECON.35 classes as a finding, or every run would block. Control P-TL-CLEAN checks this on
the actual tool-landing tree before the tool lands. The existing residual, an unpinned finding under
a tool-landing prefix that was visible but not blocking, also closes.

### 5.4 The same failure outside category 3

R6.REC.6 fails a record when "a second review whose verdict on any item is not `accept`" names it,
reading the records the run reads and the scanned sets. That is evidence against the record, and the
rule is antitone: deleting a rejecting review lets the record apply. This is the failure of
sec. 1.3, but the evidence is a rejection, not a category-3 finding. The remedy would cover it by
reading that clause over `R*` (proposed R6.OBL29.10 below). The owner decides whether it belongs to
OBL-29 or to a separate obligation. Uniqueness rules are different. "Exactly one review record" in
R6.RECON.2 (d), one record per path in (e), and ambiguous ancestry in R6.REC.7 are antitone, but
they are rules of determinism, not evidence against a record. The record that survives a removal
still passes every condition RC1-RC14 from git objects. They are left unchanged.

**R6.OBL29.10 (proposed; scope for the owner)** R6.REC.6's second-review clause counts every review
record in `R*` that names the record's reference.

### 5.5 Requirements of amendment 6 r5 that would change

No text of amendment 6 is changed here. On adoption of this remedy, these r5 requirements would need
amending (each change is the minimal one):

| Requirement | Change |
|---|---|
| R6.RECON.26 | the scan sources ("Every run scans `M`'s tree, … `F`'s tree and … `REV`'s tree") become `R*` (R6.OBL29.1, R6.OBL29.2); Form of a finding (i): "names no record the scan finds" reads over `R*` (R6.OBL29.3); (iv) unchanged |
| R6.RECON.27 | the named finding and its resolution: from `R*`, not "at the run's `M`"; Keys (a), (b): read over `R*`; repair conditions unchanged (R6.OBL29.4) |
| R6.RECON.35 | selection: no tool-landing exclusion for detection (R6.OBL29.5); the paragraphs "Removal after `F`" and "Tool-landing prefixes" are replaced by references to R6.OBL29 |
| R6.REC.17 | "Every walk runs between explicit commits, except …" gains the ancestry walk of R6.OBL29.7, which terminates at parentless commits |
| R6.RECON.36 and R6.OUT.18 | `category3.findings` elements gain `present_at_M` and `witness` (R6.OBL29.8); the result's JSON Schema follows |
| OBL-29 (sec. 32) | the statement is narrower than the failure: it also covers removal before `F`, removal of a reviewed record or an accepting review that relaxes Keys, a selector widening, and a `REV` dropped at merge; discharge as R6.OBL29.9 |
| R6.REC.6 | only if the owner extends the scope (R6.OBL29.10) |

Unchanged: R6.RECON.2 (d) and (e), R6.RECON.23, R6.RECON.28, R6.RECON.33, R6.CFG.1 to R6.CFG.8 (no
new configuration field), and the text of R6.TREE.5 (its REVIEW_REQUIRED still applies; a finding
there now also blocks). No existing expectation row of EXPECTATIONS.json at `1f576457` changes. The
check run was a search for cases expecting a finding under a tool-landing prefix not to block, or a
removed finding not to block, and there are none. RECON-BLOCK's case "a later run naming a `REV`
whose tree omits it" keeps its FAIL. The controls of CONTROLS.json would become new expectation rows
(`runner: null` until implemented) naming the R6.OBL29 requirements, under the correspondence check
of sec. 16.

**Points for the owner.**
1. *Ancestry or first-parent.* `R*` reads every reachable commit, so findings that were committed in a
   merged branch and removed before its merge bind, and so do findings in a merged `REV`. A
   first-parent-only `R*` is cheaper and matches "landed on `main`" literally. It would miss the
   merged-`REV` drop and the in-branch add-and-remove (controls N-REV-DROP, N-BRANCH-DRAFT). The
   design proposes ancestry.
2. *Mistaken independent findings.* With deletion closed, a well-formed second-kind finding by an
   independent reviewer is lifted only by a repair with reassessment, or by removing the edit from
   the plan. Whether a recorded withdrawal by that reviewer, or a rejecting further independent
   review, should admit `repair: null` is a change to R6.RECON.27 Keys (amendment 6 D3), not to this
   remedy.
3. *R6.REC.6* (sec. 5.4): inside or outside OBL-29.
4. *Rename burden* (sec. 5.2): accepted as is, or a reassessment may name every reference of one
   blob. The latter is a change to R6.RECON.27, not proposed here.

***

## 6. Assumptions, posits and residual risks

**Assumptions the remedy relies on.**
- **P-1. `main` is append-only.** Commits reachable from `main` are not removed by force-push or
  branch deletion. Host branch protection enforces this, not the tool. The tool sees the actual
  parents of `M` and cannot tell a rewritten history from an honest one.
- **P-2. Findings are committed.** A finding binds only once it is in a commit that a role commit
  reaches. R6.RECON.26's rule to land a finding at once by its own commit, and the review process,
  ensure this. The tool cannot find a category-3 change by itself (R6.RECON.26).
- **P-3. A complete object store.** The native clones are full (R6.REC.17). A missing object fails
  closed, so this posit affects availability, not correctness.
- **P-4. Detection is not narrowed by a tool revision.** A later tool revision with a narrower `Det`
  would remove findings from every run. This rests on R6.STAT.5 (no check weakened) and on the
  review of the tool revision. SCAN-PARSE and the CONTROLS.json fixtures pin the detection cases.
- **P-5. Git object ids are collision resistant**, as R6.REC.17 already assumes.

**Residual risks.**
- **R-1.** A finding never committed, or committed only on a branch that no role commit reaches,
  including a branch rewritten before merge. This is not a removal of a landed finding. It is the
  existing residual that category 3 rests on the review (control B-UNREACHABLE).
- **R-2.** A rewrite of `main`'s history that drops a commit carrying a finding. Not detectable by
  the tool; it relies on P-1 (control B-MAIN-REWRITE).
- **R-3. Permanent false positives.** Any entry that R6.RECON.35 ever classed as a finding binds
  until it is reassessed, including a fixture or data file that landed by mistake. The cost is work,
  not a bypass. A cheap scan of the 81 first-parent commits visible in a shallow clone of `main` at
  `9e52be1e` found no historical entry under `verification/audits/` that both begins a JSON value
  and contains `invalidates` or `invalidated` beside a record schema string. This is not a full-
  history result, and the review brief asks for it on a full clone.
- **R-4. Rename burden** (sec. 5.2).
- **R-5. Cost** grows linearly with the repository's history.
- **R-6.** R6.REC.6's rejection clause stays antitone unless R6.OBL29.10 is adopted.

***

## 7. Reference trace (AGENTS.md sec. A.42 item 8)

| Reference | Use | Classification |
|---|---|---|
| commit `1f5764572a98b7ae2f306e121e2e410f79c29daf` (branch `design/a1-r6-amendment-6`): DESIGN-r6.md, EXPECTATIONS.json, REQUIREMENTS.json, AMENDMENT-6.md | the requirement texts this design amends and cites | support off `main`: the base text is not on `main`; this design lands nothing and is valid only relative to that text |
| #1169 comment 7191104852 | the authority, quoted in sec. 0 | provenance; quoted with author and time |
| #1169 comments 7185092393 and 7185562871 | the lifecycle tables behind requirement (I) | support off `main`; quoted in r5 sec. 0.4 and 0.5 on the amendment branches |
| Issue #1598 and comment 7191083365; PR #1593 comments 7189446310, 7190255132, 7190966287 | the defect statement and its wider scope | provenance |
| `main` at `9e52be1e` | the state of `main` stated in sec. 0 | support on `main` |
