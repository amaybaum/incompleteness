# Verifier round V3-4 — V3 implementation conformance: PREREGISTRATION

**Status: control plane.** This file is the round's preregistration and nothing else. The changed
shadow verifier, the moved and added vectors, the README paragraph and the result note are
execution objects, created only after the certified merge of this file.

> **The shadow is brought to the specification, and the vectors decide whether it arrived.** Each
> change to the tool lands in the same commit as the vectors that justify it, each of which fails
> on the tool before the change and passes after it.

## The commit vocabulary this freeze uses, fixed first

`V3-4` is run under `AGENTS.md` §A.37 as it stands at `D`: this control plane, then one execution
pull request that carries its landing.

- `D` = `c021f12b2564a07adf9142032a0fc371d5b9c6e3`, the drafting snapshot: the certified head of
  `main` after `V3-3`'s landing (push run 35981053491, all six jobs green). Every measurement in
  this file was taken at `D` unless it says otherwise.
- `B` — the mandated execution base: the certified merge commit on `main` of this file. It has no
  object id until that merge exists and its push run is green.
- `M` — a candidate merge of this file into `main`, used only to evaluate `B`-scoped rows before the
  merge.
- `E` — the sealed execution commit, the last commit of the execution branch that branches from
  `B`.
- `L` — the landing merge: first parent current green `main`, second parent exactly `E`.

The letters `F`, `W`, `Rᵢ`, `Λ`, `LB` and `Q` keep the meanings
`verification/infrastructure/v3/architecture.md` gives them; they name objects of the synthetic
rounds the vectors build, never an object of this round.

## What `V3-4` is, and what it is not

`V3-4` is an **implementation round**. It changes `tools/v3_verifier.py` so that the shadow
implements the settlements `V3-3` fixed in `architecture.md` where the shadow departed from them —
`K2`, `K4` and `G6` — and repairs one defect in its reading of `K1` found while drafting `V3-3`. It
moves the eleven vectors of `verification/infrastructure/v3/conformance-pending/` into the corpus,
adds one vector for the `K1` defect, and brings the tool's printed rules and the README paragraph on
the shadow into line with what the tool then does.

It is not:

1. **A specification round.** `architecture.md` is not written. Where the tool and the settled text
   disagree, the text decides.
2. **A promotion.** No act of `V3-2`'s promotion boundary is performed: no release-gate wiring, no
   change to the workflow or to any required check, no receipt, no operative language in
   `AGENTS.md`. The shadow gates nothing, and `V1` and `V2` stay authoritative and unchanged.
3. **A settlement of `G8` to `G12`.** The gaps `V3-3` recorded stay open, and the tool's behaviour
   where they bear is not changed.
4. **A migration or bootstrap round.** No historical round is translated or classified, and nothing
   about the certification or publication of the first V3-governed round is addressed.

## Measurements at `D` that shape the round

### `F1` — name freedom

`V3-4`, `v3-4`, `round-v3-4`, `V34-` and `implementation-conformance` occur nowhere in the tree at
`D`. `verification/receipts/` does not exist at `D`.

### `F2` — the objects the round reads or writes, at `D`

| path | blob at `D` |
|---|---|
| `tools/v3_verifier.py` | `2c34d4d7f1adadc4bdecbad94ff8eadb7b30f974` |
| `verification/README.md` | `052dfa270479c12470173ee90f340c4f805dac37` |
| `verification/infrastructure/v3/architecture.md` | `3326bf309d6392e4e5d69a9e7ab6d812dba035af` |
| `.github/workflows/verify.yml` | `d14d19389f452b39820206d449146ac424b7706c` |

`verification/infrastructure/v3/conformance/` holds 93 vectors at `D`, and
`verification/infrastructure/v3/conformance-pending/` holds eleven, whose digest (SHA-256 of the
files concatenated in path order) is
`605f9328fa4751fb766362a743e043883249784c4899fe088038f01baa5d96bc`. Outside the `V3` round
directories, only the workflow, the tool and `verification/README.md` refer to the tool or to either
directory. The workflow runs `--self-test`, `--corpus` with the default directory, and
`--mode shadow`; it names neither vector directory.

### `F3` — the verdict table, measured at `D` in scratch

A scratch copy of the tool was edited cumulatively, stage by stage, at the sites frozen below, and
every vector was run under the tool at `D` and under each stage (`ok` = as expected):

