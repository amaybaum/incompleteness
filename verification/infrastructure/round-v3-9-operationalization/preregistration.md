# Verifier round V3-9 — V3 made operable for provisional pilots: PREREGISTRATION

**Status: control plane.** This file is the round's preregistration and nothing else. The receipt
builder, the new `AGENTS.md` section, the narrowed specification preamble and the result note are
execution objects, created only after the certified merge of this file.

> **A permanent receipt builder, and one rule that lets an owner-authorized pilot run the native V3
> lifecycle.** `tools/v3_receipt.py` derives a receipt's repository facts from exact object ids;
> `AGENTS.md` gains `§A.39`, the provisional native lifecycle; the specification's preamble says V3
> is operative for such pilots and no other round. `§A.37`, `V1` and `V2` are unchanged.

## The commit vocabulary this freeze uses, fixed first

`V3-9` is run under `AGENTS.md` §A.37 as it stands at `D`: this control plane, then one execution
pull request that carries its landing.

- `D` = `311f06ea174501587478024a09140297b56e089a`, the drafting snapshot: the certified head of
  `main` after `V3-8`'s landing (push run 36064453524, all six jobs green). Every measurement in
  this file was taken at `D` unless it says otherwise.
- `B` — the mandated execution base: the certified merge commit on `main` of this file. It has no
  object id until that merge exists and its push run is green.
- `M` — a candidate merge of this file into `main`, used only to evaluate `B`-scoped rows before the
  merge.
- `E` — the sealed execution commit, the last commit of the execution branch that branches from
  `B`.
- `L` — the landing merge: first parent current green `main`, second parent exactly `E`.

The letters `F`, `W`, `Rᵢ`, `Λ`, `LB` and `Q` keep the meanings
`verification/infrastructure/v3/architecture.md` gives them. In this file they name objects of V3
rounds in general or of the synthetic rounds the conformance vectors build, never an object of this
round.

## What `V3-9` is, and what it is not

`V3-9` is an **operationalization round**, the first of four that finish the V3 programme: `V3-9`
makes V3 operable, `V3-10` runs one real provisional pilot, `V3-11` cuts authority over, and `V3-12`
retires the old stack. Only `V3-9` is frozen here; the others are named so that the scope of this
one is legible, and nothing in this file binds them. `V3-9` adds:

1. **A receipt builder**, `tools/v3_receipt.py`. Given the exact object ids of a round's commits and
   the attestation records the host holds, it derives every repository fact the receipt carries,
   with `tools/v3_verifier.py`'s own functions, and prints the receipt. It is a builder, not a
   verifier: whether a receipt commit holds remains `tools/v3_verifier.py --verify-round`'s
   question.
2. **`§A.39` in `AGENTS.md`**: a round the owner authorizes as a provisional V3 pilot runs the
   native lifecycle — one pull request from `D`, `F` designated, linear execution to a designated
   `E`, reconciliation if needed, the receipt commit `Q` built with the builder, `--verify-round Q`
   holding before the pull request lands through ordinary review and merge. `F`'s and `E`'s
   `check-run` attestations are dispatched runs on exactly those commits, and a pilot that halts
   after `F` closes through `S12`'s halted receipt.
3. **One preamble sentence** of the specification, which says V3 is operative only for such pilots.

It is not:

1. **A promotion.** No release-gate step, workflow job or required check is added or changed, no
   verdict of `tools/v3_verifier.py` gates anything, and `V1` and `V2` stay authoritative for every
   round, pilots included.
2. **A pilot.** No receipt is written: neither `verification/receipts/` nor
   `verification/v3-seals/` is created.
3. **A change to `§A.37`, to the specification's rules, or to the verifier.** `§A.37` stays the
   default and governs `V3-9` itself; the settlements `S1`–`S13`, `K1`–`K4` and `G5`–`G12`, the
   corpus and `tools/v3_verifier.py` are unchanged.

## Measurements at `D` that shape the round

### `F1` — name freedom

`V3-9`, `v3-9`, `round-v3-9`, `V39-`, `v3_receipt` and `operationalization` occur nowhere in the
tree at `D`. Neither `tools/v3_receipt.py`, `verification/receipts/` nor `verification/v3-seals/`
exists at `D`.

### `F2` — the section number

`AGENTS.md` at `D` ends with `§A.37`, and neither `§A.38` nor `§A.39` occurs in it. `§A.38` is
already assigned, though never landed: `GH-1`'s frozen preregistration and its halt record name its
ref-hygiene rule `§A.38`. `§A.39` occurs at `D` only in `V3-1`'s preregistration, whose reading
`R2` declines to write "a prospective `§A.39`" and leaves the operative V3 rule to a later round.
This round's section is therefore `§A.39`, and `§A.38` stays `GH-1`'s.

### `F3` — the objects the round reads or writes, at `D`

| path | blob at `D` |
|---|---|
| `AGENTS.md` | `a9687b39c69973d35a2ff81c257687071fd35eca` |
| `verification/infrastructure/v3/architecture.md` | `db36dbd1ee4f779eff13525ffd3dc11d9041ab36` |
| `tools/v3_verifier.py` | `ccfbe813790e4855f408462449327f32e59d545b` |

`verification/infrastructure/v3/conformance/` holds 135 vectors at `D`. Of them, 29 are repository
vectors that commit a receipt and verify its receipt commit as holding, before any host-state step:
24 complete non-sealing, 2 complete sealing, 2 halted with execution commits and 1 halted without,
7 of the 29 with more than one reconciliation.

### `F4` — what a pilot needs from the present machinery

