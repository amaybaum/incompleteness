# Certificate infrastructure round CV-1 — the V2 round-certificate protocol: shadow, census and cutover: PREREGISTRATION

**Control plane only.** This document fixes what `CV-1` will do, what would count as each
outcome, and what no outcome licenses, before any of it is implemented. One file, added. No Lean,
no guard clause, no manifest change, no certificate, no ROADMAP edit, no manuscript edit.

**The mandated execution base is the merge commit of this pull request**, once that merge and its
`main` push run are themselves certified. The execution branches from exactly that commit and from
nothing else, and its first act is to verify this preregistration's blob at that base.

The base this freeze is written against is `D` = `effd5c865dfcc207624712a6711a54b712642f48`, the
`main` merge of `GR-2`'s landing (#712), certified by push run 35692941357.

***

## The commit vocabulary this freeze uses, fixed first

Per `§A.37`:

- **`D`** — the drafting snapshot, `effd5c865dfcc207624712a6711a54b712642f48`. Every measurement
  marked *at `D`* was taken against that commit.
- **`B`** — the mandated execution base: the certified merge commit on `main` of this control
  plane. Before that merge exists `B` has no SHA, and this freeze assigns none.
- **`M`** — a candidate merge continuous integration may construct before this control plane
  lands. Predictive test state only, never ancestry.
- **`E`** — the sealed execution head. **`L`** — the landing merge, first parent current green
  `main`, second parent exactly `E`. There is no `P`.
- **`A`** — new in this round: the **attestation**, a commit appended to `main` *after* `L`'s
  push run is certified, whose only permitted change is one row appended to the round-attestation
  ledger. `A` is not `P`: it writes no per-round constant, no per-round file and no executable
  clause. It exists because `E` cannot contain `tree(E)` or its own SHA, `L` cannot contain its
  own SHA, and neither can contain the verdict of a continuous-integration run that has not yet
  happened.

`GR-2`'s commits are named as such: `B_GR2 = c9e6d56379923195382fa8c797c464397bcedaa5`,
`E_GR2 = 0a61ea0ad6f6a28687203495ac9b29395f506178` with `tree(E_GR2) =
794ffc3cd816e6ea4fc60c49999219f8e5e5d7b2`, `L_GR2 = 4caa5634363ac8746dff8cc4ce86f55f292e4b6f`,
and the `main` merge that brought it in, `D` itself. `GR-1`'s: base
`39090ca75860e7e6cbd99fa6f3ad859cee3efaf4`, `E_GR1 = 8d08f8c913f4bb9ef413114ecceb2f72d72d8213`,
`L_GR1 = 13ffc7372d52c16bdb0e24935aa617deb67e7c51`.

***

## What `CV-1` is, and what it deliberately is not

### The defect family, measured three times

The guard file `verification/lean/edge_rigidity_probe.py` carries one executable block per
historical round. Three of those blocks, in two rounds, committed the same defect: **an
execution-time assertion left running against whatever tree the guard later finds.**

| # | where | what it asserted of every later tree | how it was found |
|---|---|---|---|
| 1 | `R7-GR1`, the declaration pair | that the file's two manifest declarations still carry `GR-1`'s execution-time values | `GR-2`'s freeze, `S1` |
| 2 | `R7-GR1`, the `landed-pin:` loop | that six blobs, three of them outside `GR-1`'s own frozen live scope, are unchanged | `GR-2`'s freeze, `S2` |
| 3 | `R7-GR2`, negative control `N12` | that the whole-file budget holds on the live tree, inside a control whose own freeze scopes the budget to `E` after landing | run 35694203310, the reopened pull request #705 at the unchanged act 29 head `bf7e96fef8135525e752fb0daba0a082cf10ed44` against `D` |

The third was committed by the round that repaired the first two, in the commit that made its
negative suite exhaustive. That is the evidence that the defect is architectural and not a lapse:
the abstraction — a historical round expressed as executable code that runs at every later head —
invites the defect at every extension point, and a repair written in the same abstraction is
another extension point. Run 35694203310 is preserved as the falsifier: on the unchanged act 29
head against `D`, three of four jobs green, `R7-PFR` 164 checks with no failure, `R7-PRA` 216
with no failure, `R7-GR1` 86 with no failure, and exactly one red row, `R7-GR2`'s `N12`, on the
positive half of a control whose subject was the live file.

### The principle `V2` implements

> **Historical rounds certify their own content and topology; they never inspect ordinary files
> at today's `HEAD`.**

A landed round is *data*: a certificate naming its protocol version, its mandated base, its
ordered control-plane artifacts, its evidence, its contributions and its dependencies; and an
attestation row naming its exact `E`, `tree(E)` and `L`. One generic, versioned verifier reads
that data. What is live on the current tree is one universal rule — every evidence artifact of
every accepted certificate still carries its certified blob, resolved through a relocation ledger —
plus a small, constrained, data-only live-policy file. An ordinary round adds no executable
live-tree assertion. The programme-level success metric is frozen here so it can fail:

> **The number of executable live-tree assertions added by an ordinary research round is zero,
> and stays zero.** A round that adds one has failed `V2` architecturally, whatever continuous
> integration reports.

### Two rounds, and the boundary between them

`CV-1` is the first of **two**. It supersedes `N12`, installs every `V2` object **in shadow**,
translates every landed round into a certificate, runs the `V2` conformance corpus and the
`V1`→`V2` differential census while `V1` remains authoritative, and — only after the census at a
fixed head matches the adjudicated profile frozen below — turns the `V2` verifier's continuous
integration job from shadow to **gating**. `V1` is not removed and is not made a shadow: from
that stage on the two gate side by side, which this freeze calls **dual gating** and never calls
"authority moved". `CV-2`, a separate round begun only from a certified `CV-1` and with act 29
landed, retires the accumulated `V1` machinery. The boundary is drawn at deletion and nowhere
else: shadow before gating, gating before deletion, exactly the `SI-1` → `SI-2` → `SI-3` order.

### What `CV-1` is not

1. **It is not the retirement.** No `R7-*` block, no legacy comparison, no validator region and no
   seal record is deleted or weakened. The diff against the base **adds**, with one exception
   named in terms: the `N12` supersession, one hashed segment.
2. **It does not move authority off `V1`.** `V1`'s every check gates at `E`, at `L` and at `A`
   exactly as at `B`. Dual gating is a second gate, not a transfer.
3. **It does not retrofit.** Every historical `B`, `E`, `L`, `P`, preregistration and result note
   stays exactly as and where it is. Translation records the present; it rewrites nothing.
4. **It decides no mathematics** and reads no manuscript for content.
5. **It is not act 29's landing, and it does not touch `#705`.** Act 29's head stays at
   `bf7e96fef8135525e752fb0daba0a082cf10ed44` throughout. Act 29 is a `V1` sealing round whose
   frozen landing shape is `E` → `L` → `P` with `P` writing `PRA.json`; it lands under `V1`, and
   **it must land after `CV-1` is certified and before `CV-2` retires `V1`** — see *The sequence
   between the two rounds* below. `PRA` receives no certificate in this round and is named as the
   one round that stays under `V1`'s sole authority while `CV-1` runs.
6. **It amends no protocol text.** `AGENTS.md` is not edited: under dual gating `§A.37` remains
   correct for every round in flight, and the `V2` protocol text is `CV-2`'s to write when `V1`
   is retired. A protocol amended before its predecessor is gone would instruct the next round to
   do both.

***

## The round's shape, declared first, in `§A.37`'s terms

**`CV-1` is NON-SEALING**, `E` → `L`, no `P`, and then `A`. It creates no seal state and alters
none. It writes no seal record — not for itself, not for `GR-1`, not for `GR-2` — and no
prospective declaration.

**The seals manifest is closed by this freeze.** From `CV-1`'s landing, no round writes a new
`V1` seal record except a round whose control plane merged before this freeze — that is act 29,
`PRA.json`, and nothing else. `GR1.json` and `GR2.json`, owed under `V1` to "a later round that
names them", are discharged by `V2` certificates and attestation rows for `GR-1` and `GR-2`, not
by `V1` records. A `V1` record for a round that has a `V2` certificate would be a second
representation of the same seal, which is the shape `SI-3` retired.

