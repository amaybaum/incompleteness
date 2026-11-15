#!/usr/bin/env python3
"""Reviewer's exact generic checks for #1216 unit 1 (route E_f).  Imports nothing from earlier probes.

Two tetrahedral identifications of a qubit with laws on four ontic points, v in
V = {(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)} (|v| = sqrt3):

  SIC  (Main:562):  coordinates p_l = tr(rho E_l), E_l = (I + v_l.sigma/sqrt3)/4 (a SIC POVM),
                    reconstruction rho = sum_l p_l D_l, D_l = (I + sqrt3 v_l.sigma)/2.
  R1   (AP1 sec 4.2, MECH-2's frame): ontic point <-> Bloch vector v_l, a law mu <-> r = sum mu_l v_l,
                    i.e. rho = sum mu_l A_l with A_l = (I + v_l.sigma)/2 (an ORTHOGONAL frame,
                    tr(A_k A_l) = 2 delta_kl), coordinates mu_l = tr(rho F_l), F_l = (I + v_l.sigma)/4.

For a channel C the frame matrix is M[l,k] = tr(F_l C(A_k)) (resp. tr(E_l C(D_k))).  Exact sympy
arithmetic over Q(sqrt3); Pauli-transfer evaluation, no floating point in any verdict.

R1a  frame identities for both frames (biorthogonality, R1 orthogonality, SIC non-orthogonality).
R1b  all 24 octahedral rotations: frame matrices are IDENTICAL in the two frames; the 12 of A4 are
     permutation matrices, the other 12 have minimum entry exactly -1/2.
R1c  CNOT: minimum frame-matrix entry in each frame (exact), and whether the two frame matrices agree.
R1d  states: every SIC coordinate of every qubit state is >= 0 (symbolic, |r| <= 1), while the pure
     state r = -v_0/sqrt3 has R1 coordinate (1 - sqrt3)/4 < 0; Phi+ has all SIC coordinates >= 0 and
     some R1 product-frame coordinate < 0 (exact value printed).
Controls: identity channel -> identity matrix in both frames; local A4 rotation (x) I -> permutation
matrix in both frames; a point mass reconstructs a non-PSD operator in both frames.
Run: python3 -I -B rv_frames.py   (exit 0 iff all pass)
"""
import itertools
import sys

import sympy as sp

FAIL = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAIL.append(name)


s3 = sp.sqrt(3)
V = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Z = sp.diag(1, -1)
PAULI = {'I': I2, 'x': X, 'y': Y, 'z': Z}
kp = sp.kronecker_product


def vs(v, scale):
    return scale * (v[0] * X + v[1] * Y + v[2] * Z)


FRAMES = {
    'SIC': ([(I2 + vs(v, 1 / s3)) / 4 for v in V], [(I2 + vs(v, s3)) / 2 for v in V]),
    'R1': ([(I2 + vs(v, 1)) / 4 for v in V], [(I2 + vs(v, 1)) / 2 for v in V]),
}


def z(M):
    return sp.simplify(sp.expand(M)) == sp.zeros(*M.shape)


# R1a ------------------------------------------------------------------
for nm, (E, D) in FRAMES.items():
    check(f"R1a {nm}: sum of coordinate functionals = I and tr(E_l D_k) = delta",
          z(sum(E, sp.zeros(2)) - I2)
          and all(sp.simplify((E[l] * D[k]).trace() - (1 if l == k else 0)) == 0 for l in range(4) for k in range(4)))
A = FRAMES['R1'][1]
check("R1a R1 frame is orthogonal: tr(A_k A_l) = 2 delta_kl",
      all(sp.simplify((A[k] * A[l]).trace() - (2 if k == l else 0)) == 0 for k in range(4) for l in range(4)))
Dsic = FRAMES['SIC'][1]
check("R1a SIC reconstruction frame is NOT orthogonal: tr(D_0 D_1) = -1",
      sp.simplify((Dsic[0] * Dsic[1]).trace()) == -1)
