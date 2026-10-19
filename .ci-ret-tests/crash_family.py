"""The KeyError crash family (scratch; never committed; the worktree is never written). argv: <worktree> <mutant> <mode> <outdir>
mode 'cli'       : the mutated check_objects.py run as its CLI would run it (main(['--self-test'])), in a subprocess,
                   so the exit code and the uncaught traceback are the CLI's.
mode 'casewise'  : the same mutant, with one scratch harness edit in the self-test only: an exception raised by a
                   case's own `also` condition is caught, its traceback recorded, and the case reported FAILS (red),
                   so every later case still runs. The checker code itself is the mutant's, unchanged.
Mutant edits are read from mutants_all.py."""
import io, contextlib, os, re, subprocess, sys, traceback, types

WT, which, mode, OUT = sys.argv[1:5]
HERE = os.path.dirname(os.path.abspath(__file__))
src_m = open(os.path.join(HERE, 'mutants_all.py')).read().split('origin, fn, kind, reason, edits, want = M[which]')[0]
ns = {}
exec(src_m.replace('wt, which, outdir = sys.argv[1:4]', 'wt, which, outdir = %r, None, None' % WT), ns)
origin, fn, kind, reason, edits, want = ns['M'][which]
A = os.path.join(WT, 'verification/audits/evidence-retention')
path = os.path.join(A, fn)
src = open(path, encoding='utf-8').read()
for old, new in edits:
    assert src.count(old) == 1
    src = src.replace(old, new)
if mode == 'cli':
    code = ('import sys, types\nsrc = open(%r, encoding="utf-8").read()\nmod = types.ModuleType("__main_mut__")\n'
            'mod.__file__ = %r\nexec(compile(src, %r, "exec"), mod.__dict__)\nsys.exit(mod.main(["--self-test"]))\n'
            % (os.path.join(OUT, which + '.mutated.py'), path, path))
    open(os.path.join(OUT, which + '.mutated.py'), 'w', encoding='utf-8').write(src)
    p = subprocess.run([sys.executable, '-I', '-B', '-c', code], cwd=WT, capture_output=True, text=True,
                       env=dict(os.environ, TMPDIR=os.environ.get('TMPDIR', '/tmp')))
    os.remove(os.path.join(OUT, which + '.mutated.py'))
    open(os.path.join(OUT, which + '.cli.out'), 'w').write(p.stdout + '\n--- stderr ---\n' + p.stderr)
    tb = [l for l in p.stderr.split('\n') if l.strip()]
    print('%s cli: exit %d; stdout case lines %d; stderr tail:' % (which, p.returncode,
          sum(1 for l in p.stdout.split('\n') if 'as required' in l or 'NOT DETECTED' in l)))
    for l in tb[-8:]:
        print('    ' + l)
    sys.exit(0)
# casewise: catch an exception of a case's `also` condition, and report the case red
harness_old = "                    extra = also is None or also(info)\n"
harness_new = ("                    try:\n                        extra = also is None or also(info)\n"
               "                    except Exception:\n                        import traceback as _tb\n"
               "                        CASE_EXC.append((name, _tb.format_exc()))\n                        extra = False\n")
assert src.count(harness_old) == 1
src = src.replace(harness_old, harness_new)
mod = types.ModuleType('casewise')
mod.__file__ = path
mod.__dict__['CASE_EXC'] = []
exec(compile(src, path, 'exec'), mod.__dict__)
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    rc = mod.self_test(mod.ROOT)
out = buf.getvalue()
open(os.path.join(OUT, which + '.casewise.out'), 'w').write(out + '\n--- caught case exceptions ---\n' +
                                                            '\n'.join('%s\n%s' % x for x in mod.CASE_EXC))
red = [re.split(r'\s{2,}', l.strip())[0] for l in out.split('\n')
       if re.search(r'\s(NOT DETECTED|FAILS)(\s|$)', l) and 'as required' not in l]
print('%s casewise: self-test rc %s; cases %s; red %d; caught case exceptions %d' % (
    which, rc, re.search(r'\((\d+) cases\)', out).group(1) if re.search(r'\((\d+) cases\)', out) else '?', len(red),
    len(mod.CASE_EXC)))
for r in red:
    print('    red: ' + r)
for name, tb in mod.CASE_EXC:
    print('    exception in case %r:' % name)
    for l in tb.strip().split('\n')[-4:]:
        print('        ' + l)
for t in want or []:
    print('    target %-100s %s' % (t[:100], 'RED (detected)' if any(r == t or r.startswith(t) for r in red) else 'green'))
killed = bool(want) and all(any(r == t or r.startswith(t) for r in red) for t in want)
print('%s casewise: %s' % (which, 'KILLED' if killed else 'SURVIVED'))