| vectors | tool at `D` | stage 1 | stage 2 | stage 3 | stage 4 |
|---|---|---|---|---|---|
| the 93 of `conformance/` | ok | ok | ok | ok | ok |
| the two `K2` pending vectors | not | ok | ok | ok | ok |
| the two `K4` pending vectors and the `G7` one | not | not | ok | ok | ok |
| the six `G6` pending vectors | not | not | not | ok | ok |
| the `K1` regression vector | not | not | not | not | ok |

Each stage turns exactly its own vectors as expected and turns no vector not as expected. The
cumulative tool after stage 3 is byte-identical to `V3-3`'s settlement patch (SHA-256 `481cf746`),
the object `V3-3`'s controls `C3` and `C4` exercised. With any one stage's edits left out of the
stage-4 tool, exactly that stage's vectors run not as expected and every other vector as expected.

### `F4` — the `K1` defect

`control_plane` derives the record directory from each path of `delta(D, F)` with the pattern
`(.+/)(preregistration\.md|amendments/.+)`. For an amendment named
`<R>amendments/preregistration.md` the pattern's greedy first group is `<R>amendments/`, so the
shadow finds two record directories, `<R>` and `<R>amendments/`, and fails a valid round with
`t1:record-directory`. `architecture.md`'s record directory holds `preregistration.md` and the
files under `amendments/`, and those are the only paths `delta(D, F)` may touch; the directory is
therefore the one `R` for which every control-plane path of `delta(D, F)` is `R`'s
`preregistration.md` or lies under `R`'s `amendments/`.

### `F5` — what the edits leave unchanged

The stage-4 and stage-5 tools give output identical to the tool at `D` for `--project` over the
subject `D` (126 cells), so `V3-2`'s `census.json` still describes the shadow's comparison with
`V2`. The self-test passes at every stage.

### `F6` — tooling at `D`

Python 3.11 and git 2.43 in the drafting environment; the workflow pins Python 3.11. The object
format is `sha1`.

## The implementation, FROZEN by site and semantics

The execution changes `tools/v3_verifier.py` at the sites below and nowhere else. Each **site** is
a block of the tool at the stage it is changed in, which must occur there exactly once; each
**semantics** is the rule the changed code must implement, stated in the words of `architecture.md`.
The replacement text shown for each site is the drafting-time implementation: it is a prediction,
as are the blobs it yields (below). The execution derives its edit against the tool at `B`, and the
frozen vectors decide whether an edit behaves as its semantics require on the cases they encode.
Because a finite set of vectors does not exhaust the semantics, an edit whose text differs from the
prediction is also recorded as a divergence, with its diff against the prediction, and before `E` is
designated the owner reviews every divergence for consistency with the frozen semantics. Textual
divergence alone is not a stop; a divergence the owner finds inconsistent with its semantics is a
stop outcome for that stage's target even when every frozen vector runs as its row says.

### Stage 1 — `K2`: the declarations lie in the preregistration at `F`

**Semantics.** At `F`, the `v3-governed-paths` and `v3-round` blocks counted are those of the
preregistration; an amendment carrying a fenced block with either info string makes the control
plane invalid (`t1:`); an unclosed block with either info string in any control-plane file at `F`
makes it invalid.

#### Site `s1.1`

The site:

```text
    texts = [repo.blob(files[p]).decode('utf-8', 'replace') for p in sorted(files)]
    gov_blocks, round_blocks = [], []
    for t in texts:
        g = fenced_blocks(t, 'v3-governed-paths')
        rb = fenced_blocks(t, 'v3-round')
        if g is None or rb is None:
            return None, None, None, None, files, codes + ['t1:unclosed-block']
        gov_blocks += g
        round_blocks += rb
```

The drafting-time replacement (a prediction):

```text
    gov_blocks, round_blocks = [], []
    for p in sorted(files):
        t = repo.blob(files[p]).decode('utf-8', 'replace')
        g = fenced_blocks(t, 'v3-governed-paths')
        rb = fenced_blocks(t, 'v3-round')
        if g is None or rb is None:
            return None, None, None, None, files, codes + ['t1:unclosed-block']
        if p == rdir + b'preregistration.md':
            gov_blocks += g
            round_blocks += rb
        elif g or rb:
            codes.append('t1:block-in-amendment')
```

### Stage 2 — `K4`: every receipt commit, with the final receipt's seal records

**Semantics.** A superseded receipt commit is a single-parent child of its reconciliation whose
delta is exactly the receipt path plus the seal records the round's **final** receipt names; the
content of a superseded receipt is not read, so an unreadable superseded receipt neither fails the
round nor stops the verifier.

#### Site `s2.1`

The site:

