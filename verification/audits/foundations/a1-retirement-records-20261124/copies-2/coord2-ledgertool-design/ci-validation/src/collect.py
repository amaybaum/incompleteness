"""collect.py MODE: `identity` writes identity.json (the commits and the workflow blob), `env` writes env.json (the
runner environment), `results` copies the runners' result files into the evidence directory and writes
ci-results.json (schema ledger-coverage-suite-ci/1, stated in the workflow header)."""
import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys

LCS = os.environ['LCS']
EV = os.path.join(LCS, 'ev')
OUT = os.path.join(LCS, 'out')
STEPS = ['1-self-test', '2-purity', '3-synthetic', '4-conformance', '5-a1-conformance', '6a-a1-controls-no-main',
         '6-a1-controls', '8-y8', '9-mutation', 'lean-install', 'lean-build', '7-release-gate']
COPIES = [('st/result.json', '1-self-test-result.json'), ('p/result.json', '2-purity-result.json'),
          ('conf/conformance-controls.json', '4-conformance-controls.json'),
          ('a1c/a1-conformance.json', '5-a1-conformance.json'), ('a1/a1-controls.json', '6-a1-controls.json'),
          ('y8/a1-controls.json', '8-y8-a1-controls.json'), ('../mutwork/results.json', '9-mutation-results.json'),
          ('../mutwork/base.json', '9-mutation-base.json')]
NOT_RUNNABLE = [
    {'id': 'RT-T', 'reason': 'needs reviewed records, none of which exists before review; the A1 runner reports it '
                             'NOT RUN, as in the local run; not bound to the host'},
    {'id': 'TR45 op-C', 'reason': 'the offline replay of an op-C result needs delegated evidence recorded by native '
                                  'runs at X and C (G-A1, deferred); no entry point or flag of the runners at the '
                                  'tool commit performs it'},
    {'id': 'RestHost real reads', 'reason': 'the tool builds RestHost only for chain admission from a plan commit F '
                                            'with a reviewed configuration (TR5) and for native delegated runs of an '
                                            'admitted configuration (G-A1); no F exists before landing and no runner '
                                            'flag performs a host read; the job token is not given to the suite '
                                            'steps, so the runs match the local ones'},
    {'id': 'sec. 16.7 double run', 'reason': 'no entry point or flag runs a tool result twice and compares the '
                                             'bytes; it would need new control code'},
]


