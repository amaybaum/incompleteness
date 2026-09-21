# Guard repair round GR-1 — scoping act 28's ROADMAP contract to act 28's own entry: PREREGISTRATION

**Control plane only.** This document fixes what `GR-1` will do, what would count as each outcome,
and what no outcome licenses, before any of it is implemented. One file, added. No Lean, no guard
clause, no manifest record, no declaration, no ROADMAP edit, no manuscript edit.

**The mandated execution base is the merge commit of this pull request**, once that merge and its
`main` push run are themselves certified. The execution branches from exactly that commit and from
nothing else, and its first act is to verify this preregistration's blob at that base.

## The commit vocabulary this freeze uses, fixed first

Per `AGENTS.md` `§A.37`, three commit names, and no other meaning of "base" anywhere in this file.

- **`D`** — the drafting snapshot, `0bedff07fc1ad2675ecab205c8836e7a90a113d4`: the merge commit of
  #704, act 29's control plane, certified as the state of `main` by push run 35566401811. Every
  measurement below marked "at `D`" was taken against that commit: the pinned blobs, the
  name-freedom checks, the line coordinates, the differential suite.
- **`B`** — the mandated execution base: the certified merge commit on `main` of this
  preregistration, or of the latest execution-affecting append-only amendment if one is made.
  **Before that merge exists `B` has no SHA, and this file assigns it none.**
- **`M`** — a candidate control-plane merge, constructed by continuous integration before this file
  lands, used to evaluate the `B`-scoped preconditions predictively. `M` is test state only. It is
  never execution ancestry, never seal state, and never historical evidence.

`D` is not `B`. `D` is also act 29's mandated execution base, which is a fact about the repository
and not a property this round uses: act 29's execution is a separate branch from that commit, and
nothing here is measured against it.

Two further names, used only for the round's own objects once they exist: **`E`**, the final
execution head, the non-first parent of the landing; and **`L`**, the landing merge, defined
exactly under *The chronology rule* below. Neither has a SHA before the execution, and this file
assigns neither one.

## What `GR-1` is, and what it deliberately is not

