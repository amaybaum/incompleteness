# Guard repair round GR-1 — AMENDMENT 1: the shape-statement mutation control had no power

**Append-only, execution-affecting.** This amendment corrects one mechanical defect in a contract
the preregistration requires and changes nothing else. Under `AGENTS.md` `§A.37` it is frozen and
reviewed separately, repeats the `M`-then-`B` certification, and **its certified merge commit
becomes the new mandated execution base**, from which the execution restarts. The preregistration
is **not edited**: its blob stays `013ca3d75c65fd884974e7e6350b7c78924bb22b`, and this file sits
beside it.

## The commit vocabulary

- **`D`** — this amendment's drafting snapshot, `4cff6771e808ad78de3392e61190b71ba5055de6`: the
  certified merge of #706, which was the preregistration's own mandated execution base and is the
  current state of `main`. Every measurement below marked "at `D`" was taken against it.
- **`B`** — the new mandated execution base: the certified merge commit on `main` of this
  amendment. **Before that merge exists `B` has no SHA, and this file assigns it none.** From that
  merge, the preregistration's `B` is provenance and the execution never resumes from it.
- **`M`** — a candidate merge of this amendment, used to evaluate the `B`-scoped preconditions
  predictively. Test state only.

## What went wrong, measured and not narrated

The preregistration's guard clause carries one mutation control over the result note's first frozen
statement. As implemented in the attempted execution it read:

```python
_gr1_checks['note-mut:shape-dropped'] = _pfr_n(_GR1_REQUIRED[0][1]) not in _pfr_n(
    _GR1_RES.replace(_GR1_REQUIRED[0][1], '', 1))
```

It deletes the frozen statement from the **raw** note text and then asks whether the **normalized**
statement survives. The frozen statement is one line; a result note wraps that sentence across
physical lines. So the raw deletion matches nothing, the text is unchanged, and the normalized
statement is still present — the control reports a failure whatever the note says, and, more
seriously, **it could never have detected a genuinely dropped statement**: its mutation has no
effect on the object the content contract actually reads.

Measured at the attempted execution's candidate head: the raw statement occurs **zero** times in
the note, the normalized statement occurs **exactly once**, the raw replacement leaves the text
identical, and the statement remains present afterwards. The content contract `note:shape` itself
passed, as did the other nine; the defect is in the control that is supposed to prove `note:shape`
has power, not in the note and not in any verdict.

## The attempted execution, recorded as evidence

The attempt is kept as history. It is **not** this round's `E`, it is **not** certified, it was
never pushed, and none of its commits is reused as ancestry.

| object | value |
| --- | --- |
| base | `4cff6771e808ad78de3392e61190b71ba5055de6` |
| stage 1 | `d5178e2fe0f1f1351168b689c9a3f7f4c9dfc465` — accepted at its own fixed-HEAD checkpoint, 92 of 92 |
| stage 2 | `70e34e82841074037409b12852694733a1ef458f` — accepted at its own fixed-HEAD checkpoint, 93 tags, the 92 inherited green and identical to stage 1's, `R7-GR1` red on exactly `artifact-result-note` and `artifact-tag-map` |
| candidate `E` | `2a67dfcab4ba443ec3b980335ce0a59e1b3e4a3b` — **failed** its fixed-HEAD checkpoint |

That checkpoint ran with start and exit `HEAD` both the candidate, a clean worktree at launch, 93
distinct tags, 92 PASS and one FAIL. `R7-GR1` reported `71 checks, 23 control group(s); chronology
EXECUTION; failures: note-mut:shape-dropped` — a single failing contract, and no other. Chronology,
the history-prefix contract, the placement contract in its execution regime, the whole-seals-tree
integrity contract, the twenty-nine-row differential suite, the fifteen lifecycle fixtures, the ten
result-note content contracts and both persisted tag-map columns all passed.

