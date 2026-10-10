import sys, time; sys.path.insert(0, 'a38')
from lib38b import *
t0 = time.time()
print('census names:', sorted(NAMES9.values()))
Wm = W_matrix()
# strict/relaxed membership of W itself in each structure (should be t1 column+row identically; others not)
print('W identically in (strict):', [(NAMES9[s], tr) for s in CENSUS9 for tr in (False, True) if in_structure([sum(Wm, [])], s, False, tr)])
print('W identically in (relaxed):', [(NAMES9[s], tr) for s in CENSUS9 for tr in (False, True) if in_structure([sum(Wm, [])], s, True, tr)])
# control: the zero matrix is in every structure; a gauge-trivial matrix is in every relaxed structure but not strict
Z = [[0]*16 for _ in range(16)]
print('0 strict all 18:', len([1 for s in CENSUS9 for tr in (False, True) if in_structure([sum(Z, [])], s, False, tr)]))
Gt = [[(i % 5) + (j % 3) for j in range(16)] for i in range(16)]
print('gauge-trivial strict / relaxed counts:', len([1 for s in CENSUS9 for tr in (False, True) if in_structure([sum(Gt, [])], s, False, tr)]), len([1 for s in CENSUS9 for tr in (False, True) if in_structure([sum(Gt, [])], s, True, tr)]))
# the straight lattice of W
B = straight_lattice(Wm)
print('dim L(Pi_W) (gauge fixed):', len(B), '%.1fs' % (time.time() - t0))
print('all basis vectors straight (exact):', all(straight_line_direct([v[i*16:(i+1)*16] for i in range(16)]) for v in B))
print('L(Pi_W) classes strict:', lattice_classes(B), ' relaxed:', lattice_classes(B, True))
# gauge normal of W in the span? W's normal form
Wn = gauge_normal(Wm)
print('W normal form straight:', straight_line(Wn))
# L(Pi_0): the gauge-trivial lattice should be 0-dimensional after gauge fixing
print('dim L(Pi_0):', len(straight_lattice(Z)))
print('%.1fs' % (time.time() - t0))