Measured at `D` with a scratch preregistration that carries no `control-plane-preconditions` block:
`tools/control_plane_lint.py` passes, `tools/control_plane_base_check.py --mode M` evaluates
0 rows with no failure, and `tools/artifact_placement_check.py` passes. `V2`'s live policy,
`verification/certificates/live-policy.json` (blob `78a5c1457ca222c65cb146cdcc9b3081b6e6909b`),
carries `"count": 0`, and the certificate verifier checks the certificate records that exist rather
than requiring one per round. A pilot therefore needs neither a precondition block nor a `V2`
certificate, and `V3-9` changes none of that machinery.

The guard reads `AGENTS.md` at the head in three places: `R7-MSP` for two phrases of `§A.35`, and
`SI2-7` and `SI3-6` for phrases of `§A.37` and the absence of two superseded sentences. Appending a
section after `§A.37` that carries none of those sentences changes none of the three.

### `F5` — the execution, simulated at `D`

The execution was simulated at `D` in a scratch worktree, each stage applied and committed with its
files, every tool run being the committed tool at that commit, run from the worktree. The results
are the predictions below:

| measurement | stage 1 | stage 2 |
|---|---|---|
| `tools/v3_receipt.py` blob | `e08d15f6e301bec4d32f9dab34b5c7b40fb48d1f` | the same |
| `AGENTS.md` blob | `a9687b39` | `864494c1a9696a3b08330da64cf9d265d6d8b92f` |
| `architecture.md` blob | `db36dbd1` | `f699471b34d4f332c557f6b5452c952db49a0306` |
| `tools/v3_verifier.py` blob | `ccfbe813` | the same |
| verifier corpus, exact and as expected | 135 | 135 |

At stage 1, `tools/v3_receipt.py --self-test` printed:

```text
rebuilt  29 receipt commit(s), each identical to the committed receipt and holding
shape    complete-non-sealing   24 vector(s)
shape    complete-sealing       2 vector(s)
shape    halted-exec            2 vector(s)
shape    halted-none            1 vector(s)
shape    multi-reconciliation   7 vector(s)
corrupt  identity: d                          29/29 failing
corrupt  identity: f                          29/29 failing
corrupt  control plane: a blob                29/29 failing
corrupt  control plane: governed digest       29/29 failing
corrupt  execution: tree_e                    26/26 failing
corrupt  execution: delta digest              26/26 failing
corrupt  landing: base                        29/29 failing
corrupt  landing: delta digest                29/29 failing
corrupt  landing: reconciliations             29/29 failing
corrupt  seal: blob                           2/2 failing
corrupt  attestation: subject commit          29/29 failing
corrupt  attestation: F designation missing   29/29 failing
corrupt  schema: version                      29/29 failing
v3_receipt: self-test OK
```

## The builder, FROZEN by semantics

At stage 1 the execution adds `tools/v3_receipt.py` and changes nothing else. The file below is the
drafting-time implementation, with SHA-256
`ff0f41b350401fb9fe165465be8ed384f24f6473e1569d5c20bee7d22e449919`.
It is a prediction, as is its blob. A file whose text differs is recorded as a divergence, with its
diff, and the owner reviews every divergence for consistency with the semantics below before `E` is
designated; a divergence the owner finds inconsistent is a stop outcome for `V39-1`.

**Semantics.**

1. **Inputs.** The status (`complete` or `halted`); the exact object ids of `D`, `F`, `E` (complete
   only), `W` (halted with execution commits only) and the round's reconciliations in order; the
   resolved paths; each candidate's commit and what was measured on it; for a complete sealing
   round, the bytes of the seal record the receipt commit will carry; and the attestation records as
   (kind, subject, record). Every commit argument is refused unless it is a full-length lowercase
   hexadecimal object id, before any repository read.
2. **Derived, never supplied:** `round` and `kind` from the declaration at `F`; `object_format`; the
   control-plane blobs and the governed-path digest at `F`; `tree_e` and `S8`'s digest of
   `delta(F, E)`; each candidate's tree; the landing's base (the last reconciliation's first
   parent), object (the last reconciliation) and `S8`'s digest of `delta(LB, Λ)`; the seal record's
   path and blob; each attestation's commit; and `absent` with its reason codes. Each derivation
   calls `tools/v3_verifier.py`'s own function for it.
3. **Refusals.** The builder refuses — prints a reason and writes no receipt — when the control
   plane at `F` is not valid, when the status and the supplied commits disagree, when the last
   reconciliation is not a two-parent merge, when an attestation names a subject the status has no
   commit for, or when the result would not satisfy `S4` standalone.
4. **Not read:** no ref, branch, host state, clock or network. The builder does not decide whether
   `F` or `E` was designated, whether a check passed, or whether the round holds.
5. **Output.** The receipt as one JSON object, indent 1, UTF-8, with a trailing newline, to
   standard output or `--out <file>`.
6. **`--self-test`.** For every conformance vector whose receipt commit holds, it replays the vector
   up to that commit, reads the committed receipt's supplied data, rebuilds the receipt, and
   requires the rebuilt receipt to equal the committed one, the same inputs to come back from its
   command line, and a receipt commit carrying the rebuilt receipt to hold. On each of those it
   commits thirteen corrupted receipts, one per field class — `d`; `f`; a control-plane blob; the
   governed-path digest; `tree_e`; the execution delta digest; the landing's base, delta digest and
   reconciliations; the seal blob; an attestation's commit; the missing `F` designation; the schema
   version — each applied where the receipt has the field, and requires every one to fail. It
   requires each of the five shapes, complete non-sealing, complete sealing, halted with and
   without execution commits, and more than one reconciliation, to occur at least once. Exit 0
   only if all of this holds.

