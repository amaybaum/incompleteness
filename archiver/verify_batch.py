#!/usr/bin/env python3
"""Verify an archived batch independently of the job that fetched it.

    python3 -I verify_batch.py --self-test                       # local server only, no network
    python3 -I verify_batch.py --batch archiver/batch.json --out ci-logs

It imports nothing from fetch_ci_logs.py or select_batch.py. What the batch must contain is derived from the
checked-out batch.json and inventory CSVs and from the host, never from the archive's own claims:
  - the runs: batch.json's run ids, or its rank range of the ranked CSV it names;
  - per run, from the API (JSON metadata only; the token goes only to the API host and no redirect is followed):
    head_sha, which must equal the inventory's and the archive record's, and run_attempt;
  - per attempt, from the API: the job list, which must equal the archive record's; the jobs the attempt itself ran
    fix how many top-level job logs its zip must hold (expected_in_zip(): a partial re-run's copies of earlier jobs,
    and jobs cancelled before they started, have none);
  - the job logs: the run's cited jobs from inventory-jobs.csv, and with "job_logs": "all" every job that ran.
Every staged file is re-read: its size and sha256 must equal the download-time record in fetch-log.jsonl; a zip
must pass its CRC test, its members' names, sizes and sha256 must equal the record, and its top-level job logs
must number the jobs that ran. No file outside that set may be present, and a credential-shaped line anywhere is
a failure. The verdict is VERIFY HOLDS only if every check passes; anything missing, changed or extra fails it."""
import argparse, contextlib, csv, hashlib, http.server, io, json, os, re, sys, tempfile, threading, zipfile
import urllib.error, urllib.parse, urllib.request

REPO = 'amaybaum/incompleteness'
API = 'https://api.github.com'
MAX_RUNS = 25
# Each pattern is paired with a fixture in the self-test that it alone matches.
PATTERNS = [re.compile(p) for p in (
    r'gh[pousr]_[A-Za-z0-9._-]{36,}', r'github_pat_[A-Za-z0-9_]{50,}', r'AKIA[0-9A-Z]{16}', r'-----BEGIN [A-Z ]*PRIVATE KEY-----',
    r'xox[abprs]-[A-Za-z0-9-]{10,}', r'(?i)\b(authorization|bearer)\b[:= ]+[A-Za-z0-9._~+/-]{20,}',
    r'(?i)\bauthorization\b[:= ]+(basic|token|bearer)\s+[A-Za-z0-9._~+/=-]{16,}', r'sk-[A-Za-z0-9]{32,}',
    r'sk-(ant|proj)-[A-Za-z0-9_-]{20,}', r'npm_[A-Za-z0-9]{36}', r'pypi-[A-Za-z0-9_-]{50,}', r'AIza[0-9A-Za-z_-]{35}',
    r'(?i)[?&](sig|signature|se|sv|skoid)=[A-Za-z0-9%._-]{16,}', r'(?i)x-amz-signature=[0-9a-f]{16,}',
    r'(?i)urlsignature=[A-Za-z0-9%._-]{16,}', r'eyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}')]
METADATA = {'fetch-log.jsonl', 'manifest.json', 'completeness.json', 'scan.json'}
TOP_LOG = re.compile(r'^-?\d+_.+\.txt$')


def expected_in_zip(jobs, earlier):
    """Ids of the jobs whose logs an attempt's zip must hold: those that ran (completed, neither skipped nor without a
    conclusion, nor cancelled before a runner took them) and were not copied from an earlier attempt. A partial re-run
    lists copied jobs under new ids with the name, start, end and runner of the original, and its zip omits them."""
    copied = {(j.get('name'), j.get('started_at'), j.get('completed_at'), j.get('runner_id')) for j in earlier if j.get('started_at')}
    out = []
    for j in jobs:
        if j.get('status') != 'completed' or j.get('conclusion') in ('skipped', None):
            continue
        if j.get('conclusion') == 'cancelled' and not j.get('runner_id'):
            continue
        if (j.get('name'), j.get('started_at'), j.get('completed_at'), j.get('runner_id')) in copied:
            continue
        out.append(str(j['id']))
    return out


