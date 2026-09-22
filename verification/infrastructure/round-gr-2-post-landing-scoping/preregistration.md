# Guard repair round GR-2 — scoping `R7-GR1`'s live-tree assertions to `GR-1`'s own history: PREREGISTRATION

`GR-2` is a guard repair round. It owns **two separately named supersessions** of one closed
round's contract, both of the same defect: an execution-time assertion left running against
whatever tree the guard later finds.

- **`S1`** — the two checks by which `R7-GR1` asserts the declaration values `GR-1` did not move.
- **`S2`** — the `landed-pin:` family, which asserts six pinned blobs on the current tree in every
  state after landing, three of them outside the live-tree scope `GR-1`'s own freeze fixes.

The common question is what remains a **live-tree obligation after the originating round has
landed**: `S1` corrects the declaration scope imposed on later trees, `S2` corrects which pinned
artifacts stay live and which become historical-only. Both keep their assertions and move them to
the history that can satisfy them. Nothing else in `R7-GR1` changes: its chronology, its owned-region check, its landed-artifact family, its
differential suite, its budget, its seals contract and its check message stand. No manuscript, no
Lean file, no ROADMAP row, no census entry, no seal record.

***

## The commit vocabulary this freeze uses, fixed first

Per `§A.37`:

- **`D`** — the drafting snapshot, `645df36974331330e99132015f6f3be550fbe64f`: `main` carrying
  `GR-1`'s landing. Every measurement marked *at `D`* was taken against that commit.
- **`B`** — the mandated execution base: the certified merge commit on `main` of this control
  plane. Before that merge exists `B` has no SHA, and this freeze assigns none.
- **`M`** — a candidate merge continuous integration may construct before this control plane
  lands, to test `B`-scoped conditions in advance. Predictive test state only, never ancestry.
- **`E`** — the sealed execution head. **`L`** — the landing merge, first parent current green
  `main`, second parent exactly `E`. There is no `P`.

`GR-1`'s own commits are named as such: its base `39090ca75860e7e6cbd99fa6f3ad859cee3efaf4`, its
sealed head `E_GR1 = 8d08f8c913f4bb9ef413114ecceb2f72d72d8213`, its landing `L_GR1 =
13ffc7372d52c16bdb0e24935aa617deb67e7c51`, and the `main` merge that brought it in, `D` itself.

***

## What `GR-2` is, and what it deliberately is not

### `S1`: the declaration contract

`R7-GR1` carries, at `D`, three statements outside its lifecycle split:

```python
_gr1_checks['prospective-untouched'] = _MANIFEST_PROSPECTIVE == {}
_gr1_checks['baseline-untouched'] = _MANIFEST_BASELINE == {
    'base': '101b8cebb140c2ee7b982641ff005b84bbf0a1cf', 'authorized': ('PFR',)}
```

`_MANIFEST_PROSPECTIVE` and `_MANIFEST_BASELINE` are the guard file's two declaration lines. Under
`§A.37` as amended by `SI3-6`, a round declares its own integrity baseline, and a sealing round
carries its mandated base in the prospective declaration while it executes, removing that entry at
`P`. Both lines therefore move with the current round, by protocol. The two statements above
compare them against `GR-1`'s execution-time values at whatever tree the guard runs on, in every
state the chronology reports.

`GR-1`'s freeze scopes the intended guarantee to `GR-1`'s own commits in terms — the integrity
contract holds "at every commit of the round up to `E`"; at `L` "the seals tree equals the first
parent's tree"; after landing, "additions by later rounds are outside this round's historical
scope"; and "the exception ends with this round. The next round to declare — the one that adds
`GR1.json`, or any later one — declares its own baseline under the ordinary rule." The implemented
comparison carries none of that scope.

### `S2`: the pinned-artifact family

`R7-GR1` carries, at `D`, inside the post-landing branch:

```python
    for _p, _b in sorted(_GR1_PINS.items()):
        if _p == _GR1_GUARD_PATH or _p == _GR1_ROAD_PATH:
            continue
        _gr1_checks['landed-pin:' + _p] = (
            (_gr1_git('rev-parse', 'HEAD:%s' % _p) or b'').decode().strip() == _b)
```

`_GR1_PINS` is introduced in the block as "the start state the freeze pins at `D` and requires at
`B`". Minus the guard and the ROADMAP, which have their own specialized contracts, the loop
asserts six blobs on the **current tree**, in every state after landing:

| path | class |
|---|---|
| act 28's `preregistration.md` | protected |
| act 28's `result.md` | protected |
| `verification/seals/PFR.json` | protected |
| act 29's `preregistration.md` | start state only |
| `verification/lean-mathlib/OIBridge/ProductLocusFreedom.lean` | start state only |
| `AGENTS.md` | start state only |

The classification is not this freeze's invention. `GR-1`'s own placement contract fixes the
post-landing live-tree scope and names its members:

