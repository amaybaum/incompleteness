# Guard repair round GR-2 — scoping `R7-GR1`'s declaration contract to `GR-1`'s own history: PREREGISTRATION

`GR-2` is a guard repair round. It owns one change to one closed round's contract: the two checks
by which `R7-GR1` asserts the declaration values `GR-1` did not move. Those checks read the live
module's globals in every lifecycle state, so they assert of every later tree a condition only
`GR-1`'s own commits can satisfy. The repair keeps the assertion exactly where it belongs — at
`GR-1`'s own commits — and reads it from `GR-1`'s recovered history once the round has landed.

Nothing else in `R7-GR1` changes. No other round's contract is touched, no manuscript is edited,
no Lean file is edited, no seal record is written, and no pinned artifact moves.

***

## The commit vocabulary this freeze uses, fixed first

Per `§A.37`:

- **`D`** — the drafting snapshot, `645df36974331330e99132015f6f3be550fbe64f`. Every measurement
  below marked *at `D`* was taken against that commit, which is `main` carrying `GR-1`'s landing.
- **`B`** — the mandated execution base: the certified merge commit on `main` of this control
  plane. Before that merge exists `B` has no SHA, and this freeze assigns none.
- **`M`** — a candidate merge continuous integration may construct before this control plane
  lands, to test `B`-scoped conditions in advance. Predictive test state only, never ancestry.
- **`E`** — the sealed execution head. **`L`** — the landing merge, first parent current green
  `main`, second parent exactly `E`. There is no `P`.

Where `GR-1`'s own commits are named, they are named as such: `GR-1`'s base
`39090ca75860e7e6cbd99fa6f3ad859cee3efaf4`, its sealed head `E_GR1 =
8d08f8c913f4bb9ef413114ecceb2f72d72d8213`, its landing `L_GR1 =
13ffc7372d52c16bdb0e24935aa617deb67e7c51`, and the `main` merge that brought it in, `D` itself.

***

## What `GR-2` is, and what it deliberately is not

`R7-GR1` carries, at `D`, three statements outside its lifecycle split:

```python
_gr1_checks['prospective-untouched'] = _MANIFEST_PROSPECTIVE == {}
_gr1_checks['baseline-untouched'] = _MANIFEST_BASELINE == {
    'base': '101b8cebb140c2ee7b982641ff005b84bbf0a1cf', 'authorized': ('PFR',)}
```

`_MANIFEST_PROSPECTIVE` and `_MANIFEST_BASELINE` are the guard file's two declaration lines. Under
`§A.37` as amended by `SI3-6`, a round declares its own integrity baseline, and a sealing round
carries its mandated base in the prospective declaration while it executes and removes that entry
at `P`. Both lines therefore move with the current round, by protocol. The two statements above
compare them against `GR-1`'s own execution-time values at whatever tree the guard runs on, in
every state the chronology reports.

`GR-1`'s freeze scopes the intended guarantee to `GR-1`'s own commits and says so in terms: the
integrity contract holds "at every commit of the round up to `E`"; at `L` "the seals tree equals
the first parent's tree"; after landing, "additions by later rounds are outside this round's
historical scope"; and "the exception ends with this round. The next round to declare — the one
that adds `GR1.json`, or any later one — declares its own baseline under the ordinary rule."
The implemented comparison carries none of that scope. `GR-2` is the round that gives it that
scope, and it owns exactly that.

**What `GR-2` is not.** It is not a Track B round and states nothing about any round's
mathematics. It is not a repair of `GR-1`'s substantive contract: the `_pfr_road_ok` scoping
`GR-1` installed stands unchanged and is not re-argued here. It does not weaken the contract it
repairs — the execution-time assertion survives verbatim, and after landing it becomes a statement
about immutable history, which is strictly harder to satisfy by accident than a statement about a
tree the current round controls. It does not read, report, or depend on act 29's verdicts. It does
not write a manifest record, and `GR1.json` remains owed to a later round that names it.

***

## The round's shape, declared first, in `§A.37`'s terms

**`GR-2` is NON-SEALING**, `E` → `L`, no `P`. It creates no seal state and alters none. It writes
no manifest record and no prospective declaration.

**The baseline: the same narrow exception, owned here.** `§A.37` says each round declares its own
integrity baseline. `GR-2` does **not**: `_MANIFEST_BASELINE` stays act 28's declaration,
`{'base': '101b8cebb140c2ee7b982641ff005b84bbf0a1cf', 'authorized': ('PFR',)}`, at every commit of
this round, and `_MANIFEST_PROSPECTIVE` stays `{}`. The reason is the one `GR-1` recorded and this
round must respect for the same head: that line is one of the two act 29's execution already
writes, and a concurrent write to it from this branch would collide textually with a sealed head
that may not move. The licence is this subsection, which replaces what the ordinary rule would
have guaranteed with the same substitute `GR-1` used:

