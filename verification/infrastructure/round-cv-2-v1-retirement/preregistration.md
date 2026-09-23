# Certificate infrastructure round CV-2 — V1 retired: act 29 translated, standing invariants migrated, V2 the sole authority: PREREGISTRATION

**Control plane only.** This document fixes what `CV-2` will do, what would count as each
outcome, and what no outcome licenses, before any of it is implemented. One file, added. No guard
edit, no verifier edit, no certificate, no attestation record, no live-policy clause, no workflow
or release-gate edit, no `AGENTS.md` edit, no manuscript edit.

**The mandated execution base is the merge commit of this pull request**, once that merge and its
`main` push run are themselves certified. The execution branches from exactly that commit and from
nothing else, and its first act is to verify this preregistration's blob at that base.

***

## The commit vocabulary this freeze uses, fixed first

Per `§A.37`:

- **`D`** — the drafting snapshot, `b5cecce3168e84fce86eec54669141ae7c4791eb`: act 29's pin
  landing, certified by `main` push run 35758779718 (all five jobs success). Every measurement
  marked *at `D`* was taken against that commit.
- **`B`** — the mandated execution base: the certified merge commit on `main` of this control
  plane. Before that merge exists `B` has no SHA, and this freeze assigns none.
- **`M`** — a candidate merge continuous integration may construct before this control plane
  lands. Predictive test state only, never ancestry.
- **`E`** — the sealed execution head. **`L`** — the landing merge, first parent current green
  `main`, second parent exactly `E`. **`A`** — the attestation: one commit appended to `main`
  after `L`'s push run is certified, creating exactly `verification/certificates/attestations/CV2.json`.
  There is no `P`.

The rounds this freeze names, by their certified objects:

| round | `B` | `E` | `tree(E)` | `L` | after `L` |
|---|---|---|---|---|---|
| `CV-1` | `395d953faa5a2bd4d33c5b642e063f355453cba0` | `9332019aed34e33e83adc5e8740f1ef7c38742da` | `05b915584230d1dcbb5f272d7c3746db642fcaa6` | `5fe921ce10e68a2496b9797b0ab2b0b08ae02cdb` | `A_CV1` = `9bea7c91…`, the bootstrap row |
| act 29 (`PRA`) | `0bedff07fc1ad2675ecab205c8836e7a90a113d4` | `bf7e96fef8135525e752fb0daba0a082cf10ed44` | `4c088b603b2a06818d10bd65fea6bc50c9421040` | `c03939c2341c7085f0a55bddb61be2d175264dba` | the terminal chain `eb11dd18` → `37b0b959` → `P` = `D` |
| `GR-1` | `39090ca75860e7e6cbd99fa6f3ad859cee3efaf4` | `8d08f8c913f4bb9ef413114ecceb2f72d72d8213` | — | `13ffc7372d52c16bdb0e24935aa617deb67e7c51` | — |
| `GR-2` | `c9e6d56379923195382fa8c797c464397bcedaa5` | `0a61ea0ad6f6a28687203495ac9b29395f506178` | `794ffc3cd816e6ea4fc60c49999219f8e5e5d7b2` | `4caa5634363ac8746dff8cc4ce86f55f292e4b6f` | — |

***

## What `CV-2` is, and what it deliberately is not

`CV-1` installed `V2` in shadow, translated every landed round, ran both censuses, and wired the
verifier into the release gate in `--mode authoritative` beside the `V1` guard — **dual gating**.
Its freeze reserved three things for this round: translating act 29 and emptying the
legacy-owned set (`V7`), migrating the standing invariants `V1` carries as code into the live
policy (`V5`), and retiring the `V1` machinery so that `V2` is the **sole** authority. It also
reserved the `V2` protocol text: "`AGENTS.md` is not edited … the `V2` protocol text is `CV-2`'s to
write when `V1` is retired."

`CV-2` does those four things, in the order *translate while both gate → migrate while both gate →
census → delete → protocol text*, the `SI-1` → `SI-2` → `SI-3` order compressed into one round's
stages with a durable checkpoint between the last dual-gated head and the first deletion.

### What `CV-2` is not

1. **It is not a research round.** It decides no mathematics and reads no manuscript for content.
2. **It rewrites no history.** Every historical `B`, `E`, `L`, `P`, `A`, preregistration,
   amendment, result note, census, tag map, seal record, certificate and attestation record stays
   byte-identical, with exactly one exception named in terms: `legacy-v1-owned.json`, whose one
   entry `CV-1` froze as `CV-2`'s to consume.
3. **It does not convert content guards that were never rounds.** Forty-one tags of the guard file
   predate the round-certificate protocol and carry no certificate, no lifecycle and no seal state
   (class `P` below). They are not `V1` authority and are retained unchanged. Their conversion, if
   any, belongs to a later round.
4. **It manufactures no attestation.** `PRA` landed under `V1`; no `A_PRA` commit ever existed.
   `PRA` is translated with `origin: translated-v1`, in the `V2` representation, exactly as the
   other fifty-one were — never as `native-v2`, which would claim an attestation that did not
   happen.
5. **It edits no manuscript, no Lean file, no `ROADMAP.md`.**
6. **It does not relocate or delete the seal records.** Every record under `verification/seals/`
   is an evidence artifact of a translated certificate, pinned by blob. The directory becomes a
   closed evidence archive; no record is written, edited, moved or removed.

***

## The start state, FROZEN

Measured at `D` from the guard's own output, the verifier's own output and git. `CV2-0` requires
every row at `B`.

| object | at `D` |
|---|---|
| `V1` guard | `edge_rigidity_probe: ALL CHECKS PASS`, **105** tags, no failure |
| `R7-PRA` | `U3 keyed on PRA.json -> PASS (ARCHIVED; pinned == derived c03939c2341c; second parent is the sealed head; ancestry and reachability hold)`; 216 checks, 133 mutation controls, no failure |
| `R7-CV1` | chronology `ATTESTED`; **106** checks, **16** control groups; censuses `VERDICTS-AS-ADJUDICATED` / `REPRESENTATION-AS-FROZEN`; bridge `BRIDGE-SIMULATED`; no failure |
| `R7-GR1` | 86 checks, 24 control groups, `LANDED-UNRECORDED`, no failure |
| `R7-GR2` | 63 checks, 7 control groups, `LANDED-UNRECORDED`, no failure |
| `V2` verifier | `LEGACY-V1-OWNED  PRA`; `CERTIFICATES 52: 52 PASS, 0 UNATTESTED, 0 FAIL; records 36; legacy-owned 1`; 157 evidence ids resolved; 0 relocations; 0 policies; `VECTORS executed 89; corpus 89; mismatches 0; exact yes` |
| legacy-owned set | exactly `{PRA}`, `count: 1`, entry `{stem PRA, directory programmes/oi-qm/track-b/act-29-product-admission, preregistration_blob 5451a52d87d7d2ab2aac48802bb80898d81f6a16, base 0bedff07fc1ad2675ecab205c8836e7a90a113d4}` |
| declarations | `_MANIFEST_PROSPECTIVE = {}`; `_MANIFEST_BASELINE = {'base': '0bedff07fc1ad2675ecab205c8836e7a90a113d4', 'authorized': ('PRA',)}` |
| seal manifest | 34 records (28 `sealed`, 6 `base-only`), tree `ea7b7161fa84d96d8bc5ae03b0c8aa58e1879125` |

Pinned blobs and trees at `D`:

| path | blob or tree at `D` |
|---|---|
| `verification/lean/edge_rigidity_probe.py` | `2eab600fb8cd078b3dd0f3867a6e7420cfc2b79f` (35098 lines) |
| `tools/certificate_verifier.py` | `a475408874b850f34c31eca5e1cb4ab549601f38` |
| `tools/release_gate.py` | `ca851befa24028655ecbbee85e53482bc186eb82` |
| `.github/workflows/verify.yml` | `3ed93ea20bb42f986850d008d5a5edc93a4b7e34` |
| `AGENTS.md` | `a9687b39c69973d35a2ff81c257687071fd35eca` |
| `verification/README.md` | `4d5cbee82bfac6a1ea7963ec7b7b35780ddad151` |
| `verification/ROADMAP.md` | `f26f7c1c8d275539bccb21d6faa2e882abc6dcf8` |
| `verification/certificates/legacy-v1-owned.json` | `8d255edfd6c5fc352c398ef00f8848f91d324951` |
| `verification/certificates/live-policy.json` | `78a5c1457ca222c65cb146cdcc9b3081b6e6909b` |
| `verification/seals/PRA.json` | `6bfec3684724302a95d6fc05b1d481a4a3d552a8` |
| `verification/certificates` (tree) | `8aa1a8fac388b625653803f7dad7c2fdabb12cc4` |
| `verification/seals` (tree) | `ea7b7161fa84d96d8bc5ae03b0c8aa58e1879125` |
| `verification/infrastructure` (tree) | `f56a79935ca4d6fcc2fe2ad2a709263d6716781b` |

***

## Seven measurements at `D` that shape the round

Each was taken in a scratch worktree, a detached checkout of `D` with the named edits committed
locally, the guard and the verifier run with the git and pull-request environment scrubbed. None
of those edits is part of this control plane.

### `F1` — the migration trips exactly one `V1` block, through four live reads

