"""Delegation contract oi-delegation/1: exact paths per class, executed natively by the tool (sec. 7, B2).

Every class is executed by the tool itself in a disposable full clone at X and, when C differs, at C, created
under --out (no --depth, no alternates; commit and tree ids checked in the clone). Checkers run from F's blobs.
The tool records each run (checker blob sha256, command line, working directory, exit status, the bytes of
each output it compares) and re-derives what it can. A result file supplied from outside the run is never
evidence for a class the tool can execute; host-run classes read the host's records through its interface. Without F
every class is a review item delegated-evidence-missing (T4); where clones cannot be made (a local run), the
same.
"""
import base64
import json
import os
import shutil
import subprocess
import sys

from . import outcome as oc
from . import util
from .host import HostUnavailable

delegation_schema = 'oi-delegation/1'
interface_version = 2


class Delegation:
    def __init__(self, doc, modules):
        if doc.get('schema') != delegation_schema:
            raise oc.Stop(oc.error, 'CONFIG_INVALID', 'unknown delegation schema')
        self.doc = doc
        self.modules = modules  # {adapter name: module}
        for c in doc['classes']:
            if c['adapter'] not in modules:
                raise oc.Stop(oc.error, 'CONFIG_INCONSISTENT', 'delegation class %s has no class adapter' % c['id'])
            for p in c.get('paths', []):
                if '*' in p or p.endswith('/') and c.get('kind') != 'record-dir':
                    raise oc.Stop(oc.error, 'CONFIG_INVALID', 'delegation paths must be exact: %s' % p)

    def paths(self):
        return [p for c in self.doc['classes'] for p in c.get('paths', []) if not p.endswith('/')]

    def record_prefixes(self):
        return [p for c in self.doc['classes'] for p in c.get('paths', []) if p.endswith('/')]

    def owns_ledgered(self, path):
        return any(path in c.get('ledgered_paths', []) for c in self.doc['classes'])

    def verify(self, repo, roles, env, ledger, supplied=None):
        """Items per class and the evidence record (for the admission snapshot). A class passes only if it passes
        at X and, where C differs, at C."""
        items, report = [], []
        F = roles.get('freeze')
        trees = [('X', roles['candidate'])]
        if roles.get('certified') and roles['certified'] != roles['candidate']:
            trees.append(('C', roles['certified']))
        for c in self.doc['classes']:
            mod = self.modules[c['adapter']]
            state, per_tree = 'pass', []
            results = []
            if F is None:
                # T4: never PASS without F; the native re-derivations that need no checker of F still run
                try:
                    got = mod.verify(repo, dict(roles, tree_role='X'), c, None, ledger)
                except Exception as exc:
                    got = [('fail', 'class adapter raised %s: %s' % (type(exc).__name__, exc))]
                got = [g for g in got if g[0] == 'fail']
                results.append(('X', got + [('missing', 'no freeze F: a delegated class never passes without F '
                                                        '(T4)')]))
            else:
                for name, tree in trees:
                    r = dict(roles, candidate=tree, tree_role=name)
                    try:
                        got = mod.verify(repo, r, c, env, ledger)
                    except Exception as exc:  # a class adapter fault is a defect of the evidence
                        got = [('fail', 'class adapter raised %s: %s' % (type(exc).__name__, exc))]
                    results.append((name, got))
            for name, n in sorted((supplied or {}).items()):
                if name in c.get('evidence', []):
                    # a supplied file is never evidence; it is inspected only to reject a defective one (G8)
                    try:
                        doc = json.loads(n.decode('utf-8'))
                    except (ValueError, UnicodeDecodeError, AttributeError):
                        doc = None
                    if isinstance(doc, dict) and ('plan' not in doc or doc.get('plan') is None):
                        results.append(('supplied', [('fail', '%s: plan field null or absent' % name)]))
            for name, got in results:
                for st, why in got:
                    if st == 'fail':
                        state = 'fail'
                        items.append(oc.make_item('DELEGATED', 'delegated-evidence-invalid',
                                                  '%s: %s' % (c['id'], why), None,
                                                  {'class': c['id'], 'tree': name, 'why': why},
                                                  delegated_class=c['id'], tree=name))
                    elif st == 'missing':
                        state = 'missing' if state == 'pass' else state
                        items.append(oc.make_item('DELEGATED', 'delegated-evidence-missing',
                                                  '%s: %s' % (c['id'], why), None,
                                                  {'class': c['id'], 'tree': name, 'why': why},
                                                  delegated_class=c['id'], tree=name))
                per_tree.append({'tree': name, 'findings': [list(x) for x in got]})
            report.append({'class': c['id'], 'adapter': c['adapter'], 'state': state, 'trees': per_tree})
        ev = env.record() if env is not None else None
        return items, {'classes': report, 'supplied_evidence_ignored': sorted(supplied or {}),
                       'evidence_record': ev}


