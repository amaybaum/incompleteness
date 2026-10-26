"""Toy design check (not v8's class): (1) native bijection of a depth-d site-time in
its FAR-slice axis extreme at distance d-1, forward and backward; (2) closure with
near+far tips (L3') vs near-only (L3) on planted cases; (3) a depth-2 planted case
that catches the off-axis mutant."""
import random, sys
src = open(sys.argv[1]).read().split('# --- Hand-checked instance')[0]
ns = {}
exec(src, ns)
Geometry, ball, even, AX, add, H, dist = (ns[k] for k in ('Geometry', 'ball', 'even', 'AX', 'add', 'H', 'dist'))

def evolve(E, Ls, T, R):
    sl = [E, Ls]
    for t in range(T):
        p2, p1 = sl[-2], sl[-1]
        out = {}
        for x in ball(R+T-t-1):
            s = 0
            for st in AX:
                s ^= p1[add(x, st)]
            out[x] = p2[x] ^ H[s]
        sl.append(out)
    return sl

rng = random.Random(5)
T, R = 5, 0
cells = ball(R+T)
bad = tested = 0
for trial in range(200):
    E = {c: rng.randrange(8) for c in cells}
    Ls = {c: rng.randrange(8) for c in cells}
    d = rng.randint(1, T)
    e = rng.choice(AX)
    u = add((0, 0, 0), e, d-1)
    vals = set()
    for v in range(8):
        E2 = dict(E); E2[u] = v
        vals.add(evolve(E2, Ls, T, R)[d+1][(0, 0, 0)])   # sl[d+1] = slice L+d
    tested += 1; bad += len(vals) != 8
print('far-slice axis extreme at distance d-1: non-bijective %d of %d (forward)' % (bad, tested))
# off-axis far cell at distance d-1 (d>=3) for contrast
nb = 0
for trial in range(100):
    E = {c: rng.randrange(8) for c in cells}
    Ls = {c: rng.randrange(8) for c in cells}
    d = rng.randint(3, T)
    e = rng.choice(AX)
    f = rng.choice([s for s in AX if s != e and s != tuple(-i for i in e)])
    u = add(add((0, 0, 0), e, d-2), f)
    vals = set()
    for v in range(8):
        E2 = dict(E); E2[u] = v
        vals.add(evolve(E2, Ls, T, R)[d+1][(0, 0, 0)])
    nb += len(vals) != 8
print('far-slice OFF-axis cell at distance d-1: non-bijective %d of 100 (expected > 0)' % nb)

class Geo2(Geometry):
    """L3': near-slice axis extremes at distance d and far-slice axis extremes at d-1."""
    def tips(self, q):
        out = super().tips(q)
        c, t = q
        d, ty = self.depth(q)
        if d >= 1:
            far = self.E if ty == 'F' else self.L
            out |= {(add(c, e, d-1), far) for e in AX}
        return out

L = 3
g1, g2 = Geometry(L), Geo2(L)
g2o = Geo2(L); g2o.offaxis = True
PHI = {(e, L-1) for e in AX} | {((0, 0, 0), L)}
FIXED = PHI | {((0, 0, 0), L-2)}
top, centre = ((0, 0, 0), L+1), ((0, 0, 0), L-1)
six = {(e, L) for e in AX}
core = {top, centre} | six
print('constraint block: L3 retains %d, L3prime retains %d (of 8)' % (len(g1.closure(set(), core)), len(g2.closure(set(), core))))
print('block minus centre: L3 retains %d, L3prime retains %d' % (len(g1.closure(set(), core-{centre})), len(g2.closure(set(), core-{centre}))))
q2 = ((0, 0, 0), L+2)
planted = {q2} | {(add((0, 0, 0), e, 2), L) for e in AX} | {(e, L-1) for e in AX}
print('depth-2 planted: L3prime retains %d of %d; off-axis mutant retains %d' %
      (len(g2.closure(set(), planted)), len(planted), len(g2o.closure(set(), planted))))
# L3' never retains more than L3 (monotone strengthening) on random toy sets
pool = [q for q in ((c, t) for c in ball(2) for t in range(L-3, L+3)) if even(q) and q not in FIXED]
viol = 0
for trial in range(300):
    S = set(rng.sample(pool, rng.randint(2, 10)))
    viol += not (g2.closure(FIXED, S) <= g1.closure(FIXED, S))
print('L3prime retains a superset of L3 in %d/300 random toy sets (expected 0)' % viol)
