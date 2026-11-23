"""An in-memory host world for the admission controls (TR1-TR47) and the simulated-chain controls.

It builds, on the engine's in-memory host, a repository with an authority record on `main` (approved, reviewed and
merged by the owner), an empty freeze ledger, a pinned workflow, a run record, and a plan thread holding the
owner's designation of a freeze `F` that the caller builds in its own (in-memory) git repository with a pin table.
Every identity here is a synthetic fixture. Nothing is written to any host.
"""
import hashlib
import json
import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
tools = os.path.dirname(os.path.dirname(here))
if tools not in sys.path:
    sys.path.insert(0, tools)

from ledger_coverage.engine import authority as auth, host as hostmod  # noqa: E402

OWNER_ID, OWNER_LOGIN = 4242, 'owner-c'
REPO_ID = 77
WF_PATH = '.github/workflows/lc.yml'
WF = b'name: lc\non: workflow_dispatch\n'
PLAN, ROUND = 'syn-plan', 'r1'
PLAN_ISSUE, AUTH_ISSUE = 11, 12
LEDGER_PATH = 'syn/freeze/freeze-ledger.json'
FORMS = {'version': 1, 'first_line': 'bytes up to the first LF, at most one trailing CR removed',
         'templates': {
             'freeze-designate': 'oi-freeze/1 designate plan=<plan_id> round=<round_id> commit=<F>',
             'freeze-withdraw': 'oi-freeze/1 withdraw plan=<plan_id> round=<round_id> commit=<F>',
             'freeze-supersede': 'oi-freeze/1 supersede plan=<plan_id> round=<round_id> commit=<F> by=<F2>',
             'authority-approve': 'oi-authority/1 approve from=<from> to=<to>',
             'ledger-append': 'oi-freeze-ledger/1 append plan=<plan_id> round=<round_id> from=<from> to=<to>'}}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def jb(o):
    return (json.dumps(o, indent=1, sort_keys=True) + '\n').encode()


def authority(pin_table_path, owner_id=OWNER_ID, supersedes=None, extra=None):
    a = {'schema': auth.authority_schema, 'status': 'synthetic fixture',
         'owner': {'id': owner_id, 'login': OWNER_LOGIN},
         'repository': {'id': REPO_ID, 'full_name': 'fixture/repo', 'fork': False},
         'workflow': {'path': WF_PATH, 'content_sha256': sha(WF)},
         'engine_pins': {},
         'plans': [{'plan_id': PLAN, 'thread': {'repository_id': REPO_ID, 'issue': PLAN_ISSUE}, 'rounds': [ROUND],
                    'pin_table_path': pin_table_path}],
         'authority_thread': {'repository_id': REPO_ID, 'issue': AUTH_ISSUE},
         'freeze_ledger_path': LEDGER_PATH, 'forms': FORMS, 'supersedes': supersedes}
    a.update(extra or {})
    return a


def pin_table(entries):
    rows = '\n'.join('| `%s` | `%s` |' % (n, h) for n, h in sorted(entries.items()))
    return ('# PREREG\n\n### 1.1 Record pins\n\n| File | sha256 |\n|---|---|\n%s\n' % rows).encode()


class World:
    """host: the in-memory host; a_bytes: A on main; run_id: the attested run."""

    def __init__(self, pin_table_path, ledger_events=None):
        self.h = hostmod.MemoryHost()
        self.h.add_repo(REPO_ID, 'fixture/repo')
        self.pin_table_path = pin_table_path
        self.a = authority(pin_table_path)
        self.a_bytes = jb(self.a)
        self.ledger = {'schema': auth.ledger_schema, 'events': list(ledger_events or [])}
        self.ledger_bytes = jb(self.ledger)
        self.review = jb({'schema': 'oi-review-record/1', 'reviewer': 'reviewer-b',
                          'reviewed': {'path': auth.authority_path, 'blob_sha256': sha(self.a_bytes)},
                          'previous': 'none', 'method': 'read A', 'verdicts': [{'item': 'A', 'verdict': 'accept'}]})
        self.t = 0
        self.cid = 0
        self.comments = {(REPO_ID, PLAN_ISSUE): [], (REPO_ID, AUTH_ISSUE): []}
        self.h.threads = self.comments
        self.approve(AUTH_ISSUE, 'oi-authority/1 approve from=none to=%s' % sha(self.a_bytes))
        self.approve(AUTH_ISSUE, 'oi-authority/1 approve from=none to=%s' % sha(self.ledger_bytes))
        files = {auth.authority_path: self.a_bytes, LEDGER_PATH: self.ledger_bytes, WF_PATH: WF,
                 auth.review_path(self.a, sha(self.a_bytes)): self.review}
        self.main = 'c1'
        self.h.add_commit(REPO_ID, 'c0', [], {})
        self.h.add_commit(REPO_ID, 'c1', ['c0'], files, merged_by=OWNER_ID, merged_at=self.tick())
        self.h.repos[REPO_ID]['main'] = 'c1'
        self.run_id = 501
        self.h.runs[self.run_id] = {'repository_id': REPO_ID, 'fork': False, 'workflow_path': WF_PATH,
                                    'head_sha': 'c1'}

    def tick(self):
        self.t += 1
        return '2026-11-23T00:00:%02dZ' % self.t

    def comment(self, issue, body, author_id=OWNER_ID, login=OWNER_LOGIN, edits=(), hidden=False, at=None):
        self.cid += 1
        c = {'id': 9000 + self.cid, 'author_id': author_id, 'author_login': login, 'created_at': at or self.tick(),
             'body': body, 'edits': list(edits), 'hidden': hidden}
        self.comments.setdefault((REPO_ID, issue), []).append(c)
        return c

    def approve(self, issue, body, **kw):
        return self.comment(issue, body, **kw)

    def designate(self, F, **kw):
        return self.comment(PLAN_ISSUE, 'oi-freeze/1 designate plan=%s round=%s commit=%s' % (PLAN, ROUND, F), **kw)

    def control(self):
        return {'host': self.h, 'run_id': self.run_id, 'repo_id': REPO_ID}

    def args(self, F):
        return ['--freeze', F, '--plan', PLAN, '--round', ROUND]

    def add_main(self, cid, files, merged_by=OWNER_ID, merged_at=None):
        """A new first-parent commit on main changing `files`."""
        base = dict(self.h.repos[REPO_ID]['commits'][self.main]['files'])
        base.update(files)
        for k in [k for k, v in base.items() if v is None]:
            del base[k]
        self.h.add_commit(REPO_ID, cid, [self.main], base, merged_by=merged_by, merged_at=merged_at or self.tick())
        self.main = cid
        self.h.repos[REPO_ID]['main'] = cid
        self.h.runs[self.run_id]['head_sha'] = cid


def freeze_files(world, cfg_path, cfg_bytes, review_path, review_bytes, auth_path, auth_bytes, extra_listed=()):
    """Files to add at F: the pin table listing the configuration, its review and authorization, and A."""
    rec_dir = world.pin_table_path.rsplit('/', 1)[0] + '/'
    entries = {}
    for p, b in [(cfg_path, cfg_bytes), (review_path, review_bytes), (auth_path, auth_bytes)] + list(extra_listed):
        entries[p[len(rec_dir):]] = sha(b)
    return {world.pin_table_path: pin_table(entries), auth.authority_path: world.a_bytes}
