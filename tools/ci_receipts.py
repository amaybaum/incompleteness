"""ci_receipts.py -- receipt-backed reuse of unchanged A42 exclusion evidence (round CI-RECEIPTS-1).

The A42 exclusion matrix runs only on workflow_dispatch. A computing shard runs the probe under an audit hook, checks
that every tracked file the run opened lies in the shard's manifest, and writes a receipt naming its run, its job, its
commit, its manifest and its result. At an intermediate execution commit that a round's preregistration names in
advance, a dispatch may present the run id of an earlier computing run; every shard is then validated against that
run's receipt, and the whole family is reused only if every shard validates. Any failure recomputes the whole family.
F, E and Q attestation runs are dispatched without a reuse input and always recompute.

  python3 tools/ci_receipts.py manifest --part P            print the manifest at HEAD in this interpreter
  python3 tools/ci_receipts.py run --probe PATH --part P --receipt-dir DIR
                                                           compute the shard under the audit hook, write the receipt
  python3 tools/ci_receipts.py decide --run R              validate every shard against run R; write mode and source
  python3 tools/ci_receipts.py validate --part P --run R   validate one shard against run R; exit 1 unless it holds
  python3 tools/ci_receipts.py --self-test                 offline controls on a synthetic repository
"""
import hashlib, io, json, os, platform, re, shutil, subprocess, sys, tempfile, time, urllib.error, urllib.request
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOL = 'tools/ci_receipts.py'
PROBE = 'verification/lean/dita_support_minimality_probe.py'
WORKFLOW = '.github/workflows/verify.yml'
DECIDE_JOB, SHARD_JOB = 'a42_receipts', 'probes_a42_exclusion'
PARTS = ('paths', 'r5', 'n18:0', 'n18:1', 'n18:2', 'dfs:0', 'dfs:1', 'dfs:2', 'dfs:3', 'dfs:4', 'dfs:5', 'sathr',
         'cubes:0', 'cubes:1', 'cubes:2')
JOB_NAME = 'Numerical probes / A42 exclusion (%s)'
CLOSURE_DIRS = ('verification/lean/a42/',)
CLOSURE = (TOOL,)
DATA = ()
REPO_CATEGORIES = ('probe', 'closure', 'data', 'pins', 'workflow')
CATEGORIES = REPO_CATEGORIES + ('environment',)
SCHEMA, VERSION = 'ci-receipt', 1


# ---- git ----------------------------------------------------------------------------------------------------------
def git(*args, cwd=None, check=True):
    r = subprocess.run(['git'] + list(args), cwd=cwd or ROOT, capture_output=True)
    if check and r.returncode != 0:
        raise RuntimeError('git %s: %s' % (' '.join(args), r.stderr.decode(errors='replace').strip()))
    return r


def tree_blobs(rev, root):
    """{path: blob} for every tracked file at rev."""
    out = git('ls-tree', '-r', '-z', '--full-tree', rev, cwd=root).stdout.decode()
    blobs = {}
    for rec in out.split('\0'):
        if not rec:
            continue
        meta, path = rec.split('\t', 1)
        mode, kind, oid = meta.split()
        if kind == 'blob':
            blobs[path] = oid
    return blobs


def show(rev, path, root):
    r = git('show', '%s:%s' % (rev, path), cwd=root, check=False)
    return r.stdout.decode() if r.returncode == 0 else None


# ---- the manifest -------------------------------------------------------------------------------------------------
def job_fragment(text, job):
    """The text of one job under jobs:, from its key line to the line before the next job key, with trailing blank
    and comment lines removed. None when absent."""
    lines = text.split('\n')
    try:
        start = lines.index('  %s:' % job)
    except ValueError:
        return None
    end = start + 1
    while end < len(lines) and not re.match(r'^(  [A-Za-z_][\w-]*:\s*$|\S)', lines[end]):
        end += 1
    frag = lines[start:end]
    while frag and (not frag[-1].strip() or frag[-1].startswith('  #')):
        frag.pop()
    return '\n'.join(frag)


def workflow_header(text):
    """Every non-comment line before the jobs: key."""
    head = text.split('\njobs:\n', 1)[0] if '\njobs:\n' in text else text
    return '\n'.join(l for l in head.split('\n') if l.strip() and not l.lstrip().startswith('#'))


def pins_of(fragment):
    pins = []
    for line in (fragment or '').split('\n'):
        m = re.search(r'\bpip install (.*)$', line)
        if m:
            pins += m.group(1).split()
    return sorted(pins)