```text
#!/usr/bin/env python3
"""v3_receipt.py -- builds a V3 receipt (round V3-9).

A BUILDER, NOT A VERIFIER. Given the exact object ids of a round's commits and the attestation
records the host holds, it derives every repository fact the receipt carries (S4 of
verification/infrastructure/v3/architecture.md) with tools/v3_verifier.py's own functions and prints
the receipt. It decides nothing about the round: whether the receipt commit holds is
tools/v3_verifier.py --verify-round's question, asked after the receipt is committed.

Entry points, exactly:

    --self-test     rebuilds the receipt of every conformance vector whose receipt commit holds,
                    commits each rebuilt receipt and verifies it, and verifies corrupted receipts
                    fail; exit 1 on any case not as expected
    --status complete|halted --d <D> --f <F> [--e <E>] [--withdrawal <W>]
        --reconciliation <R> ...  [--resolved <path> ...]  [--candidate <commit> <measured> ...]
        [--seal-file <file>]  --attest <kind> <F|E> <record> ...  [--out <file>]

Every repeatable option may be given more than once; --reconciliation in the round's order. Every
commit argument must be a full-length lowercase hexadecimal object id; a ref name, HEAD or an
abbreviated id is refused before any repository read. The repository is the current working
directory.

Derived from the repository: round and kind (the declaration at F), object_format, the
control-plane blobs and the governed-path digest at F, tree_e and the execution delta digest, each
candidate's tree, the landing's base, object and delta digest, and each attestation's commit.
Supplied, and never checked here: the status, which commits are D, F, E, W and the
reconciliations, the resolved paths, what was measured on each candidate, the attestation records,
and the seal record's bytes (--seal-file, the file the receipt commit will carry at the round's seal
record path). The tool reads no ref, branch, host state or clock.

Standard library only.
"""
import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v3_verifier as v3  # noqa: E402

USAGE = ('usage: v3_receipt.py --self-test | --status complete|halted --d <D> --f <F> [--e <E>] '
         '[--withdrawal <W>] --reconciliation <R> ... [--resolved <path> ...] '
         '[--candidate <commit> <measured> ...] [--seal-file <file>] '
         '--attest <kind> <F|E> <record> ... [--out <file>]')
ATTESTATION_KINDS = ('owner-designation', 'check-run')


class BuildError(Exception):
    pass


def blob_id(data, fmt):
    """The object id git gives a blob holding `data`, in the repository's object format."""
    h = hashlib.sha1 if fmt == 'sha1' else hashlib.sha256
    return h(b'blob %d\0' % len(data) + data).hexdigest()


def build(repo, status, d, f, reconciliations, attestations, e=None, withdrawal=None,
          resolved=(), candidates=(), seal_bytes=None):
    """The receipt, as a dict in the field table's order. `attestations` is a list of
    (kind, subject, record); `candidates` a list of (commit, measured)."""
    fmt = repo.fmt()
    for x in [d, f, e, withdrawal] + list(reconciliations) + [c for c, _ in candidates]:
        if x is not None:
            repo.need(v3.check_oid(x))
    if status not in ('complete', 'halted'):
        raise BuildError('status must be complete or halted')
    if status == 'complete' and (e is None or withdrawal is not None):
        raise BuildError('a complete receipt names E and no withdrawal')
    if status == 'halted' and e is not None:
        raise BuildError('a halted receipt names no E')
    if not reconciliations:
        raise BuildError('at least one reconciliation')
    rdir, rid, kind, entries, cp_files, codes = v3.control_plane(repo, d, f)
    if entries is None or codes:
        raise BuildError('the control plane at F is not valid: %s' % ', '.join(codes))
    r = {'schema': 'v3-receipt', 'version': 1, 'round': rid, 'status': status, 'kind': kind,
         'object_format': fmt, 'd': d, 'f': f,
         'control_plane_blobs': [{'path': p.decode('utf-8'), 'blob': cp_files[p]}
                                 for p in sorted(cp_files)],
         'governed_paths_digest': v3.governed_digest(entries)}
    if status == 'complete':
        r['e'] = e
        r['tree_e'] = repo.tree(e)
        r['execution_delta_digest'] = v3.delta_digest(repo.delta(f, e), fmt)
    elif withdrawal is not None:
        r['withdrawal'] = withdrawal
    r['candidates'] = [{'commit': c, 'tree': repo.tree(c), 'measured': m} for c, m in candidates]
    lam = reconciliations[-1]
    lp = repo.parents(lam)
    if len(lp) != 2:
        raise BuildError('the last reconciliation is not a two-parent merge')
    r['landing'] = {'base': lp[0], 'object': lam, 'reconciliations': list(reconciliations),
                    'resolved_paths': sorted(resolved, key=lambda p: p.encode('utf-8')),
                    'delta_digest': v3.delta_digest(repo.delta(lp[0], lam), fmt)}
    if kind == 'sealing' and status == 'complete':
        if seal_bytes is None:
            raise BuildError('a complete sealing receipt needs --seal-file')
        rec = {'path': v3.seal_record_path(rid), 'blob': blob_id(seal_bytes, fmt)}
        r['seal'] = {'records': [rec]}
    elif seal_bytes is not None:
        raise BuildError('only a complete sealing receipt names a seal record')
    subj = {'F': f, 'E': e}
    att = []
    for k, s, rec in attestations:
        if k not in ATTESTATION_KINDS or s not in subj or subj[s] is None:
            raise BuildError('attestation %s %s' % (k, s))
        att.append({'kind': k, 'subject': s, 'commit': subj[s], 'record': rec})
    r['attestations'] = att
    if status == 'halted':
        absent = {x: 'halted-before-certification'
                  for x in v3.REASONS['halted-before-certification']}
        if withdrawal is None:
            absent['withdrawal'] = 'no-execution-commits'
        r['absent'] = absent
    bad = v3.validate_receipt(r)
    if bad:
        raise BuildError('the receipt does not satisfy S4: %s' % ', '.join(bad))
    return r


def dump(r):
    return json.dumps(r, indent=1, ensure_ascii=False) + '\n'


def inputs_of(repo, r, q):
    """The supplied data of a committed receipt, as build()'s keyword arguments."""
    kw = {'status': r['status'], 'd': r['d'], 'f': r['f'],
          'reconciliations': r['landing']['reconciliations'],
          'attestations': [(a['kind'], a['subject'], a['record']) for a in r['attestations']],
          'e': r.get('e'), 'withdrawal': r.get('withdrawal'),
          'resolved': r['landing']['resolved_paths'],
          'candidates': [(c['commit'], c['measured']) for c in r['candidates']]}
    for x in r.get('seal', {}).get('records', []):
        kw['seal_bytes'] = repo.blob(repo.state(q, x['path'].encode())[1])
    return kw


def to_argv(kw, wd):
    """The command line that supplies `kw` (the seal record's bytes through a file in `wd`)."""
    argv = ['--status', kw['status'], '--d', kw['d'], '--f', kw['f']]
    for k in ('e', 'withdrawal'):
        if kw.get(k) is not None:
            argv += ['--' + k, kw[k]]
    for x in kw['reconciliations']:
        argv += ['--reconciliation', x]
    for x in kw['resolved']:
        argv += ['--resolved', x]
    for c, m in kw['candidates']:
        argv += ['--candidate', c, m]
    if kw.get('seal_bytes') is not None:
        path = os.path.join(wd, 'seal-record.bin')
        with open(path, 'wb') as fh:
            fh.write(kw['seal_bytes'])
        argv += ['--seal-file', path]
    for a in kw['attestations']:
        argv += ['--attest'] + list(a)
    return argv


def shape(r):
    col = v3.column(r)
    tags = [col if col != 'complete' else 'complete-' + r['kind']]
    if len(r['landing']['reconciliations']) > 1:
        tags.append('multi-reconciliation')
    return tags


def commit_receipt(sc, lam, rid, r, seal_bytes, label):
    """A single-parent child of lam carrying `r` at its receipt path (and the seal record)."""
    files = dict(sc.files[sc.label_of[lam]])
    files[('verification/receipts/%s.json' % rid).encode()] = ('100644', dump(r).encode('utf-8'))
    if seal_bytes is not None:
        files[v3.seal_record_path(rid).encode()] = ('100644', seal_bytes)
    tree = sc._tree(files)
    oid = sc.git(['commit-tree', tree, '-m', label, '-p', lam], env=v3.COMMIT_ENV).decode().strip()
    sc.labels[label] = oid
    sc.files[label] = files
    sc.label_of[oid] = label
    return oid


# One corruption per field class; each must turn a holding receipt commit into a failing one. `x`
# carries the receipt's own D and F and an all-zero object id.
MUTATIONS = (
    ('identity: d', lambda r, x: r.update(d=x['f'])),
    ('identity: f', lambda r, x: r.update(f=x['d'])),
    ('control plane: a blob', lambda r, x: r['control_plane_blobs'][0].update(blob=x['zero'])),
    ('control plane: governed digest', lambda r, x: r.update(governed_paths_digest='0' * 64)),
    ('execution: tree_e', lambda r, x: 'tree_e' in r and r.update(tree_e=x['zero'])),
    ('execution: delta digest',
     lambda r, x: 'e' in r and r.update(execution_delta_digest='0' * 64)),
    ('landing: base', lambda r, x: r['landing'].update(base=x['f'])),
    ('landing: delta digest', lambda r, x: r['landing'].update(delta_digest='0' * 64)),
    ('landing: reconciliations', lambda r, x: r['landing'].update(
        reconciliations=r['landing']['reconciliations'][1:] or [x['f']])),
    ('seal: blob', lambda r, x: 'seal' in r and r['seal']['records'][0].update(blob=x['zero'])),
    ('attestation: subject commit', lambda r, x: r['attestations'][0].update(commit=x['d'])),
    ('attestation: F designation missing', lambda r, x: r.update(attestations=[
        a for a in r['attestations'] if (a['subject'], a['kind']) != ('F', 'owner-designation')])),
    ('schema: version', lambda r, x: r.update(version=2)),
)


def self_test(corpus=v3.DEFAULT_CORPUS):
    ok = True
    shapes = {}
    rebuilt = 0
    mutated = {}
    names = sorted(n for n in os.listdir(corpus) if n.endswith('.json'))
    for name in names:
        vec = json.load(open(os.path.join(corpus, name), encoding='utf-8'))
        if vec.get('kind') != 'repo':
            continue
        with tempfile.TemporaryDirectory() as wd:
            sc = v3.Scratch(wd)
            sc.label_of = {}
            for step in vec['steps']:
                if 'commit' in step:
                    base = step.get('from', step['parents'][0] if step.get('parents') else None)
                    sets = {p.encode('utf-8'): v3.content(s, sc)
                            for p, s in step.get('set', {}).items()}
                    dels = [p.encode('utf-8') for p in step.get('del', [])]
                    oid = sc.commit(step['commit'], step.get('parents', []), base, sets, dels)
                    sc.label_of[oid] = step['commit']
                    continue
                if 'ref' in step or 'config' in step or 'write' in step:
                    break  # host-state vectors carry no receipt to rebuild
                if step.get('check') != 'verify-round' or step['expect'].get('verdict') != 'HOLDS':
                    continue
                repo = v3.Repo(wd)
                q = sc.labels[step['args'][0]]
                if v3.verify_round(repo, q)[0] != 'HOLDS':
                    continue
                lam = repo.parents(q)[0]
                rpath = [x[1] for x in repo.delta(lam, q)
                         if x[1].startswith(b'verification/receipts/')][0]
                committed = json.loads(repo.blob(repo.state(q, rpath)[1]).decode('utf-8'))
                kw = inputs_of(repo, committed, q)
                try:
                    r = build(repo, **kw)
                except (BuildError, v3.Refused, v3.Undecidable) as exc:
                    print('FAIL  %s: the builder refused (%s)' % (name, exc))
                    ok = False
                    continue
                if r != committed:
                    diff = sorted(k for k in set(r) | set(committed)
                                  if r.get(k) != committed.get(k))
                    print('FAIL  %s: the rebuilt receipt differs in %s' % (name, ', '.join(diff)))
                    ok = False
                    continue
                q2 = commit_receipt(sc, lam, r['round'], r, kw.get('seal_bytes'), 'rebuilt-' + name)
                verdict, codes, _ = v3.verify_round(repo, q2)
                if verdict != 'HOLDS':
                    print('FAIL  %s: the rebuilt receipt commit %s %s'
                          % (name, verdict, ','.join(codes)))
                    ok = False
                    continue
                argv = to_argv(kw, wd)
                if parse(argv)[0] != {k: v for k, v in kw.items() if v is not None}:
                    print('FAIL  %s: the command line does not carry the same inputs' % name)
                    ok = False
                    continue
                rebuilt += 1
                for t in shape(r):
                    shapes.setdefault(t, []).append(name[:-5])
                x = {'d': r['d'], 'f': r['f'], 'zero': '0' * len(r['f'])}
                for label, mut in MUTATIONS:
                    m = copy.deepcopy(r)
                    mut(m, x)
                    if m == r:
                        continue
                    qm = commit_receipt(sc, lam, r['round'], m, kw.get('seal_bytes'),
                                        'mutated-%s-%s' % (name, label))
                    verdict, codes, _ = v3.verify_round(repo, qm)
                    mutated.setdefault(label, [0, 0])
                    mutated[label][0] += 1
                    if verdict == 'FAILS':
                        mutated[label][1] += 1
                    else:
                        print('FAIL  %s: corruption "%s" gave %s' % (name, label, verdict))
                        ok = False
    print('rebuilt  %d receipt commit(s), each identical to the committed receipt and holding'
          % rebuilt)
    for t in ('complete-non-sealing', 'complete-sealing', 'halted-exec', 'halted-none',
              'multi-reconciliation'):
        got = shapes.get(t, [])
        print('shape    %-22s %d vector(s)' % (t, len(got)))
        ok &= bool(got)
    for label, _ in MUTATIONS:
        n, failed = mutated.get(label, [0, 0])
        print('corrupt  %-36s %d/%d failing' % (label, failed, n))
        ok &= n > 0 and failed == n
    print('v3_receipt: self-test %s' % ('OK' if ok else 'FAILED'))
    return 0 if ok else 1


def parse(argv):
    kw = {'reconciliations': [], 'attestations': [], 'resolved': [], 'candidates': []}
    out = None
    i = 0
    single = {'--status': 'status', '--d': 'd', '--f': 'f', '--e': 'e',
              '--withdrawal': 'withdrawal'}
    while i < len(argv):
        a = argv[i]
        if a in single and i + 1 < len(argv) and single[a] not in kw:
            kw[single[a]] = argv[i + 1]
            i += 2
        elif a == '--reconciliation' and i + 1 < len(argv):
            kw['reconciliations'].append(argv[i + 1])
            i += 2
        elif a == '--resolved' and i + 1 < len(argv):
            kw['resolved'].append(argv[i + 1])
            i += 2
        elif a == '--candidate' and i + 2 < len(argv):
            kw['candidates'].append((argv[i + 1], argv[i + 2]))
            i += 3
        elif a == '--attest' and i + 3 < len(argv):
            kw['attestations'].append(tuple(argv[i + 1:i + 4]))
            i += 4
        elif a == '--seal-file' and i + 1 < len(argv) and 'seal_bytes' not in kw:
            with open(argv[i + 1], 'rb') as fh:
                kw['seal_bytes'] = fh.read()
            i += 2
        elif a == '--out' and i + 1 < len(argv) and out is None:
            out = argv[i + 1]
            i += 2
        else:
            return None, None
    if not {'status', 'd', 'f'} <= set(kw):
        return None, None
    return kw, out


def main(argv):
    if argv == ['--self-test']:
        return self_test()
    kw, out = parse(argv)
    if kw is None:
        print(USAGE)
        return 2
    try:
        r = build(v3.Repo(os.getcwd()), **kw)
    except v3.Refused as rf:
        print('v3_receipt: refused (%s)' % rf.code)
        return 2
    except (BuildError, v3.Undecidable) as exc:
        print('v3_receipt: not built (%s)' % exc)
        return 1
    if out is None:
        sys.stdout.write(dump(r))
    else:
        with open(out, 'w', encoding='utf-8') as fh:
            fh.write(dump(r))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
```

