"""The host interface the admission reads (sec. 6.3): run records, files at a commit, `main`, threads and their
comments with edit history and hidden state, pull-request provenance, file histories and artifacts.

Two implementations: `RestHost`, which reads the host's interface inside a host job and is never used outside one, and
`MemoryHost`, an in-memory host for controls. Nothing here writes to any host.
"""
import base64
import hashlib
import json
import os
import urllib.error
import urllib.request


class HostUnavailable(Exception):
    pass


def first_line(body):
    """The body's bytes up to the first LF, with at most one trailing CR removed; no other normalization."""
    line = body.split('\n', 1)[0]
    if line.endswith('\r'):
        line = line[:-1]
    return line


class MemoryHost:
    """A deterministic in-memory host. Repositories hold commits {id: {parents, files}} and a `main` head;
    threads hold comments {id, author_id, author_login, created_at, body, edits: [previous bodies], hidden}."""

    def __init__(self):
        self.repos = {}
        self.runs = {}
        self.threads = {}
        self.merges = {}
        self.artifacts = {}
        self.fail = set()
        self.count_skew = {}
        self.deletions = None

    def add_repo(self, repo_id, full_name, fork=False):
        self.repos[repo_id] = {'full_name': full_name, 'fork': fork, 'commits': {}, 'main': None}

    def add_commit(self, repo_id, cid, parents, files, merged_by=None, merged_at=None):
        self.repos[repo_id]['commits'][cid] = {'parents': list(parents), 'files': dict(files)}
        if merged_by is not None:
            self.merges[(repo_id, cid)] = {'merged_by_id': merged_by, 'merged_at': merged_at, 'merge_commit': cid}

    def _need(self, what):
        if what in self.fail:
            raise HostUnavailable('host call failed: %s' % what)

    def run_record(self, run_id, repo_id=None):
        self._need('run')
        return self.runs.get(run_id)

    def repository(self, repo_id):
        self._need('repository')
        r = self.repos.get(repo_id)
        return None if r is None else {'id': repo_id, 'full_name': r['full_name'], 'fork': r['fork']}

    def main_head(self, repo_id):
        self._need('main')
        return self.repos[repo_id]['main']

    def file_at(self, repo_id, sha, path):
        self._need('file')
        c = self.repos.get(repo_id, {}).get('commits', {}).get(sha)
        v = None if c is None else c['files'].get(path)
        return v[1].encode() if isinstance(v, tuple) else v

    def paths_at(self, repo_id, sha, prefix):
        self._need('tree')
        c = self.repos[repo_id]['commits'].get(sha)
        return sorted(p for p in (c['files'] if c else {}) if p.startswith(prefix))

    def entries_at(self, repo_id, sha, prefix):
        """[(path, kind)] of every tree entry under prefix; kind is 'file', 'symlink' or 'submodule'. A fixture
        marks a non-regular entry by a tuple value ('symlink', target) or ('submodule', commit)."""
        self._need('tree')
        c = self.repos[repo_id]['commits'].get(sha)
        out = []
        for p, v in sorted((c['files'] if c else {}).items()):
            if p.startswith(prefix):
                out.append((p, v[0] if isinstance(v, tuple) else 'file'))
        return out

    def first_parents(self, repo_id, head):
        out = []
        c = head
        while c is not None:
            out.append(c)
            ps = self.repos[repo_id]['commits'][c]['parents']
            c = ps[0] if ps else None
        return out

    def on_first_parent_chain(self, repo_id, commit, head):
        self._need('chain')
        return commit in self.first_parents(repo_id, head)

    def file_history(self, repo_id, path):
        """Commits on main's first-parent chain whose `path` differs from their first parent's, oldest first, each
        with its first parent and the host's merge record (merged_by_id, merged_at, and the merge commit it names)."""
        self._need('history')
        out = []
        for c in reversed(self.first_parents(repo_id, self.repos[repo_id]['main'])):
            cm = self.repos[repo_id]['commits'][c]
            par = cm['parents'][0] if cm['parents'] else None
            before = self.repos[repo_id]['commits'][par]['files'].get(path) if par else None
            if cm['files'].get(path) != before:
                m = self.merges.get((repo_id, c), {})
                out.append({'commit': c, 'parent': par, 'blob': cm['files'].get(path),
                            'merged_by_id': m.get('merged_by_id'), 'merged_at': m.get('merged_at'),
                            'merge_commit': m.get('merge_commit')})
        return out

    def comments(self, repo_id, issue):
        """(comments in order, the host's reported count). Pages are read until the host reports no more."""
        self._need('comments')
        cs = self.threads.get((repo_id, issue), [])
        pages = [cs[i:i + 2] for i in range(0, len(cs), 2)] or [[]]
        out = []
        for k, page in enumerate(pages):
            self._need('page%d' % k)
            out.extend(page)
        return [dict(c) for c in out], len(cs) + self.count_skew.get((repo_id, issue), 0)

    def deletion_events(self, repo_id, issue):
        return self.deletions

    def runs_for(self, repo_id, head_sha):
        self._need('runs')
        return [dict(r) for r in getattr(self, 'host_runs', {}).get(head_sha, [])] or None

    def artifact_sha256(self, repo_id, run_id, name):
        return self.artifacts.get((run_id, name))


