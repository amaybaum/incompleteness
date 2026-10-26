"""Re-run of the drafter's toy self-supporting search with the Phi analogue in the SAME parity class as
the pool (as in v8). Toy geometry only. Near-only L3 (drafter's Geometry) and L3' (near+far)."""
import sys, random, time
from itertools import combinations
D = sys.argv[1]; L = int(sys.argv[2])
src = open(D + '/toy_closure.py').read().split('# --- Hand-checked instance')[0]
ns = {}; exec(src, ns)
Geometry, ball, even, AX, add = (ns[k] for k in ('Geometry', 'ball', 'even', 'AX', 'add'))
class Geo2(Geometry):
    def tips(self, q):
        out = super().tips(q); c, t = q; d, ty = self.depth(q)
        if d >= 1:
            far = self.E if ty == 'F' else self.L
            out |= {(add(c, e, d-1), far) for e in AX}
        return out
PHI = {(e, L-1) for e in AX} | {((0, 0, 0), L)}
P = ((0, 0, 0), L-2)
FIXED = PHI | {P}
print('L', L, 'Phi/p parity', sorted({(sum(map(abs, c))+t) % 2 for c, t in FIXED}))
pool = [q for q in ((c, t) for c in ball(2) for t in range(L-3, L+3)) if even(q) and q not in FIXED]
print('pool', len(pool))
for name, g in (('L3', Geometry(L)), ("L3'", Geo2(L))):
    t0 = time.perf_counter(); found = []
    for k in (1, 2, 3):
        for S in combinations(pool, k):
            if g.closure(FIXED, set(S)) == set(S): found.append(S)
    print(name, 'self-supporting sets of size 1-3 with Phi active:', len(found), '(%.1fs)' % (time.perf_counter()-t0))
    for S in found[:6]: print('   ', S)
