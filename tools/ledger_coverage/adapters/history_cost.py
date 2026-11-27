"""Read-only cost measurement of the history walks: category-3 detection (R6.OBL29.1, the cumulative record set R*
over every tree reachable through any parent from M) and the custody walk Vers(M) (R6.CUST.4), over a real
repository's history, through the tool's verified reader.

This is a measurement, not a ledger-coverage run: it evaluates no configuration, admits nothing, reaches no verdict
and writes nothing but its own JSON file. It reads only object ids it is given and the objects they reach.

Usage:
  python3 -I -S -B tools/ledger_coverage/adapters/history_cost.py --repo DIR --m COMMIT --out FILE [--max-seconds N]

COMMIT is a full 40-hex commit id (no ref is resolved). FILE receives one JSON object of schema
oi-ledger-coverage-cost/1 (section A.44: the verdict reads this file and the exit status, not log text):
  outcome      'complete' | 'timeout' | 'error'
  phases       per walk: wall_seconds, commits, objects fetched by type, bytes read, and what the walk found
  peak_rss_kib self and children (resource.getrusage; ru_maxrss in KiB on Linux)
Exit status: 0 complete, 3 timeout (partial counts kept), 4 error (a failed read or a bad argument), 64 usage.
"""
import argparse
import importlib.util
import json
import os
import platform
import re
import resource
import signal
import sys
import time

here = os.path.dirname(os.path.abspath(__file__))
if 'ledger_coverage' not in sys.modules:
    _pkg = os.path.dirname(here)
    _spec = importlib.util.spec_from_file_location('ledger_coverage', os.path.join(_pkg, '__init__.py'),
                                                   submodule_search_locations=[_pkg])
    sys.modules['ledger_coverage'] = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(sys.modules['ledger_coverage'])

from ledger_coverage import record_authority as ra  # noqa: E402
from ledger_coverage.engine import category3 as c3  # noqa: E402
from ledger_coverage.engine import custody as cust  # noqa: E402
from ledger_coverage.engine import reconcile as rcmod  # noqa: E402
from ledger_coverage.engine import recon_route  # noqa: E402
from ledger_coverage.engine.gitobj import GitRepo  # noqa: E402

schema = 'oi-ledger-coverage-cost/1'
_hex40 = re.compile(r'[0-9a-f]{40}\Z')


class Timeout(Exception):
    pass


class Counter:
    """Counts the objects the verified reader fetches from `git cat-file --batch` (a request its object cache does not
    serve), by type, with their bytes; an uncached blob read twice is fetched twice. `distinct` counts distinct ids."""

    def __init__(self, repo):
        self.by_type = {}
        self.bytes = 0
        self.seen = set()
        inner = repo._batch

        def batch(oid):
            fresh = oid not in repo._objs
            kind, data = inner(oid)
            if fresh and kind is not None:
                self.by_type[kind] = self.by_type.get(kind, 0) + 1
                self.bytes += len(data)
                self.seen.add(oid)
            return kind, data
        repo._batch = batch

    def snapshot(self):
        return dict(self.by_type), self.bytes


def rss():
    return {'self': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            'children': resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss}


def measure(repo_dir, M, max_seconds):
    res = {'schema': schema, 'operation': 'history-cost', 'repo_commit': M, 'outcome': None, 'phases': [],
           'python': platform.python_version(), 'max_seconds': max_seconds}
    repo = GitRepo(repo_dir)
    count = Counter(repo)

    def phase(name, fn):
        types0, bytes0 = count.snapshot()
        t0 = time.perf_counter()
        ph = {'name': name, 'complete': False}
        res['phases'].append(ph)
        try:
            ph.update(fn())
            ph['complete'] = True
        finally:
            types1, bytes1 = count.snapshot()
            ph['wall_seconds'] = round(time.perf_counter() - t0, 3)
            ph['objects_fetched'] = {k: types1.get(k, 0) - types0.get(k, 0) for k in sorted(types1)}
            ph['bytes_read'] = bytes1 - bytes0
            ph['peak_rss_kib_after'] = rss()

    def detection():
        cum = c3.Cumulative(repo, [M], rcmod.reconciliation_schemas, recon_route.audits_root)
        found = cum.findings()
        kinds = {}
        for f in found:
            kinds[str(f['kind'])] = kinds.get(str(f['kind']), 0) + 1
        return {'commits': len(cum.visited) if isinstance(cum.visited, (list, set, dict)) else None,
                'classified_blobs': len(cum.info), 'kept_blobs': sum(1 for v in cum.info.values() if v is not None),
                'findings': kinds}

    def custody_walk():
        h = cust.History(repo, M, ra.custody_path, recon_route.audits_root)
        return {'commits': len(h.commits), 'custody_versions': len(h.vers),
                'discharge_bearing_configurations': sum(1 for d in h.configs.values() if cust.discharge_bearing(d))}

    t_all = time.perf_counter()
    try:
        repo.resolve(M)
        phase('category3-detection', detection)
        phase('custody-history', custody_walk)
        res['outcome'] = 'complete'
    except Timeout:
        res['outcome'] = 'timeout'
    except Exception as exc:  # a failed read or any other failure: recorded, never a verdict
        res['outcome'] = 'error'
        res['error'] = '%s: %s' % (type(exc).__name__, str(exc)[:500])
    res['wall_seconds'] = round(time.perf_counter() - t_all, 3)
    types, nbytes = count.snapshot()
    res['objects_fetched'] = types
    res['distinct_objects'] = len(count.seen)
    res['bytes_read'] = nbytes
    res['peak_rss_kib'] = rss()
    return res


def main(argv=None):
    p = argparse.ArgumentParser(prog='history_cost')
    p.add_argument('--repo', required=True)
    p.add_argument('--m', required=True)
    p.add_argument('--out', required=True)
    p.add_argument('--max-seconds', type=int, default=0)
    try:
        a = p.parse_args(argv)
    except SystemExit:
        return 64
    if not _hex40.match(a.m):
        res = {'schema': schema, 'operation': 'history-cost', 'outcome': 'error',
               'error': '--m is not a full lowercase commit id'}
        code = 4
    else:
        if a.max_seconds > 0:
            def on_alarm(_s, _f):
                raise Timeout()
            signal.signal(signal.SIGALRM, on_alarm)
            signal.alarm(a.max_seconds)
        res = measure(a.repo, a.m, a.max_seconds)
        signal.alarm(0)
        code = {'complete': 0, 'timeout': 3}.get(res['outcome'], 4)
    res['exit_status'] = code
    d = os.path.dirname(os.path.abspath(a.out))
    os.makedirs(d, exist_ok=True)
    with open(a.out, 'w') as fh:
        json.dump(res, fh, sort_keys=True, indent=1)
        fh.write('\n')
    return code


if __name__ == '__main__':
    sys.exit(main())