def repo_manifest(rev, part, root=ROOT):
    """The repository-derived categories at commit rev."""
    blobs = tree_blobs(rev, root)
    wf = show(rev, WORKFLOW, root) or ''
    shard = job_fragment(wf, SHARD_JOB)
    closure = {p: blobs.get(p) for p in CLOSURE}
    for p, b in blobs.items():
        if any(p.startswith(d) for d in CLOSURE_DIRS):
            closure[p] = b
    return {
        'probe': {'path': PROBE, 'blob': blobs.get(PROBE), 'part': part},
        'closure': dict(sorted(closure.items())),
        'data': {p: blobs.get(p) for p in sorted(DATA)},
        'pins': pins_of(shard),
        'workflow': {'header': workflow_header(wf), DECIDE_JOB: job_fragment(wf, DECIDE_JOB), SHARD_JOB: shard},
    }


def environment():
    from importlib import metadata
    dists = sorted({'%s==%s' % (d.metadata['Name'].lower(), d.version) for d in metadata.distributions()
                    if d.metadata['Name']})
    return {'python': sys.version, 'implementation': sys.implementation.name, 'machine': platform.machine(),
            'system': platform.system(), 'image_os': os.environ.get('ImageOS'), 'distributions': dists}


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')


def digest(manifest):
    return hashlib.sha256(canonical(manifest)).hexdigest()


def manifest_at(rev, part, root=ROOT, env=None):
    m = repo_manifest(rev, part, root)
    m['environment'] = environment() if env is None else env
    return m


def manifest_paths(m):
    return {m['probe']['path']} | set(m['closure']) | set(m['data'])


def diff_categories(a, b):
    return [c for c in CATEGORIES if a.get(c) != b.get(c)]


# ---- the audit hook -----------------------------------------------------------------------------------------------
HOOK = r'''
import os, sys
_d = os.environ.get('CI_RECEIPTS_AUDIT_DIR')
if _d:
    _f = open(os.path.join(_d, 'open-%d.txt' % os.getpid()), 'a', buffering=1)
    _seen = set()
    def _hook(event, args, _f=_f, _seen=_seen):
        if event != 'open':
            return
        p = args[0]
        if isinstance(p, bytes):
            p = os.fsdecode(p)
        if not isinstance(p, str):
            return
        try:
            p = os.path.realpath(p if os.path.isabs(p) else os.path.join(os.getcwd(), p))
        except Exception:
            return
        if p not in _seen:
            _seen.add(p)
            _f.write(p + '\n')
    sys.addaudithook(_hook)
'''


