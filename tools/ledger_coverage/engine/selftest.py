"""In-memory engine controls (sec. 10.1 and the engine parts of sec. 10.2, 13, 16) and the preflight subset."""
import json
import os

from . import outcome as oc
from . import util


def preflight():
    """Cheap controls run before every evaluation; any failure voids the run."""
    from . import controls_engine as ce
    return ce.run(ce.preflight_ids)


def cli(a, out):
    from . import controls_engine as ce
    from . import purity
    if a.op == 'purity-lint':
        values, profs = set(), []
        if a.config:
            from . import config as cfgmod
            from .gitobj import GitRepo
            repo = GitRepo(a.repo or os.getcwd())
            rev, path = a.config.split(':', 1)
            commit = repo.resolve(rev)  # a full id; refs are not consulted
            loaded = cfgmod.load(repo, commit, path, None, None, 'harness')
            cfg = loaded.config
            values = purity.config_values(repo.read, commit, cfg)
            profs = [p for p in loaded.profiles.values() if p.kind in ('review', 'deny')]
        res = purity.lint_engine(values, profs)
        doc = {'schema': oc.result_schema, 'operation': 'purity-lint', 'findings': res,
               'outcome': oc.pass_ if not res else oc.fail, 'exit_status': 0 if not res else 20,
               'preflight': [], 'record_checks': None, 'items': []}
    else:
        rs = ce.run(None)
        bad = [r for r in rs if not r['passed']]
        doc = {'schema': oc.result_schema, 'operation': 'self-test', 'controls': rs,
               'outcome': oc.pass_ if not bad else oc.void, 'exit_status': 0 if not bad else 70,
               'preflight': rs, 'record_checks': None, 'items': []}
    oc.annotate(doc)
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, 'result.json'), 'w', encoding='utf-8') as f:
        f.write(util.dump_result(doc))
    return doc['exit_status'], doc
