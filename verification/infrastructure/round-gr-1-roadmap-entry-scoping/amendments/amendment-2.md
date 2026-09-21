# Guard repair round GR-1 — AMENDMENT 2: the landed-pin loop cannot run in the landing regime

**Append-only, execution-affecting.** This amendment corrects two mechanical defects in one loop of
a contract the preregistration requires, and changes nothing else. Under `AGENTS.md` `§A.37` it is
frozen and reviewed separately, repeats the `M`-then-`B` certification, and **its certified merge
commit becomes the new mandated execution base**, from which the execution restarts. Neither the
preregistration nor Amendment 1 is edited: their blobs stay
`013ca3d75c65fd884974e7e6350b7c78924bb22b` and `631439af8682eec66a1f9ec3aaacece76d50dfb4`, and this
file sits beside them.

## The commit vocabulary

- **`D`** — this amendment's drafting snapshot, `15d08103a9c214395a0cc7948dfda3bc6858f30e`: the
  certified merge of #707, which was Amendment 1's mandated execution base and is the current state
  of `main`. Every measurement below marked "at `D`" was taken against it.
- **`B`** — the new mandated execution base: the certified merge commit on `main` of this
  amendment. **Before that merge exists `B` has no SHA, and this file assigns it none.** From that
  merge, Amendment 1's `B` is provenance and the execution never resumes from it.
- **`M`** — a candidate merge of this amendment, used to evaluate the `B`-scoped preconditions
  predictively. Test state only.

## What went wrong, measured and not narrated

The preregistration's guard clause checks, at the landing, that each pinned start-state blob is
still the pinned blob at the current head. As implemented in the second attempted execution the
loop read:

```python
for _p, _b in sorted(_GR1_PINS.items()):
    if _p == _GR1_GUARD_PATH or _p == _GR1_ROAD_PATH:
        continue
    _gr1_checks['landed-pin:' + _p.rsplit('/', 1)[1]] = (
        (_gr1_git('rev-parse', 'HEAD:%s' % _p) or b'').decode().strip() == _b)
```

This branch executes only when the chronology state is **not** `EXECUTION`, so no checkpoint of any
attempt reached it. It carries two defects.

**Defect 1 — the extraction is not total.** `_p.rsplit('/', 1)[1]` assumes every pinned path
contains a `/`. `_GR1_PINS` includes the valid repository-root path `AGENTS.md`, for which
`rsplit('/', 1)` returns a one-element list. `sorted()` places `AGENTS.md` first, so the loop raises
`IndexError` on its first iteration and the guard aborts before `R7-GR1` can emit any verdict.

**Defect 2 — the key is not injective.** Six pinned paths reach the loop, and their leaf names
supply only five distinct keys: act 28's and act 29's preregistrations are both named
`preregistration.md`. In sorted order act 29's assignment overwrites act 28's, so one of the two
pin checks is silently discarded. This is not a false red but a weakened contract: at a correct
landing both verdicts are `True`, and the loss is invisible.

Measured at the second attempt's candidate landing: the guard aborts with `IndexError` at the
first iteration; with the extraction made total and nothing else changed, the clause reports 82
checks, of which **five**, not six, are `landed-pin` keys — the count that exhibits defect 2
independently of reading the code.

## The attempted executions, recorded as evidence

Both attempts are kept as history. Neither is this round's `E`, neither is certified as a landing,
and no commit of either is reused as ancestry.

| object | value |
| --- | --- |
| attempt 1, base | `4cff6771e808ad78de3392e61190b71ba5055de6` |
| attempt 1, candidate `E` | `2a67dfcab4ba443ec3b980335ce0a59e1b3e4a3b` — **failed** its fixed-HEAD checkpoint on `note-mut:shape-dropped`, the defect Amendment 1 corrects; never pushed |
| attempt 2, base | `15d08103a9c214395a0cc7948dfda3bc6858f30e` |
| attempt 2, stage 1 | `c511b9b95f01ee8fa93687cfaeb1be93c38da67b` — accepted, 92 of 92 |
| attempt 2, stage 2 | `7498df5e2215030348fc7efc482ae2032ff2c43d` — accepted, 93 tags, `R7-GR1` red on exactly `artifact-result-note` and `artifact-tag-map` |
| attempt 2, certified head | `5e59122e1a7f92f20a6115f8c417b865efb8382c` — **93 of 93 PASS** under chronology `EXECUTION`, `R7-GR1` reporting `73 checks, 23 control group(s); failures: none`; its exact-head pull-request build was green on all four jobs |
| attempt 2, candidate landing | `73f505974674e76b1bb425bc9f605ed5feab3a0f` — first parent current green `main`, second parent exactly the certified head, tree identical to it, adding nothing; **never pushed, and not a landing** |