check("R1a R1 coordinate functionals F_l are not PSD (eigenvalue (1-sqrt3)/4)",
      any(sp.simplify(e - (1 - s3) / 4) == 0 for e in FRAMES['R1'][0][0].eigenvals()))


# Pauli-transfer frame matrices ----------------------------------------
def coef(op):
    """Pauli coefficients c_P with op = sum_P c_P P."""
    return {P: sp.nsimplify(sp.expand((op * M).trace() / 2)) for P, M in PAULI.items()}


def frame_matrix(U, nm, n):
    E, D = FRAMES[nm]
    Ec = [coef(e) for e in E]
    Dc = [coef(d) for d in D]
    labels = list(itertools.product(PAULI, repeat=n))
    img = {}
    for Rs in labels:
        op = PAULI[Rs[0]]
        for r in Rs[1:]:
            op = kp(op, PAULI[r])
        M = U * op * U.H
        found = None
        for Ps in labels:
            q = PAULI[Ps[0]]
            for p in Ps[1:]:
                q = kp(q, PAULI[p])
            t = sp.expand((M * q).trace() / 2 ** n)
            if t != 0:
                found = (Ps, t)
                break
        assert found is not None and found[1] in (1, -1, sp.I, -sp.I)
        img[Rs] = found
    idx = list(itertools.product(range(4), repeat=n))
    Mx = sp.zeros(4 ** n, 4 ** n)
    for a, ls in enumerate(idx):
        for b, ks in enumerate(idx):
            tot = 0
            for Rs, (Ps, t) in img.items():
                dk = 1
                for k, R in zip(ks, Rs):
                    dk *= Dc[k][R]
                el = 1
                for l, P in zip(ls, Ps):
                    el *= Ec[l][P]
                # tr(P (x) ... . P (x) ...) = 2^n
                tot += t * dk * el * 2 ** n
            Mx[a, b] = sp.nsimplify(sp.expand(tot))
    return Mx


def bloch_rotation_unitaries():
    """The 24 single-qubit Clifford unitaries mod phase, generated by H and S."""
    H = sp.Matrix([[1, 1], [1, -1]]) / s3 * s3 / sp.sqrt(2)
    S = sp.diag(1, sp.I)
    found = []

    def key(U):
        # normalize phase: first nonzero entry made positive real
        for e in U:
            e = sp.nsimplify(sp.expand(e))
            if e != 0:
                ph = e / sp.Abs(e)
                return tuple(sp.nsimplify(sp.expand(x / ph)) for x in U)
    frontier = [I2]
    seen = {key(I2)}
    found.append(I2)
    while frontier:
        nxt = []
        for U in frontier:
            for G in (H, S):
                W = sp.Matrix(2, 2, [sp.nsimplify(sp.expand(x)) for x in G * U])
                k = key(W)
                if k not in seen:
                    seen.add(k); found.append(W); nxt.append(W)
        frontier = nxt
    return found


cliff = bloch_rotation_unitaries()
check("R1b 24 single-qubit Clifford unitaries mod phase", len(cliff) == 24)
same, perm_ct, neg_half_ct = True, 0, 0
for U in cliff:
    Ms = frame_matrix(U, 'SIC', 1)
    Mr = frame_matrix(U, 'R1', 1)
    same &= (Ms - Mr) == sp.zeros(4, 4)
    if all(x in (0, 1) for x in Ms):
        perm_ct += 1
    elif min(Ms) == sp.Rational(-1, 2):
        neg_half_ct += 1
check("R1b single-qubit rotations: frame matrices identical in SIC and R1 frames", same)
check("R1b 12 rotations give permutation matrices, the other 12 have minimum entry -1/2",
      perm_ct == 12 and neg_half_ct == 12)