## The rule and the preamble, FROZEN as text

At stage 2 the execution appends the text below to `AGENTS.md` as it stands at `B`, byte for byte
after its last byte, and changes nothing else in the file:

```text

---

## §A.39 Provisional native V3 rounds

§A.37 remains the default lifecycle for every round, and it governs the round that adopted this
rule, `V3-9`. A round whose preregistration the owner authorizes as a **provisional V3 pilot** runs
instead under the native lifecycle of `verification/infrastructure/v3/architecture.md`, which is
operative for such rounds and no others:

1. **One pull request from `D`.** The round's control plane — its preregistration, carrying one
   `v3-round` block and one `v3-governed-paths` block, and any amendments — is drafted on a single
   pull request from the drafting snapshot `D`. Drafting ends when the owner designates the exact
   commit `F`. No commit after `F` changes the control plane.
2. **Linear execution to `E`.** The execution commits follow `F` linearly. The owner designates the
   certified execution head `E`.
3. **Reconciliation, if needed.** Later history enters the round only through reconciliation
   merges after `E`: first parent a later base on whose first-parent chain `D` lies, second parent
   `E` or the previous receipt commit. The last reconciliation is `Λ`.
4. **The receipt.** `tools/v3_receipt.py` builds the receipt from the round's exact object ids and
   the attestation records the host holds. `Q` is a single-parent child of `Λ` that adds only the
   receipt and, for a sealing round, its seal record. `tools/v3_verifier.py --verify-round Q` must
   print `VERDICT  HOLDS` before the pull request lands.
5. **Landing.** The pull request lands through ordinary review and merge. How it lands is not part
   of the round's validity.

**The check runs at `F` and `E`.** A `check-run` attestation names the commit it was run on. Before
`F` is designated, the pilot's branch is held at exactly `F` and the workflow is dispatched on it
(`workflow_dispatch`); the run whose `head_sha` is `F`, with every job green, is `F`'s `check-run`
attestation, and only then is `F` designated and the branch moved on. `E` is attested the same way
before it is designated. A pull-request run tests a synthetic merge, not `F` or `E`, and is not
recorded as their attestation. These are host attestations, which the receipt records and no
predicate of `tools/v3_verifier.py` reads.

**A halted pilot.** A pilot that halts after `F` instead of reaching a designated `E` follows the
specification's `S12`: it appends the withdrawal commit `W` when execution commits exist, or,
when none exist, the single-parent child of `F` that changes only record paths and carries the
result note; it reconciles as `S9` requires; it builds a halted receipt with
`tools/v3_receipt.py`, which carries `F`'s owner-designation and `check-run` attestations and none
for `E`; `--verify-round Q` must hold; and it lands through the same ordinary pull request.

A provisional pilot carries no guard clause, seal manifest record, round certificate or
`control-plane-preconditions` block: its receipt, `verification/receipts/<round>.json`, is its
protocol record. It leaves `V1` and `V2` authority unchanged. The guard and the release gate run on
its pull request as on any other, and they remain the repository's authoritative checks until a
later round makes V3 the default.
```

