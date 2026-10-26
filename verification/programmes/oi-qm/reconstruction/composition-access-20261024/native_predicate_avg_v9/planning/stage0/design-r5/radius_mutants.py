"""Toys only: cone-radius variants on even-class contexts (Phi even, L = 4).
'symmetric parity-blind' (far radius d, parity ignored) should be equivalent to the
correct cone; 'far cone deleted' is what r1's symmetric variant actually was;
radius offsets of -2 / +2 (parity-preserving) are the meaningful under/over-coverage
mutants. Standard library."""
import random, sys
sys.path.insert(0, sys.argv[1])
from proto import Geometry, axes, add, dist, ball, even  # noqa: E402

class Radius(Geometry):
    def __init__(self, *a, delta=0, symblind=False, fardel=False, **k):
        super().__init__(*a, **k); self.delta, self.symblind, self.fardel = delta, symblind, fardel
    def in_cone(self, u, q):
        (uc, us), (c, t) = u, q
        d, ty = self.depth(q)
        near, far = self.slices(ty)
        r = dist(uc, c)
        if us == near:
            rr = d+self.delta; par = True
        elif us == far:
            if self.fardel: return False
            rr = (d if self.symblind else d-1)+self.delta; par = not self.symblind
        else:
            return False
        if rr < 0 or r > rr: return False
        return (not par) or (r-rr) % 2 == 0

D, L = 3, 4
AX = axes(D)
FIXED = {(e, L-1) for e in AX} | {((0, 0, 0), L), ((0, 0, 0), L-2)}
pool = [q for q in ((c, t) for c in ball(2, D) for t in range(L-3, L+3)) if even(q) and q not in FIXED]
gc = Geometry(D, L)
vs = {'symmetric parity-blind': Radius(D, L, symblind=True), 'far cone deleted': Radius(D, L, fardel=True),
      'radius -2': Radius(D, L, delta=-2), 'radius +2': Radius(D, L, delta=2)}
rng = random.Random(17)
cnt = {k: [0, 0] for k in vs}   # [retains more, retains less]
for _ in range(400):
    S = set(rng.sample(pool, rng.randint(2, 10)))
    a = gc.closure(FIXED, S)
    for k, g in vs.items():
        b = g.closure(FIXED, S)
        cnt[k][0] += not (b <= a); cnt[k][1] += not (a <= b)
for k, (m, l) in cnt.items():
    print('%-24s random sets: retains something extra %d/400, loses something %d/400' % (k, m, l))
# planted cases: HC pair (must collapse), block minus centre (must collapse), depth-2 family (must be kept)
q1, q2 = ((0, 0, 0), L+2), ((1, 0, 0), L+1)
c0 = (1, 0, 0)
blk_mc = {(c0, L+1)} | {(add(c0, e), L) for e in AX}
q = ((0, 0, 0), L+2)
fam = {q} | {(add((0, 0, 0), e, 2), L) for e in AX} | {(add((0, 0, 0), e, 1), L-1) for e in AX}
for name, g in [('correct', gc)] + list(vs.items()):
    print('%-24s HC %d (want 0)  block-minus-centre %d (want 0)  depth-2 family %d (want 13)' % (
        name, len(g.closure(set(), {q1, q2})), len(g.closure(set(), blk_mc)), len(g.closure(set(), fam))))
