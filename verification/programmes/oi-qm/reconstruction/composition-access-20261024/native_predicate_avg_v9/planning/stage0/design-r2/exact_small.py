"""R1 design check (toys only): exact elimination soundness of the prototype closure.
1D analogue, exhaustive window of 21 bits (2^21 worlds), and a 2D window of 18 bits
(2^18 worlds). For random subsets of a pool, the eliminated set must be exactly
uniform and independent of the retained set, under L3 and L3'; the wrong-far-tip
mutant must produce violations. Standard library (integer counting)."""
import random
import sys
from collections import Counter
sys.path.insert(0, sys.argv[1])
from proto import Geometry, evolve_value  # noqa: E402


def worlds_table(window, pool, dim, E, L):
    """Value of every pool quantity in every world, as one bytes object per quantity."""
    n = len(window)
    cols = {q: bytearray(1 << (3*n)) for q in pool}
    for w in range(1 << (3*n)):
        init = {v: (w >> (3*i)) & 7 for i, v in enumerate(window)}
        cache = {}
        for q in pool:
            cols[q][w] = init[q] if q in init else evolve_value(init, q, cache, dim, E, L)
    return {q: bytes(b) for q, b in cols.items()}


def exact_ok(cols, elim, ret, N):
    if not elim:
        return True
    el, rt = sorted(elim), sorted(ret)
    joint = Counter(zip(*(cols[q] for q in el), *(cols[q] for q in rt))) if rt else Counter(zip(*(cols[q] for q in el)))
    marg = Counter(zip(*(cols[q] for q in rt))) if rt else Counter({(): N})
    ne = 8**len(el)
    for key, cnt in joint.items():
        if cnt*ne != marg[key[len(el):]]:
            return False
    # every elim value must appear for every retained value
    return len(joint) == ne*len(marg)


def trial_set(name, dim, window, pool, E, L, trials, seed):
    N = 1 << (3*len(window))
    cols = worlds_table(window, pool, dim, E, L)
    rules = {'L3': Geometry(dim, L, far=False), "L3'": Geometry(dim, L, far=True),
             'wrong far tip': Geometry(dim, L, wrong_far=True)}
    rng = random.Random(seed)
    viol = {k: 0 for k in rules}
    sub = 0
    for _ in range(trials):
        S = set(rng.sample(pool, rng.randint(2, min(6, len(pool)))))
        rets = {}
        for k, g in rules.items():
            r = g.closure(set(), S)
            rets[k] = r
            viol[k] += not exact_ok(cols, S - r, r, N)
        sub += not (rets["L3'"] <= rets['L3'])
    print('%s: %d worlds, %d trials; exactness violations: %s; L3\' not within L3: %d' % (
        name, N, trials, viol, sub))
    return cols, rules, N


# 1D: pair (E, L) = (0, 1); even class |c|+t even. Window: slice 1 sites -3,-1,1,3; slice 0 sites -2,0,2.
W1 = [((c,), 1) for c in (-3, -1, 1, 3)] + [((c,), 0) for c in (-2, 0, 2)]
P1 = [((0,), 2), ((2,), 2), ((-2,), 2), ((1,), 3), ((-1,), 3), ((0,), 4),
      ((1,), -1), ((-1,), -1), ((0,), -2)] + W1
trial_set('1D', 1, W1, P1, 0, 1, 80, 29)

# 2D: pair (0, 1). Window: slice 1 sites at |c|=1 (4), slice 0 sites (0,0) and (2,0): 6 cells, 18 bits.
W2 = [((1, 0), 1), ((-1, 0), 1), ((0, 1), 1), ((0, -1), 1), ((0, 0), 0), ((2, 0), 0)]
P2 = [((0, 0), 2)] + W2
cols, rules, N = trial_set('2D', 2, W2, P2, 0, 1, 120, 7)
top, centre = ((0, 0), 2), ((0, 0), 0)
blk = set(P2) - {((2, 0), 0)}
for k, g in rules.items():
    for label, S in (('block', blk), ('block minus centre', blk - {centre})):
        r = g.closure(set(), S)
        print('  2D %-18s %-14s retained %d of %d; exact: %s' % (label, k, len(r), len(S), exact_ok(cols, S - r, r, N)))