In the same commit the sentence below, which occurs exactly once in
`verification/infrastructure/v3/architecture.md` at `B`, is replaced by the second, and nothing else
in the file changes.

The sentence at `B`:

```text
identifier. The specification is not operative: until a later round activates it, every round is
governed by `AGENTS.md` §A.37, and no `V1` or `V2` state is changed or migrated by it.
```

The sentence at `E`:

```text
identifier. The specification is operative only for a round the owner authorizes as a provisional
V3 pilot under `AGENTS.md` §A.39. Every other round is governed by `AGENTS.md` §A.37 until a later
round makes V3 the default, and no `V1` or `V2` state is changed or migrated by it.
```

## The controls, FROZEN

- **`C1` — the builder's self-test.** At stage 1, `tools/v3_receipt.py --self-test` exits 0 and its
  last line is `v3_receipt: self-test OK`, with the counts `F5` records.
- **`C2` — own rule.** At stage 1, each of six scratch copies of the builder with one derivation
  wrong runs its self-test to exit 1, ending `v3_receipt: self-test FAILED`, with at least one
  `FAIL` line: the execution delta taken from `D` instead of `F`; the landing base taken from the
  second parent; the control-plane blobs in reverse order; no `withdrawal` reason when there are no
  execution commits; the seal blob hashed without git's object header; every attestation's commit
  taken from `F`.
