# Verifier round V3-6 — V3 final implementation conformance: PREREGISTRATION

**Status: control plane.** This file is the round's preregistration and nothing else. The changed
shadow verifier, the moved vectors, the README paragraph and the result note are execution objects,
created only after the certified merge of this file.

> **The shadow is brought to the whole settled specification, and the vectors decide whether it
> arrived.** Each change to the tool lands in the same commit as the vectors that justify it, each
> of which fails on the tool before the change and passes after it.

## The commit vocabulary this freeze uses, fixed first

`V3-6` is run under `AGENTS.md` §A.37 as it stands at `D`: this control plane, then one execution
pull request that carries its landing.

- `D` = `a6efb46745e059c9c138cc7c420186521d331562`, the drafting snapshot: the certified head of
  `main` after `V3-5`'s landing (push run 36015136495, all six jobs green). Every measurement in
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

## What `V3-6` is, and what it is not

`V3-6` is an **implementation round**. It changes `tools/v3_verifier.py` so that the shadow
implements the two settlements of `V3-5` it does not yet meet, `G10` and `G12`, moves the seventeen
vectors of `verification/infrastructure/v3/conformance-pending/` into the corpus, and brings the
tool's printed rules and the README paragraph on the shadow into line with what the tool then does.
After it, the shadow implements every settlement `architecture.md` carries, and the corpus has no
pending part.

It is not:

1. **A specification round.** `architecture.md` is not written. Where the tool and the settled text
   disagree, the text decides.
2. **A promotion.** No act of `V3-2`'s promotion boundary is performed: no release-gate wiring, no
   change to the workflow or to any required check, no receipt, no operative language in
   `AGENTS.md`. The shadow gates nothing, and `V1` and `V2` stay authoritative and unchanged.
3. **A seal or receipt round.** No file is written under `verification/receipts/`,
   `verification/v3-seals/` or `verification/seals/`, and neither of the first two directories is
   created. `G12`'s seal record is a path the tool checks in the synthetic rounds the vectors
   build, not a file this round writes.
4. **A migration or bootstrap round.** No historical round is translated or classified, and nothing
   about the certification or publication of the first V3-governed round is addressed.

## Measurements at `D` that shape the round

### `F1` — name freedom

`V3-6`, `v3-6`, `round-v3-6`, `V36-` and `final-conformance` occur nowhere in the tree at `D`.
Neither `verification/receipts/` nor `verification/v3-seals/` exists at `D`.

### `F2` — the objects the round reads or writes, at `D`

| path | blob at `D` |
|---|---|
| `tools/v3_verifier.py` | `883122c4070408ee3957d969e095324b62e21a87` |
| `verification/README.md` | `50c390168966980c4ebf590a78c4269089af68c2` |
| `verification/infrastructure/v3/architecture.md` | `12cff3f2c9b2cb7803ed1572c98bccba7590c707` |
| `.github/workflows/verify.yml` | `d14d19389f452b39820206d449146ac424b7706c` |

`verification/infrastructure/v3/conformance/` holds 116 vectors at `D`, and
`verification/infrastructure/v3/conformance-pending/` holds seventeen, whose digest (SHA-256 of the
files concatenated in path order) is
`8d2209b69b5f516d4d1a6ce12d633ece91e18cc4a91fd25dfb3f7ed90a994069`: six whose ids begin `g10-` and
eleven whose ids begin `g12-`. The workflow runs `--self-test`, `--corpus` with the default
directory, and `--mode shadow`; it names neither vector directory and pins no vector count.

### `F3` — the verdict table, measured at `D` in scratch

The execution was simulated at `D` in a scratch worktree: each stage below was applied at its frozen
sites and committed there with its vectors, and every tool run was the committed tool at that
commit, run from the worktree (`ok` = as expected):

| vectors | tool at `D` | stage 1 | stage 2 | stage 3 |
|---|---|---|---|---|
| the 116 of `conformance/` | ok | ok | ok | ok |
| the six `G10` pending vectors | not | ok | ok | ok |
| the eleven `G12` pending vectors | not | not | ok | ok |

Each stage turns exactly its own vectors as expected and turns no vector not as expected; the
corpus runs as an exact set of 122, 133 and 133 vectors after stages 1 to 3. With either stage's
edits reverted in the stage-3 tool, exactly that stage's vectors run not as expected and every other
vector as expected. The finer own-rule measurement is `C3`'s table below.

### `F4` — the relation to `V3-5`'s settlement patch

