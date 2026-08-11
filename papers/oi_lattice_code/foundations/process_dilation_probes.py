#!/usr/bin/env python3
# process_dilation_probes.py — b51 preregistered probe (2026-08-10).
# Certifies the finite-horizon process-dilation construction of the b51 prereg:
# hidden = (hist, tape, clock), conditional-quantile step, lexicographic
# completion to a full bijection, mu_H = uniform on {hist = pad, clock = 0} x tapes.
# Exact rational arithmetic; any failed assertion fails the attempt.
# P1 XOR-involution law (n=2, K=3, D=2)          — full joint match, exact
# P2 hand-specified non-Markov kernels (K=3,D=4) — full joint match, exact; T2 != T1^2
# P3 b48 revival-bijection law (n=3, m=2, K=3)   — full joint match, exact
# P4 permutation target (must-be-silent)         — realized T is a permutation, P-divisible
# P5 bijectivity of every constructed phi        — sorted image == domain
# P6 capacity check on P3 (info, float)          — |C_H| >= 2^{I*}

from fractions import Fraction as F
from math import log2
import itertools

PAD = -1  # integer sentinel so mixed tuples stay orderable

# ---------- target laws as conditional kernels ----------
def kernels_from_model(phi, nV, nH, K):
    """Exact conditional kernels P(x_{k+1} | x_0..x_k) of a bijection model with
    uniform hidden prior, by enumeration; unreachable pasts -> deterministic 0."""
    # trajectories: for each (x0,h) the deterministic visible path
    paths = {}
    for x0 in range(nV):
        for h in range(nH):
            s, traj = (x0, h), [x0]
            for _ in range(K):
                s = phi[s]; traj.append(s[0])
            paths[(x0, h)] = tuple(traj)
    def kern(past):  # past = (x_0..x_c) -> dist over x_{c+1}
        c = len(past) - 1
        num = [0] * nV; den = 0
        for (x0, h), tr in paths.items():
            if tr[:c + 1] == tuple(past):
                den += 1; num[tr[c + 1]] += 1
        if den == 0: return tuple(F(1) if i == 0 else F(0) for i in range(nV))
        return tuple(F(n_, den) for n_ in num)
    return kern

def joint_from_kernels(kern, nV, K, x0):
    """Exact joint P(x_1..x_K | x_0) as dict."""
    out = {}
    for traj in itertools.product(range(nV), repeat=K):
        p = F(1); past = (x0,)
        for k in range(K):
            p *= kern(past)[traj[k]]
            past = past + (traj[k],)
        if p: out[traj] = p
    return out

# ---------- the preregistered construction ----------
def build_dilation(kern, nV, K, D):
    """Return (phi dict on full product, mu support iterator, C_H size)."""
    hist_space = list(itertools.product(list(range(nV)) + [PAD], repeat=K))
    tape_space = list(itertools.product(range(D), repeat=K))
    states = [(x, hi, tp, c) for x in range(nV) for hi in hist_space
              for tp in tape_space for c in range(K + 1)]
    def wellformed(hi, c):
        return all(hi[i] != PAD for i in range(c)) and all(hi[i] == PAD for i in range(c, K))
    # fiber map from a distribution: tape symbol s -> outcome via cumulative D-fibers
    def Q(past, s):
        dist = kern(past)
        acc = 0
        for y in range(nV):
            cnt = dist[y] * D
            assert cnt.denominator == 1, "D is not a common denominator"
            acc += int(cnt)
            if s < acc: return y
        raise AssertionError("fibers do not fill D")
    phi = {}
    for (x, hi, tp, c) in states:
        if c < K and wellformed(hi, c):
            past = tuple(hi[:c]) + (x,)
            xn = Q(past, tp[c])
            hin = tuple(list(hi[:c]) + [x] + [PAD] * (K - c - 1))
            phi[(x, hi, tp, c)] = (xn, hin, tp, c + 1)
    # injectivity of the partial map is structural; verify anyway
    imgs = list(phi.values())
    assert len(imgs) == len(set(imgs)), "partial map not injective"
    # lexicographic completion to a full bijection
    unhit = sorted(set(states) - set(imgs))
    undom = sorted(set(states) - set(phi.keys()))
    assert len(unhit) == len(undom)
    for a, b in zip(undom, unhit): phi[a] = b
    assert sorted(phi.values()) == sorted(states), "completion failed"      # P5
    mu_support = [(tuple([PAD] * K), tp, 0) for tp in tape_space]
    return phi, mu_support, len(hist_space) * len(tape_space) * (K + 1)

def realized_joint(phi, mu_support, nV, K, x0):
    out = {}
    w = F(1, len(mu_support))
    for (hi, tp, c) in mu_support:
        s, traj = (x0, hi, tp, c), []
        for _ in range(K):
            s = phi[s]; traj.append(s[0])
        t = tuple(traj); out[t] = out.get(t, F(0)) + w
    return out

def realized_Tk(phi, mu_support, nV, K, k):
    T = [[F(0)] * nV for _ in range(nV)]
    w = F(1, len(mu_support))
    for x0 in range(nV):
        for (hi, tp, c) in mu_support:
            s = (x0, hi, tp, c)
            for _ in range(k): s = phi[s]
            T[x0][s[0]] += w
    return T

