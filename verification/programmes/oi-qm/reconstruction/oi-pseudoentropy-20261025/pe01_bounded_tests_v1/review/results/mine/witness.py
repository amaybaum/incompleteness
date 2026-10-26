# Full clocked-composite checks for the PE-01 G_clk n=5 m=2 K=7 witness. Independent of the package.
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import itertools, math
from fractions import Fraction as Fr
from indep import gen, Z_of, orbit_lengths, order_of_z, companion, POLY, adv_curve

n, m, K = 5, 2, 7
rho = ([1, 0, 2, 3], [0, 2, 3, 1]); a = [1, 0, 0, 1]; chi = [0, 0, 0, 0]
phi, sig, f = gen('clk', n, True)
CB = math.ceil(math.log2(K + 1))  # clock bits
NC = 1 << CB
F = {(v, chi[v]) for v in range(1 << m)}
# joint state: (x, v, clk, out, h)
S = [(x, v, c, o, h) for x in (0, 1) for v in range(1 << m) for c in range(NC) for o in (0, 1) for h in range(1 << n)]
def rho_step(s): x, v, c, o, h = s; return (x, rho[x][v], c, o, h)
def a_step(s):   x, v, c, o, h = s; return (x ^ a[v], v, c, o, h)
def phi_step(s): x, v, c, o, h = s; x2, h2 = phi(x, h); return (x2, v, c, o, h2)
def tick(s):     x, v, c, o, h = s; return (x, v, (c + 1) % NC, o, h)
def readout(s):  # time-invariant: triggered when the clock reads K
    x, v, c, o, h = s
    return (x, v, c, o ^ (1 if (c == K and (v, x) in F) else 0), h)
def step(s): return readout(tick(phi_step(a_step(rho_step(s)))))
maps = {'rho': rho_step, 'a': a_step, 'tick': tick, 'readout': readout}
res = {}
# EX1: every map and the composite step are bijections of the joint space
for nm, g in list(maps.items()) + [('phi', phi_step), ('composite', step)]:
    res['EX1 ' + nm] = len({g(s) for s in S}) == len(S)
# EX8: observer maps: h-component identity, visible component constant across h
for nm, g in maps.items():
    okh = all(g(s)[4] == s[4] for s in S)
    vis = {}
    okc = True
    for s in S:
        key = s[:4]; img = g(s)[:4]
        if vis.setdefault(key, img) != img: okc = False
    res['EX8 ' + nm] = okh and okc
# generator acts as identity on (v, clk, out)
res['EX8 phi identity on (v,clk,out)'] = all(phi_step(s)[1:4] == s[1:4] for s in S)
# EX7: prior = mu (uniform on (x,h)) x delta(v=0,clk=0,out=0); product by construction; EX8 holds
init = [(x, 0, 0, 0, h) for x in (0, 1) for h in range(1 << n)]
# full joint-state enumeration
dist = {s: Fr(1, len(init)) for s in init}
probs = {}
for t in range(1, K + 1):
    nd = {}
    for s, p in dist.items():
        s2 = step(s); nd[s2] = nd.get(s2, 0) + p
    dist = nd
    probs[t] = sum(p for s, p in dist.items() if chi[s[1]] == s[0])
    if t == K:
        probs['out'] = sum(p for s, p in dist.items() if s[3] == 1)
res['sum to 1'] = sum(dist.values()) == 1
print('Pr[chi(v_K\')=X_K\'] - 1/2:', {t: str(probs[t] - Fr(1, 2)) for t in range(1, K + 1)})
print('Pr[out=1 at K=7] - 1/2:', probs['out'] - Fr(1, 2))
# out stays 0 before K
# Q_p: replace each generator step's visible output by a fresh fair bit; same observer policy
def q_prob(Kp):
    tot = Fr(0)
    for x0 in (0, 1):
        for bits in itertools.product((0, 1), repeat=Kp):
            x, v = x0, 0
            for b in bits:
                v = rho[x][v]; x ^= a[v]; x ^= b
            tot += Fr(1, 2 * 2 ** Kp) * (chi[v] == x)
    return tot
print('Q_p:', [str(q_prob(k)) for k in range(4, 8)])
# EX4 / EX5 / EX6
res['EX4'] = order_of_z(n, POLY[n][0]) == 2 ** n - 1
# EX5: observability of (ell, L): rank of rows ell o L^i, i<n -> h_i, trivially rank n; verify by evaluation
L = companion(n, POLY[n][0])
outs = {}
for h in range(1 << n):
    hh = h; w = []
    for i in range(n): w.append(hh & 1); hh = L[hh]
    outs[tuple(w)] = h
res['EX5'] = len(outs) == 2 ** n
T = [[Fr(0)] * 2 for _ in range(2)]
for x in (0, 1):
    for h in range(1 << n):
        T[x][phi(x, h)[0]] += Fr(1, 1 << n)
print('EX6 one-step visible matrix', [[str(e) for e in r] for r in T])
res['EX6 non-permutation'] = not all(e in (0, 1) for r in T for e in r)
# Z, orbit median, K_cx
Z = Z_of(n, sig, f)
ol = orbit_lengths(n, phi)
L_ = sorted(ol.values())
from collections import Counter
print('Z(G_clk,5) =', Z, ' orbit length distribution (states):', sorted(Counter(L_).items()))
lo, hi = L_[len(L_) // 2 - 1], L_[len(L_) // 2]
print('median (lower, upper):', lo, hi, ' K_cx(lower)=', lo // 2, ' K_cx(upper)=', hi // 2)
fp = m + CB + 1
print('footprint', fp, 'visible register widths less sys bit:', m + CB + 1, ' theta', n + 1)
print('table size', 2 * m * 2 ** m + 2 ** m + 2 ** (m + 1) + CB)
for k, v in res.items(): print(k, v)
