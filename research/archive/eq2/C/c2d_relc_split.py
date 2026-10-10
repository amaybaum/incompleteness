"""EQ2-C, C2(d): relC <=> CI and TR (EQ-B T1/T2), checked against RelcSelectBlock's reading of relC.

Kernel reading (RSB at bcbc516f): the block reduction reads relC only at RSB:95 (gate_actC_ctrl), whose only use is
RSB:103 (gate_corner_neg_ctrl), i.e. the corner identity CI; the selector reads the full relC once more at RSB:746
(finrank_plus_eq_finrank_minus_relC, RSP:329). Definitions used here (this thread's own implementation):
  M0 = the corner map at z:  G(hom z (x) Y) = hom z (x) M0 Y          (corner_form, CD:1805: frame + posFwd)
  CI : G(hom(-z) (x) Y) = hom(-z) (x) homMap(N)(M0 Y) for every Y
  TR : relC restricted to the tangent control sector, inputs lift(t) (x) Y with t orthogonal to z
Claim (written, EQ-B T1): with IsNot (N orthogonal, N z = -z) and the corner form at z, relC <=> CI and TR, because
homMap(N) preserves the control sectors C = span(hom z, hom(-z)) and T = lift(z^perp), and relC on C (x) H is CI.

DECISION RULE (fixed before the first run). Verdict "RELC-SPLIT" prints only if, on all four instances,
relC == (CI and TR) and relC restricted to C (x) H == CI, and the four instances realize the four truth patterns:
  cnot (d = 3, nflip):              CI yes, TR yes, relC yes   (kernel CD:775, CD:860)
  gC5 (d = 5, nC5):                 CI yes, TR no,  relC no    (kernel RC5:179)
  C7b (d = 7, nK 3):                CI no,  TR no,  relC no    (c2a_c7b)
  cnot' (d = 3): cnot with the -z slice acting by homMap(sigma'), sigma' = diag(-1, 1, -1) (sigma' z = -z,
                 sigma' != nflip): CI no, TR yes, relC no; frame intact.
Exact (sympy rationals).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "vendor_bal"))
from c_common import Checks  # noqa: E402
from sympy import Matrix, eye, zeros, diag  # noqa: E402
from relt_common import (hom, homMap, apply, actT_mat, actC_mat, gate_from_fun, frame, relC as relC_full,  # noqa
                         dim1_cnot)
from bal_gates import jk_gate_general, cstruct, landed_gC5  # noqa: E402

C = Checks("c2d_relc_split")


def lift(t):
    return Matrix([0] + list(t))


def corner_map(G, z):
    n = z.shape[0] + 1
    hz = hom(z)
    cols = []
    for j in range(n):
        Y = zeros(n, 1)
        Y[j] = 1
        out = apply(G, hz * Y.T)
        if not (out - hz * out[0, :]).is_zero_matrix:
            return None                      # no corner form
        cols.append(out[0, :].T)
    return Matrix.hstack(*cols)


def CI(G, z, N):
    n = z.shape[0] + 1
    M0 = corner_map(G, z)
    hm = hom(-z)
    for j in range(n):
        Y = zeros(n, 1)
        Y[j] = 1
        if not (apply(G, hm * Y.T) - hm * (homMap(N) * M0 * Y).T).is_zero_matrix:
            return False
    return True


def tangent_basis(z):
    d = z.shape[0]
    # an orthogonal basis of z^perp (Gram-Schmidt on the standard basis, exact)
    basis = []
    for i in range(d):
        v = zeros(d, 1)
        v[i] = 1
        v = v - (z.T * v)[0, 0] * z
        for b in basis:
            v = v - ((b.T * v)[0, 0] / (b.T * b)[0, 0]) * b
        if not v.is_zero_matrix:
            basis.append(v)
    return basis


def rel_on(G, N, inputs):
    TC, TT = actC_mat(N), actT_mat(N)
    for w in inputs:
        if not (apply(TC * G * TC, w) - apply(TT * G, w)).is_zero_matrix:
            return False
    return True


def TR(G, z, N):
    n = z.shape[0] + 1
    ins = []
    for t in tangent_basis(z):
        for j in range(n):
            Y = zeros(n, 1)
            Y[j] = 1
            ins.append(lift(list(t)) * Y.T)
    return rel_on(G, N, ins)


def relC_on_C(G, z, N):
    n = z.shape[0] + 1
    ins = []
    for c in (hom(z), hom(-z)):
        for j in range(n):
            Y = zeros(n, 1)
            Y[j] = 1
            ins.append(c * Y.T)
    return rel_on(G, N, ins)


def sectors_preserved(z, N):
    """homMap N maps span(hom z, hom(-z)) and lift(z^perp) into themselves"""
    H = homMap(N)
    # direct test: H hom(z) = hom(N z) = hom(-z); H lift(t) = lift(N t) with N t orthogonal to z
    okC = (H * hom(z) - hom(-z)).is_zero_matrix and (H * hom(-z) - hom(z)).is_zero_matrix
    okT = all(((N * t).T * z)[0, 0] == 0 for t in tangent_basis(z))
    return okC and okT


cases = []
# cnot at d = 3
z3 = Matrix([0, 0, 1])
nflip = diag(1, -1, -1)
cases.append(("cnot (d=3, nflip)", dim1_cnot(), z3, nflip, (True, True, True)))
# gC5 at d = 5
z5 = Matrix([0, 0, 0, 0, 1])
nC5 = diag(1, -1, -1, -1, -1)
cases.append(("gC5 (d=5, nC5)", landed_gC5(), z5, nC5, (True, False, False)))
# C7b at d = 7
z7 = Matrix([0, 0, 0, 0, 0, 0, 1])
N7 = diag(1, 1, 1, -1, -1, -1, -1)
G7 = jk_gate_general(7, 1, cstruct(8, [(1, 2), (3, 4), (5, 6)]), cstruct(8, [(2, 3), (4, 5), (6, 7)]))["G"]
cases.append(("C7b (d=7, nK 3)", G7, z7, N7, (False, False, False)))
# cnot': cnot with the -z slice acting by homMap(sigma')
Gc = dim1_cnot()
sig = diag(-1, 1, -1)
hz3, hm3 = hom(z3), hom(-z3)


def cnot_prime(w):
    # decompose the control index: w = hz (x) a + hm (x) b + sum_t lift(t) (x) c_t  (rows), linear in w
    a = (w[0, :] + w[3, :]) / 2                  # coefficient row of hom z  (hom z = e0 + e3)
    b = (w[0, :] - w[3, :]) / 2                  # coefficient row of hom(-z)
    rest = w - hz3 * a - hm3 * b                 # tangent rows 1, 2
    out = apply(Gc, hz3 * a + rest)              # cnot on hom z (x) H and on T (x) H
    out = out + hm3 * (homMap(sig) * b.T).T      # the modified -z slice
    return out


Gp = gate_from_fun(cnot_prime, 4)
cases.append(("cnot' (d=3, -z slice by sigma')", Gp, z3, nflip, (False, True, False)))
C.check("S.0 cnot' keeps the frame (sigma' maps +-z to -+z) and agrees with cnot on hom z (x) H and on T (x) H",
        frame(Gp, z3) and all((apply(Gp, c * Matrix([[1 if k == j else 0 for k in range(4)]])) -
                               apply(Gc, c * Matrix([[1 if k == j else 0 for k in range(4)]]))).is_zero_matrix
                              for c in (hz3, lift([1, 0, 0]), lift([0, 1, 0])) for j in range(4)))

for name, G, z, N, expect in cases:
    M0 = corner_map(G, z)
    ci, tr, rc = CI(G, z, N), TR(G, z, N), relC_full(G, N)
    rcC = relC_on_C(G, z, N)
    C.check(f"S.1 {name}: corner form at z (M0 exists), sectors preserved by homMap N", M0 is not None and
            sectors_preserved(z, N))
    C.check(f"S.2 {name}: CI = {ci}, TR = {tr}, relC = {rc}; expected {expect}; relC == (CI and TR); "
            f"relC on C (x) H = {rcC} == CI", (ci, tr, rc) == expect and rc == (ci and tr) and rcC == ci)

sys.exit(C.finish("RELC-SPLIT: on four instances realizing all four truth patterns, relC holds exactly when CI and TR "
                  "both hold, and relC on the classical control sector is CI (EQ-B T1 confirmed against the kernel "
                  "reading RSB:95/:103/:746)"))
