"""Diagnostic: flip type of every essential atom (permutation / monomial-with-phases / neither), per orbit."""
import sys, pickle
sys.argv = ['t_k10.py', sys.argv[1] if len(sys.argv) > 1 else 'loci_af.pkl', '0']
exec(open('t_k10.py').read().split("n = okS = okR = 0")[0])
L = pickle.load(open(sys.argv[1], 'rb'))
from collections import Counter
cnt = Counter()
for nm, P in (('A', PA), ('B', PB), ('C', PC)):
    fp, fm = flip_perm_multi([P], [-1]), flip_monomial([P], [-1])
    print('H3', nm, 'perm', fp and (fp[0], [i for i, x in enumerate(fp[1]) if x != i]), 'monomial', fm and (fm[0], [i for i, x in enumerate(fm[1]) if x != i]))
for t in sorted(L):
    Ms = [cells_to_mat(a) for a in L[t]['atoms']]
    for k, M in enumerate(Ms):
        fp, fm = flip_perm_multi([M], [-1]), flip_monomial([M], [-1])
        typ = 'perm' if fp else ('monomial' if fm else 'neither')
        cnt[('%dx%d' % L[t]['shapes'][k], typ)] += 1
        if typ == 'monomial': print('orbit', t, 'atom', k + 1, L[t]['shapes'][k], 'monomial not permutation', fm[0], [i for i, x in enumerate(fm[1]) if x != i])
print(sorted(cnt.items()))
