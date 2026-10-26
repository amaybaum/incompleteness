"""Stage 0 design controls on TOY geometries only (not v8's class): a prototype
L3 closure with asymmetric cone radii, the planted-tie detector, the off-axis and
symmetric-radius countercontrols, a hand-checked instance, a native-rule check of
cone radii and tip bijection, and timing. Standard library, exact integers."""
import random
import time
from itertools import combinations

AX = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
H = tuple(4*((v >> 1) & 1) + 2*(v & 1) + (((v >> 2) & 1) ^ ((v >> 1) & (v & 1) & 1)) for v in range(8))


def dist(a, b):
    return sum(abs(i-j) for i, j in zip(a, b))


def add(a, b, k=1):
    return tuple(i+k*j for i, j in zip(a, b))


class Geometry:
    """Reference pair (E, L) = (L-1, L). F: t >= L, B: t <= E."""

    def __init__(self, L, symmetric=False, offaxis=False):
        self.L, self.E = L, L-1
        self.symmetric, self.offaxis = symmetric, offaxis

    def depth(self, q):
        c, t = q
        return (t-self.L, 'F') if t >= self.L else (self.E-t, 'B')

    def in_cone(self, u, q):
        (uc, us), (c, t) = u, q
        d, ty = self.depth(q)
        near, far = (self.L, self.E) if ty == 'F' else (self.E, self.L)
        r = dist(uc, c)
        if us == near:
            return r <= d and (r-d) % 2 == 0
        if us == far:
            rr = d if self.symmetric else d-1
            return 0 <= r <= rr and (r-rr) % 2 == 0
        return False

    def tips(self, q):
        c, t = q
        d, ty = self.depth(q)
        s = self.L if ty == 'F' else self.E
        out = {(add(c, e, d), s) for e in AX}
        if self.offaxis and d >= 2:          # mutant: off-axis cells at distance d
            for e in AX:
                for f in AX:
                    if f != e and f != tuple(-i for i in e):
                        out.add((add(add(c, e, d-1), f), s))
        return out

    def closure(self, fixed, quants):
        ret = set(fixed) | set(quants)
        changed = True
        while changed:
            changed = False
            for q in sorted(ret - set(fixed)):
                others = ret - {q}
                if any(not any(self.in_cone(u, o) for o in others) for u in self.tips(q)):
                    ret.discard(q)
                    changed = True
        return ret - set(fixed)


def even(q):
    return (sum(map(abs, q[0]))+q[1]) % 2 == 0


def ball(r):
    return [(x, y, z) for x in range(-r, r+1) for y in range(-(r-abs(x)), r-abs(x)+1)
            for z in range(-(r-abs(x)-abs(y)), r-abs(x)-abs(y)+1)]


# --- Hand-checked instance (worked in STAGE0-NOTES.md) -----------------------
g = Geometry(L=1)
q1, q2 = ((0, 0, 0), 3), ((1, 0, 0), 2)          # F depth 2 and depth 1 on the +x line
assert (add(q1[0], AX[0], 2), 1) == (add(q2[0], AX[0], 1), 1)   # shared +x tip (2,0,0)@L
hc = g.closure(set(), {q1, q2})
print('HC hand instance closure:', sorted(hc), '(hand: empty)')
assert hc == set()

# --- Toy planted-tie search: Phi analogue = six neighbours at E plus V at L ----
L = 3
gA = Geometry(L)
PHI = {(e, L-1) for e in AX} | {((0, 0, 0), L)}
P = ((0, 0, 0), L-2)                              # p analogue (B depth 1)
FIXED = PHI | {P}
pool = [q for q in ((c, t) for c in ball(2) for t in range(L-3, L+3)) if even(q) and q not in FIXED]
print('toy pool size', len(pool))
found = []
t0 = time.perf_counter()
for k in (1, 2, 3):
    for S in combinations(pool, k):
        r = gA.closure(FIXED, set(S))
        if r == set(S):
            found.append(S)
print('toy self-supporting sets (sizes 1-3):', len(found), 'search %.1fs' % (time.perf_counter()-t0))
for S in found[:5]:
    print('  ', S)

# --- Larger planted structure: a full block is self-supporting? ---------------
block = [q for q in ((c, t) for c in ball(1) for t in range(L-2, L+2)) if even(q) and q not in FIXED]
rb = gA.closure(FIXED, set(block))
print('toy block |Q|=%d retained %d' % (len(block), len(rb)))

# --- Countercontrols on toy instances ----------------------------------------
gS, gO = Geometry(L, symmetric=True), Geometry(L, offaxis=True)
rng = random.Random(11)
more_sym = less_sym = diff_off = 0
for trial in range(400):
    S = set(rng.sample(pool, rng.randint(2, 8)))
    a, s, o = gA.closure(FIXED, S), gS.closure(FIXED, S), gO.closure(FIXED, S)
    more_sym += s > a
    less_sym += not (a <= s)
    diff_off += o != a
print('symmetric radii: retains strictly more in %d/400; ever retains less: %d' % (more_sym, less_sym))
print('off-axis mutant: differs from correct closure in %d/400' % diff_off)

# --- Native-rule check of cone radii and axis-tip bijection (toy 3D) ----------
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


T, R = 4, 0
cells = ball(R+T)
maxE, maxL = {}, {}
bij_bad = 0
for trial in range(300):
    E = {c: rng.randrange(8) for c in cells}
    Ls = {c: rng.randrange(8) for c in cells}
    base = evolve(E, Ls, T, R)
    which, c = rng.randrange(2), rng.choice(cells)
    E2, L2 = dict(E), dict(Ls)
    (E2 if which == 0 else L2)[c] ^= 1+rng.randrange(7)
    pert = evolve(E2, L2, T, R)
    for k in range(1, T+1):
        if base[k+1][(0, 0, 0)] != pert[k+1][(0, 0, 0)]:
            m = maxE if which == 0 else maxL
            m[k] = max(m.get(k, -1), dist(c, (0, 0, 0)))
    k = rng.randint(1, T)
    e = rng.choice(AX)
    u = add((0, 0, 0), e, k)
    vals = set()
    for v in range(8):
        L3 = dict(Ls)
        L3[u] = v
        vals.add(evolve(E, L3, T, R)[k+1][(0, 0, 0)])
    bij_bad += len(vals) != 8
print('native: max influencing distance (earlier, later) by depth:',
      {k: (maxE.get(k), maxL.get(k)) for k in range(1, T+1)}, '(expect k-1, k)')
print('native: axis-tip bijection failures', bij_bad, 'of 300')

# --- Timing on synthetic contexts of v8-like size (toy geometry) --------------
ctx_pool = [q for q in ((c, t) for c in ball(4) for t in range(L-5, L+8)) if even(q) and q not in FIXED]
reps, tt = 300, 0.0
for i in range(reps):
    S = set(rng.sample(ctx_pool, 30))
    t1 = time.perf_counter()
    gA.closure(FIXED, S)
    tt += time.perf_counter()-t1
print('timing: %.2f ms per closure on 30 synthetic quantities + 8 fixed' % (1000*tt/reps))
