"""Delegation class adapter rerun-equal, interface 2 (class sc42; sec. 7.3).

In the clone at the tree, the checker from F's blob is run with --verbose and --self-test, each plainly and with
-O; each must exit 0 and its output must be byte-identical to the committed result file and controls file; the
controls file must equal H's, and the result file must name the base commit. A supplied re-execution result is
never read.
"""
import sys

INTERFACE = 'delegation'
NAME = 'rerun-equal'
VERSION = 2


def verify(repo, roles, cls, env, ledger):
    out = []
    X, H = roles.get('candidate'), roles.get('scientific_base')
    tree = roles.get('tree_role', 'X')
    p = cls['params']
    path = cls['paths'][0]
    data = repo.read(X, path)
    if data is None or p['must_contain'].encode() not in data:
        out.append(('fail', '%s does not name its base commit' % path))
    ctl_path = p.get('controls_path')
    ctl = repo.read(X, ctl_path) if ctl_path else None
    if ctl_path and repo.blob_id(X, ctl_path) != repo.blob_id(H, ctl_path):
        out.append(('fail', 'controls file differs from H'))
    if env is None or not env.available():
        return out + [('missing', 'the re-execution cannot run here (no disposable clone: local run)')]
    clone = env.clone(X)
    if env.replay is None:
        f, sha = env.checker(p['checker_path'])
    else:
        f, sha = None, None
    for label, flag, want, what in (('verbose', '--verbose', data, 'result file'),
                                    ('self-test', '--self-test', ctl, 'controls file')):
        for opt in ([], ['-O']):
            lab = '%s%s' % (label, '-O' if opt else '')
            run = env.run('sc42-' + lab, tree, [sys.executable, '-I', '-B'] + opt + [f, flag], clone, sha)
            if run is None:
                out.append(('missing', 'no recorded run %s' % lab))
                continue
            ok = run['exit'] == 0 and want is not None and run['stdout'] == want
            env.derive(cls['id'], tree, '%s output equals the %s' % (lab, what), ok)
            if not ok:
                out.append(('fail', 'the re-execution (%s) does not reproduce the %s' % (lab, what)))
    return out
