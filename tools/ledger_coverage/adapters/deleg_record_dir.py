"""Delegation class adapter record-dir/1: the plan's record directory equals F's blobs; additions only under
execution/."""
INTERFACE = 'delegation'
NAME = 'record-dir'
VERSION = 1


def verify(repo, roles, cls, evidence, ledger):
    out = []
    F, X = roles.get('freeze'), roles.get('candidate')
    for d in cls['paths']:
        fp = {p: b for p, b in repo.paths(F).items() if p.startswith(d)} if F else {}
        xp = {p: b for p, b in repo.paths(X).items() if p.startswith(d)}
        if not F:
            out.append(('missing', 'no freeze commit F given'))
            continue
        for p, b in fp.items():
            if xp.get(p) != b:
                out.append(('fail', '%s differs from F' % p))
        for p in xp:
            if p not in fp and not p.startswith(d + 'execution/'):
                out.append(('fail', '%s added outside execution/' % p))
    return out