```text
            prev_r = read_receipt_at(repo, prev_q, receipt_path)
            prev_seal = [x['path'].encode() for x in (prev_r or {}).get('seal', {}).get(
                'records', [])] if isinstance(prev_r, dict) else []
            if prev_r is None or not receipt_delta_ok(repo, rc, prev_q, receipt_path, prev_seal):
                codes.append('s10:superseded-receipt-commit')
```

The drafting-time replacement (a prediction):

```text
            if not receipt_delta_ok(repo, rc, prev_q, receipt_path, seal_paths):
                codes.append('s10:superseded-receipt-commit')
```

### Stage 3 — `G6`: the record class is the round's own record

**Semantics.** At `F` (and for the `s7` vector runner): literal `record` entries for the record
directory `R` and the receipt path `P`; no `execution` entry within `R`; no other `record` entry
outside `R` except, in a sealing round, a single file. A record path is a path within `R`, `P`, or a
seal record the final receipt names; the halted landing and the record commit of a halted round
without execution commits admit record paths in that sense only, whatever class a `record` entry
gives other paths.

#### Site `s3.1`

The site:

```text
def check_t1(repo, d, f, cp_files):
```

The drafting-time replacement (a prediction):

```text
def record_class_codes(entries, rd, rp, kind, fam):
    """G6: the record class is exactly the round's own record."""
    codes = []
    literal = {e[2] for e in entries if e[0] == 'record'}
    for p in (rd, rp):
        if p not in literal:
            codes.append(fam + ':record-class-omits:' + p)
    for cls, ops, p in entries:
        if cls == 'execution' and p.startswith(rd):
            codes.append(fam + ':execution-entry-within-record-directory')
        if cls == 'record' and p not in (rd, rp) and not p.startswith(rd):
            if p.endswith('/') or kind == 'non-sealing':
                codes.append(fam + ':record-entry-outside-own-record')
    return codes


def check_t1(repo, d, f, cp_files):
```

#### Site `s3.2`

The site:

```text
    for p in (decl['record-directory'], receipt_path):
        e = governing(entries, p)
        if e is None or e[0] != 'record':
            codes.append('t1:record-class-omits:' + p)
    return rdir, decl['round'], decl['kind'], entries, files, codes
```

The drafting-time replacement (a prediction):

```text
    codes += record_class_codes(entries, decl['record-directory'], receipt_path, decl['kind'], 't1')
    return rdir, decl['round'], decl['kind'], entries, files, codes
```

#### Site `s3.3`

The site:

```text
            if rnd:
                for p in (rnd['record_directory'], rnd['receipt_path']):
                    e = governing(res, p)
                    if e is None or e[0] != 'record':
                        codes.append('s7:record-class-omits')
```

The drafting-time replacement (a prediction):

```text
            if rnd:
                codes += record_class_codes(res, rnd['record_directory'], rnd['receipt_path'],
                                            None, 's7')
```

#### Site `s3.4`

The site:

```text
def check_landing_halted(repo, lb, lam, entries, rdir):
    codes = []
    delta = repo.delta(lb, lam)
    for st, path, *_ in delta:
        g = governing(entries, path)
        if g is None or g[0] != 'record':
            codes.append('s12:landing-publishes-execution-path')
            break
```

The drafting-time replacement (a prediction):

```text
def check_landing_halted(repo, lb, lam, entries, rdir, receipt_path):
    codes = []
    delta = repo.delta(lb, lam)
    for st, path, *_ in delta:
        if not (path.startswith(rdir) or path == receipt_path):
            codes.append('s12:landing-publishes-non-record-path')
            break
```

#### Site `s3.5`

The site:

```text
        lcodes, ldelta = check_landing_halted(repo, lb, lam, entries, rdir)
```

The drafting-time replacement (a prediction):

```text
        lcodes, ldelta = check_landing_halted(repo, lb, lam, entries, rdir, receipt_path)
```

#### Site `s3.6`

The site:

```text
            for st_, path, *_ in repo.delta(f, c):
                g = governing(entries, path)
                if g is None or g[0] != 'record':
                    codes.append('s12:record-commit-changes-execution-path')
                    break
```

The drafting-time replacement (a prediction):

```text
            for st_, path, *_ in repo.delta(f, c):
                if not (path.startswith(rdir) or path == receipt_path):
                    codes.append('s12:record-commit-changes-non-record-path')
                    break
```

### Stage 4 — `K1`: the record directory

**Semantics.** `F4`: the record directory is the one directory `R` such that every control-plane
path of `delta(D, F)` is `R`'s `preregistration.md` or lies under `R`'s `amendments/`; none or more
than one such directory fails the round with `t1:record-directory`.