On `D` plus exactly the `PRA` translation frozen below (certificate, translated record, legacy set
emptied): `V2` unchanged reports `CERT PRA PASS`, `ROW PRA landed PASS`, `CERTIFICATES 53: 53 PASS,
0 UNATTESTED, 0 FAIL; records 37; legacy-owned 0`, 161 evidence ids, `authoritative OK`. The guard
reports `FAILURE`, 104 tags passing and exactly one failing, `R7-CV1`, on six contracts:
`census-6b-as-frozen`, `census-equal-to-committed`, `legacy-owned-exactly-pra`,
`note:6b-sentence`, `provenance-fifty-one-translated`, `provenance-thirty-five-translated-rows`.
Adding one live-policy clause adds a seventh, `live-policy-zero-clauses`. Adding a native `CV2`
certificate adds nothing. `R7-PRA` stays `ARCHIVED` and `R7-GR1`, `R7-GR2` stay clean on every one
of those trees.

All seven failures descend from four reads of the **live** store: `_cv1_store()` (the certificates
and records), the legacy-owned file, the live-policy file, and the legacy list the `6b` row for
`PRA` takes from the live verifier report. Each is a statement about `CV-1`'s own state, which is
fixed at `E_CV1`, asked of whatever tree the guard runs on. It is the defect family `CV-1`'s
Amendment 2 froze — "after a round has landed, a historical control evaluates its round's certified
historical subject" — in four reads that amendment did not reach. **Measured at `D` with the
replacement `T1` below applied as well: `ALL CHECKS PASS`, 105 tags; `R7-CV1` 106 checks, no
failure, `REPRESENTATION-AS-FROZEN`; `R7-PRA` `ARCHIVED`.** On that tree `V1` certifies `PRA` as
`ARCHIVED` and `V2` certifies it as a translated round with its record, at one head.

### `F2` — `V2` has no execution-time chronology for a native round

On the same tree plus a stub native `CV2` certificate, a head was built carrying pre-base side
history: a merge of a commit whose parent predates `B_CV2`. `strong_ancestry(B_CV2, head)` is
`False`; the verifier in `--mode authoritative` reports `CERT CV2 UNATTESTED ok` and
`authoritative OK`. Today execution-time chronology is enforced only by each round's own `V1`
block. **Retiring `V1` without adding it to `V2` would leave the sole authority unable to reject a
native round's chronology violation.** Slot `W1` below exists because of this measurement.

### `F3` — `CV-1`'s inventory covers 51 of the guard's 105 tags

`CV-1`'s live-read census counts the fifty-one translated round blocks. The guard at `D` emits 105
tags, which partition exactly as follows:

| class | tags | count |
|---|---|---|
| `M` — mathematical probes and the kernel lint | `R1`–`R6`, `R7` (the lint of `OIBridge`), `R8`, `R9` | 9 |
| `P` — content guards that predate the round-certificate protocol | `R7-FWD`, `-OIN`, `-CAA`, `-INV`, `-MIN`, `-MSP`, `-CTN`, `-OINN`, `-PTR`, `-RB0`, `-RB1`, `-MAX`, `-LIFT`, `-SUB`, `-SCAL`, `-INST`, `-MIG`, `-FLOW`, `-PHASE`, `-PROP`, `-Q3`, `-Q3P`, `-EXEC`, `-LSRC`, `-SRCP`, `-C5D`, `-PCL`, `-CCS`, `-SMC`, `-RPF`, `-PFE`, `-DCA`, `-DIB`, `-FSS`, `-AUDB`, `-AUDA`, `-CT3D`, `-CT3C`, `-CT3B`, `-CT3`, `-CT2` | 41 |
| `C` — translated round blocks | `R7-SOI` … `R7-GR2`, exactly `CV-1`'s fifty-one | 51 |
| `PRA` — the legacy-owned round's block | `R7-PRA` | 1 |
| `BOOT` — the bootstrap block | `R7-CV1` | 1 |
| `X` — `V1` synthetic regressions | `R7-VIS`, `R7-ARCH` | 2 |

No `P` tag reads the seals directory, a manifest declaration or git chronology (measured: no such
read in lines 1–6426, which hold every `P` computation, the seven late-emitted tags' included).

### `F4` — the kernel lint is interleaved with the blocks it must outlive

`R7`'s verdict is the accumulator `ok6`, assigned **759** times from line 348 to line 30192; **208**
of those assignments, and the `R7`, `R8` and `R9` check calls themselves, lie at lines 29756–30369,
**inside `R7-SI1`'s line range** (28841–30379). The seven late `P` check calls (`R7-AUDB` …
`R7-CT2`) sit at lines 18640–18706 inside the `C` region, with their computations at 2122–2459.
Deleting any block by its line range would silently delete kernel-lint statements and orphan
retained tags. **Retirement is therefore defined by class of statement, never by line range**, and
the retained statements are counted.

### `F5` — `V1`'s blob pins, against `V2`'s evidence

219 hexadecimal literals of twelve or more digits in the guard; 86 resolve to a blob present at
`D`; **71** of those (path, blob) pairs are evidence entries of accepted `V2` certificates. The
fifteen that are not: `PRA`'s preregistration (evidence of the translation below); two `GR-1` pins
(`AGENTS.md`, `ProductLocusFreedom.lean`), history-scoped since `GR-2`'s `S2`; eleven Lean-module
blobs, each either compared as `blob(_<STEM>_B, module)` at a round's base — an immutable git
object — or quoted inside `R7-NLV`'s declaration-table text; and `arc-c`'s preregistration blob,
which `R7-QSTAR` requires as provenance text inside a Lean file. **Read at `D`: no live-tree blob
comparison of `V1` lies outside `V2`'s evidence.** `CV2-6` makes that reading mechanical.

### `F6` — two post-`E` amendments sit outside every certificate

`CV-1`'s `amendments/amendment-1.md` (blob `41f32c0ef25f8fc45218b7adae2339f93f23fd3a`, brought in
at `5a654304`) and `amendments/amendment-2.md` (`53ffdd8852863683fcebdff1d374be5161c638e0`, at
`eb11dd18`) postdate `E_CV1`, so `CV1.json` — written at `E` and pinned by its record — cannot carry
them; the guard pins neither. Act 29's `amendments/amendment-1.md`
(`3db13437baad75f4fe1a14390c146f875c592091`, at `eb11dd18`) is carried by the translation below.
Thirty-two further round artifacts at `D` belong to rounds with no guard block and no certificate;
neither `V1` nor `V2` pins them, `CV-2` changes nothing about them, and they are recorded, not
adopted.

### `F7` — the translation is accepted by the verifier as it stands

The `PRA` certificate and record frozen below, serialized as every existing store file is (one-space
indent, sorted keys, trailing newline), have blobs `af7844f223fe2cf1a5934ad92f1e2134cb6cbd5d` and
`46349c11118781f5cfa3993203fde136e7aee246`; the emptied legacy set has blob
`052ff9b0b8529fa57578339f5be01e03d3b921e6`. `B`, `E`, `tree(E)` and `L` derive exactly (`F1`). The
translation needs no verifier change.

***

## The round's shape, declared first, in `§A.37`'s terms

**`CV-2` is NON-SEALING**, `E` → `L`, no `P`, then `A`. It creates no seal record and alters none:
the thirty-four records stay byte-identical. It retires the *authority* that read them — the
validator, the accessor, the declarations and every lifecycle clause — which is the thing `CV-1`
froze as `CV-2`'s to do, and it writes no prospective declaration and changes no baseline while
that authority still stands.

**`CV-2` is the first `native-v2` round.** Its certificate carries `protocol: 2`,
`origin: native-v2`, `shape: non-sealing`, dependencies `["CV1", "PRA"]`, and is written during
its execution; its record is written at `A` with the three run identities. `CV-1` remains the
unique `bootstrap-v1` round.

**The bootstrap, and its bound.** `V1` has no block for `CV-2` and never certifies it. `CV-2` is
certified by `V6` extended by slot `W1` — the first round certified by a verifier it changed. The
self-certification is bounded four ways, each a frozen control: (i) `W1`'s derivation and its
vectors are frozen here, with expected verdicts, before the code exists; (ii) `W1`'s verdict on
`CV-2`'s own head is compared with `V1`'s strengthened-ancestry
predicate (`_rbr_strong_ancestry` / `_si1_quiet_ancestry`) on the same `(B, head)` and on the
negative vectors' repositories, and must agree — first at the stage-3 conformance gate and
again in the stage-4 census; (iii) the verifier at `B`, read from git, run against the store and
corpus at the stage-5 head and again at the candidate `E`, returns the same verdict on every
pre-existing certificate, record and vector, and differs only where this freeze names; (iv)
exact-head continuous integration on `E` and on `L`, and the `main` push run. `V1` never certifies
`CV-2` itself: (ii) is a comparison of `W1` with `V1`'s ancestry predicate, not a `V1` verdict on
this round.

**Nothing else lands on `main` between `B` and `L`.** `V1`-shaped rounds cannot land once `V1` is
retired, and a round landing mid-execution would have to be classified by an authority this round
is removing. The owner's sequencing is the control; `CV2-0` records that `_MANIFEST_PROSPECTIVE`
is `{}` at `B`, so no `V1` round is declared in flight.

***

## `T1` — `R7-CV1`'s four live store reads, superseded, stated as text