> *In `LANDED-UNRECORDED` and `RECORDED`*: … on the current tree only the **owned regions and the
> protected artifacts** are checked — `_pfr_road_ok`'s live body equals the frozen text under
> per-line whitespace normalization; this preregistration, `result.md` and `gr1-tagmap.json` are
> at their paths with the blobs they have at `E`; act 28's preregistration, result note and
> `PFR.json` are at their pinned blobs.

The frozen live-tree set is therefore the owned region, `GR-1`'s own three artifacts — implemented
as `placement-owned-region` and the `landed-artifact:` family — and act 28's three protected
artifacts. The other three paths are start state at `B`, and the same passage anticipates later
rounds changing other material. Requiring them of every later tree **exceeds the scope `GR-1`
froze**, and would forbid any future edit to `AGENTS.md`, to act 28's shared Lean module, or to
act 29's preregistration, for as long as the block stands.

### What `GR-2` is not

It is not a Track B round and states nothing about any round's mathematics. It does not reopen
`GR-1`'s substantive `_pfr_road_ok` scoping. It does not weaken either contract: every assertion
survives, moved to history, which is immutable and so harder to satisfy by accident than a tree
the current round controls. It does not read, report or depend on act 29's verdicts. It writes no
manifest record, and `GR1.json` remains owed to a later round that names it.

***

## The round's shape, declared first, in `§A.37`'s terms

**`GR-2` is NON-SEALING**, `E` → `L`, no `P`. It creates no seal state and alters none. It writes
no manifest record and no prospective declaration.

**The baseline: the same narrow exception, owned here.** `§A.37` says each round declares its own
integrity baseline. `GR-2` does **not**: `_MANIFEST_BASELINE` stays act 28's declaration,
`{'base': '101b8cebb140c2ee7b982641ff005b84bbf0a1cf', 'authorized': ('PFR',)}`, at every commit of
this round, and `_MANIFEST_PROSPECTIVE` stays `{}`. The reason is the one `GR-1` recorded and this
round must respect for the same head: that line is one of the two act 29's execution already
writes, and a concurrent write from this branch would collide textually with a sealed head that
may not move. The licence is this subsection, which replaces what the ordinary rule would have
guaranteed with the same substitute `GR-1` used:

- **What the retained declaration guarantees.** Under act 28's declaration `U5` holds the
  thirty-two records it names against mutation, removal and any addition other than `PFR`. It does
  not hold `PFR.json`'s content, and this freeze does not claim it does.
- **What closes the gap.** `R7-GR2`'s own integrity contract: the set of `(stem, content)` pairs
  under `verification/seals/` in the working tree equals the set at `B`, read from git, byte for
  byte — zero additions, zero mutations, zero removals — at every commit of this round up to `E`,
  and at `L` the seals tree equals the first parent's.
- **`R7-GR2`'s own contracts are written scoped from the start.** Its declaration contract runs in
  the two regimes `S1` installs, and it pins no path on a later tree that it does not also require
  of its own history. A repair that reproduced either defect would be refused by its own fixtures.
- **The exception ends with this round.** The next round to declare declares its own baseline under
  the ordinary rule, and this subsection authorizes nothing for it.

**There is no `P`.** A pin commit on this round would pin nothing.

***

## The chronology rule `R7-GR2` carries, FROZEN

Identical in form to `GR-1`'s, against this round's own base:

1. **Three states.** `EXECUTION` while no landing of this round is visible; `LANDED-UNRECORDED`
   once a canonical landing is; `RECORDED` once `GR2.json` exists, which this round does not write.
2. **Ancestry and execution shape are separate questions**, each reported: act 10's strengthened
   check against `_GR2_B` does not refuse a merge whose every commit descends from the base, and
   shape does.
3. **A canonical landing** is a merge one of whose non-first parents has execution shape, ancestry
   against `_GR2_B`, this clause in its guard file, and both stage-4 artifacts; unique or
   fail-closed; `E` is that parent.
4. **The question is asked of the real `pull_request.head.sha`** and of the live base-branch tip,
   never of the synthetic merge commit; an unresolvable target fails closed.
5. **The guard recovers whatever history it needs itself** and fails if recovery fails.

***

## `S1` — the superseded contract and its replacement, stated as text and not as prose

**Superseded.** The three lines quoted above, at lines 31778–31780 of
`verification/lean/edge_rigidity_probe.py` at `D`, pinned by content:

- `sha256` of that exact three-line segment at `D`:
  `9c1493dbab4b81f46a685ea71fcef8e52af50c3509cda4139c8e76630e6ee6a7`
- the segment runs from the start of the line beginning `_gr1_checks['prospective-untouched']`
  through the end of the first line thereafter containing `'authorized': ('PFR',)}`
- each of the two keys occurs exactly once in the file at `D`

The execution extracts the segment from the **base's own guard text**, read from git, and requires
that hash before it changes anything.

**The replacement.** Four objects, and no other edit to the region:

1. A frozen table naming the two declarations and the values `GR-1` carried:

```python
_GR1_DECL_NAMES = ('_MANIFEST_PROSPECTIVE', '_MANIFEST_BASELINE')
_GR1_DECL_FROZEN = {
    '_MANIFEST_PROSPECTIVE': {},
    '_MANIFEST_BASELINE': {'base': '101b8cebb140c2ee7b982641ff005b84bbf0a1cf',
                           'authorized': ('PFR',)},
}
```

2. A historical reader, which never consults this process's own globals:

```python
def _gr1_decls(rev, cwd=None):
    """The two declaration values as the guard file at `rev` carries them, read from git and
    parsed from that historical source. Module-level assignments only, so a quoted occurrence
    elsewhere is not a declaration. None when git could not answer, when the source does not
    parse, when either name is assigned twice, or when either value is not a literal -- and
    every caller treats None as a failure."""
```

3. A verdict function carrying both regimes, so each is exercisable on a synthetic repository:

```python
def _gr1_decl_verdicts(state, e, l, live, cwd=None):
    """{'prospective-untouched': bool, 'baseline-untouched': bool}.

    While the round is EXECUTION the values are read from `live`, the running module's own
    declarations, exactly as the superseded statements did. In every other state they are read
    from the guard file at the round's recovered `e` and `l` and required to equal the frozen
    table at both; an unrecoverable `e` or `l` fails closed."""
```

4. The two call sites, inside the existing lifecycle split and with the two keys unchanged, so the
   failure vocabulary a reader of the log already knows is preserved.

***

## `S2` — the superseded contract and its replacement, stated as text and not as prose

**Superseded.** The five-line loop quoted above, at lines 31812–31816 at `D`, pinned by content:

- `sha256` of that exact segment at `D`:
  `26c4c7c6a8727e23a2547305205d045ff88090b2bff7d122f80dd46f2cc1369e`
- the segment runs from the line `    for _p, _b in sorted(_GR1_PINS.items()):`, which occurs
  once in the file at `D`, through the end of the first line thereafter containing
  `.decode().strip() == _b)`

**The replacement.** Two objects, and no other edit to the region:

1. The live-tree set, named from the freeze's own sentence:

```python
# The three artifacts GR-1's placement contract checks on the CURRENT tree after landing. The
# other pinned paths are that freeze's start state at B, and the same passage anticipates later
# rounds changing other material, so they are required of this round's history and not of a
# later tree.
_GR1_PIN_LIVE = (
    'verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/preregistration.md',
    'verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/result.md',
    'verification/seals/PFR.json',
)
```

2. A per-path verdict function, replacing the loop body:

```python
def _gr1_pin_ok(path, blob, e, l, cwd=None):
    """The pin contract, by class, for one pinned path.

    EVERY pinned path must carry its pinned blob in this round's own history: at the recovered
    `e` and at the recovered `l`. An unrecoverable revision, an absent path and a git that
    cannot answer all fail. The three paths in _GR1_PIN_LIVE must carry it at the resolved head
    as well, which is the live leg the freeze fixes; the live leg reads the same revision the
    superseded loop read, and this round does not change that resolution."""
```

The loop keeps its shape, its exclusions and **all six `landed-pin:<full path>` key identities**;
only the verdict changes, and only by class. The pinned values themselves are untouched.

**Measured at `D`, so the historical leg is known satisfiable**: all six paths carry their pinned
blobs at `E_GR1`, at `L_GR1` and at `D`. `GR-1`'s execution touched the guard file and its own
round directory and nothing else, which is what the budget contract already established.

***

## The differential acceptance suites, FROZEN

Both suites execute the **old** predicate, reconstructed from the base's own guard text with its
extraction hashed, against the **new** one. Each row names the state, the configuration and the
required verdict of each side.

### Suite A — the declaration contract

| # | state | declarations at the tree | at `E_GR1`/`L_GR1` | old | new |
|---|---|---|---|---|---|
| A1 | `EXECUTION` | `GR-1`'s | — | accept | accept |
| A2 | `EXECUTION` | a successor's | — | reject | reject |
| A3 | `LANDED-UNRECORDED` | `GR-1`'s | `GR-1`'s | accept | accept |
| A4 | `LANDED-UNRECORDED` | act 29's, both lines | `GR-1`'s | **reject** | **accept** |
| A5 | `LANDED-UNRECORDED` | a successor's baseline only | `GR-1`'s | reject | accept |
| A6 | `LANDED-UNRECORDED` | a successor's prospective only | `GR-1`'s | reject | accept |
| A7 | `LANDED-UNRECORDED` | `GR-1`'s | mutated baseline at `E` | accept | **reject** |
| A8 | `LANDED-UNRECORDED` | `GR-1`'s | mutated prospective at `L` | accept | **reject** |
| A9 | `LANDED-UNRECORDED` | anything | `E` unrecoverable | accept | reject |

`A4` is the state act 29's candidate merge is in. `A7` and `A8` are why the repair is not a
deletion. `A9` is the fail-closed leg.

### Suite B — the pinned-artifact family