#### Site `s4.1`

The site:

```text
    delta = repo.delta(d, f)
    dirs = set()
    for st, path, *_ in delta:
        m = re.fullmatch(rb'(.+/)(preregistration\.md|amendments/.+)', path)
        if not m:
            codes.append('t1:non-control-plane-change')
        else:
            dirs.add(m.group(1))
    if len(dirs) != 1:
        return None, None, None, None, {}, codes + ['t1:record-directory']
    (rdir,) = dirs
```

The drafting-time replacement (a prediction):

```text
    cp_paths = []
    for st, path, *_ in repo.delta(d, f):
        if re.fullmatch(rb'.+/(preregistration\.md|amendments/.+)', path):
            cp_paths.append(path)
        else:
            codes.append('t1:non-control-plane-change')
    # K1: the record directory is the one directory R such that every control-plane path of
    # delta(D, F) is R's preregistration.md or lies under R's amendments/.
    fits = sorted(r for r in {p[:-len(b'preregistration.md')] for p in cp_paths
                              if p.endswith(b'/preregistration.md')}
                  if all(p == r + b'preregistration.md' or p.startswith(r + b'amendments/')
                         for p in cp_paths))
    if len(fits) != 1:
        return None, None, None, None, {}, codes + ['t1:record-directory']
    (rdir,) = fits
```

### Stage 5 — the tool's description of itself

**Semantics.** The tool no longer describes `K1`–`K4` as provisional readings: its docstring, its
printed rules and its comments state the settled rules and name `architecture.md` as their source.
The printed rules are stated in terms of what the tool now checks.

#### Site `s5.1`

The site:

```text
The provisional readings K1-K4 of the V3-2 preregistration bind this tool and nothing else; they are
printed at every shadow run.
```

The drafting-time replacement (a prediction):

```text
It implements the settlements of K1-K4 and G5-G7 that round V3-3 fixed in the specification; the
rules K1-K4 are printed at every shadow run.
```

#### Site `s5.2`

The site:

```text
READINGS = (
    'K1  the preregistration at F carries one `v3-round` block: round <id>, kind '
    '<sealing|non-sealing>, record-directory <path>/; the receipt must agree with it',
    'K2  over all control-plane files at F together: exactly one `v3-governed-paths` block and '
    'exactly one `v3-round` block',
    'K3  for every reconciliation, D lies on the first-parent chain of its first parent; for i>1, '
    'the previous first parent lies on the first-parent chain of this one',
    'K4  every receipt commit, superseded or final, is a single-parent child of the reconciliation '
    'before it, changing exactly the receipt path plus the seal records it names',
)
```

The drafting-time replacement (a prediction):

```text
SETTLED = (
    'K1  the preregistration at F carries one `v3-round` block: round <id>, kind '
    '<sealing|non-sealing>, record-directory <path>/, the one directory holding every '
    'control-plane path of delta(D, F); the receipt must agree with it',
    'K2  at F the preregistration carries exactly one `v3-governed-paths` block and exactly one '
    '`v3-round` block, and no amendment carries either',
    'K3  for every reconciliation, D lies on the first-parent chain of its first parent; for i>1, '
    'the previous first parent lies on the first-parent chain of this one',
    'K4  every receipt commit, superseded or final, is a single-parent child of the reconciliation '
    'before it, changing exactly the receipt path plus the seal records the final receipt names; '
    'a superseded receipt is not read',
)
```

#### Site `s5.3`

The site:

```text
            print('provisional readings (bind this tool only; to be settled by a specification '
                  'round before any promotion):')
            for k in READINGS:
```

The drafting-time replacement (a prediction):

```text
            print('settled rules (verification/infrastructure/v3/architecture.md):')
            for k in SETTLED:
```

#### Site `s5.4`

The site:

```text
# the control plane at F (T1, with the K1 and K2 readings)
```

The drafting-time replacement (a prediction):

```text
# the control plane at F (T1, with K1 and K2)
```

#### Site `s5.5`

The site:

```text
    """S2, read as covering every commit of the round after F (gap G7): the control-plane files
    have at each named commit exactly their states at F."""
```

The drafting-time replacement (a prediction):

```text
    """S2 and G7: at every commit of the round after F, the control-plane files have exactly
    their states at F."""
```

#### Site `s5.6`

The site:

```text
    """S3's form, read as binding every execution commit, certified or not (gap G5)."""
```

The drafting-time replacement (a prediction):

```text
    """S3's form and G5: it binds every execution commit, certified or not."""
```

## The README paragraph, FROZEN as text

