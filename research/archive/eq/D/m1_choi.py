#!/usr/bin/env python3
"""EQ-D, node N2 (GPT level): the countermodel M1.

M1 has the systems Q_n (carrier C^(2^n), every CP trace-non-increasing map: the hypothetical K2 repertoire) and, for
every k >= 3 not a power of 2, a system T_k with state space D_k and every effect.  Transformations of T_k (and
between distinct systems when one of them is a T): lambda*id (same system only) + Psi with Psi measure-and-prepare,
trace non-increasing.  The set is closed under composition because measure-and-prepare maps form a two-sided ideal:
  Phi o (sum_i tr(E_i .) s_i) = sum_i tr(E_i .) Phi(s_i),  (sum_i tr(E_i .) s_i) o Phi = sum_i tr(Phi^*(E_i) .) s_i.
FP-S and FP-E hold by construction (every frame-generated face of every system is a D_j, carried by Q or T_j with
every effect; one system per capacity).  M1 has no composites involving a T system.

Checked exactly here:
  (1) the swap channel conj(P01) on T_3 is NOT of the form lambda*id + measure-and-prepare:
      witness u = e0 (x) e0 forces lambda = 0, then the Choi matrix would have to be separable, but its partial
      transpose has eigenvalue -1 (Peres; a measure-and-prepare map sum_i tr(E_i .) s_i has Choi matrix
      sum_i E_i^T (x) s_i, manifestly separable, hence PPT).
  (2) FP-T fails in M1 at exactly this point: P01 (+) 1 on C^4 is a face-preserving unitary of Q_2 (available by
      K2), its restriction to the 3-face is conj(P01) (exact), and that map is not a transformation of T_3.
  Controls: id_T3 is in the set (lambda = 1) although its Choi matrix is also NPT (so the witness step is
  load-bearing); an explicit measure-and-prepare map is in the set and its Choi matrix is PPT; conj(X) on Q_1 is
  available (K2), so the obstruction is specific to the T systems.
"""
import sys

import sympy as sp

I = sp.I

FAILS = []


def check(name, ok):
    print(('PASS ' if ok else 'FAIL ') + name)
    if not ok:
        FAILS.append(name)


def ket(d, i):
    v = sp.zeros(d, 1)
    v[i] = 1
    return v


def choi(kraus, d):
    """J = sum_{ij} E_ij (x) Phi(E_ij) for Phi(X) = sum_k K X K^dagger (input factor first)."""
    J = sp.zeros(d * d, d * d)
    for i in range(d):
        for j in range(d):
            Eij = ket(d, i) * ket(d, j).T
            out = sp.zeros(d, d)
            for K in kraus:
                out += K * Eij * K.H
            J += sp.Matrix(sp.kronecker_product(Eij, out))
    return J


def partial_transpose_out(J, d):
    """transpose on the second (output) factor"""
    T = sp.zeros(d * d, d * d)
    for a in range(d):
        for b in range(d):
            for c in range(d):
                for e in range(d):
                    T[a * d + c, b * d + e] = J[a * d + e, b * d + c]
    return T