`V3-5`'s controls ran a scratch settlement patch (SHA-256 `b63e12d8`) with five rules, one for
`G10` and four for `G12`. The stage-2 tool implements the same five rules and runs all 133 vectors
as expected, as the patch does. It differs from the patch in two ways, neither of which any vector
separates:

1. **Ownership is an argument.** The patch told `authorized` which receipt and seal record are the
   round's own through a module-level variable set during verification. The stage-2 tool passes the
   round's own receipt path and seal record path to `authorized`, and through it to every caller,
   as an explicit argument.
2. **The `s7` vector runner's round.** The runner checks a governed-path block against a round
   named by record directory and receipt path, with no kind. The patch left a file `record` entry
   outside the record directory unchecked there. The stage-2 tool admits, for a round of unknown
   kind, only the one entry a sealing round may carry — `record A` of the seal record path — and
   fails every other `record` entry outside the record directory, as it does for a round of known
   kind.

### `F5` — what the edits leave unchanged

The stage-3 tool gives output identical to the tool at `D` for `--project` over the subject `D`
(68 lines, SHA-256 `fde7c73a0b00a27a5ec41f4c699f8d83f562bbd7c9f00e3c4c84d283ce989333`), so
`V3-2`'s `census.json` still describes the shadow's comparison with `V2`. The self-test passes at
every stage.

### `F6` — the shadow report at the simulated `E`

`python3 tools/v3_verifier.py --mode shadow --subject <stage-3 commit>`, run from the scratch
worktree at the stage-3 commit, prints the unchanged banner, then the settled rules `K1`–`K4` and
`G5`–`G12` in that order, the corpus line `CORPUS  133 vector(s), exact and as expected`, the 36
projection rows with `PROJECTION  cells 126`, and `v3_verifier: shadow report complete (corpus as
expected)`, and exits 0. The tool finds its default corpus next to its own file, so a copy of the
tool run from outside a checkout reports the corpus absent; only a run of the committed tool from
the repository measures the report (`C5`).

### `F7` — tooling at `D`

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

### Stage 1 — `G10`: declaration blocks are recognized by exact lines

**Semantics.** The blocks are recognized in the bytes of each control-plane file, line by line and
without Markdown semantics, a line being the bytes between two LF bytes or between an end of the
file and an LF, with a CR belonging to the line. An opener for `I` (`v3-round` or
`v3-governed-paths`) is a line that is exactly three backticks followed by `I`; a closer is a line
that is exactly three backticks. A near miss for `I` is a line that is not an opener and consists of
zero or more spaces and TABs, a run of three or more backticks or of three or more tildes, zero or
more spaces and TABs, `I`, and then either nothing or a space, a TAB or a CR followed by any bytes.
Every line of every control-plane file at `F` is examined, a block's body included; a near miss
anywhere makes the control plane invalid (`t1:`). An opener without a closer remains invalid as at
`D`, and a line whose info string only begins with `I` is neither an opener nor a near miss.

#### Site `s1.1`

The site:

```text
    return out


def path_ok(p):
```

The drafting-time replacement (a prediction):

```text
    return out


# G10: a line with an opener's shape for a reserved info string that is not an opener.
NEAR_MISS = re.compile(r'[ \t]*(?:`{3,}|~{3,})[ \t]*(v3-round|v3-governed-paths)(?:[ \t\r].*)?',
                       re.S)


def has_near_miss(text):
    """G10: whether a line of `text` is a near miss for a reserved info string."""
    for line in text.split('\n'):
        m = NEAR_MISS.fullmatch(line)
        if m and line != '```' + m.group(1):
            return True
    return False


def path_ok(p):
```

#### Site `s1.2`

The site:

```text
        t = repo.blob(files[p]).decode('utf-8', 'replace')
        g = fenced_blocks(t, 'v3-governed-paths')
```

The drafting-time replacement (a prediction):

```text
        t = repo.blob(files[p]).decode('utf-8', 'replace')
        if has_near_miss(t):
            return None, None, None, None, files, codes + ['t1:near-miss']
        g = fenced_blocks(t, 'v3-governed-paths')