- **`C3` — the command line.** At stage 1, `--status complete --d HEAD --f HEAD` prints
  `v3_receipt: refused (input:not-an-object-id)` and exits 2, and no argument prints the usage line
  and exits 2.
- **`C4` — the verifier untouched.** At every stage's commit, `tools/v3_verifier.py` has its `D`
  blob, `--corpus` reports `CORPUS  135 vector(s), exact and as expected`, and `--self-test`
  passes.
- **`C5` — the texts.** At stage 2, `AGENTS.md` is its `B` bytes followed by the frozen text
  exactly, carrying one `## §A.39 ` heading and no `§A.38`; `architecture.md` differs from its `B`
  bytes by the frozen sentence alone and no longer contains `is not operative`.

A control whose scratch copy fails for a reason other than the rule it tests is void, and its target
stops.

## The targets, FROZEN

| target | passing outcome | stop outcome |
|---|---|---|
| `V39-0` | `BASE-HOLDS` — the execution branch starts at `B`; this file's blob at `B` is the frozen one; every `B` and `D->B` row and frozen blob holds at `B` | `BASE-BROKEN` |
| `V39-1` | `BUILDER-INSTALLED` — stage 1 adds `tools/v3_receipt.py` and nothing else; `C1`–`C4` hold | `BUILDER-WRONG` |
| `V39-2` | `PILOT-RULE-INSTALLED` — stage 2 changes `AGENTS.md` and `architecture.md` as frozen and nothing else; `C4`, `C5` hold | `RULE-WRONG` |
| `V39-3` | `AUTHORITY-UNCHANGED` — `.github/workflows/verify.yml`, `tools/release_gate.py`, `tools/certificate_verifier.py`, the guard, `tools/v3_verifier.py` and the corpus have their `B` blobs at `E`; neither `verification/receipts/` nor `verification/v3-seals/` exists; the exact-head run on `E` gives the guard 105 PASS and 0 FAIL with `D`'s verdict map, the release gate 19 of 19 with `V2` authoritative OK, and the shadow job its self-test and the 135-vector corpus | `AUTHORITY-CHANGED` — fails the round |
| `V39-4` | `SCOPE-HELD` — `git diff --no-renames --name-status B E` is exactly the mutation budget | `SCOPE-EXCEEDED` |

