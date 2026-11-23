"""Delegation class adapter preserve-check-v1 (classes tex and pdf)."""
import json
import re

INTERFACE = 'delegation'
NAME = 'preserve-check-v1'
VERSION = 1
RESULT_SCHEMA = 'a1exit-checker-result-v1'
CHECKER = 'preserve_check.py'
HEX40 = re.compile(r'^[0-9a-f]{40}$')


def verify(repo, roles, cls, evidence, ledger):
    out = []
    X, H, F = roles.get('candidate'), roles.get('scientific_base'), roles.get('freeze')
    if cls['id'] == 'tex':
        for tex, md in sorted(cls['params']['sources'].items()):
            data = repo.read(X, tex)
            src = repo.read(X, md)
            if data is None or src is None:
                out.append(('fail', '%s or its source missing at X' % tex))
                continue
            import hashlib
            last = data.rstrip(b'\n').rsplit(b'\n', 1)[-1].decode('utf-8', 'replace')
            if last != '%% source-sha256: %s' % hashlib.sha256(src).hexdigest():
                out.append(('fail', '%s: source stamp does not match X\'s source' % tex))
    elif cls['id'] == 'pdf':
        for p in cls['paths']:
            if repo.blob_id(X, p) == repo.blob_id(H, p):
                out.append(('fail', '%s: PDF unchanged from H' % p))
    for name, data in sorted(evidence.items()):
        if data is None:
            out.append(('missing', 'no result file %s' % name))
            continue
        try:
            r = json.loads(data.decode('utf-8'))
        except ValueError:
            out.append(('fail', '%s is not JSON' % name))
            continue
        bad = []
        if r.get('schema') != RESULT_SCHEMA:
            bad.append('schema')
        if r.get('checker') != CHECKER:
            bad.append('checker')
        if r.get('plan') != F:
            bad.append('plan')
        if r.get('ledger_base', r.get('base')) != H or r.get('base', H) != H:
            bad.append('base')
        if r.get('ledger_sha256') != roles.get('ledger_sha256'):
            bad.append('ledger_sha256')
        cand = r.get('candidate')
        if not isinstance(cand, str) or not HEX40.match(cand) or cand != X:
            bad.append('candidate')
        if r.get('exit', r.get('exit_status')) != 0:
            bad.append('exit')
        if r.get('verdict') != 'pass':
            bad.append('verdict')
        checks = {c.get('name'): c for c in r.get('checks', []) if isinstance(c, dict)}
        for need in cls['params'].get('required_checks', []):
            c = checks.get(need)
            if c is None or c.get('status') != 'pass' or c.get('discrepancies'):
                bad.append('check %s' % need)
        if r.get('checker_blob_sha256') != cls['params'].get('checker_sha256'):
            bad.append('checker blob')
        if bad:
            out.append(('fail', '%s: %s' % (name, ', '.join(bad))))
    return out
