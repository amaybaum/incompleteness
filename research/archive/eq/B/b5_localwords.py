"""EQ-B / B5: the J/K flow does not coexist with local rotations at d = 5 (exact), and does at d = 3 (QT).

  W5 = gC5 . (I (x) L) . gC5,  L = the 90-degree rotation of eball 5 in the coordinate plane (2, 4)
       (a signed permutation: e2 -> e4 -> -e2, coordinates 0..4).  Exact rational witness x, y (unit), a, b (unit):
       pairVal((1,a), (1,b), W5(prodState x y)) < 0, so W5(prodState x y) is not in maxCone (eball 5).
       Consequence: no joint state space S with products subset S subset maxCone is invariant under both gC5 and the
       local rotation I (x) L (it would contain W5(prodState x y)).
  W7 = G_pi . (I (x) L7) . G_pi at d = 7 (J/K gate of jk.py, L7 the 90-degree rotation in the coordinate plane (2, 6)):
       exact rational witness outside maxCone (eball 7), the same mechanism.
  W3 = cnot . (I (x) L3) . cnot with L3 the 90-degree rotation in the plane (y, z): equal to Ad(U) for the QT unitary
       U = CNOT (I (x) V) CNOT, V = exp(-i pi/4 X) up to phase, hence a QT channel (positive).  Exact identity.
  Controls: the same word with L in the plane (1, 2) (inside the J/K commutant, (w1,w2)) has no negative value at the
       witness-seeded sample; and gC5 itself has value >= 0 at the witness (kernel positivity, sanity).
Run: python3 -I -B b5_localwords.py
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blib import *   # noqa: E402
from qlib import *   # noqa: E402

checks = []


def chk(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


def stereo_unit(v, den=1000):
    """Rational unit vector near the float unit vector v (inverse stereographic projection from -e_last)."""
    d = len(v)
    # projection from the south pole -e_{d-1}: u_i = v_i / (1 + v_{d-1})
    last = v[-1]
    if last < -0.9:
        # project from the north pole instead
        u = [Fr(round(v[i] / (1 - last) * den), den) for i in range(d - 1)]
        s2 = sum(t * t for t in u)
        out = [2 * t / (1 + s2) for t in u] + [(s2 - 1) / (s2 + 1)]
        return out
    u = [Fr(round(v[i] / (1 + last) * den), den) for i in range(d - 1)]
    s2 = sum(t * t for t in u)
    out = [2 * t / (1 + s2) for t in u] + [(1 - s2) / (1 + s2)]
    return out


def givens90(d, i, j):
    L = zeros(d, d)
    for k in range(d):
        L[k][k] = Fr(1)
    L[i][i] = Fr(0); L[j][j] = Fr(0); L[j][i] = Fr(1); L[i][j] = Fr(-1)
    return L


def main():
    d, n = 5, 6
    G = gC5()
    L = givens90(d, 2, 4)
    IL = kron(eye(n), homMap(L))
    W = matmul(G, matmul(IL, G))
    # float witness from x3_simple_words_float.out (plane (2,4), target, t = s = pi)
    xf = [-0.5032865646689734, 0.5228718140773244, 0.6399261959591808, 0.2525846489123324, -0.0017772805735264455]
    yf = [-0.00508732755821443, 0.5043183972974563, -0.1356192969194169, 0.14892074570660987, -0.8396827323739072]
    af = [0.5057683782293789, -0.5272318073264012, -0.6313473819364582, -0.25992185358386205, 0.008129100692564045]
    bf = [0.014207152889768699, -0.4582620929643144, -0.6967469080775136, 0.2527338470652086, -0.4903706349189125]
    x, y, a, b = (stereo_unit(v) for v in (xf, yf, af, bf))
    for name, v in (("x", x), ("y", y), ("a", a), ("b", b)):
        assert sum(t * t for t in v) == 1, name
    print("     witness x =", [str(t) for t in x])
    print("     witness y =", [str(t) for t in y])
    print("     witness a =", [str(t) for t in a])
    print("     witness b =", [str(t) for t in b])
    val = pairVal(homvec(a), homvec(b), apply(W, prodState(x, y)))
    print("     value =", val, "~", float(val))
    chk("W5 exact: all four witness vectors are exact rational unit vectors", True)
    chk("W5 exact: pairVal((1,a),(1,b), gC5 (I(x)L) gC5 (prodState x y)) < 0  (not in maxCone eball 5)", val < 0)
    # effects (1/2)(1, a) are IsEffectOn eball 5 (Lor with head 1/2): value scales by 1/4, sign unchanged.
    # sanity: gC5 alone at the same point and effects is >= 0 (kernel positivity)
    v0 = pairVal(homvec(a), homvec(b), apply(G, prodState(x, y)))
    chk("W5 sanity: gC5 alone gives a nonnegative value at the witness (kernel gC5_posFwd)", v0 >= 0)
    # control: L in the plane (1,2) of coordinates (hom (2,3) = (y, w1)) ... use the J/K-commuting plane (w1, w2)
    Lc = givens90(d, 2, 3)   # coordinates 2,3 = hom indices 3,4 = (w1, w2): J- and K-plane
    Wc = matmul(G, matmul(kron(eye(n), homMap(Lc)), G))
    vc = pairVal(homvec(a), homvec(b), apply(Wc, prodState(x, y)))
    print("     control (w1,w2)-plane word value at the witness:", vc)
    chk("W5 control: the word with L in the (w1, w2) plane is nonnegative at the witness", vc >= 0)

    # ---------------- note (not a verdict of this thread): the Bell-like image of (e_x, z5) under gC5 is not
    # extreme in jointStates (eball 5): omega = diag(1, 1, -1, 0, 0, 1) and omega +- E_{w1 w1} are joint states,
    # since their tail blocks are diagonal with entries in {-1, 0, 1} (operator norm <= 1, so
    # e0 f0 + e_T . D f_T >= e0 f0 - |e_T||f_T| >= 0 on Lorentz vectors) and their (0,0) entry is 1.
    om = apply(G, prodState([1, 0, 0, 0, 0], [0, 0, 0, 0, 1]))
    target = diag([1, 1, -1, 0, 0, 1])
    ok_om = meq(om, target)
    for sgn_ in (1, -1):
        pert = [list(r) for r in om]
        pert[3][3] += sgn_
        tail = [r[1:] for r in pert[1:]]
        diag_ok = all(tail[i][j] == 0 for i in range(5) for j in range(5) if i != j) and \
            all(abs(tail[i][i]) <= 1 for i in range(5)) and pert[0][0] == 1 and \
            all(pert[0][j] == 0 for j in range(1, 6)) and all(pert[i][0] == 0 for i in range(1, 6))
        ok_om = ok_om and diag_ok
    chk("N1 note: gC5(prodState(e_x, z5)) = diag(1,1,-1,0,0,1), and adding +-E_{w1w1} keeps a block-diagonal "
        "contraction form (so the image is not an extreme joint state)", ok_om)
    # N2: the image is entangled: the witness Lam(w) = w00 - w_xx + w_yy - w_zz equals 1 - a.Mb >= 0 on every
    # product state (M = diag(1,-1,0,0,1) on the coordinates (x, y, w1, w2, z) is a contraction), and Lam(omega) = -2.
    lam = om[0][0] - om[1][1] + om[2][2] - om[5][5]
    chk("N2: gC5 maps the pure product (e_x, z5) to an entangled joint state (witness value -2; the witness is "
        ">= 0 on all products since its tail is a contraction)", lam == -2)

    # ---------------- d = 7: the J/K gate G_pi and the 90-degree rotation in the coordinate plane (2, 6)
    from jk import flow_op
    G7 = flow_op(7, Fr(-1), Fr(0))
    L7 = givens90(7, 2, 6)
    W7 = matmul(G7, matmul(kron(eye(8), homMap(L7)), G7))
    xf7 = [0.20450806177194797, 0.25950538419430114, 0.5000074060843196, 0.7245622132147954, 0.3192042859229002,
           -0.1180856686182723, -1.4084539785357954e-06]
    yf7 = [7.648587973212237e-08, -0.16508465597665808, 0.3261131249297993, -0.8485676337723304,
           4.6428044263473133e-07, -2.1983767398677387e-07, -0.3825313804426353]
    af7 = [-0.20450998377605584, -0.2595058733123584, -0.5000064338890006, -0.7245625512461109,
           -0.31920382752080617, 0.11808454661165975, 1.1068795225679138e-06]
    bf7 = [-1.3957519290942765e-06, 0.716760822939777, -0.03989118783573181, 0.4832958272127048,
           -3.090318785787792e-07, -3.503110470378754e-07, -0.5010865785753686]
    x7, y7, a7, b7 = (stereo_unit(v) for v in (xf7, yf7, af7, bf7))
    assert all(sum(t * t for t in v) == 1 for v in (x7, y7, a7, b7))
    val7 = pairVal(homvec(a7), homvec(b7), apply(W7, prodState(x7, y7)))
    print("     W7 value =", float(val7))
    chk("W7 exact (d = 7): G_pi (I(x)L) G_pi maps a pure product state outside maxCone (eball 7)", val7 < 0)
    v07 = pairVal(homvec(a7), homvec(b7), apply(G7, prodState(x7, y7)))
    chk("W7 sanity: G_pi alone is nonnegative at the witness", v07 >= 0)

    # ---------------- d = 3: the analogous word is a QT channel
    G3 = cnot3()
    L3 = givens90(3, 1, 2)          # 90-degree rotation in the (y, z) plane: y -> z -> -y
    W3 = matmul(G3, matmul(kron(eye(4), homMap(L3)), G3))
    # V = (I - i X)/sqrt2 rotates the Bloch (y,z) plane by 90 degrees; use the unnormalised I - iX
    # (Ad is insensitive to a positive scalar up to the factor |c|^2 = 2, divided out below)
    V = cadd(PI, cscale(Q(0, -1), PX))
    U = cmul(controlled(PI, PX), cmul(ckron(PI, V), controlled(PI, PX)))
    WU = channel_W(U)
    WU = [[t / 2 for t in r] for r in WU]           # |1 - i|^2 = 2 per factor of V... V V^dag = 2 I
    LV = local_W(V)
    LV = [[t / 2 for t in r] for r in LV]
    chk("W3 control: Ad(I - iX)/2 is the 90-degree rotation of the Bloch (y, z) plane used in the word",
        meq(LV, homMap(L3)))
    chk("W3 control: cnot (I(x)L3) cnot = Ad(CNOT (I(x)V) CNOT), a QT channel (hence positive)", meq(W3, WU))

    nfail = sum(1 for _, ok in checks if not ok)
    print(f"b5_localwords: {len(checks) - nfail}/{len(checks)} checks PASS")
    print("VERDICT", "B5-GREEN" if nfail == 0 else "B5-RED")
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
