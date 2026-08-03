#!/usr/bin/env python3
"""Deterministic separation of three notions run together in earlier drafts:
complete dephasing, entanglement breaking, and P-(in)divisibility.

  T1  Entanglement breaking does NOT imply dephasing: a measure-and-prepare
      channel (measure computational basis, prepare |+><+|) is EB by
      construction, yet its output carries off-diagonal 1/2.
  T2  Dephasing DOES imply entanglement breaking (computational-basis
      dephasing: explicit measure-and-prepare form + PPT Choi). With T1,
      the containment is strict and one-way.
  T3  An entanglement-breaking one-step channel is COMPATIBLE with a
      P-indivisible visible process. The reversible dilation
          phi(v, h) = ((v + h) mod 2, (h + 1) mod 2)
      with the hidden bit initially uncorrelated and maximally mixed gives:
        - visible channel Phi(rho) = (rho + X rho X)/2, which equals complete
          dephasing in the X eigenbasis (measure sigma_x, re-prepare the
          eigenstate) -- entanglement-breaking with an explicit
          measure-and-prepare certificate, and PPT Choi (= separable in 2x2);
        - visible transition matrices T(1 step) = [[1/2,1/2],[1/2,1/2]]
          (rank 1) and T(2 steps) = [[0,1],[1,0]] (rank 2), so no matrix M
          of any kind, stochastic or not, satisfies T(2) = M T(1):
          the visible process is P-indivisible.
      Memory lives in the hidden register, not in surviving coherence.

Run:  python3 eb_pindivisibility_tests.py   (exits non-zero on any failure)
"""
import sys
import numpy as np

TOL = 1e-12
RESULTS = []


def check(name, cond):
    RESULTS.append(bool(cond))
    print(f"  {'PASS' if cond else 'FAIL'}  {name}")
    return bool(cond)


def choi_pt_min_eig(channel, d=2):
    J = np.zeros((d * d, d * d), dtype=complex)
    for i in range(d):
        for j in range(d):
            E = np.zeros((d, d), dtype=complex)
            E[i, j] = 1.0
            J[i * d:(i + 1) * d, j * d:(j + 1) * d] = channel(E)
    JT = J.reshape(d, d, d, d).transpose(0, 3, 2, 1).reshape(d * d, d * d)
    return float(np.min(np.linalg.eigvalsh((JT + JT.conj().T) / 2)))


def main():
    X = np.array([[0., 1.], [1., 0.]])
    plus = np.array([[.5, .5], [.5, .5]])

    # T1 -- EB without dephasing
    def mp_plus(rho):          # measure computational basis, prepare |+><+|
        return (rho[0, 0] + rho[1, 1]) * plus
    rho = np.array([[.7, .2 + .1j], [.2 - .1j, .3]])
    out = mp_plus(rho)
    check("T1: measure-and-prepare (hence EB) output has off-diagonal 1/2 != 0",
          abs(out[0, 1] - .5) < TOL)
    check("T1: its Choi is PPT (consistency)", choi_pt_min_eig(mp_plus) > -1e-9)

    # T2 -- dephasing is EB
    def dephase_z(rho):
        return np.diag(np.diag(rho))
    def mp_z(rho):             # the same map as measure-Z-and-reprepare
        return sum(rho[i, i] * np.outer(np.eye(2)[i], np.eye(2)[i]) for i in range(2))
    probe = np.array([[.6, .3 - .2j], [.3 + .2j, .4]])
    check("T2: computational-basis dephasing == measure-and-prepare exactly",
          np.max(np.abs(dephase_z(probe) - mp_z(probe))) < TOL)
    check("T2: dephasing Choi is PPT", choi_pt_min_eig(dephase_z) > -1e-9)

    # T3 -- EB one-step channel atop a P-indivisible process
    def phi(v, h):
        return ((v + h) % 2, (h + 1) % 2)
    states = [(v, h) for v in range(2) for h in range(2)]
    check("T3: phi is a bijection on the 2x2 configuration space",
          len({phi(*s) for s in states}) == 4)

    def Phi(rho):
        return .5 * (rho + X @ rho @ X)
    P = [(np.eye(2) + s * X) / 2 for s in (+1, -1)]
    def mp_x(rho):             # measure sigma_x, re-prepare eigenstate
        return sum(np.trace(Pi @ rho) * Pi for Pi in P)
    check("T3: Phi equals complete dephasing in the X basis (measure-and-prepare"
          " certificate -> entanglement-breaking)",
          np.max(np.abs(Phi(probe) - mp_x(probe))) < TOL)
    check("T3: Phi Choi is PPT (= separable in 2x2)", choi_pt_min_eig(Phi) > -1e-9)

    # visible multi-time statistics from the deterministic dilation,
    # hidden bit uniform and uncorrelated at t=0
    def k_step(k):
        T = np.zeros((2, 2))
        for i in range(2):
            d = {(i, 0): .5, (i, 1): .5}
            for _ in range(k):
                nd = {}
                for (v, h), p in d.items():
                    nd[phi(v, h)] = nd.get(phi(v, h), 0.) + p
                d = nd
            for (v, h), p in d.items():
                T[v, i] += p
        return T
    T1m, T2m = k_step(1), k_step(2)
    check("T3: T(1 step) = [[1/2,1/2],[1/2,1/2]]",
          np.max(np.abs(T1m - .5)) < TOL)
    check("T3: T(2 steps) = [[0,1],[1,0]]",
          np.max(np.abs(T2m - np.array([[0., 1.], [1., 0.]]))) < TOL)
    r1 = np.linalg.matrix_rank(T1m, tol=1e-9)
    r2 = np.linalg.matrix_rank(T2m, tol=1e-9)
    check("T3: rank T(1)=1 < rank T(2)=2 -> no propagator M with T(2)=M T(1) "
          "exists -> visible process is P-INDIVISIBLE", r1 == 1 and r2 == 2)

    ok = all(RESULTS)
    print("\neb_pindivisibility_tests:", "OK" if ok else "FAILURES PRESENT")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