**The declarations: the same narrow exception, owned here for the third time.** `§A.37` says each
round declares its own integrity baseline. `CV-1` does **not**: `_MANIFEST_BASELINE` stays act
28's, `{'base': '101b8cebb140c2ee7b982641ff005b84bbf0a1cf', 'authorized': ('PFR',)}`, and
`_MANIFEST_PROSPECTIVE` stays `{}`, at every commit of this round. The reason is the one `GR-1`
and `GR-2` recorded: those two lines are among the lines act 29's sealed head already writes, and
a concurrent write from this branch would collide textually with a head that may not move. The
substitute is the same: `R7-CV1`'s own integrity contract requires the seals tree to equal
`92e0956ad6b187fddf77068f33c66e69a012f074`, `B`'s, at every commit of this round up to `E`, and at
`L` to equal the first parent's. The exception ends when act 29 lands; `CV-2` declares under
whatever rule it then lands under.

**The bootstrap.** `CV-1` is certified by `V1` and by nothing it builds: `R7-CV1` carries its
mandated base as a literal, act 10's strengthened ancestry check asked of the real
`pull_request.head.sha` and never of the synthetic merge, three states — `EXECUTION` while no
landing of this round is visible, `LANDED-UNATTESTED` once a canonical landing is,
`ATTESTED` once its attestation row exists — with ancestry and execution shape separate and
reported, a canonical landing being a merge one of whose non-first parents has execution shape,
ancestry against `_CV1_B`, this clause in its guard file and both stage-final artifacts, unique or
fail-closed. `CV-1`'s own certificate carries `protocol: 1` for this reason: it is issued by the
`V1` guard that certifies the round, so the `V2` verifier never certifies the round that installs
it.

***

## `S1` — the `N12` supersession, stated as text and not as prose

**Superseded.** The six lines at 32819–32824 of the guard file at `D`, pinned by content:

- `sha256` of that exact segment at `D`:
  `3a47d54d56aa74e939c70d880cb3c773d81437c43137ee3a7ebc9e7f80e104cc`
- the segment runs from the start of the line
  `    # N12 -- the budget must not tolerate an unrelated edit elsewhere in the R7-GR1 region.`
  through the end of the line
  `        and _gr2_budget(_GR2_SELF) is True and _gr2_budget(tampered) is False)`
- each of those two lines occurs exactly once in the file at `D`.

The execution extracts the segment from the **base's own guard text**, read from git, and requires
that hash before it changes anything.

**What is wrong with it, in `GR-2`'s own terms.** `GR-2`'s freeze, item 4 of its guard: the budget
is "whole-file while executing, and after landing measured against the recovered `E`, so a
sibling round's changes elsewhere in the file are not this round's to answer for". The budget rows
implement that. `N12` does not: its positive half is `_gr2_budget(_GR2_SELF) is True`, with
`_GR2_SELF` the file on the current tree, in every state. Measured on the act 29 synthetic merge
at `D`: `_gr2_budget` of `main`'s guard is `True`, of the merged guard `False`, of the merged
guard tampered `False`; the residue after removing the `R7-GR2` block and reverting both segments
is exactly act 29's three hunks. `N12` fails on its positive half, not because the mutant is
tolerated.

**The replacement.** One edit, and no other edit to the region:

```python
    # N12 -- the budget must not tolerate an unrelated edit elsewhere in the R7-GR1 region. The
    # subject is the lifecycle-scoped one the budget contract itself uses: this file while the
    # round is EXECUTION, the guard text at the recovered E afterwards; an unrecoverable E fails.
    mark = "    \"\"\"Per-line trailing-whitespace normalization; the freeze compares"
    _subj = (_GR2_SELF if _GR2_STATE == 'EXECUTION' else (None if _GR2_E is None else
             (_gr2_git('show', '%s:%s' % (_GR2_E, _GR1_GUARD_PATH)) or b'').decode('utf-8', 'replace')))
    tampered = _subj.replace(mark, mark + ' it', 1) if (_subj and mark in _subj) else None
    row('N12 a budget tolerating an unrelated edit in the R7-GR1 region',
        tampered is not None and tampered != _subj
        and _gr2_budget(_subj) is True and _gr2_budget(tampered) is False)
```

`_gr2_budget` itself is **not** changed: the predicate is the one both the authoritative
`placement-*` rows and `GR-2`'s freeze agree on. Only the object `N12` feeds into it moves, to the
subject those rows already use. The row name is unchanged, so the failure vocabulary a reader of
the log already knows is preserved.

**The five controls, mandatory:**

1. **Pinned and unique.** The superseded segment is extracted from the base's text, hashed, equal
   to the frozen hash, and its two anchor lines each occur once.
2. **The successor-guard demonstration.** On a synthetic repository whose current guard carries an
   unrelated edit outside the `R7-GR2` block with `GR-2`'s history intact: the superseded `N12`,
   compiled from the base's text, fails its positive half; the replacement passes; and the
   replacement's mutant still fails. Measured at `D` on the act 29 synthetic merge with the
   replacement applied, and re-measured by the guard on every build.
3. **`EXECUTION` unchanged.** With the state forced to `EXECUTION` and a live file whose budget
   holds, old and new return the same verdict.
4. **Post-landing reads `E_GR2`, and fails closed.** With the state `LANDED-UNRECORDED`: the
   replacement's subject is the guard at `E_GR2`; with `_GR2_E` forced to `None`, the row fails
   rather than skipping.
5. **The other sixty-two rows are identical.** `R7-GR2` reports 63 checks and 7 control groups
   before and after, and every row but `N12` returns the same verdict on the same inputs.

**Measured at `D`, with the replacement and a stub `R7-CV1` block applied in a scratch worktree:**
the guard ends `ALL CHECKS PASS`, 104 verdict lines, exactly one tag new, `R7-GR2` 63 checks with
no failure in `LANDED-UNRECORDED`, `R7-GR1` 86 with no failure. **No live `V1` contract other than
`N12` is tripped by `CV-1`'s planned guard edits.** That measurement is what licenses the budget
below: the round's diff to the guard file is `S1` and the `R7-CV1` block and nothing else.

***

## The `V2` objects, FROZEN

Six definition slots. Every file under `verification/certificates/` is **data**; the verifier is
**code**; nothing under `verification/certificates/` is executable.

### `V1` — the round certificate

One JSON file per round, `verification/certificates/<STEM>.json`, written **by the round during
its execution** and therefore never containing `E`, `tree(E)`, `L` or its own blob — those belong
to the attestation row, `V2`. Fields, all required unless marked:

| field | content |
|---|---|
| `schema` | the literal `oi-round-certificate` |
| `protocol` | an integer; `2` for a round executed under this protocol, `1` for a round certified by the `V1` guard — every translated round, and `CV-1` itself |
| `round` | the stem, matching the filename |
| `shape` | one of `sealing`, `non-sealing`, `content-only`; a discriminant, never inferred from nulls |
| `directory` | the round's directory under `verification/`, or absent for a `content-only` round with none |
| `control_plane` | an **ordered** list of `{path, blob, merge, execution_affecting}`: the preregistration and each amendment, the `main` merge that brought each in, and whether the artifact moves the execution base; absent for `content-only` |
| `base` | the mandated execution base, 40 lowercase hex; absent for `content-only` |
| `dependencies` | a list of stems whose certificates must be accepted, each of protocol `≤` this certificate's |
| `evidence` | a list of `{id, path, blob}`: every artifact the round certifies as immutable — its preregistration, amendments, result note, tag map, census, seal record. `id` is `<STEM>/<path relative to the round directory>`, or `seals/<STEM>.json` |
| `contributions` | a list of `{path}`: files the round changed that later rounds may change — Lean, tools, workflow, manuscript, the guard |
| `translation` | optional: `{from: "seal-record" \| "guard-block" \| "round-directory", pinned_at: "<D>"}`, present on every certificate `CV-1` writes for a landed round |

