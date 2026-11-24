"""A fake rest transport over an in-memory host, for the controls of the real-host history reader.

`FakeRest` serves the rest reads `RestHost` makes (branches, commit listings with and without a path, single
commits, trees, raw contents, a commit's pull requests, pull requests) from a `MemoryHost`'s repository. Its
path-filtered commit listing simplifies history as the host's does: a merge commit whose path equals one of its
parents' is not listed. `HybridHost` is a `RestHost` reading main, trees, files and histories through such a
transport, and run records and threads from the in-memory host. `old_file_history` is the history reader as it
stood before the correction (path-filtered listing, then a first-parent filter), kept here as a countercontrol.
Every identity is a synthetic fixture. Nothing is written to any host.
"""
import hashlib
import json
import os
import sys
import urllib.parse

here = os.path.dirname(os.path.abspath(__file__))
tools = os.path.dirname(os.path.dirname(here))
if tools not in sys.path:
    sys.path.insert(0, tools)

from ledger_coverage.engine import host as hostmod  # noqa: E402

API = 'https://api.fixture.invalid'


def git_blob(b):
    return hashlib.sha1(b'blob %d\x00' % len(b) + b).hexdigest()


def _entry_bytes(v):
    """(mode, bytes) of a fixture file value: bytes, or a tuple ('symlink', target) / ('submodule', commit)."""
    if isinstance(v, tuple):
        return ('120000' if v[0] == 'symlink' else '160000'), v[1].encode()
    return '100644', v


class FakeRest:
    """The transport: call(url, headers) -> (bytes, headers), or HostUnavailable as the real transport raises it.

    Knobs: `listing_pages` (serve at most that many pages of a commit listing, then empty pages: a host listing that
    ends early), `truncate_trees` (tree listings report truncated), `fail` (url substrings answered with HTTP 500),
    `corrupt` (paths whose raw contents are served altered)."""

    def __init__(self, mem, repo_id):
        self.mem, self.repo_id = mem, repo_id
        self.listing_pages = None
        self.truncate_trees = False
        self.fail = set()
        self.corrupt = set()
        self.log = []
        self._trees = {}

    # -- the repository model
    def _repo(self):
        return self.mem.repos[self.repo_id]

    def _commit(self, c):
        cm = self._repo()['commits'].get(c)
        if cm is None:
            raise hostmod.HostUnavailable('HTTP Error 404: Not Found')
        return cm

    def _tree_of(self, files, prefix=''):
        """The synthetic tree id of the directory `prefix` of `files`, registering every subtree."""
        entries = {}
        for p, v in files.items():
            if not p.startswith(prefix):
                continue
            rest = p[len(prefix):]
            if '/' in rest:
                d = rest.split('/', 1)[0]
                entries[d] = ('tree', '040000', None)
            else:
                mode, b = _entry_bytes(v)
                typ = 'commit' if mode == '160000' else 'blob'
                entries[rest] = (typ, mode, git_blob(b))
        for d in [k for k, e in entries.items() if e[0] == 'tree']:
            entries[d] = ('tree', '040000', self._tree_of(files, prefix + d + '/'))
        doc = [{'path': k, 'type': e[0], 'mode': e[1], 'sha': e[2]} for k, e in sorted(entries.items())]
        tid = hashlib.sha1(json.dumps(doc, sort_keys=True).encode()).hexdigest()
        self._trees[tid] = doc
        return tid

    def _reachable(self, head):
        """Every commit reachable from head, children before parents (the host's listing order)."""
        seen, order, gen = set(), [], {}

        def g(c):
            if c in gen:
                return gen[c]
            ps = self._commit(c)['parents']
            gen[c] = 1 + max([g(p) for p in ps] or [0])
            return gen[c]
        stack = [head]
        while stack:
            c = stack.pop()
            if c in seen:
                continue
            seen.add(c)
            order.append(c)
            stack.extend(self._commit(c)['parents'])
        return sorted(order, key=lambda c: (-g(c), c))

    def _path_changed(self, c, parent, path):
        a = self._commit(c)['files'].get(path)
        b = self._commit(parent)['files'].get(path) if parent is not None else None
        return a != b

    def _listed_for_path(self, c, path):
        """The host's simplified path history: a non-merge commit is listed when it changes the path against its
        parent; a merge commit only when the path differs from every parent's (a merge whose path equals one
        parent's, typically its second, is omitted)."""
        ps = self._commit(c)['parents']
        if len(ps) <= 1:
            return self._path_changed(c, ps[0] if ps else None, path)
        return all(self._path_changed(c, p, path) for p in ps)

    def _commit_json(self, c):
        cm = self._commit(c)
        return {'sha': c, 'parents': [{'sha': p} for p in cm['parents']],
                'commit': {'tree': {'sha': self._tree_of(cm['files'])}}}

    # -- the transport
    def __call__(self, url, headers):
        self.log.append(url)
        for f in self.fail:
            if f in url:
                raise hostmod.HostUnavailable('HTTP Error 500: Internal Server Error')
        u = urllib.parse.urlsplit(url)
        q = dict(urllib.parse.parse_qsl(u.query))
        parts = u.path.strip('/').split('/')
        if parts[:2] != ['repositories', str(self.repo_id)]:
            raise hostmod.HostUnavailable('HTTP Error 404: Not Found')
        rest = parts[2:]
        raw = headers.get('Accept') == 'application/vnd.github.raw'
        if rest == ['branches', 'main']:
            return self._json({'commit': {'sha': self._repo()['main']}})
        if rest == ['commits']:
            commits = self._reachable(q['sha'])
            if 'path' in q:
                commits = [c for c in commits if self._listed_for_path(c, q['path'])]
            per, page = int(q.get('per_page', 30)), int(q.get('page', 1))
            if self.listing_pages is not None and page > self.listing_pages:
                return self._json([])
            return self._json([self._commit_json(c) for c in commits[(page - 1) * per:page * per]])
        if len(rest) == 2 and rest[0] == 'commits':
            return self._json(self._commit_json(rest[1]))
        if len(rest) == 3 and rest[0] == 'commits' and rest[2] == 'pulls':
            m = self.mem.merges.get((self.repo_id, rest[1]))
            if not m:
                return self._json([])
            return self._json([{'merge_commit_sha': m['merge_commit'], 'url': '%s/repositories/%d/pulls/%s'
                                % (API, self.repo_id, rest[1])}])
        if len(rest) == 2 and rest[0] == 'pulls':
            m = self.mem.merges.get((self.repo_id, rest[1]))
            return self._json({'merged_by': {'id': m['merged_by_id']}, 'merged_at': m['merged_at'],
                               'merge_commit_sha': m['merge_commit']})
        if len(rest) == 3 and rest[:2] == ['git', 'trees']:
            if q.get('recursive') == '1':
                files = self._commit(rest[2])['files']
                out = []
                for p, v in sorted(files.items()):
                    mode, b = _entry_bytes(v)
                    out.append({'path': p, 'type': 'commit' if mode == '160000' else 'blob', 'mode': mode,
                                'sha': git_blob(b)})
                return self._json({'tree': out, 'truncated': self.truncate_trees})
            doc = self._trees.get(rest[2])
            if doc is None:
                raise hostmod.HostUnavailable('HTTP Error 404: Not Found')
            return self._json({'sha': rest[2], 'tree': doc, 'truncated': self.truncate_trees})
        if rest and rest[0] == 'contents' and raw:
            path = '/'.join(rest[1:])
            v = self._commit(q['ref'])['files'].get(path)
            if v is None:
                raise hostmod.HostUnavailable('HTTP Error 404: Not Found')
            b = _entry_bytes(v)[1]
            return (b + b' ' if path in self.corrupt else b), {}
        raise hostmod.HostUnavailable('HTTP Error 404: Not Found')

    @staticmethod
    def _json(o):
        return json.dumps(o).encode(), {}


