"""R4: the r1 design toys re-run with the Phi analogue in the pool's parity class
(L = 4: Phi = six neighbours at L-1 and V at L, p at L-2, all even), plus native
3D checks of cone radii and near/far tip bijection, forward and backward.
Toy geometry only; not v8's class. Standard library."""
import random
import sys
import time
from itertools import combinations
sys.path.insert(0, sys.argv[1])
from proto import Geometry, axes, add, dist, ball, even, evolve_value  # noqa: E402

D, L = 3, 4
AX = axes(D)
PHI = {(e, L-1) for e in AX} | {((0, 0, 0), L)}
P = ((0, 0, 0), L-2)
FIXED = PHI | {P}
print('L', L, 'parity of fixed set', sorted({(sum(map(abs, c))+t) % 2 for c, t in FIXED}))
g3, g3p = Geometry(D, L, far=False), Geometry(D, L, far=True)

# 1. hand instance
q1, q2 = ((0, 0, 0), L+2), ((1, 0, 0), L+1)
print('HC: L3 closure', sorted(g3.closure(set(), {q1, q2})), "L3' closure", sorted(g3p.closure(set(), {q1, q2})))

# 2. self-supporting search with Phi active
pool = [q for q in ((c, t) for c in ball(2, D) for t in range(L-3, L+3)) if even(q) and q not in FIXED]
print('pool', len(pool))
for name, g in (('L3', g3), ("L3'", g3p)):
    t0 = time.perf_counter()
    found = [S for k in (1, 2, 3) for S in combinations(pool, k) if g.closure(FIXED, set(S)) == set(S)]
    print('%s self-supporting sets of size 1-3 with Phi active: %d' % (name, len(found)))
    print('%s search %.1fs' % (name, time.perf_counter()-t0), file=sys.stderr)

# 3. constraint block at c0 = (1,0,0), no fixed set
c0 = (1, 0, 0)
top, centre = (c0, L+1), (c0, L-1)
six = {(add(c0, e), L) for e in AX}
blk = {top, centre} | six
print('block: L3 %d, L3prime %d of 8; minus centre: L3 %d, L3prime %d' % (
    len(g3.closure(set(), blk)), len(g3p.closure(set(), blk)),
    len(g3.closure(set(), blk-{centre})), len(g3p.closure(set(), blk-{centre}))))

# 4-6. random-set comparisons with Phi active
rng = random.Random(41)
gS = Geometry(D, L, symmetric=True)
gO = Geometry(D, L, offaxis='all')
gN = Geometry(D, L, nopar=True)
more = less = offd = npd = sub = 0
for _ in range(400):
    S = set(rng.sample(pool, rng.randint(2, 10)))
    a = g3p.closure(FIXED, S)
    s, o, n, b = gS.closure(FIXED, S), gO.closure(FIXED, S), gN.closure(FIXED, S), g3.closure(FIXED, S)
    more += s > a
    less += not (a <= s)
    offd += o != a
    npd += n != a
    sub += not (a <= b)
print("symmetric radii: strictly more %d/400, ever less %d" % (more, less))
print("off-axis mutant differs on random sets: %d/400" % offd)
print("parity-dropped mutant differs on even-class sets (Phi even): %d/400 (equivalent if 0)" % npd)
print("L3' retained not within L3: %d/400" % sub)

# 7. native 3D checks from a pair (E, L) = (0, 1): forward depth d at (0,d+1), backward at (0,-d)
E0, L0 = 0, 1
T = 4
cells = ball(T+1, D)
inf = {}
bad_near = bad_far = 0
off_nonbij = 0
for trial in range(200):
    init = {(c, s): rng.randrange(8) for c in cells for s in (E0, L0)}
    d = rng.randint(1, T)
    fwd = rng.randrange(2) == 0
    q = ((0, 0, 0), L0+d) if fwd else ((0, 0, 0), E0-d)
    near, far = (L0, E0) if fwd else (E0, L0)
    base = evolve_value(init, q, {}, D, E0, L0)
    # perturbation radii
    c = rng.choice(cells)
    s = rng.choice((near, far))
    i2 = dict(init)
    i2[(c, s)] ^= 1+rng.randrange(7)
    if evolve_value(i2, q, {}, D, E0, L0) != base:
        key = (d, 'near' if s == near else 'far')
        inf[key] = max(inf.get(key, -1), dist(c, (0, 0, 0)))
    # bijection in a near tip and a far tip
    e = rng.choice(AX)
    for slc, k, which in ((near, d, 'near'), (far, d-1, 'far')):
        u = (add((0, 0, 0), e, k), slc)
        vals = set()
        for v in range(8):
            i3 = dict(init)
            i3[u] = v
            vals.add(evolve_value(i3, q, {}, D, E0, L0))
        if len(vals) != 8:
            if which == 'near':
                bad_near += 1
            else:
                bad_far += 1
    if d >= 3:
        f = rng.choice([a for a in AX if a != e and a != tuple(-i for i in e)])
        u = (add(add((0, 0, 0), e, d-2), f), far)
        vals = set()
        for v in range(8):
            i3 = dict(init)
            i3[u] = v
            vals.add(evolve_value(i3, q, {}, D, E0, L0))
        off_nonbij += len(vals) != 8
print('native max influence distance by (depth, slice):', dict(sorted(inf.items())), '(expect near d, far d-1)')
print('native near-tip bijection failures %d, far-tip failures %d (of 200 each, fwd+bwd mixed)' % (bad_near, bad_far))
print('native off-axis far cell non-bijective (d>=3 cases): %d' % off_nonbij)

# 8. timing
ctx = [q for q in ((c, t) for c in ball(4, D) for t in range(L-5, L+8)) if even(q) and q not in FIXED]
tt = 0.0
for _ in range(200):
    S = set(rng.sample(ctx, 30))
    t1 = time.perf_counter()
    g3p.closure(FIXED, S)
    tt += time.perf_counter()-t1
print("timing: L3' %.2f ms per closure (30 quantities + 8 fixed)" % (1000*tt/200), file=sys.stderr)