At that candidate the guard aborts with `IndexError` before `R7-GR1` emits. A throwaway worktree
carrying the single substitution `[1]` → `[-1]` and no other change reports
`R7-GR1 contracts: 82 checks, 23 control group(s); chronology LANDED-UNRECORDED; failures: none`,
`PASS R7-GR1` and `ALL CHECKS PASS`. That patch identifies the defect; **it was not adopted into
any commit**, and the candidate landing was never pushed.

**These are discrepancies in the attempted implementation of one contract, not changes to what the
round measured.** The certification of `5e59122e…` in the `EXECUTION` regime stands as a historical
fact about that commit; what it does not establish is that the clause can complete at a landing. No
outcome, verdict, predicate contract or frozen sentence is affected, and none is revisited here.

## What this amendment changes — exactly two corrections and one control

**Correction 1, the extraction made total**, frozen as text. It preserves the intended leaf-name
behaviour for nested paths and is defined for a repository-root path:

```python
_p.rsplit('/', 1)[-1]
```

**Correction 2, the key made injective**, frozen as text. The landing's pin check is keyed by the
pinned path itself, so that each of the six paths reaching the loop contributes its own verdict and
none is overwritten:

```python
_gr1_checks['landed-pin:' + _p] = (
    (_gr1_git('rev-parse', 'HEAD:%s' % _p) or b'').decode().strip() == _b)
```

**The regression control**, frozen as text, exercised during ordinary execution so that neither
defect can again be latent until the landing. It runs unconditionally, outside the state split, and
requires the extraction to be total over every pinned path, to give the final component of a nested
path, to give `AGENTS.md` for the root path, and to leave the landing's keys pairwise distinct:

```python
_gr1_pin_names = dict((_p, _p.rsplit('/', 1)[-1]) for _p in _GR1_PINS)
_gr1_pin_keys = [_p for _p in sorted(_GR1_PINS)
                 if _p != _GR1_GUARD_PATH and _p != _GR1_ROAD_PATH]
_gr1_checks['landed-pin-names'] = (
    len(_gr1_pin_names) == len(_GR1_PINS)
    and _gr1_pin_names.get('AGENTS.md') == 'AGENTS.md'
    and all(_gr1_pin_names[_p] == _p.split('/')[-1] for _p in _GR1_PINS)
    and len(set(_gr1_pin_keys)) == len(_gr1_pin_keys))
_gr1_controls += 1
```

The control changes no landing semantics. It makes a previously unreachable code path testable
before the landing, which is the whole of its purpose: a contract that cannot run in the regime it
was written for is a contract that proves nothing there, and it now fails closed at every stage.

## What this amendment does NOT change, named exhaustively

1. The preregistration and Amendment 1, neither of which is edited; both blobs are pinned below and
   must be unchanged at `B`.
2. Amendment 1's correction to `note-mut:shape-dropped`, which stands exactly as frozen.
3. Any result-note wording, any frozen statement of `_GR1_REQUIRED`, and the ten content contracts
   over them.
4. Any frozen outcome, target, prediction, status rule or outcome label.
5. The predicate contract: the frozen `_pfr_road_ok` replacement, the one retired leg, the five
   retained legs, and the twenty-nine-row differential suite with its expected table.
6. The chronology rule, its three states, the separation of ancestry from execution shape, the
   canonical-landing definition and the fifteen lifecycle fixtures.
7. The stage count and the stage shapes: three execution commits, one per stage, with stage 2's
   dry run red on exactly the two artifact contracts.
8. The placement contract in either regime, the history-prefix contract, the whole-seals-tree
   integrity contract, the tag-map contracts and the `landed-artifact` contracts.
9. **Every other check and mutation control.** No check other than the `landed-pin` loop is
   altered, and the one addition is the regression control above.
10. The round's shape: still non-sealing, `E` → `L`, no `P`, no manifest record, no prospective
    declaration, and the baseline exception owned by the preregistration.
11. Act 28's and act 29's artifacts, verdicts and seal state, and act 29's pull request, which is
    not touched by this amendment and whose being behind `main` authorizes nothing.

## What the retry must do

The execution restarts from the new `B` and from no other commit, and rebuilds the same three
stages. It does not reuse either attempted execution's commits as ancestry.

| stage | what changes relative to the second attempt |
| --- | --- |
| 1 | nothing: the frozen `_pfr_road_ok` replacement, installed from the freeze |
| 2 | the `R7-GR1` block, with both corrections above and the regression control, with `_GR1_B` set to the new `B`, and with **both** amendments pinned by blob beside the preregistration |
| 3 | a **freshly measured** base column at the new `B`, the head column taken from the retry's own accepted stage-2 checkpoint, and new artifacts |

