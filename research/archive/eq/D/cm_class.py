#!/usr/bin/env python3
"""EQ-D, node N2 (K3 vocabulary): the cardinality-split class

    I_cm S K  :=  (card S is a power of 2)  or  (K is monomial)

i.e. `fullClass` on the carriers the hypothetical K2 interface supplies and `substratumClass` (monomials,
StructuralClosure.lean:180) everywhere else.  Claims checked here, exactly:

  (K2)   I_cm contains every operator on every power-of-2 carrier (so DrivesElementary holds at Fin 2).
  (ARCH) one/mul/smul/proj/block: closure of the monomial predicate (kernel lemmas submonomial_* in
         StructuralClosure.lean) plus the arithmetic lemma  card S * m = 2^j, m >= 1  =>  card S = 2^i.
         The lemma is a consequence of unique factorisation; it is checked exhaustively below as a control.
  (LABEL)(DAGGER) reindex and conjTranspose preserve cardinality and monomiality (kernel lemmas).
  (NOT-CTX)   ContextStable fails: R = Fin 3, S = Fin 2, K = flow (transition 0 1) (pi/4) is admissible
              (power-of-2 carrier) but 1_3 (x) K on the 6-element carrier is not monomial.
  (NOT-DRIVE) DrivesElementary fails at Fin 3: flow (transition 0 1) (pi/4) on Fin 3 is not monomial.
  (NOT-QM2)   Even the qubit theory genTheory I_cm (Fin 2) is not QM: its level 3 is the 6-element carrier,
              every carrier reachable from it by `discard` has size divisible by 3, so every admissible
              operator used is monomial; monomial conjugations preserve diagonal matrices and the level-3
              unitary rot (x) 1_3 does not (exact witness).

Spot checks of the monomial closure use random exact Gaussian-rational monomials (seeded), as controls only;
the closure itself is the kernel's (submonomial_mul, submonomial_block, submonomial_reindex,
submonomial_conjTranspose, submonomial_smul, submonomial_diagonal).
"""
import itertools
import random
import sys

import sympy as sp

I = sp.I
FAILS = []


def check(name, ok):
    print(('PASS ' if ok else 'FAIL ') + name)
    if not ok:
        FAILS.append(name)


def is_pow2(n):
    return n >= 1 and (n & (n - 1)) == 0


def is_monomial(M):
    """at most one nonzero entry in every row and every column (IsSubmonomial; = IsMonomial by
    monomial_iff_submonomial, StructuralClosure.lean:169)"""
    n = M.shape[0]
    for i in range(n):
        if sum(1 for j in range(n) if sp.simplify(M[i, j]) != 0) > 1:
            return False
    for j in range(n):
        if sum(1 for i in range(n) if sp.simplify(M[i, j]) != 0) > 1:
            return False
    return True


def exact_zero(M):
    return all(sp.simplify(sp.expand_complex(sp.expand(v))) == 0 for v in M)


def kron(A, B):
    return sp.Matrix(sp.kronecker_product(A, B))


def rand_monomial(n, rng):
    perm = list(range(n))
    rng.shuffle(perm)
    M = sp.zeros(n, n)
    for j in range(n):
        if rng.random() < 0.85:
            M[perm[j], j] = sp.Rational(rng.randint(-5, 5), rng.randint(1, 4)) + I * sp.Rational(rng.randint(-5, 5), rng.randint(1, 4))
    return M


def anc_block(K, n_sys, m, f, e):
    """ancBlock K f e on S x Fin m, row index (s, j) -> s*m + j"""
    return sp.Matrix(n_sys, n_sys, lambda s, t: K[s * m + f, t * m + e])