class HybridHost(hostmod.RestHost):
    """main, trees, files, chains and histories through the rest transport; run records, repositories, threads and
    artifacts from the in-memory host."""

    def __init__(self, mem, repo_id, transport=None, max_calls=20000):
        super().__init__(API, 'fixture-token', transport or FakeRest(mem, repo_id), max_calls)
        self.mem = mem

    def run_record(self, run_id, repo_id=None):
        return self.mem.run_record(run_id, repo_id)

    def repository(self, repo_id):
        return self.mem.repository(repo_id)

    def comments(self, repo_id, issue):
        return self.mem.comments(repo_id, issue)

    def deletion_events(self, repo_id, issue):
        return self.mem.deletion_events(repo_id, issue)

    def runs_for(self, repo_id, head_sha):
        return self.mem.runs_for(repo_id, head_sha)

    def artifact_sha256(self, repo_id, run_id, name):
        return self.mem.artifact_sha256(repo_id, run_id, name)


def old_file_history(h, repo_id, path):
    """The reader before the correction: the host's path-filtered listing of main, each listed commit with its pull
    request's merge record, kept only when on main's first-parent chain (walked one commit read at a time)."""
    def on_chain(commit, head, limit=5000):
        c = head
        for _ in range(limit):
            if c == commit:
                return True
            ps = h._json('/repositories/%d/commits/%s' % (repo_id, c))['parents']
            if not ps:
                return False
            c = ps[0]['sha']
        raise hostmod.HostUnavailable('first-parent walk exceeded its limit')
    out, page = [], 1
    head = h.main_head(repo_id)
    while True:
        cs = h._json('/repositories/%d/commits?sha=%s&path=%s&per_page=100&page=%d' % (repo_id, head, path, page))
        for c in cs:
            pulls = h._json('/repositories/%d/commits/%s/pulls' % (repo_id, c['sha']))
            merged = [p for p in pulls if p.get('merge_commit_sha') == c['sha']]
            m = h._json(merged[0]['url']) if merged else {}
            out.append({'commit': c['sha'], 'parent': (c.get('parents') or [{}])[0].get('sha'),
                        'blob': h.file_at(repo_id, c['sha'], path),
                        'merged_by_id': (m.get('merged_by') or {}).get('id'), 'merged_at': m.get('merged_at'),
                        'merge_commit': m.get('merge_commit_sha')})
        if len(cs) < 100:
            break
        page += 1
    out.reverse()
    return [x for x in out if on_chain(x['commit'], head)]


def as_merge_landings(mem, repo_id):
    """Rewrites every commit on main's first-parent chain that has a merge record into a two-parent merge: its
    content moves to a new branch commit `b-<id>` on its first parent, and the merge (same id, same tree, same merge
    record) takes that branch commit as its second parent. The first-parent history is unchanged; the host's
    path-filtered listing now omits each such merge, since its paths equal its second parent's."""
    r = mem.repos[repo_id]
    for c in mem.first_parents(repo_id, r['main']):
        cm = r['commits'][c]
        if (repo_id, c) in mem.merges and cm['parents'] and len(cm['parents']) == 1:
            b = 'b-' + c
            r['commits'][b] = {'parents': [cm['parents'][0]], 'files': dict(cm['files'])}
            cm['parents'] = [cm['parents'][0], b]
