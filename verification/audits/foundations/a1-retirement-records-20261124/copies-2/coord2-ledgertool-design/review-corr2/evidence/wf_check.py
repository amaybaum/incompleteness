"""Reviewer workflow probe for 4f4a9d58: YAML vs extraction, pre-run byte identity, 18 arms vs independent expectation,
unknown values, injection (incl. new input c), bash -n, quoting. usage: python3 wf_check.py NEWTREE OLDTREE WORK"""
import sys, os, re, json, shlex, subprocess, hashlib, yaml
new, old, work = sys.argv[1:4]
os.makedirs(work, exist_ok=True)
W = '.github/workflows/ledger-coverage.yml'
nb, ob = open(os.path.join(new, W), 'rb').read(), open(os.path.join(old, W), 'rb').read()
print('workflow sha256', hashlib.sha256(nb).hexdigest())
d, do = yaml.safe_load(nb), yaml.safe_load(ob)
st, sto = d['jobs']['run']['steps'], do['jobs']['run']['steps']
pre = [s for s in st if s.get('name') == 'pre-run pin check'][0]
preo = [s for s in sto if s.get('name') == 'pre-run pin check'][0]
print('pre-run step parsed equal to 3184c7f9:', pre == preo)
# raw byte identity of the step's lines
def raw_step(b, name):
    L = b.decode().split('\n'); i = [k for k, l in enumerate(L) if l.strip() == '- name: ' + name][0]
    j = i + 1
    while j < len(L) and not L[j].startswith('      - '): j += 1
    return '\n'.join(L[i:j])
print('pre-run step raw bytes identical:', raw_step(nb, 'pre-run pin check') == raw_step(ob, 'pre-run pin check'))
print('fetch step raw identical:', raw_step(nb, 'fetch F') == raw_step(ob, 'fetch F'))
src = open(os.path.join(new, 'tools/ledger_coverage/adapters/conformance_controls.py')).read()
m = re.search(r"def extract_prerun\(blob\):.*?return m.group\(1\) if m else None\n", src, re.S)
ns = {'re': re}; exec(m.group(0), ns)
argv = shlex.split(pre['run'])
ext = ns['extract_prerun'](nb)
print('pre-run argv prefix', argv[:-1], '; YAML program == extract_prerun:', argv[-1] == ext,
      'len', len(ext), 'sha256', hashlib.sha256(ext.encode()).hexdigest()[:16])
inputs = d[True]['workflow_dispatch']['inputs']
print('inputs', {k: (v['type'], v['required']) for k, v in inputs.items()})
opts = inputs['check']['options']; print('choice values', len(opts), len(set(opts)))
print('choice values equal to 3184c7f9:', opts == do[True]['workflow_dispatch']['inputs']['check']['options'])
run = [s for s in st if s.get('name') == 'ledger coverage'][0]
print('env', run['env'])
print('no ${{ in any run:', all('${{' not in (s.get('run') or '') for s in st))
print('every env value is a single ${{ inputs.<name> }} or github.token:',
      all(re.fullmatch(r'\$\{\{ (inputs\.[a-z]+|github\.token) \}\}', v) for v in run['env'].values()))
blk = run['run']
# quoting: every $ expansion in the block appears inside double quotes
unq = []
for line in blk.split('\n'):
    inq = False
    for k, ch in enumerate(line):
        if ch == '"': inq = not inq
        if ch == '$' and not inq: unq.append(line.strip()[:60])
print('unquoted expansions:', unq)
print('python3 invocations all -I -S -B:', all(x == 'exec python3 -I -S -B tools/ledger_coverage.py' for x in re.findall(r'exec python3[^\n]*?tools/ledger_coverage\.py', blk)),
      len(re.findall(r'exec python3', blk)))
r = subprocess.run(['bash', '-n', '-c', blk], capture_output=True, text=True); print('bash -n', r.returncode, r.stderr)
open(os.path.join(work, 'runblock.sh'), 'w').write(blk)
# independent expectation from PREREG s32.4 (r5), the r5 configuration's paths and the owner's D-2 (b)
P = 'verification/audits/foundations/a1exit-deletion-20261121'
A = 'verification/audits/foundations/ledger-coverage-tool-20261123'
V = dict(F='f' * 40, CFG=P + '/retirement-config.json', H='a' * 40, X='b' * 40, C='c' * 40, E='e' * 40, M='d' * 40, L='9' * 40,
         RUNNER_TEMP='/rt')