Unknown keys, malformed hashes and a `content-only` certificate carrying `base` or
`control_plane` are hard failures.

### `V2` — the attestation ledger

`verification/certificates/attestations.jsonl`, **append-only**, one JSON object per line, one
line per landed round, written at `A`. Fields:

| field | content |
|---|---|
| `round`, `protocol` | as the certificate |
| `kind` | `landed` or `base-only`; a `base-only` row **forbids** the topology fields, including as `null` |
| `certificate` | the blob of `<STEM>.json` at `E` |
| `base` | the mandated base |
| `sealed_head`, `tree`, `landing` | exact `E`, `tree(E)`, exact `L` — `landed` rows only |
| `ci` | `{exact_e: {run, head_sha, conclusion}, exact_l: {…}, main_push: {…}}`, or `"not recorded"` on a translated row |
| `translated` | `true` on rows `CV-1` writes for landed rounds; absent otherwise |

The row is a **historical fact** durably recorded, not a proof that GitHub issued those verdicts;
the verifier checks every git-derivable field and never queries an Actions run. A signed
continuous-integration attestation is an optional later strengthening and nothing here depends on
it.

### `V3` — the conformance corpus

`verification/certificates/conformance/v2/`: one JSON vector per case, each a synthetic-repository
recipe with its expected verdict and named reason, and `expected.json`, the map from vector id to
`{verdict, reason}`. **The corpus is evidence.** The verifier prints the id and verdict of every
vector it executed and the count; the continuous-integration job requires the executed set to
equal the corpus **exactly** — same ids, same verdicts, same count. Implementation is replaceable;
observable protocol semantics are not, and green-by-skipping is a count mismatch.

Families the corpus must contain, each with at least one vector, positive controls included:

- **schema** — each required field missing; a malformed hash; an unknown key; an unknown
  protocol; `content-only` carrying topology; `base-only` carrying topology, including as `null`;
- **ambiguity** — zero and multiple candidates for `B`, for `E`, for `L`;
- **visibility** — the landing reachable from the head only, from the live base-branch tip only,
  from both as one candidate, from both as two different candidates; an unresolvable base ref;
  `pull_request.base.sha` refused; a local branch refused; the synthetic merge refused;
- **artifact class** — an evidence blob changed, removed, or moved without a relocation row;
  moved with one; a relocation fork; two active locations; a contribution changed, which passes;
- **dependency** — protocol 2 depending on 1 passes; 1 depending on 2 fails; a missing dependency
  fails; a dependency whose certificate fails propagates;
- **topology** — recorded `E` unequal to derived; recorded `tree(E)` unequal to `tree(E)`; a
  tree-identical commit with different parents offered as `E`, refused; `L`'s second parent not
  `E`; a rewritten landing;
- **ledger** — a row edited; a row removed; two rows for one round; a certificate blob unequal to
  the row's; a `landed` row missing a topology field;
- **live policy** — the declared clause count unequal to the file's; a clause lacking an owner
  round, a protocol, a schema predicate type, an activation point, an expiry condition or its
  evidence;
- **vacuity** — a verifier that executes fewer vectors than the corpus, or the same count with one
  id substituted;
- **the historical-subject rule** — a negative control that consumes the live file where its
  contract consumes a certified historical subject; the correct verifier evaluates the certified
  subject. This is `N12`'s class, promoted to a vector, and it is the one every future negative
  control is checked against;
- **every preregistered `V1`→`V2` divergence**, each as its own vector: `N12`.

The count is **measured, not predicted**; the rule that every family is represented governs.

### `V4` — the relocation ledger

`verification/certificates/relocations.jsonl`, append-only, rows
`{evidence_id, from, to, blob, authorizing_round}`. A valid relocation moves the same certified
blob from the currently resolved location to the new one: no content change, no duplicate active
location, no missing source, no fork. **The universal live rule:** every evidence id of every
accepted certificate resolves through the relocation chain to exactly one current path carrying
its certified blob. `CV-1` writes an empty ledger and no relocation.

### `V5` — the live policy

`verification/certificates/live-policy.json`: `{protocol, count, policies: [...]}`, every policy
data-only with at least `owner_round`, `protocol`, `predicate` from a finite schema, `activation`,
`expiry` and `evidence`. The verifier reports every policy id and requires `count` to equal the
list's length. **`CV-1` writes `count: 0` and an empty list.** The standing invariants `V1`
carries as code — `SI-3`'s zero-legacy-statement contract among them — migrate, each with its
evidence, in `CV-2`, which is where the escape hatch is first exercised and first bounded.

### `V6` — the verifier

`tools/certificate_verifier.py`, standard library only, dispatching on `protocol` to a frozen
per-version path, with `--mode shadow` (reports; always exits 0) and `--mode authoritative` (exits
non-zero on any failing certificate, row, policy or vector), and `--self-test`. It is a
**contribution**: replaceable, and held to the corpus. Derivations, each fail-closed:

- **`B`** — the `main` merge, in **first-parent order on `main`**, of the last
  `execution_affecting` artifact in the certificate's ordered `control_plane`; the flag is carried
  by the artifact, never inferred. `GR-1`'s two amendments are the mandatory regression.
- **`E`** — derived over the **union of the visibility targets**, `SI-2`'s adjudicated rule: on
  `push` the reachable history of `HEAD`; on `pull_request` the real `pull_request.head.sha` and
  the live `refs/remotes/origin/<base ref>`, never `pull_request.base.sha`, a local branch or the
  synthetic merge. Recorded `sealed_head` must equal the derived candidate, **and separately**
  `tree(derived)` must equal the recorded `tree`. A tree-identical commit with different parents
  is not `E`: the chronology proposition is about ancestry, and a recovery from lost objects, if it
  is ever needed, is an adjudicated mode and not ordinary certification.
- **`L`** — the unique merge in that union whose non-first parent is exactly `E`; recorded
  `landing` must equal it. Zero, multiple and unequal-to-recorded remain three distinct failures.
- **`A`** — the row exists, its `certificate` blob equals the certificate at `E`, and every
  git-derivable field agrees with git.

A new continuous-integration job, `Certificate verifier`, with `fetch-depth: 0`, runs `V6` at
every event. Its mode is a stage of this round, below.

***

## The translation, FROZEN as data

Every `R7` block that is a round receives a certificate; the three that are not — `R7-VIS`,
`R7-ARCH`, the synthetic regressions, and the `R7-SI2` base region at line 10098 — do not, and are
`CV-2`'s to classify as live policy or test code. **Fifty-one certificates**, measured at `D` from
the guard's block markers and the seals manifest: twenty-seven `sealed` and six `base-only`
manifested rounds, two landed-unrecorded rounds, and sixteen content-only rounds that predate
`§A.37` and carry no topology.

Evidence blobs are pinned **at `D`**. A result note some later round corrected forward is
certified as it now stands, and the certificate says so with `translation.pinned_at`; this is a
freezing of the present, not a rewriting of the past, and no artifact is edited to make it
translate. For the twenty-seven `sealed` rounds and for `GR-1` and `GR-2`, an attestation row is
written from the record: `base`, `sealed_head`, `landing`, `tree` derived from git, `ci`
"not recorded", `translated: true`. For the six `base-only` rounds a `base-only` row. For the
content-only rounds, none.

**Measured at `D`: the derivation rule is exact on every row that has topology.** For all
twenty-seven `sealed` records, the unique merge in `D`'s reachable history whose non-first parent
is the sealed head is the pinned merge, that merge's second parent is the sealed head, and the
base is an ancestor of the sealed head. Likewise for `GR-1` (`L_GR1^2 = E_GR1`, one candidate) and
`GR-2` (`L_GR2^2 = E_GR2`, one candidate). This is recorded as a measurement, not a forecast.