```

### Stage 2 — `G12`: the seal record

**Semantics.** A sealing round's one seal record path is `verification/v3-seals/<round>.json`.

1. **The entry at `F`.** The governed-path block of a sealing round carries `record A` of that path;
   it is the one `record` entry outside the record directory a block may carry, and only with the
   operations `A`; a sealing round's block without it is invalid (`t1:`). A non-sealing round may
   carry no `record` entry outside its record directory.
2. **The receipt.** A receipt's `seal.records` names exactly one path, the seal record path of the
   receipt's `round` (`s4:`).
3. **Other rounds' state.** A change is unauthorized, whichever entry governs it, when it is to a
   path under `verification/receipts/` other than the round's receipt path, to a path under
   `verification/v3-seals/` other than its seal record path (every such path, for a non-sealing
   round), or to any path under `verification/seals/`. This binds every authorization the
   lifecycle makes: the execution, the landing, the halted landing and the receipt commits.
4. **The receipt commits.** Each receipt commit's changes, superseded or final, are authorized under
   `S7` with rule 3, so that a file already at the seal record path, whose change is a modification
   rather than an addition, is not written (`s10:`).

#### Site `s2.1`

The site:

```text
def authorized(entries, status, path):
    e = governing(entries, path)
```

The drafting-time replacement (a prediction):

```text
def seal_record_path(round_id):
    """G12: a sealing round's one seal record path."""
    return 'verification/v3-seals/%s.json' % round_id


def foreign(own, path):
    """G12: whether `path` is receipt or seal state that is not the round's own, where `own` is
    the round's (receipt path, seal record path or None)."""
    if isinstance(path, bytes):
        path = path.decode('utf-8', 'replace')
    return (path.startswith('verification/receipts/') and path != own[0]) \
        or path.startswith('verification/seals/') \
        or (path.startswith('verification/v3-seals/') and path != own[1])


def authorized(entries, status, path, own):
    if foreign(own, path):
        return False
    e = governing(entries, path)
```

#### Site `s2.2`

The site:

```text
    codes = []
    literal = {e[2] for e in entries if e[0] == 'record'}
```

The drafting-time replacement (a prediction):

```text
    codes = []
    seal = seal_record_path(rp[len('verification/receipts/'):-len('.json')])
    literal = {e[2] for e in entries if e[0] == 'record'}
```

#### Site `s2.3`

The site:

```text
        if cls == 'record' and p not in (rd, rp) and not p.startswith(rd):
            if p.endswith('/') or kind == 'non-sealing':
                codes.append(fam + ':record-entry-outside-own-record')
    return codes
```

The drafting-time replacement (a prediction):

```text
        if cls == 'record' and p not in (rd, rp) and not p.startswith(rd):
            if kind != 'non-sealing' and p == seal and ops == 'A':
                continue
            codes.append(fam + ':record-entry-outside-own-record')
    if kind == 'sealing' and ('record', 'A', seal) not in entries:
        codes.append(fam + ':seal-record-entry')
    return codes
```

#### Site `s2.4`

The site:

```text
            ps = [x['path'].encode() for x in seal['records']]
            ok = ps == sorted(set(ps))
        if not ok:
            codes.append('s4:seal')
```

The drafting-time replacement (a prediction):

```text
            ps = [x['path'].encode() for x in seal['records']]
            ok = ps == sorted(set(ps))
        if ok and isinstance(r.get('round'), str):
            ok = ps == [seal_record_path(r['round']).encode()]
        if not ok:
            codes.append('s4:seal')
```

#### Site `s2.5`

The site:

```text
def check_execution(repo, f, e, rdir, entries):
```

The drafting-time replacement (a prediction):

```text
def check_execution(repo, f, e, rdir, entries, own):
```

#### Site `s2.6`

The site:

```text
        if not authorized(entries, st, path):
            codes.append('s3:unauthorized')
```

The drafting-time replacement (a prediction):

```text
        if not authorized(entries, st, path, own):
            codes.append('s3:unauthorized')
```

#### Site `s2.7`

The site:

```text
def check_landing_complete(repo, d, e, lb, lam, entries, resolved, receipt_path):
```

The drafting-time replacement (a prediction):

```text
def check_landing_complete(repo, d, e, lb, lam, entries, resolved, receipt_path, own):
```

#### Site `s2.8`

The site:

```text
        if not authorized(entries, st, path):
            codes.append('s9:landing-unauthorized')
```

The drafting-time replacement (a prediction):

```text
        if not authorized(entries, st, path, own):
            codes.append('s9:landing-unauthorized')
```

#### Site `s2.9`

The site:

```text
def check_landing_halted(repo, lb, lam, entries, rdir, receipt_path):
```

The drafting-time replacement (a prediction):

```text
def check_landing_halted(repo, lb, lam, entries, rdir, receipt_path, own):
```

#### Site `s2.10`

The site:

```text
        if not authorized(entries, st, path):
            codes.append('s12:landing-unauthorized')
```

The drafting-time replacement (a prediction):

```text
        if not authorized(entries, st, path, own):
            codes.append('s12:landing-unauthorized')
```

#### Site `s2.11`

The site:

```text
    codes += check_t1(repo, d, f, cp_files)
