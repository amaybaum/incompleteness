#!/usr/bin/env python3
"""Preserve the CI logs of cited runs, read-only, and record exactly what was received.

    python3 -I fetch_ci_logs.py --self-test                                    # local servers only, no network
    python3 -I fetch_ci_logs.py --runs batch.csv --jobs inventory-jobs.csv --out ci-logs [--job-logs cited|all]
    python3 -I fetch_ci_logs.py --out ci-logs --manifest                       # re-hash everything, write manifest.json
    python3 -I fetch_ci_logs.py --out ci-logs --complete --runs batch.csv --jobs inventory-jobs.csv [--job-logs ...]
    python3 -I fetch_ci_logs.py --out ci-logs --scan                           # credential-shaped text, location only

The token is read from GH_TOKEN (or GITHUB_TOKEN) and needs `actions: read` on amaybaum/incompleteness.

Per run, in the order of the runs CSV (its `rank` column when it has one):
  1. GET repos/<repo>/actions/runs/<id>: its head_sha, which must equal the inventory's, and its run_attempt.
  2. For each attempt n = 1 .. run_attempt:
     - GET .../runs/<id>/attempts/<n>/jobs (every page): each job's id, name, status, conclusion, head_sha,
       start, end and runner;
     - GET .../runs/<id>/attempts/<n>/logs: the attempt's log zip, stored as runs/<id>/attempt-<n>.zip. It is
       complete when it passes its CRC test and its top-level job logs (`<k>_<name>.txt` or `-<id>_<name>.txt`)
       number the jobs the attempt ran: completed, neither skipped nor without a conclusion, not cancelled before a
       runner took them, and not copies a partial re-run made of an earlier attempt's jobs (see rerun()).
  3. Each cited job of the run (from the jobs CSV), and with --job-logs all every job that ran in any attempt, copies
     included:
     GET repos/<repo>/actions/jobs/<job_id>/logs, the job's plain-text log, stored as jobs/<job_id>.txt.

How downloads are made: the two log endpoints answer with a redirect to a short-lived download link. Redirects are
never followed automatically. The link is fetched at once in a second request that carries no credentials, and
the link, its host's path and its query are never recorded or printed; an error records the host only. The token
is attached only to requests for the API host, and a request that would carry it anywhere else is refused.

Every request outcome appends one JSON line to fetch-log.jsonl: what was asked, the outcome (archived; ok for
metadata; unavailable, with the host's status, 404 or 410; failed, with the error), and for an archived file its
size and sha256, and for a zip each member's name, size and sha256. Stored files are never overwritten or
deleted: an archived item is skipped on a later pass, so an interrupted pass resumes, and a file stored without a
log line is recorded from its bytes.

--manifest re-hashes every stored file against fetch-log.jsonl and writes manifest.json. --complete lists every
item the batch requires and its state in completeness.json, and exits 1 unless every one is present and complete.
--scan reports file, member and line of credential-shaped text in every file, metadata included, never the text,
and exits 1 on any hit. A clean scan is a scan, not a guarantee.

What a downloaded file is: the bytes GitHub served for that endpoint, byte for byte. GitHub may have masked
registered secrets as *** before serving; nothing is redacted by this tool."""
import argparse, contextlib, csv, datetime as dt, hashlib, http.server, io, json, os, re, socket, sys, tempfile, threading, time
import urllib.error, urllib.parse, urllib.request, zipfile

REPO = 'amaybaum/incompleteness'
API = 'https://api.github.com'
ORDER = {'A': 0, 'B': 1, 'J': 2, 'C': 3}
SECRETS = [re.compile(p) for p in (
    r'gh[pousr]_[A-Za-z0-9._-]{36,}',                                   # GitHub tokens, the ghs_<app>_<jwt> form included
    r'github_pat_[A-Za-z0-9_]{50,}', r'AKIA[0-9A-Z]{16}', r'-----BEGIN [A-Z ]*PRIVATE KEY-----', r'xox[abprs]-[A-Za-z0-9-]{10,}',
    r'(?i)\b(authorization|bearer)\b[:= ]+[A-Za-z0-9._~+/-]{20,}',
    r'(?i)\bauthorization\b[:= ]+(basic|token|bearer)\s+[A-Za-z0-9._~+/=-]{16,}',
    r'sk-[A-Za-z0-9]{32,}', r'sk-(ant|proj)-[A-Za-z0-9_-]{20,}', r'npm_[A-Za-z0-9]{36}', r'pypi-[A-Za-z0-9_-]{50,}',
    r'AIza[0-9A-Za-z_-]{35}',
    r'(?i)[?&](sig|signature|se|sv|skoid)=[A-Za-z0-9%._-]{16,}', r'(?i)x-amz-signature=[0-9a-f]{16,}',
    r'(?i)urlsignature=[A-Za-z0-9%._-]{16,}',
    r'eyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}')]                    # JWTs, the Actions runtime token among them
TOP = re.compile(r'^-?\d+_.+\.txt$')  # a top-level job log in an attempt's zip, <k>_<name>.txt or -<id>_<name>.txt
URL = re.compile(r'https?://[^\s"\'<>]+')


def scrub(text):
    """Text with every URL replaced by its host, so no download link, signed or not, is ever recorded."""
    def host(m):
        try:
            return '<url on %s>' % urllib.parse.urlsplit(m.group(0)).netloc
        except ValueError:
            return '<url>'
    return URL.sub(host, text)


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')


def sha(b):
    return hashlib.sha256(b).hexdigest()


class Gone(Exception):
    """The host answered 404 or 410: it no longer serves the item."""


class Failed(Exception):
    """Anything else that kept the item from being read."""


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None  # urllib then raises HTTPError with the 3xx response, which Http handles itself


