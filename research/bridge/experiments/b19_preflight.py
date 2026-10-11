#!/usr/bin/env python3
"""b19_preflight.py -- node B19 of research/bridge (round 5): pair availability is token availability. Exact preflight
of the matrix identities the design module `lean/BridgeToken.lean` (section A) proves, on the kernel's own carriers:
the token carrier Fin 2 x Fin n, the spectator carrier Fin 2 x (Fin 2 x Fin n), the pair carrier (Fin 2 x Fin 2) x
Fin n and the relabelled carrier (Fin 2 x Fin n) x Fin 2. Gaussian rationals throughout (sympy, exact).

DECISION RULE (fixed 2026-10-11T07:43:14Z, from `date -u` immediately before writing; before run 1).

Linear indices are lexicographic in the kernel's product types; a relabelling e acts on matrices by
reindex e e M = M (e^{-1} p) (e^{-1} q) (Mathlib's `Matrix.reindex`). Kernel definitions read at L:
  tensorOf A B (p, q) = A p.1 q.1 * B p.2 q.2                                        (MonoidalCompletion.lean:193)
  tokOp U n = tensorOf U 1_n;  pairOp U n = tensorOf (tensorOf 1_2 U) 1_n              (BridgeAvail.lean, round 4)
  amplRef R Phi M (p, q) = Phi (refBlockR M p.1 q.1) p.2 q.2                             (ReferenceExtension.lean:91)
  uniformAttach m rho = tensorOf rho ((1/m) 1_m);  ptraceAnc m M (s, t) = sum_e M (s, e) (t, e)
  discardWith m P Phi = ptraceAnc m . Phi . P                                             (OperationalAssembly.lean:492, :453, :515)

CHECKS (random Gaussian-rational entries in {-3..3} + i{-3..3}, seeded)
  P1  n = 1, 2, 3, three random U each: (a) reindex along the associator (Fin 2 x (Fin 2 x Fin n) -> (Fin 2 x Fin 2) x
      Fin n) carries tensorOf 1_2 (tokOp U n) to pairOp U n; (b) reindex along toEnd ((a, b), k) -> ((b, k), a) carries
      pairOp U n to tensorOf (tokOp U n) 1_2.
  P2  The discard identity: for random V on Fin 2 x Fin n (n = 1, 2) and random rho,
      discardWith 2 (uniformAttach 2) (conjChannel (tensorOf V 1_2)) rho = V rho V^H exactly.
  P3  The spectator identity: amplRef (Fin 2) (conjChannel V) M = (1_2 (x) V) M (1_2 (x) V)^H on random M (n = 1, 2).
  P4  Countercontrol: with the ancilla attached as 1_2 instead of (1/2) 1_2 the discard gives 2 V rho V^H, so the
      uniform normalization is load-bearing for P2.

VERDICT B19-PREFLIGHT-OK iff P1-P4 all PASS; otherwise VERDICT B19-PREFLIGHT-FAILED followed by the failing ids.
"""
import random
import sys

import sympy as sp

I = sp.I
random.seed(1905)
PASS, FAIL = [], []


def check(name, ok, msg):
    (PASS if ok else FAIL).append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {msg}")


def rnd(nr, nc):
    return sp.Matrix(nr, nc, lambda i, j: random.randint(-3, 3) + I * random.randint(-3, 3))


def kron(A, B):
    return sp.kronecker_product(A, B)


def dagger(M):
    return M.conjugate().T


def reindex(M, e_inv, dom, cod):
    """reindex e e M on the codomain index set `cod`: entry (p, q) = M (e^{-1} p) (e^{-1} q)."""
    di = {c: i for i, c in enumerate(dom)}
    N = len(cod)
    R = sp.zeros(N, N)
    for i, p in enumerate(cod):
        for j, q in enumerate(cod):
            R[i, j] = M[di[e_inv(p)], di[e_inv(q)]]
    return R


def entries_of(conf_fun, M):
    return M


