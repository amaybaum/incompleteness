#!/usr/bin/env python3
"""
ds5_physics.py -- thread DS, question DS.5: the input's two displayed formulas as exact symbolic identities.

DECISION RULES (fixed in this header before the first run; rules, not expected numbers)
----------------------------------------------------------------------------------------
Every check prints one line "ID | text | PASS" or "... | FAIL".
* A decisive check PASSES when the stated identity holds exactly (sympy expansion to 0, or exact equality of
  algebraic numbers).
* A countercontrol (ID starting CC-) PASSES when the stated alternative is shown to FAIL exactly at the stated
  instance (a nonzero exact difference). A countercontrol that does not find the failure is a FAIL.
* Each block (F1..F7) prints "VERDICT <block>: ..." only if every check in the block PASSES; otherwise it prints
  "VERDICT <block>: VOID (a control failed)". The final line "ALL BLOCKS GREEN" prints only if every block is green.
* Exact arithmetic only: sympy symbols declared real, sympy.I, Rationals and sympy.sqrt(2). No floats anywhere.
* <u|v> := sum_k conj(u_k) v_k (conjugate-linear in the first slot). Re(w) := (w + conj(w))/2.

Blocks
F1  Formula 1. |a+b|^2 = |a|^2 + |b|^2 + 2 Re(conj(a) b) for symbolic complex a, b.
    CC-F1a: |a+b|^2 - (|a|^2+|b|^2) is not identically zero (nonzero at a=b=1).
    CC-F1b: the sign-flipped cross term fails at a=b=1.
F2  Formula 2 from a modelled record. Path branches L, R; the source's splitting amplitudes and the propagation to
    screen position x are absorbed into psi_L(x), psi_R(x) (symbolic complex). The record is a path-conditioned map on
    a detector space C^2 that leaves the propagation unchanged: the joint vector at x is
    psi_L(x) dL + psi_R(x) dR, with dL, dR in C^2 (symbolic). The detector is not read: P(x) = sum_k |.|^2.
    F2-general: P(x) = |psi_L|^2 ||dL||^2 + |psi_R|^2 ||dR||^2 + 2 Re(conj(psi_L) psi_R <dL|dR>) identically.
    F2-norm: P(x) minus the input's formula equals |psi_L|^2 (||dL||^2-1) + |psi_R|^2 (||dR||^2-1) identically, so
             the input's formula holds iff both detector states are normalized (for psi_L, psi_R not both zero).
    F2-unitary (instance): dL = UL d0, dR = UR d0 with exact unitaries UL = 1, UR = [[3i/5,-4i/5],[4/5,3/5]],
             d0 = (1,0): ||dL|| = ||dR|| = 1, gamma = <dL|dR> = 3i/5, and on the 4-point screen
             psi_L(x) = 1/(2 sqrt 2), psi_R(x) = i^x/(2 sqrt 2) the input's formula equals P(x) at every x and the
             four values sum to 1.
    CC-F2a (normalization load-bearing): dL=(1,1), dR=(1,0): the input's formula differs from P at x=0.
    CC-F2b (conjugation order load-bearing): <dR|dL> in place of <dL|dR> fails at x=1 of the F2-unitary instance.
    CC-F2c (no path disturbance load-bearing): if the coupling also kicks the R branch, psi_R(x) -> (-1)^x psi_R(x),
             the input's formula written with the undisturbed psi_R fails at x=1.
    CC-F2d (unread detector load-bearing): the pattern conditioned on detector outcome k=0 differs from the formula
             at x=1.
F3  Mixed detector. rho0 Hermitian 2x2 (symbolic), UL, UR arbitrary 2x2 (symbolic):
    tr(sum_{a,b} psi_a conj(psi_b) U_a rho0 U_b^dag)
      = |psi_L|^2 tr(UL rho0 UL^dag) + |psi_R|^2 tr(UR rho0 UR^dag) + 2 Re(conj(psi_L) psi_R tr(UL^dag UR rho0))
    identically; and for rho0 = d0 d0^dag, tr(UL^dag UR rho0) = <UL d0|UR d0> identically.
F4  Limiting cases. (i) dL = dR with ||dL||=1 reduces formula 2 to formula 1 (identity);
    (ii) dL=(1,0), dR=(0,1): the cross term is 0 (identity in psi);
    (iii) dR = i dL, ||dL||=1: gamma = i, |gamma| = 1, and at balanced amplitudes the visibility (F5) is 1.
F5  Visibility. With |psi_L| = aL, |psi_R| = aR, |gamma| = g (aL, aR > 0, g >= 0) and the relative phase of
    conj(psi_L) psi_R gamma sweeping a full period across the fringe [W], Pmax = aL^2+aR^2+2 aL aR g,
    Pmin = aL^2+aR^2-2 aL aR g, and V := (Pmax-Pmin)/(Pmax+Pmin) = 2 aL aR g/(aL^2+aR^2) (exact simplification);
    at aL = aR, V = g.
    CC-F5: at aL=1, aR=2, g=1, V = 4/5 differs from g (V = |gamma| needs balanced amplitudes).
F6  Distinguishability of pure records. For arbitrary a, b in C^2 and A = a a^dag - b b^dag:
    charpoly_A(t) = t^2 - (||a||^2-||b||^2) t - (||a||^2 ||b||^2 - |<a|b>|^2)  (identity), and
    ||a||^2 ||b||^2 - |<a|b>|^2 = |a0 b1 - a1 b0|^2 (Lagrange identity, so |gamma| <= 1 for unit vectors).
    For unit a, b the eigenvalues are +-sqrt(1-|gamma|^2), so D := (1/2)||A||_1 = sqrt(1-|gamma|^2) [W step: the trace
    norm is the sum of |eigenvalues|; in higher dimension A has rank <= 2 and acts on span{a,b}]. With balanced
    amplitudes V^2 + D^2 = g^2 + (1-g^2) = 1 (identity).
    CC-F6 (purity load-bearing): rho0 = 1/2, UL = 1, UR = X: gamma = 0 (V = 0) while the detector's two conditional
    states are equal (D = 0), so V^2 + D^2 = 0, not 1.
F7  Eraser for the perfect record dL=(1,0), dR=(0,1). Conditioned on detector outcome e_+- = (1,+-1)/sqrt2 the
    patterns are (1/2)|psi_L +- psi_R|^2 (identities) and their sum is |psi_L|^2+|psi_R|^2; in the record basis
    they are |psi_L|^2 and |psi_R|^2.
    CC-F7: the e_+ conditional pattern differs from the unconditioned record pattern at the F2 screen, x=0.
"""
import sympy as sp