class Http:
    """The only network code. The token goes only on requests to the API host; no redirect is followed
    automatically; a redirect's target is fetched without credentials and never recorded."""

    def __init__(self, base=API, token=None, proxies=None, tries=3, pause=2.0, budget=900, link_schemes=('https',)):
        self.base = base.rstrip('/')
        self.host = urllib.parse.urlsplit(self.base).netloc
        self.token, self.tries, self.pause = token, tries, pause
        self.budget, self.api_calls, self.link_schemes = budget, 0, link_schemes
        handlers = [_NoRedirect()] + ([urllib.request.ProxyHandler(proxies)] if proxies is not None else [])
        self.opener = urllib.request.build_opener(*handlers)

    def _once(self, url, auth, accept):
        if auth and urllib.parse.urlsplit(url).netloc != self.host:
            raise Failed('refused to send the token to %s' % urllib.parse.urlsplit(url).netloc)
        req = urllib.request.Request(url, headers={'User-Agent': 'oi-log-archiver', 'Accept': accept})
        if auth:
            if not self.token:
                raise Failed('no token: set GH_TOKEN')
            req.add_unredirected_header('Authorization', 'Bearer ' + self.token)
            req.add_unredirected_header('X-GitHub-Api-Version', '2022-11-28')
        try:
            with self.opener.open(req, timeout=300) as r:
                return r.status, r.headers, r.read()
        except urllib.error.HTTPError as e:
            try:
                body = e.read() if auth else b''  # a download host's error body is never kept
            except Exception:
                body = b''
            return e.code, e.headers, body
        except (urllib.error.URLError, OSError) as ex:
            where = 'the API' if auth else 'the download host %s' % (urllib.parse.urlsplit(url).hostname or '?')
            raise ConnectionError('network error at %s: %s' % (where, scrub(type(ex).__name__)))

    def _get(self, url, auth, accept):
        """One request, retried on a network error or a 5xx; returns (status, headers, body)."""
        last = None
        for k in range(self.tries):
            try:
                code, headers, body = self._once(url, auth, accept)
            except ConnectionError as ex:
                last = str(ex)
            else:
                if code < 500:
                    return code, headers, body
                last = 'HTTP %d from %s' % (code, 'the API' if auth else 'the download host')
            if k + 1 < self.tries:
                time.sleep(self.pause * (k + 1))
        raise Failed(last + ' (after %d tries)' % self.tries)

    def _api(self, url, accept):
        if self.api_calls >= self.budget:  # GITHUB_TOKEN allows about 1000 requests an hour; a spent budget fails closed
            raise Failed('the API request budget of this pass (%d) is spent' % self.budget)
        self.api_calls += 1
        code, headers, body = self._get(url, True, accept)
        if code in (404, 410):
            raise Gone('HTTP %d from the API' % code)
        if code in (403, 429) and headers.get('x-ratelimit-remaining') == '0':
            raise Failed('rate limited by the API (resets at %s)' % headers.get('x-ratelimit-reset', '?'))
        return code, headers, body

    def json(self, path):
        code, _, body = self._api(self.base + '/' + path, 'application/vnd.github+json')
        if code != 200:
            raise Failed('HTTP %d from the API' % code)
        return json.loads(body)

    def json_pages(self, path):
        """Every page of a list endpoint, following Link rel="next" only to the API host."""
        url, docs = self.base + '/' + path, []
        while url:
            code, headers, body = self._api(url, 'application/vnd.github+json')
            if code != 200:
                raise Failed('HTTP %d from the API' % code)
            docs.append(json.loads(body))
            m = re.search(r'<([^>]+)>;\s*rel="next"', headers.get('Link', '') or '')
            url = m.group(1) if m else None
            if url and urllib.parse.urlsplit(url).netloc != self.host:
                raise Failed('a next-page link to another host, not followed')
        return docs

    def download(self, path):
        """An API endpoint answering with a redirect to a download link: the link is fetched at once, with no
        credentials, and neither the link nor its query is kept."""
        code, headers, body = self._api(self.base + '/' + path, 'application/vnd.github+json')
        if code == 200:
            return body
        if code not in (301, 302, 303, 307, 308) or not headers.get('Location'):
            raise Failed('HTTP %d from the API' % code)
        try:
            link = urllib.parse.urljoin(self.base + '/', headers['Location'])
            parts = urllib.parse.urlsplit(link)
            host = parts.hostname or '?'
        except Exception:
            raise Failed('an unreadable download link from the API')
        if parts.scheme not in self.link_schemes:
            raise Failed('a download link on %s that is not https, not followed' % host)
        try:
            code, _, body = self._get(link, False, '*/*')
        except Failed:
            raise
        except Exception as ex:  # e.g. http.client.InvalidURL, whose message quotes the link: only its type is kept
            raise Failed('%s at the download host %s' % (type(ex).__name__, host))
        if code in (301, 302, 303, 307, 308):
            raise Failed('a second redirect from the download host %s, not followed' % host)
        if code != 200:
            raise Failed('HTTP %d from the download host %s' % (code, host))
        return body


def attempt(fn):
    try:
        return fn(), 'ok', ''
    except Gone as ex:
        return None, 'unavailable', str(ex)
    except Failed as ex:
        return None, 'failed', scrub(str(ex))[:500]
    except Exception as ex:  # anything unforeseen is recorded as a failure, never echoed with a URL
        return None, 'failed', scrub('%s: %s' % (type(ex).__name__, ex))[:500]


def load_runs(path):
    rows = list(csv.DictReader(open(path, newline='')))
    for r in rows:
        assert r['run_id'].isdigit() and r['tier'] in ORDER, r
    if rows and 'rank' in rows[0]:  # an explicit ranking (priority-388.csv, a batch) is followed as given
        rows.sort(key=lambda r: int(r['rank']))
    else:
        rows.sort(key=lambda r: (r.get('r1_entry', '') != '', ORDER[r['tier']], r['created_at'], r['run_id']))
    return rows


def load_jobs(path):
    by_run = {}
    if path:
        for r in csv.DictReader(open(path, newline='')):
            assert r['job_id'].isdigit() and r['run_id'].isdigit(), r
            by_run.setdefault(r['run_id'], []).append(r['job_id'])
    return by_run


def ran(jobs):
    """Jobs that ran: completed, neither skipped nor without a conclusion, and not cancelled before a runner took them."""
    return [j for j in jobs if j['status'] == 'completed' and j['conclusion'] not in ('skipped', None)
            and not (j['conclusion'] == 'cancelled' and not j.get('runner_id'))]


def rerun(jobs, earlier):
    """The jobs of an attempt that ran in it. A partial re-run lists the jobs it did not re-run as copies of an earlier
    attempt's, under new ids but with the same name, start, end and runner; its log zip holds only the jobs it re-ran
    (GitHub docs, "Using workflow run logs"). earlier is every job of the earlier attempts, or None if one is unread."""
    if earlier is None:
        return None
    sig = lambda j: (j['name'], j.get('started_at'), j.get('completed_at'), j.get('runner_id'))
    seen = {sig(j) for j in earlier if j.get('started_at')}
    return [j for j in ran(jobs) if sig(j) not in seen]


class Store:
    def __init__(self, out):
        self.out = out
        os.makedirs(out, exist_ok=True)
        self.path = os.path.join(out, 'fetch-log.jsonl')
        self.done = {}
        if os.path.exists(self.path):
            for line in open(self.path):
                if line.strip():
                    e = json.loads(line)
                    self.done[e['key']] = e
        self.fh = open(self.path, 'a')

    def log(self, e):
        e['logged_at'] = now()
        self.fh.write(json.dumps(e, sort_keys=True) + '\n')
        self.fh.flush()
        self.done[e['key']] = e
        return e


