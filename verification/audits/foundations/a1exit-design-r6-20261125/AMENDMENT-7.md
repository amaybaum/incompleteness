# r6 amendment 7: change record (adopted)

Owner directions: amaybaum, 2026-11-27T01:59:03Z (#1169 comment 7207734407), the closing paragraph: "Preserve all outstanding obligations identified in the preceding review, including the symlink failures, representative-snapshot runner and r13 binding gaps", and item 5: "Malformed findings shall produce run-level `FAIL retirement-blocked`, preserving evidence and provenance. Reserve `ERROR` for cases where reliable evaluation is impossible."; amaybaum, 2026-11-27T02:01:22Z (#1169 comment 7207765697): "A1 retirement remains the highest current operational priority", with item 4: "Do not expand the verification infrastructure beyond the adopted requirements unless a concrete retirement-blocking defect is demonstrated."

Source of the gaps: the independent review of the r13 detection, form and binding rewrite on #1577 (comment 7202940328), finding 6:

> An entry with `side_change_commits: []` never binds; r13's R6.RECON.30 table admits an empty array.
> An element that is readable but names an edit id absent from every ledger binds nothing.

Status: adopted at r4 (`fbfeac8ae3a7914255e07d9a0351eff4bd1d1474`), with every-configuration binding for an unresolvable configuration, by owner decision recorded at #1169 comment 7208869709; landed by PR #1618, whose only change after adoption disambiguates six section headings and records this status. r2 answers the independent review of r1 (`f5d85874`) on PR #1618, findings 3, 4, 5, 7, 8 and 9. r3 answers the re-review of r2 on PR #1618: the witness used by the ancestry test of gap (i), and a nit in REASSESS-KEYS C3. r4 applies the two nits of the r3 confirmation on PR #1618: the qualifying witness in sec. 2, and a witness on a predicted `M`'s in-memory chain. This file is the only file it changes. DESIGN-r6.md, EXPECTATIONS.json, REQUIREMENTS.json and CONFORMANCE-MUTANTS.json are unchanged. On adoption, a generator-amendment7 applies the adopted wording and cases, as generator-amendment1 to generator-amendment6 did. It authorizes no merge, dispatch, freeze or trial, and it reopens nothing else of amendments 1 to 6.

Order of adoption: the wording uses three terms of the OBL-29 r9 design and its Amendment 1 (#1601 at `e79e7ca90f863115bc75b7ae5195dbba016125da`, `verification/audits/foundations/a1exit-obl29-remedy-20261126/`): `R*` (R6.OBL29.3), residual R-1 and residual R-8. That design landed on `main` by PR #1601. This amendment is adopted with or after r9 Amendment 1, and its wording is aligned with A1.5. If it were adopted first, `R*` would read as r13's "the scan", and the R-1 sentence would be dropped.

Goal link: the A1 retirement verification route (#1169, owner priority of comment 7207765697). This proposal decides whether a recorded category-3 finding blocks fail-closed in two cases where r13 lets it bind nothing. Item 4's bar is met: sec. 1 shows from r13's own text on `main` that both cases fail open. A finding that binds nothing lets a frozen plan proceed over an invalidation that an independent reviewer recorded.

Safety rule, as in amendment 6: no reading may let a category-3 finding be lost or lifted by rewording, and no rule is weakened to match the tool. Each change below adds blocked runs or bindings. The one change to a lift condition, in R6.RECON.27 Keys, permits an edit reassessment where Keys forbade one only because r13 never bound an edit and a run level together. No binding or lift condition that r13 states becomes easier to meet (sec. 3).

## 1. The gaps in r13's text

The demonstration rests on DESIGN-r6.md on `main`. The tool and a probe confirm it; they are provenance, listed in sec. 6.

**Gap (i).**
- The R6.RECON.30 entry table types `side_change_commits` as an "array of commit ids", so an empty array passes it.
- The array's acceptance condition is RC1, which only decides reconciliation.
- R6.RECON.26 limits blocking to "every run whose `M` contains one of the entry's `side_change_commits`". No `M` contains an element of `[]`.
- Neither text constrains the elements beyond their encoding. A held commit that no relevant `M` can contain therefore also leaves the finding unbound, for example a commit on an abandoned branch or one made after the record.
- The list is written by the reconciliation record's writer, the side a second-kind finding disputes.
- For a finding that names no entry, the sentence presupposes an entry and says nothing.

**Gap (ii).**
- Form (ii) makes an element whose `id` is absent from the named configuration's ledger a form failure that "blocks through the fallback of (iii)".
- (iii) binds "every configuration whose ledger carries one of its edits", by id, migrated id or target.
- An id that no ledger carries, with a target that no ledger holds, therefore binds no configuration.
- Form (iv)'s run-level case requires the fallback set to be empty, and that set is reached only when `invalidated` is "absent, empty or unreadable". A readable element with an unknown id never reaches it.
- An unresolvable `configuration` reaches (iii)'s scope through the same path, with the same result.

The tool at `7db52f38` follows this text faithfully. Its behaviour, quoted from the provenance in sec. 6:
- gap (i): no `retirement-blocked` item; for a malformed element, `record-invalid` only while the record is present;
- gap (ii): `bind` returns `([], False, form)`, so `record-invalid` while present and nothing after deletion.

## 2. Gap (i): an empty or untrustworthy `side_change_commits`

### Options, gap (i)

- (a) A form failure: make `side_change_commits` a non-empty array in the R6.RECON.30 key table.
  - This alone closes nothing. A form failure "still blocks" (Form (i)), but only through the same gate, which an empty list never meets.
  - It also changes RECON-FIELDS countercase 2 (`base-drift` with RC1 would become `record-invalid` before any condition) and the mutant list, whose sha256 is cited in RECON-SCHEMA.
- (b) Binding at run scope: where the list cannot limit the finding's runs, the finding blocks every run in which it is found. This is fail-closed whatever the list holds, and it leaves the key table, RC1 and the mutant list unchanged.

### Proposal, gap (i)

(b). The list limits the runs only when each element passes three tests:
- it is a commit id naming a commit the object store holds;
- that commit changes the entry's path against its first parent, as RC1 and drift define it (R6.RECON.30), merges included;
- that commit is an ancestor of, or equal to, a witness of the record carrying the entry (a commit whose tree holds that record at its path with its blob). Where the record has a witness in `M`'s ancestry, the witness must be one of those. Only a record with no witness in `M`'s ancestry may use a witness reached through `F`, `REV` or an explicit input, with the narrower guarantee of r9 R-1.

Consequence: a finding whose record is in `M`'s history always blocks the run. Each element that passes is an ancestor of a witness in `M`'s ancestry, so `M` contains it. Any other list blocks at run scope. A witness on another branch, such as an `F` cut from an abandoned branch, cannot unblock a record that `M` carries. For a predicted `M` (R6.TREE.15, R6.RECON.21), a witness found only on the in-memory chain from `M0` counts as in `M`'s ancestry for this test, but it is not durable until that chain lands on `main`, as r9 Amendment 1 states for `R*_M`: "For a predicted `M` (R6.TREE.15, R6.RECON.21), only `M0`'s ancestry is durable, so a record seen only on the in-memory chain from `M0` gains a durable witness, and the permanence below takes effect, when that chain lands on `main`."

The third test closes the residual in review finding 3: an abandoned-branch commit, or a commit made after the record, is not an ancestor of any qualifying witness (in `M`'s ancestry where the record has one). A legitimate entry passes all three tests. RC1 makes the list exactly the commits on `M`'s first-parent chain after `H` that change the path, and a record lands after those commits, so each is an ancestor of the commit that lands it.

Otherwise the finding blocks every run in which it is found, and the list is a form failure of the finding, so that the writer sees `record-invalid`. The key table is not changed.

A finding with no record in `R*` blocks in the same way, with the run-level item of Form (iv). Owner item 5 and r9 Amendment 1 A1.3 have already decided its outcome: FAIL `record-invalid` and `retirement-blocked`, never ERROR. The replacement states that outcome. It does not decide it again.

### Replacement wording (R6.RECON.26, body)

Current:

> A finding found there blocks every run whose `M` contains one of the entry's `side_change_commits`, with an item FAIL `retirement-blocked` (obligation `RET`): the entry's path takes the disposition `retirement-blocked` when it differs between `H` and `M`; when it does not (for example after a revert to `H`'s bytes), the item is a run-level item naming the path.

Replacement:

> A finding found there blocks every run whose `M` contains one of the entry's `side_change_commits`, with an item FAIL `retirement-blocked` (obligation `RET`): the entry's path takes the disposition `retirement-blocked` when it differs between `H` and `M`; when it does not (for example after a revert to `H`'s bytes), the item is a run-level item naming the path. The entry's `side_change_commits` limit the runs a finding blocks only when they are a non-empty array each of whose elements is a commit id (R6.RECON.29) naming a commit the object store holds, that changes the entry's path against its first parent as R6.RECON.30 defines it (a merge commit included), and that is an ancestor of, or equal to, a witness of the record carrying the entry (a commit whose tree holds that record at its path with its blob): a witness in `M`'s ancestry where the record has one, and otherwise a witness in `R*` (R6.OBL29.3) reached through `F`, `REV` or an explicit input, with the narrower guarantee of r9 R-1; for a predicted `M` (R6.TREE.15, R6.RECON.21), a witness found only on the in-memory chain from `M0` counts as in `M`'s ancestry for this test but is not durable (r9 Amendment 1, `R*_M`); a finding whose record is in `M`'s history therefore blocks every run whose `M` holds it. Where the list is absent, is not an array, is empty or holds any other element, the finding blocks every run in which it is found, as if that run's `M` contained one of the listed commits, and the list is a form failure of the finding, FAIL `record-invalid` (Form (i)). A finding that names no entry (a malformed finding of R6.RECON.35, or a review whose `reviewed` names no record in `R*`, R6.OBL29.3) likewise blocks every run in which it is found, with the run-level item of Form (iv). A finding found only through `REV`, `F` or an explicit input blocks with the narrower guarantee of r9 R-1.

The configurations the finding binds are unchanged: Form (ii) to (v) decide them, as before. Only the set of runs changes.

### Controls (new cases; FINDING-FORM, R6.RECON.26)

Each FAIL case below has no `retirement-blocked` item under r13's text.

| # | Case | Outcome |
|---|---|---|
| 1 | a first-kind finding with a well-formed `invalidated` element and a resolvable configuration of the run's lineage, whose entry has `side_change_commits: []` | FAIL, `retirement-blocked` and `record-invalid` |
| 2 | the same, the record deleted by a later commit on `M` (historical only) | FAIL, `retirement-blocked` |
| 3 | the same, the list holding one well-formed commit id that the object store does not hold | FAIL, `retirement-blocked` and `record-invalid` |
| 4 | the same, the list holding one commit the store holds that does not change the entry's path | FAIL, `retirement-blocked` and `record-invalid` |
| 5 | the same, the list holding one commit that changes the path but is not in the run's `M`, plus one element `"junk"` | FAIL, `retirement-blocked` and `record-invalid` |
| 6 | a second-kind finding (independent reviewer, `invalidates` on `<path>:scientific_effect`) on an entry whose `side_change_commits` is `[]` | FAIL, `retirement-blocked` and `record-invalid` |
| 7 | a class (b) malformed file with an invalidation signal (for example the BOM-prefixed copy of a finding) | FAIL, run-level `retirement-blocked`; no ERROR |
| 8 | the list holding, as its only element, a held commit on an unmerged branch that changes the entry's path, not an ancestor of any witness of the record (an abandoned branch) | FAIL, `retirement-blocked` and `record-invalid` |
| 9 | the list holding, as its only element, a merge commit whose tree entry for the path equals its first parent's (the path differs only from the second parent) | FAIL, `retirement-blocked` and `record-invalid` |
| 8b | case 8's list, the record squash-landed on `M` (its witness in `M`'s ancestry does not descend from the listed commit), and `F` on the abandoned branch, so that a witness reached through `F` descends from the listed commit | FAIL, `retirement-blocked` and `record-invalid` |
| 10 | provisional, with r9 Amendment 1: a second-kind finding by a reviewer distinct from every author in `R*`, whose `reviewed` names no record in `R*` | FAIL, run-level `retirement-blocked` and `record-invalid`; no ERROR |
| C1 | countercase: a well-formed finding whose record has no witness in the run's `M` ancestry and is found through `REV`, whose `side_change_commits` lists only commits that change the path, are ancestors of that witness, and are not contained in the run's `M` (the run's `M` predates the change) (positive) | ANY, not `retirement-blocked` |
| C2 | countercase: a `no-effect` entry, not a finding, with `side_change_commits: []` on a mode-only change | FAIL, `base-drift`, RC1 failing; not `retirement-blocked`, not `record-invalid` (RECON-FIELDS countercase 2, unchanged) |
| C3 | countercase: C1 (the record found through `REV` only) with its only element a merge commit that brings the change in (its tree entry for the path differs from its first parent's), an ancestor of the witness, not in the run's `M` (positive) | ANY, not `retirement-blocked` |

How the cases tell the readings apart:
- C1 rules out a fix that drops the `M` scope altogether. C2 shows that the key table and RC1 are unchanged.
- Case 5 separates the proposal from r13, where the one valid commit not in `M` leaves the finding unbound.
- Case 8 separates the ancestry test from a path-change test alone. Case 8b shows that a witness through `F` cannot stand in for the record's witness in `M`'s ancestry.
- Cases 9 and C3 pin the first-parent definition for a merge.

### Effect on existing controls, gap (i)

- Design controls: none changes its expectation.
  - RECON-FIELDS countercase 2 is unchanged, because the key table is unchanged and the entry is not a finding.
  - RECON-SCHEMA and CONFORMANCE-MUTANTS.json are unchanged.
  - RECON-BLOCK, BLOCK-KEY, FINDING-FORM, FINDING-LINEAGE and FINDING-KEYS use findings whose lists name the commits that changed the path before the record landed, so their outcomes are unchanged.
  - The SCAN-PARSE malformed-finding cases ("run level") now have a stated run scope.
- Tool controls (branch, not design): N-PREPEND changes from ERROR `DESIGN_UNSETTLED` to FAIL run-level `retirement-blocked`. That is the change owner item 5 already requires. The stop at `cli.py:358-361` is removed for these cases.

## 3. Gap (ii): an element naming an edit the named configuration does not have

### Options, gap (ii)

- (a) The Form (iv) fallback: treat such an element as unreadable, so that it binds the edits the entry's `conclusions` name, or every edit of the entry's path.
  - Not proposed. `conclusions` is the writer's list, and a second-kind finding is the case where the reviewer disagrees with the writer.
  - A revised plan could proceed by removing the named edits while still carrying the one the reviewer meant.
- (b) Run-level binding of the lineage. It is lifted only by a new freeze that cites an applying, reviewed reassessment naming the finding with `edit` null (R6.RECON.27), the remedy Form (iv) already gives an empty fallback set.

### Proposal, gap (ii)

(b), keyed on the element's `id` alone. The element binds the lineage at run level when its `id` is missing, is not a string, or is not an edit id of the named configuration's edit list (a retained edit included). This holds whether or not its `target` matches, so a fabricated `target` cannot keep the finding below run level.

The run-level binding is added to the finding's other bindings and replaces none of them (review finding 4, option (A)). Each anchored element keeps binding its edit, and the matches of (iii) and (v) keep binding configurations outside the lineage. r1 replaced the edit bindings of a run-level-bound configuration. A null-`edit` reassessment pins no wording, so a later version could then reword an anchored edit and re-cite the same reassessment, which r13 does not allow.

R6.RECON.27 Keys needs one clause for this. Its "`edit` is null exactly when the named finding is bound at run level" assumes a finding never binds an edit and a run level together. Under the proposal a null reassessment lifts the run-level binding only, and each anchored edit still needs its own reassessment pinning its wording. This eases no lift condition: before the change no finding was both bound to an edit and bound at run level, and each binding keeps the remedy it had.

Where the configuration cannot be resolved, no element can be checked against a ledger. A run cannot tell a valid id that another configuration carries from one that no configuration carries. The fail-closed reading is therefore run-level binding of every configuration, the scope Form (iv) already gives an unresolvable configuration with an empty set. Its cost is stated below.

### Replacement wording

**R6.RECON.26, Form of a finding (iv): one sentence inserted.**

Current opening of (iv):

> (iv) *The edits a finding binds.* A finding binds the edits its `invalidated` elements name, by id and, where an element carries one, by target.

Replacement (the rest of (iv) is unchanged):

> (iv) *The edits a finding binds.* A finding binds the edits its `invalidated` elements name, by id and, where an element carries one, by target. A finding whose `configuration` is absent or cannot be resolved, or one of whose `invalidated` elements has an `id` that is missing, is not a string, or is not an edit id of the named configuration's edit list (R6.ADAPT.2 `edits`, a retained edit included), whatever its `target`, also binds at run level every configuration of its lineage, and every configuration when its `configuration` cannot be resolved, as an empty set does below; this binding is in addition to the edits its other elements name and to the matches of (iii) and (v).

**R6.RECON.26, Form (v): one clause added.**

Current sentence in (v):

> A configuration bound only by an id collision (through the fallback of (iii), its edit of that id lying on another path) proceeds by a new freeze that renames the colliding id, through an AGENTS.md sec. A.48 item 3 migration where records cite it;

Replacement:

> A configuration bound only by an id collision (through the fallback of (iii), its edit of that id lying on another path, and not bound at run level under (iv)) proceeds by a new freeze that renames the colliding id, through an AGENTS.md sec. A.48 item 3 migration where records cite it;

**R6.RECON.27, Keys: one sentence replaced.**

Current:

> `edit` is null exactly when the named finding is bound at run level (R6.RECON.26, Form of a finding (iv)).

Replacement:

> `edit` is null only when the named finding binds the citing configuration at run level (R6.RECON.26, Form of a finding (iv)); a reassessment with `edit` null lifts that run-level binding only, and each edit the finding also binds in that configuration is lifted only by a reassessment that names the finding and that edit.

The body sentence of R6.RECON.27 ("unless it is null for a finding bound at run level (Keys, below)") reads with this and is unchanged.

### Controls (new cases; FINDING-KEYS for a resolvable configuration, FINDING-LINEAGE for an unresolvable one, REASSESS-KEYS for the lift)

Each FAIL case among 1 to 7 has no `retirement-blocked` item under r13's text.

| # | Row | Case | Outcome |
|---|---|---|---|
| 1 | FINDING-KEYS | an element `{id: "NO-SUCH-EDIT", sha256, target}`, its target's path and `old_sha256` held by no ledger, under a configuration that resolves to the run's configuration | FAIL, run-level `retirement-blocked` naming the finding, and `record-invalid` |
| 2 | FINDING-KEYS | the same, the record deleted by a later commit on `M` | FAIL, run-level `retirement-blocked` |
| 3 | FINDING-KEYS | the same, the run under a later version, on the named configuration's `supersedes` chain, that carries no edit of that id | FAIL, run-level `retirement-blocked` |
| 4 | FINDING-KEYS | a valid element naming edit `E1` and a second element with an unknown id | FAIL; `category3.blocked` holds an entry for `E1` and a run-level entry with `edit` null for the finding |
| 5 | FINDING-KEYS | a valid element and a second element that is an object without `id`, or whose `id` is a number | FAIL, run-level `retirement-blocked` and `record-invalid` |
| 6 | FINDING-KEYS | an element with an unknown id whose `target` matches an edit of the run's ledger by path and `old_sha256` | FAIL, run-level `retirement-blocked` (the target match does not keep it below run level) |
| 7 | FINDING-LINEAGE | an unknown-id element under a configuration that cannot be resolved, the run under a configuration of another retirement that carries neither the id nor the target | FAIL, run-level `retirement-blocked` and `record-invalid` |
| 8 | REASSESS-KEYS | case 4, then a new freeze that rewords `E1` (the same id and target) and cites an applying reassessment naming the finding with `edit` null | FAIL, `retirement-blocked` on `E1` |
| C1 | FINDING-KEYS | countercase: case 1's finding, the run under a configuration of another retirement outside the named configuration's lineage that carries neither the id nor the target (positive) | ANY, not `retirement-blocked` |
| C2 | FINDING-KEYS | countercase: case 1's finding, the configuration frozen anew citing an applying reassessment that names the finding with `edit` null (positive) | ANY, not `retirement-blocked` |
| C3 | REASSESS-KEYS | countercase: case 1's finding and an applying reassessment naming it with a non-null `edit` | FAIL, run-level `retirement-blocked` (an edit reassessment does not lift the run-level binding); the expected classes omit `record-invalid` by design, since under the amended Keys a non-null `edit` for an edit of the citing configuration is well formed and the reassessment applies, lifting nothing |
| C4 | REASSESS-KEYS | countercase: case 8's freeze also citing an applying reassessment naming the finding and `E1` as now worded (positive) | ANY, not `retirement-blocked` |

How the cases tell the readings apart:
- C1 rules out a fix that binds every configuration when the configuration resolves.
- C2 and C4 show the remedies work. C3 shows that the run-level binding needs the null reassessment.
- Case 8 shows that the null reassessment does not lift an anchored edit's binding, and so separates option (A) from r1's replacement reading.

### Effect on existing controls, gap (ii)

| Row, case | Effect |
|---|---|
| FINDING-KEYS case 3 (an id absent from the named configuration's ledger) | outcome and classes unchanged (FAIL; `retirement-blocked`, `record-invalid`); the case text gains "and binds the lineage at run level" |
| FINDING-KEYS cases 1, 2, 4, 5, 6 and countercase 7 | unchanged: each element's id is an edit id of the named configuration |
| FINDING-LINEAGE case 5 (a finding naming no configuration) | outcome unchanged (FAIL); the case text gains "and every configuration at run level" |
| FINDING-LINEAGE case 6 | unchanged (FAIL) |
| FINDING-LINEAGE countercase 4, cases 1 to 3 and 7 | unchanged: the named configuration resolves and the element is anchored |
| FINDING-LINEAGE countercase 8 (the id-collision rename) | stays positive where the fallback comes from an element that differs from a resolvable configuration's ledger: the other retirement is outside the lineage and is bound only by the global id match. The case text is narrowed to "the finding naming a readable configuration with which an element differs". Where the fallback comes from an unresolvable configuration, the other retirement is bound at run level, and its remedy is a null reassessment naming the finding |
| REASSESS-KEYS "a reassessment with edit null for a finding bound to an edit (not at run level)" | unchanged (FAIL) |
| FINDING-FORM, RECON-BLOCK, BLOCK-KEY, REASSESS-FORM | unchanged: their elements are anchored and no finding binds at run level and to an edit together |
| Tool controls | the case for review finding 1 (`invalidated: ["junk"]`, present and then deleted) still blocks: through the `conclusions` edits, and in the lineage also at run level |

**Cost of the unresolvable-configuration reading, stated for the owner.** Binding every configuration is the only fail-closed reading. The carrier-only scope of r13 leaves an id that no ledger carries binding nothing, which is gap (ii) itself. Its cost:
- It is a denial-of-service surface. One second-kind review that names an unresolvable `configuration` blocks every retirement in the corpus at run level.
- Each affected plan needs a new freeze citing a reassessment naming the finding with `edit` null. Where the reviewer appears independent, that reassessment needs a `repair` on `main` (R6.RECON.27 Keys), which an unrelated retirement may have no way to supply.
- Independence is not established by the records. Reviewer and author identities are self-declared strings (r9 R-8), so anyone able to land a file under `verification/audits/` can write a review that appears independent.
- That such a finding already fails its form does not reduce this cost.

A narrower anchor was considered and is not proposed: fall back to the reviewed entry's own `scientific_effect.configuration`. That configuration is chosen by the record's writer, the side the finding disputes, so the fallback would let the writer steer the finding's scope.

## 4. Requirements and rows touched on adoption

- R6.RECON.26: the body sentence (sec. 2), Form (iv) and Form (v) (sec. 3).
- R6.RECON.27: one Keys sentence (sec. 3).
- No other requirement changes. R6.RECON.30 and the key tables of sec. 23.1 are unchanged.
- EXPECTATIONS.json:
  - FINDING-FORM: cases 1 to 10, 8b and C1 to C3 of sec. 2;
  - FINDING-KEYS: cases 1 to 6, C1 and C2 of sec. 3, and the case 3 text;
  - FINDING-LINEAGE: case 7 of sec. 3, and the case 5 and countercase 8 text;
  - REASSESS-KEYS: case 8, C3 and C4 of sec. 3.
  - No outcome of an existing case changes.
- REQUIREMENTS.json: the amendment-7 mark on R6.RECON.26 and R6.RECON.27, with no control removed.
- CONFORMANCE-MUTANTS.json: unchanged.

## 5. Tool changes implied (not made here)

- `engine/cli.py:356-363`:
  - replace the ERROR stop and the `in_m` gate by the scope test of sec. 2: held commits, each changing the path against its first parent, each an ancestor of a witness of the record in `M`'s ancestry where one exists, and otherwise of a witness in `R*`;
  - when every element passes, `applies = in_m(...)`;
  - otherwise `applies = True`, with the form problem "side_change_commits does not scope the finding (R6.RECON.26)";
  - a finding with no readable entry binds at run level (owner item 5).
- `engine/category3.py`, `bind`: return the run-level flag `True`, together with the edits otherwise bound, when the configuration is unresolved, or when it resolves, the run's configuration is in the lineage, and some element's `id` is missing, not a string, or absent from `_edits(fled)`.
- `engine/category3.py`, `reassessment_problems`: drop the check "edit is not null for a finding bound at run level" and keep its converse; `lifting` already lifts per `(finding, edit)`, with `None` for the run-level binding.
- Runners for the new FINDING-FORM, FINDING-KEYS, FINDING-LINEAGE and REASSESS-KEYS cases.

## 6. References (AGENTS.md sec. A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| DESIGN-r6.md on `main` (R6.RECON.26 to .30) | the demonstration of sec. 1 and the current wording quoted | support on `main` |
| #1169 comments 7207734407 and 7207765697 | the owner directions, quoted with author and time | owner record, quoted here |
| #1577 comment 7202940328, finding 6 | the source of the two gaps | provenance |
| PR #1618, the review of r1 at `f5d85874` | the findings r2 answers | provenance |
| r9 design and Amendment 1, #1601 at `e79e7ca90f863115bc75b7ae5195dbba016125da` (A1.3, A1.5, R6.OBL29.3, R-1, R-8) | the terms `R*`, R-1 and R-8 and the no-entry outcome the wording aligns with | support off `main`, closed by the order of adoption stated above |
| tools/a1-ledger-coverage-r6 at `7db52f380f1e51d4af52b84f0a7e728827ac5a60`: `engine/cli.py:356-363`, `:415`; `engine/category3.py:114-121` (`in_m`), `:705-798` (`bind`), `:309-313` | the tool behaviour quoted in sec. 1 and the tool changes of sec. 5 | provenance |
| a probe importing the engine from a `git archive` of `7db52f38`, run in a session scratchpad and not committed (AGENTS.md sec. A.28) | confirmation of the tool behaviour: `in_m` is `False` for `[]`, `["junk"]` and an unheld id; `bind` returns `([], False, form)` for an unknown id with a resolvable or an unresolvable configuration | provenance |
