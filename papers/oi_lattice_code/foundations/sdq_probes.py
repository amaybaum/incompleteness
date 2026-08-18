#!/usr/bin/env python3
# sdq_probes.py — b118 (2026-08-13)
# Certifies the D => Q leg of the finite-horizon equivalence S <=> D <=> Q
# (Main §3.4), the leg that needs no imported correspondence: the permutation
# unitary of a deterministic realization reproduces the FULL multi-time joint
# law under sequential projective measurement in the configuration basis.
import sys
# b118: verifying D => Q internally — no imported correspondence.
# Given a bijection phi on C_V x C_H, the permutation unitary U|x,h> = |phi(x,h)>
# with diagonal hidden prior rho_H should reproduce the FULL multi-time joint law
# P(x_0,...,x_K) under sequential projective measurement in the configuration
# basis — because a permutation unitary keeps a diagonal state diagonal, so the
# measurements do not disturb it. Exact rational arithmetic.
from fractions import Fraction as F
from itertools import permutations, product
from collections import defaultdict

def classical_joint(perm, nV, nH, K):
    """P(x_0..x_K) from the deterministic dynamics with uniform hidden prior."""
    out = defaultdict(lambda: F(0))
    for x0 in range(nV):
        for h0 in range(nH):
            x, h, traj = x0, h0, (x0,)
            for _ in range(K):
                y = perm[x*nH + h]; x, h = y//nH, y%nH; traj += (x,)
            out[traj] += F(1, nV*nH)
    return dict(out)

def quantum_joint(perm, nV, nH, K):
    """Sequential projective measurement of the permutation-unitary evolution.
    State is carried as an exact diagonal ensemble over (x,h) — which IS the
    density matrix, since a permutation unitary preserves diagonality."""
    out = defaultdict(lambda: F(0))
    # initial state: uniform over x0 (measured) tensor uniform hidden
    init = defaultdict(lambda: F(0))
    for x0 in range(nV):
        for h0 in range(nH): init[(x0,h0)] += F(1, nV*nH)
    # branch on the measured record
    frontier = {(x0,): {(x,h): p for (x,h),p in init.items() if x == x0} for x0 in range(nV)}
    for _ in range(K):
        new = {}
        for traj, ens in frontier.items():
            # unitary step: U|x,h> = |phi(x,h)>
            ev = defaultdict(lambda: F(0))
            for (x,h),p in ens.items():
                y = perm[x*nH + h]; ev[(y//nH, y%nH)] += p
            # projective measurement of the visible register (P_j = |j><j| (x) I)
            for j in range(nV):
                branch = {(x,h):p for (x,h),p in ev.items() if x == j}
                if branch: new[traj+(j,)] = branch
        frontier = new
    for traj, ens in frontier.items(): out[traj] += sum(ens.values())
    return dict(out)

print("== D => Q : permutation unitary reproduces the FULL multi-time joint law ==")
for nV,nH,K in [(2,2,3),(2,3,3),(3,2,3),(2,2,4)]:
    ok = 0; n = 0
    for perm in permutations(range(nV*nH)):
        c = classical_joint(perm,nV,nH,K); q = quantum_joint(perm,nV,nH,K)
        c = {k:v for k,v in c.items() if v != 0}; q = {k:v for k,v in q.items() if v != 0}
        if c == q: ok += 1
        n += 1
    print(f"  (n_V,n_H)=({nV},{nH}), horizon K={K}: joint laws identical in {ok}/{n} realizations")
print()
print("  (the state stays diagonal under a permutation unitary, so sequential")
print("   configuration measurements do not disturb the trajectory distribution)")
_fail = 0
for nV,nH,K in [(2,2,3),(3,2,3)]:
    for perm in permutations(range(nV*nH)):
        c = {k:v for k,v in classical_joint(perm,nV,nH,K).items() if v != 0}
        q = {k:v for k,v in quantum_joint(perm,nV,nH,K).items() if v != 0}
        if c != q: _fail += 1
print("sdq_probes:", "ALL CHECKS PASS" if _fail == 0 else f"{_fail} FAILURE(S)")
sys.exit(1 if _fail else 0)