def zip_info(blob):
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        bad = z.testzip()
        members = [{'name': i.filename, 'size': i.file_size, 'sha256': sha(z.read(i))} for i in z.infolist() if not i.is_dir()]
    top = [m['name'] for m in members if '/' not in m['name'] and TOP.match(m['name'])]
    return bad, members, top


def store_file(st, key, rel, blob, extra):
    dest = os.path.join(st.out, rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    assert not os.path.exists(dest), dest  # never overwrite a stored file
    tmp = dest + '.part'
    open(tmp, 'wb').write(blob)
    os.replace(tmp, dest)
    return st.log({'key': key, 'outcome': 'archived', 'path': rel, 'bytes': len(blob), 'sha256': sha(blob), **extra})


def zip_record(blob, n_logs):
    """n_logs is the number of jobs the attempt re-ran, whose logs its zip must hold; None when it is not known."""
    bad, members, top = zip_info(blob)
    return {'crc_ok': bad is None, 'members': members, 'top_level_job_logs': len(top), 'logs_expected': n_logs,
            'complete': bad is None and n_logs is not None and len(top) == n_logs}


def recover_unlogged(st, key, rel, extra, n_logs=None):
    """A file a pass stored before it could log it: record it from its bytes, never refetch over it."""
    blob = open(os.path.join(st.out, rel), 'rb').read()
    e = {'key': key, 'outcome': 'archived', 'path': rel, 'bytes': len(blob), 'sha256': sha(blob), **extra,
         'detail': 'recorded from a file an interrupted pass stored without logging it'}
    if rel.endswith('.zip'):
        e.update(zip_record(blob, n_logs))
    return st.log(e)


def fetch(runs, jobs_by_run, out, http, job_logs='cited'):
    st = Store(out)
    n = {'archived': 0, 'unavailable': 0, 'failed': 0, 'skipped': 0, 'mismatch': 0}

    def counted(e):
        n[e['outcome'] if e['outcome'] in n else 'failed'] += 1
        return e

    for r in runs:
        rid = r['run_id']
        base = {'run_id': rid, 'tier': r['tier'], 'r1_entry': r.get('r1_entry', ''), 'inventory_head_sha': r['head_sha'],
                'created_at': r['created_at']}
        key = 'run:%s' % rid
        meta = st.done.get(key)
        if not meta or meta['outcome'] != 'ok':
            d, oc, err = attempt(lambda: http.json('repos/%s/actions/runs/%s' % (REPO, rid)))
            if oc != 'ok':
                counted(st.log({'key': key, **base, 'outcome': oc, 'detail': err}))
                continue
            meta = st.log({'key': key, **base, 'outcome': 'ok', 'run_attempt': d.get('run_attempt', 1),
                           'head_sha': d.get('head_sha'), 'event': d.get('event'), 'conclusion': d.get('conclusion'),
                           'head_matches_inventory': d.get('head_sha') == r['head_sha']})
            if not meta['head_matches_inventory']:
                n['mismatch'] += 1
        want = list(jobs_by_run.get(rid, []))
        for att in range(1, int(meta['run_attempt']) + 1):
            jkey = 'jobs:%s:%d' % (rid, att)
            jl = st.done.get(jkey)
            if not jl or jl['outcome'] != 'ok':
                docs, oc, err = attempt(lambda: http.json_pages(
                    'repos/%s/actions/runs/%s/attempts/%d/jobs?per_page=100' % (REPO, rid, att)))
                if oc != 'ok':  # the zip is still fetched; without the job list it cannot count as complete
                    jl = counted(st.log({'key': jkey, 'run_id': rid, 'attempt': att, 'outcome': oc, 'detail': err}))
                else:
                    jobs = [{'id': str(j['id']), 'name': j['name'], 'status': j.get('status'), 'conclusion': j.get('conclusion'),
                             'head_sha': j.get('head_sha'), 'started_at': j.get('started_at'),
                             'completed_at': j.get('completed_at'), 'runner_id': j.get('runner_id')}
                            for d in docs for j in d.get('jobs', [])]
                    jl = st.log({'key': jkey, 'run_id': rid, 'attempt': att, 'outcome': 'ok', 'jobs': jobs})
            lists = [st.done.get('jobs:%s:%d' % (rid, a)) for a in range(1, att + 1)]
            earlier = None if any(l is None or l['outcome'] != 'ok' for l in lists) else [j for l in lists[:-1] for j in l['jobs']]
            again = rerun(jl['jobs'], earlier) if jl['outcome'] == 'ok' else None
            n_logs = len(again) if again is not None else None
            if job_logs == 'all' and jl['outcome'] == 'ok':
                want += [j['id'] for j in ran(jl['jobs']) if j['id'] not in want]
            zkey, rel = 'zip:%s:%d' % (rid, att), 'runs/%s/attempt-%d.zip' % (rid, att)
            if st.done.get(zkey, {}).get('outcome') == 'archived' and os.path.exists(os.path.join(out, rel)):
                n['skipped'] += 1
            elif os.path.exists(os.path.join(out, rel)):
                counted(recover_unlogged(st, zkey, rel, {'run_id': rid, 'attempt': att}, n_logs))
            else:
                blob, oc, err = attempt(lambda: http.download('repos/%s/actions/runs/%s/attempts/%d/logs' % (REPO, rid, att)))
                if oc == 'ok' and blob[:2] == b'PK':
                    rec, zoc, zerr = attempt(lambda: zip_record(blob, n_logs))
                    if zoc != 'ok':
                        rec = {'crc_ok': False, 'complete': False, 'logs_expected': n_logs, 'detail': 'unreadable zip: ' + zerr}
                    e = counted(store_file(st, zkey, rel, blob, {'run_id': rid, 'attempt': att, **rec}))
                    if not e['complete']:
                        n['mismatch'] += 1
                else:
                    counted(st.log({'key': zkey, 'run_id': rid, 'attempt': att, 'outcome': oc if oc != 'ok' else 'failed',
                                    'detail': err or 'the response was not a zip (%d bytes)' % len(blob or b'')}))
        for jid in want:
            jkey, rel = 'joblog:%s' % jid, 'jobs/%s.txt' % jid
            if st.done.get(jkey, {}).get('outcome') == 'archived' and os.path.exists(os.path.join(out, rel)):
                n['skipped'] += 1
                continue
            if os.path.exists(os.path.join(out, rel)):
                counted(recover_unlogged(st, jkey, rel, {'run_id': rid, 'job_id': jid}))
                continue
            blob, oc, err = attempt(lambda: http.download('repos/%s/actions/jobs/%s/logs' % (REPO, jid)))
            if oc == 'ok' and not blob:
                oc, err = 'failed', 'the host served an empty job log'
            if oc == 'ok':
                counted(store_file(st, jkey, rel, blob, {'run_id': rid, 'job_id': jid, 'lines': blob.count(b'\n')}))
            else:
                counted(st.log({'key': jkey, 'run_id': rid, 'job_id': jid, 'outcome': oc, 'detail': err}))
        print(rid, r['tier'], file=sys.stderr)
    return n


def manifest(out):
    st = Store(out)
    bad, items = [], []
    for k, e in sorted(st.done.items()):
        if e['outcome'] == 'archived':
            p = os.path.join(out, e['path'])
            b = open(p, 'rb').read() if os.path.exists(p) else None
            if b is None or sha(b) != e['sha256'] or len(b) != e['bytes']:
                bad.append(e['path'])
            elif e['path'].endswith('.zip') and 'members' in e and attempt(lambda: zip_info(b)[1])[0] != e['members']:
                bad.append(e['path'])
        items.append(e)
    cnt = lambda kind, oc: sum(1 for e in items if e['key'].startswith(kind) and e['outcome'] == oc)
    m = {'repository': REPO, 'written_at': now(), 'items': items, 'rehash_mismatches': bad,
         'counts': {'runs_read': cnt('run:', 'ok'), 'zips_archived': cnt('zip:', 'archived'), 'job_logs_archived': cnt('joblog:', 'archived'),
                    'unavailable': sum(1 for e in items if e['outcome'] == 'unavailable'),
                    'failed': sum(1 for e in items if e['outcome'] == 'failed'),
                    'zips_incomplete': sum(1 for e in items if e['key'].startswith('zip:') and e.get('complete') is False),
                    'head_mismatches': sum(1 for e in items if e['key'].startswith('run:') and e.get('head_matches_inventory') is False)},
         'what_this_is': 'the log files GitHub served for these runs and jobs, byte for byte as received, with their digests; '
                         'an item the host no longer serves is recorded as unavailable with the host\'s answer'}
    json.dump(m, open(os.path.join(out, 'manifest.json'), 'w'), indent=1, sort_keys=True)
    return m


def completeness(out, runs, jobs_by_run, job_logs='cited'):
    """Every item the batch requires, and whether it is present and complete; written to completeness.json."""
    st, items = Store(out), []

    def need(key, ok, state):
        items.append({'key': key, 'ok': ok, 'state': state})

    def stored(e):
        p = os.path.join(out, e['path'])
        return os.path.exists(p) and os.path.getsize(p) == e['bytes'] and sha(open(p, 'rb').read()) == e['sha256']

    for r in runs:
        rid = r['run_id']
        meta = st.done.get('run:%s' % rid)
        if not meta or meta['outcome'] != 'ok':
            need('run:%s' % rid, False, meta['outcome'] + ': ' + meta.get('detail', '') if meta else 'no record')
            continue
        head_ok = meta['head_sha'] == r['head_sha']
        need('run:%s' % rid, head_ok, 'ok' if head_ok else 'head %s differs from the inventory\'s %s' % (meta['head_sha'], r['head_sha']))
        want = list(jobs_by_run.get(rid, []))
        for att in range(1, int(meta['run_attempt']) + 1):
            jl = st.done.get('jobs:%s:%d' % (rid, att))
            if not jl or jl['outcome'] != 'ok':
                need('jobs:%s:%d' % (rid, att), False, jl['outcome'] + ': ' + jl.get('detail', '') if jl else 'no record')
            else:
                need('jobs:%s:%d' % (rid, att), True, 'ok')
                if job_logs == 'all':
                    want += [j['id'] for j in ran(jl['jobs']) if j['id'] not in want]
            z = st.done.get('zip:%s:%d' % (rid, att))
            if not z or z['outcome'] != 'archived':
                need('zip:%s:%d' % (rid, att), False, z['outcome'] + ': ' + z.get('detail', '') if z else 'no record')
            elif not stored(z):
                need('zip:%s:%d' % (rid, att), False, 'stored file missing or changed')
            elif not z.get('complete'):
                need('zip:%s:%d' % (rid, att), False, 'incomplete: crc_ok %s, %s top-level job logs for %s job(s) re-run in the attempt' % (
                    z.get('crc_ok'), z.get('top_level_job_logs'), z.get('logs_expected')))
            else:
                need('zip:%s:%d' % (rid, att), True, 'ok')
        for jid in want:
            j = st.done.get('joblog:%s' % jid)
            if not j or j['outcome'] != 'archived':
                need('joblog:%s' % jid, False, j['outcome'] + ': ' + j.get('detail', '') if j else 'no record')
            elif not stored(j):
                need('joblog:%s' % jid, False, 'stored file missing or changed')
            elif not j['bytes']:
                need('joblog:%s' % jid, False, 'an empty job log')
            else:
                need('joblog:%s' % jid, True, 'ok')
    c = {'complete': bool(items) and all(i['ok'] for i in items), 'required': len(items),
         'missing_or_incomplete': [i for i in items if not i['ok']], 'items': items, 'job_logs': job_logs}
    json.dump(c, open(os.path.join(out, 'completeness.json'), 'w'), indent=1, sort_keys=True)
    return c


def scan(out):
    hits = []
    for root, _, files in os.walk(out):
        for f in sorted(files):
            p = os.path.join(root, f)
            rel = os.path.relpath(p, out)
            if rel == 'scan.json':
                continue
            raw = open(p, 'rb').read()
            texts = [('', raw)]
            if raw[:2] == b'PK':
                try:
                    with zipfile.ZipFile(io.BytesIO(raw)) as z:
                        texts += [(i.filename, z.read(i)) for i in z.infolist() if not i.is_dir()]
                except Exception:
                    hits.append({'file': rel, 'member': '', 'line': 0, 'pattern': 'unreadable zip: not scanned'})
            for member, b in texts:
                for k, line in enumerate(b.decode('utf-8', 'replace').split('\n'), 1):
                    for rx in SECRETS:
                        if rx.search(line):
                            hits.append({'file': rel, 'member': member, 'line': k, 'pattern': rx.pattern})
    json.dump(hits, open(os.path.join(out, 'scan.json'), 'w'), indent=1)
    return hits


# ---------------------------------------------------------------------------------------------------------- self-test
TOKEN = 'ghs_' + 'T' * 36  # a token-shaped string the servers check for; never a real credential


class _Server:
    """A local HTTP server answering from a function; it records every request's path and headers."""

    def __init__(self, answer):
        seen = self.seen = []

        class H(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                seen.append((self.path, {k.lower(): v for k, v in self.headers.items()}))
                code, headers, body = answer(self.path, self.headers)
                self.send_response(code)
                for k, v in headers.items():
                    self.send_header(k, v)
                self.send_header('Content-Length', str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, *a):
                pass

        self.srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), H)
        self.url = 'http://127.0.0.1:%d' % self.srv.server_address[1]
        threading.Thread(target=self.srv.serve_forever, daemon=True).start()

    def close(self):
        self.srv.shutdown()
        self.srv.server_close()


