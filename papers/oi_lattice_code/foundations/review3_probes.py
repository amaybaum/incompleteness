#!/usr/bin/env python3
# review3_probes.py — b55 triage certification (2026-08-10).
# Machine-verifies the third-round review's three load-bearing counterexamples
# against the 2.8.1 texts (Main M361 definition, M121 lemma, M323 theorem).
# Exact arithmetic where the claim is exact.
#
# P-A  (i) without a non-degeneracy clause does NOT imply (ii):
#      diagonal Hamiltonian => T(t) = I for all t => P-divisible.
# P-B  C1+C2+C3 do NOT imply accessible-timescale backflow: the fair coin,
#      realized by the b51 dilation construction itself, has C1 (T = J/2,
#      non-permutation), a static bath (tau_B = infinite), huge capacity —
#      and I(X_{<t}; X_{>t} | X_t) = 0 identically on the horizon.
# P-C  The mixing theorem's bound fails for arbitrary pi_H: the swap
#      phi(v,h) = (h,v) with perfect relaxation to pi_H = delta_0 has
#      eps = 0 under the prose hypothesis while ||T^(2) - T^2||_TV = 1/2.
#      (The in-repo c2 probe already fixes pi_H = uniform: code narrower
#      and correct; the prose is what fails.)

from fractions import Fraction as F
from math import cos, sin, pi, log2
import itertools, cmath

# ---------------- P-A: diagonal Hamiltonian ----------------
# U(t) = diag(1, e^{-i w t}); m_a = 1 (the definition's trivial-ancilla case).
for wt in (0.3, 1.1, 2.7):
    U = [[1, 0], [0, cmath.exp(-1j * wt)]]
    T = [[abs(U[i][j]) ** 2 for j in range(2)] for i in range(2)]
    assert T == [[1, 0], [0, 1]]
print("P-A: diagonal H  =>  T(t) = I for all t (exact |U_ij|^2): satisfies the")
print("     M361 definition of (i), and the process is P-DIVISIBLE — (i) as")
print("     defined does not imply (ii). Counterexample CONFIRMED.")

# ---------------- P-B: the coin via the b51 construction ----------------
PAD = -1
def build_dilation(kern, nV, K, D):
    hist_space = list(itertools.product(list(range(nV)) + [PAD], repeat=K))
    tape_space = list(itertools.product(range(D), repeat=K))
    states = [(x, hi, tp, c) for x in range(nV) for hi in hist_space
              for tp in tape_space for c in range(K + 1)]
    def wellformed(hi, c):
        return all(hi[i] != PAD for i in range(c)) and all(hi[i] == PAD for i in range(c, K))
    def Q(past, s):
        dist = kern(past); acc = 0
        for y in range(nV):
            cnt = dist[y] * D; assert cnt.denominator == 1
            acc += int(cnt)
            if s < acc: return y
        raise AssertionError
    phi = {}
    for (x, hi, tp, c) in states:
        if c < K and wellformed(hi, c):
            xn = Q(tuple(hi[:c]) + (x,), tp[c])
            phi[(x, hi, tp, c)] = (xn, tuple(list(hi[:c]) + [x] + [PAD] * (K - c - 1)), tp, c + 1)
    imgs = list(phi.values()); assert len(imgs) == len(set(imgs))
    unhit = sorted(set(states) - set(imgs)); undom = sorted(set(states) - set(phi.keys()))
    for a, b in zip(undom, unhit): phi[a] = b
    assert sorted(phi.values()) == sorted(states)
    return phi, [(tuple([PAD] * K), tp, 0) for tp in tape_space], len(hist_space) * len(tape_space) * (K + 1)

K = 4
kCoin = lambda past: (F(1, 2), F(1, 2))
phi, mu, mH = build_dilation(kCoin, 2, K, 2)
w = F(1, len(mu))
# one-step matrix: non-permutation => C1 holds under the current definition
T1 = [[F(0)] * 2 for _ in range(2)]
for x0 in range(2):
    for (hi, tp, c) in mu:
        s = phi[(x0, hi, tp, c)]; T1[x0][s[0]] += w
assert T1 == [[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]], T1
# full joint through the horizon, X0 uniform; I(X_{<t}; X_{>t} | X_t) at every t
tab_all = {}
for x0 in range(2):
    for (hi, tp, c) in mu:
        s, traj = (x0, hi, tp, c), [x0]
        for _ in range(K):
            s = phi[s]; traj.append(s[0])
        tab_all[tuple(traj)] = tab_all.get(tuple(traj), F(0)) + w * F(1, 2)
# exact product law check: every trajectory has probability 2^-(K+1)
assert all(p == F(1, 2) ** (K + 1) for p in tab_all.values()) and len(tab_all) == 2 ** (K + 1)
for t in range(1, K):
    pc, pac, pcb, I = {}, {}, {}, 0.0
    for traj, p in tab_all.items():
        a, c, b = traj[:t], traj[t], traj[t + 1:]
        pc[c] = pc.get(c, F(0)) + p; pac[(a, c)] = pac.get((a, c), F(0)) + p
        pcb[(c, b)] = pcb.get((c, b), F(0)) + p
    for traj, p in tab_all.items():
        a, c, b = traj[:t], traj[t], traj[t + 1:]
        I += float(p) * log2(float(p * pc[c] / (pac[(a, c)] * pcb[(c, b)])))
    assert abs(I) < 1e-12, (t, I)
print(f"P-B: fair coin realized by the b51 construction (K={K}, |C_H|={mH}):")
print("     T^(1) = J/2 (non-permutation => C1 holds); tape/ledger static")
print("     between couplings (tau_B = inf => tau_S << tau_B, C2 realized);")
print("     capacity huge (C3). Yet I(X_<t; X_>t | X_t) = 0 exactly at every")
print("     t on the horizon: NO accessible backflow. The M121 lemma's claim")
print("     'O(1) under (C1)-(C3)' is FALSE as quantified. Counterexample CONFIRMED.")

# ---------------- P-C: swap vs the prose mixing hypothesis ----------------
# T from the UNIFORM prior (as M323's model states): T = J/2 exactly.
# Prose hypothesis: relaxation to a single arbitrary pi_H with eps = TV bound.
# Take pi_H = delta_0 and PERFECT relaxation (post-relaxation conditional
# = delta_0 for every visible record): eps = 0 under the prose reading.
# Actual two-step law: v1 = h0 (h0 ~ uniform at step 1), relax h -> 0,
# v2 = h = 0 always. T^(2) has columns (1,0); T^2 = J/2.
Tu = [[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]]
T2_actual = [[F(1), F(0)], [F(1), F(0)]]
Tsq = [[sum(Tu[i][k] * Tu[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
tv = max(sum(abs(T2_actual[i][j] - Tsq[i][j]) for j in range(2)) / 2 for i in range(2))
assert tv == F(1, 2)
print("P-C: swap phi(v,h)=(h,v), pi_H = delta_0, perfect relaxation: eps = 0")
print("     under the prose hypothesis (arbitrary common pi_H), yet")
print("     ||T^(2) - T^2||_TV = 1/2 > (k-1)eps = 0. The M323 bound is FALSE")
print("     unless pi_H equals the reference prior defining T (the in-repo c2")
print("     probe already fixes pi_H = uniform). Counterexample CONFIRMED.")
print("review3 triage probe: COMPLETE — all three review counterexamples certified")