The retry's stage-3 checkpoint must be **94 of 94 PASS** with `HEAD` fixed at its `E` throughout —
the ninety-two pre-existing tags, `R7-PFR` among them, plus `R7-GR1`, with the regression control
among `R7-GR1`'s own checks — and the history contract must see exactly three commits from the new
`B`. No column, wall clock, artifact or accepted checkpoint of either attempt is reused as the
retry's evidence.

The result note gains one recorded sentence naming this amendment and the second attempt's
certified head and candidate landing, so that the round's record states why its base moved a second
time. Amendment 1's sentence stands. No other note wording changes.

## Start state, pinned

| path | blob at `D` |
| --- | --- |
| `verification/infrastructure/round-gr-1-roadmap-entry-scoping/preregistration.md` | `013ca3d75c65fd884974e7e6350b7c78924bb22b` |
| `verification/infrastructure/round-gr-1-roadmap-entry-scoping/amendments/amendment-1.md` | `631439af8682eec66a1f9ec3aaacece76d50dfb4` |
| `verification/lean/edge_rigidity_probe.py` | `5e2c36c30c2e231bc726741bd522ec051b657391` |
| `verification/ROADMAP.md` | `d0658c99b6ef13d984fd533760393c0b4a2e43c7` |
| `verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/preregistration.md` | `9e1b05bb39ce0c4ade7df38d21b2b947f8aa9011` |
| `verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/result.md` | `c445c5cef9ba01bd5271e90fe988297e0786b097` |
| `verification/seals/PFR.json` | `d09a24ff68958a19f57d4ba07f3c94263820dc83` |
| `verification/programmes/oi-qm/track-b/act-29-product-admission/preregistration.md` | `5451a52d87d7d2ab2aac48802bb80898d81f6a16` |
| `verification/lean-mathlib/OIBridge/ProductLocusFreedom.lean` | `325c09a180366765ae4d742b752099d3b219d3c9` |
| `AGENTS.md` | `a9687b39c69973d35a2ff81c257687071fd35eca` |
| `verification/seals/` (tree) | `92e0956ad6b187fddf77068f33c66e69a012f074` |

Because neither attempted execution was merged, the guard file, the ROADMAP and the seals tree at
`D` are still the ones the preregistration pins, so the retry's base column, its old-predicate
extraction and its fixtures are measured against the same objects the freeze named.

### What must hold at the new base, checkable mechanically

| # | scope | precondition | mechanical check |
| --- | --- | --- | --- |
| 1 | `D` | This amendment's own name is free | `git grep -l -- 'amendment-2' D` under this round's directory returns nothing |
| 2 | `D` | The seals tree at `D` is the pinned one | `git rev-parse D:verification/seals` is `92e0956ad6b187fddf77068f33c66e69a012f074` |
| 3 | `D → B` | `D` is an ancestor of `B` | `git merge-base --is-ancestor D B` succeeds |
| 4 | `D → B` | The blobs the round consumes are unchanged | each `frozen-blob` path below has at `B` the blob named |
| 5 | `B` | The preregistration and Amendment 1 are present and unamended in substance | their blobs at `B` are `013ca3d7…` and `631439af…` |
| 6 | `B` | No `GR-1` execution object exists | the guard file at `B` contains no `R7-GR1`, no `_GR1` and no `_gr1_`; no `verification/seals/GR1.json`; the round directory holds only `preregistration.md` and `amendments/amendment-*.md` |
| 7 | `B` | No round declares at `B`, and the retained baseline is act 28's | `_MANIFEST_PROSPECTIVE = {}` and `_MANIFEST_BASELINE` act 28's |
| 8 | `B` | Act 28 is sealed and its guard still carries the superseded leg | `PFR.json` is the pinned record; the guard carries the document-wide count line verbatim |
| 9 | `B` | Act 29 has not landed | the guard file at `B` contains no `R7-PRA` and no `_PRA`; no `PRA.json`; no `ProductAdmission.lean` |
| 10 | `B` | This amendment is in the tree at its path | the path exists at `B`; its blob is the one the retry's `R7-GR1` clause pins, which the block cannot state of itself |

