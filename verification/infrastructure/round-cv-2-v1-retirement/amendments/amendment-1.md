# Certificate infrastructure round CV-2 — AMENDMENT 1: T1 control 2 required at stage 2 a failure the stage order makes impossible there

**Append-only, execution-affecting.** This amendment supersedes exactly one frozen control, T1
control 2, moves the decision of `CV2-1` wholly to the stage-1 checkpoint, and carries the base
movement through the frozen data that names the base. It changes nothing else. Under `AGENTS.md`
`§A.37` it is frozen and reviewed separately, repeats the `M`-then-`B` certification, and **its
certified merge commit becomes the new mandated execution base**, from which the execution restarts.
The preregistration is **not edited**: its blob stays `61de8904ac4bc98eb2ae608f42d526faa1f5dcb7`,
and this file sits beside it.

## The commit vocabulary

- **`D`** — this amendment's drafting snapshot, `5608fdc0b5773efd3a98164865c1f26323af2a26`: the
  certified merge of #718, which was the preregistration's mandated execution base (push run
  35801649542, all five jobs success, mode `B` 32 rows) and is the current state of `main`. Every
  measurement below marked "at `D`" was taken against it.
- **`B`** — the new mandated execution base: the certified merge commit on `main` of this
  amendment. **Before that merge exists `B` has no SHA, and this file assigns it none.** From that
  merge, `5608fdc0…` is provenance and the execution never resumes from it. Every reference to `B`
  or `B_CV2` in the preregistration, from that merge on, means this `B`.
- **`M`** — a candidate merge of this amendment, used to evaluate the `B`-scoped preconditions
  predictively. Test state only.

## What went wrong, measured and not narrated

The preregistration's `F1` states two separate facts about the superseded `T1` segments, measured
at its own drafting snapshot:

1. on a tree carrying the frozen `PRA` translation, the superseded text fails exactly **six**
   `R7-CV1` contracts — `census-6b-as-frozen`, `census-equal-to-committed`,
   `legacy-owned-exactly-pra`, `note:6b-sentence`, `provenance-fifty-one-translated`,
   `provenance-thirty-five-translated-rows`;
2. adding one live-policy clause adds a **seventh**, `live-policy-zero-clauses`.

T1 control 2, as frozen, reads: "On the stage-2 tree (the translation present): the superseded
segments, compiled from the base's text, fail the seven contracts `F1` names; the replacements pass
them." The frozen stage order writes the first live-policy clause at stage 4. On the stage-2 tree
no clause exists, so by the freeze's own `F1` the superseded text fails six contracts there and
cannot fail seven. **The control required at stage 2 a result that `F1` shows occurs only once a
clause is present.** The defect is in the frozen control, not in the implementation, which did
what `F1` predicts.

## The attempted execution, measured

The first execution from `5608fdc0b5773efd3a98164865c1f26323af2a26` was stopped after its second
stage. It is **not** this round's `E`, it is **not** certified, and nothing from it is carried
forward. What it measured:

| object | measured |
| --- | --- |
| start | preregistration blob `61de8904…` verified before any edit; `CV2-0` `HOLD` |
| stage 1 | `T1` as frozen: the three superseded hashes verified, reverting the replacements reproduces the base guard byte for byte; checkpoint `ALL CHECKS PASS`, 105 tags, verdict map identical to the base's |
| stage 2 | the translation matched the frozen `F7` objects exactly (`PRA.json` `af7844f2…`, record `46349c11…`, empty legacy set `052ff9b0…`); checkpoint: `V6` authoritative `PRA` `PASS`, record `PASS`, `legacy-owned 0`, `CV2` `UNATTESTED`; guard `ALL CHECKS PASS`, 105 tags, `R7-PRA` `ARCHIVED` |
| T1 control 2 | on the stage-2 tree, the base guard fails exactly `R7-CV1`, on the six contracts listed above, and on no other; `live-policy-zero-clauses` passes; 104 other tags pass. The frozen wording requires seven |