The rule is `CV-1` Amendment 2's, applied to the reads that amendment did not reach, and it names
no round: **once `CV-1` has left `EXECUTION`, its store contracts read the store at `CV-1`'s
certified subject `E_CV1`, from git; while `CV-1` executes, the live tree, unchanged.** An
unrecoverable `E_CV1` or an unreadable object fails closed.

**Superseded, `T1a`.** The seventeen lines from `def _cv1_store():` through the first following
`    return certs, rows`, each anchor occurring once at `D`: `sha256`
`ee4728a63f7ff81f50529cd0b87923914918060c71d0ba64a58300f1745ee015`.

**Superseded, `T1b`.** The eighteen lines from
`    with open(os.path.join(os.path.dirname(VERIFICATION), _CV1_CERTS, 'legacy-v1-owned.json'),`
through `    and _CV1_POLICY.get('policies') == [])`, each anchor occurring once at `D`, together
with the single line `try:` immediately above the first anchor: `sha256` of the eighteen lines
`1b5549514549d525d43102deae0c1525ce64ede70d09a5219efe0a5f66d72093`.

**Superseded, `T1c`.** The two lines from `    rep6b['PRA'] = {'class': 'LEGACY-V1-OWNED'`
through `'v7_entry': rep['legacy'] == ['PRA']}`, each anchor occurring once at `D`: `sha256`
`3bb55978fcdb41c7ddbcd349dd6d2b9dfffa574ac8b6ba69df45e4afe373e272`.

The execution extracts each segment from the **base's own guard text**, read from git, and requires
its hash before it changes anything.

**The replacements, the text measured at `D` under `F1`.** `T1a` becomes:

```python
def _cv1_subject_read(rel):
    """T1: one store file, read from CV-1's certified subject E_CV1 once CV-1 has left EXECUTION, and
    from the live tree while it executes. None when unreadable; the callers fail closed on None."""
    if _CV1_STATE == 'EXECUTION':
        try:
            with open(os.path.join(os.path.dirname(VERIFICATION), *rel.split('/')), 'rb') as fh:
                return fh.read()
        except OSError:
            return None
    if _CV1_E is None:
        return None
    return _cv1_git('show', '%s:%s' % (_CV1_E, rel))


def _cv1_subject_names(rel):
    if _CV1_STATE == 'EXECUTION':
        d = os.path.join(os.path.dirname(VERIFICATION), *rel.split('/'))
        return sorted(os.listdir(d)) if os.path.isdir(d) else []
    if _CV1_E is None:
        return None
    out = _cv1_git('ls-tree', '--name-only', '%s:%s' % (_CV1_E, rel))
    return None if out is None else sorted(out.decode('utf-8', 'replace').split())


def _cv1_store():
    """T1: the certificates and records of CV-1's lifecycle subject, parsed; unparsable as None."""
    certs, rows = {}, {}
    for sub, out in (('', certs), ('attestations', rows)):
        rel = _CV1_CERTS + ('/' + sub if sub else '')
        names = _cv1_subject_names(rel)
        if names is None:
            out['__unreadable__'] = None
            continue
        for name in names:
            if not name.endswith('.json') or name in ('live-policy.json', 'legacy-v1-owned.json'):
                continue
            raw = _cv1_subject_read(rel + '/' + name)
            try:
                out[name[:-5]] = json.loads(raw.decode('utf-8')) if raw is not None else None
            except ValueError:
                out[name[:-5]] = None
    return certs, rows
```

`T1b`, with the `try:` line above it, becomes:

```python
def _cv1_subject_json(rel):
    raw = _cv1_subject_read(rel)
    try:
        return json.loads(raw.decode('utf-8')) if raw is not None else None
    except ValueError:
        return None


_CV1_LEGACY = _cv1_subject_json(_CV1_CERTS + '/legacy-v1-owned.json')
_cv1_checks['legacy-owned-exactly-pra'] = bool(
    isinstance(_CV1_LEGACY, dict) and _CV1_LEGACY.get('count') == 1
    and [e.get('stem') for e in _CV1_LEGACY.get('rounds', [])] == ['PRA']
    and 'PRA' not in _CV1_CERT_OBJS and 'PRA' not in _CV1_ROW_OBJS)
_CV1_POLICY = _cv1_subject_json(_CV1_CERTS + '/live-policy.json')
_cv1_checks['live-policy-zero-clauses'] = bool(
    isinstance(_CV1_POLICY, dict) and _CV1_POLICY.get('count') == 0
    and _CV1_POLICY.get('policies') == [])
```

`T1c` becomes:

```python
    rep6b['PRA'] = {'class': 'LEGACY-V1-OWNED', 'no_certificate': 'PRA' not in _CV1_CERT_OBJS,
                    'no_row': 'PRA' not in _CV1_ROW_OBJS,
                    'v7_entry': isinstance(_CV1_LEGACY, dict) and [e.get('stem') for e in
                                _CV1_LEGACY.get('rounds', [])] == ['PRA']}
```

No contract name changes, no contract is removed, and nothing else in the region moves.

**The controls, mandatory**, executed by the round's harness and recorded in `census.json`, not
added to the guard — the guard gains no statement outside the replacement text, so `R7-CV1`'s own
counts are the measure of control 5:

1. **Pinned and unique.** Each superseded segment extracted from the base's text, hashed, equal to
   its frozen hash, its anchors occurring once; `T1b`'s preceding line exactly `try:`.
2. **The successor-guard demonstration.** On the stage-2 tree (the translation present): the
   superseded segments, compiled from the base's text, fail the seven contracts `F1` names; the
   replacements pass them.
3. **`EXECUTION` unchanged.** With `_CV1_STATE` forced to `EXECUTION`, old and new read the same
   bytes and return the same verdict on the same tree.
4. **Post-landing reads `E_CV1`, and fails closed.** With the state `ATTESTED`: the reads observed
   go to git at `E_CV1`; with `_CV1_E` forced to `None`, and separately with the store path absent at
   the subject, the seven contracts fail rather than skip.
5. **Every other row identical.** `R7-CV1` reports 106 checks and 16 control groups before and
   after, every row but the seven returns the same verdict on the base tree, and the guard's other
   104 tags return the base's verdicts.

***

## The `PRA` translation, FROZEN as data

Translated by the rule `CV-1` froze for the twenty-seven `sealed` rounds, at migration snapshot
`D`, from the seal record:

| certificate field | value |
|---|---|
| `schema`, `protocol`, `round`, `origin`, `shape` | `oi-round-certificate`, `1`, `PRA`, `translated-v1`, `sealing` |
| `directory` | `programmes/oi-qm/track-b/act-29-product-admission` |
| `base` | `0bedff07fc1ad2675ecab205c8836e7a90a113d4` |
| `control_plane` | `preregistration.md` blob `5451a52d87d7d2ab2aac48802bb80898d81f6a16`, merge `0bedff07…`, `execution_affecting: true`; then `amendments/amendment-1.md` blob `3db13437baad75f4fe1a14390c146f875c592091`, merge `eb11dd18d4abdc13a23b4034ae19cd3e35cf3b8c` (the first-parent commit that brought it in), `execution_affecting: false` — the amendment's own text: "post-`E` … not execution-affecting" |
| `dependencies` | `["PFR"]` — `R7-PRA` reads `PFR`'s module, the rule by which `CV-1` derived every other dependency |
| `evidence` | `PRA/amendments/amendment-1.md` `3db13437…`; `PRA/preregistration.md` `5451a52d…`; `PRA/result.md` `9d0c707981e3bd05d543ba146aaafc5d290acf2c`; `seals/PRA.json` `6bfec3684724302a95d6fc05b1d481a4a3d552a8` |
| `contributions` | `verification/ROADMAP.md`, `verification/lean-manuscript-census.json`, `verification/lean-mathlib/OIBridge.lean`, `verification/lean-mathlib/OIBridge/ProductAdmission.lean`, `verification/lean/edge_rigidity_probe.py` — the files `B_PRA`..`E_PRA` changed other than evidence |
| `translation` | `{from: seal-record, migration_snapshot: b5cecce3168e84fce86eec54669141ae7c4791eb}` |

| record field | value |
|---|---|
| `round`, `protocol`, `origin`, `kind` | `PRA`, `1`, `translated-v1`, `landed` |
| `certificate` | the certificate's blob, `af7844f2…` as serialized under `F7` |
| `base`, `sealed_head`, `tree`, `landing` | `0bedff07…`, `bf7e96fe…`, `4c088b60…`, `c03939c2…` — byte-equal to `PRA.json`'s `base`, `sealed_head`, `merge`, and `tree` derived from git |
| `migration_snapshot` | `b5cecce3168e84fce86eec54669141ae7c4791eb` |
| `ci` | **absent** — no attestation commit existed |

`legacy-v1-owned.json` becomes `{protocol: 2, count: 0, rounds: []}`. That is the terminal state
of `V7`; the file stays as the empty set, so the corpus's `legacy-owned` family keeps its subject.

***

## The `V6` changes, FROZEN — three definition slots

The verifier stays standard-library only, stem-free, and dispatches on `protocol` as before. Every
pre-existing vector keeps its id, recipe, verdict and reason byte-for-byte.

### `W1` — native lifecycle states

For every accepted certificate with `origin: native-v2` and a shape other than `content-only`:

- **with a record** — `ATTESTED`: the existing derivations, unchanged.
- **without a record** — the candidate landings are the merges, over the union of the visibility
  targets, having a non-first parent `p` with `strong_ancestry(base, p)`:
  - **none** — `EXECUTION`: the execution subject — the real `pull_request.head.sha` on a pull
    request, `HEAD` otherwise, never the synthetic merge — must satisfy
    `strong_ancestry(base, subject)`; failure is `native:execution-ancestry`;
  - **exactly one** — `LANDED-UNATTESTED`: `E` is that parent; the certificate's blob at `E` must
    equal the current certificate's blob, failure `native:certificate-changed-after-e`;
  - **more than one** — `native:landing-multiple-candidates`.
- The state is reported on the certificate's line. `EXECUTION` and `LANDED-UNATTESTED` with their
  conditions holding keep the verdict `UNATTESTED`, which does not fail a build; any failure code
  fails it.

### `W2` — the verifier's own text is stem-free, checked by the verifier

`R7-CV1`'s contract 8 migrated into the verifier as a generic self-check: the verifier reads
`tools/certificate_verifier.py` under the evaluated root and fails `verifier:stem-in-source:<STEM>`
when any stem of the store — certificates, records and legacy entries — occurs anywhere in that
text as a whole word, the test `R7-CV1` applies today. It runs in every mode.

### `W3` — two additions to the live-policy predicate schema

- **`normalize`**, an optional field of `file-contains` and `file-lacks`: `"whitespace"` compares
  after collapsing every run of whitespace to one space, in both file and text — the normalization
  the guard's content contracts already apply. Absent means raw, the present semantics. Any other
  value fails `live-policy:clause:<id>:normalize`.
- **`tree-pinned`** `{path, tree}`: holds when the git tree of `path` at the evaluated root's
  working tree equals `tree` — computed from the files on disk, so an untracked added file fails
  it.

### The vectors, FROZEN with their verdicts

| id | family | recipe | verdict, reason |
|---|---|---|---|
| `native-lifecycle-execution-positive` | native-lifecycle | native certificate, no record, head strongly descends from its base | `PASS`, `ok` |
| `native-lifecycle-execution-side-history` | native-lifecycle | the head merges a commit whose parent predates the base | `FAIL`, `native:execution-ancestry` |
| `native-lifecycle-execution-stale-base` | native-lifecycle | the head does not descend from the base | `FAIL`, `native:execution-ancestry` |
| `native-lifecycle-execution-synthetic-merge-refused` | native-lifecycle | pull-request event; the checked-out synthetic merge passes, the event's head fails | `FAIL`, `native:execution-ancestry` |
| `native-lifecycle-landed-unattested-positive` | native-lifecycle | one canonical landing, certificate unchanged since `E` | `PASS`, `ok` |
| `native-lifecycle-landed-two-candidates` | native-lifecycle | two merges each carrying a strongly-descending non-first parent | `FAIL`, `native:landing-multiple-candidates` |
| `native-lifecycle-certificate-changed-after-e` | native-lifecycle | one landing; the certificate edited after `E` | `FAIL`, `native:certificate-changed-after-e` |
| `native-lifecycle-attested-positive` | native-lifecycle | native certificate with a well-formed record and `ci` | `PASS`, `ok` |
| `self-check-positive` | self-check | a verifier text free of every store stem | `PASS`, `ok` |
| `self-check-stem-in-source` | self-check | a verifier text naming a store stem in its logic | `FAIL`, `verifier:stem-in-source:ZZ` |
| `live-policy-normalized-contains-across-lines` | live-policy | the text split across a line break, `normalize: whitespace` | `PASS`, `ok` |
| `live-policy-raw-contains-across-lines` | live-policy | the same without `normalize` | `FAIL`, `live-policy:violated:p1` |
| `live-policy-normalized-lacks-violated` | live-policy | forbidden text present across a line break | `FAIL`, `live-policy:violated:p1` |
| `live-policy-normalize-unknown` | live-policy | `normalize: "case"` | `FAIL`, `live-policy:clause:p1:normalize` |
| `live-policy-tree-pinned-positive` | live-policy | the directory's tree equals the pin | `PASS`, `ok` |
| `live-policy-tree-pinned-added-file` | live-policy | one untracked file added under the directory | `FAIL`, `live-policy:violated:p1` |
| `live-policy-tree-pinned-absent` | live-policy | the directory absent | `FAIL`, `live-policy:violated:p1` |

`self-check-stem-in-source` places a verifier copy in the synthetic repository and runs the check
against the synthetic root's copy. The corpus count is **measured, not predicted**: the families
rule governs, every family `CV-1` froze keeps its vectors, and the executed set equals the corpus
exactly.

***

## The inventory and the disposition table, FROZEN

The execution's harness walks the guard at the stage-4 head and assigns **every statement of the
guard file** to exactly one item, and every item to exactly one class below, writing
`v1-inventory.json`: `{items: [{id, tag, lines, class, read_class, disposition, discharged_by,
reason}], counts, uncovered}`. Unassigned statements and items with two dispositions fail
`CV2-5`. The classes and their dispositions:

| # | class | what it is | disposition | what discharges it, or why it is retained |
|---|---|---|---|---|
| 1 | `M` | `R1`–`R9`, including all 759 `ok6` statements wherever they lie | **RETAIN** | the probe's own subject. Byte-identical statements; relocation of contiguous segments only as needed to detach them from deleted regions |
| 2 | `P` | the forty-one pre-protocol content guards, their computations and their check calls | **RETAIN** | not `V1` authority: no certificate, no lifecycle, no seal state, no chronology read (`F3`). Byte-identical; the seven late check calls may be relocated to follow their computations |
| 3 | harness | `check`, `CHECKS`, `CHECK_TAGS`, `_artifact`, `_MIGRATED`, the imports and the closing summary | **RETAIN** | used by 1 and 2 |
| 4 | chronology | every lifecycle, strengthened-ancestry, archive-mode, `U3`-keyed, landing and pin statement of classes `C`, `PRA`, `BOOT` | **DISCHARGED — `V2` topology** | the round's record: `landed` rows by `E`/`tree(E)`/`L` derivation, `base-only` rows by base reachability, `CV1` by its bootstrap row, `PRA` by its translated row. Control: every such stem has an accepted record of the matching kind |
| 5 | own artifacts | freeze-pin blobs and sentence contracts on a round's own preregistration, amendments, result, census, tag map | **DISCHARGED — `V2` evidence** where the (path, blob) is an evidence entry of that stem's certificate; otherwise **MIGRATE** to a `blob-pinned` clause | the universal evidence rule. A sentence contract on a blob-pinned artifact is implied by the pin |
| 6 | other rounds' artifacts | the same, on another round's artifacts | as 5, against the other round's certificate; the dependency must be present | the evidence rule and the dependency fixpoint |
| 7 | base-scoped history | `blob(_<STEM>_B, path)`, `git show <B>:path` and every comparison against an immutable object named by SHA | **HISTORICAL** | an immutable git object cannot change; `V2` derives the base itself |
| 8 | manuscripts | reads of `papers/` and `book/` | **MIGRATE** where the contract is a conjunction of presence and absence tests over one file each, exactly expressible under `W3`, passing at the checkpoint and failing on the mutation the `V1` block used; otherwise **HISTORICAL** | the live policy, owned by the stem, with activation, expiry and evidence. **RETAIN is not a permitted disposition**: a historical round inspecting an ordinary file at today's head is the pattern `V2` exists to end |
| 9 | Lean sources | reads of `.lean` files | **COVERED** where the identifier is an anchor of `verification/lean-manuscript-census.json` or the property is enforced by the kernel build or the `lean-axioms` step; otherwise as 8 | the generic instruments `§A.35` names |
| 10 | queue, ledger and rules text | reads of `ROADMAP.md`, `README.md`, `AGENTS.md` | **HISTORICAL** | files later rounds change legitimately; the `GR-1` defect was one of these. `R7-MSP`'s `§A.35` read is class 2 and unaffected |
| 11 | guard self-reads | budgets, declaration contracts, block-text reads | **RETIRED-WITH-GUARD** | their subject is the text being retired |
| 12 | mutation controls | negative controls of classes 4–11 | follow their contract: retired with it, or, for a MIGRATE contract, executed once against the clause in the census | — |
| 13 | `X` | `R7-VIS`, `R7-ARCH` | **DISCHARGED — `V2` corpus** | each of their cases mapped to the corpus vector covering it (`visibility`, `topology`, `ambiguity`, `native-lifecycle`); an unmapped case becomes a vector, within the corpus rule |
| 14 | `BOOT` store and provenance contracts | `R7-CV1`'s provenance, legacy, policy, vacuity and exact-corpus contracts | **DISCHARGED — `V2` native** (the `provenance`, `legacy-owned`, `live-policy`, `vacuity` families); the stem-free contract by **`W2`**; the release-gate contract by clause `P2` | — |
| 15 | `BOOT` artifacts and bridge | `R7-CV1`'s census, tag map, result note, bridge simulation | **DISCHARGED — `V2` evidence** (`CV1`'s certificate) for the artifacts; the bridge **HISTORICAL** | the bridge simulated the transition this round performs; `CV2-3` is the real one |
| 16 | the seal validator | `SI-1`'s reader and validator as relocated, `SI-2`'s base region, `SI-3`'s baseline and prospective declaration, the manifest accessor | **DELETED** | `V2` records; `CV-1`'s `6a` census agreement over the fifty-one and `CV2-3`'s over `PRA` |
| 17 | the seal records | `verification/seals/*.json`, 34 files | **RETAINED AS EVIDENCE**, closed by clause `P1` | each is an evidence entry of a translated certificate |
| 18 | protocol text | `AGENTS.md` `§A.37` where it instructs a seal record, a pin, a declaration, a baseline or a guard clause | **REWRITTEN** per `CV2-10` | — |
| 19 | external references | `verification/coverage/LEDGER.json`, `lean-manuscript-census.json`, `repertoire_lie_probe.py`, `wave_period_probe.py` naming the guard or its tags | **UNCHANGED** where the named file or tag survives (all four name the file or a class-2 tag) | control: every reference names an object present at `E` |

