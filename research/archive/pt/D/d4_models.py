#!/usr/bin/env python3
"""Thread D, certified script d4 -- consistency of T1 with the gates of the landed models (RESULT.md section 3), and
the relT clause of the CtrlGate classification (RESULT.md D1.4), on instances.

The landed models of result.md Q1-MAP use the gates cnot (M_Q, M_cl, M_max, M_refl, M_class, M_mix, M_int, M_tokC),
actT reflY . cnot (M_D at pair 13), actT reflY . cnot . actT reflY = cnotTw (M_tok at pair 13) and id (M_id).

DECISION RULES (fixed before the first run):
  M1  each non-identity model gate must satisfy the frame at z3 exactly and be of N-CLASS form with explicit
      orthogonal locals (exact identity on a symbolic table): consistent with T1 (no landed gate meets the gate premises
      and fails N-CLASS);
  M2  the identity gate (M_id) must FAIL the frame at z3 (it does not meet the candidate), consistent with T1;
  M3  instances of the CtrlGate classification: G = cnot . actT R0 satisfies the frame and relC for R0 = Rot_z(3/5, 4/5)
      and for R0 = diag(1, -1, 1); relT must hold for diag(1, -1, 1) (which commutes with nflip) and must FAIL for
      Rot_z(3/5, 4/5) (which does not commute with nflip);
  CC  countercontrol: actC(Rot_z(3/5, 4/5)) . cnot satisfies the frame but FAILS relC (so M3's relC checks can fail).
A VERDICT line prints only if every check passes and the countercontrol behaves as stated.
Exact arithmetic only (sympy, rationals). No floating point, no randomness, no timing in stdout.
"""
import sys
import sympy as sp

CHECKS = []


def chk(cid, name, ok, kind):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}", flush=True)


R4 = range(4)
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}


def cnot(w):
    return sp.Matrix(4, 4, lambda m, k: (-1 if (m, k) in NEG else 1) * w[PC[m][k], PT[m][k]])


def homMap(R):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = sp.Matrix(R)
    return M


def actC(R, w):
    return homMap(R) * w


def actT(R, w):
    return w * homMap(R).T


def hom(x):
    return sp.Matrix([1] + list(x))


def prodState(x, y):
    return hom(x) * hom(y).T


def zero_mat(M):
    return all(sp.simplify(v) == 0 for v in M)


I3 = sp.eye(3)
NFLIP = sp.diag(1, -1, -1)
REFLY = sp.diag(1, -1, 1)
RZ = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5), 0], [sp.Rational(4, 5), sp.Rational(3, 5), 0], [0, 0, 1]])
z3 = [0, 0, 1]
W = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'w{i}{j}', real=True))


def corner(c):
    return z3 if c % 2 == 0 else [0, 0, -1]


def frame(G):
    return all(zero_mat(G(prodState(corner(a), corner(b))) - prodState(corner(a), corner(a + b)))
               for a in (0, 1) for b in (0, 1))


def nclass(G, A, B, Ap, Bp):
    orth = all(sp.Matrix(M).T * sp.Matrix(M) == I3 for M in (A, B, Ap, Bp))
    return orth and zero_mat(G(W) - actC(A, actT(B, cnot(actC(Ap, actT(Bp, W))))))


gates = {
    'cnot (M_Q, M_cl, M_max, M_refl, M_class, M_mix, M_int, M_tokC)': (lambda w: cnot(w), (I3, I3, I3, I3)),
    'actT reflY . cnot (M_D at 13)': (lambda w: actT(REFLY, cnot(w)), (I3, REFLY, I3, I3)),
    'actT reflY . cnot . actT reflY = cnotTw (M_tok at 13)': (lambda w: actT(REFLY, cnot(actT(REFLY, w))),
                                                             (I3, REFLY, I3, REFLY)),
}
print('== M1  the non-identity landed gates')
for i, (name, (G, locs)) in enumerate(gates.items()):
    chk(f'M1.{i}', f'{name}: frame at z3 and N-CLASS with locals (A, B, A\', B\') = '
        f'{[str(sp.Matrix(M).diagonal().tolist()[0]) for M in locs]}', frame(G) and nclass(G, *locs), 'identity')

print()
print('== M2  the identity gate (M_id)')
chk('M2', 'id fails the frame at z3 (prodState(-z3, z3) is not mapped to prodState(-z3, -z3))',
    not frame(lambda w: w), 'witness')

print()
print('== M3  relT in the CtrlGate classification (instances)')
for nm, R0, expect_relT in (('Rot_z(3/5,4/5)', RZ, False), ('diag(1,-1,1)', REFLY, True)):
    G = (lambda R: (lambda w: cnot(actT(R, w))))(R0)
    relC = zero_mat(actC(NFLIP, G(actC(NFLIP, W))) - actT(NFLIP, G(W)))
    relT = zero_mat(actT(NFLIP, G(actT(NFLIP, W))) - G(W))
    commutes = R0 * NFLIP == NFLIP * R0
    chk(f'M3.{nm}', f'cnot . actT {nm}: frame {frame(G)}, relC {relC}, relT {relT}; R0 commutes with nflip: {commutes}',
        frame(G) and relC and relT == expect_relT and commutes == expect_relT, 'identity')

print()
print('== CC  countercontrol')
Gc = lambda w: actC(RZ, cnot(w))
chk('CC', 'countercontrol: actC(Rot_z(3/5,4/5)) . cnot has the frame and FAILS relC',
    frame(Gc) and not zero_mat(actC(NFLIP, Gc(actC(NFLIP, W))) - actT(NFLIP, Gc(W))), 'countercontrol')

print()
fails = [c for c, k, ok in CHECKS if not ok]
print(f'd4_models: {len(CHECKS)} checks, {len(fails)} failed')
if not fails:
    print('VERDICT D4-MODELS-CONSISTENT: every non-identity landed model gate has the frame and N-CLASS form; the '
          'identity gate fails the frame; relT for cnot . actT R0 holds exactly when R0 commutes with nflip on the '
          'two instances')
    sys.exit(0)
print('NO VERDICT: failed checks ' + ', '.join(fails))
sys.exit(1)
