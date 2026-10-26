"""Reviewer check (toy, 1D analogue of v8's rule; not v8's class): is L3' elimination EXACT?
Rule: x_t(c) = x_{t-2}(c) ^ H(x_{t-1}(c-1) ^ x_{t-1}(c+1)). Reference pair (E,L) = (0,1), fair prior.
Window (even class): slice L sites {-3,-1,1,3}, slice E sites {-2,0,2}: 21 bits, 2^21 worlds, exhaustive.
For random subsets of a pool of quantities whose cones fit the window, compute the closure under
(a) L3 near-only, (b) L3' near+far, (c) WRONG mutant (far tips at distance d, outside the cone),
and test exactly: eliminated set jointly uniform and independent of the retained set."""
import numpy as np, random, itertools
H = np.array([4*((v >> 1) & 1) + 2*(v & 1) + (((v >> 2) & 1) ^ ((v >> 1) & (v & 1) & 1)) for v in range(8)], dtype=np.uint8)
LS, ES = (-3, -1, 1, 3), (-2, 0, 2)
VARS = [(c, 1) for c in LS] + [(c, 0) for c in ES]
N = 1 << (3*len(VARS))
w = np.arange(N, dtype=np.uint32)
base = {v: ((w >> (3*i)) & 7).astype(np.uint8) for i, v in enumerate(VARS)}
memo = dict(base)
def val(c, t):
    if (c, t) in memo: return memo[(c, t)]
    if t >= 2:   r = val(c, t-2) ^ H[val(c-1, t-1) ^ val(c+1, t-1)]
    elif t <= -1: r = val(c, t+2) ^ H[val(c-1, t+1) ^ val(c+1, t+1)]
    else: raise KeyError((c, t))
    memo[(c, t)] = r; return r
E, L = 0, 1
def depth(q):
    c, t = q
    return (t-L, 'F') if t >= L else (E-t, 'B')
def in_cone(u, q):
    (uc, us), (c, t) = u, q
    d, ty = depth(q)
    near, far = (L, E) if ty == 'F' else (E, L)
    r = abs(uc-c)
    if us == near: return r <= d and (r-d) % 2 == 0
    if us == far:  return 0 <= r <= d-1 and (r-(d-1)) % 2 == 0
    return False
def tips(q, mode):
    c, t = q
    d, ty = depth(q)
    ns, fs = (L, E) if ty == 'F' else (E, L)
    out = {(c+d, ns), (c-d, ns)}
    if mode == 'L3p' and d >= 1: out |= {(c+d-1, fs), (c-(d-1), fs)}
    if mode == 'WRONG' and d >= 1: out |= {(c+d, fs), (c-d, fs)}
    return out
def closure(S, mode):
    ret = set(S); ch = True
    while ch:
        ch = False
        for q in sorted(ret):
            oth = ret - {q}
            if any(not any(in_cone(u, o) for o in oth) for u in tips(q, mode)):
                ret.discard(q); ch = True
    return ret
pool = [(0, 2), (2, 2), (-2, 2), (1, 3), (-1, 3), (0, 4), (1, -1), (-1, -1), (0, -2)] + VARS
for q in pool: val(*q)          # all must fit in the window
def exact_indep(elim, ret):
    if not elim: return True
    key_e = np.zeros(N, dtype=np.int64); key_r = np.zeros(N, dtype=np.int64)
    for q in sorted(elim): key_e = key_e*8 + memo[q]
    for q in sorted(ret):  key_r = key_r*8 + memo[q]
    ne, nr = 8**len(elim), 8**len(ret)
    joint = np.bincount(key_e*nr + key_r, minlength=ne*nr).reshape(ne, nr)
    mr = joint.sum(axis=0)
    return bool(np.all(joint*ne == mr[None, :]))     # uniform over elim, independent of ret
rng = random.Random(29)
stats = {m: [0, 0] for m in ('L3', 'L3p', 'WRONG')}
sub = 0
for trial in range(250):
    S = set(rng.sample(pool, rng.randint(2, 6)))
    rets = {}
    for m in stats:
        r = closure(S, m); rets[m] = r
        ok = exact_indep(S - r, r)
        stats[m][0] += 1; stats[m][1] += (not ok)
    sub += not (rets['L3p'] <= rets['L3'])
print('trials', 250)
for m, (n, bad) in stats.items(): print('%-5s exactness violations: %d of %d' % (m, bad, n))
print("L3' retained not subset of L3:", sub)
# depth-2 case from the review: q=(0,3)?? use (1,3) with its near tips only -> L3 keeps, L3' eliminates
S = {(1, 3), (-1, 1), (3, 1)}
for m in ('L3', 'L3p'):
    r = closure(S, m); print(m, 'on', sorted(S), '-> retained', sorted(r), 'exact:', exact_indep(S - r, r))