At stage 5 the paragraph below, which occurs exactly once in `verification/README.md` at `B`, is
replaced by the second, and nothing else in the file changes.

The paragraph at `B`:

```text
`tools/v3_verifier.py` is the V3 shadow verifier, installed by round `V3-2`
(`infrastructure/round-v3-2-shadow-verifier/`). It implements the protocol-3 specification
(`infrastructure/v3/architecture.md`) with the provisional readings `V3-2`'s preregistration froze,
and it gates nothing: it has no authoritative mode, no verdict it prints changes an exit status,
the release gate does not invoke it, and its workflow job, `V3 shadow verifier`, is not a required
check. `V1` and `V2` remain authoritative. Its conformance corpus is
`infrastructure/v3/conformance/`, executed as an exact set; its comparison with `V2` over the
attestation rows is `V3-2`'s `census.json`.
```

The paragraph at `E`:

```text
`tools/v3_verifier.py` is the V3 shadow verifier, installed by round `V3-2`
(`infrastructure/round-v3-2-shadow-verifier/`). It is the V3 shadow implementation of the
currently settled protocol-3 rules (`infrastructure/v3/architecture.md`), including the
settlements of `K1`–`K4` and `G5`–`G7` that round `V3-3` fixed
(`infrastructure/round-v3-3-specification-resolution/`) and round `V3-4` implemented
(`infrastructure/round-v3-4-implementation-conformance/`). The gaps `G8`–`G12` that `V3-3`
recorded remain unsettled, and the shadow implements no settlement of them. It gates nothing: it
has no authoritative mode, no verdict it prints changes an exit status, the release gate does not
invoke it, and its workflow job, `V3 shadow verifier`, is not a required check. `V1` and `V2`
remain authoritative. Its conformance corpus is `infrastructure/v3/conformance/`, executed as an
exact set; its comparison with `V2` over the attestation rows is `V3-2`'s `census.json`.
```

## The vectors, FROZEN

The eleven vectors of `conformance-pending/` move into `conformance/` unchanged, byte for byte,
each in the commit of the stage that makes it pass:

| stage | vectors moved |
|---|---|
| 1 | `k2-reject-governed-block-only-in-amendment`, `k2-reject-round-block-only-in-amendment` |
| 2 | `k4-admit-superseded-receipt-unreadable`, `k4-reject-superseded-receipt-authorizes-own-extra-path`, `g7-reject-superseded-receipt-commit-changes-preregistration` |
| 3 | `g6-reject-record-class-by-broader-entry`, `g6-reject-record-entry-outside-own-record`, `g6-reject-execution-entry-within-record-directory`, `g6-reject-record-file-entry-in-non-sealing-round`, `g6-reject-halted-landing-publishes-unnamed-seal-record`, `g6-reject-halted-record-commit-writes-unnamed-seal-record` |

After stage 3 `conformance-pending/` holds no file and so does not exist in the tree.

Stage 4 adds one vector to `conformance/`, in `V3-2`'s vector format and recipe vocabulary:

| id | settlements | recipe | expected | tool at `D` |
|---|---|---|---|---|
| `k1-admit-amendment-named-preregistration` | `K1` | round `EX-1` with the standard preregistration, committed before `F`; the commit `F` adds the amendment `<R>amendments/preregistration.md`, carrying no fenced block; two execution commits; `R1` with first parent `D`; `Q` whose receipt lists both control-plane files | HOLDS | FAILS `t1:record-directory` |

Its drafting-time bytes have SHA-256
`3c323ab012884fd8a6950354b666df58563544d26d126c5d394ab2e483284951` (a prediction, not a pin).

## The controls, FROZEN

- **`C1` — the corpus at every stage.** At each stage's commit, `tools/v3_verifier.py --corpus`
  runs `conformance/` as an exact set, every vector as expected: 95, 98, 104, 105 and 105 vectors
  after stages 1 to 5.
- **`C2` — each vector justifies its change.** Each vector moved or added at a stage runs not as
  expected under the tool at that stage's parent and as expected under the tool at that stage.
- **`C3` — own rule.** At `E`, a scratch copy of the tool with one stage's edits taken out runs
  exactly that stage's vectors not as expected and every other vector as expected, for each of
  stages 1 to 4.
- **`C4` — the census unchanged.** At `E`, `tools/v3_verifier.py --project` over the subject `B`
  gives output identical to the tool at `B` over the same subject.
- **`C5` — the self-description.** At `E`, the tool contains none of the strings `provisional`,
  `reading` and `gap G` (case-insensitive), the shadow report prints the settled rules, and
  `verification/README.md`'s paragraph is the frozen text.