def _bytes_record(b):
    if b is None:
        return None
    try:
        return {'utf8': b.decode('utf-8'), 'sha256': util.sha256(b)}
    except UnicodeDecodeError:
        return {'base64': base64.b64encode(b).decode('ascii'), 'sha256': util.sha256(b)}



# environment variables through which git reads configuration, or is pointed at another repository, index or object
# store; none of them passes to a delegated clone (R6.DELEG.3: no clone runs a configured smudge filter)
_git_env_drop = ('GIT_CONFIG_PARAMETERS', 'GIT_CONFIG_COUNT', 'GIT_CONFIG', 'GIT_DIR', 'GIT_WORK_TREE',
                 'GIT_INDEX_FILE', 'GIT_OBJECT_DIRECTORY', 'GIT_ALTERNATE_OBJECT_DIRECTORIES', 'GIT_COMMON_DIR',
                 'GIT_TEMPLATE_DIR', 'GIT_EXEC_PATH')


def clone_env(environ):
    """The git environment of a delegated clone and its checks: the caller's environment less every variable that
    carries configuration (GIT_CONFIG_PARAMETERS, GIT_CONFIG_COUNT, GIT_CONFIG_KEY_n, GIT_CONFIG_VALUE_n,
    GIT_CONFIG), redirects the repository, names a template directory (whose config and hooks a clone copies) or
    replaces git's helper programs (GIT_EXEC_PATH), with the system configuration off and the global configuration
    empty."""
    env = {k: v for k, v in environ.items()
           if k not in _git_env_drop and not k.startswith(('GIT_CONFIG_KEY_', 'GIT_CONFIG_VALUE_'))}
    env.update(GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull)
    return env


def clone_options():
    """Options of the delegated clone: an empty template, so no template config or hook reaches the clone."""
    return ['--template=']

