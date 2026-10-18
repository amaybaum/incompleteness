"""Unmutated control: run each checker's self-test exactly as mutants_all.py does, with no edits. argv: <worktree> <outdir>.
Exit 0 iff both self-tests return 0 with no red case."""
import contextlib, io, os, re, sys, types
wt, outdir = sys.argv[1:3]
A = os.path.join(wt, 'verification/audits/evidence-retention')
bad = 0
for fn in ('check_objects.py', 'check_retention.py'):
    src = open(os.path.join(A, fn), encoding='utf-8').read()
    mod = types.ModuleType('base_' + fn[:-3])
    mod.__file__ = os.path.join(A, fn)
    exec(compile(src, '<%s baseline>' % fn, 'exec'), mod.__dict__)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            rc = mod.self_test(mod.ROOT) if fn == 'check_objects.py' else \
                mod.self_test(A, os.path.abspath(os.path.join(A, '..', '..', '..')))
        except Exception as exc:
            rc = 'crash %r' % exc
    out = buf.getvalue()
    open(os.path.join(outdir, 'baseline-' + fn[:-3] + '.out'), 'w').write(out)
    if fn == 'check_objects.py':
        red = [l for l in out.split('\n') if re.search(r'\s(NOT DETECTED|FAILS)(\s|$)', l) and 'as required' not in l]
    else:
        red = [l for l in out.split('\n') if l.startswith('FAIL self: ')]
    print('baseline %s: self-test rc %s; red cases %d' % (fn, rc, len(red)))
    for l in red:
        print('    red: ' + l.strip()[:170])
    bad |= rc != 0 or bool(red)
print('BASELINE %s' % ('CLEAN' if not bad else 'NOT CLEAN'))
sys.exit(1 if bad else 0)