I = sp.I
results = {}
order = []


def chk(block, cid, text, ok):
    ok = bool(ok)
    results.setdefault(block, []).append(ok)
    if block not in order:
        order.append(block)
    print(f"{cid} | {text} | {'PASS' if ok else 'FAIL'}")


def is_zero(expr):
    return sp.expand(expr) == 0


def cplx(name):
    re_, im_ = sp.symbols(f"{name}_re {name}_im", real=True)
    return re_ + I * im_


def ab2(z):
    return sp.expand(z * sp.conjugate(z))


def Re(z):
    return sp.expand((z + sp.conjugate(z)) / 2)


def inner(u, v):
    return sp.expand(sum(sp.conjugate(u[k]) * v[k] for k in range(len(u))))


def norm2(u):
    return sp.expand(sum(ab2(c) for c in u))


def verdict(block, text):
    if all(results.get(block, [False])):
        print(f"VERDICT {block}: {text}")
    else:
        print(f"VERDICT {block}: VOID (a control failed)")


# ---------------------------------------------------------------------------------------------------- F1
a = cplx("a")
b = cplx("b")
chk("F1", "F1", "|a+b|^2 == |a|^2+|b|^2+2Re(conj(a)b), a,b symbolic complex",
    is_zero(ab2(a + b) - (ab2(a) + ab2(b) + 2 * Re(sp.conjugate(a) * b))))
inst = {sp.Symbol("a_re", real=True): 1, sp.Symbol("a_im", real=True): 0,
        sp.Symbol("b_re", real=True): 1, sp.Symbol("b_im", real=True): 0}
d1 = sp.simplify((ab2(a + b) - (ab2(a) + ab2(b))).subs(inst))
chk("F1", "CC-F1a", f"interference term at a=b=1 is {d1} (must be nonzero)", d1 != 0)
d2 = sp.simplify((ab2(a + b) - (ab2(a) + ab2(b) - 2 * Re(sp.conjugate(a) * b))).subs(inst))
chk("F1", "CC-F1b", f"sign-flipped cross term misses by {d2} at a=b=1 (must be nonzero)", d2 != 0)
verdict("F1", "formula 1 is an exact identity; its cross term is the only interference term")

