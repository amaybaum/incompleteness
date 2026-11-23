"""Delegation class adapter fingerprint-regen/1 (class coverage-ledger): the file equals the scientific base plus
its splices except the fingerprint values of the named ids; each id occurs exactly once; each value equals the
census output, which is evidence named by the contract."""
import json
import re

INTERFACE = 'delegation'
NAME = 'fingerprint-regen'
VERSION = 1


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


def verify(repo, roles, cls, evidence, ledger):
    out = []
    X, H = roles.get('candidate'), roles.get('scientific_base')
    path = cls['paths'][0]
    ids = cls['params']['stale_ids']
    exp = _apply(repo.read(H, path) or b'', [s for s in ledger['splices'] if s['file'] == path]).decode('utf-8')
    x = (repo.read(X, path) or b'').decode('utf-8')
    for i in ids:
        if x.count('"id": "%s"' % i) != 1:
            out.append(('fail', 'id %s does not occur exactly once at X' % i))
    if _blank(exp, ids) != _blank(x, ids):
        out.append(('fail', '%s differs from the base plus its splices outside the named fingerprint values' % path))
    xv = _values(x, ids)
    for name, ev in sorted(evidence.items()):
        if ev is None:
            out.append(('missing', 'no census output %s' % name))
            continue
        census = json.loads(ev.decode('utf-8'))
        entries = census.get('entries', census) if isinstance(census, dict) else census
        got = {e.get('id'): e.get('fingerprint') for e in entries} if isinstance(entries, list) else \
            census.get('fingerprints', {})
        for i in ids:
            if xv.get(i) is None or got.get(i) != xv[i][2]:
                out.append(('fail', 'fingerprint of %s differs from the census output' % i))
    return out