```

The drafting-time replacement (a prediction):

```text
    codes += check_t1(repo, d, f, cp_files)
    own = ('verification/receipts/%s.json' % rid,
           seal_record_path(rid) if kind == 'sealing' else None)
```

#### Site `s2.12`

The site:

```text
        codes += check_execution(repo, f, e, rdir, entries)
```

The drafting-time replacement (a prediction):

```text
        codes += check_execution(repo, f, e, rdir, entries, own)
```

#### Site `s2.13`

The site:

```text
                                                lan['resolved_paths'], receipt_path)
```

The drafting-time replacement (a prediction):

```text
                                                lan['resolved_paths'], receipt_path, own)
```

#### Site `s2.14`

The site:

```text
        lcodes, ldelta = check_landing_halted(repo, lb, lam, entries, rdir, receipt_path)
```

The drafting-time replacement (a prediction):

```text
        lcodes, ldelta = check_landing_halted(repo, lb, lam, entries, rdir, receipt_path,
                                              own)
```

#### Site `s2.15`

The site:

```text
            if not receipt_delta_ok(repo, rc, prev_q, receipt_path, seal_paths):
                codes.append('s10:superseded-receipt-commit')
```

The drafting-time replacement (a prediction):

```text
            if not receipt_delta_ok(repo, rc, prev_q, receipt_path, seal_paths):
                codes.append('s10:superseded-receipt-commit')
            elif not all(authorized(entries, x[0], x[1], own) for x in repo.delta(rc, prev_q)):
                codes.append('s10:receipt-commit-unauthorized')
```

#### Site `s2.16`

The site:

```text
    if not receipt_delta_ok(repo, lam, q, receipt_path, seal_paths):
        codes.append('s10:receipt-commit-delta')
```

The drafting-time replacement (a prediction):

```text
    if not receipt_delta_ok(repo, lam, q, receipt_path, seal_paths):
        codes.append('s10:receipt-commit-delta')
    elif not all(authorized(entries, x[0], x[1], own) for x in repo.delta(lam, q)):
        codes.append('s10:receipt-commit-unauthorized')