def _zip(names, extra=''):
    b = io.BytesIO()
    with zipfile.ZipFile(b, 'w') as f:
        for i, nm in enumerate(names):
            f.writestr('%d_%s.txt' % (i, nm), 'log of %s\n%s' % (nm, extra))
            f.writestr('%s/1_Set up job.txt' % nm, 'setup\n')
    return b.getvalue()


def _fixtures():
    """One credential-shaped string per SECRETS pattern, each matched by that pattern alone. Built from pieces, so
    the source holds no token-shaped literal."""
    return ['ghs_' + '1234567_' + 'ab.cd-ef_' * 5, 'github_' + 'pat_' + 'A1' * 30, 'AK' + 'IA' + 'ABCDEFGHIJKLMNOP',
            '-----BEGIN RSA ' + 'PRIVATE KEY-----', 'xo' + 'xb-' + '1234567890ab', 'Bea' + 'rer ' + 'x' * 24,
            'Authorization: Basic ' + 'QWxhZGRpbjpvcGVuIHNlc2FtZQ==', 'sk' + '-' + 'a' * 40, 'sk' + '-ant-api03_' + 'x' * 20,
            'np' + 'm_' + 'A' * 36, 'py' + 'pi-' + 'A' * 55, 'AI' + 'za' + 'B' * 35, '?si' + 'g=' + 'a' * 20,
            'X-Amz-Sig' + 'nature=' + 'abcdef0123456789' * 2, 'urlSig' + 'nature=' + 'a' * 20,
            'ey' + 'J' + 'h' * 12 + '.ey' + 'J' + 'p' * 12]