## Predictions, with strength

| target | predicted outcome | strength | reason |
|---|---|---|---|
| `V39-0` | `BASE-HOLDS` | strong | only this file lies between `D` and `B` |
| `V39-1` | `BUILDER-INSTALLED`; builder blob `e08d15f6e301bec4d32f9dab34b5c7b40fb48d1f` | strong | measured at `D` (`F5`) |
| `V39-2` | `PILOT-RULE-INSTALLED`; `AGENTS.md` blob `864494c1a9696a3b08330da64cf9d265d6d8b92f`, `architecture.md` blob `f699471b34d4f332c557f6b5452c952db49a0306` | strong | measured at `D` (`F5`) |
| `V39-3` | `AUTHORITY-UNCHANGED` | strong | no job, gate, guard, verifier or corpus file is written, and the guard's reads of `AGENTS.md` are untouched (`F4`) |
| `V39-4` | `SCOPE-HELD` | strong | the budget is fixed here |

**Status rule.** The round is COMPLETE iff every target reaches its passing outcome. It is HALTED at
the first stop outcome, and the targets not reached are recorded as such.

## The order is part of the contract

| stage | targets | commit | checkpoint |
|---|---|---|---|
| 0 | `V39-0` | none | branch from `B`; blob check; rows at `B` |
| 1 | `V39-1` | one: `tools/v3_receipt.py` | `C1`–`C4` |
| 2 | `V39-2` | one: `AGENTS.md` and `architecture.md` | `C4`, `C5` |
| 3 | `V39-3`, `V39-4` | one: the result note; its commit is `E` | the closing checks, then the exact-head run |

Stage commits are pushed without waiting for continuous integration on them; the certification of
record is the exact-head run on `E`.

## The mutation budget

- **Added:** `tools/v3_receipt.py`;
  `verification/infrastructure/round-v3-9-operationalization/result.md`.
- **Modified:** `AGENTS.md` (the appended `§A.39`); `verification/infrastructure/v3/architecture.md`
  (the one frozen sentence).
- **Never written:** every other file under `tools/`, `.github/`, the guard and everything under
  `verification/lean/` and `verification/lean-mathlib/`,
  `verification/infrastructure/v3/conformance/`, `verification/seals/`,
  `verification/certificates/`, `verification/programmes/`, `verification/audits/`,
  `verification/ROADMAP.md`, `verification/README.md`, any other round's directory, `papers/` and
  `book/`. Neither `verification/receipts/` nor `verification/v3-seals/` is
  created.

## The result note

`result.md` records: each target's outcome against its prediction; the chronology from `B` to `E`;
each stage's blobs against their predictions, with the diff of every divergence; the outputs of `C1`
to `C5`, with the SHA-256 of each scratch script, none of which is landed; and every discrepancy.
The exact-head run on `E` is identified by the `E` certification record, since the note is part of
`E`.

## What no outcome of this round licenses

1. Any sentence that V3 is the default protocol, or that a V3 receipt is an authoritative record.
2. Any wiring of `tools/v3_receipt.py` or `tools/v3_verifier.py` into a gate or required check.
3. Any change to `V1` or `V2` state, to `§A.37`, or to another round's records.
4. Running a pilot: `§A.39` admits one only when the owner authorizes it in that round's own
   preregistration.

## Hazards

- **`H1` — one author.** The builder, the rule text and the controls have one author; the owner's
  review of the freeze and of the `E` record is the check on a shared misreading.
- **`H2` — shared functions.** The builder derives each digest with the verifier's own function, so
  a defect in that function would pass the self-test's reproduction. The digest functions are held
  independently by the corpus's literal-digest vectors (`s8-landed-*`, `s4-canonical-ex-*`), which
  this round does not touch.
- **`H3` — the guard reads `AGENTS.md`.** `F4` measured which phrases it reads; the exact-head run
  on `E` is the check that appending `§A.39` disturbs none.

## Files

### Files this round reads AND writes

`AGENTS.md` (the appended section); `verification/infrastructure/v3/architecture.md` (the one
sentence); `tools/v3_receipt.py` (new).

### Files this round reads and MUST NOT write

`tools/v3_verifier.py` and `verification/infrastructure/v3/conformance/`, which the builder and its
self-test read; `.github/workflows/verify.yml`, `tools/release_gate.py`,
`tools/certificate_verifier.py`, `tools/control_plane_base_check.py`, `tools/control_plane_lint.py`,
the guard, and the other `V3` round directories.

## Preconditions

Row `db3-only-this-file` requires that nothing but this file lie between `D` and `B`; with the
frozen blobs it fixes the objects the edits are applied to.

