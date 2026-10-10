"""B1 (node N1, decisive) -- the native, field-neutral class of control gates at d = 3.

Question (B3(ii)). Does every linear G : W 3 -> W 3 with u o G = u (u = the (0,0) coordinate), IsNot (eball 3) z N and
CtrlGate (eball 3) z N G (frame, posFwd, posInv, relC; RelcSelectBlock.lean:45) reduce to the kernel cnot up to local
O(3) x O(3) maps?

Reduction used (written; landed lemmas cited in NOTES N1):
  * corner slices (landed gate_corner_ctrl RSB:60, gate_corner_neg_ctrl RSB:99): G (hom z (x) Y) = hom z (x) M0 Y and
    G (hom(-z) (x) Y) = hom(-z) (x) Ntilde M0 Y, M0 = Mfwd z G; with u o G = u, M0 = 1 (+) O, O orthogonal, O z = z;
  * parity (landed finrank_plus_eq_finrank_minus_relC, RelcSelectParity:329) makes N a pi-rotation about u0 _|_ z; a
    rotation conjugation moves (z, u0) to (z3, e_x), so N = nflip;
  * Gt := G o actT(M0)^-1 fixes hom z (x) Y and sends hom(-z) (x) Y to hom(-z) (x) Ntilde Y.
Unknowns here: the tangent block of Gt, Gt(lift t (x) e_l) for t in {e_x, e_y}, l = 0..3 (128 unknowns).
Constraint families:
  C1 relC (linear), C2 the tangent control output is orthogonal to both corners (landed gt_tangent_corners_ctrl RSB:129),
  C3 tightness at P = 0 (landed gt_sphere_ctrl RSB:162): pairVal a hom(-y) (Gt (lift c (x) hom y)) = 0, |y| = 1,
  C4 tightness at Q = 0 (the -z analogue, same proof through tangent_vanish CD:2051): pairVal a hom(-N y) (...) = 0.
Decision rule (fixed before the run):
  * the 4-parameter family F(a, a2, b1, b2) is reported as the solution space only if the exact rank upper bound equals
    4 and each basis direction satisfies C1-C4 symbolically for all unit y (stereographic parameters);
  * the +-1 restriction is reported only from exact symbolic test-point values under posFwd and posInv;
  * each admissible sign pattern is reported as l1 o cnot o l2 only by an exact matrix identity with explicit local
    O(3) x O(3) sign maps; each excluded pattern only with an exact negative witness;
  * controls: the parsed kernel cnot is F(1, 1, -1, 1); countercontrols: dropping C3 + C4 or C1 enlarges the solution
    space, and a member of the enlarged space violates posFwd at an exact point.
Usage: python3 -I -B b1_native_class.py <base>/verification/lean-mathlib/OIBridge/CompositeDimension.lean
"""
import sys
import os
import itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eq2b_lib import *  # noqa
import sympy as sp

rep = Report("B1 native control-gate class at d = 3")
CNOT, PC, PT, NEG = parse_kernel_cnot(sys.argv[1])
rep.note(f"parsed kernel cnot: sgn = -1 at {sorted(NEG)}")
NT = homMap(NFLIP)                       # Ntilde = diag(1, 1, -1, -1)
ACN, ATN = actC(NFLIP), actT(NFLIP)
hz, hmz = hom(Z3), hom([0, 0, -1])


def corner(a):
    return Z3 if a == 0 else [Fr(0), Fr(0), Fr(-1)]


def ctrl_frame(Gm, z=Z3):
    zz = [z, [-t for t in z]]
    return all(apply(Gm, prodState(zz[a], zz[b])) == prodState(zz[a], zz[(a + b) % 2]) for a in (0, 1) for b in (0, 1))


def relC(Gm, N=NFLIP):
    return meq(mmul(mmul(actC(N), Gm), actC(N)), mmul(actT(N), Gm))


def norm_pres(Gm):
    return Gm[0] == [Fr(1)] + [Fr(0)] * 15