**`GR-1` repairs one contract of one closed guard.** Act 28's guard `R7-PFR` gates the `P0` row of
`verification/ROADMAP.md` through one predicate, `_pfr_road_ok`. Its final leg is written over the
**whole document** rather than over act 28's entry: it requires the frozen act 28 sentence to occur
exactly once in the file **and the standing clause to occur exactly once in the file**. Act 29's
control plane (#704, frozen at `D`) requires act 29's execution to append act 29's own frozen `P0`
sentence after act 28's, **followed by the same standing clause**. A ROADMAP carrying both entries
therefore carries the clause twice, the document-wide count fails, and `R7-PFR` goes red on any act
29 head — for a reason that has nothing to do with act 28's mathematics, act 28's artifacts or act
29's result. Act 29's execution measured exactly this on its pull request (#705, head
`bf7e96fef8135525e752fb0daba0a082cf10ed44`) and recorded it as its discrepancy `RD2`, repairing
nothing, as its freeze requires.

The two contracts are jointly unsatisfiable as written, and neither closed round may edit the
other's. Under `§A.37` a contract is changed only by a round that **owns the change prospectively**.
This is that round. It owns exactly one change: **`_pfr_road_ok` is rewritten from a document-wide
clause count to validation of act 28's own entry** — act 28's unique frozen sentence, inside the
actual `P0` cell, after act 27's anchor, with the complete standing clause attached immediately
after it, once — so that a successor round's entry, which necessarily reuses the standing clause,
is outside the bound and neither counted nor accepted in act 28's place.

**`GR-1` is NON-SEALING**, `E` → `L`, no `P`. It creates no seal state and alters none. It writes
no manifest record, no prospective declaration and no baseline change; the last of these is a
**narrow, explicitly owned exception** to `§A.37`'s baseline rule, stated with its integrity
guarantees under *The baseline* below.

**What it is not.** It is not a Track B round and it states nothing about act 28's or act 29's
mathematics: act 28's verdicts, frozen artifacts and seal record stand at the blobs pinned below
and are not touched; act 29's verdicts are act 29's, certified or not by act 29's own lifecycle,
and this round neither reads nor reports them. It is not a repair of act 29's `RD2`: **`RD2` is
history**, a true statement about act 28's contract as frozen against act 29's head, and it stays
in act 29's record exactly as recorded. `GR-1` changes what holds **from its landing on**; it does
not make the recorded failure not have happened, and its result note says so in those terms. It
does not edit `R7-PFR`'s description string, its pins, its other predicates or its mutation
controls: only the body of the one predicate named. It does not edit `verification/ROADMAP.md`, act
28's directory, `verification/seals/`, any Lean file, the census, `AGENTS.md`, or any file outside
the guard and its own round directory. It does not change `_MANIFEST_BASELINE` or
`_MANIFEST_PROSPECTIVE`. It does not touch the validator regions.

## The round's shape, declared first, in `§A.37`'s terms — under the retired representation

A non-sealing round after `SI-3` has no worked precedent: `SI-2`, the last non-sealing round,
carried its base as a legacy constant that `SI-3` retired, and `§A.37` prescribes the prospective
declaration **for a sealing round**, whose `LANDED-PENDING-PIN` state is resolved by `P`. A
non-sealing round has no `P`; a declaration left in place after `L` would fail every descendant of
`L` as *seal pending*, and a `base-only` record written during the round would classify it
`not-applicable` and switch off its own chronology check. `§A.37` says the `base-only` record is
created **afterwards**, by a later round that names the addition in its own preregistration.

This round also runs **beside a concurrent execution**, act 29's, whose sealed head must never
change and whose pull request must be able to build a candidate merge with `main` after this round
lands (the certification path act 29's review fixed). That candidate merge conflicts if `GR-1`
touches a line act 29's execution touched, and fails act 29's own integrity rule if `GR-1` adds a
record to `verification/seals/` before act 29 lands. Act 29's execution sets exactly two lines
outside the guard blocks — `_MANIFEST_BASELINE` and `_MANIFEST_PROSPECTIVE` — and inserts its
block between `R7-PFR`'s `check(...)` and the `R7-SI1` banner. Avoiding that conflict is the
**reason** the shape below is chosen; it is not by itself an authorization for anything, and each
departure from the ordinary protocol is owned in terms in its own subsection.

| object | during execution | at `L` | afterwards |
| --- | --- | --- | --- |
| the mandated execution base | carried **inside `R7-GR1`'s own block** as the literal `_GR1_B`; act 10's strengthened check is asked of the real head against it | unchanged | unchanged until the record exists |
| `_MANIFEST_PROSPECTIVE` | **untouched**, `{}` at `B` and at every commit of the round | untouched | untouched |
| `_MANIFEST_BASELINE` | **untouched**, act 28's declaration, under the owned exception below | untouched | untouched |
| `verification/seals/` | **byte-identical to `B`'s tree**, held by `R7-GR1`'s own integrity contract | equal to the first parent's tree | `B`'s thirty-three records immutable; later authorized additions outside this round's scope |
| `verification/seals/GR1.json` | absent | **absent** | `{"round": "GR1", "kind": "base-only", "base": <B>}`, created by a later round that names it as an authorized addition, as `SI2-1` created `SI1.json` and `SI-3` created `SI2.json` |
| `R7-GR1`'s chronology verdict | `EXECUTION`: strengthened check of the real head against `_GR1_B` | `LANDED-UNRECORDED`: the canonical landing found, `E` recovered as its non-first parent | `LANDED-UNRECORDED` until the record exists; then `RECORDED`: the keyed call `_si2_authority('GR1', tag='R7-GR1')`, `not-applicable` with the base reachable |

**This shape is the freeze's reading of `§A.37` for a non-sealing round under the retired
representation, and it is flagged for owner review as such.** If the owner prefers the prospective
path with the record written at `L`, that is an amendment before the merge, and the consequences
for act 29's candidate merge — a two-line conflict and an unauthorized addition under act 29's
frozen baseline — are the owner's to weigh.

### The chronology rule `R7-GR1` carries, FROZEN

Let the **visibility targets** be those `_rbr_archive_visibility_targets` returns: the real
`pull_request.head.sha` and the current tip of the base branch as
`refs/remotes/origin/<base ref>` on a pull request, `HEAD` otherwise; an unresolvable target fails
closed. Let the **real head** be what `_rbr_target_commit` returns: `pull_request.head.sha` on a
pull request, `HEAD` otherwise, never the synthetic merge.

**Two conditions on a commit `h` relative to `_GR1_B`, kept apart because they answer different
questions.**

- **Ancestry** — act 10's strengthened check: the base an ancestor of `h`, and every commit of
  `rev-list h ^base` a descendant of the base. This is what refuses pre-freeze side history. It
  does **not** refuse a merge that absorbed a later `main` whose commits themselves descend from
  the base, nor a merge of two branches both cut from the base: every commit in such a history
  descends from the base, and the check passes.
- **Execution shape** — `rev-list h ^base` contains **no merge commit**, `h` included: the
  history from the base to `h` is a single first-parent chain. This is what refuses every
  absorption of later `main`, and every merge of any kind, inside an execution.

**The canonical landing.** A commit `X` is *a landing of this round* iff `X` is a merge commit and
some non-first parent `p` of `X` satisfies all of:

- (a) `p` satisfies **execution shape**, so `p` is not a merge and nothing below it back to the
  base is;
- (b) `p` satisfies **ancestry**;
- (c) the guard file at `p` carries `check('R7-GR1'`;
- (d) `result.md` and `gr1-tagmap.json` both exist at their paths in this round's directory at
  `p`.

(a) excludes the merge that GitHub creates when the pull request merges, whose non-first parent is
`L` itself — that merge is *not* a landing, and `L` is found inside its history — and excludes a
non-first parent that absorbed a later `main` descending from the base. (b) excludes a non-first
parent carrying pre-freeze side history. (c) excludes a sibling's control-plane branch cut from
`B` or later, whose commits also descend from `B`. (d) excludes a merge of an **incomplete**
execution — a stage-2 parent that carries the block but not the artifacts. The landing `L` of this
round is the **unique** landing reachable from the union of the visibility targets' histories, and
`E` is its non-first parent `p`. Two or more landings, or a landing whose `p` is ambiguous, **fail
closed**, as the validator's derivation fails on multiple candidates.

Then, in this order:

1. **`RECORDED`.** If `verification/seals/GR1.json` exists, the verdict is
   `_si2_authority('GR1', tag='R7-GR1')` and nothing else in this rule runs. A malformed record —
   a schema failure, a `sealed_head` or `merge` field even as null, a `round` other than `GR1`, or
   a `base` other than `_GR1_B` — **fails closed** through the validator's schema check and a
   base comparison in this clause. The rule below is not a shadow of the keyed verdict: the two
   never run together.
2. **`LANDED-UNRECORDED`.** Otherwise, if a canonical landing exists, the verdict is `PASS` with
   `L` and `E` printed, and no ancestry question is asked of the real head. This is the state on
   `main` from the landing on, and on every later pull request — a head that predates `B`
   included — whose base branch tip carries `L`.
3. **`EXECUTION`.** Otherwise the verdict is the conjunction of **ancestry** —
   `_rbr_strong_ancestry(_GR1_B, real head)`, recovery included, fail-closed — **and execution
   shape** of the real head, each printed with its own verdict, both asked of the real
   `pull_request.head.sha` and never of the synthetic merge. A head that passes ancestry and
   fails shape — a merge of an incomplete execution into a `main` that descends from the base,
   or a sibling branch merged the same way — is `EXECUTION`, `FAIL`, for shape and not for
   ancestry, and the printed line says which.

State 2 is what lets the repaired guard, once on `main`, run inside act 29's candidate merge without
asking act 29's head to descend from a base it predates. State 3 is the bootstrap form `§A.37`
names for a round with no record. The literal that carries the base is named `_GR1_B`, on the
pattern of `_PFR_B` and every Track B round's `_<STEM>_B`, and matches no legacy shape: nothing
matching `_GR1_(BASE|SEALED_HEAD|MERGE)` exists at any commit of the round, and `SI-3`'s standing
zero holds at every head.

### The baseline: a narrow exception, owned here, with its guarantees

`§A.37` says each round declares its own integrity baseline. `GR-1` **does not**: `_MANIFEST_BASELINE`
stays act 28's declaration, `{'base': '101b8cebb140c2ee7b982641ff005b84bbf0a1cf', 'authorized':
('PFR',)}`, at every commit of the round. That line is one of the two lines act 29's execution
already writes, and a concurrent write to it is the conflict that would make act 29's candidate
merge unbuildable; but the conflict is the reason, not the licence. The licence is this
subsection, which owns the departure prospectively and replaces what the ordinary rule would have
guaranteed with something at least as strong:

- **What act 28's declaration guarantees at `B`, and what it does not.** Measured at `D`: the seals
  tree at `101b8ceb…` holds thirty-two records and no `PFR.json`; the tree at `D`, blob
  `92e0956a…`, holds exactly those thirty-two plus `PFR.json`, and precondition row 11 checks
  the same identity at `B`. Under the retained declaration `U5` holds those **thirty-two** records
  against mutation, removal and any addition other than `PFR`. It does **not** hold `PFR.json`'s
  content: `U5` reads the current record of an authorized stem into its expected set, so a
  mutation of `PFR.json` passes `U5` under this declaration. The retained declaration is therefore
  **not** equivalent to a declaration of `B`'s whole tree, and this freeze does not claim it is.
  (`PFR.json`'s content is separately held by act 28's own keyed clause, which validates the
  record against the derived landing; that is act 28's guarantee, not this round's.)
- **What closes the gap: `R7-GR1`'s integrity contract, during execution.** The set of
  `(stem, content)` pairs under `verification/seals/` in the working tree equals the set at
  `_GR1_B`, read from git, byte for byte — zero additions, zero mutations, zero removals,
  `PFR.json` included — at every commit of the round up to `E`. This, and not the retained
  declaration, is what protects every record at `B` while this round runs; it is strictly stronger
  than `U5`'s authorized-addition form, since nothing is authorized and nothing is read from the
  working tree into the expectation.
- **At `L`.** The seals tree equals the first parent's tree: `GR-1` adds nothing at `L` either.
- **After landing, the closed-round rule.** `B`'s thirty-three records remain present and
  byte-identical on every later tree this guard runs on; additions by later rounds are outside this
  round's historical scope and are policed by the current round's own `U5`, exactly as `§A.37`
  reads a closed round's contracts over the records it manifested.
- **The exception ends with this round.** The next round to declare — the one that adds
  `GR1.json`, or any later one — declares its own baseline under the ordinary rule, and this
  subsection authorizes nothing for it.

### The tag, the stem and the round directory are free at `D`

Measured at `D`, each returning nothing: `R7-GR1`, `_GR1`, `round-gr-1`, `roadmap-entry-scoping`,
`gr1_`, `gr1-tagmap`. The bare token `GR1` occurs at `D` in exactly one file, as a substring of act
26's identifier `_CGR1`, and as a whole word nowhere; the freedom check is the whole-word one.
These are checks at `D`, recorded as drafting-time facts; they are not conditions on `B`, where this
file's own text carries every one of them.

### What this round does NOT own, named exhaustively

It owns no round's seal state, alters no manifest record, writes no legacy seal constant, edits no
contract other than the one named in the supersession table, and writes no manuscript file. It
makes no claim about act 29's outcome vector, about the four `R7-PRA` findings act 29's review
cleared, or about whether act 29's head certifies.

## What `GR-1` inherits, and only this

1. Act 28's certified artifacts at the blobs pinned below: its preregistration, its result note and
   `PFR.json`, read and never written. `_PFR_P0`, `_PFR_ROAD_STANDING` and act 27's anchor sentence
   are consumed as the constants act 28's guard already carries; none is restated.
2. Act 29's frozen control plane at its pinned blob, read only for the five frozen `P0` sentences
   it names — one per outcome case — which are the successor fixtures of the differential suite.
   Act 29's execution artifacts are **not** inputs, and no fixture is read from act 29's branch.
3. `U1`–`U5` and the guard's ancestry helpers as `SI-3` left them, unchanged in text and semantics.
4. `§A.37` as amended by `SI3-6`, the protocol this round lands under.

## The superseded contract and its replacement, stated as text and not as prose

Measured at `D` from `verification/lean/edge_rigidity_probe.py`, blob
`5e2c36c30c2e231bc726741bd522ec051b657391`. The predicate stands at lines 27963–27979; the
`R7-PFR` road mutation controls at lines 28179–28197; `check('R7-PFR', …)` at lines 28203–28222;
the `R7-SI1` banner at line 28225; `check('R7-SI3', …)` at lines 31184–31212; line 31213 is blank
and the closing scope print begins at line 31214.

**The predicate at `D`, the last line of which is the superseded leg:**

```python
def _pfr_road_ok(road):
    """THE PREDICATE THAT GATES the ROADMAP P0 cell. Every mutation below is passed through it."""
    cell = _pfr_p0_cell(road)
    if cell is None:
        return False
    c = _pfr_n(cell)
    p0 = _pfr_n(_PFR_P0)
    if c.count(p0) != 1:
        return False
    anchor = _pfr_n('with its selecting power left open.')
    if anchor not in c or c.index(p0) < c.index(anchor):
        return False
    # this round's standing clause is not merely present: it follows the frozen sentence it scopes.
    if not c[c.index(p0) + len(p0):].lstrip().startswith(_pfr_n(_PFR_ROAD_STANDING)):
        return False
    n = _pfr_n(road)
    return n.count(p0) == 1 and n.count(_pfr_n(_PFR_ROAD_STANDING)) == 1
```

**The replacement, frozen here, installed by `GR1-1` under the same name so that
`_pfr_checks['roadmap']` and act 28's seven mutation controls pass through it unchanged:**

```python
def _pfr_road_ok(road):
    """THE PREDICATE THAT GATES act 28's ROADMAP entry, read as a BOUNDED ENTRY.

    Act 28's entry is its unique frozen sentence, inside the ACTUAL P0 cell, after act 27's anchor,
    with the complete standing clause following it. The predicate validates that entry and counts
    nothing beyond it: a successor round's entry, which necessarily reuses the standing clause, is
    outside the bound and is neither counted nor accepted in its place.
    """
    cell = _pfr_p0_cell(road)
    if cell is None:
        return False
    c = _pfr_n(cell)
    p0 = _pfr_n(_PFR_P0)
    if c.count(p0) != 1:
        return False
    anchor = _pfr_n('with its selecting power left open.')
    if anchor not in c or c.index(p0) < c.index(anchor):
        return False
    # this round's standing clause is not merely present: it follows the frozen sentence it scopes.
    if not c[c.index(p0) + len(p0):].lstrip().startswith(_pfr_n(_PFR_ROAD_STANDING)):
        return False
    n = _pfr_n(road)
    return n.count(p0) == 1
```

What is kept, leg for leg and **verbatim**: the actual-cell read through `_pfr_p0_cell`, the unique
sentence in the cell, the position after act 27's anchor, the adjacency leg — the text after the
sentence begins with the complete clause, which already rejects a truncated clause and a detached
one — and the sentence nowhere else in the document. The adjacency leg is retained in act 28's own
text rather than restated: a restatement as "sentence + one space + clause" would reject a clause
adjoining the sentence with no whitespace, which the retained leg accepts, and this round owns no
such tightening. The **one** change is the removal of the document-wide count of the **standing
clause** from the final line, the leg that a successor entry cannot satisfy. The docstring is the
only other text that differs, and `GR1-1` measures the function against this block byte for byte.

## The differential acceptance suite, FROZEN

The suite is measured against **both** predicates: the old one, executed from the guard text at
the pinned blob `5e2c36c3…` through `git cat-file blob` and the same extraction the tag-map
measurements use — never from the live file — and the new one, live. It is the round's sharpest
evidence: the two predicates must differ on exactly the successor rows and agree everywhere else.

Fixtures, each built from the ROADMAP at `D`, blob `d0658c99b6ef13d984fd533760393c0b4a2e43c7`,
read through `git cat-file blob` and never from the working tree, so that the suite is the same
fixture set at every head of the round and after act 29's entry lands:

- **`act-28-alone`** — the blob itself. At `D` it carries act 28's entry once, the sentence once in
  the file.
- **`act-29-frozen-sentence-1` … `-5`** — act 28's entry followed by ` ` + one of act 29's five
  frozen `P0` sentences + ` ` + the standing clause, in the cell; the sentences are those act 29's
  freeze fixes for rows 1–3, row 1, row 2, rows 4/7/10 and rows 5/6/8/9/11, verbatim.
- **`generic-successor`** — the same with a sentence of no particular content: "A later round's
  sentence, of any content, in the same cell."
- **`two-successors`** — act 28's entry, then the fifth act 29 sentence with the clause, then the
  generic sentence with the clause.
- **`no-whitespace-adjoin`** — act 28's sentence with the complete clause adjoining it with no
  whitespace between. Both predicates accept it; the row exists to show that the retained adjacency
  leg is unchanged and no tightening is introduced.
- **Mutations of act 28's entry**, each applied to `act-28-alone` and again on top of
  `act-29-frozen-sentence-5`, so that a successor's presence never masks a mutation of act 28's
  entry. Act 28's seven, verbatim from its own control block: `p0-deleted`, `p0-duplicated`,
  `standing-clause-removed`, `standing-clause-detached`, `p0-before-act27`,
  `p0-block-moved-out-of-the-cell`, `p0-row-removed`. And three this round adds:
  `p0-duplicated-in-cell` (the whole entry twice in the cell), `standing-clause-truncated` (the
  clause cut to its first 120 characters) and `successor-between-sentence-and-clause` (the generic
  sentence inserted between act 28's sentence and act 28's clause).

**The expected table, measured at `D` by the drafting script and reproduced by the execution:**

| row | old | new |
| --- | --- | --- |
| `act-28-alone` | accept | accept |
| `act-29-frozen-sentence-1` … `-5` | **reject** | accept |
| `generic-successor` | **reject** | accept |
| `two-successors` | **reject** | accept |
| `no-whitespace-adjoin` | accept | accept |
| each of the ten mutations, on `act-28-alone` | reject | reject |
| each of the ten mutations, on `act-29-frozen-sentence-5` | reject | reject |

Twenty-nine rows. The seven **reject / accept** rows are the defect and its repair, in one table:
the old predicate rejecting every successor form is `RD2` reproduced from the pinned text, and the
execution reports that reproduction in the same words. At `D` the fixture
`act-29-frozen-sentence-5` is byte-identical to `verification/ROADMAP.md` at #705's head, blob
`f26f7c1c8d275539bccb21d6faa2e882abc6dcf8` — a drafting-time observation about an uncertified
head, recorded here for the reader and gating nothing.

## The objects `GR-1` builds

**`R1` — the predicate**, above, in place of the old body, same name, same call sites.

**`R2` — the guard `R7-GR1`**, one block appended after `check('R7-SI3', …)` and before the
closing scope print, and nowhere else. It carries: this preregistration pinned by blob at this
path with a one-byte drift control; the locating controls of `GR1-0`; the byte comparison and the
**placement contract** of `GR1-1`, in its two regimes below; the differential suite of `GR1-2` with
both predicates; the verdict-map contract of `GR1-3`; the chronology rule above with its lifecycle
fixtures; the integrity contract of *The baseline*; and the content contracts on the result note
listed under *The guard*. No definition, no Lean, no manifest record.

**The placement contract, in two regimes, selected by the chronology state.**

- *In `EXECUTION`*: the head's guard file, with `_pfr_road_ok`'s body reverted to the pinned text
  and the `R7-GR1` block removed, equals the pinned blob `5e2c36c3…` byte for byte — the
  whole-file form, which is exact while nothing but this round has touched the file since `B`.
- *In `LANDED-UNRECORDED` and `RECORDED`*: the whole-file form is **not** applied to the current
  tree, which by then carries other rounds' changes — act 29's two declaration lines and its
  `R7-PRA` block among them. Instead the round's **historical change budget** is measured once,
  from git objects, against its recovered checkpoint: the guard file at `E` (recovered as the
  canonical landing's non-first parent), with the same two regions reverted, equals the guard file
  at `_GR1_B`; and on the current tree only the **owned regions and the protected artifacts** are
  checked — `_pfr_road_ok`'s live body equals the frozen text under per-line whitespace
  normalization; this preregistration, `result.md` and `gr1-tagmap.json` are at their paths with
  the blobs they have at `E`; act 28's preregistration, result note and `PFR.json` are at their
  pinned blobs.

**`R3` — the result note**, `result.md` in this round's directory, and **`gr1-tagmap.json`**
beside it. The JSON carries two columns over the **ninety-two pre-existing tags** and no other:
the *base column*, the tag-to-verdict map of the base's guard file run at `B` in a detached
temporary worktree with every git and pull-request environment variable removed, exactly as
`SI2-6`(a) and `SI3-7` run their bases; and the *head column*, the same ninety-two tags' verdicts
from the stage-2 dry run on the head's guard file — the run at which the block is present and the
artifacts are not, so that the column does not depend on the file it is written into. `R7-GR1`
does not re-run the base's file on every build: the base run is taken **once**, by the execution,
and persisted, and the nested cost `SI-3` accepted is not added to. What `R7-GR1` checks live, on
every build, is stated under `GR1-3`.

**Three definition slots** are budgeted, one per object; test code, the fixtures and mutation
controls are not definition slots. Unused slots are recorded as unused.

## The order is part of the contract, with the checks that apply at each checkpoint

| stage | target | what it does | dry run required before the next commit exists |
| --- | --- | --- | --- |
| 1 | `GR1-1` | **one commit:** `_pfr_road_ok`'s body replaced by the frozen text; nothing else in the file changes | every one of the ninety-two pre-existing tags `PASS`, `R7-PFR` included, on the ROADMAP at `B`; no `R7-GR1` exists yet |
| 2 | `GR1-2` | **one commit:** the `R7-GR1` block appended, carrying the differential suite, the chronology rule and its fixtures, the pins, the placement and integrity contracts, and the artifact contracts of `GR1-3` | every pre-existing tag `PASS`; **`R7-GR1` `FAIL` on exactly its two artifact contracts** — `result.md` absent, `gr1-tagmap.json` absent — and on nothing else, its failing-contract names printed; the ninety-two verdicts of this run are the head column |
| 3 | `GR1-3` | **one commit:** the base's guard file run at `B` in a detached worktree; `gr1-tagmap.json` written with both columns; `result.md` written, recording stage 2's failure set verbatim | **every tag `PASS`, ninety-three, `R7-GR1` included: every contract of this freeze is mandatory here and at every later head** |
| — | `GR1-0` | the locating controls, measured first and reported last | — |

**Each stage is one commit, in this order, and the stage-3 commit is `E`.** No contract is
optional at `E`: the staged tolerance is exactly the one named in stage 2's row, it exists only at
that checkpoint, and it is not encoded in the guard as a tolerance — a build at stage 2 is red on
the two artifact contracts, and is expected to be. The execution pushes the chain once, at `E`; the
stage-1 and stage-2 dry runs are local and their outputs are recorded in the result note.

**The history contract, in its checkpoint form.** `R7-GR1`'s history contract reads the
first-parent chain from `_GR1_B` to the real head (in `EXECUTION`) or to the recovered `E` (after
landing) and requires it to be a **prefix of the frozen three-stage sequence**: commit 1 changes
the guard file and nothing else, and its change is exactly `_pfr_road_ok`'s body; commit 2
changes the guard file and nothing else, and its change is exactly the appended block; commit 3
adds exactly `result.md` and `gr1-tagmap.json` and changes nothing else. A chain of length one
or two that matches the sequence so far **passes** the history contract — which is what makes
stage 2's required failure set exactly the two artifact contracts and nothing else — and a chain
of length three that matches it passes. A chain that departs from the sequence at any position, or
has a fourth commit, **fails**. The complete chain is made mandatory not by the history contract
alone but by the **artifact contracts**, which fail on any prefix shorter than three: so `E` is
certifiable only at the stage-3 commit, and after landing the recovered chain from `_GR1_B` to `E`
must be exactly the three. Fixture F13 exercises each length.

## The targets, FROZEN

Each target names the artifact that decides it. A target is decided only by that artifact.

**`GR1-0` — locating controls.** The pinned blobs and the preconditions below hold at the mandated
base. Outcomes: `HOLD` / `DRIFTED`. `DRIFTED` stops the round.

**`GR1-1` — the predicate is the frozen one and nothing else moved.** The body of `_pfr_road_ok` at
the head equals the frozen replacement byte for byte after whitespace normalization of each line;
the placement contract holds in the regime the chronology state selects; `_pfr_checks['roadmap']`
and the seven `road-mut:` controls are untouched and pass through the new body. Outcomes:
`INSTALLED-AS-FROZEN` / `INSTALLED-DEVIATED`.

**`GR1-2` — the differential suite.** All twenty-nine rows return the expected pair. Outcomes:
`SUITE-AS-FROZEN` / `SUITE-DEVIATED`. A deviation on a **reject / reject** row is a finding about
the replacement's tightness and stops the round; a deviation on an **accept** row of the new
predicate is a finding about its tolerance and stops the round; a deviation in the **old**
column is a finding about the extraction and stops the round. No expectation is edited to fit.

**`GR1-3` — the verdict map is preserved.** Read from `gr1-tagmap.json` and checked live on every
build: the base column holds exactly the ninety-two tags the base's guard file carries, every
verdict `PASS`; the head column holds the same ninety-two tags, every verdict `PASS`; **the head
column equals, tag for tag, the verdicts the current run computed for those tags**; and the
current run's tag set minus the ninety-two is exactly `{R7-GR1}` at `E` — at later heads, further
tags added by later rounds are outside this round's scope and the contract on the set is that the
ninety-two are all present. Outcomes: `MAP-PRESERVED` / `MAP-CHANGED`. `MAP-CHANGED` stops the
round and reports; a changed verdict is never adopted as an improvement.

## The contract this round supersedes, named in advance

Under `§A.37`'s ownership rule this table is the authorization. **Nothing outside it is touched in
any closed round's guard**, and a failure outside it is a result requiring adjudication.

| guard | contract | why | disposition |
| --- | --- | --- | --- |
| `R7-PFR` | `_pfr_road_ok`'s final leg — the standing clause occurs exactly once in the whole document | a successor entry that `§A.37`'s own `P0` convention requires carries the same clause; the leg is unsatisfiable together with act 29's frozen `P0` instruction | **retired**; the document-wide count of act 28's **sentence** is kept |

Every other leg of the predicate, the adjacency leg included, is retained verbatim and is not in
this table; nothing else of `R7-PFR` is superseded.

What this table does **not** do: it does not edit act 28's preregistration, result note or seal
record; it does not change what act 28 recorded as its outcome; it does not change `R7-PFR`'s
description string, whose sentence "exactly one mention of each clause with that mention opening
the COMPLETE clause" is about the result note and the census entry and remains true of them; it
does not touch `R7-PRA`, act 29's guard, at any commit of act 29's branch; and it does not reopen
anything adjudicated.

## Predictions, with strength

| target | predicted | strength |
| --- | --- | --- |
| `GR1-0` | `HOLD` | HIGH |
| `GR1-1` | `INSTALLED-AS-FROZEN` | HIGH |
| `GR1-2` | `SUITE-AS-FROZEN` | HIGH |
| `GR1-3` | `MAP-PRESERVED` | HIGH |

All HIGH because every row was measured at `D` by the drafting script and the replacement is
frozen as text. The informative failure would be `GR1-3`: a tag other than `R7-PFR` whose verdict
depends on `_pfr_road_ok`'s document-wide count, which would mean another guard reads the ROADMAP
through act 28's predicate, and that is reported and not repaired.

## Lifecycle fixtures, FROZEN

The chronology rule is exercised, on every build, against **synthetic repositories** built in a
temporary directory by `R7-GR1`'s own test code, in the manner of `SI-1`'s suite, so that each state
and each exclusion is measured and not merely stated. Each fixture builds a base `b`, and the rule
is evaluated with `_GR1_B` bound to `b`, the visibility targets and the real head as the fixture
names, and the seals directory of the fixture's tree. The fixture set, with its required verdict:

| # | fixture | targets / real head | required |
| --- | --- | --- | --- |
| F1 | linear execution: `b` → `s1` → `s2` → `s3`, block from `s2`, artifacts from `s3` | head `s3`, base tip `b` | `EXECUTION`, ancestry `PASS`, shape `PASS`, **`PASS`** |
| F1a | the two-commit prefix: head `s2` | head `s2`, base tip `b` | `EXECUTION`, ancestry `PASS`, shape `PASS`, **`PASS`** on the chronology clause; the artifact contracts fail separately |
| F2 | execution that absorbed pre-freeze history: `b` → `s1` → merge of a commit not descending from `b` → `s3'` | head `s3'` | `EXECUTION`, ancestry **`FAIL`**, shape `FAIL`, **`FAIL`** |
| F2a | execution that absorbed later main descending from `b`: `b` → `s1` → merge of `main'` (a descendant of `b`) → `s3'` | head `s3'` | `EXECUTION`, ancestry `PASS`, shape **`FAIL`**, **`FAIL`** — the case ancestry alone does not refuse |
| F3 | incomplete execution merged: `m` = merge of `main'` and `s2` | head `m`, base tip `main'` | **not a landing** (d fails); `EXECUTION` asked of `m`: ancestry `PASS`, shape **`FAIL`**, **`FAIL`** |
| F4 | the canonical landing: `l` = merge of `main'` and `s3` | head `l`, base tip `main'` | `LANDED-UNRECORDED`, `PASS`, `E` = `s3` |
| F5 | the enclosing merge: `g` = merge of `main'` and `l` | head `g` (push) | `LANDED-UNRECORDED`, `PASS`, landing = `l` not `g`, `E` = `s3` |
| F6 | an older head with repaired main: head `h` a commit predating `b`, base tip `g` | head `h`, base tip `g` | `LANDED-UNRECORDED`, `PASS` — neither ancestry nor shape asked of `h` |
| F7 | sibling control plane cut after `b`: `c` = merge of `main'` and a commit descending from `b` with no `R7-GR1` | head `c` | **not a landing** (c fails); `EXECUTION` asked of `c`: ancestry `PASS`, shape **`FAIL`**, **`FAIL`** |
| F8 | two landings: `l` and a second merge `l'` of another branch whose non-first parent also satisfies (a)–(d) | head descending from both | `FAIL` — multiple candidates |
| F9 | a well-formed record: F5's tree plus `GR1.json` `base-only` with `base` = `b` | head `g` | `RECORDED`, keyed verdict `not-applicable`, `PASS` |
| F10 | malformed records, each a separate fixture on F5's tree: `GR1.json` with `sealed_head` null; with `merge` present; with `round` `GR2`; with `base` ≠ `b`; not valid JSON | head `g` | `RECORDED`, **`FAIL`** in each |
| F11 | the seals tree mutated during execution: F1 with one existing record's content changed; with one record removed; with a new record added | head `s3` | integrity contract `FAIL` in each |
| F12 | F4 with the landing's non-first parent itself a merge of `s3` and `main'` | head that merge's descendant | **not a landing** (a fails); `EXECUTION` asked of the head: shape `FAIL`, **`FAIL`** |
| F13 | the history checkpoints: heads `s1`, `s2`, `s3` of F1, and a head `s4` = `s3` + one more commit | each head, base tip `b` | history contract `PASS` at `s1` and `s2` as valid prefixes, `PASS` at `s3` as the complete chain, **`FAIL`** at `s4`; the artifact contracts `FAIL` at `s1` and `s2`, `PASS` at `s3` |

Every fixture is evaluated on every build; a fixture returning other than its required verdict
fails `R7-GR1`. Fixtures are test code, not definition slots, and touch no real ref.

## The negative suite

Each case must satisfy its named outcome for its named reason. Cases 1–20 are the twenty
**reject** rows of the differential suite and are listed there; cases F1–F13 are the lifecycle
fixtures above. In addition:

21. The frozen replacement with its adjacency leg weakened to `_pfr_n(_PFR_ROAD_STANDING) in c` —
    accepts `standing-clause-detached` — **fails `GR1-2`**; and with that leg restated as
    `c.count(p0 + ' ' + st) == 1` — rejects `no-whitespace-adjoin` — **fails `GR1-2`**.
22. The frozen replacement with its final line `return n.count(p0) == 1` replaced by `return True`
    — accepts `p0-duplicated`, the sentence copied outside the cell with the cell's entry intact —
    **fails `GR1-2`**. (Deleting the line outright is not this mutant: a function that falls off
    its end returns `None` and rejects the valid baseline too, for the wrong reason.)
23. In `EXECUTION`, one byte changed anywhere in the guard file outside the two owned regions —
    **fails the placement contract**, whole-file form.
24. After landing, `_pfr_road_ok`'s live body differing from the frozen text, or the guard at `E`
    differing from the guard at `_GR1_B` outside the two owned regions, or `result.md` or
    `gr1-tagmap.json` on the current tree differing from their blobs at `E` — **fails the placement
    contract**, landed form; the current tree carrying other rounds' changes elsewhere in the file
    **does not**.
25. `_MANIFEST_PROSPECTIVE` other than `{}` at any commit of the round, or `_MANIFEST_BASELINE`
    differing from the base's — **fails the placement contract**, both forms, these lines being
    outside the owned regions and inside the historical budget.
26. A name matching `_GR1_(BASE|SEALED_HEAD|MERGE)` — **fails `SI-3`'s standing contract**.
27. `R7-GR1`'s chronology asked of the synthetic merge `HEAD` on a pull request — **fails closed**,
    as `_rbr_target_commit` already does.
27a. In `EXECUTION`, a real head whose history from the base contains a merge commit every one of
    whose commits descends from the base — **fails** on execution shape with ancestry passing, and
    the printed verdict names shape; fixtures F2a, F3, F7 and F12 are the instances.
28. The old predicate extracted from the working tree instead of the pinned blob — **fails
    `GR1-2`'s extraction control**: the extracted text must hash to the pinned function text.
29. `gr1-tagmap.json` with a base column carrying any verdict other than `PASS`, a head column
    differing from the live verdicts of the same tags, either column missing a pre-existing tag
    or carrying `R7-GR1`, or the live tag set at `E` differing from the ninety-two plus `R7-GR1` —
    **fails `GR1-3`**.
30. The result note claiming that `RD2` is repaired, withdrawn or no longer recorded — **fails the
    content contract** that names `RD2` as history.
31. The result note omitting stage 2's recorded failure set, or recording a set other than the two
    artifact contracts — **fails the content contract** on the checkpoint record.

## What no outcome of this round licenses

1. Any change to a historical `B`, `E`, `L` or `P`, or to any preregistration, amendment, result
   note or seal record of any round, act 28's and act 29's included.
2. Any statement about act 29's verdicts, its outcome vector, its review findings or whether its
   head certifies; and any push to act 29's branch, merge of `main` into it, or edit of any file
   on it.
3. Any edit of `verification/ROADMAP.md`: act 28's entry is read, never written, and act 29's
   entry is act 29's to land.
4. Any reading of `RD2` as an error in act 28 or in act 29: it is the correct verdict of a
   contract that was written before the convention it collides with, recorded by the round that
   met it.
5. Any claim that the repaired predicate is the right contract for **every** later `P0` entry:
   it validates act 28's entry and tolerates successors; each successor's own guard validates its
   own entry, as `R7-PRA`'s does.
6. Any writing of a legacy seal constant, a manifest record or a prospective declaration by this
   round.
7. Any retrofit. Every historical `B`, `E`, `L`, `P` stays exactly where it is.
8. Any weakening of `R7-PFR` beyond the one leg retired: the actual-cell read, the unique sentence,
   the anchor order, the attached complete clause and the document-wide sentence count are kept
   and measured.
9. Any reuse of the baseline exception by a later round: it is owned here for this round alone.

## Hazards

**H1 — a repair that is too loose.** A predicate that tolerates successors could also tolerate a
mutation of act 28's entry hidden behind one. The twenty reject rows, ten of them on top of a
successor, are the bound, and rows 21 and 22 of the negative suite show two natural weakenings
each caught by a named row.

**H2 — the landing identified too early or too widely, and ancestry mistaken for shape.** A
merge whose non-first parent descends from `B` is not necessarily this round's landing: a branch
cut from `B` satisfies ancestry, a stage-2 parent carries the block without the artifacts, and the
merge GitHub creates on the pull request carries `L` itself as a non-first parent. Conditions
(a)–(d) and the uniqueness requirement are the discriminator, and fixtures F3, F5, F7, F8 and F12
exercise each exclusion. Separately, act 10's strengthened check is an ancestry check and not a
shape check: it passes any merge all of whose commits descend from the base, so a head that
absorbed a later `main` cut after `B`, or a merge of two such branches, is refused by the
execution-shape condition and by nothing else; F2a is the instance, and the two verdicts are
printed apart so that a failure names its cause.

**H3 — the concurrent execution.** Act 29's head is sealed against change and its pull request
must build a candidate merge with `main` after `L`. The two-regime placement contract exists for
this: the whole-file form is exact only while this round alone has touched the guard since `B`,
and after landing it would reject every tree carrying act 29's lines; so after landing the budget
is measured historically against `E` and only the owned regions and protected artifacts are
checked live. The head's guard file differs from the base's only inside `_pfr_road_ok`'s body
(lines 27963–27979 at `D`) and by a block appended after line 31213 at `D`, both more than twenty
unchanged lines from every line act 29's execution changed (10116, 10125, and the insertion
between 28222 and 28225). A textual conflict at act 29's candidate merge would nonetheless be a
fact about that merge, verified there, and not a claim this freeze makes; what this freeze fixes is
that nothing in this round's diff reaches those lines.

**H4 — the base run's environment.** `SI-2` recorded two wrong forms of "run the base's guard at
the base" before the right one. `GR1-3` uses the third form as `SI3-7` did: a detached temporary
worktree at `B`, no `GIT_DIR`, pull-request variables removed, the base's own file, run once by the
execution and persisted. A base column that is not all `PASS` is a finding about the environment
before it is a finding about anything else, and the round stops on it.

**H5 — the name.** The bare token `GR1` is a substring of act 26's `_CGR1`. Every name this round
introduces carries the stem with a leading underscore or a hyphenated prefix, and the whole-word
check at `D` is the freedom fact.

**H6 — a stage skipped, or a checkpoint misread.** Stage 2's dry run is expected red on exactly two
named contracts; a stage-2 run red on anything else, or green, is a stage that did not do what the
table says, and stage 3 does not begin on it. Stage 3's tag map is written from stage 2's run, so a
stage 3 committed on top of an untaken stage-2 dry run has no head column to write.

**H7 — the baseline exception read as a precedent, or as sufficient.** The retained declaration
is act 28's, kept because writing that line is what a concurrent execution must not collide with.
It protects thirty-two records and not `PFR.json`'s content; the protection of every record at `B`
during the round is `R7-GR1`'s whole-tree integrity contract, and fixture F11 measures that
contract on a mutated, a removed and an added record. The subsection *The baseline* ends the
exception with this round. Non-licence 9 exists for this.

## Start state, pinned

| path | blob at `D` |
| --- | --- |
| `verification/lean/edge_rigidity_probe.py` | `5e2c36c30c2e231bc726741bd522ec051b657391` |
| `verification/ROADMAP.md` | `d0658c99b6ef13d984fd533760393c0b4a2e43c7` |
| `verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/preregistration.md` | `9e1b05bb39ce0c4ade7df38d21b2b947f8aa9011` |
| `verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/result.md` | `c445c5cef9ba01bd5271e90fe988297e0786b097` |
| `verification/seals/PFR.json` | `d09a24ff68958a19f57d4ba07f3c94263820dc83` |
| `verification/programmes/oi-qm/track-b/act-29-product-admission/preregistration.md` | `5451a52d87d7d2ab2aac48802bb80898d81f6a16` |
| `verification/lean-mathlib/OIBridge/ProductLocusFreedom.lean` | `325c09a180366765ae4d742b752099d3b219d3c9` |
| `AGENTS.md` | `a9687b39c69973d35a2ff81c257687071fd35eca` |
| `verification/seals/` (tree) | `92e0956ad6b187fddf77068f33c66e69a012f074`, thirty-three records, twenty-seven `sealed` and six `base-only` |
| `verification/seals/` (tree at `101b8ceb…`, act 28's base) | thirty-two records, no `PFR.json`; the tree at `D` is exactly these plus `PFR.json` |

### What must have merged before the execution begins, checkable mechanically

Each row below names its scope — at `D`, at `B`, or from `D` to `B` — and the block after the table
is the machine-checkable form of the same rows, which the release gate lints and the workflow's
`control-plane-base-check` job evaluates in mode `M` against the candidate merge of this pull
request and, after the merge, in mode `B` against the actual merge commit.

| # | scope | precondition | mechanical check |
| --- | --- | --- | --- |
| 1 | `D` | The names were free when chosen | `git grep -l -- 'R7-GR1' D`, `'_GR1'`, `-w 'GR1'`, `'round-gr-1'`, `'roadmap-entry-scoping'`, `'gr1_'` and `'gr1-tagmap'` each return nothing |
| 2 | `D` | The seals tree at `D` is the pinned one | `git rev-parse D:verification/seals` is `92e0956ad6b187fddf77068f33c66e69a012f074` |
| 3 | `D` | The guard at `D` is green | ninety-two `R7-*` tags, all `PASS`, on push run 35566401811 of `D` |
| 4 | `D → B` | `D` is an ancestor of `B` | `git merge-base --is-ancestor D B` succeeds |
| 5 | `D → B` | The blobs this round consumes are unchanged | each path of the `frozen-blob` lines below has at `B` the blob named; in particular the guard file and the ROADMAP are byte-identical to `D`'s, so the superseded text and the `act-28-alone` fixture are what was measured; the seals tree at `B` is `D`'s |
| 6 | `B` | No `GR-1` execution object exists | the guard file at `B` contains no `R7-GR1`, no `_GR1` and no `_gr1_`; no `verification/seals/GR1.json`; the round directory holds nothing but `preregistration.md` and, if any, `amendments/amendment-*.md` |
| 7 | `B` | No round declares at `B`, and the retained baseline is act 28's | the guard file at `B` carries `_MANIFEST_PROSPECTIVE = {}` and `_MANIFEST_BASELINE = {'base': '101b8cebb140c2ee7b982641ff005b84bbf0a1cf', 'authorized': ('PFR',)}` |
| 8 | `B` | Act 28 is sealed at `B` and its guard reads the superseded leg | `verification/seals/PFR.json` at `B` is the pinned record; the guard file at `B` carries `check('R7-PFR'` and the superseded final line `return n.count(p0) == 1 and n.count(_pfr_n(_PFR_ROAD_STANDING)) == 1` verbatim |
| 9 | `B` | Act 29 has not landed at `B` | the guard file at `B` contains no `R7-PRA` and no `_PRA`; no `verification/seals/PRA.json`; no `verification/lean-mathlib/OIBridge/ProductAdmission.lean`; act 29's round directory holds nothing but its control-plane files — so that the repair lands before act 29 and act 29's candidate merge is the one this freeze reasons about |
| 10 | `B` | This control plane is in the tree at its path | `verification/infrastructure/round-gr-1-roadmap-entry-scoping/preregistration.md` exists at `B`; its blob is the one the `R7-GR1` clause pins, which the execution's first act verifies by `git hash-object` and the block cannot state of itself |
| 11 | `B` | The retained baseline is extensionally `B`'s whole seals tree | the record set at `B` equals the record set at `101b8ceb…` plus `PFR.json`, entry for entry with identical blobs: `git diff --name-status` between the two trees is exactly one added line, `PFR.json` |

**No sibling lane's merge is a precondition of this round**, and the execution does not wait for
one. Act 29's pull request is not an input; its state after `L` is act 29's to measure.

```control-plane-preconditions
d: 0bedff07fc1ad2675ecab205c8836e7a90a113d4
merged: false
frozen-blob: verification/lean/edge_rigidity_probe.py 5e2c36c30c2e231bc726741bd522ec051b657391
frozen-blob: verification/ROADMAP.md d0658c99b6ef13d984fd533760393c0b4a2e43c7
frozen-blob: verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/preregistration.md 9e1b05bb39ce0c4ade7df38d21b2b947f8aa9011
frozen-blob: verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/result.md c445c5cef9ba01bd5271e90fe988297e0786b097
frozen-blob: verification/seals/PFR.json d09a24ff68958a19f57d4ba07f3c94263820dc83
frozen-blob: verification/programmes/oi-qm/track-b/act-29-product-admission/preregistration.md 5451a52d87d7d2ab2aac48802bb80898d81f6a16
frozen-blob: verification/lean-mathlib/OIBridge/ProductLocusFreedom.lean 325c09a180366765ae4d742b752099d3b219d3c9
frozen-blob: AGENTS.md a9687b39c69973d35a2ff81c257687071fd35eca
# row 1: name freedom, a drafting-time fact
{"id": "d1-tag-free", "scope": "D", "check": "git grep -l -- 'R7-GR1' $D", "expect": "empty"}
{"id": "d1-stem-free", "scope": "D", "check": "git grep -l -- '_GR1' $D", "expect": "empty"}
{"id": "d1-bare-word-free", "scope": "D", "check": "git grep -l -w -- 'GR1' $D", "expect": "empty"}
{"id": "d1-dir-free", "scope": "D", "check": "git grep -l -- 'round-gr-1' $D", "expect": "empty"}
{"id": "d1-dir-suffix-free", "scope": "D", "check": "git grep -l -- 'roadmap-entry-scoping' $D", "expect": "empty"}
{"id": "d1-helper-prefix-free", "scope": "D", "check": "git grep -l -- 'gr1_' $D", "expect": "empty"}
{"id": "d1-tagmap-free", "scope": "D", "check": "git grep -l -- 'gr1-tagmap' $D", "expect": "empty"}
# row 2: the seals tree at D
{"id": "d2-seals-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/seals)\" = 92e0956ad6b187fddf77068f33c66e69a012f074", "expect": "exit0"}
# row 4: provenance
{"id": "db4-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
# row 5, the tree half: the seals tree is unchanged from D to B
{"id": "db5-seals-tree", "scope": "D->B", "check": "test \"$(git rev-parse $REF:verification/seals)\" = 92e0956ad6b187fddf77068f33c66e69a012f074", "expect": "exit0"}
# row 6: no execution object; the names occur in this file, so the guard, the seals and the tree are read directly and never through git grep
{"id": "b6-guard-clean", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e 'R7-GR1' -e '_GR1' -e '_gr1_'", "expect": "empty"}
{"id": "b6-no-record", "scope": "B", "check": "git ls-tree --name-only $REF verification/seals/ | grep -e 'GR1.json'", "expect": "empty"}
{"id": "b6-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-gr-1-roadmap-entry-scoping/ | grep -v -e '/preregistration.md$' -e '/amendments/amendment-[0-9][0-9]*.md$'", "expect": "empty"}
# row 7: no round declares at B; the retained baseline is act 28's
{"id": "b7-no-prospective", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e '^_MANIFEST_PROSPECTIVE = {}$'", "expect": "nonempty"}
{"id": "b7-baseline-pfr", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"^_MANIFEST_BASELINE = {'base': '101b8cebb140c2ee7b982641ff005b84bbf0a1cf', 'authorized': ('PFR',)}$\"", "expect": "nonempty"}
# row 8: act 28 sealed and its guard carrying the superseded leg
{"id": "b8-pfr-sealed", "scope": "B", "check": "git show $REF:verification/seals/PFR.json | tr -d ' \\n' | grep -e '\"round\":\"PFR\",\"kind\":\"sealed\",\"base\":\"101b8cebb140c2ee7b982641ff005b84bbf0a1cf\",\"sealed_head\":\"47192f150ed5e94affc7d00e6aca839e3fd461cf\",\"merge\":\"4de9777d3cdd949c798beb4a6487dfbf6da6ae4b\"'", "expect": "nonempty"}
{"id": "b8-pfr-guard", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"check('R7-PFR'\"", "expect": "nonempty"}
{"id": "b8-superseded-leg-present", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -F -e '    return n.count(p0) == 1 and n.count(_pfr_n(_PFR_ROAD_STANDING)) == 1'", "expect": "nonempty"}
# row 9: act 29 not landed at B
{"id": "b9-no-pra-guard", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e 'R7-PRA' -e '_PRA'", "expect": "empty"}
{"id": "b9-no-pra-record", "scope": "B", "check": "git ls-tree --name-only $REF verification/seals/ | grep -e 'PRA.json'", "expect": "empty"}
{"id": "b9-no-pra-module", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/lean-mathlib/ | grep -e 'ProductAdmission'", "expect": "empty"}
{"id": "b9-act29-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/programmes/oi-qm/track-b/act-29-product-admission/ | grep -v -e '/preregistration.md$' -e '/amendments/amendment-[0-9][0-9]*.md$'", "expect": "empty"}
# row 10: this control plane at its path
{"id": "b10-self-present", "scope": "B", "check": "git cat-file -e $REF:verification/infrastructure/round-gr-1-roadmap-entry-scoping/preregistration.md", "expect": "exit0"}
# row 11: the retained baseline is extensionally B's whole seals tree: the two listings differ by exactly the PFR.json line
{"id": "b11-baseline-extensional", "scope": "B", "check": "git diff --name-status 101b8cebb140c2ee7b982641ff005b84bbf0a1cf $REF -- verification/seals/ | grep -v -x -e \"$(printf 'A\\tverification/seals/PFR.json')\"", "expect": "empty"}
{"id": "b11-pfr-added", "scope": "B", "check": "git diff --name-status 101b8cebb140c2ee7b982641ff005b84bbf0a1cf $REF -- verification/seals/ | grep -x -e \"$(printf 'A\\tverification/seals/PFR.json')\"", "expect": "nonempty"}
```

## The guard

Fresh tag **`R7-GR1`**, stem **`_GR1_`** / **`_gr1_`** for its own names and **no legacy-shaped
name**: nothing matching `_GR1_(BASE|SEALED_HEAD|MERGE)` exists at any commit of the round. It
carries this preregistration pinned **by blob** at this path with a one-byte drift control; the
chronology rule stated above, in its three states, with ancestry and execution shape as separate
printed verdicts, the canonical-landing definition and the lifecycle fixtures F1–F13; the
whole-tree integrity contract of *The baseline* in its execution and landed forms; the locating
controls; `GR1-1`'s byte comparison and two-regime placement contract; `GR1-2`'s twenty-nine-row
differential suite with the old predicate extracted from the pinned blob and the extraction
hashed; `GR1-3`'s reading of `gr1-tagmap.json` with the live equality of the head column; the
history contract in its checkpoint form, a valid prefix during execution and the complete
three-commit chain at `E` and after; and content
contracts holding the result note to the distinctions this freeze makes, each mutation-tested and
each pinned to its complete content: the round's shape as **non-sealing, `E` → `L`, no `P`, no
record, no declaration, no baseline change under the owned exception**; the sentence that
`GR1.json` is owed to a later round that names it; the supersession table as the authorization,
naming one retired leg and no other; **`RD2` named as history, in act 29's record, neither
repaired nor withdrawn**; the twenty-nine-row table verbatim with the seven
reject / accept rows called the defect reproduced; the stage-2 checkpoint's failure set recorded
verbatim as the two artifact contracts; the sentence that act 28's verdicts, artifacts and seal
record are unchanged at the pinned blobs; the sentence that no ROADMAP, Lean, census or manuscript
file is edited; the sentence that act 29's verdicts are not read and not reported; the three
definition slots reported as unused; and the wall-clock of the one base run recorded.

## The landing shape

`E` → `L`, on the execution pull request, under `§A.37` as amended by `SI3-6`, with no `P`:

- **`E`** is the stage-3 commit, certified by exact-head continuous integration: the ordinary
  pull-request build, whose guard asks its question of the real `pull_request.head.sha`.
- **`L`** has current green `main` as its first parent and exactly `E` as its second, and is the
  canonical landing under conditions (a)–(d). It writes nothing: no record, no declaration change,
  no baseline change, no seals change. At `L` the guard classifies the round `LANDED-UNRECORDED`
  with `E` recovered as `L`'s non-first parent, and every later tree is classified the same way
  until `GR1.json` exists. The merge GitHub creates when the pull request merges is not a landing;
  `L` is found inside its history.
- **There is no `P`.** A pin commit on this round would pin nothing.
- Full continuous integration must pass again on exact `L` before the pull request merges, and the
  resulting `main` push run must be green before any later round's landing — act 29's included —
  is constructed.
- **The record, afterwards.** The first round whose preregistration is written after `L` names
  `verification/seals/GR1.json`, `{"round": "GR1", "kind": "base-only", "base": <this round's
  mandated base>}`, as an authorized manifest addition, and its baseline admits the stem under the
  ordinary rule. Act 29's frozen control plane predates `L` and does not name it, so act 29's
  landing adds no such record, and act 29's baseline `{'base': <act 29's base>, 'authorized':
  ('PRA',)}` holds at act 29's `L` and `P` with the seals tree it expects.

## What this round expects of act 29's certification, stated as a reading and not as a target

After `L` is on `main`, act 29's pull request builds its candidate merge from current `main` and
its unchanged head. That tree carries the repaired `_pfr_road_ok`, so `R7-PFR` reads act 29's
ROADMAP entry as a tolerated successor and passes; it carries `R7-GR1`, which on that build finds
`L` on the base branch tip, classifies the round `LANDED-UNRECORDED`, applies the landed form of
the placement contract, and passes without asking act 29's head to descend from a base it
predates; and it carries act 29's own `_MANIFEST_BASELINE`, `_MANIFEST_PROSPECTIVE` and `R7-PRA`
lines unmerged with anything, since this round touched none of them and added no record. Whether
that build's four jobs pass is measured there, on the real checkout with the real head SHA, by act
29's lifecycle; this freeze reasons about it so that nothing in this round's diff can be the
reason it does not.

## Chronology

The execution branches from the mandated base and from no other commit, and certifies that
ancestry in act 10's strengthened form — the base an ancestor of the head, and every commit of
`rev-list HEAD ^base` a descendant of the base, recovery included, fail-closed, asked of the real
pull-request head — in the bootstrap form, from the literal `_GR1_B` inside its own guard block,
and never through the prospective declaration, which stays `{}` at every commit of the round.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative**, and the path this file sits at is pinned with it.
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect, each repeating the `M`-then-`B` certification and
  each becoming the new `B`.
- The execution never absorbs later `main` before certification: no merge from `main`, no rebase,
  no amend, no force-push.
- An execution that diverges from this freeze **records the discrepancy** and does not repair the
  freeze.
- The landing is `E` → `L` on the execution pull request, and the merge of that pull request
  happens only on explicit owner direction naming the exact head.