# ---------------------------------------------------------------------------------------------------- F2
pL = cplx("pL")
pR = cplx("pR")
dL = [cplx("dL0"), cplx("dL1")]
dR = [cplx("dR0"), cplx("dR1")]


def P_joint(psiL, psiR, vL, vR, signs=(1, 1)):
    return sp.expand(sum(ab2(psiL * vL[k] + signs[k] * psiR * vR[k]) for k in range(2)))


def input_formula(psiL, psiR, g):
    return sp.expand(ab2(psiL) + ab2(psiR) + 2 * Re(sp.conjugate(psiL) * psiR * g))


Pg = P_joint(pL, pR, dL, dR)
general = ab2(pL) * norm2(dL) + ab2(pR) * norm2(dR) + 2 * Re(sp.conjugate(pL) * pR * inner(dL, dR))
chk("F2", "F2-general", "P(x) == |pL|^2||dL||^2+|pR|^2||dR||^2+2Re(conj(pL)pR<dL|dR>), all symbolic",
    is_zero(Pg - general))
diff = Pg - input_formula(pL, pR, inner(dL, dR))
chk("F2", "F2-norm", "P - input formula == |pL|^2(||dL||^2-1)+|pR|^2(||dR||^2-1) identically",
    is_zero(diff - (ab2(pL) * (norm2(dL) - 1) + ab2(pR) * (norm2(dR) - 1))))

UL = sp.eye(2)
UR = sp.Matrix([[3 * I / 5, -4 * I / 5], [sp.Rational(4, 5), sp.Rational(3, 5)]])
unit_ok = (UL.H * UL == sp.eye(2)) and (sp.simplify(UR.H * UR - sp.eye(2)) == sp.zeros(2, 2))
d0 = sp.Matrix([1, 0])
vL = list(UL * d0)
vR = list(UR * d0)
gam = inner(vL, vR)
psiL_x = [1 / (2 * sp.sqrt(2)) for _ in range(4)]
psiR_x = [I ** x / (2 * sp.sqrt(2)) for x in range(4)]
vals = [sp.simplify(P_joint(psiL_x[x], psiR_x[x], vL, vR)) for x in range(4)]
form = [sp.simplify(input_formula(psiL_x[x], psiR_x[x], gam)) for x in range(4)]
chk("F2", "F2-unitary", f"UL,UR unitary: {unit_ok}; ||dL||^2={norm2(vL)}, ||dR||^2={norm2(vR)}, gamma={gam}; "
    f"P(x)={vals}; formula={form}; sum={sum(vals)}",
    unit_ok and norm2(vL) == 1 and norm2(vR) == 1 and vals == form and sum(vals) == 1)

wL, wR = [1, 1], [1, 0]
e = sp.simplify(P_joint(psiL_x[0], psiR_x[0], wL, wR) - input_formula(psiL_x[0], psiR_x[0], inner(wL, wR)))
chk("F2", "CC-F2a", f"unnormalized dL=(1,1): P - formula at x=0 is {e} (must be nonzero)", e != 0)
gam_sw = inner(vR, vL)
e = sp.simplify(input_formula(psiL_x[1], psiR_x[1], gam_sw) - vals[1])
chk("F2", "CC-F2b", f"<dR|dL>={gam_sw} in place of <dL|dR>: formula - P at x=1 is {e} (must be nonzero)", e != 0)
kick = [(-1) ** x for x in range(4)]
Pkick = sp.simplify(P_joint(psiL_x[1], kick[1] * psiR_x[1], vL, vR))
e = sp.simplify(input_formula(psiL_x[1], psiR_x[1], gam) - Pkick)
chk("F2", "CC-F2c", f"kicked R branch: P(1)={Pkick}; undisturbed formula misses by {e} (must be nonzero)", e != 0)
Pcond = sp.simplify(ab2(psiL_x[1] * vL[0] + psiR_x[1] * vR[0]))
e = sp.simplify(Pcond - vals[1])
chk("F2", "CC-F2d", f"conditioned on detector k=0: P(1,k=0)={Pcond}; differs from formula by {e} (must be "
    f"nonzero)", e != 0)