- **What the retained declaration guarantees.** Under act 28's declaration `U5` holds the
  thirty-two records it names against mutation, removal and any addition other than `PFR`. It does
  not hold `PFR.json`'s content, and this freeze does not claim it does.
- **What closes the gap.** `R7-GR2`'s own integrity contract: the set of `(stem, content)` pairs
  under `verification/seals/` in the working tree equals the set at `B`, read from git, byte for
  byte — zero additions, zero mutations, zero removals — at every commit of this round up to `E`,
  and at `L` the seals tree equals the first parent's. That, and not the retained declaration, is
  what protects every record at `B` while this round runs.
- **`R7-GR2`'s own declaration contract is written scoped from the start.** It asserts the retained
  values on the live tree while `GR-2` is `EXECUTION`, and on the guard file at `GR-2`'s own
  recovered `E` and `L` thereafter — the same two regimes this round installs in `R7-GR1`. A
  repair that reproduced the defect it repairs would be refused by its own fixtures.
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
   against `_GR2_B`, this clause in its guard file, and both stage-3 artifacts; unique or
   fail-closed; `E` is that parent.
4. **The question is asked of the real `pull_request.head.sha`** and of the live base-branch tip,
   never of the synthetic merge commit; an unresolvable target fails closed.
5. **The guard recovers whatever history it needs itself** and fails if recovery fails.

***

## The superseded contract and its replacement, stated as text and not as prose

**Superseded.** The three lines quoted above, as they stand at `D` at lines 31778–31780 of
`verification/lean/edge_rigidity_probe.py`, are pinned by content:

- `sha256` of that exact three-line segment at `D`:
  `9c1493dbab4b81f46a685ea71fcef8e52af50c3509cda4139c8e76630e6ee6a7`
- the segment runs from the start of the line beginning `_gr1_checks['prospective-untouched']`
  through the end of the first line thereafter containing `'authorized': ('PFR',)}`
- each of the two keys occurs exactly once in the file at `D`

The execution extracts the segment from the **base's own guard text**, read from git, and requires
that hash before it changes anything. A drift of one byte fails the round rather than rewriting a
different contract than the one reviewed.

