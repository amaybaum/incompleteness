"""Class-S countermodel with (EM) and (C2-slow), and its exact finite bijective realization.

Coarse model: hidden bit g, visible bit x.
  read : x_{t+1} = g_t xor r_t,  r_t ~ Bern(1/4) fresh
  hidden channel between couplings: g_{t+1} = g_t xor f_t, f_t ~ Bern(eta) fresh, eta = 1/50
The hidden channel is BSC(eta): stationary law uniform, second eigenvalue 1 - 2 eta = 24/25 < 1, so it
mixes (EM for the coarse hidden variable) with mixing time ~ 1/(2 eta) = 25 steps >> 1 step (C2-slow);
the window n = 6 (coarse) and n = 4 (bijection) are << 25.

(A) shared hidden prior (Main §2.3 rooted family): x_0 any root, g_0 uniform independent.
(B) stationary initial law of the Markov chain (x, g) (time-homogeneous, stationary visible process);
    family Gamma_t(a, .) = P(X_t = . | X_0 = a).
(C) exact bijective realization of (A) on horizon n = 4:
    state (x, g, r_1..r_n, f_1..f_n); phi(x, g, r, f) = (g xor r_1, g xor f_1, (r_2..r_n, x), (f_2..f_n, f_1));
    prior: g uniform, r_i ~ Bern(1/4), f_i ~ Bern(eta), independent of the root.
"""
import importlib.util, sys, os
from fractions import Fraction as Fr
from itertools import product
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('trackd_lib', os.path.join(HERE, 'trackd_lib.py'))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)

eta, rho = Fr(1, 50), Fr(1, 4)
def bern(p, b): return p if b else 1 - p
green = True

def coarse_law(init, n):
    """init: dict (x0, g0) -> prob. Returns law on (x_0..x_n)."""
    P = defaultdict(Fr)
    def rec(xs, g, w, t):
        if t == n:
            P[tuple(xs)] += w; return
        for r in (0, 1):
            for f in (0, 1):
                rec(xs + [g ^ r], g ^ f, w * bern(rho, r) * bern(eta, f), t + 1)
    for (x0, g0), w in init.items():
        if w:
            rec([x0], g0, w, 0)
    return dict(P)

def family(P, n):
    G = []
    p0 = defaultdict(Fr)
    for s, w in P.items(): p0[s[0]] += w
    for t in range(n + 1):
        M = [[Fr(0)] * 2 for _ in range(2)]
        for s, w in P.items(): M[s[0]][s[t]] += w / p0[s[0]]
        G.append(M)
    return G

n = 6
# (A)
PA = coarse_law({(x, g): Fr(1, 4) for x in (0, 1) for g in (0, 1)}, n)
GA = family(PA, n)
divA, badA = L.p_divisible_window(GA, n, closed_form_check=True)
gapsA = {k: L.gap_at(PA, k, 2)[:2] for k in range(1, n)}
rank1A = all(GA[t][0] == GA[t][1] for t in range(1, n + 1))
print(f'(A) shared prior: Gamma_t rank one for 1<=t<={n}: {rank1A}; P-divisible on {{0..{n}}}: {divA}; '
      f'gaps by order: { {k: (g, str(d)) for k, (g, d) in gapsA.items()} }')
okA = divA and rank1A and all(gapsA[k][0] for k in range(2, n)) and not gapsA[1][0]
green &= okA

# (B) stationary law of the (x, g) chain: pi(x, g) = sum_{g'} (1/2) Bern(rho, x^g') Bern(eta, g^g')
pi = {(x, g): sum(Fr(1, 2) * bern(rho, x ^ gp) * bern(eta, g ^ gp) for gp in (0, 1)) for x in (0, 1) for g in (0, 1)}
assert sum(pi.values()) == 1
# stationarity check: one step of the chain maps pi to pi
step = defaultdict(Fr)
for (x, g), w in pi.items():
    for r in (0, 1):
        for f in (0, 1):
            step[(g ^ r, g ^ f)] += w * bern(rho, r) * bern(eta, f)
stat = all(step[k] == pi[k] for k in pi)
PB = coarse_law(pi, n)
GB = family(PB, n)
divB, badB = L.p_divisible_window(GB, n, closed_form_check=True)
gapsB = {k: L.gap_at(PB, k, 2)[:2] for k in range(1, n)}
lam = [GB[t][0][0] - GB[t][1][0] for t in range(n + 1)]
print(f'(B) stationary init (stationary={stat}): eigenvalues lambda_t of Gamma_t: {[str(v) for v in lam]}; '
      f'P-divisible on {{0..{n}}}: {divB}; gaps by order: { {k: (g, str(d)) for k, (g, d) in gapsB.items()} }')
okB = stat and divB and all(gapsB[k][0] for k in range(1, n))
green &= okB

# EM / C2-slow facts for the coarse hidden channel
second_eig = 1 - 2 * eta
print(f'hidden channel BSC(eta={eta}): second eigenvalue {second_eig} (<1: mixes); 1/(1-second_eig) = {1/(1-second_eig)} steps')

# (C) exact bijection for (A), horizon nb = 4
nb = 4
states = list(product((0, 1), (0, 1), product((0, 1), repeat=nb), product((0, 1), repeat=nb)))
index = {s: i for i, s in enumerate(states)}
def phi(s):
    x, g, r, f = s
    return (g ^ r[0], g ^ f[0], tuple(r[1:]) + (x,), tuple(f[1:]) + (f[0],))
perm = [index[phi(s)] for s in states]
bij = sorted(perm) == list(range(len(states)))
def prior_h(s):
    _, g, r, f = s
    w = Fr(1, 2)
    for b in r: w *= bern(rho, b)
    for b in f: w *= bern(eta, b)
    return w
PC = defaultdict(Fr)
GC = [[[Fr(0)] * 2 for _ in range(2)] for _ in range(nb + 1)]
for s in states:
    w = prior_h(s)  # hidden prior, shared by every root
    z = s; xs = [s[0]]
    GC[0][s[0]][s[0]] += w
    for t in range(1, nb + 1):
        z = phi(z); xs.append(z[0]); GC[t][s[0]][z[0]] += w
    PC[tuple(xs)] += w * Fr(1, 2)
PA4 = coarse_law({(x, g): Fr(1, 4) for x in (0, 1) for g in (0, 1)}, nb)
same_law = dict(PC) == {k: v for k, v in PA4.items() if v}
divC, badC = L.p_divisible_window(GC, nb, closed_form_check=True)
gapsC = {k: L.gap_at(dict(PC), k, 2)[:2] for k in range(1, nb)}
Lo = L.perm_order(perm)
print(f'(C) bijection on |S|={len(states)}: bijective={bij}, order L={Lo}; visible law equals coarse model (A) on '
      f'horizon {nb}: {same_law}; P-divisible on {{0..{nb}}}: {divC}; gaps: { {k: (g, str(d)) for k, (g, d) in gapsC.items()} }')
okC = bij and same_law and divC and all(gapsC[k][0] for k in range(2, nb)) and nb <= Lo - 1
green &= okC
print('EM COUNTERMODEL', 'ALL VERIFIED' if green else 'FAILED')