**Outcome of record for the attempt:** `CV2-1` `SUPERSEDED-DEVIATED`, on T1 control 2, by the
freeze's literal wording. `CV2-2`'s data were translated as frozen, but stage 2 was entered over a
target that resolved negative once its mandatory control became executable, so no outcome of the
attempt is carried forward.

## What this amendment changes

### 1. T1 control 2, superseded

T1 control 2 is replaced by two scratch demonstrations, both rooted at the retry's **own accepted
stage-1 head** — its committed `T1` — and both executed **at the stage-1 checkpoint, before stage 2
is entered**. Neither demonstration is committed; each runs in a detached scratch worktree with the
git and pull-request environment scrubbed.

- **Demonstration (a) — the translation.** The scratch tree is the stage-1 head plus exactly the
  three frozen `F7` objects: `verification/certificates/PRA.json` at blob
  `af7844f223fe2cf1a5934ad92f1e2134cb6cbd5d`,
  `verification/certificates/attestations/PRA.json` at `46349c11118781f5cfa3993203fde136e7aee246`,
  and `verification/certificates/legacy-v1-owned.json` at
  `052ff9b0b8529fa57578339f5be01e03d3b921e6`, committed in scratch. On it:
  - the **superseded text** — the guard at `B`, whose three segments are the frozen superseded
    ones — fails exactly one tag, `R7-CV1`, on **exactly** the six contracts `F1` item 1 names, and
    every other tag passes;
  - the **replacement text** — the guard at the stage-1 head — ends `ALL CHECKS PASS`.
- **Demonstration (b) — the translation and one clause.** The same scratch tree plus
  `verification/certificates/live-policy.json` replaced by exactly the file frozen below, blob
  `46fb79d1e2cfaa47493d96184961c7bc90da7fbc`, committed in scratch. On it:
  - the superseded text fails exactly one tag, `R7-CV1`, on **exactly** those six contracts and
    `live-policy-zero-clauses` — seven — and every other tag passes;
  - the replacement text ends `ALL CHECKS PASS`.

The scratch clause, frozen byte for byte (one-space indent, sorted keys, trailing newline):

```json
{
 "count": 1,
 "policies": [
  {
   "activation": "scratch: T1 control 2, demonstration (b) only",
   "evidence": "CV2/amendments/amendment-1.md",
   "expiry": "scratch: never committed",
   "id": "t1-control-2-scratch",
   "owner_round": "CV2",
   "predicate": {
    "path": "tools/release_gate.py",
    "text": "certificate-verifier",
    "type": "file-contains"
   },
   "protocol": 2
  }
 ],
 "protocol": 2
}
```

The clause is a scratch fixture and is never committed. It is not one of the stage-4 clauses
`P1`–`P5b`, and it authorizes no clause.

**Measured at `D`**, on the scratch trees just described rooted at `D` with `T1` applied — a tree
identical to the attempt's stage-1 tree:

| demonstration | superseded text | replacement text |
| --- | --- | --- |
| (a) | `FAILURE`: exactly `R7-CV1`, failures `census-6b-as-frozen`, `census-equal-to-committed`, `legacy-owned-exactly-pra`, `note:6b-sentence`, `provenance-fifty-one-translated`, `provenance-thirty-five-translated-rows`; 104 other tags `PASS` | `ALL CHECKS PASS`, 105 tags; `R7-CV1` 106 checks, no failure |
| (b) | `FAILURE`: exactly `R7-CV1`, failures the same six and `live-policy-zero-clauses`; 104 other tags `PASS` | `ALL CHECKS PASS`, 105 tags; `R7-CV1` 106 checks, no failure |

The control passes only if all four cells match the frozen expectation exactly: the named failure
sets, no other failing tag, and `ALL CHECKS PASS` for both replacements. Any other result is
`SUPERSEDED-DEVIATED` on control 2.

