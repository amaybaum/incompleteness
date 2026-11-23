"""Delegation class adapter rerun-equal/1 (class sc42): native re-execution in a disposable clone at X.

Locally no clone is made (resource discipline); the re-execution result is evidence named by the contract.
"""
import json

INTERFACE = 'delegation'
NAME = 'rerun-equal'
VERSION = 1


def verify(repo, roles, cls, evidence, ledger):
    out = []
    X, H = roles.get('candidate'), roles.get('scientific_base')
    p = cls['paths'][0]
    data = repo.read(X, p)
    if data is None or cls['params']['must_contain'].encode() not in data:
        out.append(('fail', '%s does not name its base commit' % p))
    ctl = cls['params'].get('controls_path')
    if ctl and repo.blob_id(X, ctl) != repo.blob_id(H, ctl):
        out.append(('fail', 'controls file differs from H'))
    for name, ev in sorted(evidence.items()):
        if ev is None:
            out.append(('missing', 'no re-execution result %s' % name))
            continue
        r = json.loads(ev.decode('utf-8'))
        if r.get('candidate') != X or r.get('verbose_exit') != 0 or r.get('verbose_equal') is not True or \
                r.get('self_test_equal') is not True:
            out.append(('fail', '%s: re-execution does not reproduce the file' % name))
    return out