def _self_test_more():
    """Partial re-runs, every scan pattern and file kind, exit codes, and the download-link edge cases."""
    # every pattern has a fixture it alone matches, and the scan finds each in every kind of staged file
    fx = _fixtures()
    assert len(fx) == len(SECRETS)
    for k, f in enumerate(fx):
        assert [i for i, rx in enumerate(SECRETS) if rx.search(f)] == [k], ('fixture', k, f[:12])
    kinds = ['jobs/1.txt', 'manifest.json', 'completeness.json', 'fetch-log.jsonl', 'runs/1/attempt-1.zip']
    with tempfile.TemporaryDirectory() as d:
        for k, f in enumerate(fx):
            out = os.path.join(d, str(k))
            rel = kinds[k % len(kinds)]
            os.makedirs(os.path.dirname(os.path.join(out, rel)), exist_ok=True)
            if rel.endswith('.zip'):
                b = io.BytesIO()
                with zipfile.ZipFile(b, 'w', zipfile.ZIP_DEFLATED) as z:
                    z.writestr('0_build.txt', ('padding ' * 50 + f + '\n') * 3)
                assert f.encode() not in b.getvalue(), 'the member is compressed, so only the member scan can see it'
                open(os.path.join(out, rel), 'wb').write(b.getvalue())
            else:
                open(os.path.join(out, rel), 'w').write('line one\n' + f + '\n')
            hits = scan(out)
            want = {(rel, '0_build.txt')} if rel.endswith('.zip') else {(rel, '')}
            assert hits and {(h['file'], h['member']) for h in hits} == want, (k, rel, hits)
            assert main(['--out', out, '--scan']) == 1, 'the scan exits 1 on a hit'
        out = os.path.join(d, 'clean')
        os.makedirs(os.path.join(out, 'jobs'))
        open(os.path.join(out, 'jobs', '1.txt'), 'w').write('nothing here\n')
        assert main(['--out', out, '--scan']) == 0, 'a clean scan exits 0'
        open(os.path.join(out, 'broken.zip'), 'wb').write(b'PK\x03\x04 not a zip')
        assert [h['pattern'] for h in scan(out)] == ['unreadable zip: not scanned'], 'an unreadable zip counts as a hit'

    # a partial re-run: attempt 2 copies "build" from attempt 1 and re-runs "probes"; its zip holds only "probes"
    J = lambda i, nm, st, en, rn, c='success': {'id': i, 'name': nm, 'status': 'completed', 'conclusion': c,
                                                 'head_sha': 'h', 'started_at': st, 'completed_at': en, 'runner_id': rn}
    ATT = {('11', 1): [J(111, 'build', 'a', 'b', 1), J(112, 'probes', 'a', 'c', 2)],
           ('11', 2): [J(113, 'build', 'a', 'b', 1), J(114, 'probes', 'd', 'e', 3)],
           ('12', 1): [J(121, 'build', 'a', 'b', 1)], ('12', 2): [J(123, 'build', 'f', 'g', 4)],
           ('13', 1): [J(131, 'build', 'a', 'b', 1), J(132, 'never started', None, None, None, 'cancelled')],
           ('14', 1): [J(141, 'build', 'a', 'b', 1)], ('15', 1): [J(151, 'build', 'a', 'b', 1)]}
    ZIPS = {('11', 1): ['0_build.txt', '-1_probes.txt'], ('11', 2): ['0_probes.txt'], ('12', 1): ['0_build.txt'],
            ('12', 2): [], ('13', 1): ['0_build.txt'], ('14', 1): ['0_build.txt'], ('15', 1): ['0_build.txt']}

    def blob_answer(path, headers):
        seg = path.split('?')[0].strip('/').split('/')
        if seg[0] == 'Z':
            b = io.BytesIO()
            with zipfile.ZipFile(b, 'w') as z:
                for nm in ZIPS[(seg[1], int(seg[2]))]:
                    z.writestr(nm, 'log\n')
                z.writestr('build/1_Set up job.txt', 'setup\n')
            return 200, {}, b.getvalue()
        if seg[0] == 'L':
            return 200, {}, (b'' if seg[1] == '141' else b'job log\n')
        return 404, {}, b''

    blob = _Server(blob_answer)
    tail = '?sv=2025&sig=' + 'Q' * 30

    def api(path, headers):
        ep = path.split('?')[0].strip('/').split('/')
        js = lambda o: (200, {}, json.dumps(o).encode())
        if len(ep) == 6 and ep[4] == 'runs':
            return js({'run_attempt': 2 if ep[5] in ('11', '12') else 1, 'head_sha': 'h' + ep[5]})
        if len(ep) == 9 and ep[8] == 'jobs':
            return js({'jobs': ATT[(ep[5], int(ep[7]))]})
        if len(ep) == 9 and ep[8] == 'logs':
            if ep[5] == '14':
                return 302, {'Location': blob.url + '/a space/14' + tail}, b''      # urllib refuses it: InvalidURL
            return 302, {'Location': blob.url + '/Z/%s/%s' % (ep[5], ep[7]) + tail}, b''
        if len(ep) == 7 and ep[4] == 'jobs':
            if ep[5] == '151':
                return 410, {}, b''
            return 302, {'Location': blob.url + '/L/' + ep[5] + tail}, b''
        return 400, {}, b''

    srv = _Server(api)
    try:
        with tempfile.TemporaryDirectory() as d:
            rc, jc = os.path.join(d, 'runs.csv'), os.path.join(d, 'jobs.csv')
            with open(rc, 'w', newline='') as fh:
                w = csv.writer(fh)
                w.writerow(['rank', 'run_id', 'tier', 'created_at', 'head_sha'])
                w.writerows([[str(k), r, 'A', '2026-10-01', 'h' + r] for k, r in enumerate(['11', '12', '13', '14', '15'], 1)])
            with open(jc, 'w', newline='') as fh:
                w = csv.writer(fh)
                w.writerow(['job_id', 'run_id'])
                w.writerows([['141', '14'], ['151', '15']])
            out = os.path.join(d, 'out')
            h = Http(srv.url, TOKEN, proxies={}, tries=1, pause=0, link_schemes=('http',))
            fetch(load_runs(rc), load_jobs(jc), out, h, 'all')
            st = Store(out)
            z = lambda k: st.done[k]
            assert z('zip:11:1')['complete'] and z('zip:11:1')['top_level_job_logs'] == 2, 'the -<id>_<name>.txt form counts'
            assert z('zip:11:2')['complete'] and z('zip:11:2')['logs_expected'] == 1, 'a copied job is not expected in the zip'
            assert not z('zip:12:2')['complete'] and z('zip:12:2')['logs_expected'] == 1, 'a re-run job missing from the zip'
            assert z('zip:13:1')['complete'] and z('zip:13:1')['logs_expected'] == 1, 'a job cancelled before it started is not expected'
            assert {k for k in st.done if k.startswith('joblog:')} == {'joblog:111', 'joblog:112', 'joblog:113', 'joblog:114',
                                                                       'joblog:121', 'joblog:123', 'joblog:131', 'joblog:141',
                                                                       'joblog:151'}, 'every job that ran, copies included'
            e14 = z('zip:14:1')
            assert e14['outcome'] == 'failed' and 'InvalidURL' in e14['detail'], e14
            assert z('joblog:141')['outcome'] == 'failed' and 'empty' in z('joblog:141')['detail'], 'an empty job log fails'
            assert z('joblog:151')['outcome'] == 'unavailable'
            log = open(os.path.join(out, 'fetch-log.jsonl')).read()
            for leak in ('a space', '/Z/', '/L/', 'sig=', 'QQQQ', TOKEN):
                assert leak not in log, ('recorded a download link or the token', leak)
            args = ['--out', out, '--complete', '--runs', rc, '--jobs', jc, '--job-logs', 'all']
            assert main(args) == 1, 'an incomplete batch exits 1'
            bad = {i['key'] for i in completeness(out, load_runs(rc), load_jobs(jc), 'all')['missing_or_incomplete']}
            assert bad == {'zip:12:2', 'zip:14:1', 'joblog:141', 'joblog:151'}, sorted(bad)
            one = os.path.join(d, 'one.csv')
            with open(one, 'w', newline='') as fh:
                w = csv.writer(fh)
                w.writerow(['rank', 'run_id', 'tier', 'created_at', 'head_sha'])
                w.writerow(['1', '11', 'A', '2026-10-01', 'h11'])
            assert main(['--out', out, '--complete', '--runs', one, '--jobs', jc, '--job-logs', 'all']) == 0, 'a complete run exits 0'
            # every attempt is required: drop attempt 2's zip record, and run 11 is no longer complete
            lines = open(os.path.join(out, 'fetch-log.jsonl')).read().split('\n')
            open(os.path.join(out, 'fetch-log.jsonl'), 'w').write('\n'.join(l for l in lines if '"key": "zip:11:2"' not in l))
            assert main(['--out', out, '--complete', '--runs', one, '--jobs', jc, '--job-logs', 'all']) == 1, 'attempt 2 is required'
            # a link that is not https is refused under the production default
            h2 = Http(srv.url, TOKEN, proxies={}, tries=1, pause=0)
            _, oc, err = attempt(lambda: h2.download('repos/%s/actions/runs/11/attempts/1/logs' % REPO))
            assert oc == 'failed' and 'not https' in err and 'sig=' not in err, err
            # the API budget fails closed
            h3 = Http(srv.url, TOKEN, proxies={}, tries=1, pause=0, budget=2, link_schemes=('http',))
            n = fetch(load_runs(one), {}, os.path.join(d, 'budget'), h3, 'all')
            assert n['failed'] and 'budget' in json.dumps(Store(os.path.join(d, 'budget')).done), n
    finally:
        srv.close()
        blob.close()