def main():
    d = 3
    P01 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    J_swap = choi([P01], d)
    J_id = choi([sp.eye(d)], d)
    u = sp.Matrix(sp.kronecker_product(ket(d, 0), ket(d, 0)))
    check('(1a) witness u = e0(x)e0: <u|J(conj P01)|u> = 0 and <u|J(id)|u> = 1',
          (u.T * J_swap * u)[0] == 0 and (u.T * J_id * u)[0] == 1)
    # J(conj P01) - lambda*J(id) is PSD only for lambda <= 0, by the witness; so lambda = 0
    lam = sp.symbols('lam', nonnegative=True)
    check('(1b) hence J(conj P01) - lam*J(id) has <u|.|u> = -lam, negative for every lam > 0',
          sp.simplify((u.T * (J_swap - lam * J_id) * u)[0] + lam) == 0)
    ev = partial_transpose_out(J_swap, d).eigenvals()
    check('(1c) the partial transpose of J(conj P01) has eigenvalue -1 (exact spectrum)', sp.Integer(-1) in ev)
    print('     spectrum of J(conj P01)^{T_out}:', dict(ev))
    # control: a measure-and-prepare map has PPT Choi matrix
    E = [sp.Matrix([[1, 0, 0], [0, 0, 0], [0, 0, 0]]), sp.Matrix([[0, 0, 0], [0, 1, 0], [0, 0, 1]])]
    S = [sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2), 0], [sp.Rational(1, 2), sp.Rational(1, 2), 0], [0, 0, 0]]),
         sp.Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 1]])]
    J_mp = sp.zeros(d * d, d * d)
    for Ei, Si in zip(E, S):
        J_mp += sp.Matrix(sp.kronecker_product(Ei.T, Si))
    ev_mp = partial_transpose_out(J_mp, d).eigenvals()
    check('control: a measure-and-prepare map has a PPT Choi matrix (all partial-transpose eigenvalues >= 0)',
          all(sp.re(k) >= 0 for k in ev_mp))
    ev_id = partial_transpose_out(J_id, d).eigenvals()
    check('control: J(id) is also NPT, so the witness step (lambda = 0) is load-bearing', sp.Integer(-1) in ev_id)
    # (2) FP-T fails: restriction of a face-preserving K2 unitary to the 3-face of Q_2
    U4 = sp.diag(P01, sp.Matrix([[1]]))
    iota = sp.Matrix.hstack(ket(4, 0), ket(4, 1), ket(4, 2))
    Pf = iota * iota.T
    check('(2a) U4 = P01 (+) 1 is unitary on C^4 and maps the 3-face into itself (U4 P U4^dag = P)',
          U4.H * U4 == sp.eye(4) and U4 * Pf * U4.H == Pf)
    rho = sp.Matrix(3, 3, lambda i, j: sp.Rational(1 + i + j, 7) if i == j else sp.Rational(1, 13) * (1 + i * j))
    restricted = iota.T * (U4 * (iota * rho * iota.T) * U4.H) * iota
    check('(2b) its restriction to the face is exactly conj(P01) on D_3 (generic exact test matrix)',
          sp.simplify(restricted - P01 * rho * P01.H) == sp.zeros(3, 3))
    X = sp.Matrix([[0, 1], [1, 0]])
    check('control: conj(X) on Q_1 is a K2 transformation (unitary, CP); the obstruction is specific to T systems',
          X.H * X == sp.eye(2))
    # (3) M1' : add to every T system all Lueders filters rho -> P rho P (every frame-generated face is then the image
    # of a physical filter, the Alfsen-Shultz compression reading) and close under composition and coarse-graining.
    # Every branch is then sum_l conj(Pi_l) + (measure-and-prepare), Pi_l a product of projections.  A deterministic
    # conj(U) forces every Kraus operator onto the ray of U (ray lemma, kraus_of_conj_unitary,
    # MicroscopicReversibility.lean:189); rank-one Kraus operators cannot lie on the ray of an invertible U, and a
    # product of projections on that ray is invertible, hence every factor is invertible, hence equal to 1.
    check('(3a) P01 is invertible (det = -1) and not a scalar multiple of 1', P01.det() == -1 and P01 != P01[0, 0] * sp.eye(3))
    import random as _r
    rng = _r.Random(3)
    ok = True
    for _ in range(30):
        # random rank-1 or rank-2 projector on C^3 from a Gaussian-rational unitary (Cayley transform)
        S = sp.zeros(3, 3)
        for i in range(3):
            S[i, i] = I * sp.Rational(rng.randint(-3, 3), rng.randint(1, 3))
            for j in range(i + 1, 3):
                zz = sp.Rational(rng.randint(-3, 3), rng.randint(1, 3)) + I * sp.Rational(rng.randint(-3, 3), rng.randint(1, 3))
                S[i, j], S[j, i] = zz, -sp.conjugate(zz)
        U = sp.simplify((sp.eye(3) - S) * (sp.eye(3) + S).inv())
        r = rng.randint(1, 2)
        Pr = sp.simplify(U[:, :r] * U[:, :r].H)
        ok &= sp.simplify(Pr * Pr - Pr) == sp.zeros(3, 3) and sp.simplify(Pr.det()) == 0
    check('(3b) control: proper projectors on C^3 (exact, random frames) are idempotent and singular, so any product '
          'containing one is singular and cannot be a nonzero multiple of P01', ok)
    print()
    if FAILS:
        print('VERDICT  VOID — failed:', FAILS)
        sys.exit(1)
    print('VERDICT  in M1 (K2 + FP-S + FP-E + sequential composition) the swap of the capacity-3 system is not a '
          'transformation; the restriction clause FP-T is exactly what fails')


if __name__ == '__main__':
    main()