| # | path | at the current tree | at `E_GR1`/`L_GR1` | old | new |
|---|---|---|---|---|---|
| B1 | protected, each of the three | pinned | pinned | accept | accept |
| B2 | protected, each of the three | changed | pinned | reject | **reject** |
| B3 | `AGENTS.md` | changed | pinned | **reject** | **accept** |
| B4 | `OIBridge/ProductLocusFreedom.lean` | changed | pinned | **reject** | **accept** |
| B5 | act 29's `preregistration.md` | changed | pinned | **reject** | **accept** |
| B6 | protected, each of the three | pinned | mutated at `E` | accept | **reject** |
| B7 | historical-only, each of the three | pinned or changed | mutated at `L` | accept | **reject** |
| B8 | any | any | `E` or `L` unrecoverable | accept | reject |

`B3`–`B5` are the three paths the freeze does not protect live, each exercised individually.
`B2` is the half that must not be weakened. `B6` and `B7` are why this is a scoping and not a
deletion: history remains asserted for all six.

### The composition row

| # | configuration | new |
|---|---|---|
| C1 | `LANDED-UNRECORDED`; both declarations changed to act 29's **and** one historical-only path changed, with `E_GR1`/`L_GR1` intact | **accept**, on both contracts at once |

`C1` is required because two repairs that each pass alone can still fail together — a shared
recovery of `E` and `L`, a shared fail-closed path, or a state split evaluated twice. `C1`
measures the composition rather than inferring it.

***

## The objects `GR-2` builds

1. `S1`'s four objects and `S2`'s two, inside the `R7-GR1` region of
   `verification/lean/edge_rigidity_probe.py`.
2. `R7-GR2`, a new guard block, bounded by markers assembled from pieces so that the bounds are
   not themselves occurrences of the markers.
3. `verification/infrastructure/round-gr-2-post-landing-scoping/result.md`.
4. `verification/infrastructure/round-gr-2-post-landing-scoping/gr2-tagmap.json`.

Nothing else. No Lean file, no manuscript, no ROADMAP row, no census entry, no seal record, and no
edit to any of the six pinned paths — including `AGENTS.md`, whose live pin this round retires but
does not exercise.

***

## The order is part of the contract, with the checks that apply at each checkpoint

- **`GR2-1` — `S1`.** The declaration replacement, and nothing else. The guard runs with `R7-GR1`
  green in `LANDED-UNRECORDED`, the base-blob and both superseded-segment hashes verified, and the
  emitted tag set equal to the base's.
- **`GR2-2` — `S2`.** The pin replacement, and nothing else. Same checkpoint conditions.
- **`GR2-3` — the guard block.** `R7-GR2` with its contracts, both suites, the fixtures and the
  composition row. At this checkpoint `R7-GR2` is the round's sole failure and its failure set is
  exactly the two artifact contracts, the result note and the tag map not yet existing.
- **`GR2-4` — the artifacts.** The result note and the tag map, committed together. This commit is
  the candidate `E`, and the checkpoint is fully green.

Each checkpoint is run with `HEAD` fixed for the whole run, the stage committed first, and `HEAD`
and the dirty-file count logged at the start and the end.

***

## The targets, FROZEN

- **`GR2-0`** — the start state holds at `B`: both superseded segments are present with their
  frozen hashes, `GR-1` is `LANDED-UNRECORDED` with `E_GR1` and `L_GR1` recoverable, all six
  pinned paths carry their pinned blobs at `E_GR1` and `L_GR1`, the seals tree is
  `92e0956ad6b187fddf77068f33c66e69a012f074`, and the declarations at `B` are act 28's.
  Outcomes: `HOLD` / `DEVIATED`.
- **`GR2-1`** — suite A's nine rows each return their required pair of verdicts.
  Outcomes: `SUITE-A-AS-FROZEN` / `SUITE-A-DEVIATED`.
- **`GR2-2`** — suite B's eight rows each return their required pair of verdicts, and `C1` holds.
  Outcomes: `SUITE-B-AS-FROZEN` / `SUITE-B-DEVIATED`.
- **`GR2-3`** — `R7-GR1` is unchanged outside the two superseded segments: the file at `E`, with
  the `R7-GR2` block removed and both segments reverted to the base's text, equals the base's
  guard file byte for byte. Outcomes: `BUDGET-HELD` / `BUDGET-EXCEEDED`.
- **`GR2-4`** — the verdict map is preserved: the base's own guard file is run, every tag it emits
  returns the same verdict at this head, and the head emits exactly one tag the base does not,
  `R7-GR2`. Outcomes: `MAP-PRESERVED` / `MAP-MOVED`.

The measured cardinalities are recorded in the result note; the rules above govern, and a
cardinality differing from the prediction below is recorded as a discrepancy rather than repaired
into agreement.

***

## Predictions, with strength