**This is a discrepancy in the attempted implementation of a control, not a change to what the
round measured.** No outcome, verdict, predicate contract or frozen sentence is affected by it, and
none is revisited here.

## What this amendment changes — exactly one thing

The corrected control, frozen as text. It mutates the object the content contract reads, and it
requires the mutation to have had an effect, so that a control which cannot bite fails rather than
passing quietly:

```python
_gr1_shape_req = _pfr_n(_GR1_REQUIRED[0][1])
_gr1_note_norm = _pfr_n(_GR1_RES)
_gr1_note_dropped = _gr1_note_norm.replace(_gr1_shape_req, '', 1)
_gr1_checks['note-mut:shape-dropped'] = (
    _gr1_note_dropped != _gr1_note_norm and _gr1_shape_req not in _gr1_note_dropped)
```

The first conjunct is the non-vacuity leg the defective form lacked: a mutation that changes
nothing is a control that proves nothing, and it now fails closed.

## What this amendment does NOT change, named exhaustively

1. The preregistration, which is not edited; its blob is pinned below and must be unchanged at `B`.
2. Any result-note wording, any frozen statement of `_GR1_REQUIRED`, and the ten content contracts
   over them.
3. Any frozen outcome, target, prediction, status rule or outcome label.
4. The predicate contract: the frozen `_pfr_road_ok` replacement, the one retired leg, the five
   retained legs, and the twenty-nine-row differential suite with its expected table.
5. The chronology rule, its three states, the separation of ancestry from execution shape, the
   canonical-landing definition and the fifteen lifecycle fixtures.
6. The stage count and the stage shapes: three execution commits, one per stage, with stage 2's
   dry run red on exactly the two artifact contracts.
7. The placement contract in either regime, the history-prefix contract, the whole-seals-tree
   integrity contract, and the tag-map contracts.
8. **Every other mutation control.** No control other than `note-mut:shape-dropped` is added,
   removed, renamed or reworded.
9. The round's shape: still non-sealing, `E` → `L`, no `P`, no manifest record, no prospective
   declaration, and the baseline exception owned by the preregistration.
10. Act 28's and act 29's artifacts, verdicts and seal state, and act 29's pull request, which is
    not touched by this amendment and whose being behind `main` authorizes nothing.

## What the retry must do

The execution restarts from the new `B` and from no other commit, and rebuilds the same three
stages. It does not reuse the attempted execution's commits as ancestry.

| stage | what changes relative to the attempt |
| --- | --- |
| 1 | nothing: the frozen `_pfr_road_ok` replacement, installed from the freeze |
| 2 | the `R7-GR1` block, with the corrected control above, with `_GR1_B` set to the new `B`, and with this amendment pinned by blob beside the preregistration |
| 3 | a **freshly measured** base column at the new `B`, the head column taken from the retry's own accepted stage-2 checkpoint, and new artifacts |

The retry's stage-3 checkpoint must be **93 of 93 PASS** with `HEAD` fixed at its `E` throughout,
and the history contract must see exactly three commits from the new `B`. The old attempt's
verdicts are not carried forward: no column, no wall clock and no accepted checkpoint of the
attempt is reused as the retry's evidence.

The result note gains one recorded sentence naming this amendment and the attempted execution's
candidate head, so that the round's record states why its base moved. No other note wording
changes.

## Start state, pinned