- **`C6` — the self-test.** `tools/v3_verifier.py --self-test` passes at every stage's commit.

A control whose scratch copy fails for a reason other than the rule it tests is void, and its target
stops.

## The targets, FROZEN

| target | passing outcome | stop outcome |
|---|---|---|
| `V34-0` | `BASE-HOLDS` — the execution branch starts at `B`; this file's blob at `B` is the frozen one; every `B` and `D->B` row and frozen blob holds at `B` | `BASE-BROKEN` |
| `V34-1` | `K2-CONFORMS` — stage 1 changes the tool at its site and moves its two vectors; `C1`, `C2`, `C6` hold | `K2-UNMET` |
| `V34-2` | `K4-CONFORMS` — stage 2 likewise for its three vectors | `K4-UNMET` |
| `V34-3` | `G6-CONFORMS` — stage 3 likewise for its six vectors; `conformance-pending/` is gone | `G6-UNMET` |
| `V34-4` | `K1-REPAIRED` — stage 4 changes the tool at its site and adds the `K1` vector; `C1`, `C2`, `C6` hold | `K1-UNMET` |
| `V34-5` | `SELF-DESCRIPTION-CURRENT` — stage 5 changes only the tool's text and the README paragraph; `C1`, `C5`, `C6` hold | `SELF-DESCRIPTION-STALE` |
| `V34-6` | `CONTROLS-HOLD` — `C3` and `C4` hold at `E` | `CONTROL-VOID` |
| `V34-7` | `SHADOW-ONLY` — `.github/workflows/verify.yml`, `tools/release_gate.py`, `tools/certificate_verifier.py`, the guard, `AGENTS.md` and `architecture.md` have their `B` blobs at `E`; no `verification/receipts/` directory exists; the exact-head run on `E` gives the guard 105 PASS and 0 FAIL with `D`'s verdict map, the release gate 19 of 19 with `V2` authoritative OK, and the shadow job its self-test and the 105-vector corpus | `AUTHORITY-LEAKED` — fails the round |
| `V34-8` | `SCOPE-HELD` — `git diff --no-renames --name-status B E` is exactly the mutation budget | `SCOPE-EXCEEDED` |

## Predictions, with strength

| target | predicted outcome | strength | reason |
|---|---|---|---|
| `V34-0` | `BASE-HOLDS` | strong | only this file lies between `D` and `B` |
| `V34-1` | `K2-CONFORMS`; tool blob `27f74108f5e9a5d0e8ecb0c0c400f1ccdbf01777` | strong | measured at `D` (`F3`) |
| `V34-2` | `K4-CONFORMS`; tool blob `14768bfc36fbb108ae4980c9041e34ab2b2d4175` | strong | measured at `D` (`F3`) |
| `V34-3` | `G6-CONFORMS`; tool blob `42b2d61c178af3b1a80104215a48bbea305ee714` | strong | measured at `D` (`F3`); equals `V3-3`'s settlement patch |
| `V34-4` | `K1-REPAIRED`; tool blob `2fbbf9ba0b3b55fa49b02f593d0ce9131ee90bef` | strong | measured at `D` (`F3`, `F4`) |
| `V34-5` | `SELF-DESCRIPTION-CURRENT`; tool blob `883122c4070408ee3957d969e095324b62e21a87`, README blob `690f841ec02dbafbed972667a426cf41fc4ca741` | strong | the frozen text, applied at `D` |
| `V34-6` | `CONTROLS-HOLD` | strong | measured at `D` (`F3`, `F5`) |
| `V34-7` | `SHADOW-ONLY` | strong | the budget writes no workflow, gate, guard or authority file |
| `V34-8` | `SCOPE-HELD` | strong | the budget is fixed here |

The predicted blobs are predictions, not pins: a stage whose blob differs while its vectors run as
their rows say reaches its passing outcome provisionally, records the divergence, and keeps it only
if the owner's review before `E`'s designation finds the divergence consistent with the stage's
semantics.

**Status rule.** The round is COMPLETE iff every target reaches its passing outcome. It is HALTED at
the first stop outcome, and the targets not reached are recorded as such.

## The order is part of the contract