1. **Strong.** At `B` the `GR2-0` conditions hold.
2. **Strong.** Suite A returns the frozen verdicts in all nine rows; `A4` separates old from new.
3. **Strong.** Suite B returns the frozen verdicts in all eight rows; `B3`–`B5` separate old from
   new, and `B2`, `B6`, `B7` show neither half is weakened.
4. **Strong.** `C1` holds: the two repairs compose.
5. **Strong.** The budget holds: the round's whole diff to the guard file is the two segments'
   replacements and the `R7-GR2` block.
6. **Moderate.** The base emits 93 tags and the head 94. The rule, not the number, governs.
7. **Moderate.** With `GR-2` landed, a fresh `pull_request` build of act 29's unchanged head
   against `main` has `R7-GR1` green in `LANDED-UNRECORDED`, joining `R7-PFR` and `R7-PRA`, both
   of which passed on the candidate merge measured in run `35636948285`. This is a reading of what
   the repairs imply, not a target: act 29's certification is act 29's, and this round neither
   reports nor depends on it.

***

## Fixtures, FROZEN

On synthetic repositories built with `commit-tree`, so parent order is exact, run on every build.

**Declarations.**

- **G1** — the execution regime is preserved: with the round `EXECUTION`, `GR-1`'s live values pass
  and a successor's fail.
- **G2** — the successor case: `GR-1` landed, a later round has changed both declarations on the
  tree, the history at `E`/`L` intact; the verdicts pass.
- **G3** — the successor case, one line at a time: baseline changed alone, prospective changed
  alone; both pass.
- **G4** — mutation of history fails: the baseline at `E` altered, the prospective at `L` altered,
  each a separate fixture; both fail.
- **G5** — fail-closed: an unrecoverable `E`, an unparsable source, a name assigned twice, a value
  that is not a literal; each fails rather than skipping.
- **G6** — the reader reads history and not the process: with the live globals set to values that
  would pass and a history that would not, the verdict follows the history.
- **G7** — non-vacuity: the frozen table does not equal the successor values used in `G2`.

**Pins.**

- **P1** — the protected three, unchanged live and in history: each passes.
- **P2** — the protected three, changed live, history intact: each fails, separately.
- **P3** — the historical-only three, changed live, history intact: each **passes**, separately —
  `AGENTS.md`, `OIBridge/ProductLocusFreedom.lean` and act 29's preregistration, one fixture per
  path, and each fails under the superseded loop.
- **P4** — mutation of history fails, for all six: the blob at `E` altered, and separately the
  blob at `L` altered; each fails, protected and historical-only alike.
- **P5** — fail-closed: an unrecoverable `E`, an unrecoverable `L`, a path absent at `E`, a git
  that cannot answer; each fails rather than skipping.
- **P6** — non-vacuity and classification: `_GR1_PIN_LIVE` has exactly the three protected paths,
  each a key of `_GR1_PINS`; the six keys the loop emits are unchanged from the base's; and the
  guard and the ROADMAP remain excluded from the loop, under their own contracts.

**Composition.**

- **C1** — one synthetic repository in which both declarations carry act 29's values and one
  historical-only path is changed, with `E`/`L` intact: both contracts pass in the same run, and
  the superseded pair fails on both counts in that same repository.

***

## The negative suite

Each case must fail, and for its named reason: a replacement that drops the execution regime; a
replacement that reads `l` and not `e`; one that accepts `None` from either reader; one whose
reader takes the first of two assignments rather than refusing; one that compares the declaration
lines as text rather than as values, which a reformatting would break and which this freeze does
not adopt; a `_GR1_PIN_LIVE` that omits one of the three protected paths, or that admits a fourth;
a pin replacement that drops the historical leg for the protected three, or the live leg for them;
one that changes a pinned value; one that changes or drops a `landed-pin:` key identity; a budget
that tolerates an edit elsewhere in the `R7-GR1` region; a `_GR2_(BASE|SEALED_HEAD|MERGE)` name,
which `SI-3`'s standing contract forbids.

***

## What no outcome of this round licenses

- It does not license reading `GR-1`'s substantive `_pfr_road_ok` contract as re-opened.
- It does not license a conclusion about act 29's targets, its outcome vector, or its landing.
- It does not license treating `GR1.json` as written, nor `GR-1` as `RECORDED`.
- It does not license editing act 28's preregistration, its result note or `PFR.json`: those stay
  pinned live, and this round's own fixtures require that they do.
- It does not license a later round changing a landed round's contract without its own freeze.

***

## Hazards

1. **Reproducing the defect.** A repair that asserted either condition on the live tree in some
   other guise would fail the same way one round later. `G2`, `G3`, `G6`, `P3` and `C1` are the
   controls, and `R7-GR2`'s own contracts are written in the repaired form.
2. **Weakening instead of scoping.** Deleting either check would pass every build and protect
   nothing. `A7`, `A8`, `B2`, `B6`, `B7`, `G4`, `P2` and `P4` are the controls: mutated history,
   and a changed protected artifact, must still fail.
