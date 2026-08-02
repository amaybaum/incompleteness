#!/usr/bin/env python3
"""Deterministic verification of the coherence results of Main §3.2 / Appendix B.2.

Run:  python3 coherence_enumeration.py       (exits non-zero on any failed assertion)

Conventions fixed here and used throughout:
  * visible/hidden factorisation  S = V x H, index (i,k) -> i*m + k
  * channel  Phi(rho) = Tr_H[ U_phi (rho (x) I_m/m) U_phi^dag ],  U_phi the permutation
    unitary of the bijection phi
  * Kraus operators  K_{kl} = m^{-1/2} <l| U_phi |k>_H
  * Choi matrix  C = sum_{i,j} |i><j| (x) Phi(|i><j|)   (UNNORMALISED; trace = dim V)
  * separability test: partial transpose on the INPUT factor; for dim V = 2 the Choi is a
    2 (x) 2 state, where PPT <=> separable <=> the channel is entanglement-breaking
    (Horodecki).  For dim V > 2 a negative partial transpose still certifies NON-separability,
    hence non-entanglement-breaking, but PPT alone does not certify the converse.
"""
import itertools
import sys

import numpy as np

TOL = 1e-9


def kraus(phi, n, m):
    """Kraus operators of Phi for a bijection phi given as a permutation of range(n*m)."""
    K = {}
    for i in range(n):
        for k in range(m):
            j, l = divmod(phi[i * m + k], m)
            K.setdefault((k, l), np.zeros((n, n)))[j, i] = 1.0
    return [x / np.sqrt(m) for x in K.values()]


def transition_matrix(Ks, n):
    T = np.zeros((n, n))
    for i in range(n):
        E = np.zeros((n, n))
        E[i, i] = 1.0
        T[:, i] = np.real(np.diag(sum(x @ E @ x.T for x in Ks)))
    return T


def is_permutation(T):
    return bool(np.all((np.abs(T) < TOL) | (np.abs(T - 1) < TOL)))


def choi(Ks, n):
    C = np.zeros((n * n, n * n))
    for i in range(n):
        for j in range(n):
            E = np.zeros((n, n))
            E[i, j] = 1.0
            C[i * n:(i + 1) * n, j * n:(j + 1) * n] = sum(x @ E @ x.T for x in Ks)
    return C


def min_partial_transpose_eig(C, n):
    T = C.reshape(n, n, n, n).transpose(0, 3, 2, 1).reshape(n * n, n * n)
    return float(np.min(np.linalg.eigvalsh((T + T.T) / 2)))


def is_npt(Ks, n):
    """Negative partial transpose => entangled Choi => NOT entanglement-breaking."""
    return min_partial_transpose_eig(choi(Ks, n), n) < -TOL


def check(name, condition):
    print(f"  {'PASS' if condition else 'FAIL'}  {name}")
    return condition


def main():
    ok = True

    # ---- 1. the swap counterexample: (C1) holds, yet Phi is entanglement-breaking ----
    n = m = 2
    swap = [0, 2, 1, 3]                      # phi(x,h) = (h,x) under index (x,h) -> x*m+h
    Ks = kraus(swap, n, m)
    T = transition_matrix(Ks, n)
    ok &= check("swap: T is not a permutation (C1 holds)", not is_permutation(T))
    ok &= check("swap: T_ij = 1/2 for all i,j", np.allclose(T, 0.5))
    Phi0 = sum(x @ np.array([[1.0, 0], [0, 0]]) @ x.T for x in Ks)
    ok &= check("swap: Phi(|0><0|) = I/2", np.allclose(Phi0, np.eye(2) / 2))
    ok &= check("swap: Phi is entanglement-breaking (Choi is PPT)", not is_npt(Ks, n))

    # ---- 2. exhaustive enumeration over all bijections of V x H ----
    expected = {(2, 2): (16, 16, 0), (2, 3): (648, 612, 36)}
    for (n, m), (exp_c1, exp_eb, exp_non) in expected.items():
        c1 = eb = non = 0
        for perm in itertools.permutations(range(n * m)):
            Ks = kraus(list(perm), n, m)
            if is_permutation(transition_matrix(Ks, n)):
                continue
            c1 += 1
            if is_npt(Ks, n):
                non += 1
            else:
                eb += 1
        ok &= check(f"|V|={n},|H|={m}: {c1} C1-satisfying bijections (expected {exp_c1})", c1 == exp_c1)
        ok &= check(f"|V|={n},|H|={m}: {eb} entanglement-breaking (expected {exp_eb})", eb == exp_eb)
        ok &= check(f"|V|={n},|H|={m}: {non} non-entanglement-breaking (expected {exp_non})", non == exp_non)

    # ---- 3. boundary bounds for the linear realisation on a ring ----
    def gf2_rank(M):
        M = M.copy() % 2
        r = 0
        for c in range(M.shape[1]):
            piv = next((i for i in range(r, M.shape[0]) if M[i, c]), None)
            if piv is None:
                continue
            M[[r, piv]] = M[[piv, r]]
            for i in range(M.shape[0]):
                if i != r and M[i, c]:
                    M[i] = (M[i] + M[r]) % 2
            r += 1
        return r

    def update(L):
        A = np.zeros((L, L), int)
        for i in range(L):
            A[i, (i - 1) % L] ^= 1
            A[i, (i + 1) % L] ^= 1
        M = np.zeros((2 * L, 2 * L), int)
        M[:L, :L] = A
        M[:L, L:] = np.eye(L, dtype=int)
        M[L:, :L] = np.eye(L, dtype=int)
        return M % 2

    good = True
    for L in range(4, 13):
        for Lv in range(1, L):
            M = update(L)
            vis = list(range(Lv)) + list(range(L, L + Lv))
            hid = [i for i in range(2 * L) if i not in vis]
            R, Rc = set(range(Lv)), set(range(Lv, L))
            dminus = {x for x in R if any(((x + s) % L) in Rc for s in (1, -1))}
            dplus = {y for y in Rc if any(((y + s) % L) in R for s in (1, -1))}
            good &= gf2_rank(M[np.ix_(hid, vis)]) <= len(dplus)
            good &= gf2_rank(M[np.ix_(vis, hid)]) <= len(dminus)
    ok &= check("boundary bounds rank M_HV <= |d+R|, rank M_VH <= |d-R| (rings L=4..12)", good)

    print("\ncoherence_enumeration:", "OK" if ok else "FAILURES PRESENT")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
