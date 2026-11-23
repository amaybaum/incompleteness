"""Delegation class adapter preserve-check-v1, interface 2 (classes tex and pdf; sec. 7.2, 7.3).

tex: the tool runs the plan checker from F's blob in the clone at the tree (`--commit TREE --plan F
--result-json OUT`), reads only the result file it produced, validates it, and re-derives the source stamps and
the path set itself. pdf: the host's run and job records for the exact-head run on the tree, the comparison
result naming the tree's commit and tree ids, and the uploaded artifact's sha256; the PDFs must differ from H.
"""
import hashlib
import json
import os
import re
import sys

INTERFACE = 'delegation'
NAME = 'preserve-check-v1'
VERSION = 2
RESULT_SCHEMA = 'a1exit-checker-result-v1'
CHECKER = 'preserve_check.py'
HEX40 = re.compile(r'^[0-9a-f]{40}$')


def validate(r, roles, cls, checker_sha, tree):
    bad = []
    X, H, F = tree, roles.get('scientific_base'), roles.get('freeze')
    if r.get('schema') != RESULT_SCHEMA:
        bad.append('schema')
    if r.get('checker') != CHECKER:
        bad.append('checker')
    if 'plan' not in r or r.get('plan') is None:
        bad.append('plan null or absent')
    elif r.get('plan') != F:
        bad.append('plan')
    if r.get('ledger_base', r.get('base')) != H or r.get('base', H) != H:
        bad.append('base')
    if r.get('ledger_sha256') != roles.get('ledger_sha256'):
        bad.append('ledger_sha256')
    cand = r.get('candidate', r.get('candidate_commit'))
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
    if r.get('checker_blob_sha256') != checker_sha:
        bad.append('checker blob')
    return bad


def stamps(repo, X, cls):
    out = []
    srcs = cls['params'].get('sources', {})
    if sorted(srcs) != sorted(cls['paths']):
        out.append(('fail', 'the path set differs from tex_sources'))
    for tex, md in sorted(srcs.items()):
        data, src = repo.read(X, tex), repo.read(X, md)
        if data is None or src is None:
            out.append(('fail', '%s or its source missing at %s' % (tex, X[:12])))
            continue
        last = data.rstrip(b'\n').rsplit(b'\n', 1)[-1].decode('utf-8', 'replace')
        if last != '%% source-sha256: %s' % hashlib.sha256(src).hexdigest():
            out.append(('fail', '%s: source stamp does not match the source' % tex))
    return out


def verify(repo, roles, cls, env, ledger):
    X, H, F = roles.get('candidate'), roles.get('scientific_base'), roles.get('freeze')
    tree = roles.get('tree_role', 'X')
    p = cls['params']
    if cls['id'] == 'tex':
        out = stamps(repo, X, cls)
        if env is not None:
            env.derive(cls['id'], tree, 'source stamps and path set', not out)
        if env is None or not env.available():
            return out + [('missing', 'the checker cannot be executed here (no disposable clone: local run)')]
        clone = env.clone(X)
        if env.replay is None:
            # a checker that locates the repository from its own file is written at its path in the clone
            f, sha = env.checker(p['checker_path'], place_in=clone if p.get('placement') == 'repo-path' else None)
        else:
            f, sha = None, p.get('checker_sha256')
        if sha != p.get('checker_sha256'):
            return out + [('fail', 'the checker blob at F differs from the contract\'s pin')]
        res_path = os.path.join(env.out, 'results', tree, 'tex-preserve-check.json') if env.replay is None else None
        if res_path:
            os.makedirs(os.path.dirname(res_path), exist_ok=True)
        run = env.run('tex', tree, [sys.executable, '-I', '-B', f, '--commit', X, '--plan', F, '--result-json',
                                    res_path], clone, sha, [res_path] if res_path else [])
        if run is None:
            return out + [('missing', 'no recorded run of the checker')]
        data = run['files'].get('tex-preserve-check.json')
        if data is None:
            return out + [('missing', 'the checker wrote no result file')]
        try:
            r = json.loads(data.decode('utf-8'))
        except ValueError:
            return out + [('fail', 'the result file is not JSON')]
        bad = validate(r, roles, cls, sha, X)
        if run['exit'] != 0:
            bad.append('exit status %d' % run['exit'])
        if bad:
            out.append(('fail', 'checker result: %s' % ', '.join(bad)))
        if not bad and stamps(repo, X, cls):
            out.append(('fail', 'the checker passed while the tool\'s own re-derivation fails'))
        return out
    # pdf
    out = []
    for path in cls['paths']:
        if repo.blob_id(X, path) == repo.blob_id(H, path):
            out.append(('fail', '%s: PDF unchanged from H' % path))
    if env is None or not env.available():
        return out + [('missing', 'host run records cannot be read here (local run)')]
    runs = env.host_runs(X)
    if runs is None:
        return out + [('missing', 'no host records for the exact-head run on the tree')]
    hits = [r for r in runs if r.get('workflow_path') == p.get('workflow_path')]
    if not hits:
        return out + [('missing', 'no run of the named workflow on the tree')]
    r = hits[-1]
    jobs = {j.get('name'): j.get('conclusion') for j in r.get('jobs', [])}
    if r.get('head_sha') != X or jobs.get(p.get('job')) != 'success':
        out.append(('fail', 'the host run is not a successful run of the named job on the tree'))
    res = r.get('result')
    if res is None:
        return out + [('missing', 'the comparison result was not retrieved from the run')]
    if res.get('candidate_commit') != X or res.get('candidate_tree') != repo.tree_id(X):
        out.append(('fail', 'the PDF comparison names another commit or tree'))
    if res.get('sha256') is None or r.get('artifact_sha256') != res.get('sha256'):
        out.append(('fail', 'the uploaded artifact does not hash to the result'))
    if res.get('checker_blob_sha256') != p.get('checker_sha256'):
        out.append(('fail', 'the comparison was not produced by the checker blob of F'))
    return out
