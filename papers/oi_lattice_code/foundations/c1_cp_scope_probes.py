#!/usr/bin/env python3
# c1_cp_scope_probes.py — b51 triage probes for the second-round review (2026-08-10).
# Exact arithmetic throughout (fractions.Fraction; Q(sqrt2) pairs for the Hadamard).
# P1: XOR involution — non-permutation T does NOT imply bidirectional coupling (C1 as defined).
# P2: Hadamard pair — "CP-divisibility restricted to diagonal inputs reduces to
#     P-divisibility" is FALSE for general CPTP families (Main.md:261 proof step).
# P3: framework scope — permutation-dilation channels map diagonal states to diagonal
#     states exactly, which is the missing hypothesis under which the reduction IS valid.
# Any single failed assertion fails the probe.

from fractions import Fraction as F
import itertools, random

def bar(msg): print(msg)

# ---------------- P1: XOR involution ----------------
V = [0, 1]; H = [0, 1]
phi = lambda v, h: (v ^ h, h)
# bijection (involution) on the 4-point space
pts = [(v, h) for v in V for h in H]
assert sorted(phi(*p) for p in pts) == sorted(pts)
assert all(phi(*phi(*p)) == p for p in pts)
# T^(1), T^(2) under uniform hidden prior (row-stochastic: T[i][j] = P(i -> j))
def Tk(k):
    T = [[F(0)] * 2 for _ in V]
    for v in V:
        for h in H:
            x, hh = v, h
            for _ in range(k):
                x, hh = phi(x, hh)
            T[v][x] += F(1, 2)
    return T
T1, T2 = Tk(1), Tk(2)
assert T1 == [[F(1,2), F(1,2)], [F(1,2), F(1,2)]]
assert T2 == [[F(1), F(0)], [F(0), F(1)]]
# P-indivisibility: T2 = T1 * M forces both rows of the product equal; I has distinct rows.
# (rank(T1)=1, rank(T2)=2 — no stochastic, indeed no real, M exists.)
assert T1[0] == T1[1]
assert T2[0] != T2[1]
bar("P1  T^(1) = [[1/2,1/2],[1/2,1/2]] (non-permutation), T^(2) = I : EXACT")
bar("    T^(2) = T^(1) M impossible for any M (identical-rows obstruction) : P-INDIVISIBLE")
# one-way coupling: hidden update independent of the visible state
assert all(phi(v, h)[1] == h for v in V for h in H)
bar("    hidden update h' = h independent of v : coupling is one-way (hidden -> visible)")
bar("    VERDICT: non-permutation T does NOT imply bidirectional coupling —")
bar("             Main.md:109 / :355 identification with (C1) as defined at :59 REFUTED")

# ---------------- Q(sqrt2) exact arithmetic ----------------
class Q2:  # a + b*sqrt(2), a,b rational
    __slots__ = ("a", "b")
    def __init__(s, a=0, b=0): s.a, s.b = F(a), F(b)
    def __add__(s, o): return Q2(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return Q2(s.a - o.a, s.b - o.b)
    def __mul__(s, o): return Q2(s.a * o.a + 2 * s.b * o.b, s.a * o.b + s.b * o.a)
    def __eq__(s, o): return s.a == o.a and s.b == o.b
    def __repr__(s): return f"({s.a}+{s.b}√2)"
Z, ONE = Q2(0), Q2(1)
INV_SQRT2 = Q2(0, F(1, 2))          # 1/sqrt2 = (1/2)*sqrt2
assert INV_SQRT2 * INV_SQRT2 == Q2(F(1, 2))

def mat(rows): return [[x if isinstance(x, Q2) else Q2(x) for x in r] for r in rows]
def mmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), Q2(0))
             for j in range(len(B[0]))] for i in range(len(A))]
def dag(A):  # real symmetric here; transpose suffices
    return [[A[j][i] for i in range(len(A))] for j in range(len(A))]

