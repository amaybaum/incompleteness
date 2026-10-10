"""Exploration only: family members (as maps on the 42-point sample) that act on C0 as z -> conj z,
and which other circles each fixes pointwise; plus per-circle action types."""
import cmath, itertools
import groups as g
from circles import R

N = 9
t0 = 0.7
params = [cmath.exp(1j*t0), -cmath.exp(1j*t0), cmath.exp(-1j*t0), -cmath.exp(-1j*t0), 1, -1]
pts = []; index = {}; label = {}
for r in range(N):
    for n, z in enumerate(params):
        v = g.feature(r, z); k = g.key(v)
        if k not in index:
            index[k] = len(pts); pts.append(v); label[len(pts)-1] = (r, n)
from circles import COORDS
cidx = {p: n for n, p in enumerate(COORDS)}
rho = {p: ((p[1][1], p[1][2], p[1][0]), p[0]) for p in COORDS}
def relabel(pi, tau):
    return lambda v: tuple(v[cidx[((pi[p[0][0]], pi[p[0][1]], pi[p[0][2]]), (tau[p[1][0]], tau[p[1][1]], tau[p[1][2]]))]] for p in COORDS)
conj = lambda v: tuple(x.conjugate() for x in v)
T = lambda v: tuple(v[cidx[rho[p]]].conjugate() for p in COORDS)
def perm(f):
    return tuple(index[g.key(f(v))] for v in pts)
perms = list(itertools.permutations(range(4)))
shapes = {}
Tp, Cp = perm(T), perm(conj)
members = {}
for pi in perms:
    for tau in perms:
        s = perm(relabel(pi, tau))
        members[(pi, tau, 'R')] = s
        members[(pi, tau, 'RC')] = tuple(s[Cp[i]] for i in range(len(pts)))   # relabel after conj
        members[(pi, tau, 'RT')] = tuple(s[Tp[i]] for i in range(len(pts)))
        members[(pi, tau, 'RTC')] = tuple(Cp[s[Tp[i]]] for i in range(len(pts)))
print("distinct maps:", len(set(members.values())))
# point indices
e0 = index[g.key(g.feature(0, params[0]))]
e0c = index[g.key(g.feature(0, params[2]))]
cands = {k: m for k, m in members.items() if m[e0] == e0c}
print("members sending F(e^{it0}) to F(e^{-it0}) :", len(cands), "distinct:", len(set(cands.values())))
def fixes_circle(m, r):
    return all(m[index[g.key(g.feature(r, z))]] == index[g.key(g.feature(r, z))] for z in params)
from collections import Counter
cnt = Counter()
for k, m in cands.items():
    fx = tuple(r for r in range(1, N) if fixes_circle(m, r))
    cnt[fx] += 1
print("fixed other circles among those (multiplicity over 4-shape words):")
for k, v in sorted(cnt.items()):
    print("  ", k, v)
# For each other circle r: does every candidate move some point of r generic?
for r in range(1, N):
    bad = [k for k, m in cands.items() if fixes_circle(m, r)]
    print("circle", r, R[r], "candidates fixing it pointwise:", len(bad), sorted(set(x[2] for x in bad)))