verdict("F2", "formula 2 is exact for a path-conditioned record that leaves the propagation unchanged, with "
        "normalized detector states and the detector unread")

# ---------------------------------------------------------------------------------------------------- F3
r00, r11, rp, rq = sp.symbols("r00 r11 rp rq", real=True)
rho0 = sp.Matrix([[r00, rp + I * rq], [rp - I * rq, r11]])
ULs = sp.Matrix(2, 2, [cplx(f"uL{i}") for i in range(4)])
URs = sp.Matrix(2, 2, [cplx(f"uR{i}") for i in range(4)])
psi = {"L": pL, "R": pR}
U = {"L": ULs, "R": URs}
lhs = sp.expand(sum(psi[s] * sp.conjugate(psi[t]) * (U[s] * rho0 * U[t].H).trace()
                    for s in "LR" for t in "LR"))
rhs = sp.expand(ab2(pL) * (ULs * rho0 * ULs.H).trace() + ab2(pR) * (URs * rho0 * URs.H).trace()
                + 2 * Re(sp.conjugate(pL) * pR * (ULs.H * URs * rho0).trace()))
chk("F3", "F3-mixed", "tr(sum psi_a conj(psi_b) U_a rho0 U_b^dag) == mixed-detector formula, all symbolic",
    is_zero(lhs - rhs))
dd = sp.Matrix([cplx("e0"), cplx("e1")])
rho_pure = dd * dd.H
lhs2 = sp.expand((ULs.H * URs * rho_pure).trace())
rhs2 = inner(list(ULs * dd), list(URs * dd))
chk("F3", "F3-pure", "for rho0 = d0 d0^dag: tr(UL^dag UR rho0) == <UL d0|UR d0>, all symbolic", is_zero(lhs2 - rhs2))
verdict("F3", "for a mixed detector the overlap is replaced by gamma = tr(UL^dag UR rho0); the pure case is "
        "<dL|dR>")

# ---------------------------------------------------------------------------------------------------- F4
u = [cplx("u0"), cplx("u1")]
f2_same = sp.expand(ab2(pL) + ab2(pR) + 2 * Re(sp.conjugate(pL) * pR * inner(u, u)))
f1 = sp.expand(ab2(pL + pR))
# formula 2 with dL = dR = u and ||u|| = 1: substitute <u|u> -> 1 by eliminating via the norm.
chk("F4", "F4-i", "dL = dR = u: formula 2 - formula 1 == 2Re(conj(pL)pR)(||u||^2 - 1), so equal when ||u||=1",
    is_zero(f2_same - f1 - 2 * Re(sp.conjugate(pL) * pR) * (norm2(u) - 1)))
cross = sp.expand(2 * Re(sp.conjugate(pL) * pR * inner([1, 0], [0, 1])))
chk("F4", "F4-ii", f"orthogonal records: cross term == {cross}", cross == 0)
g3 = inner([1, 0], [I, 0])
chk("F4", "F4-iii", f"dR = i dL: gamma = {g3}, |gamma|^2 = {ab2(g3)}", g3 == I and ab2(g3) == 1)
verdict("F4", "identical records leave formula 1; orthogonal records remove the cross term; records equal up to "
        "a phase keep |gamma| = 1 and shift the fringes")

# ---------------------------------------------------------------------------------------------------- F5
aL, aR, g = sp.symbols("aL aR g", positive=True)
Pmax = aL ** 2 + aR ** 2 + 2 * aL * aR * g
Pmin = aL ** 2 + aR ** 2 - 2 * aL * aR * g
V = sp.simplify((Pmax - Pmin) / (Pmax + Pmin))
chk("F5", "F5-V", f"V = {V}", sp.simplify(V - 2 * aL * aR * g / (aL ** 2 + aR ** 2)) == 0)
Vbal = sp.simplify(V.subs(aR, aL))
chk("F5", "F5-bal", f"balanced amplitudes: V = {Vbal}", Vbal == g)
Vcc = V.subs({aL: 1, aR: 2, g: 1})
chk("F5", "CC-F5", f"aL=1, aR=2, g=1: V = {Vcc} (must differ from g = 1)", Vcc != 1)
verdict("F5", "V = V0 |gamma| with V0 = 2 aL aR/(aL^2+aR^2); V = |gamma| only for balanced amplitudes")