```control-plane-preconditions
d: 15d08103a9c214395a0cc7948dfda3bc6858f30e
merged: false
frozen-blob: verification/infrastructure/round-gr-1-roadmap-entry-scoping/preregistration.md 013ca3d75c65fd884974e7e6350b7c78924bb22b
frozen-blob: verification/infrastructure/round-gr-1-roadmap-entry-scoping/amendments/amendment-1.md 631439af8682eec66a1f9ec3aaacece76d50dfb4
frozen-blob: verification/lean/edge_rigidity_probe.py 5e2c36c30c2e231bc726741bd522ec051b657391
frozen-blob: verification/ROADMAP.md d0658c99b6ef13d984fd533760393c0b4a2e43c7
frozen-blob: verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/preregistration.md 9e1b05bb39ce0c4ade7df38d21b2b947f8aa9011
frozen-blob: verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/result.md c445c5cef9ba01bd5271e90fe988297e0786b097
frozen-blob: verification/seals/PFR.json d09a24ff68958a19f57d4ba07f3c94263820dc83
frozen-blob: verification/programmes/oi-qm/track-b/act-29-product-admission/preregistration.md 5451a52d87d7d2ab2aac48802bb80898d81f6a16
frozen-blob: verification/lean-mathlib/OIBridge/ProductLocusFreedom.lean 325c09a180366765ae4d742b752099d3b219d3c9
frozen-blob: AGENTS.md a9687b39c69973d35a2ff81c257687071fd35eca
# row 2: the seals tree at D, a drafting-time fact
{"id": "d2-seals-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/seals)\" = 92e0956ad6b187fddf77068f33c66e69a012f074", "expect": "exit0"}
# row 3: provenance
{"id": "db3-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
# row 4, the tree half: the seals tree is unchanged from D to B
{"id": "db4-seals-tree", "scope": "D->B", "check": "test \"$(git rev-parse $REF:verification/seals)\" = 92e0956ad6b187fddf77068f33c66e69a012f074", "expect": "exit0"}
# row 6: no execution object; the names occur in this file, so the guard and the tree are read directly and never through git grep
{"id": "b6-guard-clean", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e 'R7-GR1' -e '_GR1' -e '_gr1_'", "expect": "empty"}
{"id": "b6-no-record", "scope": "B", "check": "git ls-tree --name-only $REF verification/seals/ | grep -e 'GR1.json'", "expect": "empty"}
{"id": "b6-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-gr-1-roadmap-entry-scoping/ | grep -v -e '/preregistration.md$' -e '/amendments/amendment-[0-9][0-9]*.md$'", "expect": "empty"}
# row 7: no round declares at B; the retained baseline is act 28's
{"id": "b7-no-prospective", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e '^_MANIFEST_PROSPECTIVE = {}$'", "expect": "nonempty"}
{"id": "b7-baseline-pfr", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"^_MANIFEST_BASELINE = {'base': '101b8cebb140c2ee7b982641ff005b84bbf0a1cf', 'authorized': ('PFR',)}$\"", "expect": "nonempty"}
# row 8: act 28 sealed and its guard still carrying the superseded leg
{"id": "b8-pfr-sealed", "scope": "B", "check": "git show $REF:verification/seals/PFR.json | tr -d ' \\n' | grep -e '\"round\":\"PFR\",\"kind\":\"sealed\",\"base\":\"101b8cebb140c2ee7b982641ff005b84bbf0a1cf\",\"sealed_head\":\"47192f150ed5e94affc7d00e6aca839e3fd461cf\",\"merge\":\"4de9777d3cdd949c798beb4a6487dfbf6da6ae4b\"'", "expect": "nonempty"}
{"id": "b8-superseded-leg-present", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -F -e '    return n.count(p0) == 1 and n.count(_pfr_n(_PFR_ROAD_STANDING)) == 1'", "expect": "nonempty"}
# row 9: act 29 not landed at B
{"id": "b9-no-pra-guard", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e 'R7-PRA' -e '_PRA'", "expect": "empty"}
{"id": "b9-no-pra-record", "scope": "B", "check": "git ls-tree --name-only $REF verification/seals/ | grep -e 'PRA.json'", "expect": "empty"}
{"id": "b9-no-pra-module", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/lean-mathlib/ | grep -e 'ProductAdmission'", "expect": "empty"}
# row 10: both amendments at their paths
{"id": "b10-amendment-1-present", "scope": "B", "check": "git cat-file -e $REF:verification/infrastructure/round-gr-1-roadmap-entry-scoping/amendments/amendment-1.md", "expect": "exit0"}
{"id": "b10-self-present", "scope": "B", "check": "git cat-file -e $REF:verification/infrastructure/round-gr-1-roadmap-entry-scoping/amendments/amendment-2.md", "expect": "exit0"}
```

## Execution discipline, unchanged

- Once frozen, immutable. A further execution-affecting correction is amendment 3, separately
  frozen and merged, and its certified merge becomes the base after this one.
- The retry never absorbs later `main` before certification: no merge from `main`, no rebase, no
  amend, no force-push.
- Neither attempted execution's commits are rewritten, amended, rebased or force-pushed; they are
  historical evidence and nothing else, and the second attempt's candidate landing is not one.
- A retry that diverges from the freeze as amended **records the discrepancy** and does not repair
  the freeze.
- The landing remains `E` → `L` on the execution pull request, and the merge of that pull request
  happens only on explicit owner direction naming the exact head.