```control-plane-preconditions
d: 311f06ea174501587478024a09140297b56e089a
frozen-blob: AGENTS.md a9687b39c69973d35a2ff81c257687071fd35eca
frozen-blob: verification/infrastructure/v3/architecture.md db36dbd1ee4f779eff13525ffd3dc11d9041ab36
frozen-blob: tools/v3_verifier.py ccfbe813790e4855f408462449327f32e59d545b
# row 1: name freedom and absences, drafting-time facts
{"id": "d1-round-free", "scope": "D", "check": "git grep -l -F -e 'V3-9' -e 'v3-9' -e 'round-v3-9' -e 'V39-' -e 'v3_receipt' -e 'operationalization' $D", "expect": "empty"}
{"id": "d1-section-free", "scope": "D", "check": "git show $D:AGENTS.md | grep -F -e '§A.38' -e '§A.39'", "expect": "empty"}
{"id": "d1-builder-absent", "scope": "D", "check": "git ls-tree --name-only $D tools/v3_receipt.py", "expect": "empty"}
{"id": "d1-receipts-absent", "scope": "D", "check": "git ls-tree -d --name-only $D verification/receipts verification/v3-seals", "expect": "empty"}
# row 2: the vector inventory at D
{"id": "d2-corpus-135", "scope": "D", "check": "test $(git ls-tree --name-only $D verification/infrastructure/v3/conformance/ | wc -l) -eq 135", "expect": "exit0"}
# row 3: provenance, D to B
{"id": "db3-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
{"id": "db3-only-this-file", "scope": "D->B", "check": "git diff --name-only $D $REF | grep -v -x -F 'verification/infrastructure/round-v3-9-operationalization/preregistration.md'", "expect": "empty"}
{"id": "db3-v3-unchanged", "scope": "D->B", "check": "git diff --quiet $D $REF -- verification/infrastructure/v3/ tools/v3_verifier.py AGENTS.md", "expect": "exit0"}
# row 4: no execution object at B
{"id": "b4-round-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-v3-9-operationalization | grep -v -x -F 'verification/infrastructure/round-v3-9-operationalization/preregistration.md'", "expect": "empty"}
{"id": "b4-builder-absent", "scope": "B", "check": "git ls-tree --name-only $REF tools/v3_receipt.py", "expect": "empty"}
{"id": "b4-agents-no-section", "scope": "B", "check": "git show $REF:AGENTS.md | grep -F -e '§A.39'", "expect": "empty"}
{"id": "b4-no-receipts", "scope": "B", "check": "git ls-tree -d --name-only $REF verification/receipts verification/v3-seals", "expect": "empty"}
# row 5: this control plane at its path
{"id": "b5-present", "scope": "B", "check": "git cat-file -e $REF:verification/infrastructure/round-v3-9-operationalization/preregistration.md", "expect": "exit0"}
```

## The landing shape

Non-sealing under §A.37, `E` → `L` on the execution pull request, no `P`. `L`'s first parent is
current green `main`, its second parent exactly `E`; conflicts, if any, are resolved in `L` by
merits. Full continuous integration passes on `L` before it merges, and the push run on `main` is
green before any later round's landing is built.

## Execution discipline

The execution branch is created from `B` and nothing else, after `B`'s push run is green including
the control-plane base check in mode `B`. Its first act is the blob check of this file at `B`. It
never absorbs later `main` before `E`; no rebase, amend or force-push. The execution pull request
may be opened after stage 1, held from merging. A stop outcome halts the round; the halt is recorded
in a result note with the outcomes reached, and nothing else of the execution lands. `V3-9` carries
no guard clause, manifest record or round certificate.

## Points at which this freeze chose a reading, recorded rather than resolved

- **`R1` — a separate builder that reuses the verifier's functions.** The builder imports
  `tools/v3_verifier.py` for `S7`, `S8`, the control plane at `F` and `S4`'s standalone check,
  rather than restating them, so the two tools cannot drift apart on a digest; the verifier is not
  changed and does not import the builder. The declined options are a `--build-receipt` entry point
  in the verifier, which would put a builder inside the tool that judges its output, and an
  independent reimplementation, which would duplicate the specification's algorithms.
- **`R2` — the corpus is the builder's test data.** The self-test's evidence is that the builder
  reproduces the receipts the corpus's vectors commit and that the verifier rejects each corrupted
  field class; it adds no vector. The corpus is read, not written.
- **`R3` — `§A.39`, not `§A.38`** (`F2`). The owner's direction named a new `§A.38`; the number is
  already `GH-1`'s, and `V3-1` pointed at `§A.39` for this rule.
- **`R4` — `§A.37` unchanged.** `§A.39` is appended; nothing in `§A.37` is amended, and `§A.37`
  remains the default lifecycle and governs `V3-9`.
- **`R5` — the preamble alone.** Only the sentence that made the specification wholly inoperative
  changes; `S13` and every settlement stand.
- **`R6` — no continuous-integration step for the builder.** Its self-test runs in this round's
  controls and in the pilot that uses it; wiring it into a job is `V3-11`'s, with the rest of V3's
  gate wiring.
- **`R7` — no `V2` artifact for a pilot** (`F4`). A pilot's receipt is its protocol record; the
  guard and the release gate remain the safety net without a parallel certificate.
- **`R8` — no guard clause, certificate or attestation**, as for `V3-1` to `V3-8`.
- **`R9` — attestations name their subject.** A pull-request run tests a synthetic merge, so
  `§A.39` makes each `check-run` attestation a `workflow_dispatch` run whose `head_sha` is exactly
  `F` or `E`, taken while the branch is held there. This is host practice that keeps the
  attestation's description of its subject true; no verifier predicate reads it.
- **`R10` — the halt path.** `§A.39` closes a pilot that stops after `F` through `S12`: `W`, or
  the record commit when no execution commits exist, reconciliation, a halted receipt with `F`'s
  attestations alone, and `--verify-round Q` holding. The builder and the verifier already carry
  both halted shapes, so nothing but the rule's text is added for it.
