"""Is 'parity filter dropped' (in the cone test) an equivalent mutant on even-class contexts? Toy only."""
import sys, random
D = sys.argv[1]
src = open(D + '/toy_closure.py').read().split('# --- Hand-checked instance')[0]
ns = {}; exec(src, ns)
Geometry, ball, even, AX, add, dist = (ns[k] for k in ('Geometry', 'ball', 'even', 'AX', 'add', 'dist'))
class Geo2(Geometry):
    def tips(self, q):
        out = super().tips(q); c, t = q; d, ty = self.depth(q)
        if d >= 1:
            far = self.E if ty == 'F' else self.L
            out |= {(add(c, e, d-1), far) for e in AX}
        return out
class Geo2NoPar(Geo2):
    def in_cone(self, u, q):
        (uc, us), (c, t) = u, q
        d, ty = self.depth(q)
        near, far = (self.L, self.E) if ty == 'F' else (self.E, self.L)
        r = dist(uc, c)
        if us == near: return r <= d
        if us == far: return 0 <= r <= d-1
        return False
L = int(sys.argv[2])
PHI = {(e, L-1) for e in AX} | {((0, 0, 0), L)}
FIXED = PHI | {((0, 0, 0), L-2)}
pool = [q for q in ((c, t) for c in ball(2) for t in range(L-3, L+3)) if even(q) and q not in FIXED]
rng = random.Random(3); diff = 0
g, gn = Geo2(L), Geo2NoPar(L)
for _ in range(400):
    S = set(rng.sample(pool, rng.randint(2, 10)))
    diff += g.closure(FIXED, S) != gn.closure(FIXED, S)
print('parity-filter-dropped mutant differs on even-class sets: %d of 400' % diff)
print('L =', L, '; parity of Phi analogue:', sorted({(sum(map(abs, c))+t) % 2 for c, t in FIXED}), '; pool parity: 0 (even)')
