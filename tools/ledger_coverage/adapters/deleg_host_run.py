"""Delegation class adapter host-run, interface 2 (class ci): the host's run and job records for the exact-head
run on the tree, read by the tool from the host's API (never a supplied file)."""
INTERFACE = 'delegation'
NAME = 'host-run'
VERSION = 2


def verify(repo, roles, cls, env, ledger):
    X = roles.get('candidate')
    if env is None or not env.available():
        return [('missing', 'host run records cannot be read here (local run)')]
    runs = env.host_runs(X)
    if not runs:
        return [('missing', 'no host run on the tree')]
    out = []
    jobs = {}
    for r in runs:
        if r.get('head_sha') != X:
            out.append(('fail', 'a host record names another head_sha'))
        for j in r.get('jobs', []):
            jobs[j.get('name')] = j.get('conclusion')
    for need in cls['params']['jobs']:
        if jobs.get(need) != 'success':
            out.append(('fail', 'job %s did not conclude success' % need))
    return out