class _Refuse(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a):
        return None


def api_pages(base, token, path, proxies=None):
    """Every page of an API answer. Only the API host is ever contacted, and only it receives the token."""
    host = urllib.parse.urlsplit(base).netloc
    opener = urllib.request.build_opener(_Refuse(), *([urllib.request.ProxyHandler(proxies)] if proxies is not None else []))
    url, docs = base.rstrip('/') + '/' + path, []
    while url:
        if urllib.parse.urlsplit(url).netloc != host:
            raise RuntimeError('a link to another host, not followed')
        req = urllib.request.Request(url, headers={'Accept': 'application/vnd.github+json', 'User-Agent': 'oi-log-verifier'})
        req.add_unredirected_header('Authorization', 'Bearer ' + token)
        try:
            with opener.open(req, timeout=120) as r:
                docs.append(json.loads(r.read()))
                m = re.search(r'<([^>]+)>;\s*rel="next"', r.headers.get('Link', '') or '')
        except urllib.error.HTTPError as e:
            raise RuntimeError('HTTP %d from the API' % e.code)
        url = m.group(1) if m else None
    return docs


def digest(b):
    return hashlib.sha256(b).hexdigest()


def select(batch_path):
    spec = json.load(open(batch_path))
    rows = list(csv.DictReader(open(os.path.join(os.path.dirname(os.path.abspath(batch_path)), spec['source']), newline='')))
    if 'ranks' in spec:
        a, b = (int(x) for x in spec['ranks'])
        ids = [r['run_id'] for r in sorted(rows, key=lambda r: int(r['rank'])) if a <= int(r['rank']) <= b]
        if len(ids) != b - a + 1:
            raise SystemExit('verify: rank range %d..%d is not fully in %s' % (a, b, spec['source']))
    else:
        ids = [str(x) for x in spec['run_ids']]
    if not ids or len(ids) > MAX_RUNS or len(set(ids)) != len(ids):
        raise SystemExit('verify: a batch names 1 to %d distinct runs, not %d' % (MAX_RUNS, len(ids)))
    return ids, spec.get('job_logs', 'cited')


