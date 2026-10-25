#!/usr/bin/env python3
"""Mutants for checks.py (PLAN §3, amendment A2).

Each mutant patches one function of a fresh copy of checks.py and runs the full suite.
A mutant is caught iff the run fails cleanly (would print VOID and exit 2) and its targeted
control is among the failed controls; collateral failures are listed.
Run:  python3 -I -B mutants.py > mutants-output.txt
"""
import sys
import os
import math
import importlib.util
import multiprocessing

HERE = os.path.dirname(os.path.abspath(__file__))


def fresh():
    spec = importlib.util.spec_from_file_location("bh02_checks", os.path.join(HERE, "checks.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def m_bij(c):
    orig = c.random_perm
    def rp(N, rng):
        lst = orig(N, rng)
        lst[1] = lst[0]
        return lst
    c.random_perm = rp


def m_rank(c):
    c.exact_rank = lambda M: 1


def m_overlap(c):
    c.cc3_unitary = lambda psi, n: c.apply_perm(c.cnot_perm(n, 0, 1), psi)


def m_tight(c):
    c.tight_cnot = lambda n, i, k: c.cnot_perm(n, i, (i + 1) % k)


def m_eig(c):
    orig = c.jacobi_eigs
    c.jacobi_eigs = lambda A, max_sweeps=60: orig(A, 1)   # stops after one sweep


def m_page_mc(c):
    def hs(dim, rng):
        v = [complex(rng.gauss(0.0, 1.0), 0.0) for _ in range(dim)]
        nrm = math.sqrt(sum(abs(a) ** 2 for a in v))
        return [a / nrm for a in v]
    c.haar_state = hs


def m_page_formula(c):
    Fr = c.Fr
    def pe(m, k):
        if m > k:
            m, k = k, m
        s = Fr(0)
        for j in range(k, m * k + 1):          # off by one
            s += Fr(1, j)
        return s - Fr(m - 1, 2 * k)
    c.page_exact = pe


def m_unitary(c):
    orig = c.gram_schmidt_unitary
    c.gram_schmidt_unitary = lambda rng, d=4, normalize=True: orig(rng, d, normalize=False)


def m_ln(c):
    orig = c.atanh2_interval
    c.atanh2_interval = lambda z, terms=60, remainder=True: orig(z, 3, False)


def m_plus(c):
    def ps(n):
        v = [1] * (2 ** n)
        v[0] = -1
        return v
    c.plus_state_scaled = ps


def m_page2013(c):
    Fr = c.Fr
    def pf(beta):
        y = Fr(beta) / (1 + Fr(beta))
        return 1 - y, 1 - y, y                 # exponent 3/2 replaced by 1
    c.page_fraction_beta = pf


def m_ode(c):
    def rk(alpha_of_M, turnover_M2, steps=200000):
        def integ(a, b):
            h = (b - a) / steps
            f = lambda m: 1.0 / alpha_of_M(m)  # m^2 factor dropped
            return sum(h * (f(a + i * h) + 4 * f(a + i * h + h / 2) + f(a + i * h + h)) / 6
                       for i in range(steps))
        return integ(math.sqrt(turnover_M2), 1.0) / integ(0.0, 1.0)
    c.simpson_page_time = rk


def m_classical(c):
    def ev(p, sigma):
        q = [0.0] * len(p)
        for x in range(len(p)):
            q[sigma[x] if x != 1 else sigma[0]] += p[x]   # not injective
        return q
    c.evolve_dist = ev


def m_cc5(c):
    Fr = c.Fr
    c.low_entropy_state = lambda n: [Fr(-1 if (x >> (n - 1)) & 1 else 1, 2 ** (n // 2))
                                     for x in range(2 ** n)]


def m_canonical(c):
    orig = c.canonical_entropy_interval
    def ci(D, secs):
        lo, hi = orig(D, secs)
        return lo * c.Fr(9, 10), hi * c.Fr(9, 10)    # reviewer mutant R5
    c.canonical_entropy_interval = ci


def m_diag(c):
    c.diag_shell_mean = lambda m: c.harmonic(m) - c.Fr(1, 2)


def m_ct1(c):
    c.PAGE_TOL = 0.001


MUTANTS = [
    ("M-bij", "K-bij", m_bij),
    ("M-rank", "K-rank", m_rank),
    ("M-overlap", "K-overlap", m_overlap),
    ("M-tight", "K-tight", m_tight),
    ("M-eig", "K-eig", m_eig),
    ("M-page-mc", "K-page-mc", m_page_mc),
    ("M-page-formula", "K-page-formula", m_page_formula),
    ("M-unitary", "K-unitary", m_unitary),
    ("M-ln", "K-ln", m_ln),
    ("M-plus", "K-plus", m_plus),
    ("M-page2013", "K-page2013", m_page2013),
    ("M-ode", "K-ode", m_ode),
    ("M-classical", "K-classical", m_classical),
    ("M-cc5", "CC5", m_cc5),
    ("M-ct1", "CT1", m_ct1),
    ("M-canonical", "K-shell", m_canonical),
    ("M-diag", "K-diag", m_diag),
]


def run_one(i):
    name, target, patch = MUTANTS[i]
    c = fresh()
    patch(c)
    try:
        _, controls = c.run()
    except Exception as e:  # an unclean failure is not a catch
        return (name, target, "exception: %s" % type(e).__name__, [], False)
    failed = sorted(k for k, v in controls.items() if not v)
    caught = bool(failed) and target in failed
    return (name, target, "clean", failed, caught)


def main():
    base = fresh()
    _, controls = base.run()
    unmod_failed = sorted(k for k, v in controls.items() if not v)
    print("unmodified run: failed controls = %s" % (unmod_failed or "none"))
    if unmod_failed:
        print("VOID: unmodified run fails; mutants not run")
        sys.exit(2)
    with multiprocessing.Pool(4) as pool:
        rows = pool.map(run_one, range(len(MUTANTS)))
    allc = True
    for name, target, mode, failed, caught in rows:
        allc = allc and caught
        print("%-15s target=%-15s run=%s caught=%s failed=[%s]"
              % (name, target, mode, caught, ", ".join(failed)))
    print("ALL MUTANTS CAUGHT" if allc else "VOID: a mutant was not caught")
    sys.exit(0 if allc else 2)


if __name__ == "__main__":
    main()