# ---------------------------------------------------------------------------------------------------- F6
av = [cplx("x0"), cplx("x1")]
bv = [cplx("y0"), cplx("y1")]
A = sp.Matrix(av) * sp.Matrix(av).H - sp.Matrix(bv) * sp.Matrix(bv).H
t = sp.Symbol("t")
cp = sp.expand(A.charpoly(t).as_expr())
target = sp.expand(t ** 2 - (norm2(av) - norm2(bv)) * t - (norm2(av) * norm2(bv) - ab2(inner(av, bv))))
chk("F6", "F6-charpoly", "charpoly(a a^dag - b b^dag) == t^2 - (|a|^2-|b|^2)t - (|a|^2|b|^2 - |<a|b>|^2)",
    is_zero(cp - target))
lag = sp.expand(norm2(av) * norm2(bv) - ab2(inner(av, bv)) - ab2(av[0] * bv[1] - av[1] * bv[0]))
chk("F6", "F6-lagrange", "|a|^2|b|^2 - |<a|b>|^2 == |a0 b1 - a1 b0|^2 (so |gamma| <= 1 for unit vectors)",
    lag == 0)
gg = sp.Symbol("gg", nonnegative=True)
D = sp.sqrt(1 - gg ** 2)
chk("F6", "F6-compl", "balanced amplitudes, pure records: V^2 + D^2 == 1 with V = g, D = sqrt(1-g^2)",
    sp.simplify(gg ** 2 + D ** 2 - 1) == 0)
rho_mix = sp.Matrix([[sp.Rational(1, 2), 0], [0, sp.Rational(1, 2)]])
Xm = sp.Matrix([[0, 1], [1, 0]])
gam_mix = (sp.eye(2).H * Xm * rho_mix).trace()
sL = sp.eye(2) * rho_mix * sp.eye(2).H
sR = Xm * rho_mix * Xm.H
chk("F6", "CC-F6", f"rho0 = 1/2, UR = X: gamma = {gam_mix} (V = 0) and the conditional detector states are equal: "
    f"{sL == sR} (D = 0); V^2 + D^2 = 0 (must differ from 1)", gam_mix == 0 and sL == sR)
verdict("F6", "for pure records D = sqrt(1-|gamma|^2) and V^2 + D^2 = 1 at balanced amplitudes; for mixed records "
        "the detector's own distinguishability does not fix V")

# ---------------------------------------------------------------------------------------------------- F7
r2 = sp.sqrt(2)
ep = [1 / r2, 1 / r2]
em = [1 / r2, -1 / r2]
vec = [pL, pR]          # psi_L dL + psi_R dR with dL=(1,0), dR=(0,1)
Pp = sp.expand(ab2(inner(ep, vec)))
Pm = sp.expand(ab2(inner(em, vec)))
chk("F7", "F7-plus", "P(x,+) == (1/2)|pL+pR|^2", is_zero(Pp - ab2(pL + pR) / 2))
chk("F7", "F7-minus", "P(x,-) == (1/2)|pL-pR|^2", is_zero(Pm - ab2(pL - pR) / 2))
chk("F7", "F7-sum", "P(x,+) + P(x,-) == |pL|^2 + |pR|^2", is_zero(Pp + Pm - ab2(pL) - ab2(pR)))
P0 = sp.expand(ab2(inner([1, 0], vec)))
P1 = sp.expand(ab2(inner([0, 1], vec)))
chk("F7", "F7-record", "record basis: P(x,0) == |pL|^2 and P(x,1) == |pR|^2", is_zero(P0 - ab2(pL)) and
    is_zero(P1 - ab2(pR)))
cplus = sp.simplify(ab2(psiL_x[0] + psiR_x[0]) / 2)
cunc = sp.simplify(ab2(psiL_x[0]) + ab2(psiR_x[0]))
chk("F7", "CC-F7", f"x=0: P(0,+) = {cplus} vs the unconditioned record pattern {cunc} (must differ)", cplus != cunc)
verdict("F7", "reading the detector in a basis complementary to the record restores fringes and antifringes in the "
        "conditioned subensembles; they sum to the fringe-free pattern")

# ---------------------------------------------------------------------------------------------------- summary
green = [blk for blk in order if all(results[blk])]
print(f"SUMMARY: {sum(len(v) for v in results.values())} checks; blocks green {len(green)}/{len(order)}")
if len(green) == len(order):
    print("ALL BLOCKS GREEN")