def main():
    rng = random.Random(20261008)
    # (K2) and the arithmetic lemma
    ok = True
    for nS in range(0, 65):
        for m in range(1, 65):
            if is_pow2(nS * m) and not is_pow2(nS):
                ok = False
    check('ARCH arithmetic lemma: card S * m = 2^j with m >= 1 forces card S = 2^i (exhaustive, card S, m <= 64)', ok)

    # monomial closure spot checks (controls; the closure is kernel-proved)
    ok = True
    for _ in range(40):
        n = rng.randint(1, 6)
        A, B = rand_monomial(n, rng), rand_monomial(n, rng)
        ok &= is_monomial(A * B) and is_monomial(A.H) and is_monomial(sp.Rational(1, 3) * A)
        perm = list(range(n))
        rng.shuffle(perm)
        P = sp.Matrix(n, n, lambda i, j: 1 if perm[j] == i else 0)
        ok &= is_monomial(P * A * P.T)
    for _ in range(20):
        nS, m = rng.randint(1, 3), rng.randint(1, 3)
        K = rand_monomial(nS * m, rng)
        ok &= all(is_monomial(anc_block(K, nS, m, f, e)) for f in range(m) for e in range(m))
    check('ARCH/LABEL/DAGGER control: products, adjoints, scalings, relabellings and ancilla blocks of exact random monomials are monomial', ok)

    # the witness operator: flow (transition 0 1) (pi/4) = [[cos, -i sin], [-i sin, cos]] at pi/4
    h = sp.sqrt(2) / 2
    rot = sp.Matrix([[h, -I * h], [-I * h, h]])
    X = sp.Matrix([[0, 1], [1, 0]])
    check('witness is flow (transition 0 1) (pi/4) exactly (sympy matrix exponential)',
          exact_zero((-I * sp.pi / 4 * X).exp() - rot))
    check('K2: the witness is admissible at Fin 2 (power-of-2 carrier: every operator admissible)', is_pow2(2))
    ctx = kron(sp.eye(3), rot)       # tensorOf 1_{Fin 3} K on Fin 3 x Fin 2, index (r, j) -> 2r + j
    check('NOT-CTX: 1_3 (x) K on the 6-element carrier is not monomial, and 6 is not a power of 2',
          (not is_monomial(ctx)) and not is_pow2(6))
    rot3 = sp.eye(3)
    rot3[0:2, 0:2] = rot
    T3 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    check('flow (transition 0 1) (pi/4) on Fin 3 equals exp(-i pi/4 (E01 + E10)) exactly',
          exact_zero((-I * sp.pi / 4 * T3).exp() - rot3))
    check('NOT-DRIVE: flow (transition 0 1) (pi/4) on Fin 3 is not monomial; 3 is not a power of 2',
          (not is_monomial(rot3)) and not is_pow2(3))

    # NOT-QM2: carriers reachable from the level-3 carrier of the qubit theory by discard have size 6m
    ok = all(not is_pow2(6 * m) for m in range(1, 200))
    check('NOT-QM2: every carrier Fin 2 x Fin 3 x Fin m (m >= 1, checked m < 200) has size divisible by 3, never a power of 2', ok)
    lvl3 = kron(rot, sp.eye(3))      # rot on the system, identity on the 3-level ancilla (a composite unitary)
    check('NOT-QM2: rot (x) 1_3 is unitary and not monomial',
          sp.simplify(lvl3.H * lvl3 - sp.eye(6)) == sp.zeros(6, 6) and not is_monomial(lvl3))
    D = sp.diag(*[sp.Rational(k + 1) for k in range(6)])
    out = sp.simplify(lvl3 * D * lvl3.H)
    check('NOT-QM2: conjugation by rot (x) 1_3 does not preserve the diagonal (exact witness)',
          any(sp.simplify(out[i, j]) != 0 for i in range(6) for j in range(6) if i != j))
    ok = True
    for _ in range(20):
        Mm = rand_monomial(6, rng)
        o = sp.expand(Mm * D * Mm.H)
        ok &= all(sp.simplify(o[i, j]) == 0 for i in range(6) for j in range(6) if i != j)
    check('NOT-QM2 control: monomial conjugations preserve the diagonal (exact random instances)', ok)

    # countercontrol: the lift of fa_lift.py, run on exactly the operator I_cm refuses (1_3 (x) rot),
    # extracts the Fin 3 flow at time pi/2; so the one failing closure is the one the lift consumes.
    def perm_mat(n, g):
        return sp.Matrix(n, n, lambda i, j: 1 if g[j] == i else 0)

    def idx(r, j):
        return 2 * r + j
    sig = list(range(6))
    sig[idx(0, 1)], sig[idx(1, 0)] = idx(1, 0), idx(0, 1)            # swap (a,1) <-> (b,0), a=0, b=1
    tau = list(range(6))
    tau[idx(0, 0)], tau[idx(0, 1)] = idx(0, 1), idx(0, 0)
    tau[idx(1, 0)], tau[idx(1, 1)] = idx(1, 1), idx(1, 0)
    Ps, Pt = perm_mat(6, sig), perm_mat(6, tau)
    M = Ps * kron(sp.eye(3), rot) * Ps.T                              # reindex sig sig (1_3 (x) rot)
    Dm = Pt * kron(sp.eye(3), sp.diag(-1, 1)) * Pt.T                  # reindex tau tau (1_3 (x) diag(-1,1))
    P = sp.expand(M * Dm * M * Dm)
    blk = anc_block(P, 3, 2, 0, 0)
    half = sp.Matrix([[0, -I, 0], [-I, 0, 0], [0, 0, 1]])             # flow (transition 0 1) (pi/2) on Fin 3
    check('countercontrol: the lift run on 1_3 (x) rot (the operator I_cm refuses) extracts flow (transition 0 1) (pi/2) on Fin 3',
          exact_zero(blk - half) and exact_zero(anc_block(P, 3, 2, 0, 1)) and not is_monomial(M))
    print()
    if FAILS:
        print('VERDICT  VOID — failed:', FAILS)
        sys.exit(1)
    print('VERDICT  I_cm: K2 holds at every power-of-2 carrier, Architecture/LabelInvariant/DaggerStable hold; '
          'ContextStable fails, DrivesElementary fails at Fin 3, and genTheory I_cm (Fin 2) has no level-3 control')


if __name__ == '__main__':
    main()