3. **Over-reading the freeze's live set.** The three protected paths are taken from `GR-1`'s
   placement contract verbatim and from nothing else. `P6` checks the set is exactly those three,
   each a pinned key, so the classification cannot drift by one path in either direction.
4. **The concurrent line.** Declaring this round's own baseline would put a second writer on a line
   act 29's sealed head already writes. The freeze forbids it, and precondition rows check the
   declarations at `B` and at every stage.
5. **Editing a retired pin in the same round that retires it.** This round edits none of the six
   pinned paths, `AGENTS.md` included. Retiring the live leg and exercising it in one round would
   make the round's own diff the evidence for its own repair.
6. **The token `GR2` at `D`.** The whole word occurs at `D` in exactly two files, both as a quoted
   synthetic value in `GR-1`'s malformed-record fixture and the table that freezes it. It is not an
   identifier and not a stem in use, and this round writes no record.

***

## Start state, pinned

Measured at `D`, read from git:

| path | blob at `D` |
|---|---|
| `verification/lean/edge_rigidity_probe.py` | `9c3a1b6aea01a691d0f8299672905b1a330994db` |
| `verification/seals` (tree) | `92e0956ad6b187fddf77068f33c66e69a012f074` |

The six pinned paths keep the blobs `R7-GR1` pins, at `E_GR1`, at `L_GR1` and at `D`; they are not
re-pinned here, since this round leaves those values in force and edits none of them.

### Name freedom, at `D`

`R7-GR2`, `_GR2`, `round-gr-2`, `post-landing-scoping`, `gr2_` and `gr2-tagmap` each return nothing
at `D`. The bare word `GR2` returns exactly two files, as hazard 6 records.

***

## Preconditions

