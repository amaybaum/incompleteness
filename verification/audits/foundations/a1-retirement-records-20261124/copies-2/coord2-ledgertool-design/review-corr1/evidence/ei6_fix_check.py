"""Checks a candidate EI6 predicate: under an -I -S directory and not under the interpreter's purelib/platlib."""
import sys, os, re, subprocess, json
q = subprocess.run([sys.executable, '-I', '-S', '-c', 'import sys, json, sysconfig; p = sysconfig.get_paths(); '
                    'print(json.dumps([sys.path, [p["purelib"], p["platlib"]]]))'], capture_output=True, text=True, cwd='/')
path, pkgs = json.loads(q.stdout)
dirs = {os.path.realpath(x) for x in path if x}; pk = {os.path.realpath(x) for x in pkgs}
ok = lambda f: any(f.startswith(s + os.sep) for s in dirs) and not any(f == x or f.startswith(x + os.sep) for x in pk)
T = sys.argv[1]
p = subprocess.run([sys.executable, '-I', '-S', '-B', '-v', 'tools/ledger_coverage.py', 'self-test', '--out', sys.argv[2]],
                   capture_output=True, text=True, cwd=T)
loaded = sorted(set(re.findall(r"(?:code object from|matches|loaded from) '?([^'\s]+\.(?:pyc|py|so))\b", p.stderr)))
outside = [f for f in loaded if not os.path.realpath(f).startswith(os.path.realpath(T) + os.sep)]
print('tool run exit', p.returncode, 'imports outside the tree', len(outside), 'refused by candidate', [f for f in outside if not ok(os.path.realpath(f))][:5])
c = os.path.realpath('/usr/local/lib/python3.13/site-packages/certifi/__init__.py'); print('certifi', c, 'refused:', not ok(c))