| # | stem | tag | seal record at `D` | class | round directory | directory tree at `D` |
|---|---|---|---|---|---|---|
| 1 | `SOI` | `R7-SOI` | — | content-only | `audits/operational` | `—` |
| 2 | `C4R` | `R7-C4R` | — | content-only | `audits/physical-realization/c4-causal-readback` | `—` |
| 3 | `RCH` | `R7-RCH` | — | content-only | `programmes/oi-qm/track-i/recurrence-tightness` | `c4362f61191b` |
| 4 | `SCF` | `R7-SCF` | — | content-only | `programmes/oi-qm/track-i/recurrence-scaling` | `2bdc9bc1f0a1` |
| 5 | `RCL` | `R7-RCL` | — | content-only | `audits/physical-realization/c4-causal-readback` | `—` |
| 6 | `QSTAR` | `R7-QSTAR` | — | content-only | — | — |
| 7 | `SOURCE` | `R7-SOURCE` | — | content-only | `programmes/oi-qm/track-i/arc-d-operational-sourcing` | `bf8bbc2604d2` |
| 8 | `BRIDGE` | `R7-BRIDGE` | — | content-only | `programmes/oi-qm/track-b/act-01-indivisibility` | `2dc2b2ca7ee9` |
| 9 | `TBRIDGE` | `R7-TBRIDGE` | — | content-only | `programmes/oi-qm/track-b/act-02-transpose-bridge` | `df4841890507` |
| 10 | `CAND` | `R7-CAND` | — | content-only | `programmes/oi-qm/track-b/act-03-candidate-selection` | `8a5dac49471d` |
| 11 | `DILMAP` | `R7-DILMAP` | — | content-only | `programmes/oi-qm/track-b/act-04-dilation-mapping` | `2f4917a58ec4` |
| 12 | `SRCA` | `R7-SRCA` | — | content-only | `programmes/oi-qm/track-b/act-05-source-a-candidate` | `cc79c3f1db83` |
| 13 | `TUPLE` | `R7-TUPLE` | — | content-only | `programmes/oi-qm/track-b/act-06-tuple-instantiation` | `e8336b9c3cbf` |
| 14 | `DILCH` | `R7-DILCH` | — | content-only | `programmes/oi-qm/track-b/act-07-dilation-choice` | `ca3d76c0578b` |
| 15 | `DILL2` | `R7-DILL2` | — | content-only | `programmes/oi-qm/track-b/act-07-dilation-choice` | `ca3d76c0578b` |
| 16 | `RBR` | `R7-RBR` | `base-only` `24dc899b845a` | manifested | `programmes/oi-qm/track-b/act-09-readback-robustness` | `646bb1f230e1` |
| 17 | `ABR` | `R7-ABR` | `base-only` `1a6181bd097d` | manifested | `programmes/oi-qm/track-b/act-10-anchor-robustness` | `1d90cc494b6d` |
| 18 | `HYA` | `R7-HYA` | `sealed` `9625115f78d6` | manifested | `programmes/hydrodynamics/round-h-a-source-audit` | `45b7c9d858e3` |
| 19 | `CLG` | `R7-CLG` | `base-only` `686ef7af0d6b` | manifested | `programmes/oi-qm/track-b/act-11-coherent-lift-gauge` | `8711e5b21fb8` |
| 20 | `TSG` | `R7-TSG` | `base-only` `55bb13a52bae` | manifested | `programmes/oi-qm/track-b/act-12-two-sided-gauge` | `e01f259c020a` |
| 21 | `SGT` | `R7-SGT` | `sealed` `2ff4f68bd5e4` | manifested | `programmes/substratum/lemma-24-1-semigroup-transfer` | `8bfc0ec0aac3` |
| 22 | `A11P` | `R7-A11P` | — | content-only | — | — |
| 23 | `A12P` | `R7-A12P` | `sealed` `fb46a870866b` | manifested | — | — |
| 24 | `CTI` | `R7-CTI` | `sealed` `100ba4994dea` | manifested | `programmes/oi-qm/track-b/act-13-cross-time-invariants` | `133626f3c48f` |
| 25 | `PQT` | `R7-PQT` | `sealed` `8ca866fd80c0` | manifested | `programmes/oi-qm/track-b/act-14-threading-observability` | `4b8a45fb3a7f` |
| 26 | `HYB` | `R7-HYB` | `sealed` `7235e5411677` | manifested | `programmes/hydrodynamics/round-h-b-reversible-fluid-substratum` | `b3c55b9074b3` |
| 27 | `A6P` | `R7-A6P` | `sealed` `0f42d74c71b5` | manifested | `programmes/substratum/a6-background-independence` | `c089848ae9c1` |
| 28 | `WTS` | `R7-WTS` | `sealed` `27104c27c5ca` | manifested | `programmes/substratum/lemma-24-1a-word-trace-sufficiency` | `745659bf61da` |
| 29 | `PC4` | `R7-PC4` | `sealed` `d309359cc3a2` | manifested | `programmes/physical-realization/round-c4-1-physical-discharge` | `b5704b1a12d4` |
| 30 | `PC4S` | `R7-PC4S` | `sealed` `acd4aa0eb07c` | manifested | `programmes/physical-realization/round-c4-2-storage-readback` | `df73bd9b6a82` |
| 31 | `A6D` | `R7-A6D` | `sealed` `3b3f2e1d5491` | manifested | `programmes/substratum/a6-background-independence` | `c089848ae9c1` |
| 32 | `A6I` | `R7-A6I` | `sealed` `a57b7eca74b0` | manifested | `programmes/substratum/a6-instantiation` | `5b5d24d54d50` |
| 33 | `HYE` | `R7-HYE` | `sealed` `55b5c811c23a` | manifested | `programmes/hydrodynamics/round-h-e-h3-closure-bridge` | `b9183db2cd2e` |
| 34 | `TCF` | `R7-TCF` | `sealed` `635a4f0c3d8f` | manifested | `programmes/oi-qm/track-b/act-15-pq3d-cancellation-fork` | `c3bac7c03a4d` |
| 35 | `RNC` | `R7-RNC` | `sealed` `a3dc61afb728` | manifested | `programmes/oi-qm/track-b/act-16-reanchored-channel-cancellation` | `a879eb8ad652` |
| 36 | `TRJ` | `R7-TRJ` | `sealed` `e2f327f03847` | manifested | `programmes/oi-qm/track-b/act-17-gram-trajectory-selection` | `3d259d03e19e` |
| 37 | `XTS` | `R7-XTS` | `sealed` `b481dbbdb8b6` | manifested | `programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure` | `5419c2fcac80` |
| 38 | `RNT` | `R7-RNT` | `sealed` `546965414aa4` | manifested | `programmes/oi-qm/track-b/act-20-representative-naturality` | `f60bb11ace71` |
| 39 | `OLT` | `R7-OLT` | `sealed` `8ed0ef539141` | manifested | `programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted` | `bc0663e8c0ed` |
| 40 | `OLN` | `R7-OLN` | `sealed` `1552065eeae2` | manifested | `programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization` | `c5a65df2ece9` |
| 41 | `OLG` | `R7-OLG` | `sealed` `8a058df23c07` | manifested | `programmes/oi-qm/track-b/act-23-orbit-law-gaps` | `00ef0e0cc0f3` |
| 42 | `OGS` | `R7-OGS` | `sealed` `5436e01852e9` | manifested | `programmes/oi-qm/track-b/act-24-orbit-geometry-selector` | `5500ab432ca5` |
| 43 | `OGC` | `R7-OGC` | `sealed` `6674357ff7a5` | manifested | `programmes/oi-qm/track-b/act-25-orbit-geometry-isometries` | `1adf564a2885` |
| 44 | `CGR` | `R7-CGR` | `sealed` `5a1c18831a6c` | manifested | `programmes/oi-qm/track-b/act-26-orbit-geometry-rigidity` | `f2bb67e5b01b` |
| 45 | `NLV` | `R7-NLV` | `sealed` `752f88a91e6c` | manifested | `programmes/oi-qm/track-b/act-27-strict-natural-lift` | `b8ba77edcbee` |
| 46 | `PFR` | `R7-PFR` | `sealed` `d09a24ff6895` | manifested | `programmes/oi-qm/track-b/act-28-product-locus-freedom` | `ca879832b41c` |
| 47 | `SI1` | `R7-SI1` | `base-only` `9cefa2001d2e` | manifested | `infrastructure/round-si-1-shadow-seal-validator` | `cdf5287753dd` |
| 48 | `SI2` | `R7-SI2` | `base-only` `7cc81e5be6fb` | manifested | `infrastructure/round-si-2-authority-cutover` | `e872ba9a4730` |
| 49 | `SI3` | `R7-SI3` | `sealed` `7c447c3fff08` | manifested | `infrastructure/round-si-3-legacy-seal-retirement` | `6ded263dce33` |
| 50 | `GR1` | `R7-GR1` | — | landed-unrecorded | `infrastructure/round-gr-1-roadmap-entry-scoping` | `e71ced1daf60` |
| 51 | `GR2` | `R7-GR2` | — | landed-unrecorded | `infrastructure/round-gr-2-post-landing-scoping` | `70bb6b68573a` |