**Predicted at `E`:** the guard emits **50** tags — the 9 of class `M` and the 41 of class `P` —
each with the verdict it had at `B`, and none of the 55 tags of `C`, `PRA`, `BOOT` and `X`. The
count is moderate-confidence; the rule governs.

***

## The standing invariants migrated into the live policy, FROZEN

Protocol-level clauses, each `{id, owner_round: CV2, protocol: 2, predicate, activation, expiry,
evidence}`:

| id | predicate | written at | expiry | evidence |
|---|---|---|---|---|
| `P1` `v1-seal-archive-closed` | `tree-pinned` `verification/seals` = `ea7b7161fa84d96d8bc5ae03b0c8aa58e1879125` | stage 4 | a later freeze that relocates the archive through the relocation ledger and replaces this clause | `CV2/preregistration.md` |
| `P2` `v2-release-gate-authoritative` | `file-contains` `tools/release_gate.py`: `"tools/certificate_verifier.py", "--mode", "authoritative"` | stage 4 | a later freeze that replaces the release gate's verifier step | `CV1/preregistration.md` |
| `P3a` `v2-standalone-authoritative` | `file-contains` `.github/workflows/verify.yml`: `python3 tools/certificate_verifier.py --mode authoritative` | stage 5 | as `P2` | `CV2/preregistration.md` |
| `P3b` `v2-no-shadow-job` | `file-lacks` `.github/workflows/verify.yml`: `certificate_verifier.py --mode shadow` | stage 5 | as `P2` | `CV2/preregistration.md` |
| `P4` `v1-declarations-absent` | `file-lacks` `verification/lean/edge_rigidity_probe.py`: `_MANIFEST_` | stage 5 | none while the guard file exists | `SI3/result.md`, `CV2/preregistration.md` — the migrated form of `SI-3`'s zero-legacy-statement contract, fixed-string rather than pattern, which is recorded as its limitation |
| `P5a` `cv1-amendment-1-pinned` | `blob-pinned` `verification/infrastructure/round-cv-1-certificate-protocol/amendments/amendment-1.md` = `41f32c0ef25f8fc45218b7adae2339f93f23fd3a` | stage 4 | none | `CV1/preregistration.md` (`F6`) |
| `P5b` `cv1-amendment-2-pinned` | `blob-pinned` `…/amendments/amendment-2.md` = `53ffdd8852863683fcebdff1d374be5161c638e0` | stage 4 | none | as `P5a` |

To these are added, at stage 4, the **content clauses** that class 5, 6, 8 and 9 items resolve to
under MIGRATE, each owned by the stem whose block carried the contract, each with the mutation the
block used. Their number is measured, not predicted. No clause may encode chronology, seal state or
a lifecycle notion; a clause that would need one is a failed MIGRATE and the item is recorded
HISTORICAL with its reason.

***

## The protocol text, FROZEN as propositions

At stage 6 `AGENTS.md` `§A.37` is revised so that, for rounds begun after `CV-2`'s landing, it
states and does not contradict:

1. a round is a control plane, then an execution pull request that carries its landing; the `D` /
   `B` / `M` vocabulary and the machine-checkable preconditions are unchanged;
2. the landing is `E` → `L` → `A`: no `P`, no seal record, no prospective declaration, no
   baseline; `A` is one commit creating exactly the round's attestation record, `native-v2`, with
   the run identities of exact `E`, exact `L` and `L`'s `main` push;
3. the round's certificate is written during its execution, `protocol: 2`, `origin: native-v2`, and
   carries neither `E`, `tree(E)`, `L` nor its own blob;
4. the verifier is the sole authority, certifying `EXECUTION`, `LANDED-UNATTESTED` and `ATTESTED`,
   through the release gate's authoritative step;
5. standing invariants live in `live-policy.json`, each clause with its owner, activation, expiry
   and evidence; **an ordinary round adds no executable live-tree assertion**;
6. `verification/seals/` is a closed evidence archive;
7. rounds landed under earlier text keep the chronology their frozen controls state.

It no longer instructs any round to write a seal record, a pin commit, a prospective declaration,
a manifest baseline or a guard clause. Everything in `AGENTS.md` outside `§A.37` is unchanged,
except at most one line in the lessons register.

***

## The order is part of the contract, and each checkpoint is committed

| stage | what it does | may not begin until |
|---|---|---|
| 1 | `T1`, and nothing else. Checkpoint: the guard `ALL CHECKS PASS` at the fixed head, 105 tags with the base's verdicts; the three superseded hashes verified | `CV2-0` `HOLD` |
| 2 | the `PRA` certificate, its record, the empty legacy set; `CV2.json` with the evidence written so far. Checkpoint: the guard `ALL CHECKS PASS`, 105 tags, `R7-PRA` `ARCHIVED`; `V6` authoritative OK: `PRA` `PASS`, its record `PASS`, `legacy-owned 0`, `CV2` `UNATTESTED` | stage 1, with `CV2-1` `SUPERSEDED-AS-FROZEN` |
| 3 | `W1`, `W2`, `W3` and their vectors. Checkpoint: the stage-3 conformance gate, `CV2-4`(a); the guard unchanged in verdict | stage 2, with `CV2-2` `TRANSLATED-AS-FROZEN` |
| 4 | `v1-inventory.json`; clauses `P1`, `P2`, `P5a`, `P5b` and the content clauses; `census.json`, committed. **The dual-gated checkpoint**: every object `V1` certifies is gated here by both authorities; `CV2` itself is certified by `V6` alone, its `W1` chronology compared with `V1`'s ancestry predicate | stage 3, with `CV2-4`(a) `CONFORMANCE-EXACT` |
| 5 | the deletions of the table above; `P3a`, `P3b`, `P4`; the standalone job to `--mode authoritative`; the release gate's comment naming `V1`. Checkpoint: the guard ends `ALL CHECKS PASS` with the retained tags only; `V6` authoritative OK; then the `B`-verifier cross-check, `CV2-4`(b), on this head | stage 4, with `CV2-3`, `CV2-5` and `CV2-6` at their frozen outcomes |
| 6 | `AGENTS.md`; the `README.md` ledger section; `result.md` and `cv2-tagmap.json`; the `V2` side of the census re-measured at this head | stage 5, with `CV2-4`(b) `CROSS-CHECK-AS-NAMED` |
| — | this commit is the candidate `E`. It is declared `E` only with `CV2-4`(b) `CROSS-CHECK-AS-NAMED` re-run on it, `CV2-7` `V1-RETIRED`, `CV2-8` `HISTORY-PRESERVED`, `CV2-9` `SOLE-AUTHORITY`, `CV2-10` `PROTOCOL-TEXT-AS-FROZEN` and `CV2-11` `SCOPED`, each decided at this commit; any other outcome of those six stops the round before `E` is declared | everything above |

**Durability.** The `V1` side of the census exists only while `V1` does. It is measured at the
stage-4 head, committed there, and that head is an ancestor of `E`; the stage-4 head, not a later
recomputation, is its certificate, and a local measurement taken before a later commit is not
evidence. The `V2` side is re-measured at `E` and required equal. Each checkpoint is run with
`HEAD` fixed for the run, the stage committed first, and `HEAD` and the dirty-file count logged at
start and end.

***

## The targets, FROZEN

Each target names the artifact that decides it, and is decided only by that artifact.

- **`CV2-0` — the start state holds at `B`**: every row of the start-state table; the three
  superseded segments present with their hashes and anchors; nothing between `D` and `B` but this
  file. Outcomes: `HOLD` / `DEVIATED`. `DEVIATED` stops the round.
- **`CV2-1` — `T1` as frozen**, with its five controls. Outcomes: `SUPERSEDED-AS-FROZEN` /
  `SUPERSEDED-DEVIATED`, the latter naming the segment or control and **stopping the round
  before stage 2**.
- **`CV2-2` — `PRA` translated.** The certificate and record byte-equal to the frozen data under
  the frozen serialization; `V6` `PASS` on both; `legacy-owned 0`; `LEGACY-V1-OWNED` reported for
  no stem. Outcomes: `TRANSLATED-AS-FROZEN` / `TRANSLATION-DEVIATED`, naming the field
  and **stopping the round before stage 3**.
