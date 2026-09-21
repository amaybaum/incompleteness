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

## What `GR-1` is, and what it deliberately is not

**`GR-1` repairs one contract of one closed guard.** Act 28's guard `R7-PFR` gates the `P0` row of
`verification/ROADMAP.md` through one predicate, `_pfr_road_ok`. Two of that predicate's legs are
written over the **whole document** rather than over act 28's entry: the final line requires the
frozen act 28 sentence to occur exactly once in the file **and the standing clause to occur exactly
once in the file**, and the adjacency leg requires the text after act 28's sentence to *begin* with
the standing clause. Act 29's control plane (#704, frozen at `D`) requires act 29's execution to
append act 29's own frozen `P0` sentence after act 28's, **followed by the same standing clause**.
A ROADMAP carrying both entries therefore carries the clause twice, the document-wide count fails,
and `R7-PFR` goes red on any act 29 head — for a reason that has nothing to do with act 28's
mathematics, act 28's artifacts or act 29's result. Act 29's execution measured exactly this on its
pull request (#705, head `bf7e96fef8135525e752fb0daba0a082cf10ed44`) and recorded it as its
discrepancy `RD2`, repairing nothing, as its freeze requires.

The two contracts are jointly unsatisfiable as written, and neither closed round may edit the
other's. Under `§A.37` a contract is changed only by a round that **owns the change prospectively**.
This is that round. It owns exactly one change: **`_pfr_road_ok` is rewritten from a document-wide
clause count to validation of act 28's own entry** — act 28's unique frozen sentence, inside the
actual `P0` cell, after act 27's anchor, with the complete standing clause attached immediately
after it, once — so that a successor round's entry, which necessarily reuses the standing clause,
is outside the bound and neither counted nor accepted in act 28's place.

**`GR-1` is NON-SEALING**, `E` → `L`, no `P`. It creates no seal state and alters none. It writes
no manifest record, no prospective declaration and no baseline change, for the reason stated in the
next section.

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
block between `R7-PFR`'s `check(...)` and the `R7-SI1` banner. So:

| object | during execution | at `L` | afterwards |
| --- | --- | --- | --- |
| the mandated execution base | carried **inside `R7-GR1`'s own block** as the literal the chronology clause reads; act 10's strengthened check is asked of the real head against it | unchanged | unchanged until the record exists |
| `_MANIFEST_PROSPECTIVE` | **untouched**, `{}` at `B` and at every commit of the round | untouched | untouched |
| `_MANIFEST_BASELINE` | **untouched** | untouched | untouched |
| `verification/seals/GR1.json` | absent | **absent** | `{"round": "GR1", "kind": "base-only", "base": <B>}`, created by a later round that names it as an authorized addition, as `SI2-1` created `SI1.json` and `SI-3` created `SI2.json` |
| `R7-GR1`'s chronology verdict | `EXECUTION`: strengthened check of the real head against the base | `LANDED-UNRECORDED`: the landing named, reachable | `LANDED-UNRECORDED` until the record exists; then the keyed call `_si2_authority('GR1', tag='R7-GR1')`, `not-applicable` with the base reachable |

**The chronology rule `R7-GR1` carries, frozen.** Let the visibility targets be those
`_rbr_archive_visibility_targets` returns: the real `pull_request.head.sha` and the current tip of
the base branch as `refs/remotes/origin/<base ref>` on a pull request, `HEAD` otherwise; an
unresolvable target fails closed. Then, in this order:

1. **Recorded.** If `verification/seals/GR1.json` exists, the verdict is
   `_si2_authority('GR1', tag='R7-GR1')` and nothing else runs. The rule below is not a shadow of
   that verdict: the two never run together.
2. **Landed, unrecorded.** Otherwise, if some merge reachable from some visibility target has a
   non-first parent `p` such that `p` passes the strengthened check against the base **and** the
   guard file at `p` carries `check('R7-GR1'`, the round has landed: the verdict is `PASS`, the
   landing and the base are printed, and no ancestry question is asked of the head. The second
   conjunct is what keeps a sibling's control-plane branch cut from `B` or later — whose commits
   also descend from `B` — from being read as this round's landing.
3. **Execution.** Otherwise the verdict is `_rbr_strong_ancestry(base, real head)`: the base an
   ancestor of the head and every commit of `rev-list head ^base` a descendant of the base,
   recovery included, fail-closed, asked of the real `pull_request.head.sha` and never of the
   synthetic merge.

State 2 is what lets the repaired guard, once on `main`, run inside act 29's candidate merge without
asking act 29's head to descend from a base it predates: on that build the base branch tip carries
`L`, so the round is landed, and the clause passes for a foreign head exactly as an `ARCHIVED`
round's clause does. State 3 is the bootstrap form `§A.37` names for a round with no record. The
literal that carries the base is named `_GR1_B`, on the pattern of `_PFR_B` and every Track B
round's `_<STEM>_B`, and matches no legacy shape: nothing matching `_GR1_(BASE|SEALED_HEAD|MERGE)`
exists at any commit of the round, and `SI-3`'s standing zero holds at every head.

**This shape is the freeze's reading of `§A.37` for a non-sealing round under the retired
representation, and it is flagged for owner review as such.** If the owner prefers the prospective
path with the record written at `L`, that is an amendment before the merge, and the consequences
for act 29's candidate merge — a two-line conflict and an unauthorized addition under act 29's
frozen baseline — are the owner's to weigh.

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
the `R7-SI1` banner at line 28225; `check('R7-SI3', …)` at line 31184; the closing scope print
begins at line 31214.

**The predicate at `D`, the last five lines of which are the superseded legs:**

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
    with the complete standing clause attached immediately after it. The predicate validates that
    entry and counts nothing beyond it: a successor round's entry, which necessarily reuses the
    standing clause, is outside the bound and is neither counted nor accepted in its place.
    """
    cell = _pfr_p0_cell(road)
    if cell is None:
        return False
    c = _pfr_n(cell)
    p0 = _pfr_n(_PFR_P0)
    st = _pfr_n(_PFR_ROAD_STANDING)
    anchor = _pfr_n('with its selecting power left open.')
    if c.count(p0) != 1:                                   # unique sentence, in the actual cell
        return False
    if anchor not in c or c.index(p0) < c.index(anchor):  # after act 27's
        return False
    if c.count(p0 + ' ' + st) != 1:                        # the clause attached, complete, once
        return False
    return _pfr_n(road).count(p0) == 1                     # the sentence nowhere else in the file
```

What is kept, leg for leg: the actual-cell read through `_pfr_p0_cell`, the unique sentence in the
cell, the position after act 27's anchor, and the sentence nowhere else in the document. What
changes: the adjacency leg, which accepted any text *beginning* with the clause, becomes the
requirement that the sentence **immediately followed by the complete clause** occurs exactly once
in the cell — stricter on truncation and on in-cell duplication than the leg it replaces — and the
document-wide count of the **standing clause** is removed, being the leg that a successor entry
cannot satisfy. Nothing else in the function's text differs from the block above, byte for byte,
and `GR1-1` measures that.

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
| each of the ten mutations, on `act-28-alone` | reject | reject |
| each of the ten mutations, on `act-29-frozen-sentence-5` | reject | reject |

Twenty-eight rows. The seven **reject / accept** rows are the defect and its repair, in one table:
the old predicate rejecting every successor form is `RD2` reproduced from the pinned text, and the
execution reports that reproduction in the same words. At `D` the fixture
`act-29-frozen-sentence-5` is byte-identical to `verification/ROADMAP.md` at #705's head, blob
`f26f7c1c8d275539bccb21d6faa2e882abc6dcf8` — a drafting-time observation about an uncertified
head, recorded here for the reader and gating nothing.

## The objects `GR-1` builds

**`R1` — the predicate**, above, in place of the old body, same name, same call sites.

**`R2` — the guard `R7-GR1`**, one block appended after `check('R7-SI3', …)` and before the
closing scope print, and nowhere else. It carries: this preregistration pinned by blob at this
path with a one-byte drift control; the locating controls of `GR1-0`; the byte comparison of
`GR1-1`; the differential suite of `GR1-2` with both predicates; the verdict-map contract of
`GR1-3`; the chronology rule above; the placement contract that the head's guard file differs from
the base's **only** inside `_pfr_road_ok`'s body and by the appended `R7-GR1` block, measured by
reverting exactly those two regions and requiring byte equality with the pinned blob; and the
content contracts on the result note listed under *The guard*. No definition, no Lean, no
manifest record.

**`R3` — the result note**, `result.md` in this round's directory, and **`gr1-tagmap.json`**
beside it: the tag-to-verdict map of the base's guard file run at `B` in a detached temporary
worktree with every git and pull-request environment variable removed, exactly as `SI2-6`(a) and
`SI3-7` run their bases, paired with the head's map at `E`. The base run is taken **once**, by the
execution at `E`, and persisted; `R7-GR1` does not re-run the base's file on every build. The
nested cost `SI-3` accepted is not added to by this round, and the reason is recorded: the
evidence a base run gives here — that every pre-existing tag returns the same verdict at `E` — is
a fact about `E`, fixed once `E` is fixed, and the persisted artifact is pinned by blob from `L`
on, as `SI-1`'s and `SI-2`'s tag maps are.

**Three definition slots** are budgeted, one per object; test code and mutation controls are not
definition slots. Unused slots are recorded as unused.

## The order is part of the contract, and the final head is the checkpoint

| stage | target | what it does | may not begin until |
| --- | --- | --- | --- |
| 1 | `GR1-1` | **one commit:** `_pfr_road_ok`'s body replaced by the frozen text; nothing else in the file changes. The stage's dry run has every tag `PASS`, `R7-PFR` included, on the ROADMAP at `B` | the base-blob check of this file at `B` |
| 2 | `GR1-2` | **one commit:** the `R7-GR1` block appended, carrying the differential suite, the chronology rule, the pins and the placement contract | stage 1's dry run |
| 3 | `GR1-3` | the base's guard file run at `B` in a detached worktree; `gr1-tagmap.json` written with both maps; the result note written | stage 2's dry run: every tag `PASS`, `R7-GR1` included |
| — | `GR1-0` | the locating controls, measured first and reported last | — |

**Each stage is one commit, in this order.** The final head `E` carries the whole repair, and
`GR1-3`'s base column is measured at the commit that carries it.

## The targets, FROZEN

Each target names the artifact that decides it. A target is decided only by that artifact.

**`GR1-0` — locating controls.** The pinned blobs and the preconditions below hold at the mandated
base. Outcomes: `HOLD` / `DRIFTED`. `DRIFTED` stops the round.

**`GR1-1` — the predicate is the frozen one and nothing else moved.** The body of `_pfr_road_ok` at
the head equals the frozen replacement byte for byte after whitespace normalization of each line;
the head's guard file with that body reverted to the pinned text and the `R7-GR1` block removed
equals the pinned blob `5e2c36c3…` byte for byte; `_pfr_checks['roadmap']` and the seven
`road-mut:` controls are untouched and pass through the new body. Outcomes: `INSTALLED-AS-FROZEN` /
`INSTALLED-DEVIATED`.

**`GR1-2` — the differential suite.** All twenty-eight rows return the expected pair. Outcomes:
`SUITE-AS-FROZEN` / `SUITE-DEVIATED`. A deviation on a **reject / reject** row is a finding about
the replacement's tightness and stops the round; a deviation on an **accept** row of the new
predicate is a finding about its tolerance and stops the round; a deviation in the **old**
column is a finding about the extraction and stops the round. No expectation is edited to fit.

**`GR1-3` — the verdict map is preserved.** Every tag present in the base's map is present in the
head's map with the same verdict, and every verdict in both columns is `PASS`; the head's map has
exactly one tag the base's lacks, `R7-GR1`. Outcomes: `MAP-PRESERVED` / `MAP-CHANGED`.
`MAP-CHANGED` stops the round and reports; a changed verdict is never adopted as an improvement.

## The contract this round supersedes, named in advance

Under `§A.37`'s ownership rule this table is the authorization. **Nothing outside it is touched in
any closed round's guard**, and a failure outside it is a result requiring adjudication.

| guard | contract | why it is superseded | disposition |
| --- | --- | --- | --- |
| `R7-PFR` | `_pfr_road_ok`'s adjacency leg — the text after act 28's sentence *begins with* the standing clause | it accepts a truncated clause and does not bound the entry | **replaced** by the bounded-entry leg: sentence + complete clause, once, in the cell |
| `R7-PFR` | `_pfr_road_ok`'s final leg — the standing clause occurs exactly once in the whole document | a successor entry that `§A.37`'s own `P0` convention requires carries the same clause; the leg is unsatisfiable together with act 29's frozen `P0` instruction | **retired**; the document-wide count of act 28's **sentence** is kept |

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

## The negative suite

Each case must satisfy its named outcome for its named reason. Cases 1–20 are the twenty
**reject** rows of the differential suite and are listed there. In addition:

21. The frozen replacement with `c.count(p0 + ' ' + st) != 1` weakened to `st not in c` — accepts
    `standing-clause-detached` — **fails `GR1-2`**.
22. The frozen replacement with the final line dropped — accepts `p0-duplicated`, the sentence
    copied outside the cell with the cell's entry intact — **fails `GR1-2`**.
23. One byte changed anywhere in the guard file outside the two authorized regions — **fails
    `GR1-1`'s placement contract**.
24. `_MANIFEST_PROSPECTIVE` other than `{}` at any commit of the round, or `_MANIFEST_BASELINE`
    differing from the base's, or any file under `verification/seals/` differing from the base's —
    **fails `R7-GR1`'s placement contract**, and for the seals tree also `U5`.
25. A name matching `_GR1_(BASE|SEALED_HEAD|MERGE)` — **fails `SI-3`'s standing contract**.
26. `R7-GR1`'s chronology asked of the synthetic merge `HEAD` on a pull request — **fails closed**,
    as `_rbr_target_commit` already does.
27. A merge reachable from a visibility target whose non-first parent descends from the base but
    carries no `R7-GR1` — a sibling control plane cut after `B` — **does not classify the round as
    landed**; the execution check still runs.
28. The old predicate extracted from the working tree instead of the pinned blob — **fails
    `GR1-2`'s extraction control**: the extracted text must hash to the pinned function text.
29. `gr1-tagmap.json` with a base column carrying any verdict other than `PASS`, or a head column
    missing a base tag, or more than one head-only tag — **fails `GR1-3`**.
30. The result note claiming that `RD2` is repaired, withdrawn or no longer recorded — **fails the
    content contract** that names `RD2` as history.

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
8. Any weakening of `R7-PFR` beyond the two legs named: the actual-cell read, the unique sentence,
   the anchor order and the document-wide sentence count are kept and measured.

## Hazards

**H1 — a repair that is too loose.** A predicate that tolerates successors could also tolerate a
mutation of act 28's entry hidden behind one. The twenty reject rows, ten of them on top of a
successor, are the bound, and rows 21 and 22 of the negative suite show two natural weakenings
each caught by a named row.

**H2 — the landed state read too early.** A merge whose non-first parent descends from `B` is not
necessarily this round's landing: any branch cut from `B` or later satisfies the ancestry half.
The `R7-GR1`-at-the-parent conjunct is the discriminator, and negative case 27 exercises it. If the
owner judges the discriminator insufficient the amendment is to require, in addition, that the
parent's tree carry this round's result note at its path.

**H3 — the concurrent execution.** Act 29's head is sealed against change and its pull request
must build a candidate merge with `main` after `L`. The placement contract exists for this: the
head's guard file differs from the base's only inside `_pfr_road_ok`'s body (lines 27963–27979 at
`D`) and by a block appended after line 31213 at `D`, both at a distance of more than twenty
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

**H6 — a stage skipped.** Stage 2's block measures a base-versus-head difference; committed on top
of a stage 1 whose dry run was never taken it cannot say which stage moved `R7-PFR`. The dry run
named in the table is taken before the next commit exists.

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
| 5 | `D → B` | The blobs this round consumes are unchanged | each path of the `frozen-blob` lines below has at `B` the blob named; in particular the guard file and the ROADMAP are byte-identical to `D`'s, so the superseded text and the `act-28-alone` fixture are what was measured |
| 6 | `B` | No `GR-1` execution object exists | the guard file at `B` contains no `R7-GR1`, no `_GR1` and no `_gr1_`; no `verification/seals/GR1.json`; the round directory holds nothing but `preregistration.md` and, if any, `amendments/amendment-*.md` |
| 7 | `B` | No round declares at `B` | the guard file at `B` carries `_MANIFEST_PROSPECTIVE = {}` and `_MANIFEST_BASELINE = {'base': '101b8cebb140c2ee7b982641ff005b84bbf0a1cf', 'authorized': ('PFR',)}` |
| 8 | `B` | Act 28 is sealed at `B` and its guard reads the superseded legs | `verification/seals/PFR.json` at `B` is the pinned record; the guard file at `B` carries `check('R7-PFR'` and the superseded final line `return n.count(p0) == 1 and n.count(_pfr_n(_PFR_ROAD_STANDING)) == 1` verbatim |
| 9 | `B` | Act 29 has not landed at `B` | the guard file at `B` contains no `R7-PRA` and no `_PRA`; no `verification/seals/PRA.json`; no `verification/lean-mathlib/OIBridge/ProductAdmission.lean`; act 29's round directory holds nothing but its control-plane files — so that the repair lands before act 29 and act 29's candidate merge is the one this freeze reasons about |
| 10 | `B` | This control plane is in the tree at its path | `verification/infrastructure/round-gr-1-roadmap-entry-scoping/preregistration.md` exists at `B`; its blob is the one the `R7-GR1` clause pins, which the execution's first act verifies by `git hash-object` and the block cannot state of itself |

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
# row 7: no round declares at B
{"id": "b7-no-prospective", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e '^_MANIFEST_PROSPECTIVE = {}$'", "expect": "nonempty"}
{"id": "b7-baseline-pfr", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"^_MANIFEST_BASELINE = {'base': '101b8cebb140c2ee7b982641ff005b84bbf0a1cf', 'authorized': ('PFR',)}$\"", "expect": "nonempty"}
# row 8: act 28 sealed and its guard carrying the superseded legs
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
```

## The guard

Fresh tag **`R7-GR1`**, stem **`_GR1_`** / **`_gr1_`** for its own names and **no legacy-shaped
name**: nothing matching `_GR1_(BASE|SEALED_HEAD|MERGE)` exists at any commit of the round. It
carries this preregistration pinned **by blob** at this path with a one-byte drift control; the
chronology rule stated above, in its three states; the locating controls; `GR1-1`'s byte
comparison and placement contract; `GR1-2`'s twenty-eight-row differential suite with the old
predicate extracted from the pinned blob and the extraction hashed; `GR1-3`'s reading of
`gr1-tagmap.json`, pinned by blob from `L`; and content contracts holding the result note to the
distinctions this freeze makes, each mutation-tested and each pinned to its complete content:
the round's shape as **non-sealing, `E` → `L`, no `P`, no record, no declaration, no baseline
change**; the sentence that `GR1.json` is owed to a later round that names it; the supersession
table as the authorization, naming the two legs and no other; **`RD2` named as history, in act
29's record, neither repaired nor withdrawn**; the twenty-eight-row table verbatim with the seven
reject / accept rows called the defect reproduced; the sentence that act 28's verdicts, artifacts
and seal record are unchanged at the pinned blobs; the sentence that no ROADMAP, Lean, census or
manuscript file is edited; the sentence that act 29's verdicts are not read and not reported; the
three definition slots reported as unused; and the wall-clock of the one base run recorded.

## The landing shape

`E` → `L`, on the execution pull request, under `§A.37` as amended by `SI3-6`, with no `P`:

- **`E`** is the final head after stage 3, certified by exact-head continuous integration: the
  ordinary pull-request build, whose guard asks its question of the real `pull_request.head.sha`.
- **`L`** has current green `main` as its first parent and exactly `E` as its second. It writes
  nothing: no record, no declaration change, no baseline change. At `L` the guard classifies `GR1`
  as landed and unrecorded, and every descendant of `L` is classified the same way until
  `GR1.json` exists.
- **There is no `P`.** A pin commit on this round would pin nothing.
- Full continuous integration must pass again on exact `L` before the pull request merges, and the
  resulting `main` push run must be green before any later round's landing — act 29's included —
  is constructed.
- **The record, afterwards.** The first round whose preregistration is written after `L` names
  `verification/seals/GR1.json`, `{"round": "GR1", "kind": "base-only", "base": <this round's
  mandated base>}`, as an authorized manifest addition, and its baseline admits the stem. Act 29's
  frozen control plane predates `L` and does not name it, so act 29's landing adds no such record,
  and act 29's baseline `{'base': <act 29's base>, 'authorized': ('PRA',)}` holds at act 29's `L`
  and `P` with the seals tree it expects.

## What this round expects of act 29's certification, stated as a reading and not as a target

After `L` is on `main`, act 29's pull request builds its candidate merge from current `main` and
its unchanged head. That tree carries the repaired `_pfr_road_ok`, so `R7-PFR` reads act 29's
ROADMAP entry as a tolerated successor and passes; it carries `R7-GR1`, which on that build finds
`L` on the base branch tip and passes without asking act 29's head to descend from a base it
predates; and it carries act 29's own `_MANIFEST_BASELINE`, `_MANIFEST_PROSPECTIVE` and `R7-PRA`
lines unmerged with anything, since this round touched none of them and added no record. Whether
that build's four jobs pass is measured there, on the real checkout with the real head SHA, by act
29's lifecycle; this freeze reasons about it so that nothing in this round's diff can be the
reason it does not.

## Chronology

The execution branches from the mandated base and from no other commit, and certifies that
ancestry in act 10's strengthened form — the base an ancestor of the head, and every commit of
`rev-list HEAD ^base` a descendant of the base, recovery included, fail-closed, asked of the real
pull-request head — in the bootstrap form, from a literal inside its own guard block, and never
through the prospective declaration, which stays `{}` at every commit of the round.

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
