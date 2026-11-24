"""purity-lint over a staged configuration (sec. 16.1, 16.2).

The configuration does not land with the tool: it belongs in the retirement plan's record directory, frozen with
the plan at F. This runs the engine's purity lint exactly as `ledger_coverage.py purity-lint --config REV:PATH`
does, with the configuration read from an in-memory stand-in for F (REV's tree plus the staged file at PATH).
Nothing reaches the repository.

Usage: python3 -I -B tools/ledger_coverage/adapters/staged_purity_lint.py --repo DIR --config REV:PATH
       --staged-config FILE --out DIR
"""
import argparse
import json
import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
tools = os.path.dirname(os.path.dirname(here))
if 'ledger_coverage' not in sys.modules:
    # the package is loaded by its location, as the entry point loads it; no directory is put on sys.path
    import importlib.util
    _pkg = os.path.dirname(here)
    _spec = importlib.util.spec_from_file_location('ledger_coverage', os.path.join(_pkg, '__init__.py'),
                                                   submodule_search_locations=[_pkg])
    sys.modules['ledger_coverage'] = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(sys.modules['ledger_coverage'])

from ledger_coverage.engine import config as cfgmod, gitobj, outcome as oc, purity, util  # noqa: E402
from ledger_coverage.adapters import a1_controls as a1c  # noqa: E402


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True)
    ap.add_argument('--config', required=True)
    ap.add_argument('--staged-config', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args(argv)
    repo = gitobj.Overlay(gitobj.GitRepo(args.repo))
    rev, path = args.config.split(':', 1)
    with open(args.staged_config, 'rb') as f:
        commit = a1c.simulated_freeze(repo, repo.resolve(a1c.rev_parse(args.repo, rev)), path, f.read())
    loaded = cfgmod.load(repo, commit, path, None, None, 'harness')
    values = purity.config_values(repo.read, commit, loaded.config)
    profs = [p for p in loaded.profiles.values() if p.kind in ('review', 'deny')]
    res = purity.lint_engine(values, profs)
    doc = {'schema': oc.result_schema, 'operation': 'purity-lint', 'findings': res,
           'outcome': oc.pass_ if not res else oc.fail, 'exit_status': 0 if not res else 20,
           'preflight': [], 'record_checks': None, 'items': [],
           'config': {'path': path, 'stand_in_for_F': commit, 'blob_sha256': util.sha256(repo.read(commit, path))}}
    os.makedirs(args.out, exist_ok=True)
    with open(os.path.join(args.out, 'result.json'), 'w', encoding='utf-8') as f:
        f.write(util.dump_result(doc))
    print(json.dumps({'outcome': doc['outcome'], 'findings': len(res)}))
    return doc['exit_status']


if __name__ == '__main__':
    sys.exit(main())
