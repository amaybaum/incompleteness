"""Reviewer probe: try to break EI6's predicate at 4f4a9d58. usage: python3 -I ei6_break.py TREE WORK"""
import importlib.util, json, os, re, subprocess, sys, zipfile
tree, work = sys.argv[1], sys.argv[2]
os.makedirs(work, exist_ok=True)
spec = importlib.util.spec_from_file_location('cc', os.path.join(tree, 'tools/ledger_coverage/adapters/conformance_controls.py'))
cc = importlib.util.module_from_spec(spec); spec.loader.exec_module(cc)
stdlib = sorted({os.path.realpath(x) for x in json.loads(subprocess.run([sys.executable,'-I','-S','-c','import sys,json;print(json.dumps(sys.path))'],cwd='/',capture_output=True,text=True).stdout) if x})
installed = cc._installed_dirs()
print('stdlib', stdlib); print('installed', sorted(installed))
A = lambda f, st=stdlib, ins=installed: cc.ei6_allowed(os.path.realpath(f), set(), st, ins)
res = {}
def t(name, f, expect, st=stdlib, ins=installed):
    got = A(f, st, ins); res[name] = (f, got, expect, 'ok' if got == expect else 'UNEXPECTED'); print('%-55s %-5s exp %-5s %s' % (name, got, expect, '' if got==expect else '<<< UNEXPECTED'))

# 1 installed package by real path and via the site-packages symlink name
t('certifi real path', '/usr/local/lib/python3.13/dist-packages/certifi/core.py', False)
t('certifi via site-packages symlink', '/usr/local/lib/python3.13/site-packages/certifi/core.py', False)
t('debian system dist-packages', '/usr/lib/python3/dist-packages/six.py', False)
t('user site', os.path.expanduser('~/.local/lib/python3.13/site-packages/x.py'), False)
t('egg/zip inside site-packages', '/usr/local/lib/python3.13/site-packages/foo.egg/foo/__init__.py', False)
t('stdlib-prefix sibling dir', '/usr/local/lib/python3.13-evil/x.py', False)
t('stdlib-prefix sibling dir 2', '/usr/local/lib/python3.13x/x.py', False)
t('lib-dynload so', [os.path.join('/usr/local/lib/python3.13/lib-dynload', n) for n in os.listdir('/usr/local/lib/python3.13/lib-dynload')][0], True)
t('stdlib json', '/usr/local/lib/python3.13/json/__init__.py', True)
t('stdlib zip member', '/usr/local/lib/python313.zip/json/__init__.pyc', True)
t('stdlib __pycache__', '/usr/local/lib/python3.13/json/__pycache__/__init__.cpython-313.pyc', True)
t('sitecustomize in stdlib dir (image file)', '/usr/local/lib/python3.13/sitecustomize.py', True)
# symlinked site dir under stdlib with a non-standard real name: only the real-path rule refuses
S = os.path.join(work, 'symstd'); os.makedirs(os.path.join(S, 'vendor', 'pkg'), exist_ok=True)
open(os.path.join(S, 'vendor', 'pkg', '__init__.py'), 'w').write('')
if not os.path.lexists(os.path.join(S, 'site-packages')): os.symlink('vendor', os.path.join(S, 'site-packages'))
rS = os.path.realpath(S); ins2 = set(installed) | {os.path.realpath(os.path.join(S, 'site-packages'))}
t('symlinked site dir, real name vendor (real-path rule)', os.path.join(S, 'site-packages/pkg/__init__.py'), False, stdlib + [rS], ins2)
# D02 equivalent: real-path rule removed (installed empty), name rule only
t('  same under D02 (no real-path rule)', os.path.join(S, 'site-packages/pkg/__init__.py'), False, stdlib + [rS], set())
t('certifi under D02', '/usr/local/lib/python3.13/dist-packages/certifi/core.py', False, stdlib, set())
# installed dir name in a deeper component
t('nested site-packages deep under stdlib', '/usr/local/lib/python3.13/a/b/site-packages/c/d.py', False)
t('file named site-packages.py in stdlib', '/usr/local/lib/python3.13/site-packages.py', True)
t('dir dist-packages2 under stdlib (not installed)', '/usr/local/lib/python3.13/dist-packages2/x.py', True)
# .pth: a real -I -B run (site active) with a .pth in a temp site dir is not EI's flags; under -S no .pth is read
P = os.path.join(work, 'pth'); os.makedirs(os.path.join(P, 'tgt'), exist_ok=True)
open(os.path.join(P, 'tgt', 'pthmod.py'), 'w').write('X=1\n')
r = subprocess.run([sys.executable, '-I', '-S', '-B', '-v', '-c', 'import pthmod'], cwd=P, capture_output=True, text=True)
print('-S run with pthmod importable only via .pth: exit', r.returncode, '(nonzero means .pth not processed)')
# real traced -I (no -S) run: does anything the site machinery loads get admitted?
r = subprocess.run([sys.executable, '-I', '-B', '-v', '-c', 'import certifi'], cwd='/', capture_output=True, text=True)
tr = sorted({os.path.realpath(f) for f in re.findall(cc._TRACE, r.stderr)})
adm = [f for f in tr if A(f)]
non_std = [f for f in adm if not any(f.startswith(s + os.sep) for s in stdlib)]
print('-I -B run importing certifi: traced', len(tr), 'admitted', len(adm), 'refused', [f for f in tr if not A(f)])
print('admitted files that are site hooks:', [f for f in adm if 'sitecustom' in f or 'usercustom' in f or '_distutils' in f])
# namespace package portion in dist-packages
N = '/usr/local/lib/python3.13/dist-packages'
ns = [d for d in os.listdir(N) if os.path.isdir(os.path.join(N,d)) and not os.path.exists(os.path.join(N,d,'__init__.py')) and not d.endswith(('info','__pycache__'))][:3]
for d in ns:
    fs = [f for f in os.listdir(os.path.join(N,d)) if f.endswith('.py')][:1]
    if fs: t('namespace-portion module '+d, os.path.join(N,d,fs[0]), False)
json.dump(res, open(os.path.join(work, 'ei6_break.json'), 'w'), indent=1)
print('UNEXPECTED count', sum(1 for v in res.values() if v[3] != 'ok'))