Four rows carry no directory: `QSTAR` and `A11P` cite artifacts by name that resolve to no round
directory, and `A12P` and `SOI`/`C4R`/`RCL` cite audit directories or none. The execution resolves
each of those four from the block's own `_artifact` names and records the resolution; a stem whose
evidence set cannot be resolved is a certificate with an empty `evidence` list, reported as such,
and not a certificate invented from prose. Directory trees are cited at twelve hex here and at
forty in the certificates.

***

## The live-read census, measured at `D`, and what it is for

What each historical block reads on the live tree, by class, counted from the block's string
literals resolved against `D`'s tree and the migration manifest. Totals over the fifty-one round
blocks: **own artifacts 58, other rounds' artifacts 31, manuscripts 54, Lean sources 15,
`ROADMAP`/`README`/`AGENTS` 33, the guard file itself 12, git 132.** The per-block table is
carried in the result note as data. This census is an **inventory for `CV-2`**, not a target of
this round: it says which classes of live read the retirement must dispose of, and `CV-2`'s freeze
decides each class — own and other rounds' artifacts become evidence pins and dependencies;
manuscript sentences are adjudicated one by one against the coverage ledger and the manuscript
census, which are the generic instruments for that job; `ROADMAP` cells are retired with the queue
they describe; guard self-reads are retired with the guard. Nothing here decides any of that.

***

## The order is part of the contract, and the final head is the checkpoint

| stage | what it does | may not begin until |
|---|---|---|
| 1 | `CV1-1`: `S1`, the `N12` supersession, and nothing else. Checkpoint: the guard green at the fixed head, both hashes verified, the emitted tag set equal to the base's | — |
| 2 | `V1`, `V3`, `V4`, `V5` written; the fifty-one certificates and their attestation rows translated; the corpus written | stage 1 |
| 3 | `V6` built; the `Certificate verifier` job added to `verify.yml` in **`--mode shadow`**; `R7-CV1` added, with its chronology, its integrity contract, the five `S1` controls, and its artifact contracts | stage 2 |
| 4 | the shadow census `CV1-6` at this stage's head, **committed as `census.json`** | stage 3, and the corpus exact |
| 5 | the job's mode set to **`--mode authoritative`** — dual gating | stage 4's census matches the adjudicated profile |
| 6 | the result note and the tag map; the census **re-measured at this head** and required equal to stage 4's | stage 5 |
| — | this commit is the candidate `E` | everything above |

**Durability.** Because nothing is deleted, `E` is the checkpoint: the census that licenses dual
gating is measured at the commit that carries it, re-measured at `E`, and `CV-2` begins from a
world in which both are in the tree. A local measurement taken before some later commit is not
evidence and is not what `CV1-6` accepts.

Each checkpoint is run with `HEAD` fixed for the whole run, the stage committed first, and `HEAD`
and the dirty-file count logged at the start and the end.

***

## The targets, FROZEN

Each target names the artifact that decides it, and is decided only by that artifact.

- **`CV1-0` — the start state holds at `B`**: the pinned blobs below; the `N12` segment present
  with its frozen hash and unique anchors; `GR-2` `LANDED-UNRECORDED` with `E_GR2` and `L_GR2`
  recoverable and `tree(E_GR2)` as frozen; the seals tree `92e0956ad6b187fddf77068f33c66e69a012f074`;
  no `verification/certificates/`; no `PRA.json`; the declarations act 28's. Outcomes: `HOLD` /
  `DEVIATED`. `DEVIATED` stops the round.
- **`CV1-1` — `S1` as frozen**, with its five controls. Outcomes: `SUPERSEDED-AS-FROZEN` /
  `SUPERSEDED-DEVIATED`.
- **`CV1-2` — the certificates.** Fifty-one certificates validating against `V1`, each
  translated from the source the table names, evidence pinned at `D`, and the attestation ledger
  carrying twenty-nine `landed` rows and six `base-only` rows. Outcomes:
  `CERTIFICATES-TRANSLATED` / `CERTIFICATES-INCOMPLETE`, the latter naming each stem.
- **`CV1-3` — the verifier and the corpus.** `V6` built with its four derivations and its
  self-test; every family of `V3` represented; the executed vector set equal to the corpus. The
  count is measured and recorded. Outcomes: `CONFORMANCE-EXACT` / `CONFORMANCE-PARTIAL`, naming
  each family or vector that does not behave.
- **`CV1-4` — the derivations on the record.** `B` derived for every certificate with a control
  plane and equal to the recorded base; `E` and `L` derived for every `landed` row and equal to the
  recorded values with `tree(E)` equal. Outcomes: `DERIVE-EXACT` / `DERIVE-PARTIAL`, naming each
  disagreement.
- **`CV1-5` — the live rules in shadow.** The evidence rule over all fifty-one certificates and
  the empty relocation ledger, and the live policy with `count: 0`, both evaluated and reported by
  the shadow job, gating nothing. Outcomes: `LIVE-RULES-SHADOWED` / `LIVE-RULES-ABSENT`.
- **`CV1-6` — the differential census, at the stage-4 head and again at `E`.** For each of the
  fifty-one certificates, the `V1` verdict — the block's own `R7` tag at that head, and for a
  manifested round the keyed `U3` lifecycle and verdict from the same guard run — beside the `V2`
  verdict on each axis it has: `evidence` for all fifty-one, `topology` for the twenty-nine
  `landed` rows, `base` for the six `base-only` rows. And for each control: the twenty `SI-1`
  cases and the eleven `SI-2` cases re-executed, each classified `agree`, `no-analogue` (a `V1`
  lifecycle notion `V2` does not have: `LANDED-PENDING-PIN`, `seal pending`, the legacy
  inventory) or `diverge`; the `V2` corpus; and **`C-N12`**: `R7-GR2` as it stood at `B`,
  reconstructed from the base's text and executed at the census head, beside `V2`'s verdict on
  `GR2`'s certificate. The frozen profile, stated so it can fail: **every record row agrees on
  every axis; every comparable control agrees; `C-N12` diverges — the reconstructed `N12` fails
  its positive half, `V2` passes — and it is the only divergence.** Outcomes:
  `CENSUS-AS-ADJUDICATED` / `CENSUS-UNEXPECTED` / `CENSUS-BROKEN`. `CENSUS-UNEXPECTED` is any
  other divergence, or `C-N12` agreeing; it is reported, not repaired, and **stops the round
  before stage 5**. `CENSUS-BROKEN` is a record-axis disagreement.
- **`CV1-7` — dual gating.** The job runs `--mode authoritative` at `E`; the `V1` guard is
  unchanged in verdict and in every existing tag; both gate. Outcomes: `DUAL-GATING` /
  `NOT-GATING`.