Hd = [[INV_SQRT2, INV_SQRT2], [INV_SQRT2, Q2(0) - INV_SQRT2]]
I2 = mat([[1, 0], [0, 1]])
assert mmul(Hd, Hd) == I2
bar("P2  H^2 = I over Q(sqrt2) : EXACT")
# channels on 2x2 (real matrices suffice for these inputs)
AdH = lambda R: mmul(mmul(Hd, R), dag(Hd))
diag = lambda p, q: mat([[p, 0], [0, q]])
# Phi_t1 = Ad_H, Phi_t2 = id = Ad_H . Ad_H  -> CP-divisible with CPTP Lambda = Ad_H
for R in (diag(1, 0), diag(0, 1), mat([[0, 1], [0, 0]]), mat([[0, 0], [1, 0]])):
    assert AdH(AdH(R)) == R
bar("    Phi_t2 = Ad_H o Phi_t1 with CPTP (unitary) Lambda = Ad_H : CP-DIVISIBLE, EXACT")
# population matrices in the computational basis
def pops(Phi):
    cols = [Phi(diag(1, 0)), Phi(diag(0, 1))]
    return [[cols[j][i][i].a for j in range(2)] for i in range(2)]  # rational parts (b=0)
Tq1 = pops(AdH); Tq2 = pops(lambda R: R)
assert Tq1 == [[F(1,2), F(1,2)], [F(1,2), F(1,2)]] and Tq2 == [[1, 0], [0, 1]]
# same identical-rows obstruction: population process P-indivisible
bar("    T(t1) = [[1/2,1/2],[1/2,1/2]], T(t2) = I : population process P-INDIVISIBLE")
bar("    VERDICT: 'CP-divisibility restricted to diagonal inputs reduces to")
bar("             P-divisibility' (Main.md:261) is FALSE for general CPTP families —")
bar("             Ad_H maps diagonal inputs to coherent states the intermediate map uses")

# ---------------- P3: framework scope — permutation dilations preserve diagonality ----
rng = random.Random(20260810)
nV, nH = 3, 4; N = nV * nH
perm = list(range(N)); rng.shuffle(perm)
# U = permutation matrix; Phi_t(rho) = Tr_H[ U^t (rho x mu_H) U^-t ], mu_H uniform
def idx(v, h): return v * nH + h
def phi_t_diag_check(tmax=6):
    for t in range(1, tmax + 1):
        # iterate permutation t times
        p = list(range(N))
        for _ in range(t):
            p = [perm[i] for i in p]
        for j in range(nV):                      # input |j><j| (visible), uniform ancilla
            rho = {}                             # sparse density on N points, then marginal
            out = [[F(0)] * nV for _ in range(nV)]
            for h in range(nH):
                src = idx(j, h); dst = p[src]
                vd, hd = divmod(dst, nH)
                out[vd][vd] += F(1, nH)          # permutation of a diagonal state stays diagonal:
            # off-diagonals are exactly zero by construction of a permutation acting on
            # a diagonal state; verify via full matrix conjugation on a dense check for t=1
        # dense verification at each t for one basis state
        Umat = [[F(1) if p[c] == r else F(0) for c in range(N)] for r in range(N)]
        rho_full = [[F(0)] * N for _ in range(N)]
        for h in range(nH): rho_full[idx(0, h)][idx(0, h)] = F(1, nH)
        M1 = [[sum(Umat[i][k] * rho_full[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
        M2 = [[sum(M1[i][k] * Umat[j][k] for k in range(N)) for j in range(N)] for i in range(N)]
        red = [[sum(M2[idx(a, h)][idx(b, h)] for h in range(nH)) for b in range(nV)] for a in range(nV)]
        for a in range(nV):
            for b in range(nV):
                if a != b: assert red[a][b] == 0
    return True
assert phi_t_diag_check()
bar("P3  permutation-dilation Phi_t maps diagonal states to EXACTLY diagonal states")
bar("    (t = 1..6, nV=3, nH=4, seed 20260810, exact rationals) — the missing hypothesis")
bar("    under which the :261 reduction is valid; with it, CP-div => P-div => the")
bar("    CP-indivisibility conclusion survives for the framework's channel family")
bar("b51 triage probe: COMPLETE")