### 2. `CV2-1` decided wholly at the stage-1 checkpoint

All five `T1` controls — control 1 (pinned and unique), control 2 as superseded above, control 3
(`EXECUTION` unchanged), control 4 (post-landing reads `E_CV1`, and fails closed) and control 5
(every other row identical) — are executed at the stage-1 checkpoint, against the committed
stage-1 head, and `CV2-1` is decided there. Controls 1, 3, 4 and 5 are unchanged in content; only
the point at which they are executed is fixed. **`SUPERSEDED-DEVIATED` stops the round before
stage 2 is entered**, as the status rule already states.

The results are recorded in the execution's stage-1 log and again in `census.json` at stage 4,
where the harness re-executes all five controls rooted at the stage-1 commit and must reproduce the
stage-1 outcomes exactly. A stage-4 re-execution that differs is recorded in the result note; it
does not reopen a stage already entered.

### 3. The base movement, carried through the frozen data

- **The retry's first act** verifies, at `B`, the preregistration blob `61de8904…` **and** this
  amendment's blob, and then runs `CV2-0` as amended below. No edit precedes those checks.
- **`CV2-0`, amended.** Every row of the preregistration's start-state table and pinned-blob table
  is required at `B` with its frozen value — this amendment changes none of those objects. The row
  "nothing between `D` and `B` but this file" becomes: nothing between the preregistration's
  drafting snapshot `b5cecce3…` and `B` but the preregistration and this amendment. The round's
  directory at `B` holds exactly `preregistration.md` and `amendments/amendment-1.md`.
- **The retry's `CV2.json`** carries `base` = `B`; `control_plane` = the preregistration (blob
  `61de8904…`, merge `5608fdc0…`, `execution_affecting: true`) followed by this amendment (its blob,
  merge `B`, `execution_affecting: true`); `evidence` = `CV2/preregistration.md` and
  `CV2/amendments/amendment-1.md` at their blobs, together with the artifacts later stages add.
  The last execution-affecting entry is this amendment, so `V6` derives the base as `B`.
- **Counts that include `CV-2`'s own evidence** include this amendment. At the retry's stage-2
  checkpoint the verifier reports 157 + `PRA`'s 4 + `CV2`'s 2 = **163** evidence ids; `CV2-8`'s
  "157 + `PRA`'s 4 + `CV2`'s own" counts this amendment among `CV2`'s own.
- **`W1`'s comparisons** on `(B_CV2, head)` use the new `B`.
- **The `PRA` translation and the empty legacy set are unchanged**: `af7844f2…`, `46349c11…` and
  `052ff9b0…`, the `F7` values. The translation's `migration_snapshot` stays
  `b5cecce3168e84fce86eec54669141ae7c4791eb`, the snapshot its facts were read at.
- **The retry branches** from the new certified `B` and from nothing else.

## What this amendment does NOT change, named exhaustively

1. The preregistration, which is not edited; its blob is pinned below and must be unchanged at `B`.
2. `T1`'s superseded segments, their hashes and anchors, and `T1`'s replacement text.
3. `T1` controls 1, 3, 4 and 5, in content.
4. The stage-2 translation, its frozen data and blobs, and the stage-2 checkpoint, except that the
   evidence count carries this amendment.
5. Every other target, prediction, outcome label, status rule and frozen post-round sentence.
6. The three verifier slots, the seventeen frozen vectors, the disposition table, the policy
   clauses `P1`–`P5b`, the protocol-text propositions, the mutation budget and the landing shape.
7. The stage count and stage order: six stages, each committed before its checkpoint; no stage is
   compressed or combined.
8. The round's shape: non-sealing, first `native-v2` round, `E` → `L` → `A`, no `P`.

## Start state, pinned