```control-plane-preconditions
d: 645df36974331330e99132015f6f3be550fbe64f
merged: false
frozen-blob: verification/lean/edge_rigidity_probe.py 9c3a1b6aea01a691d0f8299672905b1a330994db
# row 1: name freedom, a drafting-time fact
{"id": "d1-tag-free", "scope": "D", "check": "git grep -l -- 'R7-GR2' $D", "expect": "empty"}
{"id": "d1-stem-free", "scope": "D", "check": "git grep -l -- '_GR2' $D", "expect": "empty"}
{"id": "d1-dir-free", "scope": "D", "check": "git grep -l -- 'round-gr-2' $D", "expect": "empty"}
{"id": "d1-dir-suffix-free", "scope": "D", "check": "git grep -l -- 'post-landing-scoping' $D", "expect": "empty"}
{"id": "d1-helper-prefix-free", "scope": "D", "check": "git grep -l -- 'gr2_' $D", "expect": "empty"}
{"id": "d1-tagmap-free", "scope": "D", "check": "git grep -l -- 'gr2-tagmap' $D", "expect": "empty"}
{"id": "d1-bare-word-known", "scope": "D", "check": "test \"$(git grep -l -w -- 'GR2' $D | sed 's|^[^:]*:||' | sort | tr '\\n' ',')\" = 'verification/infrastructure/round-gr-1-roadmap-entry-scoping/preregistration.md,verification/lean/edge_rigidity_probe.py,'", "expect": "exit0"}
# row 2: the seals tree at D
{"id": "d2-seals-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/seals)\" = 92e0956ad6b187fddf77068f33c66e69a012f074", "expect": "exit0"}
# row 3: provenance
{"id": "db3-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
{"id": "db3-seals-tree", "scope": "D->B", "check": "test \"$(git rev-parse $REF:verification/seals)\" = 92e0956ad6b187fddf77068f33c66e69a012f074", "expect": "exit0"}
# row 4: no execution object at B; the names occur in this file, so the guard and the tree are read directly and never through git grep
{"id": "b4-guard-clean", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e 'R7-GR2' -e '_GR2' -e '_gr2_'", "expect": "empty"}
{"id": "b4-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-gr-2-post-landing-scoping/ | grep -v -e '/preregistration.md$'", "expect": "empty"}
{"id": "b4-no-record", "scope": "B", "check": "git ls-tree --name-only $REF verification/seals/ | grep -e 'GR2.json'", "expect": "empty"}
# row 5: S1's superseded segment is present at B, with its frozen hash, and each key occurs once
{"id": "b5-segment-hash", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | sed -n '/^_gr1_checks\\['\"'\"'prospective-untouched'\"'\"'\\]/,/authorized.: (.PFR.,)}/p' | sha256sum | cut -d' ' -f1 | grep -x '9c1493dbab4b81f46a685ea71fcef8e52af50c3509cda4139c8e76630e6ee6a7'", "expect": "nonempty"}
{"id": "b5-prospective-key-once", "scope": "B", "check": "test \"$(git show $REF:verification/lean/edge_rigidity_probe.py | grep -c \"_gr1_checks\\['prospective-untouched'\\]\")\" = 1", "expect": "exit0"}
{"id": "b5-baseline-key-once", "scope": "B", "check": "test \"$(git show $REF:verification/lean/edge_rigidity_probe.py | grep -c \"_gr1_checks\\['baseline-untouched'\\]\")\" = 1", "expect": "exit0"}
# row 6: S2's superseded loop is present at B, with its frozen hash, and its head occurs once
{"id": "b6-pin-loop-hash", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | sed -n '/^    for _p, _b in sorted(_GR1_PINS.items()):/,/decode().strip() == _b)/p' | sha256sum | cut -d' ' -f1 | grep -x '26c4c7c6a8727e23a2547305205d045ff88090b2bff7d122f80dd46f2cc1369e'", "expect": "nonempty"}
{"id": "b6-pin-loop-once", "scope": "B", "check": "test \"$(git show $REF:verification/lean/edge_rigidity_probe.py | grep -c '^    for _p, _b in sorted(_GR1_PINS.items()):')\" = 1", "expect": "exit0"}
{"id": "b6-pin-live-set-free", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e '_GR1_PIN_LIVE' -e '_gr1_pin_ok' -e '_gr1_decls' -e '_gr1_decl_verdicts' -e '_GR1_DECL_FROZEN'", "expect": "empty"}
# row 7: the declarations at B are act 28's, which this round retains
{"id": "b7-prospective-empty", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -x \"_MANIFEST_PROSPECTIVE = {}\"", "expect": "nonempty"}
{"id": "b7-baseline-act28", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -x \"_MANIFEST_BASELINE = {'base': '101b8cebb140c2ee7b982641ff005b84bbf0a1cf', 'authorized': ('PFR',)}\"", "expect": "nonempty"}
# row 8: GR-1 is landed and unrecorded at B, with its history present
{"id": "b8-gr1-clause-present", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"check('R7-GR1'\"", "expect": "nonempty"}
{"id": "b8-gr1-no-record", "scope": "B", "check": "git ls-tree --name-only $REF verification/seals/ | grep -e 'GR1.json'", "expect": "empty"}
{"id": "b8-gr1-landing-reachable", "scope": "B", "check": "git merge-base --is-ancestor 13ffc7372d52c16bdb0e24935aa617deb67e7c51 $REF", "expect": "exit0"}
{"id": "b8-gr1-landing-second-parent", "scope": "B", "check": "test \"$(git rev-parse 13ffc7372d52c16bdb0e24935aa617deb67e7c51^2)\" = 8d08f8c913f4bb9ef413114ecceb2f72d72d8213", "expect": "exit0"}
# row 9: GR-1's declarations in its own history are the frozen ones, which S1's repair will read
{"id": "b9-decls-at-gr1-e", "scope": "B", "check": "git show 8d08f8c913f4bb9ef413114ecceb2f72d72d8213:verification/lean/edge_rigidity_probe.py | grep -x \"_MANIFEST_PROSPECTIVE = {}\"", "expect": "nonempty"}
{"id": "b9-decls-at-gr1-l", "scope": "B", "check": "git show 13ffc7372d52c16bdb0e24935aa617deb67e7c51:verification/lean/edge_rigidity_probe.py | grep -x \"_MANIFEST_PROSPECTIVE = {}\"", "expect": "nonempty"}
# row 10: the six pinned blobs in GR-1's own history, which S2's repair will read
{"id": "b10-a28-prereg-e", "scope": "B", "check": "test \"$(git rev-parse 8d08f8c913f4bb9ef413114ecceb2f72d72d8213:verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/preregistration.md)\" = 9e1b05bb39ce0c4ade7df38d21b2b947f8aa9011", "expect": "exit0"}
{"id": "b10-a28-prereg-l", "scope": "B", "check": "test \"$(git rev-parse 13ffc7372d52c16bdb0e24935aa617deb67e7c51:verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/preregistration.md)\" = 9e1b05bb39ce0c4ade7df38d21b2b947f8aa9011", "expect": "exit0"}
{"id": "b10-a28-result-e", "scope": "B", "check": "test \"$(git rev-parse 8d08f8c913f4bb9ef413114ecceb2f72d72d8213:verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/result.md)\" = c445c5cef9ba01bd5271e90fe988297e0786b097", "expect": "exit0"}
{"id": "b10-a28-result-l", "scope": "B", "check": "test \"$(git rev-parse 13ffc7372d52c16bdb0e24935aa617deb67e7c51:verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/result.md)\" = c445c5cef9ba01bd5271e90fe988297e0786b097", "expect": "exit0"}
{"id": "b10-pfr-json-e", "scope": "B", "check": "test \"$(git rev-parse 8d08f8c913f4bb9ef413114ecceb2f72d72d8213:verification/seals/PFR.json)\" = d09a24ff68958a19f57d4ba07f3c94263820dc83", "expect": "exit0"}
{"id": "b10-pfr-json-l", "scope": "B", "check": "test \"$(git rev-parse 13ffc7372d52c16bdb0e24935aa617deb67e7c51:verification/seals/PFR.json)\" = d09a24ff68958a19f57d4ba07f3c94263820dc83", "expect": "exit0"}
{"id": "b10-a29-prereg-e", "scope": "B", "check": "test \"$(git rev-parse 8d08f8c913f4bb9ef413114ecceb2f72d72d8213:verification/programmes/oi-qm/track-b/act-29-product-admission/preregistration.md)\" = 5451a52d87d7d2ab2aac48802bb80898d81f6a16", "expect": "exit0"}
{"id": "b10-a29-prereg-l", "scope": "B", "check": "test \"$(git rev-parse 13ffc7372d52c16bdb0e24935aa617deb67e7c51:verification/programmes/oi-qm/track-b/act-29-product-admission/preregistration.md)\" = 5451a52d87d7d2ab2aac48802bb80898d81f6a16", "expect": "exit0"}
{"id": "b10-lean-module-e", "scope": "B", "check": "test \"$(git rev-parse 8d08f8c913f4bb9ef413114ecceb2f72d72d8213:verification/lean-mathlib/OIBridge/ProductLocusFreedom.lean)\" = 325c09a180366765ae4d742b752099d3b219d3c9", "expect": "exit0"}
{"id": "b10-lean-module-l", "scope": "B", "check": "test \"$(git rev-parse 13ffc7372d52c16bdb0e24935aa617deb67e7c51:verification/lean-mathlib/OIBridge/ProductLocusFreedom.lean)\" = 325c09a180366765ae4d742b752099d3b219d3c9", "expect": "exit0"}
{"id": "b10-agents-e", "scope": "B", "check": "test \"$(git rev-parse 8d08f8c913f4bb9ef413114ecceb2f72d72d8213:AGENTS.md)\" = a9687b39c69973d35a2ff81c257687071fd35eca", "expect": "exit0"}
{"id": "b10-agents-l", "scope": "B", "check": "test \"$(git rev-parse 13ffc7372d52c16bdb0e24935aa617deb67e7c51:AGENTS.md)\" = a9687b39c69973d35a2ff81c257687071fd35eca", "expect": "exit0"}
# row 11: this round edits none of the pinned paths, so they still carry their pinned blobs at B
{"id": "b11-a28-prereg-at-b", "scope": "B", "check": "test \"$(git rev-parse $REF:verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/preregistration.md)\" = 9e1b05bb39ce0c4ade7df38d21b2b947f8aa9011", "expect": "exit0"}
{"id": "b11-agents-at-b", "scope": "B", "check": "test \"$(git rev-parse $REF:AGENTS.md)\" = a9687b39c69973d35a2ff81c257687071fd35eca", "expect": "exit0"}
# row 12: this control plane at its path
{"id": "b12-self-present", "scope": "B", "check": "git ls-tree --name-only $REF verification/infrastructure/round-gr-2-post-landing-scoping/preregistration.md", "expect": "nonempty"}
```

