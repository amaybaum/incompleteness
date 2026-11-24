"""An in-memory host world for the admission and execution-identity controls (TR1-TR3, TR5, TR13-TR15, TR28-TR30,
TR48, TR50-TR52, GV7, EI1-EI7) and the simulated-chain controls.

It builds, in the caller's in-memory git repository, a tool commit `T` holding a small fixture tool (an entry point
and one module under the package directory) and a pinned workflow, and a plan commit `F` whose `PREREG.md` carries the
pin table; on the engine's in-memory host it records the run (repository, head repository, event, head branch,
workflow path, `head_sha`) and the artifacts. Every identity here is a synthetic fixture. Nothing is written to any
host.
"""
import hashlib
import importlib.util
import json
import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
if 'ledger_coverage' not in sys.modules:
    _pkg = os.path.dirname(here)
    _spec = importlib.util.spec_from_file_location('ledger_coverage', os.path.join(_pkg, '__init__.py'),
                                                   submodule_search_locations=[_pkg])
    sys.modules['ledger_coverage'] = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(sys.modules['ledger_coverage'])

from ledger_coverage.engine import config as cfgmod, host as hostmod  # noqa: E402

REPO_ID = 77
RUN_ID = 501
WF_PATH = '.github/workflows/lc.yml'
WF = (b'name: lc\non:\n  workflow_dispatch:\npermissions:\n  contents: read\njobs:\n  run:\n'
      b'    runs-on: ubuntu-24.04\n    steps:\n'
      b'      - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683\n')
ENTRY, PKG = cfgmod.tool_layout()
TOOL_FILES = {ENTRY: b'# fixture entry point\n', PKG + 'engine/x.py': b'x = 1\n'}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def jb(o):
    return (json.dumps(o, indent=1, sort_keys=True) + '\n').encode()


def tool_pins(files=None, wf=None, wf_path=WF_PATH):
    """The configuration's `tool` field for the fixture tool."""
    files = TOOL_FILES if files is None else files
    return {'files': [{'path': p, 'blob_sha256': sha(b)} for p, b in sorted(files.items())],
            'workflow': {'path': wf_path, 'blob_sha256': sha(WF if wf is None else wf)}}


def pin_table(entries, earlier=None):
    """A PREREG.md whose last `Record pins` subsection lists `entries` {file: sha256}; `earlier`, if given, is listed
    in an earlier `Record pins` subsection."""
    def table(e):
        return '| File | sha256 |\n|---|---|\n' + ''.join('| `%s` | `%s` |\n' % (n, h) for n, h in sorted(e.items()))
    text = '# PREREG\n\n'
    if earlier is not None:
        text += '### 1.1 Record pins\n\n' + table(earlier) + '\n### 1.2 Results\n\nText.\n\n'
    text += '### 1.3 Record pins\n\n' + table(entries)
    return text.encode()


class World:
    """The tool commit T in `repo` (derived from `base`) and an in-memory host holding the run record of one run of
    the pinned workflow at T."""

    def __init__(self, repo, base, tool_files=None, wf=None, wf_path=WF_PATH, extra=None, run=None):
        self.repo = repo
        # T holds exactly the fixture tool under the tool's paths (the base's own files there are removed)
        files = {p: None for p in repo.entries(base) if p == ENTRY or p.startswith(PKG)}
        files.update(TOOL_FILES if tool_files is None else tool_files)
        files[wf_path] = WF if wf is None else wf
        files.update(extra or {})
        self.T = repo.derive(base, files, parents=[base], subject='tool commit')
        self.h = hostmod.MemoryHost()
        self.run_id = RUN_ID
        self.h.runs[RUN_ID] = dict({'repository_id': REPO_ID, 'head_repository_id': REPO_ID,
                                    'event': 'workflow_dispatch', 'head_branch': 'main', 'workflow_path': WF_PATH,
                                    'head_sha': self.T}, **(run or {}))

    def checkout(self):
        """{path: bytes} of T's tool files, as a checkout of T holds them."""
        ents = self.repo.entries(self.T)
        return {p: self.repo.read(self.T, p) if m in ('100644', '100755') else ('non-regular', m)
                for p, (m, _) in ents.items() if p == ENTRY or p.startswith(PKG)}

    def control(self, checkout=None):
        c = {'host': self.h, 'run_id': self.run_id, 'repo_id': REPO_ID}
        if checkout is not None:
            c['checkout'] = checkout
        return c

    @staticmethod
    def args(F):
        return ['--freeze', F]


def freeze(repo, commit, cfg_path, listed=None, extra=None, earlier=None, prereg=None):
    """F: `commit` plus a PREREG.md beside the configuration whose last Record pins subsection lists `listed`
    ({path: bytes}; by default every json file of the configuration's directory)."""
    d = cfg_path.rsplit('/', 1)[0] + '/'
    if listed is None:
        listed = {p: repo.read(commit, p) for p in repo.paths(commit)
                  if p.startswith(d) and p.endswith('.json') and '/' not in p[len(d):]}
    files = {d + 'PREREG.md': prereg if prereg is not None else
             pin_table({p[len(d):]: sha(b) for p, b in listed.items()}, earlier)}
    files.update(extra or {})
    return repo.derive(commit, files, parents=repo.parents(commit), subject='freeze')