| path | blob or tree at `D` |
| --- | --- |
| `verification/infrastructure/round-cv-2-v1-retirement/preregistration.md` | `61de8904ac4bc98eb2ae608f42d526faa1f5dcb7` |
| `verification/lean/edge_rigidity_probe.py` | `2eab600fb8cd078b3dd0f3867a6e7420cfc2b79f` |
| `tools/certificate_verifier.py` | `a475408874b850f34c31eca5e1cb4ab549601f38` |
| `tools/release_gate.py` | `ca851befa24028655ecbbee85e53482bc186eb82` |
| `.github/workflows/verify.yml` | `3ed93ea20bb42f986850d008d5a5edc93a4b7e34` |
| `AGENTS.md` | `a9687b39c69973d35a2ff81c257687071fd35eca` |
| `verification/certificates/legacy-v1-owned.json` | `8d255edfd6c5fc352c398ef00f8848f91d324951` |
| `verification/certificates/live-policy.json` | `78a5c1457ca222c65cb146cdcc9b3081b6e6909b` |
| `verification/seals/PRA.json` | `6bfec3684724302a95d6fc05b1d481a4a3d552a8` |
| `verification/programmes/oi-qm/track-b/act-29-product-admission/preregistration.md` | `5451a52d87d7d2ab2aac48802bb80898d81f6a16` |
| `verification/certificates` (tree) | `8aa1a8fac388b625653803f7dad7c2fdabb12cc4` |
| `verification/seals` (tree) | `ea7b7161fa84d96d8bc5ae03b0c8aa58e1879125` |

The attempted execution never reached `main`, so every object the preregistration pins is, at `D`,
the one it pins.

