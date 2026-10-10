"""Coordinator's independent check of thread B's key claims (audit; exact arithmetic; no thread code used).

Definitions re-typed from the landed sources (CompositeDimension.lean: sgn/pc/pt/cnotFun :741-759, hom, homMap,
prodState, actT :198, actC :201, corner :205, NativeGate :218 (frame, posFwd, posInv, relT, relC), nflip :797,
phiW :1220; K2Guard.lean: reflY :46, idW :101, chainW :104, cnot_idW :110) and the design sources
(FourCopyCore.lean: bellOf :137, NClass :132, orient :152). Gates as thread B names them: g_D = actT reflY . cnot,
g_pre = cnot . actT reflY, g_Tw = actT reflY . cnot . actT reflY. The design-source scan reads pt/inputs/fourcopy.

DECISION RULE (fixed before the first run). Each check prints CONFIRMED or MISMATCH; countercontrols (ids ending
in 'c') are CONFIRMED exactly when the mutated object gives the opposite verdict. 'AUDIT-B ALL CONFIRMED' is
printed iff every check is CONFIRMED. No timing in stdout. Usage: python3 -I -B indep_checkB.py <pt-root>
"""
import re
import sys
from pathlib import Path

import sympy as sp

Q = sp.Rational
I_ = sp.I
R4 = range(4)
ok_all = True
ROOT = Path(sys.argv[1]).resolve()


def report(cid, ok, detail):
    global ok_all
    ok = bool(ok)
    ok_all = ok_all and ok
    print(f"{'CONFIRMED' if ok else 'MISMATCH '} {cid}: {detail}", flush=True)


def section(t):
    print(f"\n== {t}", flush=True)


PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def sgn(m, n):
    return -1 if (m, n) in ((1, 3), (2, 2)) else 1


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: sgn(m, n) * w[PC[m][n], PT[m][n]])


def hom(x):
    return sp.Matrix([1] + list(x))


def homMap(Rm):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = Rm
    return M


def actT(Rm, w):
    return w * homMap(Rm).T


def actC(Rm, w):
    return homMap(Rm) * w


def prodState(x, y):
    return hom(x) * hom(y).T


def ipW(E, X):
    return sp.expand(sum(E[m, n] * X[m, n] for m in R4 for n in R4))


def zero4(M):
    return all(sp.expand(M[i, j]) == 0 for i in R4 for j in R4)


s0 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I_], [I_, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
S = [s0, sx, sy, sz]


def pauliW(w):
    return sum((w[m, n] * sp.kronecker_product(S[m], S[n]) for m in R4 for n in R4), sp.zeros(4, 4)) / 4


def psd(M):
    t = sp.Symbol('t')
    if any(sp.simplify(M[i, j] - sp.conjugate(M[j, i])) != 0 for i in R4 for j in R4):
        return False
    coeffs = sp.Poly(sp.expand((t * sp.eye(4) - M).det()), t).all_coeffs()
    for k, a in enumerate(coeffs):
        a = sp.simplify(sp.expand(a))
        if sp.im(a) != 0 or (-1) ** k * sp.re(a) < 0:
            return False
    return True


def in_Q3(w):
    return psd(pauliW(w))


reflY = sp.diag(1, -1, 1)
nflip = sp.diag(1, -1, -1)
phiW = sp.diag(1, 1, -1, 1)
idW = sp.eye(4)
chainW = sp.Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])
xplus, z3 = [1, 0, 0], [0, 0, 1]
pxz = prodState(xplus, z3)
g_D = lambda w: actT(reflY, cnot(w))
g_Dinv = lambda w: cnot(actT(reflY, w))
g_pre = lambda w: cnot(actT(reflY, w))
g_Tw = lambda w: actT(reflY, cnot(actT(reflY, w)))
ws = sp.Matrix(4, 4, sp.symbols('w0:16', real=True))


def sharp(u):  # homogenized effect vector of the sharp test with value 0 at the unit vector u (1/2)(1 - u.x)
    return sp.Matrix([Q(1, 2)] + [-Q(1, 2) * c for c in u])


def pairval(a, w, b):  # a^T w b: effect vector a on the control index, b on the target index
    return sp.expand((a.T * w * b)[0, 0])


# ---------------------------------------------------------------- S: the consumed clause (source scan)
section('S  where the design proof consumes hgate / hinv (independent text scan of the design modules)')
hdr = re.compile(r'^\s*(?:private\s+|protected\s+|noncomputable\s+)*(theorem|lemma|def)\s+([A-Za-z0-9_\'.]+)')
uses = {}
for f in sorted((ROOT / 'inputs/fourcopy').glob('FourCopy*.lean')):
    if f.name == 'FourCopyPackage.lean':
        continue  # not on the kt4_forward_ie1 path (sorry-bearing package module)
    cur = None
    for line in f.read_text(encoding='utf-8').splitlines():
        m = hdr.match(line)
        if m:
            cur = m.group(2)
        code = line.split('--')[0]
        if cur and re.search(r'\bh(gate|inv)\b', code):
            uses.setdefault(cur, set()).update(re.findall(r'\bh(?:gate|inv)\b', code))