def verify(batch_path, out, base=API, token=None, proxies=None):
    here = os.path.dirname(os.path.abspath(batch_path))
    ids, job_logs = select(batch_path)
    inventory = {r['run_id']: r for r in csv.DictReader(open(os.path.join(here, 'inventory-runs.csv'), newline=''))}
    cited = {}
    for r in csv.DictReader(open(os.path.join(here, 'inventory-jobs.csv'), newline='')):
        cited.setdefault(r['run_id'], []).append(r['job_id'])
    problems, lines, expected = [], [], set(METADATA)
    record = {}
    log_path = os.path.join(out, 'fetch-log.jsonl')
    if not os.path.exists(log_path):
        return ['fetch-log.jsonl is missing'], []
    for line in open(log_path):
        if line.strip():
            e = json.loads(line)
            record[e['key']] = e

    def staged(key, rel):
        """The staged file under rel, checked against the download-time record of key; its bytes, or None."""
        expected.add(rel)
        e = record.get(key)
        if not e or e.get('outcome') != 'archived' or e.get('path') != rel:
            problems.append('%s: no archived record for %s (%s)' % (key, rel, e.get('outcome') if e else 'none'))
            return None
        p = os.path.join(out, rel)
        if not os.path.isfile(p):
            problems.append('%s: %s is not in the artifact' % (key, rel))
            return None
        b = open(p, 'rb').read()
        if len(b) != e['bytes'] or digest(b) != e['sha256']:
            problems.append('%s: %s differs from its download-time record' % (key, rel))
            return None
        return b

    n_zip = n_job = n_bytes = 0
    for rid in ids:
        inv = inventory.get(rid)
        if not inv:
            problems.append('run %s is not in the inventory' % rid)
            continue
        try:
            host_run = api_pages(base, token, 'repos/%s/actions/runs/%s' % (REPO, rid), proxies)[0]
        except Exception as ex:
            problems.append('run %s: the host could not be read: %s' % (rid, str(ex)[:120]))
            continue
        rec = record.get('run:%s' % rid, {})
        heads = {'inventory': inv['head_sha'], 'host': host_run.get('head_sha'), 'archive record': rec.get('head_sha')}
        if len(set(heads.values())) != 1:
            problems.append('run %s: heads disagree: %s' % (rid, json.dumps(heads, sort_keys=True)))
        attempts = int(host_run.get('run_attempt') or 1)
        if rec.get('run_attempt') != attempts:
            problems.append('run %s: the host reports %d attempt(s), the archive record %s' % (rid, attempts, rec.get('run_attempt')))
        want, earlier = list(cited.get(rid, [])), []
        for att in range(1, attempts + 1):
            try:
                jobs = [j for d in api_pages(base, token, 'repos/%s/actions/runs/%s/attempts/%d/jobs?per_page=100' % (REPO, rid, att), proxies)
                        for j in d.get('jobs', [])]
            except Exception as ex:
                problems.append('run %s attempt %d: the job list could not be read: %s' % (rid, att, str(ex)[:120]))
                continue
            ran_ids = expected_in_zip(jobs, [])
            in_zip = expected_in_zip(jobs, earlier)
            earlier += jobs
            rec_jobs = record.get('jobs:%s:%d' % (rid, att), {}).get('jobs')
            if rec_jobs is None or sorted(str(j['id']) for j in rec_jobs) != sorted(str(j['id']) for j in jobs):
                problems.append('run %s attempt %d: the archive\'s job list differs from the host\'s' % (rid, att))
            if job_logs == 'all':
                want += [j for j in ran_ids if j not in want]
            key, rel = 'zip:%s:%d' % (rid, att), 'runs/%s/attempt-%d.zip' % (rid, att)
            b = staged(key, rel)
            if b is None:
                continue
            try:
                with zipfile.ZipFile(io.BytesIO(b)) as z:
                    if z.testzip() is not None:
                        raise ValueError('CRC failure')
                    members = [{'name': i.filename, 'size': i.file_size, 'sha256': digest(z.read(i))} for i in z.infolist() if not i.is_dir()]
            except Exception as ex:
                problems.append('%s: unreadable: %s' % (key, ex))
                continue
            if members != record[key].get('members'):
                problems.append('%s: members differ from the download-time record' % key)
            top = [m for m in members if '/' not in m['name'] and TOP_LOG.match(m['name'])]
            if len(top) != len(in_zip):
                problems.append('%s: %d top-level job log(s) for %d job(s) re-run in the attempt' % (key, len(top), len(in_zip)))
            n_zip += 1
            n_bytes += len(b)
            lines.append('ZIP     %s  %s  %d bytes  %d member(s)  %d job log(s) for %d job(s) re-run in the attempt' % (
                key, digest(b), len(b), len(members), len(top), len(in_zip)))
        for jid in want:
            b = staged('joblog:%s' % jid, 'jobs/%s.txt' % jid)
            if b is not None and not b:
                problems.append('joblog:%s: the staged job log is empty' % jid)
            elif b is not None:
                n_job += 1
                n_bytes += len(b)
                lines.append('JOBLOG  joblog:%s  %s  %d bytes' % (jid, digest(b), len(b)))
        lines.append('RUN     %s  head %s  %d attempt(s)' % (rid, inv['head_sha'], attempts))
    for f in sorted(METADATA):
        if not os.path.isfile(os.path.join(out, f)):
            problems.append('%s is not in the artifact' % f)
    try:
        if json.load(open(os.path.join(out, 'scan.json'))) != []:
            problems.append('the archive job\'s scan.json records credential-shaped lines')
    except Exception:
        problems.append('scan.json is unreadable')
    for root, _, files in os.walk(out):
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), out).replace(os.sep, '/')
            if rel not in expected:
                problems.append('unexpected file in the artifact: %s' % rel)
            raw = open(os.path.join(root, f), 'rb').read()
            texts = [('', raw)]
            if raw[:2] == b'PK':
                try:
                    with zipfile.ZipFile(io.BytesIO(raw)) as z:
                        texts += [(i.filename, z.read(i)) for i in z.infolist() if not i.is_dir()]
                except Exception:
                    problems.append('%s: an unreadable zip, not scanned' % rel)
            for member, t in texts:
                for k, line in enumerate(t.decode('utf-8', 'replace').split('\n'), 1):
                    if any(rx.search(line) for rx in PATTERNS):
                        problems.append('credential-shaped line: %s %s:%d' % (rel, member, k))
    lines.append('TOTAL   %d run(s), %d zip(s), %d job log(s), %d bytes' % (len(ids), n_zip, n_job, n_bytes))
    return problems, lines


