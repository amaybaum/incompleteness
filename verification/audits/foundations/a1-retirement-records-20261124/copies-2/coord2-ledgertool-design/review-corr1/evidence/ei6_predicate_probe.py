"""EI6 predicate probe: the -I -S import path's directories (conformance_controls._interpreter_dirs at 3184c7f9) and the
predicate allowed_file (prefix test). Shows which of the interpreter's installed-package files the predicate admits."""
import sys, os, re, subprocess, importlib.util, sysconfig, json
T = sys.argv[1]
src = open(T + '/tools/ledger_coverage/adapters/conformance_controls.py').read()
fn = re.search(r"def _interpreter_dirs\(checkout\):.*?\n    return \{x for x in dirs if not \(x == root or x.startswith\(root \+ os.sep\)\)\}\n", src, re.S).group(0)
ns = {'subprocess': subprocess, 'sys': sys, 'json': json, 'os': os}; exec(fn, ns)
stdlib = ns['_interpreter_dirs'](sys.argv[2])
pred_src = re.search(r"\n(        return rf in pinned or any\(rf.startswith\(s \+ os.sep\) for s in stdlib\))", src).group(1)
print('predicate line at 3184c7f9:', pred_src.strip())
allowed = lambda rf: any(rf.startswith(s + os.sep) for s in stdlib)
print('-I -S dirs:', sorted(stdlib))
print('sysconfig purelib/platlib:', sysconfig.get_paths()['purelib'], sysconfig.get_paths()['platlib'])
# a real import of an installed (non-stdlib) package, traced as EI6 traces imports
p = subprocess.run([sys.executable, '-I', '-B', '-v', '-c', 'import certifi'], capture_output=True, text=True, cwd='/')
loaded = sorted(set(re.findall(r"(?:code object from|matches|loaded from) '?([^'\s]+\.(?:pyc|py|so))\b", p.stderr)))
pkg = [f for f in loaded if 'certifi' in f]
print('certifi (site-packages) files loaded:', len(pkg), pkg[:3])
print('admitted by the -I -S predicate:', [allowed(os.path.realpath(f)) for f in pkg][:3], 'all:', all(allowed(os.path.realpath(f)) for f in pkg))
print('dist-packages example admitted:', allowed('/usr/lib/python3/dist-packages/_distutils_hack/__init__.py'))
