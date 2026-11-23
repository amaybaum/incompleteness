"""Delegation class adapter fingerprint-regen, interface 2 (class coverage-ledger; sec. 7.3): the file equals the
scientific base plus its splices except the fingerprint values of the named ids; each id occurs exactly once;
each value equals the census output that the tool itself produces in the clone at the tree (the tree's census
blob, exit 0). A supplied census file is never read."""
import json
import re
import sys

INTERFACE = 'delegation'
NAME = 'fingerprint-regen'
VERSION = 2


def _apply(data, splices):
    out, pos = [], 0
    for sp in sorted(splices, key=lambda x: (x['start'], x['end'])):
        out.append(data[pos:sp['start']])
        out.append(sp['new_bytes'])
        pos = sp['end']
    out.append(data[pos:])
    return b''.join(out)


def _values(text, ids):
    out = {}
    for i in ids:
        m = re.search(r'"id": "%s",.*?"fingerprint": "([0-9a-f]*)"' % re.escape(i), text, re.S)
        out[i] = None if m is None else (m.start(1), m.end(1), m.group(1))
    return out


def _blank(text, ids):
    vals = sorted((v for v in _values(text, ids).values() if v), reverse=True)
    for a, b, _ in vals:
        text = text[:a] + text[b:]
    return text


def census_values(data):
    census = json.loads(data.decode('utf-8'))
    entries = census.get('entries', census) if isinstance(census, dict) else census
    if isinstance(entries, list):
        return {e.get('id'): e.get('fingerprint') for e in entries if isinstance(e, dict)}
    return census.get('fingerprints', {}) if isinstance(census, dict) else {}


def verify(repo, roles, cls, env, ledger):
    out = []
    X, H = roles.get('candidate'), roles.get('scientific_base')
    tree = roles.get('tree_role', 'X')
    path = cls['paths'][0]
    ids = cls['params']['stale_ids']
    exp = _apply(repo.read(H, path) or b'', [s for s in ledger['splices'] if s['file'] == path]).decode('utf-8')
    x = (repo.read(X, path) or b'').decode('utf-8')
    for i in ids:
        if x.count('"id": "%s"' % i) != 1:
            out.append(('fail', 'id %s does not occur exactly once at the tree' % i))
    if _blank(exp, ids) != _blank(x, ids):
        out.append(('fail', '%s differs from the base plus its splices outside the named fingerprint values' % path))
    if env is None or not env.available():
        return out + [('missing', 'the census cannot run here (no disposable clone: local run)')]
    clone = env.clone(X)
    census = cls['params'].get('census_path', 'tools/proof_census.py')
    sha = None
    if env.replay is None:
        import hashlib
        sha = hashlib.sha256(repo.read(X, census) or b'').hexdigest()
    run = env.run('census', tree, [sys.executable, '-I', '-B', census, '--json'], clone, sha)
    if run is None:
        return out + [('missing', 'no recorded census run')]
    if run['exit'] != 0:
        return out + [('fail', 'the census exited %d' % run['exit'])]
    try:
        got = census_values(run['stdout'])
    except ValueError:
        return out + [('fail', 'the census output is not JSON')]
    xv = _values(x, ids)
    for i in ids:
        ok = xv.get(i) is not None and got.get(i) == xv[i][2]
        env.derive(cls['id'], tree, 'fingerprint of %s equals the census' % i, ok)
        if not ok:
            out.append(('fail', 'fingerprint of %s differs from the census output' % i))
    return out