- **`CV1-8` — the verdict map and the budget.** (a) The base's own guard file is run; every tag it
  emits returns the same verdict at `E`, and `E` emits exactly one tag the base does not,
  `R7-CV1`: `MAP-PRESERVED` / `MAP-MOVED`. (b) The guard at `E`, with the `R7-CV1` block removed
  and `S1` reverted to the base's segment, equals the base's guard file byte for byte —
  **whole-file while executing, and after landing measured against the recovered `E`**, as `GR-2`
  froze and as `N12` now respects: `BUDGET-HELD` / `BUDGET-EXCEEDED`. The two rules govern; a
  cardinality differing from the prediction below is recorded, not repaired.
- **`CV1-9` — non-deletion, checked mechanically.** The execution's diff against `B` deletes no
  `R7-*` block, no clause, no seal record, no validator region text, and edits no file under
  `verification/seals/`, `verification/programmes/` or `verification/audits/`; the only edits to
  existing files are `S1`, the `R7-CV1` block, one job in `verify.yml`, and one ledger section in
  `verification/README.md`. Outcomes: `ADDITIVE` / `NOT-ADDITIVE`, the latter failing the round.

***

## The preregistered predictions, with signs, strengths and recorded reasons

| target | prediction | strength | recorded reason |
|---|---|---|---|
| `CV1-0` | `HOLD` | HIGH | each item measured at `D`; nothing between `D` and `B` but this file |
| `CV1-1` | `SUPERSEDED-AS-FROZEN` | HIGH | the replacement is written and was measured at `D` on two trees |
| `CV1-2` | `CERTIFICATES-TRANSLATED` | MEDIUM | four stems resolve to no directory and are the likely `INCOMPLETE` |
| `CV1-3` | `CONFORMANCE-EXACT` | MEDIUM | the corpus is the largest object here and the one most likely to be short a family on first pass; the count is not predicted |
| `CV1-4` | `DERIVE-EXACT` | HIGH | measured at `D`: 27 of 27 sealed, and both landed-unrecorded rounds, exact |
| `CV1-5` | `LIVE-RULES-SHADOWED` | HIGH | both rules are trivial on a tree nothing has moved on |
| `CV1-6` | `CENSUS-AS-ADJUDICATED`, `C-N12` the sole divergence | MEDIUM | the record rows should agree because `V2` asks less of each round than `V1` at a fixed head; the controls are where a misreading would show |
| `CV1-7` | `DUAL-GATING` | HIGH | a job flag |
| `CV1-8` | `MAP-PRESERVED`, `BUDGET-HELD`; the base emits **103** tags and `E` **104** | HIGH; the count MODERATE | measured at `D` with the stub: 104, one new |
| `CV1-9` | `ADDITIVE` | HIGH | the diff is enumerated above |

One reading of what the repairs imply, not a target: with `CV-1` landed, a fresh `pull_request`
build of act 29's **unchanged** head against `main` has `R7-GR2` green in `LANDED-UNRECORDED`,
joining `R7-GR1`, `R7-PFR` and `R7-PRA`, all four of which were green on the candidate merge
measured in run 35694203310 except `R7-GR2`. **Measured at `D`** on the act 29 synthetic merge —
`effd5c86` with `bf7e96fe` merged, the tree run 35694203310 evaluated — with `S1` applied and
nothing else, under a mimicked `pull_request` event naming that head and `refs/remotes/origin/main`:
the guard ends `ALL CHECKS PASS`, 104 verdict lines, no failure; `R7-GR2` 63 checks with no
failure in `LANDED-UNRECORDED`; `R7-PRA` 216 checks with no failure, `EXECUTION` certified against
`0bedff07`; `R7-GR1` 86 and `R7-PFR` 164 with no failure. That is the second successor-guard
measurement of `S1` and the direct falsifier of the third defect above turned green by one
segment. Act 29's certification is act 29's, and this round neither reports nor depends on it.

***

## The STATUS RULE, FROZEN

- A target is decided only by the artifact it names: a certificate by its bytes, a verifier
  property by an executed vector, an agreement by the census.
- `CENSUS-AS-ADJUDICATED` is **not** a claim that `V2` is correct. It is a claim that two
  implementations agree on the cases presented, with one divergence they were told in advance to
  have. Both could be wrong together; the frozen sentence says so.
- `CENSUS-UNEXPECTED` **stops the round before stage 5**. The mode is not flipped over a
  divergence this freeze did not name, whatever the argument for it.
- `NOT-ADDITIVE` on `CV1-9` **fails the round**: it means the round did the thing it promised
  not to do.
- No outcome licenses any sentence that `V1` has been superseded, replaced or made a shadow.

## The frozen post-round sentences

**`CV1-6`, `CENSUS-AS-ADJUDICATED`:** "On every one of the fifty-one certificates, and on every
comparable control, the `V1` guard and the `V2` verifier returned the same verdict at the same
head, and they differed on exactly one control, `C-N12`, in the direction this freeze named: the
superseded `N12`, reconstructed from the base's text, fails its positive half on a tree that
carries a later edit, and `V2`, which evaluates `GR-2`'s certified subject, passes. This is an
agreement census with one adjudicated divergence and not a proof of correctness."

**`CV1-6`, `CENSUS-UNEXPECTED`:** "The two implementations disagreed on the rows named below,
which this freeze did not name. Both verdicts are recorded. The round stopped before dual gating
and changed neither implementation to remove the disagreement."

**`CV1-7`, `DUAL-GATING`:** "From this head the `V2` verifier gates every event alongside the `V1`
guard. `V1` gates exactly as it did at the base, on every tag it carried there. Authority has not
moved; a second gate has been added, and `CV-2` is where the first is retired."

***

## What no outcome of this round licenses

1. Any deletion, weakening or bypass of an existing check, clause, region or seal record.
2. Any change to a historical `B`, `E`, `L`, `P`, preregistration or result note.
3. Any claim that `V2` is *correct*, as distinct from *in agreement where it agrees, adjudicated
   where it differs, and now gating*.
4. Any sentence that `V1` is superseded, replaced, retired or a shadow.
5. Any change to act 29's head, any edit to `#705`, or any statement about act 29's targets.
6. Any `V1` seal record for `GR-1`, `GR-2` or `CV-1`.
7. Any executable live-tree assertion beyond `R7-CV1`'s own contracts, which are scoped to this
   round's own history after landing and are themselves retired by `CV-2`.
8. Any claim that `CV-2` is safe because `CV-1` was green.

***

## The sequence between the two rounds, stated because the plan depends on it

Act 29 is a `V1` sealing round: its frozen landing is `E` → `L` → `P` with `P` writing
`verification/seals/PRA.json` and removing its prospective declaration, and its head carries the
`R7-PRA` block at line 28225 of the guard. That head **cannot** merge into a `main` from which
`CV-2` has removed the `V1` machinery, and its freeze cannot be reinterpreted to land any other
way. Therefore, in order:

1. `CV-1` lands and its `main` push run is certified; `A_CV1` is appended and certified.
2. `#705` is closed and reopened, unchanged; the expectation is four green jobs with `R7-GR2`
   green in `LANDED-UNRECORDED`, and `V2` in `--mode authoritative` reporting `PRA` as absent from
   the certificate set and gating nothing about it.
3. Act 29 lands under `V1`: `L`, `P` writing `PRA.json`, certified.
4. `CV-2`'s control plane is written from that world, translating `PRA` and retiring `V1`.

`PRA` stays under `V1`'s sole authority throughout `CV-1`; `V2` neither classifies nor gates a
round in flight under the old protocol. A `V2` verifier that attempted to implement `V1`'s
prospective state machine for `PRA` would be reimplementing what `CV-2` deletes.

***

## Named hazards

**`H1` — self-certification.** `CV-1` is certified by `R7-CV1`'s `V1` bootstrap guard, the
exact-head runs and the `main` push run, never by `V6`. `CV-1`'s certificate carries `protocol: 1`
for that reason.

**`H2` — dual gating reddens `main`.** From stage 5 a `V6` defect fails every build. That is the
cost of a gate and is accepted; what is not accepted is a `V6` that passes by skipping, which the
exact-count rule in `V3` exists to catch.

**`H3` — agreement mistaken for correctness.** The census sentence says in terms what it is not.

