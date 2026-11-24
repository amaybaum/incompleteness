"""C08 probe: a SYSTEM git configuration (GIT_CONFIG_SYSTEM) defining a required smudge filter; Native.clone must not
run it; countercontrol: plain clone+checkout with that system config in force runs it. Also, for information,
the same filter supplied via GIT_CONFIG_COUNT/KEY/VALUE environment variables."""
import os, subprocess, sys, importlib.util, shutil
T, P, mode = sys.argv[1], sys.argv[2], sys.argv[3]
spec = importlib.util.spec_from_file_location('ledger_coverage', T + '/tools/ledger_coverage/__init__.py',
                                              submodule_search_locations=[T + '/tools/ledger_coverage'])
m = importlib.util.module_from_spec(spec); sys.modules['ledger_coverage'] = m; spec.loader.exec_module(m)
from ledger_coverage.engine import delegation, gitobj
P = P + '/' + mode; shutil.rmtree(P, ignore_errors=True); os.makedirs(P)
src, out, marker = P + '/src', P + '/out', P + '/MARKER'
env = dict(os.environ, GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull, GIT_AUTHOR_NAME='p', GIT_AUTHOR_EMAIL='p',
           GIT_COMMITTER_NAME='p', GIT_COMMITTER_EMAIL='p')
g = lambda *a: subprocess.run(['git', '-C', src] + list(a), env=env, capture_output=True, text=True)
os.makedirs(src); g('init', '-q'); open(src + '/.gitattributes', 'w').write('*.txt filter=evil\n'); open(src + '/a.txt', 'w').write('x\n')
g('add', '.'); g('commit', '-qm', 'c'); c = g('rev-parse', 'HEAD').stdout.strip()
os.environ['GIT_CONFIG_GLOBAL'] = os.devnull
cmd = "sh -c 'touch %s; cat'" % marker
if mode == 'system':
    f = P + '/systemconfig'
    open(f, 'w').write('[filter "evil"]\n\tsmudge = "%s"\n\trequired = true\n' % cmd.replace('"', '\\"'))
    os.environ['GIT_CONFIG_SYSTEM'] = f
    os.environ.pop('GIT_CONFIG_NOSYSTEM', None)
else:
    os.environ.update(GIT_CONFIG_COUNT='2', GIT_CONFIG_KEY_0='filter.evil.smudge', GIT_CONFIG_VALUE_0=cmd,
                      GIT_CONFIG_KEY_1='filter.evil.required', GIT_CONFIG_VALUE_1='true')
n = delegation.Native(gitobj.GitRepo(src), src, out, c, True)
try:
    d = n.clone(c); err = None
except Exception as e:
    d = None; err = repr(e)
print(mode, 'Native.clone: marker written:', os.path.exists(marker), 'err', err)
if os.path.exists(marker): os.remove(marker)
cc = P + '/counter'
subprocess.run(['git', 'clone', '-q', '--no-local', '--no-checkout', src, cc], env=dict(os.environ), capture_output=True)
r = subprocess.run(['git', '-C', cc, 'checkout', '-q', '--detach', c], env=dict(os.environ), capture_output=True, text=True)
print(mode, 'countercontrol: marker written:', os.path.exists(marker), r.returncode)