def self_test():
    JOBS = {'1': [('11', 'build', 'success'), ('12', 'probes', 'success')], '2': [('21', 'build', 'failure')],
            '3': [('31', 'build', 'success'), ('32', 'skipped job', 'skipped')], '4': [('41', 'build', 'success')],
            '5': [('51', 'build', 'success'), ('52', 'probes', 'success')], '7': [('71', 'build', 'success')],
            '8': [('81', 'build', 'success')], '9': [('91', 'build', 'success')]}
    third = _Server(lambda p, h: (200, {}, b'third host'))

    def blob_answer(path, headers):
        seg = path.split('?')[0].strip('/').split('/')
        if seg[0] == 'again':
            return 302, {'Location': third.url + '/x?sig=' + 'S' * 30}, b''
        if seg[0] == 'missing':
            return 500, {}, b'download host error'
        if seg[0] == 'forbidden':
            return 403, {}, b'<Error>AuthenticationFailed: the signature has expired</Error>'
        if seg[0] == 'BLOBPATH':
            rid = seg[1]
            names = [nm for i, nm, c in JOBS[rid] if c != 'skipped']
            return 200, {}, _zip(names[:1] if rid == '1' else names, 'token ghp_' + 'a' * 36 if rid == '4' else '')
        if seg[0] == 'JOBPATH':
            return 200, {}, ('full log of job %s\n' % seg[1]).encode()
        return 404, {}, b''

    blob = _Server(blob_answer)
    signed = lambda p: '?sv=2025&se=2026&sp=r&sig=' + 'AbCdEf' + 'x' * 30

    def api(path, headers):
        if headers.get('Authorization') != 'Bearer ' + TOKEN:
            return 401, {}, b'{"message": "Bad credentials"}'
        ep = path.split('?')[0].strip('/').split('/')
        js = lambda o: (200, {'Content-Type': 'application/json'}, json.dumps(o).encode())
        if len(ep) == 6 and ep[4] == 'runs':                        # repos/o/r/actions/runs/<id>
            rid = ep[5]
            if rid == '6':
                return 404, {}, b'{"message": "Not Found"}'
            return js({'id': int(rid), 'run_attempt': 2 if rid == '3' else 1, 'event': 'push', 'conclusion': 'success',
                       'head_sha': 'deadbeef' if rid == '4' else 'h' + rid})
        if len(ep) == 9 and ep[8] == 'jobs':                        # .../runs/<id>/attempts/<n>/jobs
            rid = ep[5]
            att = ep[7]
            jobs = [{'id': int(i) if att == '1' else int(i) * 10 + int(att), 'name': nm, 'status': 'completed', 'conclusion': c, 'head_sha': 'h' + rid,
                     'started_at': 'S%s.%s' % (i, att), 'completed_at': 'E%s.%s' % (i, att), 'runner_id': int(i)}
                    for i, nm, c in JOBS[rid]]
            if 'page=2' in path:
                return js({'total_count': len(jobs), 'jobs': jobs[1:]})
            nxt = ('http://elsewhere.invalid' if rid == '9' else api_srv.url) + path.split('?')[0] + '?per_page=100&page=2'
            return 200, {'Content-Type': 'application/json', 'Link': '<%s>; rel="next"' % nxt}, json.dumps(
                {'total_count': len(jobs), 'jobs': jobs[:1]}).encode()
        if len(ep) == 9 and ep[8] == 'logs':                        # .../runs/<id>/attempts/<n>/logs
            rid = ep[5]
            if rid == '2':
                return 410, {}, b'{"message": "Gone"}'
            if rid == '5':
                return 302, {'Location': blob.url + '/missing/5' + signed(path)}, b''
            if rid == '7':
                return 302, {'Location': blob.url + '/again/7' + signed(path)}, b''
            if rid == '8':
                return 302, {'Location': blob.url + '/forbidden/8' + signed(path)}, b''
            return 302, {'Location': blob.url + '/BLOBPATH/%s/%s' % (rid, ep[7]) + signed(path)}, b''
        if len(ep) == 7 and ep[4] == 'jobs':                        # repos/o/r/actions/jobs/<job>/logs
            return 302, {'Location': blob.url + '/JOBPATH/%s' % ep[5] + signed(path)}, b''
        return 400, {}, b'{"message": "unknown endpoint"}'

    api_srv = _Server(api)
    try:
        http_ = Http(api_srv.url, TOKEN, proxies={}, tries=2, pause=0, link_schemes=('http',))
        with tempfile.TemporaryDirectory() as d:
            rc, jc = os.path.join(d, 'runs.csv'), os.path.join(d, 'jobs.csv')
            with open(rc, 'w', newline='') as fh:
                w = csv.writer(fh)
                w.writerow(['run_id', 'r1_entry', 'tier', 'created_at', 'head_sha'])
                w.writerows([['1', '', 'B', '2026-09-20', 'h1'], ['2', '', 'A', '2026-09-21', 'h2'], ['3', '', 'A', '2026-09-19', 'h3'],
                             ['4', 'ci-4', 'A', '2026-09-18', 'h4'], ['5', '', 'C', '2026-09-22', 'h5'], ['6', '', 'J', '2026-09-23', 'h6'],
                             ['7', 'ci-7', 'C', '2026-09-24', 'h7'], ['8', 'ci-8', 'C', '2026-09-24', 'h8'],
                             ['9', 'ci-9', 'C', '2026-09-25', 'h9']])
            with open(jc, 'w', newline='') as fh:
                w = csv.writer(fh)
                w.writerow(['job_id', 'run_id'])
                w.writerows([['11', '1'], ['31', '3']])
            out = os.path.join(d, 'out')
            runs = load_runs(rc)
            assert [r['run_id'] for r in runs] == ['3', '2', '1', '6', '5', '4', '7', '8', '9'], ('priority order', [r['run_id'] for r in runs])
            rk = os.path.join(d, 'ranked.csv')
            with open(rk, 'w', newline='') as fh:
                w = csv.writer(fh)
                w.writerow(['rank', 'run_id', 'r1_entry', 'tier', 'created_at', 'head_sha'])
                w.writerows([['1', '4', '', 'A', '2026-09-18', 'h4'], ['2', '1', '', 'B', '2026-09-20', 'h1']])
            assert [r['run_id'] for r in load_runs(rk)] == ['4', '1'], 'an explicit rank is followed'
            n = fetch(runs, load_jobs(jc), out, http_)
            # archived: zips of run 3 (2 attempts), 1, 4 = 4; job logs 11, 31 = 2. unavailable: run 2's zip (410), run 6 (404).
            # and run 9's zip, fetched without its job list. failed: run 5's zip (500 at the download host), run 7's zip
            # (a second redirect), run 8's zip (403 at the download host), run 9's job list (a next page on another host)
            assert n['archived'] == 7 and n['unavailable'] == 2 and n['failed'] == 4, n
            st = Store(out)
            assert st.done['run:4']['head_matches_inventory'] is False, 'a head that differs from the inventory is flagged'
            assert st.done['zip:1:1']['complete'] is False, 'a zip missing a job log is flagged incomplete'
            assert st.done['zip:3:1']['complete'] is True and st.done['zip:3:2']['complete'] is True, 'skipped jobs are not expected'
            assert st.done['jobs:3:1']['jobs'][1]['conclusion'] == 'skipped' and len(st.done['jobs:1:1']['jobs']) == 2, 'all pages read'
            assert 'second redirect' in st.done['zip:7:1']['detail'] and not third.seen, 'a second redirect is not followed'
            assert 'another host' in st.done['jobs:9:1']['detail'], 'a next-page link to another host is not followed'
            assert '500' in st.done['zip:5:1']['detail'] and '403' in st.done['zip:8:1']['detail'], (st.done['zip:5:1'], st.done['zip:8:1'])
            assert 'expired' not in st.done['zip:8:1']['detail'], 'a download host\'s error body is not kept'
            assert st.done['zip:9:1']['complete'] is False and st.done['zip:9:1']['logs_expected'] is None, 'no job list, not complete'
            assert n['mismatch'] == 3, n
            # credentials: every API request carried the token; no download-host request did; no link was recorded
            assert api_srv.seen and all(h.get('authorization') == 'Bearer ' + TOKEN for _, h in api_srv.seen), 'API requests authenticated'
            assert blob.seen and not any('authorization' in h or TOKEN in json.dumps(h) for _, h in blob.seen), 'no token to the download host'
            log_text = open(os.path.join(out, 'fetch-log.jsonl')).read()
            for leak in ('BLOBPATH', 'JOBPATH', '/missing/', '/again/', '/forbidden/', 'sig=', 'AbCdEf', 'SSSS', TOKEN):
                assert leak not in log_text, ('recorded a download link or the token', leak)
            seen_before = len(api_srv.seen)
            n2 = fetch(runs, load_jobs(jc), out, http_)
            assert n2['archived'] == 0 and n2['skipped'] == 7, ('resume', n2)
            lines = open(os.path.join(out, 'fetch-log.jsonl')).read().split('\n')
            open(os.path.join(out, 'fetch-log.jsonl'), 'w').write('\n'.join(l for l in lines if '"key": "zip:4:1"' not in l))
            n3 = fetch([r for r in runs if r['run_id'] == '4'], {}, out, http_)
            assert n3['archived'] == 1 and 'interrupted' in Store(out).done['zip:4:1']['detail'], ('interrupted pass', n3)
            assert len(api_srv.seen) > seen_before
            m = manifest(out)
            assert m['counts']['zips_archived'] == 5 and m['counts']['job_logs_archived'] == 2 and not m['rehash_mismatches'], m['counts']
            assert m['counts']['zips_incomplete'] == 2 and m['counts']['head_mismatches'] == 1, m['counts']
            c = completeness(out, runs, load_jobs(jc))
            bad = {i['key'] for i in c['missing_or_incomplete']}
            assert not c['complete'] and bad == {'zip:1:1', 'zip:2:1', 'run:6', 'zip:5:1', 'run:4', 'zip:7:1', 'zip:8:1', 'jobs:9:1', 'zip:9:1'}, sorted(bad)
            good = [r for r in runs if r['run_id'] == '3']
            assert completeness(out, good, load_jobs(jc))['complete'], 'a fully archived run is complete'
            one = [r for r in runs if r['run_id'] == '1']
            missing = lambda mode: {i['key'] for i in completeness(out, one, load_jobs(jc), mode)['missing_or_incomplete']}
            assert missing('cited') == {'zip:1:1'} and missing('all') == {'zip:1:1', 'joblog:12'}, 'all ran jobs are required'
            n4 = fetch(one, load_jobs(jc), out, http_, 'all')
            assert n4['archived'] == 1 and missing('all') == {'zip:1:1'}, ('every job that ran is fetched', n4)
            assert not completeness(out, [], {})['complete'], 'an empty batch is not complete'
            with open(os.path.join(out, 'jobs', '11.txt'), 'ab') as fh:
                fh.write(b'x')
            assert manifest(out)['rehash_mismatches'] == ['jobs/11.txt'], 'a changed file is caught'
            os.remove(os.path.join(out, 'jobs', '12.txt'))
            assert manifest(out)['rehash_mismatches'] == ['jobs/11.txt', 'jobs/12.txt'], 'a missing file is caught'
            assert {'joblog:11', 'joblog:12'} <= {i['key'] for i in completeness(out, runs, load_jobs(jc), 'all')['missing_or_incomplete']}
            hits = scan(out)
            assert {(h['file'], h['member']) for h in hits} >= {('runs/4/attempt-1.zip', '0_build.txt')}, hits
            assert {h['file'] for h in hits} == {'runs/4/attempt-1.zip'} and 'aaaa' not in json.dumps(hits), hits
            with open(os.path.join(out, 'fetch-log.jsonl'), 'a') as fh:
                fh.write(json.dumps({'key': 'note:x', 'outcome': 'ok', 'detail': 'https://h.invalid/p?sig=' + 'Z' * 20}) + '\n')
            assert 'fetch-log.jsonl' in {h['file'] for h in scan(out)}, 'metadata files are scanned too'
            assert scrub('see https://a.b/c?sig=XYZ and http://d.e/f') == 'see <url on a.b> and <url on d.e>'
            try:
                Http(api_srv.url, TOKEN, proxies={})._once(blob.url + '/x', True, '*/*')
                raise AssertionError('the token was sent to another host')
            except Failed:
                pass
            _, oc, err = attempt(lambda: Http(api_srv.url, 'wrong', proxies={}, tries=1).json('repos/o/r/actions/runs/1'))
            assert oc == 'failed' and '401' in err, (oc, err)
    finally:
        for s in (api_srv, blob, third):
            s.close()
    with contextlib.redirect_stdout(io.StringIO()):
        _self_test_more()
    print('self-test: OK (priority order; explicit rank; head check; every attempt; all job pages; skipped jobs; completeness; '
          '404/410 unavailable; download-host failure; second redirect refused; foreign next page refused; token only to the API '
          'host; no download link recorded; per-job logs; all ran job logs; resume; interrupted pass; re-hash; scan of logs and '
          'metadata without echo; partial re-runs; jobs cancelled before they started; the -<id>_ log name; one fixture per pattern in '
          'every file kind; an unreadable zip; exit codes of --scan and --complete; every attempt required; empty and unavailable '
          'job logs; a link urllib rejects; a non-https link; the API budget)')


