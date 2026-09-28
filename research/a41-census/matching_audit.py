"""Gem-finding check: does the sorted label matching of the act-36/37 structure search hide exact Dita structures?
For every candidate (index sets passing the proportionality test) that the search reports as not exact, test every
label matching exactly (monomial calculus). Cases: SIG (act 36 census), the W arc at generic u (act 37), the act-38
witness arc at generic u."""
import itertools, json
from lib41 import *
from matchlib import valid_per_group, n_matchings
def mdiv3(x, y): return ((x[0] - y[0]) % 4, x[1] - y[1], x[2] - y[2])
out = {}
cases = [('SIG', lambda i, j: SIGE[i][j], mdiv3, None),
         ('SIG^T', lambda i, j: SIGE[j][i], mdiv3, None),
         ('W-arc generic', gen_entry, gen_div, None),
         ('W-arc generic, transpose', lambda i, j: gen_entry(j, i), gen_div, None),
         ('A38 witness generic', ent_of(EE), gen_div, None),
         ('A38 witness generic, transpose', ent_of(ET), gen_div, None)]
for name, ent, div, _ in cases:
    for (m, n) in SHAPES:
        ratio = [[[div(ent(i, s), ent(i, s0)) for s in range(16)] for s0 in range(16)] for i in range(16)]
        mul = (lambda a, b: ((a[0] + b[0]) % 4, a[1] + b[1], a[2] + b[2])) if div is mdiv3 else gen_mul
        one = (0, 0, 0) if div is mdiv3 else GEN_ONE
        cands, exact = structures(ent, div, mul, lambda x: x == one, m, n, ratio)
        rec = []
        for cp, rows in cands:
            vs = n_matchings(valid_per_group(ent, cp, rows, False, div)); vr = n_matchings(valid_per_group(ent, cp, rows, True, div))
            rec.append({'blocks': cp, 'groups': rows, 'sorted_exact': (cp, rows) in exact, 'valid_strict_matchings': vs, 'valid_relaxed_matchings': vr})
        out['%s %dx%d' % (name, m, n)] = rec
        print('%-32s %dx%d candidates %2d sorted-exact %2d | exact under some matching: strict %2d relaxed %2d' % (name, m, n, len(cands), len(exact),
              sum(1 for r in rec if r['valid_strict_matchings']), sum(1 for r in rec if r['valid_relaxed_matchings'])), flush=True)
json.dump(out, open('matching_audit.json', 'w'), default=str, indent=0)
