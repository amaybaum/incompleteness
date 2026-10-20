"""AND-OR solver: deterministic exact preparation of a target token state by finite protocols built from
native configuration permutations, configuration attach (the start |0...0>), and sharp token tests in a
fixed finite set of bases with feed-forward. Exact Gaussian-rational arithmetic (fractions.Fraction).

A state is an unnormalized vector over Q(i) on n binary tokens, canonicalised by dividing by its first
nonzero entry. Moves: (a) a permutation generator (deterministic), (b) a test of one token in one basis,
whose positive-probability outcomes are all required to reach the win set (AND). Update modes:
  'luders'      : the tested token is left in the outcome eigenstate (local Lueders instrument),
  'destructive' : the tested token is reset to |0> after the outcome (test, discard, native re-attach).
Win: some token is exactly |t> and unentangled with the rest. The solver explores the reachable graph to
a bound and computes the least fixed point on the explored part; unexplored successors count as losing,
so a reported win is a real finite protocol (sound), and a reported loss is relative to the bound."""
from fractions import Fraction as F
import itertools, sys

def c(a, b=0): return (F(a), F(b))
def add(x, y): return (x[0]+y[0], x[1]+y[1])
def mul(x, y): return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def neg(x): return (-x[0], -x[1])
def inv(x):
    d = x[0]*x[0]+x[1]*x[1]; return (x[0]/d, -x[1]/d)
def conj(x): return (x[0], -x[1])
Z0 = c(0); ONE = c(1); I_ = c(0, 1)

def canon(v):
    for a in v:
        if a != Z0:
            ia = inv(a); return tuple(mul(e, ia) for e in v)
    return None

# token bases: each basis is a pair of (unnormalised) vectors (v, v_perp); the projector is |v><v|/<v|v>
BASES = {
    'Z': ((ONE, Z0), (Z0, ONE)),
    'X': ((ONE, ONE), (ONE, neg(ONE))),
    'Y': ((ONE, I_), (ONE, neg(I_))),
}

def bit(idx, j, n): return (idx >> (n-1-j)) & 1

def apply_perm(v, perm):
    out = [Z0]*len(v)
    for i, a in enumerate(v): out[perm[i]] = a
    return tuple(out)

def perm_gens(n, nonaffine):
    N = 2**n; gens = {}
    def mk(f):
        return tuple(f(i) for i in range(N))
    def setbit(i, j, b):
        s = n-1-j; return (i & ~(1 << s)) | (b << s)
    for j in range(n):
        gens['X%d' % j] = mk(lambda i, j=j: i ^ (1 << (n-1-j)))
    for j in range(n):
        for k in range(n):
            if j != k:
                gens['CN%d%d' % (j, k)] = mk(lambda i, j=j, k=k: i ^ ((1 << (n-1-k)) if bit(i, j, n) else 0))
    for j, k in itertools.combinations(range(n), 2):
        gens['SW%d%d' % (j, k)] = mk(lambda i, j=j, k=k: setbit(setbit(i, j, bit(i, k, n)), k, bit(i, j, n)))
    if nonaffine and n >= 3:
        for a, b, t in [(0, 1, 2), (0, 2, 1), (1, 2, 0)]:
            gens['TOF%d%d%d' % (a, b, t)] = mk(lambda i, a=a, b=b, t=t: i ^ ((1 << (n-1-t)) if bit(i, a, n) and bit(i, b, n) else 0))
        for ctl, x, y in [(0, 1, 2), (1, 0, 2), (2, 0, 1)]:
            gens['FRE%d%d%d' % (ctl, x, y)] = mk(lambda i, ctl=ctl, x=x, y=y: setbit(setbit(i, x, bit(i, y, n)), y, bit(i, x, n)) if bit(i, ctl, n) else i)
    return gens

def test_outcomes(v, j, basis, n, mode):
    outs = []
    for w in BASES[basis]:
        nw = add(mul(w[0], conj(w[0])), mul(w[1], conj(w[1])))
        new = [Z0]*len(v)
        for i in range(len(v)):
            if bit(i, j, n) != 0: continue
            i1 = i | (1 << (n-1-j))
            amp = add(mul(conj(w[0]), v[i]), mul(conj(w[1]), v[i1]))   # <w| on token j
            if mode == 'luders':
                new[i] = add(new[i], mul(amp, w[0])); new[i1] = add(new[i1], mul(amp, w[1]))
            else:
                new[i] = add(new[i], amp)
        cv = canon(new)
        if cv is not None: outs.append(cv)
    return outs

def is_target(v, n, t):
    # some token k is exactly |t> (unnormalised vector t=(t0,t1)) and unentangled: v(1,r)*t0 == v(0,r)*t1
    for k in range(n):
        ok = True; nz = False
        for i in range(len(v)):
            if bit(i, k, n): continue
            i1 = i | (1 << (n-1-k))
            if mul(v[i1], t[0]) != mul(v[i], t[1]): ok = False; break
            if v[i] != Z0 or v[i1] != Z0: nz = True
        if ok and nz: return True
    return False

def solve(n, bases, target, mode='luders', nonaffine=False, start=None, max_states=200000):
    gens = perm_gens(n, nonaffine)
    s0 = canon(start) if start is not None else canon(tuple(ONE if i == 0 else Z0 for i in range(2**n)))
    seen = {s0: None}; order = [s0]; edges = {}
    q = 0; truncated = False
    while q < len(order):
        s = order[q]; q += 1
        pm = {g: apply_perm(s, p) for g, p in gens.items()}
        tm = {}
        for j in range(n):
            for b in bases:
                outs = test_outcomes(s, j, b, n, mode)
                if len(outs) >= 1: tm[(j, b)] = outs
        edges[s] = (pm, tm)
        for t in list(pm.values()) + [o for outs in tm.values() for o in outs]:
            if t not in seen:
                if len(seen) >= max_states: truncated = True; continue
                seen[t] = None; order.append(t)
    win = {s: ('goal',) for s in order if is_target(s, n, target)}
    changed = True
    while changed:
        changed = False
        for s in order:
            if s in win or s not in edges: continue
            pm, tm = edges[s]
            for g, t in pm.items():
                if t in win: win[s] = ('perm', g, t); changed = True; break
            if s in win: continue
            for key, outs in tm.items():
                if len(outs) >= 2 and all(o in win for o in outs):
                    win[s] = ('test', key, tuple(outs)); changed = True; break
    return s0, win, len(order), truncated

def strategy(s, win, depth=0, out=None, budget=[400]):
    if out is None: out = []
    budget[0] -= 1
    if budget[0] < 0: out.append('  '*depth + '...'); return out
    w = win[s]
    if w[0] == 'goal': out.append('  '*depth + 'GOAL'); return out
    if w[0] == 'perm':
        out.append('  '*depth + 'apply ' + w[1]); strategy(w[2], win, depth, out); return out
    out.append('  '*depth + 'test token %d in basis %s' % w[1])
    for k, o in enumerate(w[2]):
        out.append('  '*depth + ' outcome %d:' % k); strategy(o, win, depth+1, out)
    return out
