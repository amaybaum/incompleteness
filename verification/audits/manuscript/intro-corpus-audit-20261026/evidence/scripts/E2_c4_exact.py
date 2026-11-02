#!/usr/bin/env python3
"""E2: exact / rigorous-interval re-evaluation of the instances in
papers/oi_lattice_code/foundations/c4_backflow_probes.py@eae01647 (cited for Introduction L84 and
Main.md:170, "Certified exactly"), which builds exact Fraction laws but evaluates the conditional
mutual information and the bound p0*delta^2/ln2 in floating point.

Exact CMI: with D the lcm of the joint probabilities' denominators,
  I(A;B|C) = (1/D) log2 Q,  Q = prod r^(D p) an exact rational, r = p(a,c,b)p(c)/(p(a,c)p(c,b)).
Equalities (I = 1, 2/3, 0) are decided exactly (Q a power of 2); the inequality I >= p0 delta^2/ln2
is ln Q >= D p0 delta^2, decided with mpmath interval arithmetic (rigorous enclosure of ln Q).
Tables Q1, Q2, Q5 are rebuilt from the probe's stated definitions; Q3 reuses the probe's
construction (copied, with attribution) and decides I = 0 exactly.

Usage: python3 -I E2_c4_exact.py [out.json]
"""
import itertools, json, os, sys
from fractions import Fraction as F
from math import lcm
from mpmath import iv

iv.dps = 60

def exact_cmi(tab):
    """tab: (a, c, b) -> Fraction. Returns (Q, D) with I = log2(Q)/D."""
    pc, pac, pcb = {}, {}, {}
    for (a, c, b), p in tab.items():
        pc[c] = pc.get(c, 0) + p; pac[(a, c)] = pac.get((a, c), 0) + p; pcb[(c, b)] = pcb.get((c, b), 0) + p
    D = 1
    for p in tab.values():
        D = lcm(D, p.denominator)
    Q = F(1)
    for (a, c, b), p in tab.items():
        if p:
            Q *= (p * pc[c] / (pac[(a, c)] * pcb[(c, b)])) ** int(D * p)
    return Q, D

def log2_exact(Q):
    if Q.denominator == 1 and Q.numerator & (Q.numerator - 1) == 0:
        return F(Q.numerator.bit_length() - 1)
    if Q.numerator == 1 and Q.denominator & (Q.denominator - 1) == 0:
        return -F(Q.denominator.bit_length() - 1)
    return None

def gap(tab):
    laws = {}
    for (a, c, b), p in tab.items():
        laws.setdefault((a, c), {}); laws[(a, c)][b] = laws[(a, c)].get(b, 0) + p
    best = F(0)
    ks = list(laws)
    for i in range(len(ks)):
        for j in range(i + 1, len(ks)):
            if ks[i][1] != ks[j][1]:
                continue
            w1, w2 = sum(laws[ks[i]].values()), sum(laws[ks[j]].values())
            P1 = {b: v / w1 for b, v in laws[ks[i]].items()}; P2 = {b: v / w2 for b, v in laws[ks[j]].items()}
            tv = sum(abs(P1.get(b, 0) - P2.get(b, 0)) for b in set(P1) | set(P2)) / 2
            best = max(best, min(w1, w2) * tv * tv)
    return best          # bound = best / ln 2 bits

def verdict(tab, claimed_I=None):
    Q, D = exact_cmi(tab)
    c = gap(tab)
    lnQ = iv.log(iv.mpf([Q.numerator, Q.numerator]) / iv.mpf([Q.denominator, Q.denominator]))
    holds = bool(lnQ.a >= D * c.numerator / iv.mpf(c.denominator)) if Q > 0 else False
    I = log2_exact(Q)
    r = {"Q": str(Q), "D": D, "I_bits_exact": None if I is None else str(I / D),
         "p0_delta2": str(c), "bound_holds_rigorous": holds,
         "I_enclosure_bits_float": [float((lnQ / iv.log(2) / D).a), float((lnQ / iv.log(2) / D).b)]}
    if claimed_I is not None:
        r["claimed_I_exact"] = (I is not None and I / D == claimed_I)
    return r

