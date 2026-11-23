"""Delegation class adapter host-run/1 (class ci): host run and job records for the exact-head run on X."""
import json

INTERFACE = 'delegation'
NAME = 'host-run'
VERSION = 1


def verify(repo, roles, cls, evidence, ledger):
    out = []
    for name, ev in sorted(evidence.items()):
        if ev is None:
            out.append(('missing', 'no host run record %s' % name))
            continue
        r = json.loads(ev.decode('utf-8'))
        if r.get('head_sha') != roles.get('candidate'):
            out.append(('fail', '%s: head_sha is not X' % name))
        jobs = {j.get('name'): j.get('conclusion') for j in r.get('jobs', [])}
        for need in cls['params']['jobs']:
            if jobs.get(need) != 'success':
                out.append(('fail', '%s: job %s did not conclude success' % (name, need)))
    return out