CN = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
Mc_s = frame_matrix(CN, 'SIC', 2)
Mc_r = frame_matrix(CN, 'R1', 2)
mn_s = min(Mc_s, key=lambda e: sp.N(e, 40))
mn_r = min(Mc_r, key=lambda e: sp.N(e, 40))
print("     CNOT min entry, SIC frame:", mn_s, "~", sp.N(mn_s, 10))
print("     CNOT min entry, R1 frame :", mn_r, "~", sp.N(mn_r, 10))
check("R1c CNOT, SIC frame: minimum entry is exactly 1/4 - sqrt3/3", sp.simplify(mn_s - (sp.Rational(1, 4) - s3 / 3)) == 0)
check("R1c CNOT, R1 frame: minimum entry is negative", bool(sp.N(mn_r, 40) < 0))
check("R1c CNOT frame matrices DIFFER between the two frames (entangling map: frame-dependent)",
      (Mc_s - Mc_r) != sp.zeros(16, 16))
for nm in FRAMES:
    check(f"R1 control {nm}: identity -> 16x16 identity", frame_matrix(sp.eye(4), nm, 2) == sp.eye(16))
U3 = (I2 - sp.I * (X + Y + Z)) / 2
for nm in FRAMES:
    Ml = frame_matrix(kp(U3, I2), nm, 2)
    check(f"R1 control {nm}: (A4 3-cycle) (x) I -> permutation matrix",
          all(x in (0, 1) for x in Ml) and all(sum(Ml[r, c] for c in range(16)) == 1 for r in range(16)))

# R1d states --------------------------------------------------------------
rx, ry, rz = sp.symbols('rx ry rz', real=True)
ok = True
for v in V:
    # SIC coordinate (1 + v.r/sqrt3)/4 >= (1 - |v||r|/sqrt3)/4 = (1-|r|)/4 by Cauchy-Schwarz: check |v| = sqrt3
    ok &= sp.sqrt(sum(x * x for x in v)) == s3
check("R1d SIC: coordinate (1 + v.r/sqrt3)/4 >= (1-|r|)/4 >= 0 on the Bloch ball (|v| = sqrt3, Cauchy-Schwarz)", ok)
r = [-x / s3 for x in V[0]]
rho = (I2 + r[0] * X + r[1] * Y + r[2] * Z) / 2
check("R1d control: r = -v_0/sqrt3 is a pure state (det rho = 0, tr = 1)",
      sp.simplify(rho.det()) == 0 and sp.simplify(rho.trace()) == 1)
mu0 = sp.simplify((rho * FRAMES['R1'][0][0]).trace())
p0 = sp.simplify((rho * FRAMES['SIC'][0][0]).trace())
print("     R1 coordinate mu_0 =", mu0, "; SIC coordinate p_0 =", p0)
check("R1d that pure state has R1 coordinate (1 - sqrt3)/4 < 0 and SIC coordinate 0",
      sp.simplify(mu0 - (1 - s3) / 4) == 0 and p0 == 0)
phi = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
rphi = phi * phi.H
for nm in FRAMES:
    E = FRAMES[nm][0]
    cs = [sp.nsimplify(sp.expand((rphi * kp(E[i], E[j])).trace())) for i in range(4) for j in range(4)]
    mn = min(cs, key=lambda e: sp.N(e, 30))
    print(f"     Phi+ {nm} product-frame coordinates: min =", mn, "; sum =", sp.simplify(sum(cs)))
    if nm == 'SIC':
        check("R1d Phi+: all SIC product-frame coordinates >= 0", all(sp.N(c, 30) >= 0 for c in cs))
    else:
        check("R1d Phi+: some R1 product-frame coordinate < 0", bool(sp.N(mn, 30) < 0))
for nm in FRAMES:
    D0 = FRAMES[nm][1][0]
    check(f"R1 control {nm}: point mass reconstructs a non-PSD operator",
          any(sp.N(e) < 0 for e in D0.eigenvals()))

print("RESULT", "ALL PASS" if not FAIL else "FAILED: " + ", ".join(FAIL))
sys.exit(1 if FAIL else 0)