```

### Stage 3 — the tool's description of itself

**Semantics.** The tool describes itself as implementing the settled specification, naming the
rounds that fixed the settlements; its printed rules state `K1`–`K4` and `G5`–`G12`, in that order,
each once, in terms of what the tool checks; it carries no statement that a settlement is
unimplemented or pending. The banner, the entry points and every verdict are unchanged.

#### Site `s3.1`

The site:

```text
It implements the settlements of K1-K4 and G5-G7 that round V3-3 fixed in the specification; the
rules K1-K4 are printed at every shadow run.
```

The drafting-time replacement (a prediction):

```text
It implements the settled specification: the settlements of K1-K4 and G5-G7 that round V3-3 fixed
and of G8-G12 that round V3-5 fixed. The settled rules are printed at every shadow run.
```

#### Site `s3.2`

The site:

```text
    'K4  every receipt commit, superseded or final, is a single-parent child of the reconciliation '
    'before it, changing exactly the receipt path plus the seal records the final receipt names; '
    'a superseded receipt is not read',
)
```

The drafting-time replacement (a prediction):

```text
    'K4  every receipt commit, superseded or final, is a single-parent child of the reconciliation '
    'before it, changing exactly the receipt path plus the seal records the final receipt names; '
    'a superseded receipt is not read',
    'G5  the execution commits of a halted round are linear from F and change no control-plane '
    'file; their delta from F need not be authorized',
    'G6  the governed-path block at F has literal record entries for the record directory and the '
    'receipt path, no execution entry within the record directory, and no other record entry '
    'outside it but a sealing round\'s `record A` of its seal record path',
    'G7  at every commit of the round after F, superseded or final, the control-plane files are '
    'exactly those at F, each with its state at F',
    'G8  no ref, branch or host state is a predicate input; a control plane that names one changes '
    'no predicate',
    'G9  before F the control plane is a draft: its commits may add, modify or delete '
    'control-plane files, and only the declarations at F are read',
    'G10 declaration blocks are recognized by exact lines: an opener is three backticks and the '
    'info string, a closer three backticks; a near miss of a reserved info string in any '
    'control-plane file at F makes the control plane invalid',
    'G11 the reconciliations and receipt commits of the round are exactly the chain Q reaches; an '
    'abandoned attempt is not an object of the round',
    'G12 a sealing round has one seal record, verification/v3-seals/<round>.json, declared '
    '`record A` and named alone by its receipt; no round changes another round\'s receipt or V3 '
    'seal record, or any path under verification/seals/',
)
```

## The README paragraph, FROZEN as text

At stage 3 the paragraph below, which occurs exactly once in `verification/README.md` at `B`, is
replaced by the second, and nothing else in the file changes.

The paragraph at `B`:

```text
`tools/v3_verifier.py` is the V3 shadow verifier, installed by round `V3-2`
(`infrastructure/round-v3-2-shadow-verifier/`). It implements the protocol-3 rules of
`infrastructure/v3/architecture.md` with two exceptions. It implements the settlements of
`K1`–`K4` and `G5`–`G7` that round `V3-3` fixed
(`infrastructure/round-v3-3-specification-resolution/`) and round `V3-4` implemented
(`infrastructure/round-v3-4-implementation-conformance/`), and it meets the settlements of `G8`,
`G9` and `G11` that round `V3-5` fixed (`infrastructure/round-v3-5-specification-completion/`).
It does not implement `V3-5`'s settlements of `G10` and `G12`; the vectors that separate them from
its behaviour are in `infrastructure/v3/conformance-pending/`, which it does not run. It gates
nothing: it has no authoritative mode, no verdict it prints changes an exit status, the release
gate does not invoke it, and its workflow job, `V3 shadow verifier`, is not a required check. `V1`
and `V2` remain authoritative. Its conformance corpus is `infrastructure/v3/conformance/`, executed
```

The paragraph at `E`:

```text
`tools/v3_verifier.py` is the V3 shadow verifier, installed by round `V3-2`
(`infrastructure/round-v3-2-shadow-verifier/`). It implements the settled protocol-3 rules of
`infrastructure/v3/architecture.md`: the settlements of `K1`–`K4` and `G5`–`G7` that round `V3-3`
fixed (`infrastructure/round-v3-3-specification-resolution/`) and round `V3-4` implemented
(`infrastructure/round-v3-4-implementation-conformance/`), and the settlements of `G8`–`G12` that
round `V3-5` fixed (`infrastructure/round-v3-5-specification-completion/`) and round `V3-6`
implemented (`infrastructure/round-v3-6-final-conformance/`). It gates nothing: it has no
authoritative mode, no verdict it prints changes an exit status, the release gate does not invoke
it, and its workflow job, `V3 shadow verifier`, is not a required check. `V1` and `V2` remain
authoritative. Its conformance corpus is `infrastructure/v3/conformance/`, executed as an exact
set; its comparison with `V2` over the attestation rows is `V3-2`'s `census.json`.
```

## The vectors, FROZEN

The seventeen vectors of `conformance-pending/` move into `conformance/` unchanged, byte for byte,
each in the commit of the stage that makes it pass. No vector is added, changed or removed
otherwise.

| stage | vectors moved |
|---|---|
| 1 | `g10-reject-indented-opener`, `g10-reject-longer-backtick-fence`, `g10-reject-near-miss-in-amendment`, `g10-reject-opener-with-cr`, `g10-reject-opener-with-trailing-text`, `g10-reject-tilde-fence` |
| 2 | `g12-reject-execution-changes-another-rounds-receipt`, `g12-reject-execution-changes-another-rounds-seal-record`, `g12-reject-execution-changes-legacy-seal-namespace`, `g12-reject-receipt-names-second-seal-record`, `g12-reject-receipt-seal-path-not-fixed`, `g12-reject-seal-entry-in-legacy-namespace`, `g12-reject-seal-entry-names-another-rounds-receipt`, `g12-reject-seal-entry-not-add-only`, `g12-reject-seal-entry-not-at-fixed-path`, `g12-reject-seal-record-path-already-present`, `g12-reject-sealing-round-without-seal-entry` |

After stage 2 `conformance-pending/` holds no file and so does not exist in the tree.

## The controls, FROZEN

- **`C1` — the corpus at every stage.** At each stage's commit and at `E`,
  `tools/v3_verifier.py --corpus` runs `conformance/` as an exact set, every vector as expected:
  122, 133 and 133 vectors after stages 1 to 3, and 133 at `E`.
- **`C2` — each vector justifies its change.** Each vector moved at a stage runs not as expected
  under the tool at that stage's parent and as expected under the tool at that stage.
- **`C3` — own rule.** At `E`, a scratch copy of the tool with one rule's behaviour taken out runs
  exactly that rule's vectors not as expected and every other vector of the corpus as expected, for
  each of the five rules; and a scratch copy with one stage's edits reverted does the same for that
  stage's vectors, for stages 1 and 2:

  | rule taken out | its vectors |
  |---|---|
  | near misses (`G10`) | the six `g10-reject-` vectors moved at stage 1 |
  | the seal entry at `F` (`G12` 1) | `g12-reject-seal-entry-in-legacy-namespace`, `g12-reject-seal-entry-names-another-rounds-receipt`, `g12-reject-seal-entry-not-add-only`, `g12-reject-seal-entry-not-at-fixed-path`, `g12-reject-sealing-round-without-seal-entry` |
  | the receipt names the seal record alone (`G12` 2) | `g12-reject-receipt-names-second-seal-record`, `g12-reject-receipt-seal-path-not-fixed` |
  | no change to other rounds' state (`G12` 3) | `g12-reject-execution-changes-another-rounds-receipt`, `g12-reject-execution-changes-another-rounds-seal-record`, `g12-reject-execution-changes-legacy-seal-namespace` |
  | each receipt commit's changes authorized (`G12` 4) | `g12-reject-seal-record-path-already-present` |

- **`C4` — the census unchanged.** At `E`, `tools/v3_verifier.py --project` over the subject `B`
  gives output identical to the tool at `B` over the same subject.
- **`C5` — the self-description, by its semantic outputs.** At `E`, the committed tool, run from a
  checkout of `E` as `python3 tools/v3_verifier.py --mode shadow --subject E`, exits 0 and prints:
  as its first line the banner `v3_verifier shadow report -- SHADOW ONLY: this report gates nothing;
  V1 and V2 remain authoritative`; the settled rules `K1`–`K4` and `G5`–`G12`, in that order, each
  once; the line `CORPUS  133 vector(s), exact and as expected`; the line `PROJECTION  cells 126`;
  and as its last line `v3_verifier: shadow report complete (corpus as expected)`. The tool and
  `verification/README.md` contain none of the strings `conformance-pending`, `does not implement`
  and `remain unsettled` (case-insensitive), and the README's paragraph is the frozen text. The
  wording of each printed rule and the report's bytes are not controls.
- **`C6` — the self-test.** `tools/v3_verifier.py --self-test` passes at every stage's commit.

A control whose scratch copy fails for a reason other than the rule it tests is void, and its target
stops.

## The targets, FROZEN

| target | passing outcome | stop outcome |
|---|---|---|
| `V36-0` | `BASE-HOLDS` — the execution branch starts at `B`; this file's blob at `B` is the frozen one; every `B` and `D->B` row and frozen blob holds at `B` | `BASE-BROKEN` |
| `V36-1` | `G10-CONFORMS` — stage 1 changes the tool at its sites and moves its six vectors; `C1`, `C2`, `C6` hold | `G10-UNMET` |
| `V36-2` | `G12-CONFORMS` — stage 2 changes the tool at its sites and moves its eleven vectors; `C1`, `C2`, `C6` hold; `conformance-pending/` is gone | `G12-UNMET` |
| `V36-3` | `SELF-DESCRIPTION-CURRENT` — stage 3 changes only the tool's text and the README paragraph; `C1`, `C6` hold | `SELF-DESCRIPTION-STALE` |
| `V36-4` | `CONTROLS-HOLD` — `C3`, `C4` and `C5` hold at `E` | `CONTROL-VOID` |
| `V36-5` | `SHADOW-ONLY` — `.github/workflows/verify.yml`, `tools/release_gate.py`, `tools/certificate_verifier.py`, the guard, `AGENTS.md` and `architecture.md` have their `B` blobs at `E`; neither `verification/receipts/` nor `verification/v3-seals/` exists at `E` and nothing under `verification/seals/` changed; the exact-head run on `E` gives the guard 105 PASS and 0 FAIL with `D`'s verdict map, the release gate 19 of 19 with `V2` authoritative OK, and the shadow job its self-test and the 133-vector corpus | `AUTHORITY-LEAKED` — fails the round |
| `V36-6` | `SCOPE-HELD` — `git diff --no-renames --name-status B E` is exactly the mutation budget | `SCOPE-EXCEEDED` |

## Predictions, with strength

| target | predicted outcome | strength | reason |
|---|---|---|---|
| `V36-0` | `BASE-HOLDS` | strong | only this file lies between `D` and `B` |
| `V36-1` | `G10-CONFORMS`; tool blob `db23329d43c0aeafac054a556a64f5a4c364dfcb` | strong | measured at `D` (`F3`) |
| `V36-2` | `G12-CONFORMS`; tool blob `5bd01380dd301bad6ddfc0569ec90369905ff881` | strong | measured at `D` (`F3`, `F4`) |
| `V36-3` | `SELF-DESCRIPTION-CURRENT`; tool blob `21ea40977655d4a36c6e387b496ec5e353e9196b`, README blob `08cb79621b1c0e85d4180d8a00081906f35f11f9` | strong | the frozen text, applied at `D` |
| `V36-4` | `CONTROLS-HOLD` | strong | measured at `D` (`F3`, `F5`, `F6`) |
| `V36-5` | `SHADOW-ONLY` | strong | the budget writes no workflow, gate, guard, authority, receipt or seal file |
| `V36-6` | `SCOPE-HELD` | strong | the budget is fixed here |

The predicted blobs are predictions, not pins: a stage whose blob differs while its vectors run as
their rows say reaches its passing outcome provisionally, records the divergence, and keeps it only
if the owner's review before `E`'s designation finds the divergence consistent with the stage's
semantics.

**Status rule.** The round is COMPLETE iff every target reaches its passing outcome. It is HALTED at
the first stop outcome, and the targets not reached are recorded as such.

## The order is part of the contract

| stage | targets | commit | checkpoint |
|---|---|---|---|
| 0 | `V36-0` | none | branch from `B`; blob check; rows at `B` |
| 1 | `V36-1` | one: the `G10` edits and their six vectors | `C1`, `C2`, `C6` |
| 2 | `V36-2` | one: the `G12` edits and their eleven vectors | `C1`, `C2`, `C6` |
| 3 | `V36-3` | one: the tool's text and the README paragraph | `C1`, `C6` |
| 4 | `V36-4`, `V36-5`, `V36-6` | one: the result note; its commit is `E` | `C3`, `C4`, `C5`, the closing checks, then the exact-head run |

A stage's commit changes only the tool and that stage's vectors (stages 1 and 2), or only the tool
and `verification/README.md` (stage 3). A stage whose frozen vector does not run as its row says is
a stop outcome for that target; it is recorded, and neither the vector nor the settlement is
repaired in this round.

## The mutation budget

- **Modified:** `tools/v3_verifier.py`; `verification/README.md` (the one frozen paragraph).
- **Added:** under `verification/infrastructure/v3/conformance/`, the seventeen moved vectors;
  `verification/infrastructure/round-v3-6-final-conformance/result.md`.
- **Deleted:** the seventeen files of `verification/infrastructure/v3/conformance-pending/`.
- **Never written:** `verification/infrastructure/v3/architecture.md`, every other file under
  `tools/`, `.github/`, `AGENTS.md`, the guard and everything under `verification/lean/` and
  `verification/lean-mathlib/`, `verification/seals/`, `verification/certificates/`,
  `verification/programmes/`, `verification/audits/`, `verification/ROADMAP.md`, any other round's
  directory, `papers/` and `book/`. Neither `verification/receipts/` nor `verification/v3-seals/`
  is created.

Scope is accounted with rename detection off: each moved vector is one deletion under
`conformance-pending/` and one addition under `conformance/`.

## The result note

`result.md` records: each target's outcome against its prediction; the chronology from `B` to `E`;
each stage's tool blob against its prediction, with the diff of every divergence from the predicted
text; the outputs of `C1` to `C6`, with the SHA-256 of each scratch script, none of which is landed;
the corpus count; and every discrepancy. The `E` certification record lists the divergences for the
owner's review. The exact-head run on `E` is identified by the `E` certification record on the
execution pull request, since the note is part of `E`.

## What no outcome of this round licenses

1. Any sentence that V3 is operative, or any wiring of the shadow into a gate or required check.
2. Any claim that the settlements are correct; the vectors show that the tool implements them.
3. Any seal record, receipt or V3 certification of any round, this one included.
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
- **`H5` — where the tool runs.** The tool resolves its default corpus from its own location, so a
  shadow report taken from a copy outside a checkout is not a measurement of the tool (`F6`). `C5`
  is taken from the committed tool at `E`, by its semantic outputs.

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
d: a6efb46745e059c9c138cc7c420186521d331562
frozen-blob: tools/v3_verifier.py 883122c4070408ee3957d969e095324b62e21a87
frozen-blob: verification/README.md 50c390168966980c4ebf590a78c4269089af68c2
frozen-blob: verification/infrastructure/v3/architecture.md 12cff3f2c9b2cb7803ed1572c98bccba7590c707
# row 1: name freedom and absences, drafting-time facts
{"id": "d1-round-free", "scope": "D", "check": "git grep -l -F -e 'V3-6' -e 'v3-6' -e 'round-v3-6' -e 'V36-' -e 'final-conformance' $D", "expect": "empty"}
{"id": "d1-receipts-absent", "scope": "D", "check": "git ls-tree -d --name-only $D verification/receipts", "expect": "empty"}
{"id": "d1-v3-seals-absent", "scope": "D", "check": "git ls-tree -d --name-only $D verification/v3-seals", "expect": "empty"}
# row 2: the vector inventory at D
{"id": "d2-corpus-116", "scope": "D", "check": "test $(git ls-tree --name-only $D verification/infrastructure/v3/conformance/ | wc -l) -eq 116", "expect": "exit0"}
{"id": "d2-pending-17", "scope": "D", "check": "test $(git ls-tree --name-only $D verification/infrastructure/v3/conformance-pending/ | wc -l) -eq 17", "expect": "exit0"}
# row 3: provenance, D to B
{"id": "db3-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
{"id": "db3-only-this-file", "scope": "D->B", "check": "git diff --name-only $D $REF | grep -v -x -F 'verification/infrastructure/round-v3-6-final-conformance/preregistration.md'", "expect": "empty"}
{"id": "db3-v3-unchanged", "scope": "D->B", "check": "git diff --quiet $D $REF -- verification/infrastructure/v3/ tools/v3_verifier.py", "expect": "exit0"}
# row 4: no execution object at B
{"id": "b4-round-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-v3-6-final-conformance | grep -v -x -F 'verification/infrastructure/round-v3-6-final-conformance/preregistration.md'", "expect": "empty"}
{"id": "b4-pending-intact", "scope": "B", "check": "test $(git ls-tree --name-only $REF verification/infrastructure/v3/conformance-pending/ | wc -l) -eq 17", "expect": "exit0"}
{"id": "b4-no-receipts", "scope": "B", "check": "git ls-tree -d --name-only $REF verification/receipts", "expect": "empty"}
{"id": "b4-no-v3-seals", "scope": "B", "check": "git ls-tree -d --name-only $REF verification/v3-seals", "expect": "empty"}
# row 5: this control plane at its path
{"id": "b5-present", "scope": "B", "check": "git cat-file -e $REF:verification/infrastructure/round-v3-6-final-conformance/preregistration.md", "expect": "exit0"}
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
commits before its checkpoint, and stage commits are pushed without waiting for continuous
integration on them; the certification of record is the exact-head run on `E`. The execution pull
request may be opened after stage 1, held from merging. A stop outcome halts the round; the halt is
recorded in a result note with the outcomes reached, and nothing else of the execution lands.

The round's chronology is the executor's check at `E` that every commit of `git rev-list E ^B` has
one parent, that the oldest has `B` as its parent, and that the branch absorbed no later `main`,
recorded in the result and followed by exact-head review. `V3-6` carries no guard clause, manifest
record or round certificate.

## Points at which this freeze chose a reading, recorded rather than resolved

- **`R1` — sites and semantics frozen, text predicted**, as for `V3-4`: the owner reviews every
  divergence from the predicted text before `E`'s designation. The declined options are freezing
  the replacement text, which would make any rewording a stop, and accepting any edit that passes
  the vectors, which would make the semantics no stronger than the vectors.
- **`R2` — one stage per settlement.** `G10` and `G12` are decided by disjoint vectors (`F3`), so
  each commit is a self-contained step from failing vectors to passing ones. `G10` goes first
  because it changes only how the control plane at `F` is read, which precedes every check `G12`
  adds.
- **`R3` — ownership as an argument.** The round's own receipt path and seal record path reach
  `authorized` as an explicit argument, not as module state set during verification (`F4` 1). The
  declined option, the patch's module-level variable, makes a predicate's result depend on state
  outside its arguments, which the tool otherwise avoids.
- **`R4` — the `s7` runner's round of unknown kind** admits only `record A` of the seal record path
  outside the record directory (`F4` 2). The declined option, the patch's leaving a file entry
  unchecked there, keeps a pre-`G12` allowance that no settlement now grants any round.
- **`R5` — the self-description last**, as for `V3-4`: the tool's text and the README paragraph
  change only once the behaviour conforms, and the printed rules extend to `G5`–`G12` so that the
  report states every settlement the tool implements.
- **`R6` — the self-test unchanged.** The `G10` and `G12` cases are carried by the corpus, which the
  shadow job runs at every push; the declined option adds self-test fixtures that duplicate
  vectors.
- **`R7` — `C5` by semantic outputs.** The shadow report is controlled by what it states — the
  banner, the rules, the corpus result, the projection cells, the completion line — from the
  committed tool at `E`, not by byte identity with a scratch run, whose output depends on where the
  scratch file lies (`F6`, `H5`).
- **`R8` — no guard clause, certificate or attestation**, as for `V3-1` to `V3-5`.