**The replacement.** Four objects, and no other edit inside the `R7-GR1` region:

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
    table at both; an unrecoverable `e` or `l` leaves the verdicts to the state, `RECORDED`
    alone passing, which is how this block already handles an unrecoverable head."""
```

4. The two call sites, inside the existing lifecycle split and with the two keys unchanged, so the
   failure vocabulary a reader of the log already knows is preserved.

Every other statement of `R7-GR1` — its chronology, its placement budget, its owned-region check,
its landed-pin and landed-artifact families, its suite, its fixtures, its seals contract, its
check message — is unchanged, and the execution demonstrates that mechanically rather than
asserting it.

***

## The differential acceptance suite, FROZEN

Executed over the **old** predicate, reconstructed from the base's own guard text with its
extraction hashed, and the **new** one. Each row names the state and the required verdict of each
side. Rows 1–4 are the states that exist today; rows 5–9 are synthetic.

| # | state | declarations at the tree | declarations at `E_GR1`/`L_GR1` | old | new |
|---|---|---|---|---|---|
| 1 | `EXECUTION` | `GR-1`'s | — | accept | accept |
| 2 | `EXECUTION` | a successor's | — | reject | reject |
| 3 | `LANDED-UNRECORDED` | `GR-1`'s | `GR-1`'s | accept | accept |
| 4 | `LANDED-UNRECORDED` | act 29's, both lines | `GR-1`'s | **reject** | **accept** |
| 5 | `LANDED-UNRECORDED` | a successor's baseline only | `GR-1`'s | reject | accept |
| 6 | `LANDED-UNRECORDED` | a successor's prospective only | `GR-1`'s | reject | accept |
| 7 | `LANDED-UNRECORDED` | `GR-1`'s | mutated baseline at `E` | accept | **reject** |
| 8 | `LANDED-UNRECORDED` | `GR-1`'s | mutated prospective at `L` | accept | **reject** |
| 9 | `LANDED-UNRECORDED` | anything | `E` unrecoverable | accept | reject |

Row 4 is the state act 29's candidate merge is in, and the row the round exists for. Rows 7 and 8
are why the repair is not a deletion: the assertion survives, against history. Row 9 is the
fail-closed leg. Rows 1 and 2 are the execution regime, preserved verbatim.

***

## The objects `GR-2` builds

1. The four objects of the replacement, inside the `R7-GR1` region of
   `verification/lean/edge_rigidity_probe.py`.
2. `R7-GR2`, a new guard block, bounded by markers assembled from pieces so that the bounds are
   not themselves occurrences of the markers.
3. `verification/infrastructure/round-gr-2-declaration-scoping/result.md`.
4. `verification/infrastructure/round-gr-2-declaration-scoping/gr2-tagmap.json`.

Nothing else. No Lean file, no manuscript, no ROADMAP row, no census entry, no seal record, no
edit to `AGENTS.md`.

***

## The order is part of the contract, with the checks that apply at each checkpoint

- **`GR2-1` — the repair.** The four objects of the replacement, and nothing else. At this
  checkpoint the guard runs with `R7-GR1` green in `LANDED-UNRECORDED`, the base-blob and
  superseded-segment hashes verified, and the emitted tag set equal to the base's.
- **`GR2-2` — the guard block.** `R7-GR2` with its contracts, its differential suite and its
  fixtures. At this checkpoint `R7-GR2` is the round's sole failure and its failure set is exactly
  the two artifact contracts, the result note and the tag map not yet existing.
- **`GR2-3` — the artifacts.** The result note and the tag map, committed together. This commit is
  the candidate `E`, and the checkpoint is fully green.

Each checkpoint is run with `HEAD` fixed for the whole run, the stage committed first, and `HEAD`
and the dirty-file count logged at the start and the end.

***

## The targets, FROZEN

- **`GR2-0`** — the start state holds at `B`: the superseded segment is present with its frozen
  hash, `GR-1` is `LANDED-UNRECORDED` with `E_GR1` and `L_GR1` recoverable, the seals tree is
  `92e0956ad6b187fddf77068f33c66e69a012f074`, and the declarations at `B` are act 28's.
  Outcomes: `HOLD` / `DEVIATED`.
- **`GR2-1`** — the replacement is installed and the differential suite's nine rows each return
  their required pair of verdicts. Outcomes: `SUITE-AS-FROZEN` / `SUITE-DEVIATED`.
- **`GR2-2`** — `R7-GR1` is unchanged outside the superseded segment: the file at `E`, with the
  `R7-GR2` block removed and the segment reverted to the base's text, equals the base's guard file
  byte for byte. Outcomes: `BUDGET-HELD` / `BUDGET-EXCEEDED`.
- **`GR2-3`** — the verdict map is preserved: the base's own guard file is run, every tag it emits
  returns the same verdict at this head, and the head emits exactly one tag the base does not,
  `R7-GR2`. Outcomes: `MAP-PRESERVED` / `MAP-MOVED`.

The measured cardinalities are recorded in the result note; the rule above governs, and a
cardinality that differs from the prediction below is recorded as a discrepancy rather than
repaired into agreement.

***

## Predictions, with strength

1. **Strong.** At `B` the four `GR2-0` conditions hold.
2. **Strong.** The differential suite returns the frozen verdicts in all nine rows; in particular
   row 4 separates old from new, which is the round's reason to exist.
3. **Strong.** The budget holds: the round's whole diff to the guard file is the superseded
   segment's replacement and the `R7-GR2` block.
4. **Moderate.** The base emits 93 tags and the head 94. The rule, not the number, governs.
5. **Moderate.** With `GR-2` landed, a fresh `pull_request` build of act 29's unchanged head
   against `main` has `R7-GR1` green in `LANDED-UNRECORDED`, joining `R7-PFR` and `R7-PRA`, both
   of which passed on the candidate merge measured in run `35636948285`. This is a reading of what
   the repair implies, not a target of this round: act 29's certification is act 29's, and this
   round neither reports nor depends on it.

***

## Lifecycle and declaration fixtures, FROZEN

On synthetic repositories built with `commit-tree`, so parent order is exact, run on every build:

- **G1** — the execution regime is preserved: with the round `EXECUTION`, `GR-1`'s live values pass
  and a successor's fail.
- **G2** — the successor case: `GR-1` landed, a later round has changed both declarations on the
  tree, the history at `E`/`L` intact; the verdicts pass. This is the positive fixture, and it
  reproduces the state act 29's candidate merge is in.
- **G3** — the successor case, one line at a time: baseline changed alone, prospective changed
  alone; both pass.
- **G4** — mutation of history fails: the baseline at `E` altered, the prospective at `L` altered,
  each a separate fixture; both fail.
- **G5** — fail-closed: an unrecoverable `E`, an unparsable source, a name assigned twice, a value
  that is not a literal; each fails rather than skipping.
- **G6** — the reader reads history and not the process: with the live globals set to values that
  would pass and a history that would not, the verdict follows the history.
- **G7** — non-vacuity: the frozen table does not equal the successor values used in `G2`, so `G2`
  is not passing by coincidence of equal dictionaries.

***

## The negative suite

Each case must fail, and for its named reason: a replacement that drops the execution regime
entirely; a replacement that reads `l` and not `e`; a replacement that accepts `None` from the
reader; a replacement whose reader takes the first of two assignments rather than refusing; a
replacement that compares the *text* of the declaration lines rather than their values, which a
reformatting would break and which this freeze does not adopt; a budget that tolerates an edit
elsewhere in the `R7-GR1` region; a `_GR2_(BASE|SEALED_HEAD|MERGE)` name, which `SI-3`'s standing
contract forbids.

***

## What no outcome of this round licenses

- It does not license reading `GR-1`'s substantive `_pfr_road_ok` contract as re-opened.
- It does not license a conclusion about act 29's targets, its outcome vector, or its landing.
- It does not license treating `GR1.json` as written, nor `GR-1` as `RECORDED`.
- It does not license a later round changing a landed round's contract without its own freeze.

***

## Hazards

1. **Reproducing the defect.** A repair that asserted the new condition on the live tree in some
   other guise would fail the same way one round later. `G2`, `G3` and `G6` are the controls.
2. **Weakening instead of scoping.** Deleting the checks would pass every build and protect
   nothing. `G4` and rows 7–8 of the suite are the controls: a mutated history must still fail.
3. **The concurrent line.** Declaring this round's own baseline would put a second writer on a line
   act 29's sealed head already writes. The freeze forbids it and precondition rows check the
   declarations at `B` and at every stage.
4. **The pinned-artifact family, named and left alone.** `R7-GR1`'s `landed-pin:` checks assert six
   pinned blobs — among them `AGENTS.md` and `OIBridge/ProductLocusFreedom.lean` — on the *current*
   tree in every state after landing. They are of the same family as the defect repaired here: an
   execution-time invariant left running against the live head. They are **out of this round's
   scope by this freeze**, and this round therefore edits none of those six paths. A round that
   needs to edit one of them owns that change prospectively, as this round owns this one.
5. **The token `GR2` at `D`.** The whole word occurs at `D` in exactly two files, both as a quoted
   synthetic value in `GR-1`'s malformed-record fixture and the table that freezes it. It is not an
   identifier and not a stem in use, and this round writes no record, so the fixture's synthetic
   "wrong round" value keeps its meaning.

***

## Start state, pinned

Measured at `D`, read from git:

| path | blob at `D` |
|---|---|
| `verification/lean/edge_rigidity_probe.py` | `9c3a1b6aea01a691d0f8299672905b1a330994db` |
| `verification/seals` (tree) | `92e0956ad6b187fddf77068f33c66e69a012f074` |

`GR-1`'s frozen artifacts, act 28's and act 29's artifacts, `verification/seals/PFR.json`,
`verification/ROADMAP.md` and `AGENTS.md` are not pinned again here: they are pinned by `R7-GR1`,
which this round leaves in force, and this round edits none of them.

### Name freedom, at `D`

`R7-GR2`, `_GR2`, `round-gr-2`, `declaration-scoping`, `gr2_` and `gr2-tagmap` each return nothing
at `D`. The bare word `GR2` returns exactly two files, as hazard 5 records.

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
{"id": "d1-dir-suffix-free", "scope": "D", "check": "git grep -l -- 'declaration-scoping' $D", "expect": "empty"}
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
{"id": "b4-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-gr-2-declaration-scoping/ | grep -v -e '/preregistration.md$'", "expect": "empty"}
{"id": "b4-no-record", "scope": "B", "check": "git ls-tree --name-only $REF verification/seals/ | grep -e 'GR2.json'", "expect": "empty"}
# row 5: the superseded segment is present at B, with its frozen hash, and each key occurs once
{"id": "b5-segment-hash", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | sed -n '/^_gr1_checks\\['\"'\"'prospective-untouched'\"'\"'\\]/,/authorized.: (.PFR.,)}/p' | sha256sum | cut -d' ' -f1 | grep -x '9c1493dbab4b81f46a685ea71fcef8e52af50c3509cda4139c8e76630e6ee6a7'", "expect": "nonempty"}
{"id": "b5-prospective-key-once", "scope": "B", "check": "test \"$(git show $REF:verification/lean/edge_rigidity_probe.py | grep -c \"_gr1_checks\\['prospective-untouched'\\]\")\" = 1", "expect": "exit0"}
{"id": "b5-baseline-key-once", "scope": "B", "check": "test \"$(git show $REF:verification/lean/edge_rigidity_probe.py | grep -c \"_gr1_checks\\['baseline-untouched'\\]\")\" = 1", "expect": "exit0"}
# row 6: the declarations at B are act 28's, which this round retains
{"id": "b6-prospective-empty", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -x \"_MANIFEST_PROSPECTIVE = {}\"", "expect": "nonempty"}
{"id": "b6-baseline-act28", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -x \"_MANIFEST_BASELINE = {'base': '101b8cebb140c2ee7b982641ff005b84bbf0a1cf', 'authorized': ('PFR',)}\"", "expect": "nonempty"}
# row 7: GR-1 is landed and unrecorded at B, with its history present
{"id": "b7-gr1-clause-present", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"check('R7-GR1'\"", "expect": "nonempty"}
{"id": "b7-gr1-no-record", "scope": "B", "check": "git ls-tree --name-only $REF verification/seals/ | grep -e 'GR1.json'", "expect": "empty"}
{"id": "b7-gr1-landing-reachable", "scope": "B", "check": "git merge-base --is-ancestor 13ffc7372d52c16bdb0e24935aa617deb67e7c51 $REF", "expect": "exit0"}
{"id": "b7-gr1-sealed-head-reachable", "scope": "B", "check": "git merge-base --is-ancestor 8d08f8c913f4bb9ef413114ecceb2f72d72d8213 $REF", "expect": "exit0"}
{"id": "b7-gr1-landing-second-parent", "scope": "B", "check": "test \"$(git rev-parse 13ffc7372d52c16bdb0e24935aa617deb67e7c51^2)\" = 8d08f8c913f4bb9ef413114ecceb2f72d72d8213", "expect": "exit0"}
# row 8: GR-1's declarations in its own history are the frozen ones, which the repair will read
{"id": "b8-decls-at-gr1-e", "scope": "B", "check": "git show 8d08f8c913f4bb9ef413114ecceb2f72d72d8213:verification/lean/edge_rigidity_probe.py | grep -x \"_MANIFEST_PROSPECTIVE = {}\"", "expect": "nonempty"}
{"id": "b8-decls-at-gr1-l", "scope": "B", "check": "git show 13ffc7372d52c16bdb0e24935aa617deb67e7c51:verification/lean/edge_rigidity_probe.py | grep -x \"_MANIFEST_PROSPECTIVE = {}\"", "expect": "nonempty"}
# row 9: this control plane at its path
{"id": "b9-self-present", "scope": "B", "check": "git ls-tree --name-only $REF verification/infrastructure/round-gr-2-declaration-scoping/preregistration.md", "expect": "nonempty"}
```

***

## The guard

`R7-GR2` carries, each contract mutation-tested:

1. **The frozen blob.** This file at this path, pinned by blob with a one-byte drift control,
   fail-closed.
2. **The superseded segment.** Extracted from the base's own guard text, hashed, and equal to the
   frozen hash.
3. **The replacement is installed**, and the differential suite's nine rows return their frozen
   verdicts, the old side reconstructed from the base's text rather than retyped.
4. **The budget.** This file, with the `R7-GR2` block removed and the segment reverted to the
   base's, equals the base's guard file — whole-file while executing, and after landing measured
   against the recovered `E`, so a sibling round's changes elsewhere in the file are not this
   round's to answer for.
5. **The chronology**, as frozen above, with ancestry and execution shape separated and reported.
6. **The seals tree** is byte-identical to the base's while the round runs.
7. **The declarations**, this round's own, in the two regimes this round installs.
8. **No legacy-shaped name**: nothing matching `_GR2_(BASE|SEALED_HEAD|MERGE)` at any commit.
9. **No record**: `GR2` is absent from the manifest.
10. **The verdict map**: the base's guard file is run, its tags all return the same verdict here,
    and exactly one tag is new.
11. **The fixtures** `G1`–`G7` and the negative suite.

***

## The landing shape

`E` → `L`, on the execution pull request, under `§A.37` as amended by `SI3-6`, with no `P`:

- **`E`** is the `GR2-3` commit, certified by exact-head continuous integration.
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