```control-plane-preconditions
d: 5608fdc0b5773efd3a98164865c1f26323af2a26
merged: false
frozen-blob: verification/infrastructure/round-cv-2-v1-retirement/preregistration.md 61de8904ac4bc98eb2ae608f42d526faa1f5dcb7
frozen-blob: verification/lean/edge_rigidity_probe.py 2eab600fb8cd078b3dd0f3867a6e7420cfc2b79f
frozen-blob: tools/certificate_verifier.py a475408874b850f34c31eca5e1cb4ab549601f38
frozen-blob: tools/release_gate.py ca851befa24028655ecbbee85e53482bc186eb82
frozen-blob: .github/workflows/verify.yml 3ed93ea20bb42f986850d008d5a5edc93a4b7e34
frozen-blob: AGENTS.md a9687b39c69973d35a2ff81c257687071fd35eca
frozen-blob: verification/certificates/legacy-v1-owned.json 8d255edfd6c5fc352c398ef00f8848f91d324951
frozen-blob: verification/certificates/live-policy.json 78a5c1457ca222c65cb146cdcc9b3081b6e6909b
frozen-blob: verification/seals/PRA.json 6bfec3684724302a95d6fc05b1d481a4a3d552a8
frozen-blob: verification/programmes/oi-qm/track-b/act-29-product-admission/preregistration.md 5451a52d87d7d2ab2aac48802bb80898d81f6a16
# row 1: the amendment's path is free at D, and the round directory holds the preregistration alone
{"id": "d1-amendment-free", "scope": "D", "check": "git ls-tree -r --name-only $D verification/infrastructure/round-cv-2-v1-retirement/ | grep -v -x -e 'verification/infrastructure/round-cv-2-v1-retirement/preregistration.md'", "expect": "empty"}
# row 2: the trees at D
{"id": "d2-seals-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/seals)\" = ea7b7161fa84d96d8bc5ae03b0c8aa58e1879125", "expect": "exit0"}
{"id": "d2-certificates-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/certificates)\" = 8aa1a8fac388b625653803f7dad7c2fdabb12cc4", "expect": "exit0"}
# row 3: provenance, D to B: D an ancestor, nothing but this file between them, the trees unchanged
{"id": "db3-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
{"id": "db3-only-this-file", "scope": "D->B", "check": "git diff --name-only $D $REF | grep -v -x -e 'verification/infrastructure/round-cv-2-v1-retirement/amendments/amendment-1.md'", "expect": "empty"}
{"id": "db3-seals-tree", "scope": "D->B", "check": "test \"$(git rev-parse $REF:verification/seals)\" = ea7b7161fa84d96d8bc5ae03b0c8aa58e1879125", "expect": "exit0"}
{"id": "db3-certificates-tree", "scope": "D->B", "check": "test \"$(git rev-parse $REF:verification/certificates)\" = 8aa1a8fac388b625653803f7dad7c2fdabb12cc4", "expect": "exit0"}
# row 4: no execution object at B
{"id": "b4-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-cv-2-v1-retirement/ | grep -v -e '/preregistration.md$' -e '/amendments/amendment-1.md$'", "expect": "empty"}
{"id": "b4-no-cv2-certificate", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/certificates/ | grep -e '/CV2\\.json$'", "expect": "empty"}
{"id": "b4-no-pra-certificate", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/certificates/ | grep -e '/PRA\\.json$'", "expect": "empty"}
# row 5: the legacy-owned set is exactly act 29 at B; act 29 pinned under V1; no V1 round declared
{"id": "b5-legacy-names-pra", "scope": "B", "check": "git show $REF:verification/certificates/legacy-v1-owned.json | grep -e '\"stem\": \"PRA\"'", "expect": "nonempty"}
{"id": "b5-pra-clause-present", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"check('R7-PRA'\"", "expect": "nonempty"}
{"id": "b5-prospective-empty", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -x \"_MANIFEST_PROSPECTIVE = {}\"", "expect": "nonempty"}
{"id": "b5-manifest-count", "scope": "B", "check": "test \"$(git ls-tree --name-only $REF verification/seals/ | grep -c '\\.json$')\" = 34", "expect": "exit0"}
# row 6: T1's superseded segments at B, with their frozen hashes
{"id": "b6-t1a-hash", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | sed -n '/^def _cv1_store():$/,/^    return certs, rows$/p' | sha256sum | cut -d' ' -f1 | grep -x 'ee4728a63f7ff81f50529cd0b87923914918060c71d0ba64a58300f1745ee015'", "expect": "nonempty"}
{"id": "b6-t1b-hash", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | sed -n \"/^    with open(os.path.join(os.path.dirname(VERIFICATION), _CV1_CERTS, 'legacy-v1-owned.json'),\\$/,/^    and _CV1_POLICY.get('policies') == \\[\\])\\$/p\" | sha256sum | cut -d' ' -f1 | grep -x '1b5549514549d525d43102deae0c1525ce64ede70d09a5219efe0a5f66d72093'", "expect": "nonempty"}
{"id": "b6-t1c-hash", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | sed -n \"/^    rep6b\\['PRA'\\] = {'class': 'LEGACY-V1-OWNED'/,/'v7_entry': rep\\['legacy'\\] == \\['PRA'\\]}\\$/p\" | sha256sum | cut -d' ' -f1 | grep -x '3bb55978fcdb41c7ddbcd349dd6d2b9dfffa574ac8b6ba69df45e4afe373e272'", "expect": "nonempty"}
# row 7: this amendment at its path
{"id": "b7-self-present", "scope": "B", "check": "git cat-file -e $REF:verification/infrastructure/round-cv-2-v1-retirement/amendments/amendment-1.md", "expect": "exit0"}
```

## Execution discipline, unchanged

- Once frozen, immutable. A further execution-affecting correction is amendment 2, separately
  frozen and merged, and its certified merge becomes the base after this one.
- The retry never absorbs later `main` before `E` is certified: no merge from `main`, no rebase, no
  amend, no force-push.
- A retry that diverges from the freeze as amended records the discrepancy and does not repair the
  freeze.
- The landing remains `E` → `L` → `A`, and each merge to `main` happens only on explicit owner
  direction naming the exact head.
