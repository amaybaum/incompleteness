p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/rd/controls.py'
t = open(p).read()
old = """        out[name] = ([('the guard', evaluate(fn_src, name, var, text)),
                      ('the sought strings removed outside it', evaluate(fn_src, name, var, stripped)),
                      ('its own definition alone', evaluate(fn_src, name, var, fn_src))], n_out)
    return out
"""
new = """        # the countercontrols: the evaluation can fail, on a text without the strings, or, for the
        # one negative conjunct, on a text carrying the statement it forbids
        counter = [('a text without its strings', evaluate(fn_src, name, var, ''))]
        if name == '_oln_supersession':
            counter.append(('the guard with the forbidden statement appended', evaluate(
                fn_src, name, var, text + "\\nif not (_MANIFEST_BASELINE == {'base': _OLT_B\\n")))
        out[name] = ([('the guard', evaluate(fn_src, name, var, text)),
                      ('the sought strings removed outside it', evaluate(fn_src, name, var, stripped)),
                      ('its own definition alone', evaluate(fn_src, name, var, fn_src))], n_out,
                     counter)
    return out
"""
assert t.count(old) == 1; t = t.replace(old, new)
old = """        for name, (evals, n_out) in vacuity_of(text).items():
            for what, v in evals:
                lines.append('%s  %-5s %s on %s: %s' % ('EVAL' if required else 'NOTE', label, name,
                                                        what, 'holds' if v else 'FAILS'))
                ok &= v or not required
"""
new = """        for name, (evals, n_out, counter) in vacuity_of(text).items():
            for what, v in evals:
                lines.append('%s  %-5s %s on %s: %s' % ('EVAL' if required else 'NOTE', label, name,
                                                        what, 'holds' if v else 'FAILS'))
                ok &= v or not required
            for what, v in counter if required else ():
                lines.append('COUNTERCONTROL  %s on %s: %s' % (name, what, 'holds' if v else 'FAILS'))
                ok &= not v
"""
assert t.count(old) == 1; t = t.replace(old, new)
t = t.replace("""          definitions removed, and on their own definitions alone, all of which must hold. Also
          reported, not required: the same evaluations on the guard at <D>.""",
"""          definitions removed, and on their own definitions alone, all of which must hold; the
          countercontrols, which must fail: each on a text without its strings, and
          _oln_supersession on the guard with the statement it forbids appended. Also reported,
          not required: the same evaluations on the guard at <D>.""")
open(p, 'w').write(t)