# ---------------------------------------------------------------- Part A: controls on the parsed kernel cnot
rep.check("A.1 kernel cnot is an involution and preserves the normalization u = w00 (row 0 is e00)",
          meq(mmul(CNOT, CNOT), I16) and norm_pres(CNOT))
rep.check("A.2 kernel cnot satisfies the frame at z3 and relC with nflip (exact operator identities)",
          ctrl_frame(CNOT) and relC(CNOT))
rep.check("A.3 [M] kernel cnot = Ad(CNOT, control = copy A) in the Pauli dictionary", meq(CNOT, conj_map(CNOT_U)))
ok = True
for l in range(4):
    Y = [Fr(1) if k == l else Fr(0) for k in range(4)]
    ok &= apply(CNOT, tens(hz, Y)) == tens(hz, Y)
    ok &= apply(CNOT, tens(hmz, Y)) == tens(hmz, mvec(NT, Y))
rep.check("A.4 corner forms of cnot: hom z (x) Y fixed, hom(-z) (x) Y -> hom(-z) (x) Ntilde Y (M0 = I)", ok)

# ---------------------------------------------------------------- the family F(a, a2, b1, b2)
X4 = zeros(4, 4); X4[0][1] = X4[1][0] = Fr(1)                       # e0 <-> e_x, kills e_y, e_z
J4 = zeros(4, 4); J4[3][2] = Fr(1); J4[2][3] = Fr(-1)              # e_y -> e_z, e_z -> -e_y


def gate_from(tblock):
    """16x16 matrix of Gt: corner columns fixed by the corner forms (M0 = I), tangent columns from tblock[(ti, l)]."""
    M = zeros(16, 16)
    for l in range(4):
        Y = [Fr(1) if k == l else Fr(0) for k in range(4)]
        cz, cm_ = tens(hz, Y), tens(hmz, mvec(NT, Y))
        e0col = [(cz[m][n] + cm_[m][n]) / 2 for (m, n) in IDX]            # input e0 (x) e_l
        ezcol = [(cz[m][n] - cm_[m][n]) / 2 for (m, n) in IDX]            # input lift z (x) e_l
        for r in range(16):
            M[r][4 * 0 + l] = e0col[r]
            M[r][4 * 3 + l] = ezcol[r]
        for ti in (0, 1):
            col = tblock[(ti, l)]
            for r in range(16):
                M[r][4 * (ti + 1) + l] = col[r]
    return M


def family_block(a, a2, b1, b2):
    """Tangent block of F: Gt(lift e_x (x) Y) = a lift e_x (x) X Y + b2 lift e_y (x) J Y,
    Gt(lift e_y (x) Y) = b1 lift e_x (x) J Y + a2 lift e_y (x) X Y."""
    ex, ey = lift([1, 0, 0]), lift([0, 1, 0])
    tb = {}
    for l in range(4):
        Y = [Fr(1) if k == l else Fr(0) for k in range(4)]
        XY, JY = mvec(X4, Y), mvec(J4, Y)
        w1 = madd(tens(ex, XY), tens(ey, JY), a, b2)
        w2 = madd(tens(ex, JY), tens(ey, XY), b1, a2)
        tb[(0, l)] = vec(w1)
        tb[(1, l)] = vec(w2)
    return tb


def fam(a, a2, b1, b2):
    return gate_from(family_block(F(a), F(a2), F(b1), F(b2)))


rep.check("A.5 control: the parsed kernel cnot equals F(1, 1, -1, 1)", meq(fam(1, 1, -1, 1), CNOT))

# ---------------------------------------------------------------- Part B: the linear classification
NU = 128


def uidx(ti, l, o):
    return (ti * 4 + l) * 16 + o


def rows_C1():
    rows = []
    for ti in (0, 1):
        kap = ti + 1
        A = madd(mscale(ACN, NT[kap][kap]), ATN, 1, -1)
        for l in range(4):
            for r in range(16):
                row = [Fr(0)] * NU
                for o in range(16):
                    if A[r][o] != 0:
                        row[uidx(ti, l, o)] = A[r][o]
                rows.append(row)
    return rows


