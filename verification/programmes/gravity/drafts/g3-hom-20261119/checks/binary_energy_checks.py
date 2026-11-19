#!/usr/bin/env python3
"""G3-HOM node 1: the real value of the quadratic E on binary configurations.

Rule (SM Remark, cycle structure): F(u, v) = (v, A v - u) mod q on the torus
(Z/L)^d, A = alpha * (sum of the 2d nearest neighbours), alpha = 1.
E(u, v) = u.u + v.v - u.A v, evaluated as an INTEGER on the representatives
0..q-1 (not reduced mod q).

Checks (all exact integer arithmetic):
  1. d=1, q=2: the mover counts N_L = sum_i [u_i xor v_{i+1}] and
     N_R = sum_i [u_{i+1} xor v_i] are each conserved, exhaustively, L = 3..10;
     E_int = (N_L + N_R)/2 identically, so E_int is conserved over the integers.
  2. Time reversal Theta(u, v) = (v, u) maps N_L to N_R.
  3. N_L and N_R are linearly independent with the constants (two witnesses).
  4. Countercontrols: E_int is NOT conserved for d=1, q=3 at L=5 (exhaustive
     search for a witness), for d=2, q=2 at L=3 (exhaustive) and for d=3, q=2 at
     L=3, 4 (exhaustive over u = 0 and v supported on at most three sites).
     Each reports the first witness found.
Run:  python3 -I binary_energy_checks.py   (exit status 0 iff every check holds)
"""

import sys
from itertools import combinations, product

RESULTS = []


def check(name, ok):
    RESULTS.append((name, bool(ok)))
    print(f"CHECK {name}: {'PASS' if ok else 'FAIL'}")


def torus(L, d):
    sites = list(product(range(L), repeat=d))
    idx = {s: k for k, s in enumerate(sites)}
    nbrs = []
    for s in sites:
        nb = []
        for j in range(d):
            for e in (-1, 1):
                t = list(s)
                t[j] = (t[j] + e) % L
                nb.append(idx[tuple(t)])
        nbrs.append(nb)
    return len(sites), nbrs


def step(u, v, nbrs, q):
    return v, tuple((sum(v[j] for j in nbrs[i]) - u[i]) % q for i in range(len(u)))


def E_int(u, v, nbrs):
    return sum(x * x for x in u) + sum(x * x for x in v) - sum(u[i] * sum(v[j] for j in nbrs[i]) for i in range(len(u)))


def movers(u, v):
    L = len(u)
    NL = sum(u[i] ^ v[(i + 1) % L] for i in range(L))
    NR = sum(u[(i + 1) % L] ^ v[i] for i in range(L))
    return NL, NR


def main():
    ok_mov = ok_id = ok_rev = True
    for L in range(3, 11):
        n, nbrs = torus(L, 1)
        for bits in product((0, 1), repeat=2 * L):
            u, v = bits[:L], bits[L:]
            u2, v2 = step(u, v, nbrs, 2)
            NL, NR = movers(u, v)
            NL2, NR2 = movers(u2, v2)
            ok_mov &= (NL, NR) == (NL2, NR2)
            ok_id &= 2 * E_int(u, v, nbrs) == NL + NR
            ok_rev &= movers(v, u) == (NR, NL)
    check("d=1, q=2, L=3..10: N_L and N_R each conserved (exhaustive)", ok_mov)
    check("d=1, q=2, L=3..10: 2 E_int = N_L + N_R identically, so E_int is conserved over Z", ok_id)
    check("d=1, q=2: reversal (u,v)->(v,u) exchanges N_L and N_R", ok_rev)
    e0, e1 = (1, 0, 0, 0, 0), (0, 1, 0, 0, 0)
    z = (0, 0, 0, 0, 0)
    check("N_L, N_R and 1 are linearly independent (values (0,0), (0,2), (2,0) at three configurations)",
          movers(z, z) == (0, 0) and movers(e0, e1) == (0, 2) and movers(e1, e0) == (2, 0))

    def sparse(n, kmax=3):
        # u = 0 and v supported on at most kmax sites, in lexicographic order
        for k in range(1, kmax + 1):
            for S in combinations(range(n), k):
                yield tuple([0] * n) + tuple(1 if i in S else 0 for i in range(n))

    def witness(L, d, q, exhaustive):
        n, nbrs = torus(L, d)
        gen = product(range(q), repeat=2 * n) if exhaustive else sparse(n)
        for bits in gen:
            u, v = bits[:n], bits[n:]
            u2, v2 = step(u, v, nbrs, q)
            e1, e2 = E_int(u, v, nbrs), E_int(u2, v2, nbrs)
            if e1 != e2:
                return (u, v, e1, e2)
            if (e1 - e2) % q:
                return ("modular violation", u, v)
        return None

    for (L, d, q, ex) in [(5, 1, 3, True), (3, 2, 2, True), (3, 3, 2, False), (4, 3, 2, False)]:
        w = witness(L, d, q, ex)
        print(f"d={d} q={q} L={L}: witness of non-conservation over Z = {w}")
        check(f"countercontrol d={d}, q={q}, L={L}: E_int not conserved over Z (witness found)",
              w is not None and w[0] != "modular violation")
    ok = all(o for _, o in RESULTS)
    print("ALL CHECKS", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
