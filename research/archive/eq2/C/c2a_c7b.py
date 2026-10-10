"""EQ2-C, C2(a): C7b at d = 7 as a Lean-ready signed-permutation gate.

Construction rule (BAL LEDGER B1, written independently here as tables): homogeneous indices 0 (unit), 1..6 tangent,
7 = z.  u0 = e_1 (homogeneous 1), sigma = 2 u0 u0^T - I, J pairs (1,2),(3,4),(5,6), K pairs (2,3),(4,5),(6,7):
  G(e_0 (x) e_v) = e_0 (x) e_v (v <= 1),  e_7 (x) e_v (v >= 2);   G(e_7 (x) e_v) = e_7 (x) e_v (v <= 1),  e_0 (x) e_v;
  G(e_m (x) e_v) = e_m (x) e_(1-v) (v <= 1),   (J e_m) (x) (K e_v) (v >= 2),   m = 1..6.
The NOT is the landed OddChar.nK 3 (signs + on homogeneous 0..3, - on 4..7) with axis OddChar.zK 3 = e_7.

DECISION RULE (fixed before the first run). Verdict "C7B-LEAN-READY" prints only if all pass:
  T0 controls: the same table rule with gC5's data (d = 5, J (1,2),(3,4), K (2,5),(3,4)) reproduces the landed
     RelcSelectC5 tables sgnC5/pcC5/ptC5 entry for entry; the rule's C7b equals BAL's builder (vendored verbatim,
     sha256 recorded in NOTES) as a 64 x 64 matrix.
  T1 nK 3 recomputed from OddChar's definitions (oddK 3 mu = decide (3 < mu)) is diag(1,1,1,-1,-1,-1,-1); IsNot holds
     with zK 3; homogenized eigenspaces (4, 4): balanced (kernel: finrank_plus_eq_finrank_minus_nK, OC:176).
  T2 frame, relT with nK 3, G^2 = I (so G^-1 = G).
  T3 relC fails (explicit entry), the corner identity CI fails (explicit Y), the tangent relation TR fails.
  T4 the value identity for prodEffVal e f (G (prodState x y)) (the Lean statement, symbolic), BAL's six
     certificate identities I1-I6, and the tight witness (value 0) with the 2J countercontrol (value -1).
  T5 countercontrol on the tables: flipping one sign breaks G^2 = I or relT.
Exact (sympy rationals / polynomials).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "vendor_bal"))
from c_common import Checks  # noqa: E402
from sympy import Matrix, Rational as R, eye, zeros, diag, symbols, expand  # noqa: E402
from relt_common import (hom, homMap, apply, prod, isNot, frame, relT, relC, eig_dims, pairVal, actT_mat,  # noqa
                         actC_mat, gate_from_fun)
from bal_gates import cstruct, jk_gate_general, certificate_identities, landed_gC5, entW  # noqa: E402

C = Checks("c2a_c7b")


def table_rule(d, Jpairs, Kpairs):
    """signed-permutation tables (pc, pt, sgn) of the J/K gate with u0 = e_1, from the construction rule."""
    n = d + 1
    Jm, Js, Km, Ks = {}, {}, {}, {}
    for i, j in Jpairs:
        Jm[i], Js[i], Jm[j], Js[j] = j, 1, i, -1
    for i, j in Kpairs:
        Km[i], Ks[i], Km[j], Ks[j] = j, 1, i, -1
    pc = [[0] * n for _ in range(n)]
    pt = [[0] * n for _ in range(n)]
    sg = [[1] * n for _ in range(n)]
    for m in range(n):
        for v in range(n):
            if m == 0:
                pc[m][v], pt[m][v] = (0 if v <= 1 else d), v
            elif m == d:
                pc[m][v], pt[m][v] = (d if v <= 1 else 0), v
            elif v <= 1:
                pc[m][v], pt[m][v] = m, 1 - v
            else:
                pc[m][v], pt[m][v] = Jm[m], Km[v]
                sg[m][v] = Js[m] * Ks[v]
    return pc, pt, sg


def gate_of_tables(pc, pt, sg):
    n = len(pc)
    def f(w):
        return Matrix(n, n, lambda m, v: sg[m][v] * w[pc[m][v], pt[m][v]])
    return gate_from_fun(f, n)


# ----------------------------------------------------------------------------- T0 controls

print("== T0 controls: the table rule reproduces the landed gC5 and BAL's C7b")
pc5, pt5, sg5 = table_rule(5, [(1, 2), (3, 4)], [(2, 5), (3, 4)])
k_pc5 = [[0, 0, 5, 5, 5, 5], [1, 1, 2, 2, 2, 2], [2, 2, 1, 1, 1, 1], [3, 3, 4, 4, 4, 4], [4, 4, 3, 3, 3, 3],
         [5, 5, 0, 0, 0, 0]]
k_pt5 = [[0, 1, 2, 3, 4, 5], [1, 0, 5, 4, 3, 2], [1, 0, 5, 4, 3, 2], [1, 0, 5, 4, 3, 2], [1, 0, 5, 4, 3, 2],
         [0, 1, 2, 3, 4, 5]]
k_sg5 = [[-1 if ((m in (1, 3)) and (v in (4, 5))) or ((m in (2, 4)) and (v in (2, 3))) else 1 for v in range(6)]
         for m in range(6)]
C.check("T0.1 the table rule at d = 5 with gC5's J, K equals the landed RelcSelectC5 tables (sgnC5 RC5:89, pcC5 RC5:94, ptC5 RC5:104) entry for "
        "entry (pcC5, ptC5, sgnC5)", pc5 == k_pc5 and pt5 == k_pt5 and sg5 == k_sg5)
C.check("T0.2 ... and as a 36 x 36 matrix equals BAL's transcription of the landed gC5",
        (gate_of_tables(pc5, pt5, sg5) - landed_gC5()).is_zero_matrix)
pc7, pt7, sg7 = table_rule(7, [(1, 2), (3, 4), (5, 6)], [(2, 3), (4, 5), (6, 7)])
G7 = gate_of_tables(pc7, pt7, sg7)
J7, K7 = cstruct(8, [(1, 2), (3, 4), (5, 6)]), cstruct(8, [(2, 3), (4, 5), (6, 7)])
bal = jk_gate_general(7, 1, J7, K7)
C.check("T0.3 the C7b tables equal BAL's builder C7b as a 64 x 64 matrix", (G7 - bal["G"]).is_zero_matrix)

# ----------------------------------------------------------------------------- T1 the NOT

print("== T1 the NOT nK 3 from OddChar's definitions")
oddK3 = lambda mu: 3 < mu  # noqa: E731   OddChar.oddK k mu = decide (k < mu)
cK3 = [(-1 if oddK3(j + 1) else 1) for j in range(7)]
N7 = diag(*cK3)
z7 = Matrix([0, 0, 0, 0, 0, 0, 1])     # zK 3 = indicator of coordinate 2k = 6
C.check(f"T1.1 nK 3 = diagSign(cK 3) = diag{tuple(cK3)} and zK 3 = e_7", cK3 == [1, 1, 1, -1, -1, -1, -1])
C.check("T1.2 IsNot (eball 7) (zK 3) (nK 3): unit axis, involution, orthogonal (so ball-preserving), flips z",
        all(isNot(z7, N7).values()))
C.check(f"T1.3 homogenized eigenspaces {eig_dims(N7)}: balanced, as the kernel's finrank_plus_eq_finrank_minus_nK 3",
        eig_dims(N7) == (4, 4))

# ----------------------------------------------------------------------------- T2 frame, relT, involution

print("== T2 frame, relT, involution")
C.check("T2.1 frame on the corners +-zK 3", frame(G7, z7))
C.check("T2.2 relT with nK 3", relT(G7, N7))
C.check("T2.3 G^2 = I (pc, pt an involution of index pairs, sgn(m,v) sgn(pc,pt) = 1)",
        (G7 * G7 - eye(64)).is_zero_matrix and
        all(pc7[pc7[m][v]][pt7[m][v]] == m and pt7[pc7[m][v]][pt7[m][v]] == v and
            sg7[m][v] * sg7[pc7[m][v]][pt7[m][v]] == 1 for m in range(8) for v in range(8)))

# ----------------------------------------------------------------------------- T3 relC, CI and TR fail

print("== T3 the control relation and its two halves fail")
TC, TT = actC_mat(N7), actT_mat(N7)
E02 = entW(8, 0, 2)
lhs = apply(TC * G7 * TC, E02)[7, 2]
rhs = apply(TT * G7, E02)[7, 2]
C.check(f"T3.1 relC fails at entW 0 2, entry (7,2): actC side {lhs}, actT side {rhs}",
        lhs == -1 and rhs == 1 and not relC(G7, N7))
hz, hmz = hom(z7), hom(-z7)
M0cols = []
for j in range(8):
    Y = zeros(8, 1)
    Y[j] = 1
    out = apply(G7, hz * Y.T)
    M0cols.append(out[0, :].T)
M0 = Matrix.hstack(*M0cols)
Y2 = zeros(8, 1)
Y2[2] = 1
ci_lhs = apply(G7, hmz * Y2.T)
ci_rhs = hmz * (homMap(N7) * M0 * Y2).T
C.check("T3.2 the corner identity G(hom(-z) (x) Y) = hom(-z) (x) homMap(nK 3)(M0 Y) fails at Y = e_2 (M0 = I; G acts "
        "there by homMap(sigma), sigma != nK 3): the two sides differ by sign",
        M0 == eye(8) and (ci_lhs + ci_rhs).is_zero_matrix and not ci_lhs.is_zero_matrix)
tr_fail = None
for t in range(1, 7):
    for v in range(8):
        w = zeros(8, 8)
        w[t, v] = 1
        a = apply(TC * G7 * TC, w)
        b = apply(TT * G7, w)
        if not (a - b).is_zero_matrix:
            tr_fail = (t, v)
            break
    if tr_fail:
        break
C.check(f"T3.3 the tangent relation TR (relC on lift(z^perp) (x) H) fails, first at the tangent input entW {tr_fail}",
        tr_fail is not None)

# ----------------------------------------------------------------------------- T4 positivity: the Lean value identity

print("== T4 positivity: the value identity (Lean statement) and BAL's certificate identities")
xs = symbols("x0:7")
ys = symbols("y0:7")
es = symbols("e0:8")
fs = symbols("f0:8")
val = pairVal(Matrix(es), Matrix(fs), apply(G7, hom(list(xs)) * hom(list(ys)).T))
E, F, x, y = es, fs, xs, ys
claimed = ((E[0] + x[6] * E[7]) * (F[0] + F[1] * y[0])
           + (E[7] + x[6] * E[0]) * (F[2] * y[1] + F[3] * y[2] + F[4] * y[3] + F[5] * y[4] + F[6] * y[5] + F[7] * y[6])
           + (E[1] * x[0] + E[2] * x[1] + E[3] * x[2] + E[4] * x[3] + E[5] * x[4] + E[6] * x[5]) * (F[0] * y[0] + F[1])
           + (E[2] * x[0] - E[1] * x[1] + E[4] * x[2] - E[3] * x[3] + E[6] * x[4] - E[5] * x[5])
           * (F[3] * y[1] - F[2] * y[2] + F[5] * y[3] - F[4] * y[4] + F[7] * y[5] - F[6] * y[6]))
C.check("T4.1 prodEffVal_gC7b_prodState (symbolic in x, y in R^7 and the homogenized effect vectors e, f): "
        "(e0 + x6 e7)(f0 + f1 y0) + (e7 + x6 e0)(f2 y1 + ... + f7 y6) + (e1 x0 + ... + e6 x5)(f0 y0 + f1) "
        "+ (e2 x0 - e1 x1 + e4 x2 - e3 x3 + e6 x4 - e5 x5)(f3 y1 - f2 y2 + f5 y3 - f4 y4 + f7 y5 - f6 y6)",
        expand(val - claimed) == 0)
ids = certificate_identities(bal)
C.check(f"T4.2 BAL's certificate identities I1-I6 and the orthogonal complex structures hold at d = 7 "
        f"({sum(ids.values())}/{len(ids)})", all(ids.values()))
xw = Matrix([1, 0, 0, 0, 0, 0, 0])
yw = Matrix([0, 1, 0, 0, 0, 0, 0])
ew = Matrix([1, 0, -1, 0, 0, 0, 0, 0])
fw = Matrix([1, 0, 0, 1, 0, 0, 0, 0])
g2J = jk_gate_general(7, 1, 2 * J7, K7)
v0 = pairVal(ew, fw, apply(G7, prod(xw, yw)))
v2 = pairVal(ew, fw, apply(g2J["G"], prod(xw, yw)))
C.check(f"T4.3 tightness and countercontrol: at the witness (x = e1, y = e2, e = (1, -J e1), f = (1, K e2)) C7b's "
        f"value is {v0} and the 2J variant's (frame and relT intact) is {v2}",
        v0 == 0 and v2 == -1 and frame(g2J["G"], z7) and relT(g2J["G"], N7))

# ----------------------------------------------------------------------------- T5 table countercontrol

print("== T5 countercontrol on the tables")
broken = 0
for (m, v) in [(1, 3), (2, 2), (0, 5), (6, 7)]:
    sgb = [row[:] for row in sg7]
    sgb[m][v] = -sgb[m][v]
    Gb = gate_of_tables(pc7, pt7, sgb)
    if not ((Gb * Gb - eye(64)).is_zero_matrix and relT(Gb, N7)):
        broken += 1
C.check(f"T5.1 flipping any one of four sampled signs breaks G^2 = I or relT ({broken}/4)", broken == 4)

# ----------------------------------------------------------------------------- the Lean tables, printed

print("== Lean-ready tables (for the UNBUILT module; homogeneous indices 0..7)")
print("def pcC7b : Fin 8 -> Fin 8 -> Fin 8")
for m in range(8):
    print("  " + " ".join(f"| {m}, {v} => {pc7[m][v]}" for v in range(8)))
print("def ptC7b : Fin 8 -> Fin 8 -> Fin 8")
for m in range(8):
    print("  " + " ".join(f"| {m}, {v} => {pt7[m][v]}" for v in range(8)))
neg = sorted((m, v) for m in range(8) for v in range(8) if sg7[m][v] == -1)
print("sgnC7b mu nu = -1 exactly at " + ", ".join(f"({m},{v})" for m, v in neg))
C.check("T5.2 the sign pattern is -1 exactly on {1,3,5} x {3,5,7} and {2,4,6} x {2,4,6}",
        set(neg) == {(m, v) for m in (1, 3, 5) for v in (3, 5, 7)} | {(m, v) for m in (2, 4, 6) for v in (2, 4, 6)})

sys.exit(C.finish("C7B-LEAN-READY: C7b is the signed permutation (pcC7b, ptC7b, sgnC7b) of the 64 entries of W 7; with "
                  "the landed nK 3 / zK 3 it satisfies IsNot, balance (4,4), the frame, relT, G^2 = I and two-sided "
                  "positivity (value identity + I1-I6), and fails relC, CI and TR"))
