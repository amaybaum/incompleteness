"""Local, never-pushed rehearsal of A32's lifecycle for one outcome row. Usage: sim_a30.py <row-kind>"""
import json, os, subprocess, sys, importlib.util
S = os.path.dirname(os.path.abspath(__file__))
kind = sys.argv[1]
WT = os.path.join(S, 'wt-sim33-' + kind)
D = 'db82376dfc0e2ae561ec541fd0d3a915f082beda'
REPO = '/home/user/incompleteness'
def sh(*a, cwd=WT, inp=None):
    r = subprocess.run(a, cwd=cwd, capture_output=True, text=True, input=inp)
    if r.returncode: print(r.stdout, r.stderr); raise SystemExit('failed: %s' % (a,))
    return r.stdout.strip()
spec = importlib.util.spec_from_file_location('controls', os.path.join(S, 'controls.py'))
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
vec = {'classified': 'A33-CLASSIFIED', 'notclassified': 'A33-NOT-CLASSIFIED', 'undecided': 'A33-UNDECIDED'}[kind]
if os.path.exists(WT):
    sh('git', 'worktree', 'remove', '--force', WT, cwd=REPO)
sh('git', 'worktree', 'add', '--detach', WT, D, cwd=REPO)
env_msg = 'sim\n'
os.makedirs(os.path.join(WT, C.RDIR), exist_ok=True)
open(os.path.join(WT, C.RDIR, 'preregistration.md'), 'w', encoding='utf-8').write(
    open(os.path.join(S, 'preregistration.md'), encoding='utf-8').read())
sh('git', 'add', '-A'); sh('git', 'commit', '-qm', 'F (sim)')
F = sh('git', 'rev-parse', 'HEAD')
fd = {p: sh('git', 'show', '%s:%s' % (D, p)) + '\n' for p in (C.GUARD, C.ROADMAP, C.CENSUS, C.ROOT)}
fd = {p: subprocess.run(['git', 'show', '%s:%s' % (D, p)], cwd=WT, capture_output=True).stdout.decode()
      for p in (C.GUARD, C.ROADMAP, C.CENSUS, C.ROOT)}
fe, _ = C._synthetic_e(fd, vec)
open(os.path.join(WT, C.RDIR, 'controls.py'), 'w', encoding='utf-8').write(
    open(os.path.join(S, 'controls.py'), encoding='utf-8').read())
for p, t in fe.items():
    open(os.path.join(WT, p), 'w', encoding='utf-8').write(t)
sh('git', 'add', '-A'); sh('git', 'commit', '-qm', 'E (sim)')
E = sh('git', 'rev-parse', 'HEAD')
print(sh('python3', os.path.join(WT, C.RDIR, 'controls.py'), 'check', E))
print(sh('python3', os.path.join(WT, C.RDIR, 'controls.py'), '--self-test'))
sh('git', 'checkout', '-q', '--detach', D)
sh('git', 'merge', '-q', '--no-ff', '-m', 'Lambda (sim)', E)
L = sh('git', 'rev-parse', 'HEAD')
P = 'https://github.com/amaybaum/incompleteness'
sh('python3', 'tools/v3_receipt.py', '--status', 'complete', '--d', D, '--f', F, '--e', E,
   '--reconciliation', L,
   '--attest', 'owner-designation', 'F', P + '/pull/1#issuecomment-1',
   '--attest', 'check-run', 'F', P + '/actions/runs/1',
   '--attest', 'owner-designation', 'E', P + '/pull/1#issuecomment-2',
   '--attest', 'check-run', 'E', P + '/actions/runs/2', '--out', 'verification/receipts/A33.json')
sh('git', 'add', '-A'); sh('git', 'commit', '-qm', 'Q (sim)')
Q = sh('git', 'rev-parse', 'HEAD')
print(sh('python3', 'tools/v3_verifier.py', '--verify-round', Q).splitlines()[-1])
print(sh('python3', 'tools/v3_verifier.py', '--receipts', Q).splitlines()[-1])
print(sh('python3', 'tools/legacy_records_check.py', Q).splitlines()[-1])
print('changed D..E:', len(sh('git', 'diff', '--no-renames', '--name-status', D, E).splitlines()))
print(sh('git', 'diff', '--no-renames', '--name-status', D, Q))
sh('git', 'worktree', 'remove', '--force', WT, cwd=REPO)