| stage | targets | commit | checkpoint |
|---|---|---|---|
| 0 | `V34-0` | none | branch from `B`; blob check; rows at `B` |
| 1 | `V34-1` | one: the `K2` edit and its two vectors | `C1`, `C2`, `C6` |
| 2 | `V34-2` | one: the `K4` edit and its three vectors | `C1`, `C2`, `C6` |
| 3 | `V34-3` | one: the `G6` edits and its six vectors | `C1`, `C2`, `C6` |
| 4 | `V34-4` | one: the `K1` edit and its vector | `C1`, `C2`, `C6` |
| 5 | `V34-5` | one: the tool's text and the README paragraph | `C1`, `C5`, `C6` |
| 6 | `V34-6`, `V34-7`, `V34-8` | one: the result note; its commit is `E` | `C3`, `C4`, the closing checks, then the exact-head run |

A stage's commit changes only the tool and that stage's vectors (stages 1 to 4), or only the tool
and `verification/README.md` (stage 5). A stage whose frozen vector does not run as its row says is
a stop outcome for that target; it is recorded, and neither the vector nor the settlement is
repaired in this round.

## The mutation budget

- **Modified:** `tools/v3_verifier.py`; `verification/README.md` (the one frozen paragraph).
- **Added:** under `verification/infrastructure/v3/conformance/`, the eleven moved vectors and
  `k1-admit-amendment-named-preregistration.json`;
  `verification/infrastructure/round-v3-4-implementation-conformance/result.md`.
- **Deleted:** the eleven files of `verification/infrastructure/v3/conformance-pending/`.
- **Never written:** `verification/infrastructure/v3/architecture.md`, every other file under
  `tools/`, `.github/`, `AGENTS.md`, the guard and everything under `verification/lean/` and
  `verification/lean-mathlib/`, `verification/seals/`, `verification/certificates/`,
  `verification/programmes/`, `verification/audits/`, `verification/ROADMAP.md`, any other round's
  directory, `papers/` and `book/`. No `verification/receipts/` directory is created.

Scope is accounted with rename detection off: each moved vector is one deletion under
`conformance-pending/` and one addition under `conformance/`.

## The result note

`result.md` records: each target's outcome against its prediction; the chronology from `B` to `E`;
each stage's tool blob against its prediction, with the diff of every divergence from the
predicted text; the outputs of `C1` to `C6`, with the SHA-256 of each scratch script, none of which
is landed; the corpus count; and every discrepancy. The `E` certification record lists the
divergences for the owner's review. The exact-head run
on `E` is identified by the `E` certification record on the execution pull request, since the note
is part of `E`.

## What no outcome of this round licenses

1. Any sentence that V3 is operative, or any wiring of the shadow into a gate or required check.
2. Any claim that the settlements are correct; the vectors show that the tool implements them.
3. Treating `G8` to `G12` as settled.
4. Any change to `V1` or `V2` state, to `architecture.md`, or to another round's records.
5. Any claim about the validity of a historical round under any protocol.

## Hazards

- **`H1` — one author.** The settlements, the vectors, the tool and the controls have one author.
  The controls establish that the tool implements what the vectors encode; a misreading shared by
  all of them is not excluded, and the owner's review is the check on it.
- **`H2` — each stage is a CI build.** The shadow job runs the corpus at every push; a stage that
  moved a vector before its change would turn the job red. `F3` shows each stage's corpus runs as
  expected.
- **`H3` — the finite-vector gap.** The frozen sites and semantics bind; the predicted replacement
  text does not. The vectors cover finitely many cases of each semantics, so an implementation that
  departs from the prediction passes its vectors without thereby being shown to implement its
  semantics; the owner's review of every divergence before `E`'s designation closes that gap.
- **`H4` — frozen blobs.** If `main` moves before `B` and changes a file this freeze pins, the
  preconditions fail at `M` and the freeze is redrafted from a new `D`.

## Files

### Files this round reads AND writes

`tools/v3_verifier.py`; `verification/README.md` (the one paragraph);
`verification/infrastructure/v3/conformance/`; `verification/infrastructure/v3/conformance-pending/`
(emptied).

### Files this round reads and MUST NOT write

`verification/infrastructure/v3/architecture.md`, `.github/workflows/verify.yml`,
`tools/release_gate.py`, `tools/certificate_verifier.py`, `tools/control_plane_base_check.py`,
`tools/control_plane_lint.py`, the guard, `AGENTS.md`, and the `V3` round directories.

## Preconditions

Row `db3-only-this-file` requires that nothing but this file lie between `D` and `B`; with the
frozen blobs it fixes the objects the edits are applied to. The `B`-scoped rows assert that no
execution object exists at `B`, reading the tree directly.