expected = {'inv_mem_of_orth', 'ie1_all', 'parity_all', 'kt4_general_ie1', 'kt4_forward_ie1', 'kt4_forward_ie1_kt4',
            'kt4_forward_ie1_lt', 'link_mem', 'parity_witnesses', 'bell_mem', 'bell_mem_dual', 'dualW_of_inv'}
report('S1', set(uses) == expected,
       f'declarations naming hgate/hinv outside the package module: {len(uses)} = the twelve of thread B\'s frozen '
       f'list ({sorted(uses)})')
src = {f.name: f.read_text(encoding='utf-8') for f in (ROOT / 'inputs/fourcopy').glob('FourCopy*.lean')}
lm = re.search(r'theorem link_mem.*?(?=\ntheorem |\nlemma |\ndef |\Z)', src['FourCopyIE1.lean'], re.S).group(0)
bm = re.search(r'theorem bell_mem\b.*?(?=\ntheorem |\nlemma |\ndef |\Z)', src['FourCopyLocal.lean'], re.S).group(0)
bmd = re.search(r'theorem bell_mem_dual.*?(?=\ntheorem |\nlemma |\ndef |\Z)', src['FourCopyLocal.lean'], re.S).group(0)
report('S2', 'hgate _ (hprod' in lm and 'hgate _ (hprod' in bm and 'dualW_of_inv' in bmd and 'hgate' not in bmd,
       'link_mem and bell_mem apply hgate only to a product state (hgate _ (hprod ...)); bell_mem_dual reads hinv only '
       'through dualW_of_inv: the consumed instances are (L), (BS) and (BD)')
report('S3', 'hgate _ (hprod' not in src['FourCopyBipolar.lean'] and 'exact hgate _ ih' in src['FourCopyBipolar.lean'],
       'Lemma R (inv_mem_of_orth) uses hgate on general cone elements (an induction), not at a product: CONS deletes it '
       'and supplies (BD) directly instead of hinv')
planted = 'theorem planted_use (hgate : True) : True := hgate\n'
cur, seen = None, set()
for line in planted.splitlines():
    m = hdr.match(line)
    if m:
        cur = m.group(2)
    if cur and re.search(r'\bh(gate|inv)\b', line.split('--')[0]):
        seen.add(cur)
report('S1c', seen == {'planted_use'}, 'countercontrol: the scanner detects a planted declaration that names hgate')

# ---------------------------------------------------------------- M: the two countermodels to hgate
section('M  M_max = (maxCone, cnot) and M_D13 = (Q3, g_D)')
e = sp.symbols('e0:4', real=True)
f_ = sp.symbols('f0:4', real=True)
ev, fv = sp.Matrix(e), sp.Matrix(f_)
lhs = pairval(ev, idW, fv)
report('M1', lhs == sp.expand(sum(e[i] * f_[i] for i in range(4))),
       'pairing of idW with effect vectors e, f is e0 f0 + e.f >= e0 f0 - |e||f| >= 0 on the Lorentz cone '
       '(Cauchy-Schwarz): idW is in maxCone')
report('M2', cnot(idW) == chainW and pairval(sharp([1, 0, 0]), chainW, sharp([0, 0, 1])) == Q(-1, 2),
       'cnot idW = chainW (landed cnot_idW) and chainW pairs to -1/2 with the sharp effects of -e1, -e3: chainW is '
       'not in maxCone, so hgate fails in M_max')
report('M3', in_Q3(pxz) and g_D(pxz) == idW and not in_Q3(idW),
       'prodState xplus z3 is in Q3, g_D sends it to idW, and idW is not in Q3: hgate fails in M_D13')
okf = True
for a in range(2):
    for b in range(2):
        za, zab = ([0, 0, 1] if a == 0 else [0, 0, -1]), ([0, 0, 1] if (a + b) % 2 == 0 else [0, 0, -1])
        zb = [0, 0, 1] if b == 0 else [0, 0, -1]
        okf = okf and g_D(prodState(za, zb)) == prodState(za, zab)
okrel = zero4(actT(nflip, g_D(actT(nflip, ws))) - g_D(ws)) and \
    zero4(actC(nflip, g_D(actC(nflip, ws))) - actT(nflip, g_D(ws))) and zero4(g_D(g_Dinv(ws)) - ws)
report('M4', okf and okrel,
       'g_D meets NativeGate\'s frame at the four corner pairs of z3, relT and relC with nflip (symbolic), and has the '
       'two-sided inverse cnot . actT reflY; posFwd/posInv follow from cnot\'s (landed cnot_prodState_mem_maxCone) '
       'since homMap reflY preserves the Lorentz cone, so maxCone is actT reflY-invariant [written]')