class Native:
    """The disposable clones, the checker blobs from F and the run records of one tool run."""

    def __init__(self, repo, repo_path, out, freeze, enabled, host=None, repo_id=None, why_disabled=None,
                 replay=None):
        self.repo = repo
        self.repo_path = repo_path
        self.out = out
        self.freeze = freeze
        self.enabled = enabled
        self.why_disabled = why_disabled
        self.host = host
        self.repo_id = repo_id
        self.clones = {}
        self.runs = []
        self.host_records = []
        self.derivations = []
        self.replay = replay  # a snapshot's evidence record: runs are taken from it, nothing is executed

    def available(self):
        return self.enabled or self.replay is not None

    def clone(self, commit):
        if commit in self.clones:
            return self.clones[commit]
        if self.replay is not None:
            return None
        d = os.path.join(self.out, 'clones', commit)
        if os.path.exists(d):
            shutil.rmtree(d)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        # no configuration from the runner (for example a filter driver) applies to the clone, so its working tree is
        # checked out from X's blobs as they are (O-3, R6.DELEG.3)
        env = clone_env(os.environ)
        r = subprocess.run(['git', 'clone'] + clone_options() + ['--no-local', '--no-checkout', '--quiet',
                                                                  self.repo_path, d],
                           capture_output=True, text=True, env=env)
        if r.returncode != 0:
            raise RuntimeError('clone failed: %s' % r.stderr[-300:])
        if os.path.exists(os.path.join(d, '.git', 'objects', 'info', 'alternates')):
            raise RuntimeError('the clone has alternates')
        r = subprocess.run(['git', '-C', d, 'checkout', '--quiet', '--detach', commit], capture_output=True,
                           text=True, env=env)
        if r.returncode != 0:
            raise RuntimeError('checkout failed: %s' % r.stderr[-300:])
        head = subprocess.run(['git', '-C', d, 'log', '-1', '--format=%H %T'], capture_output=True,
                              text=True, env=env).stdout.split()
        if head != [commit, self.repo.tree_id(commit)]:
            raise RuntimeError('the clone\'s commit or tree differs from %s' % commit)
        self.clones[commit] = d
        return d

    def checker(self, path, place_in=None):
        """F's blob of a checker, written under --out (or, for a checker that locates the repository from its own
        file, at its path inside the clone, which lies under --out). Returns (file, sha256)."""
        data = self.repo.read(self.freeze, path)
        if data is None:
            raise RuntimeError('checker %s absent at F' % path)
        sha = util.sha256(data)
        if place_in is not None:
            f = os.path.join(place_in, path)
        else:
            f = os.path.join(self.out, 'checkers', sha, os.path.basename(path))
        os.makedirs(os.path.dirname(f), exist_ok=True)
        with open(f, 'wb') as fh:
            fh.write(data)
        return f, sha

    def run(self, label, tree, argv, cwd, checker_sha, result_files=(), timeout=3600):
        """Runs one command; records it with the complete bytes of stdout and of each result file it wrote."""
        if self.replay is not None:
            for r in self.replay.get('runs', []):
                if r['label'] == label and r['tree'] == tree:
                    return _replayed(r)
            return None
        r = subprocess.run(argv, cwd=cwd, capture_output=True, timeout=timeout)
        files = {}
        for f in result_files:
            p = f if os.path.isabs(f) else os.path.join(cwd, f)
            files[os.path.basename(f)] = open(p, 'rb').read() if os.path.isfile(p) else None
        rel = [a.replace(self.out, '<out>') if isinstance(a, str) else a for a in argv]
        rec = {'label': label, 'tree': tree, 'checker_sha256': checker_sha, 'argv': rel,
               'cwd': cwd.replace(self.out, '<out>'), 'exit': r.returncode, 'stdout': _bytes_record(r.stdout),
               'stderr_sha256': util.sha256(r.stderr), 'files': {k: _bytes_record(v) for k, v in files.items()}}
        self.runs.append(rec)
        return {'exit': r.returncode, 'stdout': r.stdout, 'files': files}

    def host_runs(self, head_sha):
        """The host's run and job records for a commit, as returned (B2 host-run classes): only runs with event
        `push` or `workflow_dispatch` whose repository and head repository ids equal the configuration's
        `repository_id` (sec. 7.2); a failed or incomplete read gives None, never another source (GV7)."""
        if self.replay is not None:
            return [h for h in self.replay.get('host_records', []) if h.get('head_sha') == head_sha] or None
        if self.host is None:
            return None
        try:
            got = self.host.runs_for(self.repo_id, head_sha)
        except HostUnavailable:
            return None
        keep = []
        for r in got or []:
            if not isinstance(r, dict) or not isinstance(r.get('jobs'), list):
                return None
            if r.get('event') in ('push', 'workflow_dispatch') and r.get('repository_id') == self.repo_id and \
                    r.get('head_repository_id') == self.repo_id:
                keep.append(r)
        self.host_records += keep
        return keep or None

    def derive(self, cls, tree, what, holds):
        self.derivations.append({'class': cls, 'tree': tree, 'check': what, 'holds': bool(holds)})

    def record(self):
        if self.replay is not None:
            return self.replay
        return {'enabled': self.enabled, 'why_disabled': self.why_disabled, 'clones': sorted(self.clones),
                'runs': self.runs, 'host_records': self.host_records, 'derivations': self.derivations,
                'python': sys.version.split()[0]}


def _replayed(r):
    def back(x):
        if x is None:
            return None
        if 'utf8' in x:
            return x['utf8'].encode('utf-8')
        return base64.b64decode(x['base64'])
    return {'exit': r['exit'], 'stdout': back(r['stdout']), 'files': {k: back(v) for k, v in r['files'].items()}}
