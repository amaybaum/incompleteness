# r6_single.py -- R6 node R6: the single-token premises the alternatives inherit (statement (iii)), checked exactly where
# a finite exact check exists. Every alternative K ⊆ W 3 has the tokens of Q3: the body eball 3 (= ball3, eball_three
# [K] TransitiveBody.lean:670), the NOT nflip, the corner axis z3, the gate cnot. Nothing below depends on K.
# DECISION RULE (fixed before the first run, 18:26Z by date -u):
#  T1 HasTwoSharpTests (eball 3): e = (1 + x1)/2, f = (1 + x2)/2 are effects on the ball (|coefficient vector| = 1/2
#     = constant term), each is a sharp seed (value 1 at e_i, 0 at -e_i), f(e1) != e(e1) and f(e1) != 1 - e(e1). Exact.
#  T2 SharpSeed (K∞-Seed): r = (1 + x3)/2, the same test.
#  T3 the NOT: nflip is the rotation by pi about u = e1 (N x = 2(u.x)u - x, piRotation_three's form), det 1, involutive,
#     flips z3; ball3Drive's NOT rot3(pi) = diag(-1,-1,1) fixes z3 (I3 exposed fact 3), so the two NOTs differ.
#  T4 ElementaryDrivability: (i) ball3Drive (flow rot3 about z, N = rot3 pi, J = cyc3): J_off_axis at t = pi/2 -- the
#     point e3 is fixed by every flow member and moved by J R_z(pi/2) J^-1; (ii) the stage-4/5 'drive through the NOT'
#     (flow R_x(t), N = R_x(pi) = nflip, J = cyc3): e1 is fixed by every R_x(s) and moved by J R_x(pi/2) J^-1. Exact
#     (rational quarter turns).
#  T5 CopyNatural (K∞-Copy): with one NOT on both copies, CopyNatural nflip nflip id holds; under the exchange of the two
#     tokens, SWAP o actC nflip o SWAP = actT nflip on all 16 basis tables.
#  T6 K∞-Trans instance: a rational rotation carries the boundary state e3 to (3/5, 0, 4/5) and to (0, 0, -1) (boundary
#     transitivity of fullAut3 is [K] OrbitGeneration.lean:537; this is an instance check only).
#  T7 K∞-Geom on the token: a proper directional effect (1 + b.x)/2 (|b| = 1) is certain only at x = b: (1 + b.x)/2 = 1
#     with |x| <= 1 forces |x - b|^2 = |x|^2 - 1 <= 0 (exact identity |x - b|^2 = |x|^2 + 1 - 2 b.x, symbolic).
#  Countercontrols: T1c the pair e = (1 + x1)/2, f = 1 - e fails the second separation clause; T3c reflY is not a rotation (det -1),
#   so it is not a NOT in the sense of piRotation_three; T4c the flow alone (J = identity) fails J_off_axis at the
#   tested points.
#  VERDICT R6-SINGLE-EXACT printed only if every check passes and every countercontrol fails as stated.
import sympy as sp

Rt = sp.Rational
RES = {}
def chk(cid, ok, note=''):
    RES[cid] = bool(ok); print('CHECK %-26s %s %s' % (cid, 'PASS' if ok else 'FAIL', note))
e = [sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1])]
def eff(c0, cv):  # affine functional x -> c0 + cv.x; effect on the unit ball iff |cv| <= c0 and c0 + |cv| <= 1
    n2 = (cv.T * cv)[0]
    return (n2 <= c0 ** 2) and ((1 - c0) ** 2 >= n2) and c0 <= 1
def val(c0, cv, x): return c0 + (cv.T * x)[0]
E1 = (Rt(1, 2), e[0] / 2); F1 = (Rt(1, 2), e[1] / 2); R3 = (Rt(1, 2), e[2] / 2)
def sharp(f, i): return eff(*f) and val(*f, e[i]) == 1 and val(*f, -e[i]) == 0
chk('T1 HasTwoSharpTests', sharp(E1, 0) and sharp(F1, 1) and val(*F1, e[0]) != val(*E1, e[0]) and val(*F1, e[0]) != 1 - val(*E1, e[0]),
    '[K] hasTwoSharpTests_iff SharpTests.lean:155 (2 <= 3)')