def rows_C2():
    rows = []
    for ti in (0, 1):
        for l in range(4):
            for nu in range(4):
                for mu in (0, 3):
                    row = [Fr(0)] * NU
                    row[uidx(ti, l, 4 * mu + nu)] = Fr(1)
                    rows.append(row)
    return rows


def rows_tight(y, b):
    """For the unit target y and functional b (hom(-y) or hom(-N y)): for each control tangent t and each mu,
    sum_nu (sum_l hom(y)_l col_{t,l})[mu][nu] b_nu = 0."""
    hy = hom(y)
    rows = []
    for ti in (0, 1):
        for mu in range(4):
            row = [Fr(0)] * NU
            for l in range(4):
                if hy[l] == 0:
                    continue
                for nu in range(4):
                    if b[nu] != 0:
                        row[uidx(ti, l, 4 * mu + nu)] += hy[l] * b[nu]
            rows.append(row)
    return rows


def unit_vec(s, t):
    s, t = F(s), F(t)
    d = 1 + s * s + t * t
    return [2 * s / d, 2 * t / d, (s * s + t * t - 1) / d]


POOL = [unit_vec(s, t) for (s, t) in [(0, 0), (1, 0), (0, 1), (2, 0), (0, 3), (1, 1), (Fr(1, 2), 2), (3, -1),
                                         (-2, Fr(1, 3)), (Fr(2, 5), Fr(-3, 4)), (5, 7), (-1, -4), (Fr(1, 3), Fr(1, 7))]]
POOL += [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0]]


def nflip_vec(y):
    return [F(y[0]), -F(y[1]), -F(y[2])]


def rows_C3():
    return [r for y in POOL for r in rows_tight(y, hom([-F(t) for t in y]))]


def rows_C4():
    return [r for y in POOL for r in rows_tight(y, hom([-t for t in nflip_vec(y)]))]


R1, R2, R3, R4 = rows_C1(), rows_C2(), rows_C3(), rows_C4()
dims = {}
for name, rows in [("C1+C2+C3+C4", R1 + R2 + R3 + R4), ("C1+C2+C3", R1 + R2 + R3), ("C1+C2+C4", R1 + R2 + R4),
                   ("C1+C2", R1 + R2), ("C2+C3+C4 (no relC)", R2 + R3 + R4), ("C1+C3+C4 (no corner-orth)", R1 + R3 + R4)]:
    dims[name] = NU - rank(rows, NU)
rep.note("solution-space dimensions (exact rational rank, 18 sample targets): " +
         ", ".join(f"{k}: {v}" for k, v in dims.items()))
rep.check("B.1 upper bound: C1+C2+C3+C4 leave exactly 4 free parameters", dims["C1+C2+C3+C4"] == 4)


def blockvec(tb):
    return [tb[(ti, l)][o] for ti in (0, 1) for l in range(4) for o in range(16)]


basis = [blockvec(family_block(*[Fr(1) if i == k else Fr(0) for i in range(4)])) for k in range(4)]
rep.check("B.2 the four family directions are independent and satisfy every sampled C1-C4 row exactly",
          rank(basis, NU) == 4 and all(sum(r[i] * v[i] for i in range(NU)) == 0 for v in basis for r in R1 + R2 + R3 + R4))

# symbolic lower bound: C3, C4 for every unit y (stereographic s, t), and C1, C2 exactly
s, t = sp.symbols("s t", real=True)
den = 1 + s * s + t * t
ysym = [2 * s / den, 2 * t / den, (s * s + t * t - 1) / den]


def sym_tight_ok(v, use_N):
    hy = [sp.Integer(1)] + ysym
    yb = [ysym[0], -ysym[1], -ysym[2]] if use_N else ysym
    b = [sp.Integer(1)] + [-c for c in yb]
    for ti in (0, 1):
        for mu in range(4):
            e = 0
            for l in range(4):
                for nu in range(4):
                    c = v[uidx(ti, l, 4 * mu + nu)]
                    if c != 0:
                        e += sp.Rational(c.numerator, c.denominator) * hy[l] * b[nu]
            if sp.simplify(sp.together(e)) != 0:
                return False
    return True


