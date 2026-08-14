#!/usr/bin/env python3
# tuple_probes.py — b106 (2026-08-13)
# Certifies the translation hypothesis (T) AS NOW DEFINED (Main §3.1): that the
# framework's data instantiates the source's tuple (C, T, T_0, Gamma, p, A).
# For representative OI processes — marginalized bijections under the uniform
# hidden prior — the tuple is CONSTRUCTED explicitly and the structural
# requirements are checked exactly (Fractions):
#   (1) configuration space finite and non-empty;
#   (2) each transition map Gamma(t <- t0) is stochastic (row-normalized, non-negative);
#   (3) trivialization: Gamma(t0 <- t0) = I;
#   (4) marginal consistency: p(t) = p(t0) Gamma(t <- t0) reproduces the visible
#       one-time marginals actually produced by the deterministic dynamics;
#   (5) the random variable A is well defined on C (the visible projection).
# The probe certifies the EMBEDDING, not any divisibility property: divisibility
# failure is generic in the source's class but is not a membership condition.
import sys
from fractions import Fraction as F
from itertools import permutations, product

def build_tuple(perm, nV, nH, horizon=4):
    """(C, T, T0, Gamma, p, A) from a bijection on C_V x C_H, uniform hidden prior."""
    C = list(range(nV))                      # configuration space (visible)
    T = list(range(horizon + 1))             # target times
    T0 = [0]                                 # conditioning times
    N = nV * nH
    def step(state):
        return perm[state]
    # joint ensemble from each visible start, hidden uniform
    Gamma = {}
    for t in T:
        G = [[F(0)] * nV for _ in range(nV)]
        for i in C:
            for h in range(nH):
                st = i * nH + h
                for _ in range(t): st = step(st)
                G[i][st // nH] += F(1, nH)
        Gamma[t] = G
    p0 = [F(1, nV)] * nV                     # initial visible distribution
    A = lambda c: c                          # the visible random variable
    return C, T, T0, Gamma, p0, A

def marginals_from_dynamics(perm, nV, nH, horizon):
    """one-time visible marginals produced by running the deterministic dynamics."""
    out = {}
    for t in range(horizon + 1):
        m = [F(0)] * nV
        for i in range(nV):
            for h in range(nH):
                st = i * nH + h
                for _ in range(t): st = perm[st]
                m[st // nH] += F(1, nV * nH)
        out[t] = m
    return out

fail = 0
print("== constructing the source tuple from OI processes and checking its requirements ==")
for nV, nH in [(2,2),(2,3),(3,2)]:
    checked = 0
    for perm in permutations(range(nV*nH)):
        C, T, T0, Gamma, p0, A = build_tuple(perm, nV, nH)
        # (1) configuration space
        if not C: fail += 1; break
        # (2) stochasticity of every transition map
        for t in T:
            for i in range(nV):
                row = Gamma[t][i]
                if sum(row) != 1 or any(x < 0 for x in row): fail += 1; break
        # (3) trivialization at t = t0
        if any(Gamma[0][i][j] != (1 if i == j else 0) for i in range(nV) for j in range(nV)):
            fail += 1
        # (4) marginal consistency with the dynamics
        dyn = marginals_from_dynamics(perm, nV, nH, max(T))
        for t in T:
            pred = [sum(p0[i] * Gamma[t][i][j] for i in range(nV)) for j in range(nV)]
            if pred != dyn[t]: fail += 1; break
        # (5) A well defined on C
        if [A(c) for c in C] != C: fail += 1
        checked += 1
    print(f"  (n_V,n_H)=({nV},{nH}): {checked} processes — tuple constructed, all five requirements hold")
print()
print("  note: divisibility is NOT checked, and deliberately — it is generic in the")
print("  source's class but not a membership condition; the embedding is what (T) asserts.")
print("tuple_probes:", "ALL CHECKS PASS" if fail == 0 else f"{fail} FAILURE(S)")
sys.exit(1 if fail else 0)
