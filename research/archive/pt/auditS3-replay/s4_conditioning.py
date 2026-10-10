#!/usr/bin/env python3
"""S3 nodes S3.2(c, d) -- orientation coherence and conditioning principles: which arguments of FCC must range over
the full cones and full duals (no-restriction), on the aligned-gate family.

Run: python3 -I -B s4_conditioning.py

Setting (stated scope): aligned gates N_p = gateOf tau_p (cnot for tau = 0, cnotTw for tau = 1), pairs in the order
01, 23, 02, 13. Gen_tau := the products prodState x y (x, y in the ball) and the gate images gateOf tau (prodState x y);
a "generated" argument of FCC is a table in cone(Gen_tau) of its pair (used as a state or, as the same table, as an
effect). A slot pattern of FCC fixes, for each of the four arguments of famI and of famII, whether it ranges over the
full cone / full dual of its pair (F) or over the generated tables (g).
  AG  all arguments generated;
  C1  states full, effects generated;   C2  states generated, effects full;
  ESC states generated, one effect generated, the effect on the conditioned pair full (entanglement swapping).

DECISION RULES (fixed before the first run; rules, not expected numbers):
  R1. One PASS/FAIL line per check; kinds as in s1-s3.
  R2. VERDICT only if all checks pass; else 'S4-CONDITIONING: FAILED -- <ids>' and exit 1.
  R3. Exact integer/rational arithmetic; no floating point, randomness or timing in stdout.
  R4. Searches scan fixed finite lists in a fixed order and report the first witness; no witness found is a FAIL of
      that check, not evidence of the universal statement.
"""
import sys
from itertools import product

import sympy as sp

Q = sp.Rational
R4 = range(4)
CHECKS = []


def chk(cid, name, ok, kind, detail=''):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}" + (f" -- {detail}" if detail else ''), flush=True)


def note(cid, text):
    print(f"NOTE [written] {cid}  -- {text}", flush=True)


def section(t):
    print()
    print(f"== {t}", flush=True)


def ex(v):
    return sp.expand(v)


def zero(v):
    return ex(v) == 0


def mzero(M):
    return all(ex(v) == 0 for v in M)


PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: (-1 if (m, n) in NEG else 1) * w[PC[m][n], PT[m][n]])


def hom(x):
    return sp.Matrix([1] + list(x))


def homMap(R):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = sp.Matrix(R)
    return M


def actC(R, w):
    return homMap(R) * w


def actT(R, w):
    return w * homMap(R).T


def prodState(x, y):
    return hom(x) * hom(y).T


def ipW(E, X):
    return sum(E[m, n] * X[m, n] for m in R4 for n in R4)


def fourVal(X, Y, E, F):
    return sum(X[a, b] * Y[c, d] * E[a, c] * F[b, d] for a, b, c, d in product(R4, repeat=4))


def g2(e, f, L, Lp):
    return sum(e[a, b] * f[c, d] * L[a, c] * Lp[b, d] for a, b, c, d in product(R4, repeat=4))


def symtab(nm):
    return sp.Matrix(4, 4, lambda m, n: sp.Symbol(f'{nm}{m}{n}', real=True))


reflY = sp.diag(1, -1, 1)
phiW = sp.diag(1, 1, -1, 1)
sing4 = sp.diag(1, -1, -1, -1)
Lp = actT(reflY, sing4)
xplus, z3 = [1, 0, 0], [0, 0, 1]
I3 = sp.eye(3)


def cnotTw(w):
    return actT(reflY, cnot(actT(reflY, w)))


def gateOf(t, w):
    return cnotTw(w) if t else cnot(w)


def chartR(ei, ej, w):
    out = w
    if ej:
        out = actT(reflY, out)
    if ei:
        out = actC(reflY, out)
    return out


PAIRS = [(0, 1), (2, 3), (0, 2), (1, 3)]   # p01, p23, p02, p13


def cob(eps):
    return tuple(eps[i] ^ eps[j] for i, j in PAIRS)


# ================================================================================================================
section('S1  token orientation coherence is the coboundary condition (exhaustive)')
cobs = {cob(e) for e in product((0, 1), repeat=4)}
even = {t for t in product((0, 1), repeat=4) if sum(t) % 2 == 0}
chk('O1', 'the coboundaries of the 16 token-bit assignments are exactly the 8 even twist patterns of the cycle '
    '0-1-3-2-0 (EvenCycle)', cobs == even and len(cobs) == 8, 'enumerate')
chk('O1c', 'countercontrol: the odd pattern (0,0,0,1) of M_tok is not a coboundary', (0, 0, 0, 1) not in cobs,
    'countercontrol')
W = symtab('w')
ok_tr = True
for ei, ej, t in product((0, 1), repeat=3):
    ok_tr = ok_tr and mzero(chartR(ei, ej, gateOf(t, chartR(ei, ej, W))) - gateOf(t ^ ei ^ ej, W))
chk('O2', 'chart transport of aligned gates: chartR ei ej . gateOf tau . chartR ei ej = gateOf (tau xor ei xor ej), '
    'all 8 cases, symbolic (the package\'s open chartR_gateOf, generalized)', ok_tr, 'enumerate')