def certify(name, kern, nV, K, D):
    phi, mu, mH = build_dilation(kern, nV, K, D)
    for x0 in range(nV):
        assert realized_joint(phi, mu, nV, K, x0) == joint_from_kernels(kern, nV, K, x0), \
            f"{name}: joint mismatch at x0={x0}"
    print(f"{name}: FULL multi-time joint reproduced EXACTLY (all x0; K={K}, D={D}, |C_H|={mH})")
    return phi, mu, mH

# ---------- P1: XOR involution ----------
phiX = {(v, h): (v ^ h, h) for v in range(2) for h in range(2)}
kX = kernels_from_model(phiX, 2, 2, 3)
certify("P1 XOR-law", kX, 2, 3, 2)

# ---------- P2: hand-specified non-Markov kernels ----------
def kNM(past):
    c = len(past) - 1
    if c == 0:
        return (F(3,4), F(1,4)) if past[0] == 0 else (F(1,4), F(3,4))
    if c == 1:
        return (F(1), F(0)) if past[0] == past[1] else (F(0), F(1))
    return (F(1,4), F(3,4)) if past[1] == 0 else (F(3,4), F(1,4))
phi2, mu2, _ = certify("P2 non-Markov", kNM, 2, 3, 4)
T1 = realized_Tk(phi2, mu2, 2, 3, 1); T2 = realized_Tk(phi2, mu2, 2, 3, 2)
T1sq = [[sum(T1[i][k] * T1[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
assert T2 != T1sq, "P2 must be non-Markovian"
print(f"P2: T^(2) != (T^(1))^2 certified — realized T2 row0 {T2[0]} vs product {T1sq[0]}")

# ---------- P3: b48 revival law ----------
phiR = {(0,0):(0,0), (0,1):(0,1), (1,0):(1,0), (1,1):(2,0), (2,0):(1,1), (2,1):(2,1)}
kR = kernels_from_model(phiR, 3, 2, 3)
phi3, mu3, mH3 = certify("P3 revival-law", kR, 3, 3, 2)
R1 = realized_Tk(phi3, mu3, 3, 3, 1); R2 = realized_Tk(phi3, mu3, 3, 3, 2)
assert R1 == [[F(1),F(0),F(0)],[F(0),F(1,2),F(1,2)],[F(0),F(1,2),F(1,2)]] and \
       R2 == [[F(1) if i==j else F(0) for j in range(3)] for i in range(3)]
print("P3: realized family reproduces the P-indivisible revival exactly (T1 rank-2, T2 = I)")

# ---------- P4: permutation control (must-be-silent) ----------
phiP = {(v, h): (1 - v, h) for v in range(2) for h in range(2)}
kP = kernels_from_model(phiP, 2, 2, 3)
phi4, mu4, _ = certify("P4 permutation", kP, 2, 3, 1)
P1m = realized_Tk(phi4, mu4, 2, 3, 1)
assert all(sorted(row) == [F(0), F(1)] for row in P1m), "control must yield a permutation T"
# P-divisibility: T^(k) = (T^(1))^k for all k on the horizon
for k in (2, 3):
    Pk = realized_Tk(phi4, mu4, 2, 3, k)
    Mk = P1m
    for _ in range(k - 1):
        Mk = [[sum(Mk[i][l] * P1m[l][j] for l in range(2)) for j in range(2)] for i in range(2)]
    assert Pk == Mk
print("P4: permutation target realized as a permutation process, P-divisible (control silent)")

# ---------- P6: capacity (info, float) ----------
# I* over the P3 horizon: I(X_{<t}; X_{>t} | X_t) at t = 1, 2 from the exact joint
def Istar():
    # I(X_{<t}; X_{>t} | X_t) with X0 uniform, aggregated over x0 BEFORE the
    # information computation (b55 fix: the earlier per-x0 aggregation dropped
    # the X0 uncertainty from A and under-reported I*; review-3 finding).
    best = 0.0
    for t in (1, 2):
        tab = {}
        for x0 in range(3):
            J = joint_from_kernels(kR, 3, 3, x0)
            for traj, p in J.items():
                full = (x0,) + traj
                a, c, b = full[:t], full[t], full[t + 1:]
                tab[(a, c, b)] = tab.get((a, c, b), F(0)) + p * F(1, 3)
        pc, pac, pcb = {}, {}, {}
        for (a, c, b), p in tab.items():
            pc[c] = pc.get(c, F(0)) + p
            pac[(a, c)] = pac.get((a, c), F(0)) + p
            pcb[(c, b)] = pcb.get((c, b), F(0)) + p
        I = 0.0
        for (a, c, b), p in tab.items():
            if p: I += float(p) * log2(float(p * pc[c] / (pac[(a, c)] * pcb[(c, b)])))
        best = max(best, I)
    return best
Istar_v = Istar()
assert abs(Istar_v - 2/3) < 1e-9, f"revival I* must be 2/3 bits (X2 = X0 reveals X0 beyond X1): got {Istar_v}"
assert 2 ** Istar_v <= mH3 + 1e-9
print(f"P6: I* = {Istar_v:.4f} bits, 2^I* = {2**Istar_v:.3f} <= |C_H| = {mH3} (capacity bound holds; info)")
print("b51 dilation probe: COMPLETE")