```control-plane-preconditions
d: c021f12b2564a07adf9142032a0fc371d5b9c6e3
frozen-blob: tools/v3_verifier.py 2c34d4d7f1adadc4bdecbad94ff8eadb7b30f974
frozen-blob: verification/README.md 052dfa270479c12470173ee90f340c4f805dac37
frozen-blob: verification/infrastructure/v3/architecture.md 3326bf309d6392e4e5d69a9e7ab6d812dba035af
# row 1: name freedom and absences, drafting-time facts
{"id": "d1-round-free", "scope": "D", "check": "git grep -l -F -e 'V3-4' -e 'v3-4' -e 'round-v3-4' -e 'V34-' -e 'implementation-conformance' $D", "expect": "empty"}
{"id": "d1-receipts-absent", "scope": "D", "check": "git ls-tree -d --name-only $D verification/receipts", "expect": "empty"}
# row 2: the vector inventory at D
{"id": "d2-corpus-93", "scope": "D", "check": "test $(git ls-tree --name-only $D verification/infrastructure/v3/conformance/ | wc -l) -eq 93", "expect": "exit0"}
{"id": "d2-pending-11", "scope": "D", "check": "test $(git ls-tree --name-only $D verification/infrastructure/v3/conformance-pending/ | wc -l) -eq 11", "expect": "exit0"}
# row 3: provenance, D to B
{"id": "db3-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
{"id": "db3-only-this-file", "scope": "D->B", "check": "git diff --name-only $D $REF | grep -v -x -F 'verification/infrastructure/round-v3-4-implementation-conformance/preregistration.md'", "expect": "empty"}
{"id": "db3-v3-unchanged", "scope": "D->B", "check": "git diff --quiet $D $REF -- verification/infrastructure/v3/ tools/v3_verifier.py", "expect": "exit0"}
# row 4: no execution object at B
{"id": "b4-round-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-v3-4-implementation-conformance | grep -v -x -F 'verification/infrastructure/round-v3-4-implementation-conformance/preregistration.md'", "expect": "empty"}
{"id": "b4-pending-intact", "scope": "B", "check": "test $(git ls-tree --name-only $REF verification/infrastructure/v3/conformance-pending/ | wc -l) -eq 11", "expect": "exit0"}
{"id": "b4-no-receipts", "scope": "B", "check": "git ls-tree -d --name-only $REF verification/receipts", "expect": "empty"}
# row 5: this control plane at its path
{"id": "b5-present", "scope": "B", "check": "git cat-file -e $REF:verification/infrastructure/round-v3-4-implementation-conformance/preregistration.md", "expect": "exit0"}
```

## The landing shape

Non-sealing under §A.37, `E` → `L` on the execution pull request, no `P`. `L`'s first parent is
current green `main`, its second parent exactly `E`; conflicts, if any, are resolved in `L` by
merits. Full continuous integration passes on `L` before it merges, and the push run on `main` is
green before any later round's landing is built.

## Execution discipline

The execution branch is created from `B` and nothing else, after `B`'s push run is green including
the control-plane base check in mode `B`. Its first act is the blob check of this file at `B`. It
never absorbs later `main` before `E`; no rebase, amend or force-push. Each commit-bearing stage
commits before its checkpoint. The execution pull request may be opened after stage 1, held from
merging, so that every stage's push receives continuous integration. A stop outcome halts the round;
the halt is recorded in a result note with the outcomes reached, and nothing else of the execution
lands.

The round's chronology is the executor's check at `E` that every commit of `git rev-list E ^B` has
one parent, that the oldest has `B` as its parent, and that the branch absorbed no later `main`,
recorded in the result and followed by exact-head review. `V3-4` carries no guard clause, manifest
record or round certificate.

## Points at which this freeze chose a reading, recorded rather than resolved

- **`R1` — sites and semantics frozen, text predicted.** The owner's direction freezes the sites
  and their semantics, not the scratch patch, and requires the owner's review of any divergence from
  the predicted text before `E`'s designation. The declined options are freezing the replacement
  text, which would make any rewording a stop, and accepting any edit that passes the vectors,
  which would make the semantics no stronger than the vectors.
- **`R2` — one stage per settlement.** Each stage's vectors are decided by its own edits alone
  (`F3`), so each commit is a self-contained step from a failing vector to a passing one. The
  declined option lands all edits in one commit, which loses that audit trail.
- **`R3` — the `K1` repair as its own stage.** The repair is not a settlement departure but a defect
  against the `V3-2` reading as well; it is staged after the settlements so that their vectors are
  measured on the tool that `V3-3` measured.
- **`R4` — the self-description last.** The tool's text and the README paragraph change only once
  the behaviour conforms (`V34-5` after `V34-1` to `V34-4`).
- **`R5` — no guard clause, certificate or attestation**, as for `V3-1` to `V3-3`.