def audited_run(argv, cwd, echo=True):
    """Run argv with the audit hook in it and every child interpreter. Returns (exit, output, opened realpaths)."""
    hook_dir = tempfile.mkdtemp(prefix='cirhook-')
    log_dir = tempfile.mkdtemp(prefix='cirlog-')
    with open(os.path.join(hook_dir, 'sitecustomize.py'), 'w') as fh:
        fh.write(HOOK)
    env = dict(os.environ)
    env['PYTHONPATH'] = hook_dir + (os.pathsep + env['PYTHONPATH'] if env.get('PYTHONPATH') else '')
    env['CI_RECEIPTS_AUDIT_DIR'] = log_dir
    proc = subprocess.Popen(argv, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = io.BytesIO()
    for line in proc.stdout:
        out.write(line)
        if echo:
            sys.stdout.buffer.write(line)
            sys.stdout.flush()
    code = proc.wait()
    opened = set()
    for name in os.listdir(log_dir):
        with open(os.path.join(log_dir, name)) as fh:
            opened |= {l.rstrip('\n') for l in fh if l.strip()}
    shutil.rmtree(hook_dir), shutil.rmtree(log_dir)
    return code, out.getvalue(), opened


def audit_violations(opened, manifest, root=ROOT):
    """Tracked files at HEAD that the run opened and the manifest does not list."""
    tracked = set(tree_blobs('HEAD', root))
    real_root = os.path.realpath(root)
    rel = set()
    for p in opened:
        if p.startswith(real_root + os.sep):
            rel.add(os.path.relpath(p, real_root).replace(os.sep, '/'))
    return sorted((rel & tracked) - manifest_paths(manifest)), sorted(rel & tracked)


# ---- computing a shard --------------------------------------------------------------------------------------------
def artifact_name(part):
    return 'a42-receipt-' + part.replace(':', '_')


def summary_line(output, part):
    lines = [l for l in output.decode(errors='replace').split('\n')
             if l.startswith('dita_support_minimality_probe %s: ' % part)]
    return lines[-1] if lines else None


def cmd_run(probe, part, receipt_dir, root=ROOT, echo=True, environ=os.environ):
    if probe != PROBE:
        print('ci_receipts: probe %s is not the A42 exclusion probe %s' % (probe, PROBE)); return 1
    if part not in PARTS:
        print('ci_receipts: unknown part %s' % part); return 1
    m = manifest_at('HEAD', part, root)
    dirty = git('status', '--porcelain', '--', *sorted(manifest_paths(m) | {WORKFLOW}), cwd=root).stdout.decode().strip()
    if dirty:
        print('ci_receipts: manifest paths differ from HEAD:\n' + dirty); return 1
    started = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    code, output, opened = audited_run([sys.executable, os.path.join(root, probe), '--part', part],
                                       os.path.dirname(os.path.join(root, probe)), echo)
    finished = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    if code != 0:
        print('ci_receipts: probe exit %d; no receipt' % code); return code
    summary = summary_line(output, part)
    if not summary or ': OK -- ' not in summary:
        print('ci_receipts: no OK summary line; no receipt'); return 1
    bad, seen = audit_violations(opened, m, root)
    if bad:
        print('ci_receipts: closure audit FAILED -- the run opened tracked files outside the manifest; no receipt')
        for p in bad:
            print('  ' + p)
        return 1
    if manifest_at('HEAD', part, root, m['environment']) != m:
        print('ci_receipts: the manifest changed during the run; no receipt'); return 1
    receipt = {
        'schema': SCHEMA, 'version': VERSION, 'part': part, 'manifest': m, 'manifest_digest': digest(m),
        'mode': 'computed',
        'result': {'summary': summary, 'output_sha256': hashlib.sha256(output).hexdigest(),
                   'check_lines': sum(1 for l in output.split(b'\n') if l.startswith(b'PASS '))},
        'source': {'repository': environ.get('GITHUB_REPOSITORY'), 'run_id': environ.get('GITHUB_RUN_ID'),
                   'run_attempt': environ.get('GITHUB_RUN_ATTEMPT'), 'job': JOB_NAME % part,
                   'event': environ.get('GITHUB_EVENT_NAME'), 'head_sha': environ.get('GITHUB_SHA')},
        'metadata': {'started': started, 'finished': finished, 'image_version': environ.get('ImageVersion'),
                     'opened_tracked': seen},
    }
    os.makedirs(receipt_dir, exist_ok=True)
    with open(os.path.join(receipt_dir, 'receipt.json'), 'w') as fh:
        json.dump(receipt, fh, indent=1, sort_keys=True)
    print('ci_receipts: receipt %s, manifest %s, %s' % (artifact_name(part), digest(m)[:16], summary))
    gh_output(environ, artifact=artifact_name(part))
    return 0


def gh_output(environ, **kv):
    path = environ.get('GITHUB_OUTPUT')
    if path:
        with open(path, 'a') as fh:
            for k, v in kv.items():
                fh.write('%s=%s\n' % (k, v))


# ---- the GitHub API -----------------------------------------------------------------------------------------------
class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


class API:
    def __init__(self, repo, token=None, base='https://api.github.com'):
        self.repo, self.token, self.base = repo, token, base

    def _req(self, url, accept='application/vnd.github+json'):
        req = urllib.request.Request(url, headers={'Accept': accept, 'X-GitHub-Api-Version': '2022-11-28',
                                                   'User-Agent': 'ci-receipts'})
        if self.token:
            req.add_unredirected_header('Authorization', 'Bearer ' + self.token)
        return req

    def get(self, path):
        with urllib.request.urlopen(self._req(self.base + path), timeout=60) as r:
            return json.load(r)

    def jobs(self, run_id, attempt):
        jobs, page = [], 1
        while True:
            d = self.get('/repos/%s/actions/runs/%s/attempts/%s/jobs?per_page=100&page=%d'
                         % (self.repo, run_id, attempt, page))
            jobs += d['jobs']
            if len(d['jobs']) < 100:
                return jobs
            page += 1

    def artifacts(self, run_id, name):
        return self.get('/repos/%s/actions/runs/%s/artifacts?name=%s&per_page=100'
                        % (self.repo, run_id, name))['artifacts']

    def artifact_file(self, artifact_id, member):
        url = self.base + '/repos/%s/actions/artifacts/%s/zip' % (self.repo, artifact_id)
        opener = urllib.request.build_opener(_NoRedirect)
        try:
            with opener.open(self._req(url), timeout=60) as r:
                data = r.read()
        except urllib.error.HTTPError as e:
            if e.code not in (301, 302, 303, 307, 308):
                raise
            with urllib.request.urlopen(urllib.request.Request(e.headers['Location'],
                                        headers={'User-Agent': 'ci-receipts'}), timeout=120) as r:
                data = r.read()
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            names = z.namelist()
            if names != [member]:
                raise ValueError('artifact holds %s, not exactly %s' % (names, member))
            return z.read(member)

    def is_ancestor(self, base, head):
        d = self.get('/repos/%s/compare/%s...%s' % (self.repo, base, head))
        return d['status'] in ('ahead', 'identical')


# ---- validation ---------------------------------------------------------------------------------------------------
class Reject(Exception):
    pass


def fetch_commit(sha, root):
    if git('cat-file', '-e', sha + '^{commit}', cwd=root, check=False).returncode == 0:
        return
    if git('fetch', '-q', '--no-tags', '--depth=1', 'origin', sha, cwd=root, check=False).returncode != 0:
        raise Reject('source commit %s is not fetchable' % sha)


def validate(part, run_id, api, head='HEAD', root=ROOT, env=None):
    """Return the validation record for one shard; raise Reject naming the first failed check."""
    if part not in PARTS:
        raise Reject('unknown part %s' % part)
    if not re.fullmatch(r'[1-9][0-9]*', str(run_id)):
        raise Reject('run id %r is not a run id' % (run_id,))
    run = api.get('/repos/%s/actions/runs/%s' % (api.repo, run_id))
    # 1. the run
    if run.get('path') != WORKFLOW:
        raise Reject('check 1: run %s is a run of %s, not %s' % (run_id, run.get('path'), WORKFLOW))
    if (run.get('repository') or {}).get('full_name') != api.repo or \
            (run.get('head_repository') or {}).get('full_name') != api.repo:
        raise Reject('check 1: run %s is not a run in %s' % (run_id, api.repo))
    if run.get('event') != 'workflow_dispatch':
        raise Reject('check 1: run %s event is %s, not workflow_dispatch' % (run_id, run.get('event')))
    if run.get('status') != 'completed' or run.get('conclusion') != 'success':
        raise Reject('check 1: run %s is %s/%s, not completed/success' % (run_id, run.get('status'),
                                                                          run.get('conclusion')))
    sha, attempt = run['head_sha'], run['run_attempt']
    # 2. the job
    named = [j for j in api.jobs(run_id, attempt) if j.get('name') == JOB_NAME % part]
    if len(named) != 1:
        raise Reject('check 2: run %s attempt %s has %d jobs named %r' % (run_id, attempt, len(named), JOB_NAME % part))
    job = named[0]
    if job.get('conclusion') != 'success' or job.get('head_sha') != sha:
        raise Reject('check 2: job %s concluded %s at %s' % (job.get('id'), job.get('conclusion'), job.get('head_sha')))
    # 3. the receipt
    arts = [a for a in api.artifacts(run_id, artifact_name(part)) if a.get('name') == artifact_name(part)]
    if len(arts) != 1 or arts[0].get('expired'):
        raise Reject('check 3: run %s carries %d live artifacts named %s' % (run_id, len(arts), artifact_name(part)))
    try:
        rc = json.loads(api.artifact_file(arts[0]['id'], 'receipt.json'))
    except Exception as e:
        raise Reject('check 3: receipt unreadable: %s' % e)
    src = rc.get('source') or {}
    want = {'repository': api.repo, 'run_id': str(run_id), 'run_attempt': str(attempt), 'job': JOB_NAME % part,
            'event': 'workflow_dispatch', 'head_sha': sha}
    got = {k: (str(src.get(k)) if k in ('run_id', 'run_attempt') else src.get(k)) for k in want}
    if rc.get('schema') != SCHEMA or rc.get('version') != VERSION or rc.get('part') != part \
            or rc.get('mode') != 'computed' or got != want:
        raise Reject('check 3: receipt identity %s does not match the run %s' % (
            {k: got[k] for k in want if got[k] != want[k]} or {'schema/part/mode': (rc.get('schema'), rc.get('part'),
                                                                                   rc.get('mode'))}, want))
    m = rc.get('manifest')
    if not isinstance(m, dict) or sorted(m) != sorted(CATEGORIES):
        raise Reject('check 3: receipt manifest malformed')
    # 4. self-consistency
    if digest(m) != rc.get('manifest_digest'):
        raise Reject('check 4: receipt manifest does not serialize to its digest')
    # 5. the repository-derived categories, recomputed at the source commit
    fetch_commit(sha, root)
    at_src = repo_manifest(sha, part, root)
    bad = [c for c in REPO_CATEGORIES if m.get(c) != at_src.get(c)]
    if bad:
        raise Reject('check 5: receipt %s differ from the source commit %s' % (', '.join(bad), sha))
    # 6. the current manifest
    now = manifest_at(head, part, root, env)
    bad = diff_categories(m, now)
    if bad:
        raise Reject('check 6: manifest mismatch in %s' % ', '.join(bad))
    # 7. the source is an ancestor of the current commit
    cur = git('rev-parse', head, cwd=root).stdout.decode().strip()
    if not api.is_ancestor(sha, cur):
        raise Reject('check 7: source commit %s is not an ancestor of %s' % (sha, cur))
    return {'part': part, 'source_run': str(run_id), 'source_attempt': str(attempt), 'source_job': job.get('id'),
            'source_commit': sha, 'manifest_digest': rc['manifest_digest'], 'summary': rc['result']['summary'],
            'output_sha256': rc['result']['output_sha256']}


def cmd_decide(run_id, api, root=ROOT, environ=os.environ, env=None):
    """One decision for the whole family: reuse only if every shard validates against run_id."""
    if not run_id:
        print('ci_receipts: no reuse input; mode compute')
        gh_output(environ, mode='compute', source='')
        return 0
    held = []
    for part in PARTS:
        try:
            v = validate(part, run_id, api, root=root, env=env)
        except Reject as e:
            print('ci_receipts: %s: %s' % (part, e))
            print('ci_receipts: mode compute (no partial reuse)')
            gh_output(environ, mode='compute', source='')
            return 0
        except Exception as e:
            print('ci_receipts: %s: error %s: %s' % (part, type(e).__name__, e))
            print('ci_receipts: mode compute (no partial reuse)')
            gh_output(environ, mode='compute', source='')
            return 0
        held.append(v)
        print('ci_receipts: %-8s receipt holds: run %s job %s commit %s manifest %s'
              % (part, v['source_run'], v['source_job'], v['source_commit'][:12], v['manifest_digest'][:16]))
    print('ci_receipts: all %d shards hold; mode reuse from run %s' % (len(held), run_id))
    gh_output(environ, mode='reuse', source=str(run_id))
    return 0


def cmd_validate(part, run_id, api, root=ROOT):
    try:
        v = validate(part, run_id, api, root=root)
    except Exception as e:
        print('ci_receipts: %s: receipt does NOT hold: %s' % (part, e)); return 1
    print('ci_receipts: %s receipt-validated: source run %s attempt %s job %s commit %s manifest %s'
          % (part, v['source_run'], v['source_attempt'], v['source_job'], v['source_commit'], v['manifest_digest']))
    print('ci_receipts: source result: %s (output sha256 %s)' % (v['summary'], v['output_sha256']))
    return 0


def default_api():
    repo = os.environ.get('GITHUB_REPOSITORY', 'amaybaum/incompleteness')
    return API(repo, os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN'))


# ---- self-test ----------------------------------------------------------------------------------------------------
class FakeAPI:
    """Serves runs, jobs and artifacts from dictionaries, with the real API's shapes."""
    def __init__(self, repo, root):
        self.repo, self.root, self.runs, self.jobs_, self.arts = repo, root, {}, {}, {}

    def get(self, path):
        m = re.fullmatch(r'/repos/[^/]+/[^/]+/actions/runs/(\d+)', path)
        if not m or m.group(1) not in self.runs:
            raise urllib.error.HTTPError(path, 404, 'Not Found', {}, None)
        return self.runs[m.group(1)]

    def jobs(self, run_id, attempt):
        return self.jobs_.get((str(run_id), str(attempt)), [])

    def artifacts(self, run_id, name):
        return [{'id': '%s/%s' % (run_id, n), 'name': n, 'expired': False}
                for n in self.arts.get(str(run_id), {}) if n == name]

    def artifact_file(self, artifact_id, member):
        run_id, name = artifact_id.split('/')
        return self.arts[run_id][name]

    def is_ancestor(self, base, head):
        return git('merge-base', '--is-ancestor', base, head, cwd=self.root, check=False).returncode == 0


SYN_PROBE = r'''import os, sys
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, 'a42'))
import helper
data = open(os.path.join(here, 'a42', 'Rle13_39.txt')).read()
if os.environ.get('SYN_EXTRA'):
    open(os.path.join(here, 'unlisted.txt')).read()
print('PASS synthetic %s' % helper.VALUE)
print('dita_support_minimality_probe %s: OK -- 1 checks (0s)' % sys.argv[2])
'''

SYN_WORKFLOW = '''name: verify
on:
  workflow_dispatch:
jobs:
  %s:
    runs-on: ubuntu-latest
    steps:
      - run: python3 tools/ci_receipts.py decide
  %s:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install numpy==2.4.6 python-sat==1.9.dev15
  probes:
    runs-on: ubuntu-latest
    steps:
      - run: echo aggregate
''' % (DECIDE_JOB, SHARD_JOB)


def self_test():
    repo = 'owner/repo'
    tmp = tempfile.mkdtemp(prefix='cirtest-')
    root = os.path.join(tmp, 'r')
    fails = []

    def expect(name, cond):
        if not cond:
            fails.append(name)

    def write(path, text):
        full = os.path.join(root, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, 'w') as fh:
            fh.write(text)

    def commit(msg):
        git('add', '-A', cwd=root)
        git('-c', 'user.name=t', '-c', 'user.email=t@t', 'commit', '-q', '-m', msg, cwd=root)
        return git('rev-parse', 'HEAD', cwd=root).stdout.decode().strip()

    os.makedirs(root)
    git('init', '-q', cwd=root)
    write(PROBE, SYN_PROBE)
    write('verification/lean/a42/helper.py', 'VALUE = 1\n')
    write('verification/lean/a42/Rle13_39.txt', '1 2 3\n')
    write('verification/lean/unlisted.txt', 'x\n')
    write(WORKFLOW, SYN_WORKFLOW)
    write(TOOL, open(os.path.abspath(__file__)).read())
    write('papers/Other.md', 'unrelated\n')
    c0 = commit('source')
    env = {'python': '3.11.16', 'implementation': 'cpython', 'machine': 'x86_64', 'system': 'Linux',
           'image_os': 'ubuntu24', 'distributions': ['numpy==2.4.6', 'python-sat==1.9.dev15']}
    part = 'cubes:0'

    # computing a shard: receipt written, closure audit clean
    rdir = os.path.join(tmp, 'receipt')
    environ = {'GITHUB_REPOSITORY': repo, 'GITHUB_RUN_ID': '100', 'GITHUB_RUN_ATTEMPT': '1',
               'GITHUB_EVENT_NAME': 'workflow_dispatch', 'GITHUB_SHA': c0}
    code = cmd_run(PROBE, part, rdir, root=root, echo=False, environ=environ)
    expect('run: a computing shard writes a receipt', code == 0 and os.path.exists(os.path.join(rdir, 'receipt.json')))
    rc = json.load(open(os.path.join(rdir, 'receipt.json')))
    expect('run: the receipt records run, commit, digest and result',
           rc['source']['run_id'] == '100' and rc['source']['head_sha'] == c0 and rc['manifest_digest']
           == digest(rc['manifest']) and rc['result']['summary'].startswith('dita_support_minimality_probe cubes:0: OK'))
    expect('run: the audit saw the helper and the data file',
           'verification/lean/a42/helper.py' in rc['manifest']['closure'])
    # the closure audit: a run that opens a tracked file outside the manifest fails and writes no receipt
    rdir2 = os.path.join(tmp, 'receipt2')
    os.environ['SYN_EXTRA'] = '1'
    try:
        code = cmd_run(PROBE, part, rdir2, root=root, echo=False, environ=environ)
    finally:
        del os.environ['SYN_EXTRA']
    expect('closure audit: an unlisted tracked read fails the shard', code == 1 and not os.path.exists(rdir2))
    # the receipt's environment is the test interpreter's; pin it to env for the remaining controls
    rc['manifest']['environment'] = env
    rc['manifest_digest'] = digest(rc['manifest'])

    def serve(api, run_id, sha, receipt, event='workflow_dispatch', conclusion='success', job_conclusion='success',
              parts=PARTS, attempt=1):
        api.runs[str(run_id)] = {'id': int(run_id), 'path': WORKFLOW, 'event': event, 'status': 'completed',
                                 'conclusion': conclusion, 'head_sha': sha, 'run_attempt': attempt,
                                 'repository': {'full_name': repo}, 'head_repository': {'full_name': repo}}
        api.jobs_[(str(run_id), str(attempt))] = [{'id': 1000 + i, 'name': JOB_NAME % p, 'conclusion': job_conclusion,
                                                  'head_sha': sha} for i, p in enumerate(parts)]
        arts = {}
        if receipt is not None:
            for p in parts:
                r = json.loads(json.dumps(receipt))
                r['part'] = p
                r['source'].update(job=JOB_NAME % p, run_id=str(run_id), run_attempt=str(attempt), head_sha=sha,
                                   event=event)
                r['manifest'] = manifest_at(sha, p, root, env)
                r['manifest_digest'] = digest(r['manifest'])
                arts[artifact_name(p)] = json.dumps(r).encode()
        api.arts[str(run_id)] = arts

    def holds(api, run_id, head='HEAD', e=env, p=part):
        try:
            validate(p, run_id, api, head=head, root=root, env=e)
            return 'holds'
        except Reject as ex:
            return str(ex)

    api = FakeAPI(repo, root)
    serve(api, 100, c0, rc)
    expect('baseline: the receipt holds at its own commit', holds(api, 100) == 'holds')

    # positive control: an unrelated edit leaves the manifest unchanged and the receipt holds
    write('papers/Other.md', 'unrelated, edited\n')
    write(WORKFLOW, SYN_WORKFLOW.replace('echo aggregate', 'echo aggregate, edited'))
    c1 = commit('unrelated')
    expect('positive: unrelated edit keeps the digest',
           digest(manifest_at(c1, part, root, env)) == digest(manifest_at(c0, part, root, env)))
    expect('positive: unrelated edit, receipt holds', holds(api, 100) == 'holds')
    rec = io.StringIO()
    so, sys.stdout = sys.stdout, rec
    try:
        cmd_decide('100', api, root=root, environ={}, env=env)
    finally:
        sys.stdout = so
    expect('decide: every shard holds, mode reuse', 'mode reuse from run 100' in rec.getvalue())

    # mutation controls: one change per category, each a mismatch naming that category
    def mutation(name, path, new_text, category, e=env):
        old = open(os.path.join(root, path)).read() if os.path.exists(os.path.join(root, path)) else None
        write(path, new_text)
        commit('mutate ' + name)
        r = holds(api, 100, e=e)
        expect('mutation %s: %s' % (name, r), r == 'check 6: manifest mismatch in %s' % category)
        if old is not None:
            write(path, old)
        else:
            os.remove(os.path.join(root, path))
        commit('restore ' + name)

    mutation('probe source', PROBE, SYN_PROBE + '# edit\n', 'probe')
    mutation('imported helper', 'verification/lean/a42/helper.py', 'VALUE = 1  # edit\n', 'closure')
    mutation('new helper', 'verification/lean/a42/helper2.py', 'X = 2\n', 'closure')
    mutation('dependency pin', WORKFLOW, SYN_WORKFLOW.replace('numpy==2.4.6', 'numpy==2.4.7'), 'pins, workflow')
    mutation('workflow config', WORKFLOW, SYN_WORKFLOW.replace("'3.11'", "'3.12'"), 'workflow')
    mutation('decision job', WORKFLOW, SYN_WORKFLOW.replace('ci_receipts.py decide', 'ci_receipts.py decide '),
             'workflow')
    mutation('receipt tool', TOOL, open(os.path.abspath(__file__)).read() + '# edit\n', 'closure')
    r = holds(api, 100, e=dict(env, python='3.11.17'))
    expect('mutation python version: %s' % r, r == 'check 6: manifest mismatch in environment')
    r = holds(api, 100, e=dict(env, distributions=['numpy==2.4.6', 'python-sat==1.9.dev16']))
    expect('mutation resolved dependency: %s' % r, r == 'check 6: manifest mismatch in environment')
    saved = DATA
    globals()['DATA'] = ('verification/lean/unlisted.txt',)
    try:
        serve(api, 100, c0, rc)
        expect('data baseline holds', holds(api, 100) == 'holds')
        write('verification/lean/unlisted.txt', 'y\n')
        commit('mutate data')
        r = holds(api, 100)
        expect('mutation data file: %s' % r, r == 'check 6: manifest mismatch in data')
    finally:
        globals()['DATA'] = saved
        write('verification/lean/unlisted.txt', 'x\n')
        commit('restore data')
    serve(api, 100, c0, rc)
    expect('restored tree holds again', holds(api, 100) == 'holds')

    # stale and forged receipts: correct manifest with a wrong run identity
    good = api.arts['100'][artifact_name(part)]
    serve(api, 200, c0, rc)
    api.arts['200'][artifact_name(part)] = good
    expect('forged: run 100 receipt presented under run 200', holds(api, 200).startswith('check 3:'))
    serve(api, 300, c0, rc, event='push')
    expect('forged: push run', holds(api, 300).startswith('check 1:') and 'push' in holds(api, 300))
    serve(api, 301, c0, rc, event='pull_request')
    expect('forged: pull-request run', holds(api, 301).startswith('check 1:'))
    serve(api, 302, c0, None, event='push', job_conclusion='skipped')
    expect('skipped matrix: push run with the matrix skipped', holds(api, 302).startswith('check 1:'))
    serve(api, 303, c0, rc, conclusion='failure', job_conclusion='skipped')
    expect('skipped matrix: dispatch run with the matrix skipped', holds(api, 303).startswith('check 1:'))
    serve(api, 304, c0, rc)
    api.runs['304']['conclusion'] = 'success'
    for j in api.jobs_[('304', '1')]:
        j['conclusion'] = 'skipped'
    expect('skipped matrix: a skipped shard job is no source', holds(api, 304).startswith('check 2:'))
    serve(api, 305, c0, rc)
    api.arts['305'] = {}
    expect('missing receipt', holds(api, 305).startswith('check 3:'))
    serve(api, 306, c0, rc)
    r6 = json.loads(api.arts['306'][artifact_name(part)])
    r6['source']['head_sha'] = c1
    api.arts['306'][artifact_name(part)] = json.dumps(r6).encode()
    expect('forged: receipt names another commit', holds(api, 306).startswith('check 3:'))
    serve(api, 307, c0, rc)
    r7 = json.loads(api.arts['307'][artifact_name(part)])
    r7['mode'] = 'receipt-validated'
    api.arts['307'][artifact_name(part)] = json.dumps(r7).encode()
    expect('a receipt-validated record is no source', holds(api, 307).startswith('check 3:'))
    # correct result with a wrong manifest
    serve(api, 400, c0, rc)
    r4 = json.loads(api.arts['400'][artifact_name(part)])
    r4['manifest']['closure']['verification/lean/a42/helper.py'] = '0' * 40
    api.arts['400'][artifact_name(part)] = json.dumps(r4).encode()
    expect('forged: manifest edited, digest stale', holds(api, 400).startswith('check 4:'))
    r4['manifest_digest'] = digest(r4['manifest'])
    api.arts['400'][artifact_name(part)] = json.dumps(r4).encode()
    expect('forged: manifest edited, digest consistent', holds(api, 400).startswith('check 5:'))
    serve(api, 401, c0, rc)
    r5 = json.loads(api.arts['401'][artifact_name(part)])
    write('verification/lean/a42/helper.py', 'VALUE = 2\n')
    c2 = commit('helper changed')
    r5['manifest'] = manifest_at(c2, part, root, env)
    r5['manifest_digest'] = digest(r5['manifest'])
    api.arts['401'][artifact_name(part)] = json.dumps(r5).encode()
    expect('forged: receipt claims the current manifest from an older commit', holds(api, 401).startswith('check 5:'))
    write('verification/lean/a42/helper.py', 'VALUE = 1\n')
    c3 = commit('helper restored')
    # a source that is not an ancestor
    git('checkout', '-q', '-b', 'side', c0, cwd=root)
    write('papers/Side.md', 'side\n')
    cs = commit('side')
    git('checkout', '-q', '-', cwd=root)
    serve(api, 500, cs, rc)
    expect('a source off the current line is rejected', holds(api, 500).startswith('check 7:'))
    # decide: one failing shard means no reuse at all
    serve(api, 600, c0, rc)
    del api.arts['600'][artifact_name('dfs:3')]
    rec = io.StringIO()
    so, sys.stdout = sys.stdout, rec
    try:
        out = {}
        path = os.path.join(tmp, 'gh_output')
        cmd_decide('600', api, root=root, environ={'GITHUB_OUTPUT': path}, env=env)
        out = dict(l.split('=', 1) for l in open(path).read().split())
    finally:
        sys.stdout = so
    expect('decide: one shard without a receipt means mode compute', out.get('mode') == 'compute')
    rec = io.StringIO()
    so, sys.stdout = sys.stdout, rec
    try:
        path = os.path.join(tmp, 'gh_output2')
        cmd_decide('', api, root=root, environ={'GITHUB_OUTPUT': path}, env=env)
        out = dict(l.split('=', 1) for l in open(path).read().split('\n') if l)
    finally:
        sys.stdout = so
    expect('decide: no input means mode compute', out.get('mode') == 'compute')
    expect('decide: malformed run id rejected', holds(api, 'abc').startswith('run id'))
    # the fragment extractor
    expect('fragment: decision job extracted', job_fragment(SYN_WORKFLOW, DECIDE_JOB).startswith('  %s:' % DECIDE_JOB)
           and 'probes:' not in job_fragment(SYN_WORKFLOW, SHARD_JOB))
    expect('fragment: absent job is None', job_fragment(SYN_WORKFLOW, 'nope') is None)
    shutil.rmtree(tmp)
    if fails:
        print('ci_receipts self-test FAILED:')
        for f in fails:
            print('  ' + f)
        return 1
    print('ci_receipts: self-test OK (receipt written and audited; unrelated edit holds; probe, helper, new helper, '
          'data, pin, workflow, decision job, tool, python and dependency mutations each rejected by category; '
          'forged identity, push, pull-request, skipped matrix, skipped shard, missing receipt, wrong commit, '
          'reused record, stale digest, edited manifest, older-commit manifest and off-line source each rejected; '
          'no partial reuse)')
    return 0


def main(argv):
    if argv == ['--self-test']:
        return self_test()
    if not argv:
        print(__doc__); return 2
    cmd, rest = argv[0], argv[1:]
    opts = dict(zip(rest[::2], rest[1::2]))
    if cmd == 'manifest' and set(opts) == {'--part'}:
        m = manifest_at('HEAD', opts['--part'])
        print(json.dumps(m, indent=1, sort_keys=True))
        print('digest', digest(m))
        return 0
    if cmd == 'run' and set(opts) == {'--probe', '--part', '--receipt-dir'}:
        return cmd_run(opts['--probe'], opts['--part'], opts['--receipt-dir'])
    if cmd == 'decide' and set(opts) <= {'--run'} and len(rest) in (0, 2):
        return cmd_decide(opts.get('--run', '').strip(), default_api())
    if cmd == 'validate' and set(opts) == {'--part', '--run'}:
        return cmd_validate(opts['--part'], opts['--run'], default_api())
    print(__doc__); return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