F = V['F']
com = ['-I', '-S', '-B', 'tools/ledger_coverage.py']
base = ['--freeze', F, '--config', F + ':' + V['CFG'], '--out', '/rt/out']
led, eds = ['--ledger', F + ':' + P + '/ledger.json'], ['--edits', F + ':' + P + '/edits.json']
dele = ['--delegation', F + ':' + A + '/delegation-draft.json']
gr58 = ['--classify', F + ':' + A + '/records/gr58-hit-classification-v1.json']
exe = lambda *a: com + ['execution'] + base + ['--scientific-base', V['H']] + list(a)
EXP = {
 'item1-execution': exe('--candidate', V['X'], *led, *eds),
 'item1-terms': com + ['terms'] + base + ['--commit', V['X'], '--profile', 'ptr'] + gr58,
 'item2-record': com + ['record'] + base + ['--pin', V['E'], '--record', F],
 'item2-coverage': com + ['coverage'] + base + ['--commit', V['X'], '--segment', V['E'] + '..' + V['H'],
                    '--segment', V['H'] + '..' + V['X'] + '=' + F + ':' + P + '/ledger.json', '--hp', F + ':' + P + '/hp.json'] + gr58,
 'item7': com + ['terms'] + base + ['--commit', V['X'], '--profile', 'item7-literal'],
 'item7-amended': com + ['terms'] + base + ['--commit', V['X'], '--base', V['H'], *led, '--check', 'item7', '--final'] + gr58,
 'item11': com + ['terms'] + base + ['--commit', V['X'], '--check', 'item11', '--scope', F + ':' + A + '/records/repo-scope-v1.json', '--final'],
 'item14': exe('--main', V['M'], '--candidate', V['X'], *led, *eds, *dele),
 'item14-landing': exe('--main', V['M'], '--certified', V['C'], '--landing', V['L'], '--candidate', V['X'], *led, *eds, *dele),
}
for k in ('item3', 'item4', 'item5', 'item6', 'item8', 'item9', 'item10', 'item12', 'item13'):
    EXP[k] = exe('--candidate', V['X'], *led, *eds, *dele)
assert set(EXP) == set(opts), set(EXP) ^ set(opts)
env0 = {'PATH': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'stub') + ':/usr/bin:/bin'}
def run_block(check, **over):
    out = os.path.join(work, 'argv.txt')
    if os.path.exists(out): os.remove(out)
    env = dict(env0, **V, CHECK=check, STUBOUT=out); env.update(over)
    p = subprocess.run(['bash', '-e', '-c', blk], env=env, capture_output=True, text=True, cwd=work)
    a = open(out).read().split('\n')[:-1] if os.path.exists(out) else None
    return p.returncode, a
bad = 0
for k in opts:
    rc, a = run_block(k)
    ok = rc == 0 and a == EXP[k]
    bad += not ok
    print('%-16s %s' % (k, 'argv == expectation' if ok else 'MISMATCH rc=%s\n  got %s\n  exp %s' % (rc, a, EXP[k])))
print('arms mismatching the independent expectation:', bad)
for k in ['bogus', '*', 'item3 item4', 'item1-terms;id', '', 'item1-term?', 'ITEM3', 'item3|item4', ' item3', 'item14-landing\n']:
    rc, a = run_block(k); print('unknown %-18r exit %s argv %s' % (k, rc, a))
# injection in every input, including the new c
evil = {'C': '--landing=evil', 'X': '$(touch PWNED)', 'H': '`touch PWNED2`', 'E': 'a;touch PWNED3', 'M': '*', 'L': 'x y',
        'F': '--repo=<tmp>/x', 'CFG': 'a/$(touch PWNED4)/b'}
rc, a = run_block('item14-landing', **evil)
print('injection item14-landing exit', rc); print('  argv', a)
print('  files created:', [f for f in os.listdir(work) if f.startswith('PWNED')])
rc, a = run_block('item2-coverage', **evil); print('injection item2-coverage exit', rc, 'argv count', len(a))
print('  files created:', [f for f in os.listdir(work) if f.startswith('PWNED')])
# an empty C: one empty argv element (argparse then reads '' as the value)
rc, a = run_block('item14-landing', C=''); i = a.index('--certified'); print('empty C ->', repr(a[i + 1]))