***

## The guard

`R7-GR2` carries, each contract mutation-tested:

1. **The frozen blob.** This file at this path, pinned by blob with a one-byte drift control,
   fail-closed.
2. **The two superseded segments.** Each extracted from the base's own guard text, hashed, and
   equal to its frozen hash.
3. **The replacements are installed**, and both suites plus the composition row return their
   frozen verdicts, the old side reconstructed from the base's text rather than retyped.
4. **The budget.** This file, with the `R7-GR2` block removed and both segments reverted to the
   base's, equals the base's guard file — whole-file while executing, and after landing measured
   against the recovered `E`, so a sibling round's changes elsewhere in the file are not this
   round's to answer for.
5. **The chronology**, as frozen above, with ancestry and execution shape separated and reported.
6. **The seals tree** is byte-identical to the base's while the round runs.
7. **The declarations**, this round's own, in the two regimes `S1` installs.
8. **The classification**, `P6`: `_GR1_PIN_LIVE` is exactly the three protected paths, the six
   `landed-pin:` key identities are the base's, and no pinned value moved.
9. **No legacy-shaped name**: nothing matching `_GR2_(BASE|SEALED_HEAD|MERGE)` at any commit.
10. **No record**: `GR2` is absent from the manifest.
11. **The verdict map**: the base's guard file is run, its tags all return the same verdict here,
    and exactly one tag is new.
12. **The fixtures** `G1`–`G7`, `P1`–`P6`, `C1` and the negative suite.

***

## The landing shape

`E` → `L`, on the execution pull request, under `§A.37` as amended by `SI3-6`, with no `P`:

- **`E`** is the `GR2-4` commit, certified by exact-head continuous integration.
- **`L`** has current green `main` as first parent and exactly `E` as second. It writes nothing:
  no record, no declaration change, no baseline change, no seals change.
- Full continuous integration must pass again on exact `L` before the pull request merges, and the
  resulting `main` build must be green before anything else lands.

***

## Execution discipline

The execution begins only from the certified merge of this control plane and from nothing else,
and its first act is to verify this file's blob at that base. It absorbs no later `main` before
`E` is certified. A divergence between this freeze and what the execution measures is **recorded
in the result note**, never repaired into agreement by editing this file.