**`H4` — `tree(E)` inside `E`.** The certificate is written at execution and cannot contain
`E`'s SHA, `tree(E)`, `L` or its own blob; those belong to `A`. A certificate found carrying any of
them is a schema failure, and the corpus carries the vector.

**`H5` — tree-equivalence.** A commit with `tree(E)` and other parents is not `E`. The corpus
carries the vector, and the verifier records both `E` and `tree(E)` and requires both.

**`H6` — external state as evidence.** Branch protection is operational defence, not an axiom of
validity; the ledger restores git-object evidence for `E`, `tree(E)` and `L`. Continuous-integration
identities in a row are recorded facts and are never re-queried.

**`H7` — the evidence rule breaking a migration.** Paths are pinned through the relocation ledger
and not directly; the ninety-one-artifact layout migration this repository already performed is the
regression the `artifact class` family models.

**`H8` — the live-policy file regrowing the guard.** Data-only, schema-bound, owner-and-expiry
per clause, exact-count. `CV-1` writes zero clauses. The metric above is the standing test.

**`H9` — the concurrent line.** The two declarations are not edited; `R7-CV1`'s integrity
contract is the substitute, as in `GR-1` and `GR-2`.

**`H10` — scope creep into `CV-2`.** Nothing is deleted; `AGENTS.md` is not edited; the guard
checks that no file under `verification/infrastructure/round-cv-2-*` exists at `E`.

**`H11` — the four unresolved stems.** A certificate whose evidence cannot be resolved from the
block's own names is reported with an empty evidence list, never filled in from prose.

**`H12` — the token `CV1`/`CV2` at `D`.** Both are free at `D` as whole words and as every prefix
form checked below.

***

## Definition budget

**Six** slots — `V1` through `V6` — and the execution may fire no more. The corpus vectors, the
census harness, the translation script and the `S1` controls are test code and data, not
definition slots. No slot may introduce a round-specific branch: no stem appears in `V6`'s logic,
and `R7-CV1` checks that mechanically against the verifier's source.

## Evidence level

Level 2 — executed code with recorded output — for `CV1-1` through `CV1-9`. `CV1-0` is a bounded
mechanical check. The live-read census is an inventory of type P and is out of any table of
certified results.

***

## Start state, pinned

Measured at `D`, read from git:

| path | blob or tree at `D` |
|---|---|
| `verification/lean/edge_rigidity_probe.py` | `558263cb322e0301745c8c1f312d9afdd8d4130b` |
| `verification/seals` (tree) | `92e0956ad6b187fddf77068f33c66e69a012f074` |
| `verification/infrastructure` (tree) | `40be16b2bc86ee6165f61b6e69ac53610f181d94` |
| `AGENTS.md` | `a9687b39c69973d35a2ff81c257687071fd35eca` |
| `.github/workflows/verify.yml` | `d0040de87341445b0d5c5928e34002be190212c8` |
| `tools/release_gate.py` | `819833f480af3bc20aa1a40dbcdc79582a136e89` |
| `verification/README.md` | `8bef177b48d621a590e75779f9e5c0843bc25b7f` |
| `verification/ROADMAP.md` | `d0658c99b6ef13d984fd533760393c0b4a2e43c7` |

Evidence inventory at `D`: 62 preregistrations, 16 amendments, 53 result notes, 2 `census.json`,
5 tag maps, 33 seal records; 59 round directories; 51 round blocks.

### Files this round reads AND writes

- `verification/lean/edge_rigidity_probe.py` — `S1`; the `R7-CV1` block appended after
  `# ---- R7-GR2 ends.`; nothing else.
- `.github/workflows/verify.yml` — one job added.
- `verification/README.md` — one ledger section appended, in the form `SI-1`'s, `SI-2`'s and
  `SI-3`'s take. No live contract pins that file's blob at `D`; three blocks read it for
  sentences, none of which this section touches.
- `tools/certificate_verifier.py` — created.
- `verification/certificates/**` — created: fifty-one certificates, `attestations.jsonl`,
  `relocations.jsonl`, `live-policy.json`, `conformance/v2/**`.
- `verification/infrastructure/round-cv-1-certificate-protocol/{result.md, census.json,
  cv1-tagmap.json}` — created.

### Files this round reads and MUST NOT write

`AGENTS.md`; `verification/ROADMAP.md`; `tools/release_gate.py`; every file under
`verification/seals/`, `verification/programmes/` and `verification/audits/`; every `.lean` file;
every file under `papers/` and `book/`; the two declaration lines. The guard checks each
mechanically against the execution's diff.

### Name freedom, at `D`

`R7-CV1`, `_CV1`, `round-cv-1`, `cv1_`, `cv1-`, `certificate-protocol`, `R7-CV2`, `_CV2`,
`round-cv-2`, `certificate_verifier`, `attestations.jsonl`, `relocations.jsonl`,
`live-policy.json`, `conformance/` and `verification/certificates` each return nothing at `D`;
`CV1` and `CV2` return nothing as whole words.

***

## Preconditions