rep.check("B.3 lower bound: each family direction satisfies C3 and C4 identically on the unit sphere (symbolic)",
          all(sym_tight_ok(v, False) and sym_tight_ok(v, True) for v in basis))
rep.check("B.4 every F(a, a2, b1, b2) satisfies relC with nflip, the frame at z3 and u o F = u (four directions + the "
          "corner columns, exact)", all(relC(fam(*p)) and ctrl_frame(fam(*p)) and norm_pres(fam(*p))
                                         for p in [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (2, -3, 5, 7)]))

# ---------------------------------------------------------------- Part C: two-sided positivity forces +-1
A_, A2, B1, B2 = sp.symbols("a a2 b1 b2", real=True)
E = sp.symbols("e0 e1 e2 e3", real=True)
Fv = sp.symbols("f0 f1 f2 f3", real=True)


def sym_gate(a, a2, b1, b2):
    """Symbolic F: the corner columns (fam(0,0,0,0)) plus the four tangent directions (fam(e_k) - fam(0,0,0,0)).
    Run 1 added fam(e_k) itself, counting the corner columns once per parameter (harness error, kept in run1)."""
    M = sp.zeros(16, 16)
    zero = fam(0, 0, 0, 0)
    base = [madd(fam(*[1 if i == k else 0 for i in range(4)]), zero, 1, -1) for k in range(4)]
    for r in range(16):
        for c in range(16):
            M[r, c] = sp.Rational(zero[r][c].numerator, zero[r][c].denominator) + sum(
                sp.Rational(base[k][r][c].numerator, base[k][r][c].denominator) * sym
                for k, sym in enumerate([a, a2, b1, b2]) if base[k][r][c] != 0)
    return M


GS = sym_gate(A_, A2, B1, B2)
GSI = sym_gate(1 / A_, 1 / A2, -1 / B2, -1 / B1)
rep.check("C.0 the inverse of F(a, a2, b1, b2) is F(1/a, 1/a2, -1/b2, -1/b1) (symbolic product = I)",
          sp.simplify(GS * GSI - sp.eye(16)) == sp.zeros(16, 16))


def sym_val(Mg, x, y):
    w = Mg * sp.Matrix([hx * hy for hx in [1] + list(x) for hy in [1] + list(y)])
    return sp.expand(sum(E[m] * w[4 * m + n] * Fv[n] for m in range(4) for n in range(4)))


v_a = sym_val(GS, [1, 0, 0], [1, 0, 0])
rep.check("C.1 at x = e_x, y = e_x: pairVal e f (F (prodState x y)) = (e0 + a e1)(f0 + f1) exactly",
          sp.expand(v_a - (E[0] + A_ * E[1]) * (Fv[0] + Fv[1])) == 0)
v_a2 = sym_val(GS, [0, 1, 0], [1, 0, 0])
sub_f = {Fv[0]: 1, Fv[1]: 0, Fv[2]: 0, Fv[3]: 0}
v_b2 = sym_val(GS, [1, 0, 0], [0, 1, 0])
v_b1 = sym_val(GS, [0, 1, 0], [0, 1, 0])
sub_fz = {Fv[0]: 1, Fv[1]: 0, Fv[2]: 0, Fv[3]: 1}
rep.note(f"value at x = e_y, y = e_x, f = (1,0,0,0): {sp.factor(v_a2.subs(sub_f))}")
rep.note(f"value at x = e_x, y = e_y, f = (1,0,0,1): {sp.factor(v_b2.subs(sub_fz))}")
rep.note(f"value at x = e_y, y = e_y, f = (1,0,0,1): {sp.factor(v_b1.subs(sub_fz))}")
rep.check("C.2 the three other test values are e0 + a2 e2, e0 + b2 e2 and e0 + b1 e1 (with e2, e1 free on the cone)",
          sp.expand(v_a2.subs(sub_f) - (E[0] + A2 * E[2])) == 0
          and sp.expand(v_b2.subs(sub_fz) - (E[0] + B2 * E[2])) == 0
          and sp.expand(v_b1.subs(sub_fz) - (E[0] + B1 * E[1])) == 0)
