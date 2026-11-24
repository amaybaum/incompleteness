"""Offline replay of a committed landing record (sec. 5, C3, F2).

`replay --snapshot rev:path|file --out dir` reads a landing record (oi-ledger-landing/1) and the committed result
and admission snapshot beside it, checks their hashes, and recomputes the result from git objects and the
snapshot alone: admission from the snapshot, every delegated class from the snapshot's recorded evidence, with no
host call, clone, build or checker run. Apart from the admission mode, the output must equal the committed result
byte for byte; the replay writes replay-result.json with admission mode "replay", which is never acceptable.
"""
import base64
import gzip
import json
import os
import posixpath

from . import outcome as oc
from . import util

landing_schema = 'oi-ledger-landing/1'


def _reader(spec, repo):
    """A function reading a sibling of the landing record, from git (rev:path) or the filesystem."""
    if ':' in spec and not os.path.exists(spec):
        rev, path = spec.split(':', 1)
        commit = repo.resolve(rev)
        base = posixpath.dirname(path)

        def read(name):
            return repo.read(commit, posixpath.join(base, name) if name else path)
        return read
    base = os.path.dirname(os.path.abspath(spec))

    def read_file(name):
        p = os.path.join(base, name) if name else spec
        return open(p, 'rb').read() if os.path.isfile(p) else None
    return read_file


def evidence_problems(ev):
    """Every recorded result file and output must hash to the sha256 recorded beside it."""
    out = []
    for r in (ev or {}).get('runs', []):
        for name, b in [('stdout', r.get('stdout'))] + sorted((r.get('files') or {}).items()):
            if b is None:
                continue
            data = b['utf8'].encode('utf-8') if 'utf8' in b else base64.b64decode(b['base64'])
            if util.sha256(data) != b.get('sha256'):
                out.append('%s/%s: recorded bytes do not hash to the recorded sha256' % (r.get('label'), name))
    return out


def cli(a, out, repo, stderr):
    from . import cli as climod
    from .gitobj import GitRepo, Overlay
    if repo is None:
        repo = Overlay(GitRepo(getattr(a, 'repo', None) or os.getcwd()))

    def fail(cls, msg, **d):
        res = {'schema': oc.result_schema, 'operation': 'replay', 'outcome': oc.error, 'exit_status': 65,
               'stop': {'class': cls, 'message': msg, 'detail': d}, 'items': [], 'preflight': [],
               'record_checks': None}
        oc.annotate(res)
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, 'replay-result.json'), 'w', encoding='utf-8') as f:
            f.write(util.dump_result(res))
        return 65, res
    read = _reader(a.snapshot, repo)
    try:
        land = json.loads(read(None).decode('utf-8'))
    except (ValueError, AttributeError):
        return fail('REPLAY_REFUSED', 'the landing record cannot be read')
    if land.get('schema') != landing_schema:
        return fail('REPLAY_REFUSED', 'not an oi-ledger-landing/1 record')
    gz = read(land['result']['path'])
    snap_b = read(land['snapshot']['path'])
    if gz is None or snap_b is None:
        return fail('REPLAY_REFUSED', 'the committed result or snapshot is missing')
    try:
        raw = gzip.decompress(gz)
    except OSError:
        return fail('REPLAY_REFUSED', 'the committed result is not gzip')
    if util.sha256(raw) != land['result']['sha256'] or util.sha256(gz) != land['result'].get('compressed_sha256'):
        return fail('REPLAY_REFUSED', 'the committed result does not hash to its recorded sha256')
    snap = json.loads(snap_b.decode('utf-8'))
    if util.fingerprint(snap) != land['snapshot']['sha256']:
        return fail('REPLAY_REFUSED', 'the snapshot does not hash to its recorded sha256')
    committed = json.loads(raw.decode('utf-8'))
    adm = (committed.get('config') or {}).get('admission') or {}
    if adm.get('snapshot_sha256') != land['snapshot']['sha256']:
        return fail('REPLAY_REFUSED', 'the result names another admission snapshot')
    ev = snap.get('delegated_evidence')
    probs = evidence_problems(ev)
    if probs:
        return fail('REPLAY_REFUSED', probs[0], problems=probs[:20])
    decided = [c['class'] for c in (committed.get('delegation') or {}).get('classes', [])
               if c.get('state') in ('pass', 'fail')]
    if decided and not (ev and ev.get('runs') is not None):
        return fail('REPLAY_REFUSED', 'the snapshot lacks the evidence for a class the result decided',
                    classes=decided)
    argv = list(snap.get('invocation') or committed.get('invocation') or [])
    if not argv:
        return fail('REPLAY_REFUSED', 'no recorded invocation')
    argv = argv[:1] + ['--out', os.path.join(out, 'run')] + argv[1:]
    control = {'replay_snapshot': snap, 'replay_evidence': ev or {'runs': [], 'host_records': []}}
    import io
    code, res = climod.run(argv, repo=repo, harness=False, stderr=io.StringIO(), control=control)
    if res is None:
        return fail('REPLAY_REFUSED', 'the replay produced no result')
    a1 = json.loads(util.dump_result(res))
    a2 = json.loads(raw.decode('utf-8'))
    for d in (a1, a2):
        if isinstance(d.get('config', {}).get('admission'), dict):
            d['config']['admission']['mode'] = 'replay'
    equal = util.canonical(a1) == util.canonical(a2)
    res['replay'] = {'equal_to_committed': equal, 'landing': land.get('name'),
                     'committed_sha256': land['result']['sha256']}
    oc.annotate(res)
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, 'replay-result.json'), 'w', encoding='utf-8') as f:
        f.write(util.dump_result(res))
    if not equal:
        return fail('REPLAY_MISMATCH', 'the replay differs from the committed result')
    return res['exit_status'], res