x, y = [sp.Symbol(f'x{i}', real=True) for i in range(3)], [sp.Symbol(f'y{i}', real=True) for i in range(3)]
chk('O3', 'chartR ei ej (prodState x y) = prodState (reflY^ei x) (reflY^ej y), symbolic: charts carry products to '
    'products, so (O2) charts carry Gen_tau onto Gen_(tau xor ei xor ej)',
    all(mzero(chartR(ei, ej, prodState(x, y)) - prodState(list((reflY if ei else I3) * sp.Matrix(x)),
                                                           list((reflY if ej else I3) * sp.Matrix(y))))
        for ei, ej in product((0, 1), repeat=2)), 'enumerate')
Xs, Ys, Es, Fs = symtab('X'), symtab('Y'), symtab('E'), symtab('F')
ok_inv = True
for e in product((0, 1), repeat=4):
    ok_inv = ok_inv and zero(fourVal(chartR(e[0], e[1], Xs), chartR(e[2], e[3], Ys), chartR(e[0], e[2], Es),
                                     chartR(e[1], e[3], Fs)) - fourVal(Xs, Ys, Es, Fs))
chk('O4', 'per-token transport invariance of the four-copy contraction, all 16 token charts, symbolic', ok_inv,
    'enumerate')

# ================================================================================================================
section('S2  all-generated conditioning (AG) is exactly orientation coherence on the aligned family')
tau0 = (0, 0, 0, 1)
wit0 = (gateOf(0, prodState(xplus, z3)), gateOf(0, prodState(xplus, z3)), gateOf(0, prodState(xplus, z3)),
        gateOf(1, prodState([-1, 0, 0], [0, 0, -1])))
chk('G1', 'M_tok pattern (0,0,0,1): the generated tables phiW, phiW, phiW (cnot images) and L\' (a cnotTw image) give '
    'fourVal = -2', wit0[0] == phiW and wit0[3] == Lp and fourVal(*wit0) == -2, 'witness', f'value {fourVal(*wit0)}')
bad = []
for e in product((0, 1), repeat=4):
    t = tuple(tau0[k] ^ cob(e)[k] for k in range(4))
    tw = (chartR(e[0], e[1], wit0[0]), chartR(e[2], e[3], wit0[1]), chartR(e[0], e[2], wit0[2]),
          chartR(e[1], e[3], wit0[3]))
    pts = [(xplus, z3), (xplus, z3), (xplus, z3), ([-1, 0, 0], [0, 0, -1])]
    gen_ok = True
    for k, (i, j) in enumerate(PAIRS):
        a, b = pts[k]
        a2 = list((reflY if e[i] else I3) * sp.Matrix(a))
        b2 = list((reflY if e[j] else I3) * sp.Matrix(b))
        gen_ok = gen_ok and tw[k] == gateOf(t[k], prodState(a2, b2))
    if not (gen_ok and fourVal(*tw) == -2 and sum(t) % 2 == 1):
        bad.append((e, t))
odd_hit = {tuple(tau0[k] ^ cob(e)[k] for k in range(4)) for e in product((0, 1), repeat=4)}
chk('G2', 'for each of the 8 odd patterns (all 16 charts of the M_tok witness), the transported witness consists of '
    'gate images of products for that pattern\'s aligned gates and gives fourVal = -2', not bad
    and odd_hit == {t for t in product((0, 1), repeat=4) if sum(t) % 2 == 1}, 'enumerate', f'failures {bad}')
note('AG.W', 'even patterns: Gen_tau <= twistQ3(tau) (products are in Q3 n twin; cnot images in Q3 by s2 D1, D3; '
     'cnotTw images in twin by O2 with the chart), and for an even pattern tau = coboundary(eps) the cones '
     '(twistQ3 tau_p) are the chart images of uniform Q3 (O2, O3; chartR ei ej Q3 = twistQ3(ei xor ej)), where FCC '
     'holds (landed F2/F3 with Kronecker PSD), so FCC holds for them by O4 and AG holds a fortiori. Odd patterns: AG '
     'fails (G2). AG reads only the gates, not the cones: on the aligned family AG is exactly EvenCycle, i.e. token '
     'orientation coherence (O1). It holds for every uniform cone with cnot gates (K_gen, K_gen*, Q3).')

# ================================================================================================================
section('S3  one-sided no-restriction: C1 fails on K_gen*, C2 fails on K_gen; ESC holds on K_gen* and fails on K_gen')
E0 = sp.zeros(4, 4)
E0[0, 0], E0[1, 3], E0[2, 2] = 1, 1, -1
G = sp.Matrix([[1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0], [0, -1, 0, 0]])
chk('S1', 'C1 fails on uniform K_gen*: states E0, G (full: E0 in K_gen*, G in Q3 <= K_gen*), effects phiW, phiW '
    '(generated: cnot images) give fourVal = -1', fourVal(E0, G, phiW, phiW) == -1 and cnot(prodState(xplus, z3)) == phiW,
    'witness')