class RestHost:
    """Reads the host's rest and graphql interfaces with the job token. Used only inside a host job.

    Every rest read goes through `transport(url, headers)`, which returns (body bytes, headers) or raises
    HostUnavailable; by default it is an https get request. `max_calls` bounds the rest reads of one instance: a
    read beyond it raises HostUnavailable, so a history or chain that cannot be read within the bound refuses
    (fail-closed)."""

    max_pages = 2000

    def __init__(self, api, token, transport=None, max_calls=20000):
        self.api = api.rstrip('/')
        self.token = token
        self.transport = transport or self._https_get
        self.max_calls = max_calls
        self.calls = 0
        self._chains = {}
        self._trees = {}

    @staticmethod
    def detect(env):
        if env.get('GITHUB_ACTIONS') != 'true' or not env.get('GITHUB_RUN_ID') or not env.get('GITHUB_TOKEN'):
            return None
        return RestHost(env.get('GITHUB_API_URL', 'https://api.github.com'), env['GITHUB_TOKEN']), \
            int(env['GITHUB_RUN_ID']), int(env.get('GITHUB_REPOSITORY_ID') or 0)

    def _https_get(self, url, headers):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read(), r.headers
        except (urllib.error.URLError, OSError) as exc:
            raise HostUnavailable(str(exc))

    def _get(self, url, accept='application/vnd.github+json'):
        self.calls += 1
        if self.calls > self.max_calls:
            raise HostUnavailable('more than %d host reads' % self.max_calls)
        return self.transport(url if url.startswith('http') else self.api + url,
                              {'Authorization': 'Bearer ' + self.token, 'Accept': accept,
                               'X-GitHub-Api-Version': '2022-11-28'})

    def _json(self, url):
        data, _ = self._get(url)
        return json.loads(data.decode('utf-8'))

    def _graphql(self, query, variables):
        body = json.dumps({'query': query, 'variables': variables}).encode()
        req = urllib.request.Request(self.api + '/graphql', data=body,
                                     headers={'Authorization': 'Bearer ' + self.token})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                doc = json.loads(r.read().decode('utf-8'))
        except (urllib.error.URLError, OSError) as exc:
            raise HostUnavailable(str(exc))
        if doc.get('errors'):
            raise HostUnavailable('graphql errors')
        return doc['data']

    def run_record(self, run_id, repo_id):
        r = self._json('/repositories/%d/actions/runs/%d' % (repo_id, run_id))
        return {'run_id': run_id, 'repository_id': r['repository']['id'], 'fork': r['repository']['fork'],
                'workflow_path': r['path'].split('@', 1)[0], 'head_sha': r['head_sha']}

    def repository(self, repo_id):
        r = self._json('/repositories/%d' % repo_id)
        return {'id': r['id'], 'full_name': r['full_name'], 'fork': r['fork']}

    def main_head(self, repo_id):
        return self._json('/repositories/%d/branches/main' % repo_id)['commit']['sha']

    def file_at(self, repo_id, sha, path):
        try:
            data, _ = self._get('/repositories/%d/contents/%s?ref=%s' % (repo_id, path, sha),
                                accept='application/vnd.github.raw')
            return data
        except HostUnavailable as exc:
            if '404' in str(exc):
                return None
            raise

    def paths_at(self, repo_id, sha, prefix):
        return sorted(p for p, _ in self.entries_at(repo_id, sha, prefix))

    def entries_at(self, repo_id, sha, prefix):
        t = self._json('/repositories/%d/git/trees/%s?recursive=1' % (repo_id, sha))
        if t.get('truncated'):
            raise HostUnavailable('tree listing truncated')
        out = []
        for e in t['tree']:
            if not e['path'].startswith(prefix) or e['type'] == 'tree':
                continue
            kind = 'submodule' if e['type'] == 'commit' else 'symlink' if e.get('mode') == '120000' else \
                'file' if e['type'] == 'blob' and e.get('mode') in ('100644', '100755') else 'other'
            out.append((e['path'], kind))
        return sorted(out)

    def first_parent_chain(self, repo_id, head):
        """[(commit, first parent or None, root tree id)] of `head`'s first-parent chain, newest first, down to the
        root commit. The host's commit listing of `head` (no path, so no history simplification) holds every commit
        reachable from it; the chain is followed through it by first parents. A listing that ends, or a page bound
        reached, before the root is found raises HostUnavailable."""
        key = (repo_id, head)
        if key in self._chains:
            return self._chains[key]
        known, chain, cur = {}, [], head
        for page in range(1, self.max_pages + 1):
            cs = self._json('/repositories/%d/commits?sha=%s&per_page=100&page=%d' % (repo_id, head, page))
            if not isinstance(cs, list):
                raise HostUnavailable('commit listing of %s is not a list' % head)
            for c in cs:
                try:
                    known[c['sha']] = ([p['sha'] for p in c['parents']], c['commit']['tree']['sha'])
                except (KeyError, TypeError):
                    raise HostUnavailable('commit listing entry without its parents or tree')
            while cur in known:
                ps, tree = known[cur]
                chain.append((cur, ps[0] if ps else None, tree))
                if not ps:
                    self._chains[key] = chain
                    return chain
                cur = ps[0]
            if len(cs) < 100:
                raise HostUnavailable('the commit listing of %s ends before the root of its first-parent chain '
                                      '(missing %s)' % (head[:12], cur[:12]))
        raise HostUnavailable('the first-parent chain of %s exceeds %d listing pages' % (head[:12], self.max_pages))

    def on_first_parent_chain(self, repo_id, commit, head):
        return any(c == commit for c, _, _ in self.first_parent_chain(repo_id, head))

    def _tree(self, repo_id, sha):
        if sha not in self._trees:
            t = self._json('/repositories/%d/git/trees/%s' % (repo_id, sha))
            if t.get('truncated') or not isinstance(t.get('tree'), list):
                raise HostUnavailable('tree %s listing truncated or unreadable' % sha[:12])
            self._trees[sha] = {e['path']: (e['type'], e.get('mode'), e['sha']) for e in t['tree']}
        return self._trees[sha]

    def _entry(self, repo_id, tree, path):
        """(type, mode, object id) of `path` in the root tree `tree`, or None when absent."""
        parts = path.split('/')
        for k, name in enumerate(parts):
            e = self._tree(repo_id, tree).get(name)
            if e is None:
                return None
            if k == len(parts) - 1:
                return e
            if e[0] != 'tree':
                return None
            tree = e[2]

    def file_history(self, repo_id, path):
        """Commits on main's first-parent chain whose `path` differs from their first parent's, oldest first, each
        with its first parent, its bytes (None when deleted) and the host's merge record. Exact: every commit of the
        chain, merge commits included, is compared with its first parent by the path's blob id; the host's
        path-filtered commit listing is not used, since it simplifies history and omits a merge whose path equals
        its second parent's. The bytes read are checked against the tree entry's blob id."""
        head = self.main_head(repo_id)
        chain = self.first_parent_chain(repo_id, head)
        out = []
        after = None
        for k in range(len(chain) - 1, -1, -1):
            c, par, tree = chain[k]
            here = self._entry(repo_id, tree, path)
            if here is not None and (here[0] != 'blob' or here[1] not in ('100644', '100755')):
                raise HostUnavailable('%s is not a regular file at %s' % (path, c[:12]))
            blob_id = here[2] if here is not None else None
            if blob_id != after:
                blob = None
                if here is not None:
                    blob = self.file_at(repo_id, c, path)
                    if blob is None or hashlib.sha1(b'blob %d\x00' % len(blob) + blob).hexdigest() != here[2]:
                        raise HostUnavailable('the bytes of %s at %s do not match its tree entry' % (path, c[:12]))
                pulls = self._json('/repositories/%d/commits/%s/pulls' % (repo_id, c))
                merged = [p for p in pulls if p.get('merge_commit_sha') == c]
                m = self._json(merged[0]['url']) if merged else {}
                out.append({'commit': c, 'parent': par, 'blob': blob,
                            'merged_by_id': (m.get('merged_by') or {}).get('id'), 'merged_at': m.get('merged_at'),
                            'merge_commit': m.get('merge_commit_sha')})
            after = blob_id
        return out

    def comments(self, repo_id, issue):
        total = self._json('/repositories/%d/issues/%d' % (repo_id, issue))['comments']
        out, page = [], 1
        while True:
            cs = self._json('/repositories/%d/issues/%d/comments?per_page=100&page=%d' % (repo_id, issue, page))
            for c in cs:
                q = ('query($id:ID!){node(id:$id){... on IssueComment{isMinimized lastEditedAt '
                     'userContentEdits(first:100){totalCount nodes{diff editedAt}}}}}')
                d = self._graphql(q, {'id': c['node_id']})['node']
                if d['userContentEdits']['totalCount'] > len(d['userContentEdits']['nodes']):
                    raise HostUnavailable('edit history incomplete for comment %d' % c['id'])
                edits = [n['diff'] for n in d['userContentEdits']['nodes'] if n.get('diff') is not None]
                out.append({'id': c['id'], 'author_id': c['user']['id'], 'author_login': c['user']['login'],
                            'created_at': c['created_at'], 'body': c['body'],
                            'edited': bool(d['lastEditedAt']) or c['updated_at'] != c['created_at'],
                            'edits': edits, 'hidden': bool(d['isMinimized'])})
            if not cs:
                break
            page += 1
        return out, total

    def deletion_events(self, repo_id, issue):
        return None

    def runs_for(self, repo_id, head_sha):
        runs = self._json('/repositories/%d/actions/runs?head_sha=%s&per_page=100' % (repo_id, head_sha))
        out = []
        for r in runs.get('workflow_runs', []):
            jobs = self._json('/repositories/%d/actions/runs/%d/jobs?per_page=100' % (repo_id, r['id']))
            out.append({'run_id': r['id'], 'workflow_path': r['path'].split('@', 1)[0], 'head_sha': r['head_sha'],
                        'conclusion': r.get('conclusion'),
                        'jobs': [{'id': j['id'], 'name': j['name'], 'conclusion': j.get('conclusion')}
                                 for j in jobs.get('jobs', [])],
                        'result': None, 'artifact_sha256': None})
        return out or None

    def artifact_sha256(self, repo_id, run_id, name):
        arts = self._json('/repositories/%d/actions/runs/%d/artifacts' % (repo_id, run_id))['artifacts']
        for a in arts:
            if a['name'] == name and (a.get('digest') or '').startswith('sha256:'):
                return a['digest'][7:]
        return None


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def b64(b):
    return base64.b64encode(b).decode()


def environment():
    return dict(os.environ)
