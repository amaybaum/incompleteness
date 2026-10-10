"""controls.py -- the frozen controls of round CI-RECEIPTS-1.

  python3 controls.py --self-test
      runs the receipt tool's offline self-test and this file's offline controls on the repository at HEAD
  python3 controls.py check --commit C --source-run S
      every control at commit C, with S the round's computing source run; needs read access to the GitHub API

The controls take the real repository at C. Each mutation is made in a scratch clone, never in the working tree.

  K1  the manifest is deterministic, and the fifteen shard manifests differ only in the shard id
  K2  positive control: an edit outside the manifest (a manuscript and the aggregate job) changes no manifest
  K3  mutation controls: each single change below is a mismatch in exactly the stated categories
  K4  the closure and data lists name tracked files at C, and the workflow matrix is the tool's shard list
  K5  push and pull-request semantics: both A42 jobs are dispatch-only, the matrix needs the decision job, the reuse
      input defaults to empty, and the aggregate requires success on dispatch and skipped otherwise
  K6  stale and forged receipts, with run and job identities read from the live API: a receipt presented under a
      wrong run, a push run, a failed run, a skipped job, an edited manifest with a stale digest, an edited manifest
      with a consistent digest, and a receipt naming another commit each fail at their stated check; the honest
      receipt rebuilt from C holds through checks 1-6
  K7  the receipt tool's self-test passes
"""
import importlib.util, json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
PUSH_RUN = '36896981080'       # main-push run at D: the A42 matrix skipped
FAILED_RUN = '36900831018'     # design dispatch whose shards failed the closure audit
FAILS, COUNT = [], [0]


def check(name, cond):
    COUNT[0] += 1
    print(('  PASS  ' if cond else '  FAIL  ') + name, flush=True)
    if not cond:
        FAILS.append(name)