| path | blob at `D` |
| --- | --- |
| `verification/infrastructure/round-gr-1-roadmap-entry-scoping/preregistration.md` | `013ca3d75c65fd884974e7e6350b7c78924bb22b` |
| `verification/lean/edge_rigidity_probe.py` | `5e2c36c30c2e231bc726741bd522ec051b657391` |
| `verification/ROADMAP.md` | `d0658c99b6ef13d984fd533760393c0b4a2e43c7` |
| `verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/preregistration.md` | `9e1b05bb39ce0c4ade7df38d21b2b947f8aa9011` |
| `verification/programmes/oi-qm/track-b/act-28-product-locus-freedom/result.md` | `c445c5cef9ba01bd5271e90fe988297e0786b097` |
| `verification/seals/PFR.json` | `d09a24ff68958a19f57d4ba07f3c94263820dc83` |
| `verification/programmes/oi-qm/track-b/act-29-product-admission/preregistration.md` | `5451a52d87d7d2ab2aac48802bb80898d81f6a16` |
| `verification/lean-mathlib/OIBridge/ProductLocusFreedom.lean` | `325c09a180366765ae4d742b752099d3b219d3c9` |
| `AGENTS.md` | `a9687b39c69973d35a2ff81c257687071fd35eca` |
| `verification/seals/` (tree) | `92e0956ad6b187fddf77068f33c66e69a012f074` |

Because the attempted execution was never pushed, the guard file, the ROADMAP and the seals tree
at `D` are still the ones the preregistration pins, so the retry's base column, its old-predicate
extraction and its fixtures are measured against the same objects the freeze named.

### What must hold at the new base, checkable mechanically

| # | scope | precondition | mechanical check |
| --- | --- | --- | --- |
| 1 | `D` | The amendment's own name is free | `git grep -l -- 'amendment-1' D` under this round's directory returns nothing |
| 2 | `D` | The seals tree at `D` is the pinned one | `git rev-parse D:verification/seals` is `92e0956ad6b187fddf77068f33c66e69a012f074` |
| 3 | `D → B` | `D` is an ancestor of `B` | `git merge-base --is-ancestor D B` succeeds |
| 4 | `D → B` | The blobs the round consumes are unchanged | each `frozen-blob` path below has at `B` the blob named |
| 5 | `B` | The preregistration is present and unamended in substance | its blob at `B` is `013ca3d7…` |
| 6 | `B` | No `GR-1` execution object exists | the guard file at `B` contains no `R7-GR1`, no `_GR1` and no `_gr1_`; no `verification/seals/GR1.json`; the round directory holds only `preregistration.md` and `amendments/amendment-*.md` |
| 7 | `B` | No round declares at `B`, and the retained baseline is act 28's | `_MANIFEST_PROSPECTIVE = {}` and `_MANIFEST_BASELINE` act 28's |
| 8 | `B` | Act 28 is sealed and its guard still carries the superseded leg | `PFR.json` is the pinned record; the guard carries `check('R7-PFR'` and the document-wide count line verbatim |
| 9 | `B` | Act 29 has not landed | the guard file at `B` contains no `R7-PRA` and no `_PRA`; no `PRA.json`; no `ProductAdmission.lean` |
| 10 | `B` | This amendment is in the tree at its path | the path exists at `B`; its blob is the one the retry's `R7-GR1` clause pins, which the block cannot state of itself |

```control-plane-preconditions
d: 4cff6771e808ad78de3392e61190b71ba5055de6
merged: false
frozen-blob: verification/infrastructure/round-gr-1-roadmap-entry-scoping/preregistration.md 013ca3d75c65fd884974e7e6350b7c78924bb22b
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
# row 10: this amendment at its path
{"id": "b10-self-present", "scope": "B", "check": "git cat-file -e $REF:verification/infrastructure/round-gr-1-roadmap-entry-scoping/amendments/amendment-1.md", "expect": "exit0"}
```

## Execution discipline, unchanged

- Once frozen, immutable. A further execution-affecting correction is amendment 2, separately
  frozen and merged, and its certified merge becomes the base after this one.
- The retry never absorbs later `main` before certification: no merge from `main`, no rebase, no
  amend, no force-push.
- The attempted execution's three commits are not rewritten, not amended, not rebased and not
  force-pushed; they are historical evidence and nothing else.
- A retry that diverges from the freeze as amended **records the discrepancy** and does not repair
  the freeze.
- The landing remains `E` → `L` on the execution pull request, and the merge of that pull request
  happens only on explicit owner direction naming the exact head.
