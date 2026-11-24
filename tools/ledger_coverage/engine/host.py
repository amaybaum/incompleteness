"""The host records the tool reads (sec. 6.3, "Host reads"): GitHub Actions runs, their jobs and their artifacts,
through the host's REST API, each with a GET. No comment, Issue, pull request, branch, commit listing, tree or file
content is read through the host, and its GraphQL API is not used.

Two implementations: `RestHost`, which reads the host's interface inside a host job and is never used outside one, and
`MemoryHost`, an in-memory host for controls. Nothing here writes to any host.
"""
import hashlib
import json
import os
import urllib.error
import urllib.request


class HostUnavailable(Exception):
    pass


class MemoryHost:
    """A deterministic in-memory host: run records {run id: record}, the runs of each commit with their jobs, and
    artifacts {(run id, name): sha256}. A name in `fail` makes that read fail ('run', 'runs', 'artifacts'); a name in
    `incomplete` makes it return an incomplete record."""

    def __init__(self):
        self.runs = {}
        self.host_runs = {}
        self.artifacts = {}
        self.fail = set()
        self.incomplete = set()

    def _need(self, what):
        if what in self.fail:
            raise HostUnavailable('host call failed: %s' % what)

    def run_record(self, run_id, repo_id=None):
        self._need('run')
        r = self.runs.get(run_id)
        if r is None:
            return None
        r = dict(r, run_id=run_id)
        if 'run' in self.incomplete:
            r.pop('head_repository_id', None)
        return r

    def runs_for(self, repo_id, head_sha):
        self._need('runs')
        got = [dict(r) for r in self.host_runs.get(head_sha, [])]
        if 'runs' in self.incomplete:
            got = [{k: v for k, v in r.items() if k != 'jobs'} for r in got]
        return got or None

    def artifact_sha256(self, repo_id, run_id, name):
        self._need('artifacts')
        if 'artifacts' in self.incomplete:
            return None
        return self.artifacts.get((run_id, name))


class RestHost:
    """Reads the host's REST records of Actions runs with the job token. Used only inside a host job.

    Every read goes through `transport(url, headers)`, which returns (body bytes, headers) or raises HostUnavailable;
    by default it is an https GET request. `max_calls` bounds the reads of one instance: a read beyond it raises
    HostUnavailable (fail-closed). A record that lacks a field the tool reads raises HostUnavailable."""

    def __init__(self, api, token, transport=None, max_calls=2000):
        self.api = api.rstrip('/')
        self.token = token
        self.transport = transport or self._https_get
        self.max_calls = max_calls
        self.calls = 0

    @staticmethod
    def detect(env):
        """(host, run id, repository id) of the job the tool runs in, from the job's own environment; None outside
        a host job."""
        if env.get('GITHUB_ACTIONS') != 'true' or not env.get('GITHUB_RUN_ID') or not env.get('GITHUB_TOKEN') or \
                not env.get('GITHUB_REPOSITORY_ID'):
            return None
        try:
            run_id, repo_id = int(env['GITHUB_RUN_ID']), int(env['GITHUB_REPOSITORY_ID'])
        except ValueError:
            return None
        return RestHost(env.get('GITHUB_API_URL', 'https://api.github.com'), env['GITHUB_TOKEN']), run_id, repo_id

    def _https_get(self, url, headers):
        req = urllib.request.Request(url, headers=headers, method='GET')
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read(), r.headers
        except (urllib.error.URLError, OSError) as exc:
            raise HostUnavailable(str(exc))

    def _get(self, url):
        self.calls += 1
        if self.calls > self.max_calls:
            raise HostUnavailable('more than %d host reads' % self.max_calls)
        return self.transport(url if url.startswith('http') else self.api + url,
                              {'Authorization': 'Bearer ' + self.token, 'Accept': 'application/vnd.github+json',
                               'X-GitHub-Api-Version': '2022-11-28'})

    def _json(self, url):
        data, _ = self._get(url)
        try:
            return json.loads(data.decode('utf-8'))
        except (ValueError, UnicodeDecodeError) as exc:
            raise HostUnavailable('unreadable host record: %s' % exc)

    @staticmethod
    def _run(r):
        try:
            return {'run_id': r['id'], 'repository_id': r['repository']['id'],
                    'head_repository_id': r['head_repository']['id'], 'event': r['event'],
                    'head_branch': r['head_branch'], 'workflow_path': r['path'].split('@', 1)[0],
                    'head_sha': r['head_sha'], 'conclusion': r.get('conclusion'),
                    'repository_url': r['repository'].get('html_url')}
        except (KeyError, TypeError, AttributeError) as exc:
            raise HostUnavailable('incomplete run record: %s' % exc)

    def run_record(self, run_id, repo_id):
        return self._run(self._json('/repositories/%d/actions/runs/%d' % (repo_id, run_id)))

    def runs_for(self, repo_id, head_sha):
        runs = self._json('/repositories/%d/actions/runs?head_sha=%s&per_page=100' % (repo_id, head_sha))
        if not isinstance(runs.get('workflow_runs'), list) or runs.get('total_count', 0) > len(runs['workflow_runs']):
            raise HostUnavailable('incomplete run listing for %s' % head_sha[:12])
        out = []
        for r in runs['workflow_runs']:
            rec = self._run(r)
            jobs = self._json('/repositories/%d/actions/runs/%d/jobs?per_page=100' % (repo_id, r['id']))
            if not isinstance(jobs.get('jobs'), list) or jobs.get('total_count', 0) > len(jobs['jobs']):
                raise HostUnavailable('incomplete job listing for run %d' % r['id'])
            rec.update(jobs=[{'id': j['id'], 'name': j['name'], 'conclusion': j.get('conclusion')}
                             for j in jobs['jobs']], result=None, artifact_sha256=None)
            out.append(rec)
        return out or None

    def artifact_sha256(self, repo_id, run_id, name):
        doc = self._json('/repositories/%d/actions/runs/%d/artifacts' % (repo_id, run_id))
        if not isinstance(doc.get('artifacts'), list):
            raise HostUnavailable('incomplete artifact listing for run %d' % run_id)
        for a in doc['artifacts']:
            if a.get('name') == name and (a.get('digest') or '').startswith('sha256:'):
                return a['digest'][7:]
        return None


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def environment():
    return dict(os.environ)