def load_tool(root):
    spec = importlib.util.spec_from_file_location('ci_receipts_under_test', os.path.join(root, 'tools', 'ci_receipts.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def git(root, *args):
    r = subprocess.run(['git'] + list(args), cwd=root, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError('git %s: %s' % (' '.join(args), r.stderr.strip()))
    return r.stdout.strip()


ENV = {'python': '3.11.16 (main) [GCC]', 'implementation': 'cpython', 'machine': 'x86_64', 'system': 'Linux',
       'image_os': 'ubuntu24', 'distributions': ['numpy==2.4.6', 'python-sat==1.9.dev15']}


def offline(root, commit):
    t = load_tool(root)
    tmp = tempfile.mkdtemp(prefix='circtl-')
    clone = os.path.join(tmp, 'c')
    subprocess.run(['git', 'clone', '-q', '--no-checkout', root, clone], check=True)
    git(clone, 'checkout', '-q', '--detach', commit)

    def man(rev, part='cubes:0'):
        return t.manifest_at(rev, part, clone, ENV)

    base = man('HEAD')
    # K1
    check('K1 the manifest at C is deterministic', t.digest(base) == t.digest(man('HEAD')))
    parts = [man('HEAD', p) for p in t.PARTS]
    check('K1 the fifteen shard manifests differ only in the shard id',
          len({t.digest(m) for m in parts}) == 15 and all(
              {k: v for k, v in m.items() if k != 'probe'} == {k: v for k, v in base.items() if k != 'probe'}
              and m['probe']['blob'] == base['probe']['blob'] for m in parts))
    check('K1 the manifest names the probe, %d closure files and %d data files'
          % (len(base['closure']), len(base['data'])),
          base['probe']['blob'] is not None and all(base['closure'].values()) and all(base['data'].values()))

    def mutate(edits, msg):
        git(clone, 'checkout', '-q', '--detach', commit)
        for path, fn in edits:
            full = os.path.join(clone, path)
            old = open(full).read() if os.path.exists(full) else None
            new = fn(old)
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, 'w') as fh:
                fh.write(new)
        git(clone, 'add', '-A')
        if not git(clone, 'status', '--porcelain'):
            return None
        git(clone, '-c', 'user.name=c', '-c', 'user.email=c@c', 'commit', '-q', '-m', msg)
        return git(clone, 'rev-parse', 'HEAD')

    wf = t.WORKFLOW
    # K2
    c = mutate([('papers/Main.md', lambda s: s + '\nunrelated\n'),
                (wf, lambda s: s.replace('echo "foundations=${FOUNDATIONS_RESULT}"',
                                         'echo "foundations=${FOUNDATIONS_RESULT} "'))], 'unrelated')
    check('K2 positive: a manuscript and an aggregate-job edit change no shard manifest',
          c is not None and git(clone, 'diff', '--name-only', commit, c).split() == ['.github/workflows/verify.yml', 'papers/Main.md']
          and all(t.digest(man(c, p)) == t.digest(man(commit, p)) for p in t.PARTS))

    # K3
    def k3(name, edits, expect):
        c = mutate(edits, name)
        if c is None:
            check('K3 %s: the mutation applies' % name, False)
            return
        got = t.diff_categories(base, man(c))
        check('K3 %s: mismatch in %s' % (name, ', '.join(got) or 'nothing'), got == expect)

    k3('probe source', [(t.PROBE, lambda s: s + '# edit\n')], ['probe'])
    k3('imported helper a42/lib42.py', [('verification/lean/a42/lib42.py', lambda s: s + '# edit\n')], ['closure'])
    k3('new helper under a42/', [('verification/lean/a42/new_helper.py', lambda s: 'X = 1\n')], ['closure'])
    k3('executed source dita_arc_exclusivity_probe.py',
       [('verification/lean/dita_arc_exclusivity_probe.py', lambda s: s + '# edit\n')], ['closure'])
    k3('receipt tool', [(t.TOOL, lambda s: s + '# edit\n')], ['closure'])
    k3('data file Rle13_39.txt', [('verification/lean/a42/Rle13_39.txt', lambda s: s + '\n')], ['data'])
    k3('data file measurements.json', [(t.DATA[0], lambda s: s + '\n')], ['data'])
    k3('dependency pin', [(wf, lambda s: s.replace(
        'run: pip install numpy==2.4.6 python-sat==1.9.dev15\n\n      - name: Mode',
        'run: pip install numpy==2.4.7 python-sat==1.9.dev15\n\n      - name: Mode', 1))], ['pins', 'workflow'])
    k3('workflow python-version', [(wf, lambda s: re.sub(
        r"(  probes_a42_exclusion:.*?python-version: )'3\.11'", r"\1'3.12'", s, count=1, flags=re.S))], ['workflow'])
    k3('decision job', [(wf, lambda s: s.replace('Decide (one decision for all fifteen shards)',
                                                 'Decide (one decision)', 1))], ['workflow'])
    k3('workflow header', [(wf, lambda s: s.replace("        default: ''", "        default: ' '", 1))], ['workflow'])
    got = t.diff_categories(base, t.manifest_at(commit, 'cubes:0', clone, dict(ENV, python='3.11.17 (main) [GCC]')))
    check('K3 resolved python version: mismatch in %s' % ', '.join(got), got == ['environment'])
    got = t.diff_categories(base, t.manifest_at(commit, 'cubes:0', clone,
                                                dict(ENV, distributions=['numpy==2.4.6', 'python-sat==1.9.dev16'])))
    check('K3 resolved dependency version: mismatch in %s' % ', '.join(got), got == ['environment'])

    # K4
    tracked = set(git(clone, 'ls-tree', '-r', '--name-only', commit).split('\n'))
    check('K4 every closure and data path is tracked at C',
          set(t.CLOSURE) | set(t.DATA) <= tracked and t.PROBE in tracked)
    wtext = git(clone, 'show', '%s:%s' % (commit, wf))
    frag = t.job_fragment(wtext, t.SHARD_JOB)
    m = re.search(r"part: \[(.*?)\]", frag, re.S)
    matrix = tuple(re.findall(r"'([^']+)'", m.group(1))) if m else ()
    check('K4 the workflow matrix is the tool\'s fifteen shards', matrix == t.PARTS)

    # K5
    dec = t.job_fragment(wtext, t.DECIDE_JOB) or ''
    agg = t.job_fragment(wtext, 'probes') or ''
    check('K5 decision job and matrix are dispatch-only',
          "if: ${{ github.event_name == 'workflow_dispatch' }}" in dec
          and "if: ${{ github.event_name == 'workflow_dispatch' }}" in frag)
    check('K5 the matrix needs the decision job and refuses an unknown mode',
          'needs: [a42_receipts]' in frag and 'test "${MODE}" = compute || test "${MODE}" = reuse' in frag)
    check('K5 the reuse input is optional and defaults to empty',
          re.search(r"a42_reuse_run:\n.*?required: false\n\s+default: ''\n", wtext, re.S) is not None)
    check('K5 the aggregate requires both A42 jobs: success on dispatch, skipped otherwise',
          'a42_receipts, probes_a42_exclusion' in agg and 'test "${A42R_RESULT}" = success' in agg
          and 'test "${A42R_RESULT}" = skipped' in agg and 'test "${A42X_RESULT}" = skipped' in agg
          and 'receipt-validated from run ${A42R_SOURCE}' in agg and 'computed (15 shards)' in agg)
    shutil.rmtree(tmp)
    return t


class LiveIdentity:
    """Run and job identities from the live API; receipt contents served locally."""
    def __init__(self, t, arts):
        self.real, self.arts, self.repo = t.default_api(), arts, t.default_api().repo

    def get(self, path):
        return self.real.get(path)

    def jobs(self, run_id, attempt):
        return self.real.jobs(run_id, attempt)

    def artifacts(self, run_id, name):
        return [{'id': '%s/%s' % (run_id, name), 'name': name, 'expired': False}] \
            if (str(run_id), name) in self.arts else []

    def artifact_file(self, artifact_id, member):
        run_id, name = artifact_id.split('/')
        return self.arts[(run_id, name)]

    def is_ancestor(self, base, head):
        return self.real.is_ancestor(base, head)


def live(root, commit, source):
    t = load_tool(root)
    api = t.default_api()
    run = api.get('/repos/%s/actions/runs/%s' % (api.repo, source))
    sha, attempt = run['head_sha'], run['run_attempt']
    part = 'cubes:0'
    name = t.artifact_name(part)
    honest_m = t.manifest_at(sha, part, root, ENV)

    def receipt(run_id, head, m):
        return {'schema': t.SCHEMA, 'version': t.VERSION, 'part': part, 'mode': 'computed', 'manifest': m,
                'manifest_digest': t.digest(m),
                'result': {'summary': 'dita_support_minimality_probe %s: OK -- 10 checks' % part,
                           'output_sha256': '0' * 64, 'check_lines': 10},
                'source': {'repository': api.repo, 'run_id': str(run_id), 'run_attempt': str(attempt),
                           'job': t.JOB_NAME % part, 'event': 'workflow_dispatch', 'head_sha': head}}

    def outcome(run_id, rc, env=ENV, head=None):
        a = LiveIdentity(t, {(str(run_id), name): json.dumps(rc).encode()} if rc is not None else {})
        try:
            t.validate(part, run_id, a, head=head or commit, root=root, env=env)
            return 'holds'
        except t.Reject as e:
            return str(e)

    honest = receipt(source, sha, honest_m)
    r = outcome(source, honest, env=ENV)
    check('K6 the honest receipt rebuilt at the source commit holds at C (%s)' % r[:60], r == 'holds')
    other = receipt(source, sha, honest_m)
    other['source']['run_id'] = PUSH_RUN
    r = outcome(source, other)
    check('K6 correct manifest, wrong run id in the receipt: %s' % r[:70], r.startswith('check 3:'))
    r = outcome(PUSH_RUN, receipt(PUSH_RUN, sha, honest_m))
    check('K6 correct manifest presented from a push run: %s' % r[:70], r.startswith('check 1:') and 'push' in r)
    r = outcome(FAILED_RUN, receipt(FAILED_RUN, sha, honest_m))
    check('K6 correct manifest presented from a failed run: %s' % r[:70], r.startswith('check 1:'))
    stale = receipt(source, sha, json.loads(json.dumps(honest_m)))
    stale['manifest']['closure']['verification/lean/a42/lib42.py'] = '0' * 40
    r = outcome(source, stale)
    check('K6 correct result, edited manifest, stale digest: %s' % r[:70], r.startswith('check 4:'))
    stale['manifest_digest'] = t.digest(stale['manifest'])
    r = outcome(source, stale)
    check('K6 correct result, edited manifest, consistent digest: %s' % r[:70], r.startswith('check 5:'))
    wrong = receipt(source, commit if commit != sha else '0' * 40, honest_m)
    r = outcome(source, wrong)
    check('K6 receipt names another commit: %s' % r[:70], r.startswith('check 3:'))
    r = outcome(source, None)
    check('K6 no receipt: %s' % r[:70], r.startswith('check 3:'))


def tool_self_test(root):
    r = subprocess.run([sys.executable, os.path.join(root, 'tools', 'ci_receipts.py'), '--self-test'],
                       capture_output=True, text=True)
    check('K7 the receipt tool self-test passes', r.returncode == 0 and 'self-test OK' in r.stdout)


def main(argv):
    if argv == ['--self-test']:
        commit = git(ROOT, 'rev-parse', 'HEAD')
        offline(ROOT, commit)
        tool_self_test(ROOT)
    elif len(argv) == 5 and argv[0] == 'check' and argv[1] == '--commit' and argv[3] == '--source-run':
        commit = git(ROOT, 'rev-parse', argv[2])
        offline(ROOT, commit)
        live(ROOT, commit, argv[4])
        tool_self_test(ROOT)
    else:
        print(__doc__)
        return 2
    if FAILS:
        print('controls: FAILED (%d of %d): %s' % (len(FAILS), COUNT[0], '; '.join(FAILS)))
        return 1
    print('controls: OK -- %d checks' % COUNT[0])
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