```control-plane-preconditions
d: effd5c865dfcc207624712a6711a54b712642f48
merged: false
frozen-blob: verification/lean/edge_rigidity_probe.py 558263cb322e0301745c8c1f312d9afdd8d4130b
frozen-blob: AGENTS.md a9687b39c69973d35a2ff81c257687071fd35eca
frozen-blob: .github/workflows/verify.yml d0040de87341445b0d5c5928e34002be190212c8
# row 1: name freedom, drafting-time facts
{"id": "d1-tag-free", "scope": "D", "check": "git grep -l -- 'R7-CV1' $D", "expect": "empty"}
{"id": "d1-stem-free", "scope": "D", "check": "git grep -l -- '_CV1' $D", "expect": "empty"}
{"id": "d1-dir-free", "scope": "D", "check": "git grep -l -- 'round-cv-1' $D", "expect": "empty"}
{"id": "d1-dir-suffix-free", "scope": "D", "check": "git grep -l -- 'certificate-protocol' $D", "expect": "empty"}
{"id": "d1-helper-prefix-free", "scope": "D", "check": "git grep -l -- 'cv1_' $D", "expect": "empty"}
{"id": "d1-verifier-free", "scope": "D", "check": "git grep -l -- 'certificate_verifier' $D", "expect": "empty"}
{"id": "d1-certdir-free", "scope": "D", "check": "git grep -l -- 'verification/certificates' $D", "expect": "empty"}
{"id": "d1-next-round-free", "scope": "D", "check": "git grep -l -- 'round-cv-2' $D", "expect": "empty"}
{"id": "d1-bare-word-free", "scope": "D", "check": "git grep -l -w -- 'CV1' $D", "expect": "empty"}
# row 2: the trees at D
{"id": "d2-seals-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/seals)\" = 92e0956ad6b187fddf77068f33c66e69a012f074", "expect": "exit0"}
{"id": "d2-infra-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/infrastructure)\" = 40be16b2bc86ee6165f61b6e69ac53610f181d94", "expect": "exit0"}
# row 3: provenance
{"id": "db3-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
{"id": "db3-seals-tree", "scope": "D->B", "check": "test \"$(git rev-parse $REF:verification/seals)\" = 92e0956ad6b187fddf77068f33c66e69a012f074", "expect": "exit0"}
# row 4: no execution object at B; the names occur in this file, so the guard and the tree are read directly and never through git grep
{"id": "b4-guard-clean", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e 'R7-CV1' -e '_CV1' -e '_cv1_'", "expect": "empty"}
{"id": "b4-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-cv-1-certificate-protocol/ | grep -v -e '/preregistration.md$'", "expect": "empty"}
{"id": "b4-no-certificates-dir", "scope": "B", "check": "git ls-tree --name-only $REF verification/ | grep -e '^verification/certificates$'", "expect": "empty"}
{"id": "b4-no-verifier", "scope": "B", "check": "git ls-tree --name-only $REF tools/ | grep -e 'certificate_verifier'", "expect": "empty"}
{"id": "b4-workflow-unchanged", "scope": "B", "check": "test \"$(git rev-parse $REF:.github/workflows/verify.yml)\" = d0040de87341445b0d5c5928e34002be190212c8", "expect": "exit0"}
# row 5: S1's superseded segment is present at B, with its frozen hash, and each anchor occurs once
{"id": "b5-n12-segment-hash", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | sed -n '/^    # N12 -- the budget must not tolerate an unrelated edit elsewhere in the R7-GR1 region\\.$/,/^        and _gr2_budget(_GR2_SELF) is True and _gr2_budget(tampered) is False)$/p' | sha256sum | cut -d' ' -f1 | grep -x '3a47d54d56aa74e939c70d880cb3c773d81437c43137ee3a7ebc9e7f80e104cc'", "expect": "nonempty"}
{"id": "b5-n12-open-once", "scope": "B", "check": "test \"$(git show $REF:verification/lean/edge_rigidity_probe.py | grep -c '^    # N12 -- the budget must not tolerate an unrelated edit elsewhere in the R7-GR1 region\\.$')\" = 1", "expect": "exit0"}
{"id": "b5-n12-close-once", "scope": "B", "check": "test \"$(git show $REF:verification/lean/edge_rigidity_probe.py | grep -c '^        and _gr2_budget(_GR2_SELF) is True and _gr2_budget(tampered) is False)$')\" = 1", "expect": "exit0"}
{"id": "b5-budget-unchanged", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -x 'def _gr2_budget(src):'", "expect": "nonempty"}
# row 6: the declarations at B are act 28's, which this round retains
{"id": "b6-prospective-empty", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -x \"_MANIFEST_PROSPECTIVE = {}\"", "expect": "nonempty"}
{"id": "b6-baseline-act28", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -x \"_MANIFEST_BASELINE = {'base': '101b8cebb140c2ee7b982641ff005b84bbf0a1cf', 'authorized': ('PFR',)}\"", "expect": "nonempty"}
# row 7: GR-2 is landed and unrecorded at B, with its history present and its tree as frozen
{"id": "b7-gr2-clause-present", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"check('R7-GR2'\"", "expect": "nonempty"}
{"id": "b7-gr2-no-record", "scope": "B", "check": "git ls-tree --name-only $REF verification/seals/ | grep -e 'GR2.json' -e 'GR1.json'", "expect": "empty"}
{"id": "b7-gr2-landing-reachable", "scope": "B", "check": "git merge-base --is-ancestor 4caa5634363ac8746dff8cc4ce86f55f292e4b6f $REF", "expect": "exit0"}
{"id": "b7-gr2-landing-second-parent", "scope": "B", "check": "test \"$(git rev-parse 4caa5634363ac8746dff8cc4ce86f55f292e4b6f^2)\" = 0a61ea0ad6f6a28687203495ac9b29395f506178", "expect": "exit0"}
{"id": "b7-gr2-tree", "scope": "B", "check": "test \"$(git rev-parse 0a61ea0ad6f6a28687203495ac9b29395f506178^{tree})\" = 794ffc3cd816e6ea4fc60c49999219f8e5e5d7b2", "expect": "exit0"}
{"id": "b7-gr1-landing-second-parent", "scope": "B", "check": "test \"$(git rev-parse 13ffc7372d52c16bdb0e24935aa617deb67e7c51^2)\" = 8d08f8c913f4bb9ef413114ecceb2f72d72d8213", "expect": "exit0"}
# row 8: act 29 has not landed at B: no PRA record, no R7-PRA clause on main
{"id": "b8-no-pra-record", "scope": "B", "check": "git ls-tree --name-only $REF verification/seals/ | grep -e 'PRA.json'", "expect": "empty"}
{"id": "b8-no-pra-clause", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"check('R7-PRA'\"", "expect": "empty"}
# row 9: the manifest is exactly the thirty-three records this freeze translates
{"id": "b9-manifest-count", "scope": "B", "check": "test \"$(git ls-tree --name-only $REF verification/seals/ | grep -c '\\.json$')\" = 33", "expect": "exit0"}
# row 10: this control plane at its path
{"id": "b10-self-present", "scope": "B", "check": "git ls-tree --name-only $REF verification/infrastructure/round-cv-1-certificate-protocol/preregistration.md", "expect": "nonempty"}
```

***

## The guard

`R7-CV1` carries, each contract mutation-tested:

1. **The frozen blob.** This file at this path, pinned by blob with a one-byte drift control.
2. **`S1`**: the superseded segment extracted from the base's text and hashed; the five controls.
3. **The chronology**, as frozen above, ancestry and shape separate and reported, asked of the
   real `pull_request.head.sha` and the live base-branch tip, never the synthetic merge.
4. **The seals tree** byte-identical to `B`'s at every commit up to `E`; at `L`, equal to the
   first parent's.
5. **The declarations** unchanged, act 28's, at every commit of this round.
6. **No `V1` record** for `GR1`, `GR2` or `CV1`; no legacy-shaped `_CV1_(BASE|SEALED_HEAD|MERGE)`
   name.
7. **Non-deletion**, `CV1-9`, against the execution's diff.
8. **The verifier is stem-free**: no round stem in `tools/certificate_verifier.py`.
9. **The corpus is exact**: the executed vector set equals the corpus, at every build.
10. **The census** is committed and, at `E`, equal to the stage-4 census.
11. **The budget and the verdict map**, `CV1-8`, lifecycle-scoped exactly as `GR-2`'s.
12. **The artifact contracts**, `result.md`, `census.json`, `cv1-tagmap.json`, at their blobs at
    `E` after landing and on the live tree only while executing.
13. **No `CV-2` object** at `E`.

***

## The landing shape

`E` → `L` → `A`, under `§A.37` as amended by `SI3-6`, with no `P`:

- **`E`** is the stage-6 commit, certified by exact-head continuous integration on all five jobs.
- **`L`** has current green `main` as first parent and exactly `E` as second. It writes nothing.
  Full continuous integration passes again on exact `L` before the pull request merges, and the
  resulting `main` push run is green before anything else lands.
- **`A`** is a pull request from certified `main` carrying **one commit whose diff is exactly one
  appended line** of `attestations.jsonl`: `CV1`'s row, `protocol: 1`, `kind: landed`, with the
  certificate blob at `E`, `base`, `sealed_head`, `tree`, `landing`, and the three run identities
  with their conclusions. `V6` in authoritative mode validates the row against git on `A`'s own
  build; `R7-CV1` moves to `ATTESTED` on it. `A` merges only after that build is green, and
  nothing else lands between `L` and `A`.

***

## Execution discipline

The execution begins only from the certified merge of this control plane and from nothing else,
and its first act is to verify this file's blob at that base. It absorbs no later `main` before
`E` is certified. A divergence between this freeze and what the execution measures is **recorded
in the result note**, never repaired into agreement by editing this file. Stage 5 is not entered
over a `CENSUS-UNEXPECTED`.

## Points at which this freeze chose a reading, recorded rather than resolved

1. **One round for shadow, census and gating; a second for retirement.** The owner's sequence.
   The alternative — three rounds on `SI-1`/`SI-2`/`SI-3`'s exact shape — was rejected because
   `V2` is a separate job and not a replacement call site, so "authority moves" has no cutover
   edit to make; what it has is a mode flag, gated on the census inside one round.
2. **Dual gating, not shadowing `V1`.** Turning `V1`'s fifty-one blocks into shadows would edit
   each of them; the retirement deletes them instead. The word "authority" is reserved for `CV-2`.
3. **Evidence pinned at `D`, not at each round's `E`.** Result notes have been corrected forward
   since landing, legitimately; certifying the present state is the honest translation, and the
   certificate records it.
4. **The seals manifest closed, `GR1.json`/`GR2.json` discharged by certificates.** A `V1` record
   for a round that has a `V2` certificate would be the double representation `SI-3` retired.
5. **`AGENTS.md` untouched.** The protocol text changes when the protocol changes, in `CV-2`.
6. **`PRA` outside `V2`.** A round in flight under `V1` is `V1`'s; act 29 lands between the two
   rounds and is translated by the second.