# ---------------- P1 ----------------
p1 = True
for n in (1, 2, 3):
    tok_dom = [(b, k) for b in (0, 1) for k in range(n)]
    spec_dom = [(a, (b, k)) for a in (0, 1) for b in (0, 1) for k in range(n)]
    pair_dom = [((a, b), k) for a in (0, 1) for b in (0, 1) for k in range(n)]
    end_dom = [((b, k), a) for b in (0, 1) for k in range(n) for a in (0, 1)]
    for _ in range(3):
        U = rnd(2, 2)
        tokOp = kron(U, sp.eye(n))
        pairOp = kron(kron(sp.eye(2), U), sp.eye(n))
        spec = kron(sp.eye(2), tokOp)
        # (a) associator: e : Fin 2 x (Fin 2 x Fin n) -> (Fin 2 x Fin 2) x Fin n, e^{-1} ((a,b),k) = (a,(b,k))
        Ra = reindex(spec, lambda p: (p[0][0], (p[0][1], p[1])), spec_dom, pair_dom)
        # (b) toEnd: e ((a,b),k) = ((b,k),a), e^{-1} ((b,k),a) = ((a,b),k)
        Rb = reindex(pairOp, lambda q: ((q[1], q[0][0]), q[0][1]), pair_dom, end_dom)
        ok_a = sp.simplify(Ra - pairOp) == sp.zeros(4 * n, 4 * n)
        ok_b = sp.simplify(Rb - kron(tokOp, sp.eye(2))) == sp.zeros(4 * n, 4 * n)
        p1 = p1 and ok_a and ok_b
check("P1", p1, "reindex along the associator: 1 (x) tokOp = pairOp; along toEnd: pairOp = tokOp (x) 1_2 "
      "(n = 1, 2, 3; three random U each)")


# ---------------- P2, P4 ----------------
def ptrace_last(M, dA, m):
    out = sp.zeros(dA, dA)
    for s in range(dA):
        for tt in range(dA):
            out[s, tt] = sum(M[s * m + e, tt * m + e] for e in range(m))
    return out


p2 = p4 = True
for n in (1, 2):
    dA = 2 * n
    for _ in range(3):
        V = rnd(dA, dA)
        rho = rnd(dA, dA)
        K = kron(V, sp.eye(2))
        attached = kron(rho, sp.Rational(1, 2) * sp.eye(2))
        out = ptrace_last(K * attached * dagger(K), dA, 2)
        p2 = p2 and sp.simplify(out - V * rho * dagger(V)) == sp.zeros(dA, dA)
        attached1 = kron(rho, sp.eye(2))
        out1 = ptrace_last(K * attached1 * dagger(K), dA, 2)
        p4 = p4 and sp.simplify(out1 - 2 * V * rho * dagger(V)) == sp.zeros(dA, dA)
check("P2", p2, "discardWith 2 (uniformAttach 2) (conjChannel (V (x) 1_2)) rho = V rho V^H, exactly (n = 1, 2)")

# ---------------- P3 ----------------
p3 = True
for n in (1, 2):
    dS = 2 * n
    for _ in range(3):
        V = rnd(dS, dS)
        M = rnd(2 * dS, 2 * dS)
        ampl = sp.zeros(2 * dS, 2 * dS)
        for a in range(2):
            for a2 in range(2):
                blk = M[a * dS:(a + 1) * dS, a2 * dS:(a2 + 1) * dS]
                img = V * blk * dagger(V)
                ampl[a * dS:(a + 1) * dS, a2 * dS:(a2 + 1) * dS] = img
        L = kron(sp.eye(2), V)
        p3 = p3 and sp.simplify(ampl - L * M * dagger(L)) == sp.zeros(2 * dS, 2 * dS)
check("P3", p3, "amplRef (Fin 2) (conjChannel V) M = (1_2 (x) V) M (1_2 (x) V)^H, exactly (n = 1, 2)")
check("P4", p4, "countercontrol: the ancilla attached as 1_2 gives 2 V rho V^H (the uniform normalization is load-bearing)")

print()
print(f"PASS {len(PASS)}  FAIL {len(FAIL)}")
print("VERDICT B19-PREFLIGHT-OK" if not FAIL else "VERDICT B19-PREFLIGHT-FAILED " + " ".join(FAIL))
sys.exit(0)