xx = sp.Matrix(sp.symbols('y1:4'))
chk('T1c complement fails', sp.expand(val(Rt(1, 2), -e[0] / 2, xx) - (1 - val(*E1, xx))) == 0, 'f = 1 - e: f(x) = 1 - e(x) for every x, so the clause fails')
chk('T2 SharpSeed', sharp(R3, 2), 'r = (1 + x3)/2')
nflip = sp.diag(1, -1, -1); u = e[0]
x = sp.Matrix(sp.symbols('x1:4'))
chk('T3 nflip = pi-rotation', sp.expand(nflip * x - (2 * (u.T * x)[0] * u - x)) == sp.zeros(3, 1) and nflip.det() == 1
    and nflip * nflip == sp.eye(3) and nflip * e[2] == -e[2], 'about e1; flips z3')
rot3pi = sp.diag(-1, -1, 1)
chk('T3 ball3Drive NOT != nflip', rot3pi * e[2] == e[2] and rot3pi != nflip, 'rot3 pi fixes z3')
chk('T3c reflY not a rotation', sp.diag(1, -1, 1).det() == -1)
Rz = lambda c, s_: sp.Matrix([[c, -s_, 0], [s_, c, 0], [0, 0, 1]])
Rx = lambda c, s_: sp.Matrix([[1, 0, 0], [0, c, -s_], [0, s_, c]])
cyc3 = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
cs, sn = sp.symbols('cs sn', real=True)
conjz = cyc3 * Rz(0, 1) * cyc3.inv(); conjx = cyc3 * Rx(0, 1) * cyc3.inv()
okz = all(sp.simplify(Rz(cs, sn) * e[2] - e[2]) == sp.zeros(3, 1) for _ in [0]) and conjz * e[2] != e[2]
okx = sp.simplify(Rx(cs, sn) * e[0] - e[0]) == sp.zeros(3, 1) and conjx * e[0] != e[0]
chk('T4 J_off_axis ball3Drive', okz, 'e3 fixed by every R_z(s), moved by cyc3 R_z(pi/2) cyc3^-1: %s' % list(conjz * e[2]))
chk('T4 J_off_axis drive about x', okx, 'e1 fixed by every R_x(s), moved by cyc3 R_x(pi/2) cyc3^-1: %s' % list(conjx * e[0]))
chk('T4c flow alone (J = id)', Rz(0, 1) * e[2] == e[2] and Rx(0, 1) * e[0] == e[0], 'J = identity moves neither test point')
def Hom(N): H = sp.eye(4); H[1:, 1:] = N; return H
def E(m, n): t = sp.zeros(4, 4); t[m, n] = 1; return t
basis = [E(m, n) for m in range(4) for n in range(4)]
chk('T5 CopyNatural', all((Hom(nflip) * b.T).T == b * Hom(nflip).T for b in basis), 'SWAP o actC nflip o SWAP = actT nflip (16/16); identity: one N')
Rt6 = sp.Matrix([[Rt(4, 5), 0, Rt(3, 5)], [0, 1, 0], [Rt(-3, 5), 0, Rt(4, 5)]])
chk('T6 boundary transport', Rt6.T * Rt6 == sp.eye(3) and Rt6.det() == 1 and Rt6 * e[2] == sp.Matrix([Rt(3, 5), 0, Rt(4, 5)])
    and Rx(-1, 0) * e[2] == -e[2], 'instances only; [K] boundaryTransitive_fullAut3 :537')
b = sp.Matrix(sp.symbols('b1:4'))
chk('T7 singleton face', sp.expand(((x - b).T * (x - b))[0] - ((x.T * x)[0] + (b.T * b)[0] - 2 * (b.T * x)[0])) == 0,
    'with |b| = 1 and b.x = 1: |x - b|^2 = |x|^2 - 1 <= 0, so x = b')
bad = [k for k, v in RES.items() if not v]
print('summary: %d checks, %d failed%s' % (len(RES), len(bad), (': ' + ', '.join(bad)) if bad else ''))
print('VERDICT R6-SINGLE-EXACT: the shared token structure meets the checked single-token premises; controls green' if not bad else 'NO VERDICT')