rep.note("C.3 [written from C.1-C.2] posFwd with e = (1, -+1, 0, 0) or (1, 0, -+1, 0) on the cone boundary gives "
         "|a|, |a2|, |b1|, |b2| <= 1; posInv applies the same values to the inverse F(1/a, 1/a2, -1/b2, -1/b1) (C.0), "
         "giving |1/a|, ... <= 1; invertibility excludes 0. Hence a, a2, b1, b2 in {+1, -1}.")


# exact sign-pattern analysis
def posfwd_witness(Gm):
    """Search small rational points for a negative product-effect value of Gm on a product (exact)."""
    circ = [(Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(-1), Fr(0)), (Fr(0), Fr(-1)), (Fr(3, 5), Fr(4, 5)), (Fr(4, 5), Fr(3, 5)),
            (Fr(-3, 5), Fr(4, 5)), (Fr(-4, 5), Fr(3, 5)), (Fr(3, 5), Fr(-4, 5)), (Fr(4, 5), Fr(-3, 5)),
            (Fr(-3, 5), Fr(-4, 5)), (Fr(-4, 5), Fr(-3, 5))]
    for (tx, ty) in circ[4:6]:
        x = [tx, ty, Fr(0)]
        for y in ([0, 1, 0], [1, 0, 0], [0, 0, 1]):
            w = apply(Gm, prodState(x, y))
            for (fx, fz) in circ:
                f = [Fr(1), fx, Fr(0), fz]
                for (ex, ey) in circ:
                    e = [Fr(1), ex, ey, Fr(0)]
                    v = pairVal(e, f, w)
                    if v < 0:
                        return (x, y, e, f, v)
    return None


LOC = [diag3(*sg) for sg in itertools.product((1, -1), repeat=3)]
LOCMATS = [(i, j, mmul(actC(LOC[i]), actT(LOC[j]))) for i in range(8) for j in range(8)]
good, bad = [], []
for sg in itertools.product((1, -1), repeat=4):
    a, a2, b1, b2 = sg
    Gm = fam(*sg)
    if a * b1 + a2 * b2 == 0:
        hit = None
        for (i1, j1, L1) in LOCMATS:
            for (i2, j2, L2) in LOCMATS:
                if meq(mmul(mmul(L1, CNOT), L2), Gm):
                    hit = (i1, j1, i2, j2)
                    break
            if hit:
                break
        good.append((sg, hit))
    else:
        bad.append((sg, posfwd_witness(Gm)))
rep.check("C.4 exactly 8 sign patterns satisfy a b1 + a2 b2 = 0, and each equals (actC D1 actT D2) cnot (actC D3 actT D4) "
          "with diagonal sign matrices D_i (exact identity found for all 8)",
          len(good) == 8 and all(h is not None for _, h in good))
for sg, h in good:
    rep.note(f"pattern (a,a2,b1,b2) = {sg}: D1, D2, D3, D4 = {[LOC[k] and [int(LOC[k][i][i]) for i in range(3)] for k in h]}")
rep.check("C.5 each of the other 8 sign patterns has an exact negative product-effect value on a product (posFwd fails)",
          len(bad) == 8 and all(w is not None and w[4] < 0 for _, w in bad))
for sg, w in bad:
    rep.note(f"excluded pattern {sg}: x = {[str(c) for c in w[0]]}, y = {w[1]}, e = {[str(c) for c in w[2]]}, "
             f"f = {[str(c) for c in w[3]]}, value {w[4]}")
rep.check("C.6 the 8 admissible patterns all satisfy CtrlGate's frame and relC exactly, and are all distinct",
          all(ctrl_frame(fam(*sg)) and relC(fam(*sg)) for sg, _ in good)
          and len({tuple(flat(fam(*sg))) for sg, _ in good}) == 8)