out = {}
# Q1: X0, X1 independent uniform bits; X2 = X0
t1 = {((x0,), x1, (x0,)): F(1, 4) for x0 in (0, 1) for x1 in (0, 1)}
out["Q1"] = verdict(t1, F(1))
# Q2: revival permutation on {0,1,2} x {0,1}, uniform on the six states
phiR = {(0, 0): (0, 0), (0, 1): (0, 1), (1, 0): (1, 0), (1, 1): (2, 0), (2, 0): (1, 1), (2, 1): (2, 1)}
t2 = {}
for s in phiR:
    s1 = phiR[s]; s2 = phiR[s1]
    k = ((s[0],), s1[0], (s2[0],)); t2[k] = t2.get(k, 0) + F(1, 6)
out["Q2"] = verdict(t2, F(2, 3))
# Q5: X0, X1 uniform; X2 | x0 = (1/2 + s, 1/2 - s), s = +-1/8
t5 = {}
for x0, x1, x2 in itertools.product((0, 1), repeat=3):
    s = F(1, 8) if x0 == 0 else F(-1, 8)
    t5[((x0,), x1, (x2,))] = F(1, 4) * ((F(1, 2) + s) if x2 == 0 else (F(1, 2) - s))
out["Q5"] = verdict(t5)
# Q3: the b51 dilation of a fair coin (construction copied from c4_backflow_probes.py:67-83)
PAD = -1
def build(kern, nV, K, D):
    hs = list(itertools.product(list(range(nV)) + [PAD], repeat=K)); ts = list(itertools.product(range(D), repeat=K))
    states = [(x, h, t, c) for x in range(nV) for h in hs for t in ts for c in range(K + 1)]
    wf = lambda h, c: all(h[i] != PAD for i in range(c)) and all(h[i] == PAD for i in range(c, K))
    def Qf(p, s):
        acc = 0
        for y in range(nV):
            acc += int(kern(p)[y] * D)
            if s < acc:
                return y
    phi = {}
    for (x, h, t, c) in states:
        if c < K and wf(h, c):
            phi[(x, h, t, c)] = (Qf(tuple(h[:c]) + (x,), t[c]), tuple(list(h[:c]) + [x] + [PAD] * (K - c - 1)), t, c + 1)
    un = sorted(set(states) - set(phi.values())); ud = sorted(set(states) - set(phi.keys()))
    for a, b in zip(ud, un):
        phi[a] = b
    assert sorted(phi.values()) == sorted(states), "not a bijection"
    return phi, [(tuple([PAD] * K), t, 0) for t in ts]
K = 4
phi, mu = build(lambda p: (F(1, 2), F(1, 2)), 2, K, 2)
traj = {}
for x0 in (0, 1):
    for (h, t, c) in mu:
        s, tr = (x0, h, t, c), [x0]
        for _ in range(K):
            s = phi[s]; tr.append(s[0])
        traj[tuple(tr)] = traj.get(tuple(tr), 0) + F(1, 2) / len(mu)
uniform = len(traj) == 2 ** (K + 1) and set(traj.values()) == {F(1, 2 ** (K + 1))}
zero_all = True
for k in range(1, K):
    tab = {}
    for tr, p in traj.items():
        key = (tr[:k], tr[k], tr[k + 1:]); tab[key] = tab.get(key, 0) + p
    Q, D = exact_cmi(tab)
    zero_all &= (Q == 1) and gap(tab) == 0
out["Q3"] = {"trajectory_law_iid_uniform_exact": uniform, "I_zero_and_no_gap_every_order_exact": zero_all}
out["all_hold"] = (out["Q1"]["claimed_I_exact"] and out["Q1"]["bound_holds_rigorous"] and out["Q2"]["claimed_I_exact"]
                   and out["Q2"]["bound_holds_rigorous"] and out["Q5"]["bound_holds_rigorous"] and uniform and zero_all)
js = json.dumps(out, indent=1)
if len(sys.argv) > 1:
    if os.path.abspath(sys.argv[1]) == os.path.abspath(__file__):
        sys.exit("refusing to overwrite this script")
    open(sys.argv[1], "w").write(js + "\n")
print(js)