- **`CV2-3` — the dual census, at the stage-4 head.** (a) `PRA`: `V1` `ARCHIVED` with pinned
  equal to derived, and `V2` certificate and record `PASS`, with `base`, `sealed_head` and
  `landing`/`merge` byte-equal between the two representations and `tree` equal to git. (b)
  `W1` against `V1`'s strengthened-ancestry predicate — a comparison, `V1` certifying nothing
  about `CV-2` — re-measured on `(B_CV2, stage-4 head)` and on the two negative repositories of
  `native-lifecycle-execution-side-history` and `…-stale-base`: the same verdict each time.
  (c) Every MIGRATE item: the `V1` contract and its clause both pass, and the mutation the block
  used fails the clause. (d) Every DISCHARGED item: the named `V2` object
  passes. (e) The guard's 105 tags all pass. The frozen profile: **every axis agrees, and there is
  no divergence to adjudicate.** Outcomes: `DUAL-AS-ADJUDICATED` / `DUAL-UNEXPECTED` (any
  disagreement, reported, not repaired; **stops the round before stage 5**) / `DUAL-BROKEN` (a
  disagreement on `PRA`'s facts).
- **`CV2-4` — the verifier and the corpus**, decided in two parts at two heads.
  - **(a) The stage-3 conformance gate, at the stage-3 head.** `W1`–`W3` as frozen; every frozen
    vector with its verdict and reason; the executed set equal to the corpus; every one of the
    eighty-nine pre-existing vectors with its id, recipe, verdict and reason unchanged; and `W1`
    against `V1`'s strengthened-ancestry predicate on `(B_CV2, stage-3 head)` and on the negative
    repositories of `native-lifecycle-execution-side-history` and `…-stale-base`, the same verdict
    each time. Outcomes: `CONFORMANCE-EXACT` / `CONFORMANCE-PARTIAL`, naming each vector, family
    or comparison; `CONFORMANCE-PARTIAL` **stops the round before stage 4**.
  - **(b) The `B`-verifier cross-check, at the stage-5 head and again at the candidate `E`.** The
    verifier at `B`, read from git, run on that tree, returns the same verdict as the head's
    verifier on every pre-existing certificate and record, and differs on exactly — `CV2`'s state
    label; each clause using `tree-pinned` (`live-policy:clause:<id>:predicate-type`); each clause
    using `normalize` whose raw reading differs; and, run over the head's corpus, the new vectors
    whose verdict depends on `W1`–`W3` — and on nothing else. Outcomes: `CROSS-CHECK-AS-NAMED` /
    `CROSS-CHECK-UNEXPECTED`, naming each divergence; `CROSS-CHECK-UNEXPECTED` at the stage-5 head
    **stops the round before stage 6**, and at the candidate `E` **stops it before `E` is
    declared**.
- **`CV2-5` — the inventory is complete.** Every statement of the guard at the stage-4 head in
  exactly one item, every item in exactly one class with one disposition; `ok6` counted at 759;
  `uncovered` empty. Outcomes: `INVENTORY-COMPLETE` / `INVENTORY-INCOMPLETE`, which **stops the
  round before stage 5**.
- **`CV2-6` — protection preserved.** Every (path, blob) pair a `V1` statement compares against
  the live tree at the stage-4 head is a `V2` evidence entry or a `blob-pinned` clause; every
  MIGRATE item has its clause; every DISCHARGED item names a passing `V2` object; every
  HISTORICAL item records the rule that makes it so. Outcomes: `PROTECTION-PRESERVED` /
  `PROTECTION-LOST`, naming each item, which **stops the round before stage 5**.
- **`CV2-7` — `V1` retired.** At `E` no statement of classes 4–16 remains in the guard; no seal
  validator, accessor, declaration, chronology, seal or pin code; no tag of `C`, `PRA`, `BOOT` or
  `X`; the retained statements of classes 1–3 byte-identical to the base's (after relocation),
  `ok6` at 759; the guard `ALL CHECKS PASS` with exactly the retained tags, each with the base's
  verdict. Outcomes: `V1-RETIRED` / `V1-RESIDUAL`, naming the residue, the latter
  **stopping the round before `E` is declared**.
- **`CV2-8` — historical meanings preserved.** Every certificate, record and vector present at `B`
  byte-identical at `E`; every one `PASS` at `E` as at `B`; the seals tree `ea7b7161…` at `E`;
  `CV1` `ATTESTED` on its unchanged bootstrap record; `GR1`, `GR2` and every translated round
  `PASS`; no file under `verification/programmes/`, `verification/audits/`, `verification/seals/`
  or another round's `verification/infrastructure/` directory changed; the evidence count at `E`
  = 157 + `PRA`'s 4 + `CV2`'s own. Outcomes: `HISTORY-PRESERVED` / `HISTORY-MOVED`,
  naming each object, the latter **stopping the round before `E` is declared**.
- **`CV2-9` — sole authority.** The release gate's `certificate-verifier` step in
  `--mode authoritative`, failing the gate when `V6` fails (one mutation control); the standalone
  job in `--mode authoritative`, exiting non-zero on the same mutation; `legacy-owned 0`; no `V1`
  tag in any job's output; clauses `P1`–`P5b` holding. Outcomes: `SOLE-AUTHORITY` / `NOT-SOLE`,
  naming the gap, the latter **stopping the round before `E` is declared**.
- **`CV2-10` — the protocol text.** `§A.37` states the seven propositions and none of the
  retired instructions; nothing else in `AGENTS.md` changes but one optional lessons line; `R7-MSP`
  returns its base verdict. Outcomes: `PROTOCOL-TEXT-AS-FROZEN` / `PROTOCOL-TEXT-DEVIATED`,
  naming the proposition or instruction, the latter **stopping the round before `E` is declared**.
- **`CV2-11` — scoped.** The diff against `B` touches exactly the files named under *Files this
  round reads AND writes*, deletes no file, and edits no manuscript, Lean file, `ROADMAP.md`,
  seal record, historical artifact, existing certificate, record or vector. Outcomes: `SCOPED` /
  `NOT-SCOPED`, the latter failing the round and **stopping the round before `E` is declared**.

***

## The preregistered predictions, with signs, strengths and recorded reasons

| target | prediction | strength | recorded reason |
|---|---|---|---|
| `CV2-0` | `HOLD` | HIGH | each row measured at `D`; nothing between `D` and `B` but this file |
| `CV2-1` | `SUPERSEDED-AS-FROZEN` | HIGH | the replacements are the text measured under `F1`: 105 tags, `ALL CHECKS PASS` |
| `CV2-2` | `TRANSLATED-AS-FROZEN` | HIGH | measured under `F1` and `F7` with the unchanged verifier |
| `CV2-3` | `DUAL-AS-ADJUDICATED` | MEDIUM | (a) and (e) measured at `D`; (b) and (c) run code that does not yet exist |
| `CV2-4`(a) | `CONFORMANCE-EXACT` | MEDIUM | `W1` must leave the eighty-nine vectors unchanged; the native schema-positive vectors are the ones it could reach |
| `CV2-4`(b) | `CROSS-CHECK-AS-NAMED` | MEDIUM | the divergences are named from the slots' definitions; a clause whose raw and normalized readings coincide is where the count could differ from a naive expectation |
| `CV2-5` | `INVENTORY-COMPLETE` | MEDIUM | `F4`'s interleaving is where a statement is missed |
| `CV2-6` | `PROTECTION-PRESERVED` | MEDIUM | `F5` is a reading at `D`; the manuscript contracts are where a MIGRATE fails |
| `CV2-7` | `V1-RETIRED`, **50** tags | HIGH; the count MODERATE | `F3`'s partition |
| `CV2-8` | `HISTORY-PRESERVED` | HIGH | the round writes no historical object |
| `CV2-9` | `SOLE-AUTHORITY` | HIGH | one wiring edit and one mutation control |
| `CV2-10` | `PROTOCOL-TEXT-AS-FROZEN` | MEDIUM | text; `R7-MSP` reads `§A.35` only, measured at `D` |
| `CV2-11` | `SCOPED` | HIGH | the budget below |

***

## The STATUS RULE, FROZEN

- A target is decided only by the artifact it names.
- Every negative outcome of a staged target stops the round at the next stage boundary, and
  continuation is never implied: `DEVIATED` on `CV2-0` stops it before stage 1;
  `SUPERSEDED-DEVIATED` before stage 2; `TRANSLATION-DEVIATED` before stage 3;
  `CONFORMANCE-PARTIAL` before stage 4; `DUAL-UNEXPECTED`, `DUAL-BROKEN`, `INVENTORY-INCOMPLETE`
  and `PROTECTION-LOST` **before stage 5** — nothing is deleted over a disagreement, a gap or a lost
  protection this freeze did not name, whatever the argument for it; `CROSS-CHECK-UNEXPECTED`
  before stage 6, or, at the candidate `E`, before `E` is declared.
- At the candidate `E`, `CROSS-CHECK-UNEXPECTED`, `V1-RESIDUAL`, `HISTORY-MOVED`, `NOT-SOLE`,
  `PROTOCOL-TEXT-DEVIATED` or `NOT-SCOPED` stops the round before `E` is declared. `E` is declared
  only with `CV2-4`(b) `CROSS-CHECK-AS-NAMED`, `CV2-7` `V1-RETIRED`, `CV2-8` `HISTORY-PRESERVED`,
  `CV2-9` `SOLE-AUTHORITY`, `CV2-10` `PROTOCOL-TEXT-AS-FROZEN` and `CV2-11` `SCOPED`, each decided
  at that commit. Every negative outcome of every target therefore blocks either the next stage or
  `E` itself.
- `NOT-SCOPED` fails the round.
- `DUAL-AS-ADJUDICATED` is an agreement claim on the objects compared, not a claim that `V2` is
  correct.
- No outcome licenses a sentence that `V1`'s verdicts were wrong, or that the retained class `P`
  is `V2` authority.

## The frozen post-round sentences

**`CV2-3`, `DUAL-AS-ADJUDICATED`:** "At the dual-gated checkpoint the `V1` guard and the `V2`
verifier certified act 29 at one head — `V1` as `ARCHIVED` from its seal record, `V2` as a
translated round from its certificate and record, with the same base, sealed head, landing and
tree — and agreed on every other object compared: each invariant migrated into the live policy
by that checkpoint (clauses `P1`, `P2`, `P5a`, `P5b` and the content clauses) together with the
mutation that exercises it, and every protection discharged to a named `V2` object; the new
verifier's execution chronology for this round's own head agreed with `V1`'s strengthened-ancestry
predicate on the same base and head, `V1` itself certifying nothing about this round. This is an
agreement census, not a proof of correctness."

**`CV2-7`, `V1-RETIRED`:** "From this head no seal validator, manifest declaration, lifecycle
clause or round block remains in the guard file; it carries the mathematical probes, the kernel
lint and the pre-protocol content guards, each with the verdict it had at the base. The seal
records remain as evidence, byte-identical and closed."

**`CV2-9`, `SOLE-AUTHORITY`:** "From this head the `V2` verifier is the sole authority over round
certificates: the release gate rejects any build it rejects, and no `V1` verdict gates anything.
Act 29 is an ordinary translated round and the legacy-owned set is empty."

***

## What no outcome of this round licenses

1. Any change to a historical `B`, `E`, `L`, `P`, `A`, preregistration, amendment, result note,
   census, tag map, seal record, certificate, record or vector.
2. Any `native-v2` claim, `ci` block or attestation identity for `PRA`.
3. Any claim that `V2` is correct, as distinct from in agreement where compared and authoritative.
4. Any conversion, deletion or weakening of the class-`P` guards.
5. Any manuscript, Lean or `ROADMAP.md` edit.
6. Any new `V1` object: no seal record, declaration, baseline, pin or `R7` block — `R7-CV2`
   included.
7. Any live-policy clause encoding chronology, seal state or lifecycle.
8. Any claim that a later round is safe because this one was green.

***

## Named hazards

**`H1` — self-certification.** Bounded by the four controls under *The bootstrap, and its bound*.

**`H2` — the lint dies with the block it sits in.** `F4`. Retirement is by class of statement;
`ok6` is counted at 759 at `B`, at stage 4 and at `E`.

**`H3` — the retirement commits the defect it retires.** `F1` is the seventh measured instance of
a historical control reading the live tree; `T1` repairs it before the store changes, and the
stage-2 checkpoint is where a miss would show.

**`H4` — protection loss dressed as retirement.** `CV2-6`, with MIGRATE failing closed to
HISTORICAL only by the recorded rule.

**`H5` — the live-policy file regrowing the guard.** Data-only, finite schema, owner and expiry
per clause, no lifecycle content, exact count. The metric `CV-1` froze is restated in `§A.37`.

**`H6` — manufactured history.** `PRA` translated, never native; its record structurally unable to
carry `ci`.

**`H7` — the archive.** The seal records are evidence; `P1` closes the directory.

**`H8` — a round in flight.** Nothing lands between `B` and `L`; `_MANIFEST_PROSPECTIVE = {}` at
`B`.

**`H9` — the protocol text tripping a retained guard.** `R7-MSP` reads `§A.35`'s heading and one
sentence; `CV2-10` requires its verdict unchanged.

**`H10` — the cross-check divergence discovered rather than named.** Named under `CV2-4`.

**`H11` — an untracked file under the archive.** `P1` evaluates the tree of the files on disk,
not the index.

**`H12` — the synthetic merge.** `W1` reads the event's head, never the checkout; one vector
exercises exactly that.

***

## Definition budget

**Three** slots — `W1`, `W2`, `W3` — and the execution may fire no more. The `PRA` translation,
the clauses, the inventory, the census, the harness, the vectors and the protocol text are data,
test code and text, not definition slots. No slot introduces a round-specific branch; `W2`
checks that on every run.

## The mutation budget

**What the execution may change.**

| change | where | limit |
|---|---|---|
| modify | `verification/lean/edge_rigidity_probe.py` | `T1` at stage 1; deletion of every statement of classes 4–16 at stage 5; relocation of retained segments. No statement added outside `T1`, no tag added |
| modify | `tools/certificate_verifier.py` | `W1`, `W2`, `W3` |
| modify | `tools/release_gate.py` | the comment naming `V1`; the step itself unchanged |
| modify | `.github/workflows/verify.yml` | the standalone job's `--mode shadow` to `--mode authoritative`, and its step name |
| modify | `verification/certificates/legacy-v1-owned.json` | to the empty set |
| modify | `verification/certificates/live-policy.json` | the clauses above |
| modify | `verification/certificates/conformance/v2/expected.json` | the new vectors' entries added; no existing entry changed |
| modify | `verification/README.md` | one ledger section appended |
| modify | `AGENTS.md` | `§A.37` per `CV2-10`; at most one lessons-register line |
| create | `verification/certificates/PRA.json`, `…/attestations/PRA.json`, `…/CV2.json` | as frozen |
| create | `verification/certificates/conformance/v2/<new vectors>.json` | the vectors frozen above, and any vector the `X` mapping adds under class 13 |
| create | `verification/infrastructure/round-cv-2-v1-retirement/{result.md, census.json, v1-inventory.json, cv2-tagmap.json, cv2_inventory.py}` | — |
| create at `A` | `verification/certificates/attestations/CV2.json` | alone in its commit |
| delete | — | no file is deleted |

**The controls every change carries**, at minimum: `T1`'s five; for the translation, a record with
`sealed_head` altered and a legacy set re-listing `PRA` beside its certificate, each failing `V6`;
the seventeen vectors; for every MIGRATE clause, its mutation failing it; for `P1`, an added
record failing it; for `P4`, a reintroduced declaration failing it; for the gate, one altered
evidence blob failing both the release gate and the standalone job; for retirement, removal of any
one retained statement changing the retained-statement count or its multiset hash.

## Evidence level

Level 2 — executed code with recorded output — for `CV2-1` through `CV2-9`. `CV2-0` and `CV2-11`
are bounded mechanical checks; `CV2-10` is a text check against the frozen propositions.

***

## Files

### Files this round reads AND writes

Exactly those in the mutation budget.

### Files this round reads and MUST NOT write

Every file under `verification/seals/`, `verification/programmes/`, `verification/audits/`, and
`verification/infrastructure/` outside this round's directory — `CV-1`'s directory included; every
existing certificate, attestation record and conformance vector; `verification/ROADMAP.md`;
`verification/lean-manuscript-census.json`; `verification/coverage/`; every `.lean` file; every
file under `papers/` and `book/`; `tools/control_plane_base_check.py`,
`tools/control_plane_lint.py`; every other probe.

### Name freedom, at `D`

`round-cv-2-v1-retirement`, `v1-retirement`, `v1-inventory`, `cv2_`, `native-lifecycle` and
`tree-pinned` each return nothing at `D`; `verification/certificates/CV2.json` and
`verification/certificates/attestations/CV2.json` do not exist. `R7-CV2`, `_CV2` and `round-cv-2`
occur at `D` only in `CV-1`'s preregistration and `R7-CV1`'s own contracts, which reserve them;
this round creates no `R7-CV2` tag and no `_CV2` name.

***

## Preconditions

```control-plane-preconditions
d: b5cecce3168e84fce86eec54669141ae7c4791eb
merged: false
frozen-blob: verification/lean/edge_rigidity_probe.py 2eab600fb8cd078b3dd0f3867a6e7420cfc2b79f
frozen-blob: tools/certificate_verifier.py a475408874b850f34c31eca5e1cb4ab549601f38
frozen-blob: tools/release_gate.py ca851befa24028655ecbbee85e53482bc186eb82
frozen-blob: .github/workflows/verify.yml 3ed93ea20bb42f986850d008d5a5edc93a4b7e34
frozen-blob: AGENTS.md a9687b39c69973d35a2ff81c257687071fd35eca
frozen-blob: verification/certificates/legacy-v1-owned.json 8d255edfd6c5fc352c398ef00f8848f91d324951
frozen-blob: verification/certificates/live-policy.json 78a5c1457ca222c65cb146cdcc9b3081b6e6909b
frozen-blob: verification/seals/PRA.json 6bfec3684724302a95d6fc05b1d481a4a3d552a8
frozen-blob: verification/programmes/oi-qm/track-b/act-29-product-admission/preregistration.md 5451a52d87d7d2ab2aac48802bb80898d81f6a16
# row 1: name freedom, drafting-time facts
{"id": "d1-dir-free", "scope": "D", "check": "git grep -l -- 'round-cv-2-v1-retirement' $D", "expect": "empty"}
{"id": "d1-inventory-free", "scope": "D", "check": "git grep -l -- 'v1-inventory' $D", "expect": "empty"}
{"id": "d1-prefix-free", "scope": "D", "check": "git grep -l -- 'cv2_' $D", "expect": "empty"}
{"id": "d1-family-free", "scope": "D", "check": "git grep -l -- 'native-lifecycle' $D", "expect": "empty"}
{"id": "d1-predicate-free", "scope": "D", "check": "git grep -l -- 'tree-pinned' $D", "expect": "empty"}
{"id": "d1-no-cv2-certificate", "scope": "D", "check": "git ls-tree -r --name-only $D verification/certificates/ | grep -e '/CV2\\.json$'", "expect": "empty"}
# row 2: the trees at D
{"id": "d2-seals-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/seals)\" = ea7b7161fa84d96d8bc5ae03b0c8aa58e1879125", "expect": "exit0"}
{"id": "d2-certificates-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/certificates)\" = 8aa1a8fac388b625653803f7dad7c2fdabb12cc4", "expect": "exit0"}
{"id": "d2-infra-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/infrastructure)\" = f56a79935ca4d6fcc2fe2ad2a709263d6716781b", "expect": "exit0"}
# row 3: provenance, D to B: D an ancestor, and nothing but this file between them
{"id": "db3-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
{"id": "db3-only-this-file", "scope": "D->B", "check": "git diff --name-only $D $REF | grep -v -x -e 'verification/infrastructure/round-cv-2-v1-retirement/preregistration.md'", "expect": "empty"}
{"id": "db3-seals-tree", "scope": "D->B", "check": "test \"$(git rev-parse $REF:verification/seals)\" = ea7b7161fa84d96d8bc5ae03b0c8aa58e1879125", "expect": "exit0"}
{"id": "db3-certificates-tree", "scope": "D->B", "check": "test \"$(git rev-parse $REF:verification/certificates)\" = 8aa1a8fac388b625653803f7dad7c2fdabb12cc4", "expect": "exit0"}
# row 4: no execution object at B
{"id": "b4-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-cv-2-v1-retirement/ | grep -v -e '/preregistration.md$'", "expect": "empty"}
{"id": "b4-no-cv2-certificate", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/certificates/ | grep -e '/CV2\\.json$'", "expect": "empty"}
{"id": "b4-no-pra-certificate", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/certificates/ | grep -e '/PRA\\.json$'", "expect": "empty"}
{"id": "b4-guard-no-cv2-tag", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"check('R7-CV2'\"", "expect": "empty"}
# row 5: the legacy-owned set is exactly act 29 at B
{"id": "b5-legacy-names-pra", "scope": "B", "check": "git show $REF:verification/certificates/legacy-v1-owned.json | grep -e '\"stem\": \"PRA\"'", "expect": "nonempty"}
{"id": "b5-legacy-count-one", "scope": "B", "check": "git show $REF:verification/certificates/legacy-v1-owned.json | grep -e '\"count\": 1,'", "expect": "nonempty"}
# row 6: act 29 is pinned under V1 at B, and no V1 round is declared in flight
{"id": "b6-pra-clause-present", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"check('R7-PRA'\"", "expect": "nonempty"}
{"id": "b6-prospective-empty", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -x \"_MANIFEST_PROSPECTIVE = {}\"", "expect": "nonempty"}
{"id": "b6-baseline-act29", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -x \"_MANIFEST_BASELINE = {'base': '0bedff07fc1ad2675ecab205c8836e7a90a113d4', 'authorized': ('PRA',)}\"", "expect": "nonempty"}
{"id": "b6-manifest-count", "scope": "B", "check": "test \"$(git ls-tree --name-only $REF verification/seals/ | grep -c '\\.json$')\" = 34", "expect": "exit0"}
{"id": "b6-pra-landing-second-parent", "scope": "B", "check": "test \"$(git rev-parse c03939c2341c7085f0a55bddb61be2d175264dba^2)\" = bf7e96fef8135525e752fb0daba0a082cf10ed44", "expect": "exit0"}
{"id": "b6-pra-tree", "scope": "B", "check": "test \"$(git rev-parse bf7e96fef8135525e752fb0daba0a082cf10ed44^{tree})\" = 4c088b603b2a06818d10bd65fea6bc50c9421040", "expect": "exit0"}
{"id": "b6-pra-landing-reachable", "scope": "B", "check": "git merge-base --is-ancestor c03939c2341c7085f0a55bddb61be2d175264dba $REF", "expect": "exit0"}
# row 7: T1's superseded segments at B, with their frozen hashes and unique anchors
{"id": "b7-t1a-hash", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | sed -n '/^def _cv1_store():$/,/^    return certs, rows$/p' | sha256sum | cut -d' ' -f1 | grep -x 'ee4728a63f7ff81f50529cd0b87923914918060c71d0ba64a58300f1745ee015'", "expect": "nonempty"}
{"id": "b7-t1a-close-once", "scope": "B", "check": "test \"$(git show $REF:verification/lean/edge_rigidity_probe.py | grep -c '^    return certs, rows$')\" = 1", "expect": "exit0"}
{"id": "b7-t1b-hash", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | sed -n \"/^    with open(os.path.join(os.path.dirname(VERIFICATION), _CV1_CERTS, 'legacy-v1-owned.json'),\\$/,/^    and _CV1_POLICY.get('policies') == \\[\\])\\$/p\" | sha256sum | cut -d' ' -f1 | grep -x '1b5549514549d525d43102deae0c1525ce64ede70d09a5219efe0a5f66d72093'", "expect": "nonempty"}
{"id": "b7-t1b-close-once", "scope": "B", "check": "test \"$(git show $REF:verification/lean/edge_rigidity_probe.py | grep -c \"^    and _CV1_POLICY.get('policies') == \\[\\])$\")\" = 1", "expect": "exit0"}
{"id": "b7-t1c-hash", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | sed -n \"/^    rep6b\\['PRA'\\] = {'class': 'LEGACY-V1-OWNED'/,/'v7_entry': rep\\['legacy'\\] == \\['PRA'\\]}\\$/p\" | sha256sum | cut -d' ' -f1 | grep -x '3bb55978fcdb41c7ddbcd349dd6d2b9dfffa574ac8b6ba69df45e4afe373e272'", "expect": "nonempty"}
# row 8: this control plane at its path
{"id": "b8-self-present", "scope": "B", "check": "git ls-tree --name-only $REF verification/infrastructure/round-cv-2-v1-retirement/preregistration.md", "expect": "nonempty"}
```

***

## The landing shape

`E` → `L` → `A`, no `P`:

- **`E`** is the stage-6 commit, certified by exact-head continuous integration on all five jobs,
  the verifier reporting `CV2` in `EXECUTION`.
- **`L`** has current green `main` as first parent and exactly `E` as second, and writes nothing.
  Full continuous integration passes on exact `L`, the verifier reporting `CV2`
  `LANDED-UNATTESTED`, and the resulting `main` push run is green before anything else lands.
- **`A`** is one commit on certified `main` creating exactly
  `verification/certificates/attestations/CV2.json`: `protocol: 2`, `origin: native-v2`,
  `kind: landed`, the certificate blob at `E`, `base`, `sealed_head`, `tree`, `landing`, and the
  three run identities with their conclusions. The verifier moves `CV2` to `ATTESTED` on `A`'s own
  build; `A` lands only after that build is green, and nothing else lands between `L` and `A`.

***

## Execution discipline

The execution begins only from the certified merge of this control plane, and its first act is to
verify this file's blob at that base. It absorbs no later `main` before `E` is certified. A
divergence between this freeze and what the execution measures is recorded in the result note,
never repaired into agreement by editing this file. No stage is entered over a negative outcome
of the target that gates it, as the status rule lists; in particular stage 5 is not entered over a
`DUAL-UNEXPECTED`, `DUAL-BROKEN`, `INVENTORY-INCOMPLETE` or `PROTECTION-LOST`, and no commit is
declared `E` over a negative outcome of `CV2-4`(b) or `CV2-7` through `CV2-11`.

## Points at which this freeze chose a reading, recorded rather than resolved

1. **One round, with a committed dual-gated checkpoint, rather than two.** `CV-1`'s freeze named
   one retirement round. The checkpoint at stage 4 is where both authorities gate every object
   `V1` certifies; the stop rules make it a gate rather than a milestone.
2. **`T1` before the translation, rather than deleting `R7-CV1` first.** Deleting it first would
   leave `PRA` certified by neither side for a stage and remove `CV-1`'s controls while `V1` still
   stands. Superseding four reads keeps the checkpoint dual.
3. **`PRA` as `translated-v1`.** The owner's instruction says "native `V2` certificate/attestation
   representation"; this freeze reads that as the `V2` representation — certificate and record —
   with the origin discriminant `translated-v1`, because `native-v2` would assert an `A_PRA` that
   never happened.
4. **Class `P` retained.** The forty-one pre-protocol guards are content contracts that were never
   rounds. Retiring `V1` authority does not require touching them; converting them is its own round.
5. **Manuscript contracts: MIGRATE or HISTORICAL, never RETAIN.** Keeping them as code would keep
   historical rounds inspecting today's files, the pattern `V2` ends. The cost is that a contract
   not exactly expressible under `W3` loses live enforcement; `CV2-6` names every such item.
6. **`W3`'s two additions, rather than none.** Without `normalize`, most manuscript contracts
   (written against whitespace-normalized text) would fail MIGRATE on line wrapping alone; without
   `tree-pinned`, the closed archive could not be stated. Both were weighed against a fourth slot
   — bounded-lifetime executable round checks in native certificates — which was rejected: a
   native round's contracts are data, and `CV-2`'s own are decided by committed artifacts, the
   verifier and exact-head runs.
7. **The standalone job made authoritative.** With `V1` gone a report-only job printing green over a
   failure would be the only visible `V2` job; the release gate remains the gate.
8. **`CV-1`'s post-`E` amendments pinned by policy (`P5a`, `P5b`)**, since no certificate can carry
   them and neither authority pins them today.
