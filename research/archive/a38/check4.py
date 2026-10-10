import sys, time; sys.path.insert(0, 'a38')
from lib38b import *
t0 = time.time()
T = defect_rows(SIG)
# nullspace bases of L_S ∩ T for the 18 strict structures; the dimension of their sum inside T
bases = []
for s in CENSUS9:
    for tr in (False, True):
        B = nullspace(T + struct_eqs(s[0], s[1], s[2], False, tr)); bases.append(B)
allv = [v for B in bases for v in B]
print('sum of the 18 strict (L_S ∩ T): dim', rank_int(allv), 'of dim T = 80', '%.0fs' % (time.time() - t0))
# by shape family
for fam, names in (('4x4', ('k1', 'k2', 'k3', 'k4')), ('8x2', ('e1', 'e2')), ('2x8', ('t1', 't2', 't3'))):
    vs = [v for (s, B) in zip([(s, tr) for s in CENSUS9 for tr in (False, True)], bases) if NAMES9[s[0]] in names for v in B]
    print(fam, 'sum dim', rank_int(vs))