# ---------------------------------------------------------------------------------------------------------- self-test
def _fixtures():
    """One credential-shaped string per pattern, matched by that pattern alone, built from pieces."""
    return ['ghs_' + '7654321_' + 'zy.xw-vu_' * 5, 'github_' + 'pat_' + 'B2' * 30, 'AK' + 'IA' + 'QRSTUVWXYZABCDEF',
            '-----BEGIN EC ' + 'PRIVATE KEY-----', 'xo' + 'xp-' + 'abcdef123456', 'bea' + 'rer: ' + 'y' * 24,
            'authorization=token ' + 'z' * 20, 'sk' + '-' + 'b' * 40, 'sk' + '-proj-' + 'c' * 24, 'np' + 'm_' + 'C' * 36,
            'py' + 'pi-' + 'D' * 52, 'AI' + 'za' + 'E' * 35, '&sig' + 'nature=' + 'f' * 20,
            'x-amz-sig' + 'nature=' + '0123456789abcdef' * 2, 'urlsig' + 'nature=' + 'g' * 20,
            'ey' + 'J' + 'k' * 11 + '.ey' + 'J' + 'm' * 11]


def self_test():
    token = 'test-token-' + 'q' * 20
    J = lambda i, c='success', name=None, st=None, en=None, rn=None: {
        'id': i, 'name': name or 'job%d' % i, 'status': 'completed', 'conclusion': c,
        'started_at': st or 's%d' % i, 'completed_at': en or 'e%d' % i, 'runner_id': rn if rn is not None else i}
    JOBS = {('1', 1): [J(11), J(12, 'skipped'), J(13, 'cancelled', rn=0)],      # job 13 was cancelled before it started
            ('2', 1): [J(21), J(22, 'failure')], ('2', 2): [J(23, name='job21'), J(24, 'failure', name='job22')],
            ('3', 1): [J(31, name='build'), J(32, name='probes')],              # attempt 2 copies build, re-runs probes
            ('3', 2): [J(33, name='build', st='s31', en='e31', rn=31), J(34, name='probes')]}
    attempts = {'1': 1, '2': 2, '3': 2}
    cfg = {'foreign': False, 'redirect': False}
    other_seen = []

    class Other(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            other_seen.append(dict(self.headers.items()))
            b = json.dumps({'jobs': [], 'head_sha': 'h1', 'run_attempt': 1}).encode()
            self.send_response(200); self.send_header('Content-Length', str(len(b))); self.end_headers(); self.wfile.write(b)

        def log_message(self, *a):
            pass

    other = http.server.ThreadingHTTPServer(('127.0.0.1', 0), Other)
    threading.Thread(target=other.serve_forever, daemon=True).start()
    other_url = 'http://127.0.0.1:%d' % other.server_address[1]

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            ep = self.path.split('?')[0].strip('/').split('/')
            extra = {}
            if self.headers.get('Authorization') != 'Bearer ' + token:
                code, body = 401, {}
            elif len(ep) == 6 and cfg['redirect'] and ep[5] == '1':
                code, body, extra = 302, {}, {'Location': other_url + self.path}
            elif len(ep) == 6:
                code, body = 200, {'head_sha': 'h' + ep[5], 'run_attempt': attempts[ep[5]]}
            else:
                code, body = 200, {'jobs': JOBS[(ep[5], int(ep[7]))]}
                if cfg['foreign'] and ep[5] == '1':
                    extra = {'Link': '<%s%s&page=2>; rel="next"' % (other_url, self.path)}
            b = json.dumps(body).encode()
            self.send_response(code)
            for k, v in extra.items():
                self.send_header(k, v)
            self.send_header('Content-Length', str(len(b))); self.end_headers(); self.wfile.write(b)

        def log_message(self, *a):
            pass

    srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = 'http://127.0.0.1:%d' % srv.server_address[1]

    def zipped(names, member_text=None):
        b = io.BytesIO()
        with zipfile.ZipFile(b, 'w', zipfile.ZIP_DEFLATED) as z:
            for i, nm in enumerate(names):
                z.writestr(('-%d_%s.txt' if i == 1 else '%d_%s.txt') % (i, nm), (member_text or 'log %s\n' % nm) * 4)
                z.writestr('%s/1_step.txt' % nm, 'step\n')
        return b.getvalue()

    def members(b):
        with zipfile.ZipFile(io.BytesIO(b)) as z:
            return [{'name': i.filename, 'size': i.file_size, 'sha256': digest(z.read(i))} for i in z.infolist()]

    ZIPS = {('1', 1): ['job11'], ('2', 1): ['job21', 'job22'], ('2', 2): ['job21', 'job22'], ('3', 1): ['build', 'probes'],
            ('3', 2): ['probes']}

    def build(d, mode='cited'):
        cfgd, out = os.path.join(d, 'cfg'), os.path.join(d, 'out')
        os.makedirs(cfgd); os.makedirs(out)
        with open(os.path.join(cfgd, 'inventory-runs.csv'), 'w', newline='') as fh:
            w = csv.writer(fh); w.writerow(['run_id', 'head_sha']); w.writerows([['1', 'h1'], ['2', 'h2'], ['3', 'h3']])
        with open(os.path.join(cfgd, 'inventory-jobs.csv'), 'w', newline='') as fh:
            w = csv.writer(fh); w.writerow(['job_id', 'run_id']); w.writerows([['21', '2']])
        json.dump({'source': 'inventory-runs.csv', 'run_ids': ['1', '2', '3'], 'job_logs': mode}, open(os.path.join(cfgd, 'batch.json'), 'w'))
        log = []

        def put(key, rel, b):
            os.makedirs(os.path.dirname(os.path.join(out, rel)), exist_ok=True)
            open(os.path.join(out, rel), 'wb').write(b)
            e = {'key': key, 'outcome': 'archived', 'path': rel, 'bytes': len(b), 'sha256': digest(b)}
            if rel.endswith('.zip'):
                e['members'] = members(b)
            log.append(e)

        for rid in ('1', '2', '3'):
            log.append({'key': 'run:' + rid, 'outcome': 'ok', 'head_sha': 'h' + rid, 'run_attempt': attempts[rid]})
            for att in range(1, attempts[rid] + 1):
                log.append({'key': 'jobs:%s:%d' % (rid, att), 'outcome': 'ok', 'jobs': [{'id': str(j['id'])} for j in JOBS[(rid, att)]]})
                put('zip:%s:%d' % (rid, att), 'runs/%s/attempt-%d.zip' % (rid, att), zipped(ZIPS[(rid, att)]))
        put('joblog:21', 'jobs/21.txt', b'job 21\n')
        if mode == 'all':
            for jid in ('11', '22', '23', '24', '31', '32', '33', '34'):
                put('joblog:' + jid, 'jobs/%s.txt' % jid, ('job %s\n' % jid).encode())
        with open(os.path.join(out, 'fetch-log.jsonl'), 'w') as fh:
            fh.writelines(json.dumps(e) + '\n' for e in log)
        open(os.path.join(out, 'manifest.json'), 'w').write('{}')
        open(os.path.join(out, 'completeness.json'), 'w').write('{}')
        open(os.path.join(out, 'scan.json'), 'w').write('[]')
        return os.path.join(cfgd, 'batch.json'), out

    def run(mutate=None, mode='cited'):
        with tempfile.TemporaryDirectory() as d:
            batch, out = build(d, mode)
            if mutate:
                mutate(out, os.path.dirname(batch))
            return verify(batch, out, base, token, proxies={})

    def edit_log(out, fn):
        p = os.path.join(out, 'fetch-log.jsonl')
        es = [fn(json.loads(l)) for l in open(p)]
        open(p, 'w').writelines(json.dumps(e) + '\n' for e in es if e)

    def flip(out, rel):
        p = os.path.join(out, rel)
        b = bytearray(open(p, 'rb').read()); b[-1] ^= 1; open(p, 'wb').write(bytes(b))

    def regen(out, rel, b):
        """Replace a staged file and its whole record consistently, so only a content check can tell."""
        open(os.path.join(out, rel), 'wb').write(b)
        upd = {'bytes': len(b), 'sha256': digest(b)}
        if rel.endswith('.zip'):
            upd['members'] = members(b)
        edit_log(out, lambda e: dict(e, **upd) if e.get('path') == rel else e)

    def drop(out, key, rel):
        edit_log(out, lambda e: None if e['key'] == key else e)
        os.remove(os.path.join(out, rel))

    try:
        p, lines = run()
        assert not p and lines[-1].startswith('TOTAL   3 run(s), 5 zip(s), 1 job log(s)'), (p, lines)
        p, _ = run(mode='all')
        assert not p, p
        fx = _fixtures()
        assert len(fx) == len(PATTERNS)
        for k, f in enumerate(fx):
            assert [i for i, rx in enumerate(PATTERNS) if rx.search(f)] == [k], ('fixture', k)
        # each case must be caught by the check it targets: (mutation, a substring of the expected problem)
        cases = {
            'a staged zip is missing': (lambda o, c: os.remove(os.path.join(o, 'runs/2/attempt-2.zip')), 'not in the artifact'),
            'a byte of a zip changed': (lambda o, c: flip(o, 'runs/1/attempt-1.zip'), 'download-time record'),
            'a cited job log is missing': (lambda o, c: os.remove(os.path.join(o, 'jobs/21.txt')), 'jobs/21.txt is not in'),
            'a job log changed': (lambda o, c: flip(o, 'jobs/21.txt'), 'download-time record'),
            'an extra file is present': (lambda o, c: open(os.path.join(o, 'runs/1/extra.txt'), 'w').write('x'), 'unexpected file'),
            'an attempt has no record': (lambda o, c: edit_log(o, lambda e: None if e['key'] == 'zip:2:2' else e), 'no archived record'),
            'an attempt dropped from record, files and count': (lambda o, c: (drop(o, 'zip:2:2', 'runs/2/attempt-2.zip'), edit_log(
                o, lambda e: None if e['key'] == 'jobs:2:2' else dict(e, run_attempt=1) if e['key'] == 'run:2' else e)), 'attempt(s)'),
            'the archive head differs': (lambda o, c: edit_log(o, lambda e: dict(e, head_sha='x') if e['key'] == 'run:1' else e), 'heads disagree'),
            'the inventory head differs': (lambda o, c: open(os.path.join(c, 'inventory-runs.csv'), 'w').write(
                'run_id,head_sha\n1,zz\n2,h2\n3,h3\n'), 'heads disagree'),
            'the job list differs': (lambda o, c: edit_log(o, lambda e: dict(e, jobs=e['jobs'][:1]) if e['key'] == 'jobs:2:1' else e), 'job list differs'),
            'a re-run job log is absent from a zip': (lambda o, c: regen(o, 'runs/2/attempt-1.zip', zipped(['job21'])), 'top-level job log'),
            'a partial re-run zip without its re-run job': (lambda o, c: regen(o, 'runs/3/attempt-2.zip', zipped([])), 'top-level job log'),
            'zip members differ from the record': (lambda o, c: edit_log(o, lambda e: dict(e, members=e['members'][:1]) if e['key'] == 'zip:1:1' else e), 'members differ'),
            'a credential in a compressed zip member': (lambda o, c: regen(o, 'runs/1/attempt-1.zip', zipped(['job11'], 'x ' * 40 + fx[0] + '\n')), 'attempt-1.zip 0_job11.txt'),
            'a credential in the metadata': (lambda o, c: open(os.path.join(o, 'manifest.json'), 'w').write('{"u": "x?sig=' + 'k' * 20 + '"}'), 'manifest.json'),
            'fetch-log.jsonl is missing': (lambda o, c: os.remove(os.path.join(o, 'fetch-log.jsonl')), 'fetch-log.jsonl is missing'),
            'completeness.json is missing': (lambda o, c: os.remove(os.path.join(o, 'completeness.json')), 'completeness.json is not in'),
            'the archive scan recorded hits': (lambda o, c: open(os.path.join(o, 'scan.json'), 'w').write('[{"file": "x"}]'), 'scan.json records'),
            'an empty job log': (lambda o, c: regen(o, 'jobs/21.txt', b''), 'empty'),
        }
        for k, f in enumerate(fx):
            cases['fixture %d in a job log' % k] = ((lambda f: lambda o, c: regen(o, 'jobs/21.txt', ('a\n' + f + '\n').encode()))(f),
                                                    'credential-shaped line: jobs/21.txt :2')
        for name, (m, want) in cases.items():
            p, _ = run(m)
            assert any(want in x for x in p), ('not caught as expected: ' + name, want, p)
        p, _ = run(lambda o, c: os.remove(os.path.join(o, 'jobs/34.txt')), 'all')
        assert any('joblog:34' in x for x in p), ('with all job logs required, a missing one is caught', p)
        cfg['foreign'] = True
        p, _ = run()
        cfg['foreign'] = False
        assert any('another host' in x for x in p) and not other_seen, ('a next page on another host is not followed', p, other_seen)
        cfg['redirect'] = True
        p, _ = run()
        cfg['redirect'] = False
        assert any('HTTP 302' in x for x in p) and not other_seen, ('a redirect is not followed', p, other_seen)
        with tempfile.TemporaryDirectory() as d:
            batch, out = build(d)
            with contextlib.redirect_stdout(io.StringIO()):
                assert main(['--batch', batch, '--out', out], base, token, {}) == 0, 'a clean batch exits 0'
                flip(out, 'jobs/21.txt')
                assert main(['--batch', batch, '--out', out], base, token, {}) == 1, 'a failed check exits 1'
            assert verify(batch, out, base, 'wrong-token', proxies={})[0], 'a host that cannot be read fails the check'
            json.dump({'source': 'inventory-runs.csv', 'run_ids': [str(i) for i in range(MAX_RUNS + 1)]}, open(batch, 'w'))
            try:
                verify(batch, out, base, token, proxies={})
                raise AssertionError('an oversized batch was accepted')
            except SystemExit:
                pass
    finally:
        srv.shutdown(); srv.server_close(); other.shutdown(); other.server_close()
    print('verify self-test: OK (clean batch holds, cited and all job logs, a partial re-run, a job cancelled before it '
          'started, the -<id>_ log name; %d cases each caught by the check it targets, one fixture per pattern among them; '
          'a missing job log in all mode; a foreign next page and a redirect, neither followed; exit codes; an unreadable '
          'host; an oversized batch)' % len(cases))


def main(argv, base=API, token=None, proxies=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--batch'); ap.add_argument('--out'); ap.add_argument('--self-test', action='store_true')
    a = ap.parse_args(argv)
    if a.self_test:
        self_test()
        return 0
    token = token or os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if not token:
        print('verify: no token (set GH_TOKEN)')
        return 1
    problems, lines = verify(a.batch, a.out, base, token, proxies)
    print('## independent verification')
    for l in lines:
        print(l)
    for p in problems:
        print('PROBLEM ' + p)
    print('VERIFY  %s' % ('HOLDS' if not problems else 'FAILS (%d problem(s))' % len(problems)))
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