def main(argv, http=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--runs'); ap.add_argument('--jobs'); ap.add_argument('--out')
    ap.add_argument('--job-logs', choices=('cited', 'all'), default='cited')
    ap.add_argument('--manifest', action='store_true'); ap.add_argument('--complete', action='store_true')
    ap.add_argument('--scan', action='store_true'); ap.add_argument('--self-test', action='store_true')
    a = ap.parse_args(argv)
    if a.self_test:
        self_test()
        return 0
    if a.manifest:
        print(json.dumps(manifest(a.out)['counts']))
        return 0
    if a.complete:
        c = completeness(a.out, load_runs(a.runs), load_jobs(a.jobs), a.job_logs)
        print('%s: %d required item(s), %d missing or incomplete' % ('complete' if c['complete'] else 'NOT COMPLETE',
                                                                     c['required'], len(c['missing_or_incomplete'])))
        for i in c['missing_or_incomplete']:
            print('  %s  %s' % (i['key'], i['state'][:200]))
        return 0 if c['complete'] else 1
    if a.scan:
        h = scan(a.out)
        print('%d credential-shaped line(s); locations in scan.json' % len(h))
        return 1 if h else 0
    http = http or Http(API, os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN'))
    print(json.dumps(fetch(load_runs(a.runs), load_jobs(a.jobs), a.out, http, a.job_logs)))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