orient = {}
for sg, h in good:
    dets = tuple(int(det(LOC[k])) for k in h)
    orient[sg] = dets
rep.note("determinants (D1, D2, D3, D4) of the local sign maps found: " + str(orient))

# ---------------------------------------------------------------- Part D: the M0 freedom and the general (z, N)
OS = [("rot_z(3/5,4/5)", rot_axis(2, Fr(3, 5), Fr(4, 5))), ("reflY", REFLY), ("diag(-1,1,1)", diag3(-1, 1, 1))]
ok = True
for name, O in OS:
    Gm = mmul(CNOT, actT(O))
    ok &= ctrl_frame(Gm) and relC(Gm) and norm_pres(Gm)
rep.check("D.1 cnot o actT(O) satisfies frame, relC and normalization for O a z-rotation, reflY and diag(-1,1,1) "
          "(every O in O(3) with O z = z is allowed by the corner analysis)", ok)
q = (1, 2, -1, 3)
Rq = rot_from_quat(q)
zq = [sum(Rq[i][k] * Z3[k] for k in range(3)) for i in range(3)]
u0 = [Rq[i][0] for i in range(3)]
Nq = m3mul(m3mul(Rq, NFLIP), tr(Rq))
Lam = mmul(actC(Rq), actT(Rq))
LamI = mmul(actC(tr(Rq)), actT(tr(Rq)))
Gq = mmul(mmul(Lam, CNOT), LamI)
isnot = (m3mul(Nq, Nq) == I3 and [sum(Nq[i][k] * zq[k] for k in range(3)) for i in range(3)] == [-c for c in zq]
         and m3mul(Nq, tr(Nq)) == I3 and sum(c * c for c in zq) == 1)
rep.check("D.2 transport: for the rational rotation R(1,2,-1,3), Lam cnot Lam^-1 (Lam = actC R actT R) satisfies the frame "
          "at z = R z3 and relC with N = R nflip R^T, and IsNot holds for (z, N) (involution, N z = -z, orthogonal)",
          isnot and ctrl_frame(Gq, zq) and relC(Gq, Nq) and norm_pres(Gq))

# ---------------------------------------------------------------- Part E: entangling, inherited
ok = True
for sg, _ in good:
    w = apply(fam(*sg), prodState([1, 0, 0], Z3))
    ok &= rank([list(r) for r in w], 4) >= 2
rep.check("E.1 every admissible pattern maps prodState xplus z3 to a joint vector of matrix rank >= 2 (not a product)", ok)

# ---------------------------------------------------------------- Part F: countercontrols for the classification
ns12 = nullspace(R1 + R2, NU)
rnd = [(k * 7 + 3) % 11 - 5 for k in range(len(ns12))]
v = [sum(Fr(rnd[k]) * ns12[k][i] for k in range(len(ns12))) for i in range(NU)]
tb = {(ti, l): v[uidx(ti, l, 0): uidx(ti, l, 0) + 16] for ti in (0, 1) for l in range(4)}
Gx = gate_from(tb)
wit = posfwd_witness(Gx)
rep.check(f"F.1 countercontrol: without C3+C4 the space has dimension {dims['C1+C2']} > 4, and a fixed member of it "
          "violates posFwd at an exact point", dims["C1+C2"] > 4 and wit is not None and wit[4] < 0,
          f"value {wit[4] if wit else None}")
rep.check(f"F.2 countercontrol: without relC (C2+C3+C4) the space has dimension {dims['C2+C3+C4 (no relC)']} > 4",
          dims["C2+C3+C4 (no relC)"] > 4)
rep.verdict("NATIVE-CLASS: every CtrlGate at d = 3 with u o G = u is, after the rotation moving (z, u0) to (z3, e_x) and "
            "the corner map actT(M0), one of 8 sign patterns, each (local sign maps) o cnot o (local sign maps); "
            "hence every such gate is l1 o cnot o l2 with l1, l2 local O(3) x O(3) maps")