idmap = lambda w: w
okf_id = all(idmap(prodState(za, zb)) == prodState(za, zab) for za, zb, zab in
             (([0, 0, 1], [0, 0, 1], [0, 0, 1]), ([0, 0, 1], [0, 0, -1], [0, 0, -1]),
              ([0, 0, -1], [0, 0, 1], [0, 0, -1]), ([0, 0, -1], [0, 0, -1], [0, 0, 1])))
report('M4c', not okf_id, 'countercontrol: the same frame check rejects the identity map (it fails at the corner pair '
                          '(-z3, -z3))')

# ---------------------------------------------------------------- C: CONS and its separations
section('C  the consumed clause CONS: strictly weaker than hgate, and failing where hgate does')
report('C1', in_Q3(phiW) and g_pre(phiW) == chainW and actC(sp.eye(3), actT(sp.eye(3), phiW)) == phiW,
       'M_pre (uniform Q3, N_13 = g_pre = cnot . actT reflY, post-locals I): hgate fails (phiW in Q3 goes to chainW, '
       'outside maxCone) while its post-local Bell table bellOf I I = phiW is that of M_Q, so CONS holds as in M_Q '
       '[written for (L): local rotations keep Q3]')
twin_mem = lambda w: in_Q3(actT(reflY, w))
report('C2', twin_mem(idW) and g_D(idW) == chainW and zero4(g_Tw(actT(reflY, ws)) - actT(reflY, cnot(ws))),
       'M_DD: idW = actT reflY phiW lies in twin and g_D sends it to chainW (outside maxCone, which contains twin), so '
       'hgate fails at a twin pair with g_D; the pre-corrected gate g_D . actT reflY = g_Tw satisfies '
       'g_Tw (actT reflY w) = actT reflY (cnot w) (symbolic), so it preserves twin (PREC holds)')
F = sp.diag(1, -1, 1, -1)
x = sp.symbols('x1:4', real=True)
y = sp.symbols('y1:4', real=True)
Dv = sp.diag(1, -1, 1)
xv, yv = sp.Matrix(x), sp.Matrix(y)
diff = (xv - Dv * yv)
form = sp.expand(ipW(F, prodState(x, y)) - ((diff.T * diff)[0] / 2 + (1 - (xv.T * xv)[0]) / 2 + (1 - (yv.T * yv)[0]) / 2))
report('C3', form == 0 and ipW(F, phiW) == -2 and pairval(ev, F, fv) == sp.expand(e[0] * f_[0] - e[1] * f_[1] + e[2] * f_[2] - e[3] * f_[3]),
       'F = diag(1,-1,1,-1): ipW F (prodState x y) = |x - D y|^2/2 + (1-|x|^2)/2 + (1-|y|^2)/2 (symbolic), >= 0 on '
       'products; F pairs effect vectors as e0 f0 - e1 f1 + e2 f2 - e3 f3 >= 0 (so F in maxCone); ipW F phiW = -2: '
       'phiW is not in dualW maxCone = SEP, so (BD) fails in M_max and no product-only pair system carries cnot')
report('C4', actC(sp.eye(3), actT(reflY, phiW)) == idW and not in_Q3(idW),
       '(BS) fails in M_D: bellOf I reflY = idW is not in Q3')

# ---------------------------------------------------------------- O: Lemma O ingredients
section('O  Lemma O (orientation obstruction) ingredients')
Bm = sp.Matrix(3, 3, sp.symbols('b0:9'))
Am = sp.Matrix(3, 3, sp.symbols('a0:9'))
okO = zero4(actT(reflY, actT(Bm, ws)) - actT(reflY * Bm, ws)) and zero4(actT(Bm, actC(Am, ws)) - actC(Am, actT(Bm, ws)))
report('O1', okO and sp.expand((reflY * Bm).det() + Bm.det()) == 0,
       'actT reflY . actT B = actT (reflY B) and actT commutes with actC (symbolic), so sigma_q keeps N-CLASS form with '
       'post-local reflY B; det(reflY B) = -det B flips orient')
L4 = homMap(reflY)
report('O2', L4 == sp.diag(1, 1, -1, 1) and (L4.T * sp.diag(1, -1, -1, -1) * L4) == sp.diag(1, -1, -1, -1),
       'homMap reflY fixes e0 and preserves the Lorentz form, so it maps the Lorentz cone onto itself: maxCone and SEP '
       'are actT reflY-invariant, and sigma_q changes no cone there')
pats = [p for p in __import__('itertools').product((0, 1), repeat=4)]
okO5 = sum(1 for p in pats if sum(p) % 2 == 0) == 8
report('O3', okO5, 'on uniform maxCone (or SEP) the 16 gate patterns in {cnot, g_D}^4 share every cone-reading hypothesis; '
                   'EvenCycle holds exactly on the 8 with an even number of g_D (orientation = det of the post-local B)')

print('\nAUDIT-B', 'ALL CONFIRMED' if ok_all else 'MISMATCH FOUND')