chk('S2', 'C2 fails on uniform K_gen: states phiW, phiW (generated), effects E0, G (full: in K_gen*) give fourVal = -1',
    fourVal(phiW, phiW, E0, G) == -1, 'witness')
note('S.W', 'C1 holds on uniform K_gen (states in K_gen <= Q3, generated effects in Q3 = dualW Q3, FCC for uniform '
     'Q3); C2 holds on uniform K_gen* (generated states in Q3, effects in dualW K_gen* = closure K_gen <= Q3). Both '
     'foils satisfy hcls, hadm, hcl, hgate and fail FCC (s2 G5, H1). So each one-sided conditioning principle is '
     'refuted as a route: C1 by K_gen, C2 by K_gen*.')
# ESC: X, Y generated on 01, 23; F generated on 13 (the measured pair); E full on 02 (the conditioned pair):
# fourVal X Y E F = ipW E (X F Y^T). Scan X, Y, F over cnot images of axis-point products and products.
AX = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
GEN0 = []
for a, b in product(AX, AX):
    GEN0.append(('prod', a, b, prodState(a, b)))
for a, b in product(AX, AX):
    GEN0.append(('cnot', a, b, cnot(prodState(a, b))))
GL = [[[int(M[i, j]) for j in R4] for i in R4] for (_, _, _, M) in GEN0]
E0l = [[int(E0[i, j]) for j in R4] for i in R4]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in R4) for j in R4] for i in R4]


def tr_(A):
    return [[A[j][i] for j in R4] for i in R4]


found = None
for ix, Xl in enumerate(GL):
    for iF, Fl in enumerate(GL):
        XF = mm(Xl, Fl)
        for iy, Yl in enumerate(GL):
            C = mm(XF, tr_(Yl))
            val = sum(E0l[i][j] * C[i][j] for i in R4 for j in R4)
            if val < 0:
                found = (ix, iF, iy, val)
                break
        if found:
            break
    if found:
        break
if found:
    ix, iF, iy, val = found
    Xw, Fw, Yw = GEN0[ix][3], GEN0[iF][3], GEN0[iy][3]
    chk('S3', 'ESC fails on uniform K_gen: generated X (01), Y (23), F (13) and the full effect E0 in K_gen* on the '
        'conditioned pair 02 give fourVal X Y E0 F = ipW E0 (X F Y^T) < 0', fourVal(Xw, Yw, E0, Fw) == val < 0,
        'witness', f'X = {GEN0[ix][:3]}, F = {GEN0[iF][:3]}, Y = {GEN0[iy][:3]}, value {val}')
else:
    chk('S3', 'ESC fails on uniform K_gen (no witness in the scanned list)', False, 'witness')
chk('S3c', 'countercontrol: with the full effect E0 replaced by the generated effect phiW no scanned triple is negative '
    '(all-generated holds for cnot gates)',
    all(sum(int(phiW[i, j]) * mm(mm(Xl, Fl), tr_(Yl))[i][j] for i in R4 for j in R4) >= 0
        for Xl in GL[36:48] for Fl in GL[36:48] for Yl in GL[36:48]), 'countercontrol')
note('ESC.W', 'ESC holds on uniform K_gen*: the conditioned table X F Y^T of generated tables lies in Q3 (entanglement '
     'swapping of quantum states, Kronecker PSD and the partial trace) and the full effects dualW K_gen* = closure '
     'K_gen lie in Q3 = dualW Q3. With S3, ESC excludes K_gen and M_tok (G1 is an ESC instance) but not K_gen*: '
     'refuted as a route by K_gen*.')

# ================================================================================================================
section('S4  the slot table (written)')
note('SLOT', 'on the aligned family: AG = EvenCycle (gate parity only; holds on K_gen, K_gen*, Q3; fails on M_tok). '
     'C1 (full states, generated effects): fails on K_gen* and M_tok, holds on K_gen. C2 (generated states, full '
     'effects): fails on K_gen and M_tok, holds on K_gen*. ESC: fails on K_gen and M_tok, holds on K_gen*. C1 and C2 '
     'together contain every FCC instance the design proof reads (link instances: famI with full target states and '
     'Bell effects; famII with rotated-link and Bell states and full target effects; FourCopyIE1 cross_rel, '
     'inv_*), so relative to the pair hypotheses C1 & C2 gives IE1 (design proof, [D]), hence {Q3, twin} cones '
     '(classification, [W + L]), hence EvenCycle by AG <= C1 and FCC by B2. A conditioning principle sufficient for '
     'FCC must therefore let full (no-restriction) arguments enter on BOTH the state side and the effect side.')

# ================================================================================================================
print()
failed = [c[0] for c in CHECKS if not c[2]]
print('kinds: ' + ', '.join(f"{k} {sum(1 for c in CHECKS if c[1] == k)}"
                            for k in ('identity', 'witness', 'enumerate', 'countercontrol')), flush=True)
if failed:
    print(f"S4-CONDITIONING: FAILED -- {len(failed)} of {len(CHECKS)}: {', '.join(failed)}", flush=True)
    sys.exit(1)
print(f'VERDICT S4-CONDITIONING-EXACT -- {len(CHECKS)} checks', flush=True)
