# r6 amendment 7: change record (proposal)

Owner directions: amaybaum, 2026-11-27T01:59:03Z (#1169 comment 7207734407), the closing paragraph: "Preserve all outstanding obligations identified in the preceding review, including the symlink failures, representative-snapshot runner and r13 binding gaps", and item 5: "Malformed findings shall produce run-level `FAIL retirement-blocked`, preserving evidence and provenance. Reserve `ERROR` for cases where reliable evaluation is impossible."; amaybaum, 2026-11-27T02:01:22Z (#1169 comment 7207765697): "A1 retirement remains the highest current operational priority", with item 4: "Do not expand the verification infrastructure beyond the adopted requirements unless a concrete retirement-blocking defect is demonstrated."

Source of the gaps: the independent review of the r13 detection, form and binding rewrite on #1577 (comment 7202940328), finding 6:

> An entry with `side_change_commits: []` never binds; r13's R6.RECON.30 table admits an empty array.
> An element that is readable but names an edit id absent from every ledger binds nothing.

Status: a proposal for owner disposition. It needs independent review and the owner's decision. This file is the only file it changes. DESIGN-r6.md, EXPECTATIONS.json, REQUIREMENTS.json and CONFORMANCE-MUTANTS.json are unchanged. On adoption, a generator-amendment7 applies the adopted wording and cases, as generator-amendment1 to generator-amendment6 did. It authorizes no merge, dispatch, freeze or trial, and it reopens nothing else of amendments 1 to 6.

Goal link: the A1 retirement verification route (#1169, owner priority of comment 7207765697). This proposal decides whether a recorded category-3 finding blocks fail-closed in two cases where r13 lets it bind nothing. Item 4's bar is met: section 1 shows that both cases fail open in the tool at `7db52f38`, and a finding that binds nothing lets a frozen plan proceed over an invalidation that an independent reviewer recorded.

Safety rule, as in amendment 6: no reading may let a category-3 finding be lost or lifted by rewording, and no rule is weakened to match the tool. Both gaps are closed by binding more, never less.

## 1. How the tool treats each case at `7db52f38`

The evidence is the code on branch tools/a1-ledger-coverage-r6 at `7db52f380f1e51d4af52b84f0a7e728827ac5a60`. A probe that imports the engine from a `git archive` of that commit confirms the reading (recipe in sec. 6).

**Gap (i): `side_change_commits`.**

- `engine/cli.py:356-363` reads the entry. If the entry is not an object, or `side_change_commits` is not a list, the run stops with ERROR `DESIGN_UNSETTLED` (fail-closed). This is the stop the review calls stop 1, and it covers malformed findings and reviews whose reviewed record is absent.
- Otherwise `applies = c3.in_m(repo, M, entry['side_change_commits'])`. `engine/category3.py:114-121` returns `False` for an empty list. It also returns `False` for any element that is not a string or that the object store does not hold, because the exception is caught and the element is skipped.
- When `applies` is false, `bind` is never called. The finding then has no edits, no run-level binding, and only the form problems it had before binding.
- Probe results: `in_m([])`, `in_m(["junk"])` and `in_m([<40-hex id not in the store>])` are each `False`, and `in_m([<commit in M>])` is `True`.
- Effect:
  - With `[]`, which passes the R6.RECON.30 key table (`('arr', 'commit')`), the run emits no item for the finding at all.
  - With a malformed element, the schema form failure gives FAIL `record-invalid` only while the record is present at `M` (`cli.py:415`, `form and (present or hits)`), and never `retirement-blocked`.
  - With a well-formed id that names no commit, or a commit unrelated to the path that no run's `M` contains, the finding binds nothing and the record passes its schema.
  - A deleted record leaves no trace in any of these cases.

**Gap (ii): an element naming an unknown edit id.**

- `engine/category3.py:705-798` (`bind`): an element that passes `element_ok` but whose `id` is absent from the named configuration's ledger adds the form problem "differs from the named configuration's ledger" and sets `global_scope` (`:743-749`).
- `carry_id` (`:752-757`) then fails, because the id is not in the run's ledger either. The target match (`:765-775`) fails when no splice or retained edit of the run's ledger has the target's path and `old_sha256`.
- `bind` returns `([], False, form)` at `:776`, so the result has no edits and no run-level binding.
- The same holds when the configuration cannot be resolved: `unresolved` sets `global_scope`, but the usable-list path never reaches the run-level return at `:798`.
- Probe results:
  - unknown id with a resolvable configuration: `([], False, ["invalidated element NO-SUCH-EDIT differs from the named configuration's ledger (Form (ii))"])`;
  - unknown id with an unresolvable configuration: `([], False, ['its configuration is absent or cannot be resolved (Form (iii))'])`;
  - controls: a valid element gives `(['E1'], False, [])`, and `invalidated: ["junk"]` (review finding 1, fixed at `7db52f38`) gives `(['E1'], False, [...Form (iv) fallback])`.
- Effect: the run shows FAIL `record-invalid` while the record is present, and never `retirement-blocked`. After the record is deleted it shows nothing.

In both cases the tool follows the r13 text faithfully. The holes are in the design, as the review states.

## 2. Gap (i): an empty or untrustworthy `side_change_commits`

### Options

- (a) A form failure: make `side_change_commits` a non-empty array in the R6.RECON.30 key table.
  - This alone closes nothing. Form (i) says a form failure "still blocks", but the block still passes through the same gate, "every run whose `M` contains one of the entry's `side_change_commits`", which an empty list never meets.
  - It also changes two existing controls:
    - RECON-FIELDS countercase 2 (the mode-only change with `side_change_commits` empty) would become `record-invalid` before any condition, instead of `base-drift` with RC1 failing, because the RECON-SCHEMA conformance invariant forbids failed conditions on a schema-invalid record;
    - CONFORMANCE-MUTANTS.json would gain an `empty-array` mutant, which changes its sha256, cited in RECON-SCHEMA and in amendment 6 sec. 6a.
- (b) Binding at run scope: where the list cannot scope the finding, the finding blocks every run in which it is found. This is fail-closed whatever the list holds. It leaves the key table, RC1 and the mutant list unchanged.

### Proposal

(b), with the untrustworthy list also counted as a form failure of the finding, so that the writer sees `record-invalid`. The key table is not changed.

"Untrustworthy" covers:
- an empty list;
- an element that is not a commit id;
- an id that names no commit;
- a commit that does not change the entry's path.

The last two are included because they fail open in the same way as `[]`. A legitimate entry is never affected: RC1 makes the list exactly the commits on `M`'s first-parent chain after `H` that change the path, so each element names a held commit that changes it.

The same sentence must also say what happens to a finding with no entry, because the r13 sentence presupposes one. Owner item 5 has decided that case: run-level FAIL `retirement-blocked`, not ERROR. The replacement states that decision. It does not decide it again.

### Replacement wording (R6.RECON.26, body)

Current:

> A finding found there blocks every run whose `M` contains one of the entry's `side_change_commits`, with an item FAIL `retirement-blocked` (obligation `RET`): the entry's path takes the disposition `retirement-blocked` when it differs between `H` and `M`; when it does not (for example after a revert to `H`'s bytes), the item is a run-level item naming the path.

Replacement:

> A finding found there blocks every run whose `M` contains one of the entry's `side_change_commits`, with an item FAIL `retirement-blocked` (obligation `RET`): the entry's path takes the disposition `retirement-blocked` when it differs between `H` and `M`; when it does not (for example after a revert to `H`'s bytes), the item is a run-level item naming the path. The entry's `side_change_commits` limit the runs a finding blocks only when they are a non-empty array each of whose elements is a commit id (R6.RECON.29) naming a commit the object store holds that changes the entry's path (R6.RECON.30). Where the list is absent, is not an array, is empty or holds any other element, the finding blocks every run in which it is found, as if that run's `M` contained one of the listed commits, and the list is a form failure of the finding, FAIL `record-invalid` (Form (i)). A finding that names no entry the scan finds (a malformed finding of R6.RECON.35, or a review whose `reviewed` names no record the scan finds) likewise blocks every run in which it is found, with the run-level item of Form (iv).

The configurations the finding binds are unchanged: Form (ii) to (v) decide them, as before. Only the set of runs changes.

### Controls (new cases; FINDING-FORM, R6.RECON.26)

Each FAIL case below fails at `7db52f38` without the change: no `retirement-blocked` item is emitted, or, for the no-entry case, the run stops with ERROR.

| # | Case | Outcome |
|---|---|---|
| 1 | a first-kind finding with a well-formed `invalidated` element and a resolvable configuration of the run's lineage, whose entry has `side_change_commits: []` | FAIL, `retirement-blocked` and `record-invalid` |
| 2 | the same, the record deleted by a later commit on `M` (historical only) | FAIL, `retirement-blocked` |
| 3 | the same, the list holding one well-formed commit id that the object store does not hold | FAIL, `retirement-blocked` and `record-invalid` |
| 4 | the same, the list holding one commit the store holds that does not change the entry's path | FAIL, `retirement-blocked` and `record-invalid` |
| 5 | the same, the list holding one commit that changes the path but is not in the run's `M`, plus one element `"junk"` | FAIL, `retirement-blocked` and `record-invalid` |
| 6 | a second-kind finding (independent reviewer, `invalidates` on `<path>:scientific_effect`) on an entry whose `side_change_commits` is `[]` | FAIL, `retirement-blocked` and `record-invalid` |
| 7 | a class (b) malformed file with an invalidation signal (for example the BOM-prefixed copy of a finding) | FAIL, run-level `retirement-blocked`; no ERROR |
| C1 | countercase: a well-formed finding whose `side_change_commits` lists only commits that change the path and that the run's `M` does not contain (the run's `M` predates the change) (positive) | ANY, not `retirement-blocked` |
| C2 | countercase: a `no-effect` entry, not a finding, with `side_change_commits: []` on a mode-only change | FAIL, `base-drift`, RC1 failing; not `retirement-blocked`, not `record-invalid` (RECON-FIELDS countercase 2, unchanged) |

C1 rules out a fix that drops the `M` scope altogether. C2 shows that the key table and RC1 are unchanged. Case 5 tells the two readings apart: under r13, the one valid commit not in `M` leaves the finding unbound.

### Effect on existing controls

- Design controls: none changes its expectation.
  - RECON-FIELDS countercase 2 is unchanged, because the key table is unchanged and the entry is not a finding.
  - RECON-SCHEMA and CONFORMANCE-MUTANTS.json are unchanged.
  - RECON-BLOCK, BLOCK-KEY, FINDING-FORM, FINDING-LINEAGE and FINDING-KEYS use findings whose lists name the commits that changed the path, so their outcomes are unchanged.
  - The SCAN-PARSE malformed-finding cases ("run level") now have a stated run scope.
- Tool controls (branch, not design): N-PREPEND changes from ERROR `DESIGN_UNSETTLED` to FAIL run-level `retirement-blocked`. That is the change owner item 5 already requires. The stop at `cli.py:358-361` is removed for these cases.

## 3. Gap (ii): an element naming an edit the named configuration does not have

### Options

- (a) The Form (iv) fallback: treat such an element as unreadable, so that it binds the edits the entry's `conclusions` name, or every edit of the entry's path, and binds at run level only when that set is empty.
  - Not proposed. `conclusions` is the writer's list, and a second-kind finding is the case where the reviewer disagrees with the writer. The edit the reviewer meant may be in neither set.
  - A revised plan could then proceed by removing the edits the fallback names while it still carries the one the reviewer meant. That fails open through a route Form (iv) does not otherwise allow.
- (b) Run-level binding of the lineage: the element names no edit, so the finding binds every configuration of its lineage at run level. Run-level binding is lifted only by a new freeze that cites an applying, reviewed reassessment naming the finding, with `edit` null (R6.RECON.27). It is the remedy Form (iv) already gives for an empty fallback set.

### Proposal

(b), keyed on the element's `id` alone. The element binds the lineage at run level when its `id` is missing, is not a string, or is not an edit id of the named configuration's edit list (a retained edit included). This holds whether or not its `target` matches, so a fabricated `target` cannot keep it below run level. Configurations outside the lineage stay bound by the matches of (iii) and (v), as now.

Where the configuration cannot be resolved, no element can be checked against a ledger. A run cannot tell a valid id that another configuration carries from an id that no configuration carries: both look the same from a configuration that does not carry it. The only fail-closed reading is therefore the one Form (iv) already applies to an unresolvable configuration with an empty set: run-level binding of every configuration.

For a configuration bound at run level, that binding takes the place of the finding's edit bindings of it. This blocks the same runs, since a run-level item fails the run. It also keeps R6.RECON.27 Keys unchanged ("`edit` is null exactly when the named finding is bound at run level"), and the tool's reassessment check (`category3.py:309-313`) already reads it that way. Keeping both bindings was considered and not proposed: it would need a Keys change allowing a null and a non-null reassessment of one finding for one configuration.

### Replacement wording (R6.RECON.26, Form of a finding (iv); one sentence inserted, one clause added to (v))

Current opening of (iv):

> (iv) *The edits a finding binds.* A finding binds the edits its `invalidated` elements name, by id and, where an element carries one, by target.

Replacement (the rest of (iv) is unchanged):

> (iv) *The edits a finding binds.* A finding binds the edits its `invalidated` elements name, by id and, where an element carries one, by target. A finding whose `configuration` is absent or cannot be resolved, or one of whose `invalidated` elements has an `id` that is missing, is not a string, or is not an edit id of the named configuration's edit list (R6.ADAPT.2 `edits`, a retained edit included), whatever its `target`, binds at run level every configuration of its lineage, and every configuration when its `configuration` cannot be resolved, as an empty set does below; for each configuration it binds at run level, that binding takes the place of its edit bindings of that configuration, and every other configuration is bound by the matches of (iii) and (v).

Current sentence in (v):

> A configuration bound only by an id collision (through the fallback of (iii), its edit of that id lying on another path) proceeds by a new freeze that renames the colliding id, through an AGENTS.md sec. A.48 item 3 migration where records cite it;

Replacement:

> A configuration bound only by an id collision (through the fallback of (iii), its edit of that id lying on another path, and not bound at run level under (iv)) proceeds by a new freeze that renames the colliding id, through an AGENTS.md sec. A.48 item 3 migration where records cite it;

### Controls (new cases; FINDING-KEYS for a resolvable configuration, FINDING-LINEAGE for an unresolvable one)

Each FAIL case below fails at `7db52f38` without the change: no `retirement-blocked` item is emitted.

| # | Row | Case | Outcome |
|---|---|---|---|
| 1 | FINDING-KEYS | an element `{id: "NO-SUCH-EDIT", sha256, target}`, its target's path and `old_sha256` held by no ledger, under a configuration that resolves to the run's configuration | FAIL, run-level `retirement-blocked` naming the finding, and `record-invalid` |
| 2 | FINDING-KEYS | the same, the record deleted by a later commit on `M` | FAIL, run-level `retirement-blocked` |
| 3 | FINDING-KEYS | the same, the run under a later version, on the named configuration's `supersedes` chain, that carries no edit of that id | FAIL, run-level `retirement-blocked` |
| 4 | FINDING-KEYS | a valid element naming edit `E1` and a second element with an unknown id: in the run's configuration the run-level binding takes the place of `E1`'s | FAIL, run-level `retirement-blocked`; `category3.blocked` holds one entry with `edit` null for the finding |
| 5 | FINDING-KEYS | a valid element and a second element that is an object without `id`, or whose `id` is a number | FAIL, run-level `retirement-blocked` and `record-invalid` |
| 6 | FINDING-KEYS | an element with an unknown id whose `target` matches an edit of the run's ledger by path and `old_sha256` | FAIL, run-level `retirement-blocked` (the target match does not keep it below run level) |
| 7 | FINDING-LINEAGE | an unknown-id element under a configuration that cannot be resolved, the run under a configuration of another retirement that carries neither the id nor the target | FAIL, run-level `retirement-blocked` and `record-invalid` |
| C1 | FINDING-KEYS | countercase: case 1's finding, the run under a configuration of another retirement outside the named configuration's lineage that carries neither the id nor the target (positive) | ANY, not `retirement-blocked` |
| C2 | FINDING-KEYS | countercase: case 1's finding, the configuration frozen anew citing an applying reassessment that names the finding with `edit` null (positive) | ANY, not `retirement-blocked` |
| C3 | FINDING-KEYS | countercase: case 1's finding and a reassessment naming it with a non-null `edit` | FAIL, `record-invalid` (Keys) and `retirement-blocked` |

C1 rules out a fix that binds every configuration when the configuration resolves. C2 shows the remedy works. C3 shows the run-level binding cannot be lifted through an edit reassessment.

### Effect on existing controls

| Row, case | Effect |
|---|---|
| FINDING-KEYS case 3 (an id absent from the named configuration's ledger) | outcome and classes unchanged (FAIL; `retirement-blocked`, `record-invalid`); the case text gains "and binds the lineage at run level" |
| FINDING-KEYS cases 1, 2, 4, 5, 6 and countercase 7 | unchanged: each element's id is an edit id of the named configuration |
| FINDING-LINEAGE case 5 (a finding naming no configuration) | outcome unchanged (FAIL); the case text gains "and every configuration at run level" |
| FINDING-LINEAGE case 6 | unchanged (FAIL) |
| FINDING-LINEAGE countercase 4, cases 1 to 3 and 7 | unchanged: the named configuration resolves and the element is anchored |
| FINDING-LINEAGE countercase 8 (the id-collision rename) | stays positive where the fallback comes from an element that differs from a resolvable configuration's ledger, because the other retirement is outside the lineage and is bound only by the global id match; the case text is narrowed to "the finding naming a readable configuration with which an element differs". Where the fallback comes from an unresolvable configuration, the other retirement is now bound at run level, and its remedy becomes an applying reassessment naming the finding with `edit` null. For a second-kind finding by an independent reviewer, R6.RECON.27 Keys then requires a `repair`, which is the cost noted below |
| FINDING-FORM, RECON-BLOCK, BLOCK-KEY, REASSESS-FORM, REASSESS-KEYS | unchanged: their elements are anchored; REASSESS-KEYS "edit null for a finding bound to an edit (not at run level)" still FAILs |
| Tool controls | the case for review finding 1 (`invalidated: ["junk"]`, present and then deleted) still blocks; in the lineage it now blocks at run level instead of through the `conclusions` edits; the run-level return of `bind` is reached for every unanchored or unresolvable finding |

**Cost, stated for the owner.** For an unresolvable configuration, every configuration is bound at run level, including those of other retirements. An unrelated retirement can lift that binding only with a reassessment naming the finding. If the finding is a second-kind finding by an independent reviewer, that reassessment needs a `repair` on `main` (R6.RECON.27 Keys). The over-blocking falls only on findings that already fail their form, because a missing or unresolvable `configuration` is a form failure, and it is the scope Form (iv) already gives the empty-set case. The alternative, keeping r13's carrier-only scope for an unresolvable configuration, leaves gap (ii) open for that sub-case and is not proposed. A narrower anchor for the second kind was considered and not proposed, because owner item 4 rules out additions without a demonstrated defect: it would fall back to the reviewed entry's own `scientific_effect.configuration` when the review's `configuration` does not resolve.

## 4. Requirements and rows touched on adoption

- R6.RECON.26: the body sentence (sec. 2), Form (iv) and Form (v) (sec. 3). No other requirement changes. R6.RECON.27, R6.RECON.30 and the key tables of sec. 23.1 are unchanged.
- EXPECTATIONS.json: FINDING-FORM (cases 1 to 7 and C1 to C2 of sec. 2), FINDING-KEYS (cases 1 to 6 and C1 to C3 of sec. 3; case 3 text), and FINDING-LINEAGE (case 7 of sec. 3; case 5 and countercase 8 text). No outcome of an existing case changes.
- REQUIREMENTS.json: the amendment-7 mark on R6.RECON.26, with no control removed.
- CONFORMANCE-MUTANTS.json: unchanged.

## 5. Tool changes implied (not made here)

- `engine/cli.py:356-363`:
  - replace the ERROR stop and the `in_m` gate by a scope test;
  - when the entry's list is a non-empty array of held commits that each change the entry's path, `applies = in_m(...)`;
  - otherwise `applies = True`, with the form problem "side_change_commits does not scope the finding (R6.RECON.26)";
  - a finding with no readable entry binds at run level (owner item 5).
- `engine/category3.py`, `bind`:
  - when the configuration is unresolved, return `([], True, form)`;
  - when it resolves, the run's configuration is in the lineage, and some element's `id` is missing, not a string, or absent from `_edits(fled)`, return `([], True, form)`;
  - otherwise bind as now.
- `blocked_items` and the reassessment check need no change.
- Runners for the new FINDING-FORM, FINDING-KEYS and FINDING-LINEAGE cases.

## 6. Probe recipe (provenance for sec. 1)

Run from a checkout holding `7db52f38`, with `S` a scratch directory:

```sh
mkdir -p "$S/tool" && git archive 7db52f380f1e51d4af52b84f0a7e728827ac5a60 tools/ledger_coverage | tar -x -C "$S/tool"
python3 -I probe.py "$S/tool"
```

`probe.py` imports `tools.ledger_coverage.engine.category3` from that directory. It then:

1. calls `in_m` with a stub repository, on `[]`, `["junk"]`, an unheld 40-hex id and a commit in `M`;
2. calls `bind` with a `Binding` whose run configuration has one edit `E1` (one splice on `doc.md`), on a second-kind finding whose `invalidated` is:
   - `[valid E1]`;
   - `[{id: "NO-SUCH-EDIT", ...}]` with the configuration resolving to the run's;
   - the same with an unresolvable configuration;
   - `["junk"]`.

The results expected at `7db52f38` are those quoted in sec. 1. The probe reads the code. It is not a control, and it is kept off the repository under AGENTS.md sec. A.28.