def git(*a):
    r = subprocess.run(['git'] + list(a), capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def read(p):
    try:
        with open(p) as f:
            return f.read()
    except OSError:
        return None


def dump(name, obj):
    with open(os.path.join(EV, name), 'w') as f:
        json.dump(obj, f, indent=1, sort_keys=True, default=str)
        f.write('\n')


def identity():
    ws = os.environ['GITHUB_WORKSPACE']
    ci_dir, wfp = os.path.join(ws, 'ci'), os.environ['WFP']
    dump('identity.json', {
        'ci_commit': git('-C', ci_dir, 'rev-parse', 'HEAD'),
        'ci_commit_parents': (git('-C', ci_dir, 'rev-list', '--parents', '-n', '1', 'HEAD') or '').split()[1:],
        'tool_commit': os.environ['T'],
        'tool_worktree_head': git('-C', os.environ['TOOL'], 'rev-parse', 'HEAD'),
        'main': os.environ['MAIN'],
        'origin_main_at_run': git('-C', ci_dir, 'rev-parse', '--verify', '-q', 'refs/remotes/origin/main'),
        'workflow': {'path': wfp, 'git_blob': git('-C', ci_dir, 'rev-parse', 'HEAD:' + wfp),
                     'sha256': sha256_file(os.path.join(ci_dir, wfp))},
    })


def env():
    mem = None
    for line in (read('/proc/meminfo') or '').splitlines():
        if line.startswith('MemTotal:'):
            mem = int(line.split()[1])
    osr = {}
    for line in (read('/etc/os-release') or '').splitlines():
        if '=' in line:
            k, v = line.split('=', 1)
            osr[k] = v.strip('"')
    du = shutil.disk_usage('/')
    dump('env.json', {'os': osr.get('PRETTY_NAME'), 'kernel': platform.release(),
                      'image_os': os.environ.get('ImageOS'), 'image_version': os.environ.get('ImageVersion'),
                      'runner_name': os.environ.get('RUNNER_NAME'), 'runner_arch': os.environ.get('RUNNER_ARCH'),
                      'python': sys.version, 'python_executable': sys.executable, 'git': git('--version'),
                      'cpus': os.cpu_count(), 'mem_total_kB': mem,
                      'disk_root_bytes': {'total': du.total, 'used': du.used, 'free': du.free}})


def time_report(step):
    out = {}
    for line in (read(os.path.join(EV, step + '.time')) or '').splitlines():
        if ':' in line:
            k, v = line.rsplit(':', 1)
            out[k.strip()] = v.strip()
    try:
        return int(out['Maximum resident set size (kbytes)'])
    except (KeyError, ValueError):
        return None


def results():
    for src, dst in COPIES:
        p = os.path.normpath(os.path.join(OUT, src))
        if os.path.exists(p):
            shutil.copy(p, os.path.join(EV, dst))
    ident = json.loads(read(os.path.join(EV, 'identity.json')) or '{}')
    steps, controls, mutation = [], {}, None
    for s in STEPS:
        v = json.loads(read(os.path.join(EV, s + '.verdict.json')) or 'null')
        ex = read(os.path.join(EV, s + '.exit'))
        wall = (read(os.path.join(EV, s + '.wall')) or '').split()
        df = (read(os.path.join(EV, s + '.df')) or '').split()
        steps.append({'id': s, 'exit': int(ex) if ex and ex.strip().lstrip('-').isdigit() else None,
                      'wall_seconds': round(float(wall[1]) - float(wall[0]), 1) if len(wall) == 2 else None,
                      'max_rss_kB': time_report(s),
                      'disk_used_bytes': int(df[0]) if len(df) == 2 else None,
                      'disk_avail_bytes': int(df[1]) if len(df) == 2 else None,
                      'verdict': ('PASS' if v['pass'] else 'FAIL') if v else 'NOT RUN',
                      'reasons': v['reasons'] if v else []})
        if v and v.get('controls') is not None:
            controls[s] = v['controls']
        if s == '9-mutation' and v:
            mutation = dict(v.get('extra') or {}, source_files=(read(os.path.join(EV, '9-mutation.source-files'))
                                                                or '').strip(),
                            tree_entries=(read(os.path.join(EV, '9-mutation.tree-entries')) or '').strip(),
                            mutant_trees_bytes=(read(os.path.join(EV, '9-mutation.trees-bytes')) or '').strip())
    y8 = json.loads(read(os.path.join(EV, '8-y8.verdict.json')) or 'null')
    syn = json.loads(read(os.path.join(EV, '3-synthetic.verdict.json')) or 'null')
    doc = {
        'schema': 'ledger-coverage-suite-ci/1',
        'commits': {'ci_commit': ident.get('ci_commit'), 'tool_commit': ident.get('tool_commit'),
                    'main': ident.get('main'), 'origin_main_at_run': ident.get('origin_main_at_run')},
        'workflow': ident.get('workflow'),
        'config': {'path': os.environ.get('CFG'), 'sha256_expected': os.environ.get('CFGSHA'),
                   'sha256': (read(os.path.join(EV, 'staged-config.sha256')) or '').strip() or None},
        'run': {'id': os.environ.get('GITHUB_RUN_ID'), 'attempt': os.environ.get('GITHUB_RUN_ATTEMPT'),
                'repository': os.environ.get('GITHUB_REPOSITORY'), 'ref': os.environ.get('GITHUB_REF'),
                'event': os.environ.get('GITHUB_EVENT_NAME'), 'sha': os.environ.get('GITHUB_SHA')},
        'environment': json.loads(read(os.path.join(EV, 'env.json')) or 'null'),
        'steps': steps,
        'controls': controls,
        'y8': {'synthetic_engine': ((syn or {}).get('extra') or {}).get('informational', {}).get('_Y8_engine'),
               'actual': ((y8 or {}).get('extra') or {}).get('y8_actual')},
        'mutation': mutation,
        'deferred_post_landing': ['TR5', 'G-A1', 'EI14'],
        'not_runnable_pre_landing': NOT_RUNNABLE,
        'all_verdicts_pass': all(s['verdict'] == 'PASS' for s in steps),
    }
    doc['evidence_sha256'] = {n: sha256_file(os.path.join(EV, n)) for n in sorted(os.listdir(EV))
                              if n != 'ci-results.json' and os.path.isfile(os.path.join(EV, n))}
    dump('ci-results.json', doc)
    print(json.dumps({'all_verdicts_pass': doc['all_verdicts_pass'],
                      'steps': {s['id']: s['verdict'] for s in steps}}, indent=1))


if __name__ == '__main__':
    {'identity': identity, 'env': env, 'results': results}[sys.argv[1]]()
