"""Reviewer toy checks of the plan's L1/L3 on v8's 3D rule (random instances) -- not the plan's question."""
import random, sys
H = tuple(4*((v >> 1) & 1) + 2*(v & 1) + (((v >> 2) & 1) ^ ((v >> 1) & (v & 1) & 1)) for v in range(8))
assert sorted(H) == list(range(8))
STEPS = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
def ball(r):
    return [(x,y,z) for x in range(-r,r+1) for y in range(-(r-abs(x)),r-abs(x)+1)
            for z in range(-(r-abs(x)-abs(y)), r-abs(x)-abs(y)+1)]
def add(a,b): return tuple(i+j for i,j in zip(a,b))
def evolve(s0, s1, T, R):
    """s0 = earlier slice, s1 = later slice (dicts on ball(R+T)); forward T steps; returns list of slices."""
    sl = [s0, s1]
    for t in range(T):
        p2, p1 = sl[-2], sl[-1]; out = {}
        for x in ball(R+T-t-1):
            s = 0
            for st in STEPS: s ^= p1[add(x,st)]
            out[x] = p2[x] ^ H[s]
        sl.append(out)
    return sl  # index k -> slice (k-1) relative: sl[0]=earlier, sl[1]=later, sl[2]=+1 ...
rng = random.Random(7)
T, R = 5, 1
cells = ball(R+T)
def rnd(): return {c: rng.randrange(8) for c in cells}
# L1 parity: flip odd-class initial var, all even-class site-times unchanged; flip even -> something changes
bad = 0; even_changed = 0
for trial in range(40):
    a, b = rnd(), rnd()
    base = evolve(a, b, T, R)
    for which in (0, 1):
        c = rng.choice(cells)
        a2, b2 = dict(a), dict(b)
        (a2 if which == 0 else b2)[c] ^= 1 + rng.randrange(7)
        pert = evolve(a2, b2, T, R)
        par0 = (sum(c) + (which - 1)) % 2       # slice index: which=0 -> t=-1, which=1 -> t=0
        for k in range(2, len(base)):
            t = k - 1
            for x in ball(R + T - (k-1)):
                if x in base[k] and base[k][x] != pert[k][x]:
                    if (sum(x) + t) % 2 != par0: bad += 1
                    else: even_changed += 1
print('L1 violations', bad, '; same-parity changes seen', even_changed)
# L3 bijection along axis: site-time (x,t), u = slice-0 triple at x + t*e
viol = 0; tested = 0
for trial in range(60):
    a, b = rnd(), rnd()
    t = rng.randrange(1, T+1); x = rng.choice(ball(R)); e = rng.choice(STEPS)
    u = tuple(x[i] + t*e[i] for i in range(3))
    vals = set()
    for v in range(8):
        b2 = dict(b); b2[u] = v
        vals.add(evolve(a, b2, T, R)[t+1][x])
    tested += 1; viol += (len(vals) != 8)
print('L3 axis bijection: tested', tested, 'non-bijective', viol)
# Off-axis extreme at distance t (e.g. x+(t-1)e+f): not guaranteed bijective
nb = 0; tested = 0
for trial in range(60):
    a, b = rnd(), rnd()
    t = rng.randrange(2, T+1); x = rng.choice(ball(R)); e = rng.choice(STEPS)
    f = rng.choice([s for s in STEPS if s != e and s != tuple(-i for i in e)])
    u = tuple(x[i] + (t-1)*e[i] + f[i] for i in range(3))
    vals = set()
    for v in range(8):
        b2 = dict(b); b2[u] = v
        vals.add(evolve(a, b2, T, R)[t+1][x])
    tested += 1; nb += (len(vals) != 8)
print('off-axis distance-t extreme: tested', tested, 'non-bijective', nb)
# Backward L3: reverse rule from pair (s7, s8) = (later-earlier swapped): x_{t-2} = x_t ^ H(sum x_{t-1}); same form
viol = 0
for trial in range(30):
    a, b = rnd(), rnd()   # a = slice 8 (plays 'earlier' in reversed time), b = slice 7 (plays 'later')
    t = rng.randrange(1, T+1); x = rng.choice(ball(R)); e = rng.choice(STEPS)
    u = tuple(x[i] + t*e[i] for i in range(3))
    vals = set()
    for v in range(8):
        b2 = dict(b); b2[u] = v
        vals.add(evolve(a, b2, T, R)[t+1][x])  # slice 7 - t
    viol += (len(vals) != 8)
print('L3 backward (time-reversed evolve) non-bijective', viol)
