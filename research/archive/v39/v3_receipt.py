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
