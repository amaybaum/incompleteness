#!/usr/bin/env python3
"""Thread B (PAIR-ACT), script b1_consumed -- the clause the design proof of kt4_forward_ie1 consumes from hgate.

Research only.  Exact arithmetic (sympy Rationals and rational functions); no floating point, no randomness, no
time-dependence in stdout.  Run as:  python3 -I -B b1_consumed.py <pt-root>
where <pt-root> is the directory holding base/ and inputs/.  The script only reads files.

WHAT IT CHECKS
  S0  [source]   transcription of the landed tables (sgn, pc, pt, phiW, idW, chainW, reflY) and of the design
                 rotation matrices (Rz, Rx) from the Lean sources.
  S1  [source]   every occurrence of the identifiers hgate and hinv in the design modules on the proof path of
                 kt4_forward_ie1 (FourCopyHeadline, IE1, Local, Bipolar, Parity, Bridge, Core, Tables, Euler, Defs),
                 grouped by declaration, against the frozen expected use list below; FourCopyPackage (not imported by
                 FourCopyHeadline) is checked to be off the path.
  S2  [identity] the exact identities that rewrite each consumed instance of hgate / hinv as a statement about
                 tables:  (L) the link family, (BS) the Bell state, (BD) the Bell effect.
  S3  [identity] the identities behind "SECT => OQ1 => CONS": ipW-adjointness of the token actions and of cnot,
                 pairVal a b w = ipW (a b^T) w, and N(sharp product) = 1/4 N(product).

FROZEN EXPECTED USE LIST (from reading the design modules before the first run; S1 compares against it)
  FourCopyHeadline.ie1_all            hgate: binder + 1 use (link_mem)                      hinv: none
  FourCopyHeadline.parity_all         hgate: binder + 4 uses (parity_witnesses)             hinv: binder + 4 uses
  FourCopyHeadline.kt4_general_ie1    hgate: binder + 4 uses (inv_mem_of_orth, bell_mem, ie1_all, parity_all)
                                      hinv: have + 2 uses (bell_mem_dual, parity_all)
  FourCopyHeadline.kt4_forward_ie1    hgate: binder + 1 use (kt4_general_ie1)
  FourCopyHeadline.kt4_forward_ie1_kt4, kt4_forward_ie1_lt   hgate: binder + 1 use each (kt4_forward_ie1)
  FourCopyIE1.link_mem                hgate: binder + 1 use (applied to a product state)
  FourCopyIE1.parity_witnesses        hgate: binder + 1 use (bell_mem); hinv: binder + 1 use (bell_mem_dual)
  FourCopyLocal.bell_mem              hgate: binder + 1 use (applied to a product state)
  FourCopyLocal.bell_mem_dual         hinv: binder + 1 use (dualW_of_inv)
  FourCopyBipolar.inv_mem_of_orth     hgate: binder + 1 use (inside the orbit induction)
  FourCopyParity.dualW_of_inv         hinv: binder + 1 use
  (header comments, docstrings and FourCopyPackage are not on the proof path and are excluded / checked separately)

DECISION RULE (fixed before the first run)
  * Each check prints PASS or FAIL.  A check passes iff its stated exact equality holds (identities: the difference
    expands/cancels to 0; sources: the parsed text equals the transcription / the expected use list exactly).
  * Countercontrols (kind 'countercontrol') are mutated objects that must give the opposite verdict; such a check
    PASSES iff the mutated object FAILS the identity.
  * The VERDICT lines are printed only if every check passed.  Their text is generated from the measured results:
    the consumed clause is stated as the list of instances whose identities passed.  Otherwise the script prints
    'b1_consumed: NO VERDICT' and exits 1.
"""
import re
import sys
from itertools import product
from pathlib import Path

import sympy as sp

Q = sp.Rational
R4 = range(4)
CHECKS = []


def chk(cid, name, ok, kind, detail=''):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}" + (f" -- {detail}" if detail else ''), flush=True)


def section(t):
    print()
    print(f'== {t}', flush=True)


def mzero(M):
    return all(sp.cancel(sp.together(v)) == 0 for v in M)


if len(sys.argv) != 2:
    print('usage: b1_consumed.py <pt-root>')
    sys.exit(2)
ROOT = Path(sys.argv[1]).resolve()
LEAN_BASE = ROOT / 'base' / 'verification' / 'lean-mathlib' / 'OIBridge'
DESIGN = ROOT / 'inputs' / 'fourcopy'

# ---------------------------------------------------------------------------------------------------------------
# own transcription of the landed conventions (checked in S0)
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}


def sgn(m, n):
    return -1 if (m, n) in NEG else 1


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: sgn(m, n) * w[PC[m][n], PT[m][n]])


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


def pairVal(a, b, w):
    return (sp.Matrix(a).T * w * sp.Matrix(b))[0, 0]


def sharpVec(b):
    return sp.Matrix([Q(1, 2)] + [Q(1, 2) * v for v in b])


def tens(a, b):
    return sp.Matrix(a) * sp.Matrix(b).T


phiW = sp.diag(1, 1, -1, 1)
idW = sp.eye(4)
chainW = sp.Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])
reflY = sp.diag(1, -1, 1)
I3 = sp.eye(3)
xplus = [1, 0, 0]
z3 = [0, 0, 1]


def Rz(c, s):
    return sp.Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])


def Rx(c, s):
    return sp.Matrix([[1, 0, 0], [0, c, -s], [0, s, c]])


def symtab(nm):
    return sp.Matrix(4, 4, lambda m, n: sp.Symbol(f'{nm}{m}{n}', real=True))


def symmat3(nm):
    return sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'{nm}{i}{j}', real=True))


def symvec(nm, k):
    return [sp.Symbol(f'{nm}{i}', real=True) for i in range(k)]


# ===============================================================================================================
section('S0  transcription of the landed tables and of the design rotation matrices')
CD = (LEAN_BASE / 'CompositeDimension.lean').read_text(encoding='utf-8')
KG = (LEAN_BASE / 'K2Guard.lean').read_text(encoding='utf-8')
EU = (DESIGN / 'FourCopyEuler.lean').read_text(encoding='utf-8')

msg = re.search(r'^def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) '
                r'then -1 else 1$', CD, re.M)
neg_src = {(int(msg.group(1)), int(msg.group(2))), (int(msg.group(3)), int(msg.group(4)))} if msg else None
chk('S0.sgn', 'landed sgn is -1 exactly at (1,3) and (2,2)', neg_src == NEG, 'source')


def lean_table(nm):
    mm = re.search(rf'^def {nm} : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n){{4}})', CD, re.M)
    if not mm:
        return None
    T = [[None] * 4 for _ in R4]
    for a, b, v in re.findall(r'\|\s*(\d),\s*(\d)\s*=>\s*(\d)', mm.group(1)):
        T[int(a)][int(b)] = int(v)
    return T


chk('S0.pc', 'landed pc table', lean_table('pc') == PC, 'source')
chk('S0.pt', 'landed pt table', lean_table('pt') == PT, 'source')
chk('S0.phiW', 'landed phiW = diag(1,1,-1,1)',
    'def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0' in CD, 'source')


def lean_w3(nm):
    mm = re.search(rf'^def {nm} : W 3 := !\[(.*)\]$', KG, re.M)
    if not mm:
        return None
    rows = re.findall(r'!\[([^\]]*)\]', mm.group(1))
    return sp.Matrix([[int(v) for v in r.split(',')] for r in rows])


chk('S0.idW', 'landed idW = identity table', lean_w3('idW') == idW, 'source')
chk('S0.chainW', 'landed chainW', lean_w3('chainW') == chainW, 'source')
chk('S0.reflY', 'landed reflY = diag(1,-1,1)', 'toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i' in KG,
    'source')
chk('S0.Rz', 'design Rz t = [[cos,-sin,0],[sin,cos,0],[0,0,1]]',
    '!![Real.cos t, -Real.sin t, 0; Real.sin t, Real.cos t, 0; 0, 0, 1]' in EU, 'source')
chk('S0.Rx', 'design Rx t = [[1,0,0],[0,cos,-sin],[0,sin,cos]]',
    '!![1, 0, 0; 0, Real.cos t, -Real.sin t; 0, Real.sin t, Real.cos t]' in EU, 'source')
chk('S0.sharp', 'landed sharpVec convention: sharpVec ![-1,0,0] = ![1/2,-1/2,0,0]',
    'sharpVec (![-1, 0, 0] : Fin 3 → ℝ) = ![1 / 2, -1 / 2, 0, 0]' in KG
    and list(sharpVec([-1, 0, 0])) == [Q(1, 2), Q(-1, 2), 0, 0], 'source')

# ===============================================================================================================
section('S1  every use of hgate / hinv on the proof path of kt4_forward_ie1')

PATH_FILES = ['FourCopyHeadline', 'FourCopyIE1', 'FourCopyLocal', 'FourCopyBipolar', 'FourCopyParity',
              'FourCopyBridge', 'FourCopyCore', 'FourCopyTables', 'FourCopyEuler', 'FourCopyDefs']
DECL_RE = re.compile(r'^(?:theorem|lemma|def|abbrev|structure|noncomputable def)\s+([A-Za-z0-9_.\']+)', re.M)


def strip_comments(src):
    src = re.sub(r'/-.*?-/', lambda m: '\n' * m.group(0).count('\n'), src, flags=re.S)
    return re.sub(r'--[^\n]*', '', src)


def decl_uses(fname):
    src = strip_comments((DESIGN / f'{fname}.lean').read_text(encoding='utf-8'))
    starts = [(m.start(), m.group(1)) for m in DECL_RE.finditer(src)]
    starts.append((len(src), None))
    out = {}
    for (s, nm), (e, _) in zip(starts, starts[1:]):
        body = src[s:e]
        g = len(re.findall(r'(?<![A-Za-z0-9_\'])hgate(?![A-Za-z0-9_\'])', body))
        i = len(re.findall(r'(?<![A-Za-z0-9_\'])hinv(?![A-Za-z0-9_\'])', body))
        if g or i:
            out[f'{fname}.{nm}'] = (g, i)
    return out


EXPECTED = {
    'FourCopyHeadline.ie1_all': (2, 0),
    'FourCopyHeadline.parity_all': (5, 5),
    'FourCopyHeadline.kt4_general_ie1': (5, 3),
    'FourCopyHeadline.kt4_forward_ie1': (2, 0),
    'FourCopyHeadline.kt4_forward_ie1_kt4': (2, 0),
    'FourCopyHeadline.kt4_forward_ie1_lt': (2, 0),
    'FourCopyIE1.link_mem': (2, 0),
    'FourCopyIE1.parity_witnesses': (2, 2),
    'FourCopyLocal.bell_mem': (2, 0),
    'FourCopyLocal.bell_mem_dual': (0, 2),
    'FourCopyBipolar.inv_mem_of_orth': (2, 0),
    'FourCopyParity.dualW_of_inv': (0, 2),
    # gate_sharp_mem_dualW and kt4_parity_aligned use hG / g01..g13, not hgate: not on kt4_forward_ie1's path
}
found = {}
for f in PATH_FILES:
    found.update(decl_uses(f))
chk('S1.uses', 'the hgate/hinv occurrence counts per declaration on the path equal the frozen expected list',
    found == EXPECTED, 'source', '; '.join(f'{k}={v}' for k, v in sorted(found.items())))
HL = strip_comments((DESIGN / 'FourCopyHeadline.lean').read_text(encoding='utf-8'))
imports = re.findall(r'^import (\S+)', (DESIGN / 'FourCopyHeadline.lean').read_text(encoding='utf-8'), re.M)
chk('S1.offpath', 'FourCopyHeadline imports FourCopyIE1, Bridge, Local, Bipolar and not FourCopyPackage',
    set(imports) == {'OIBridge.FourCopyIE1', 'OIBridge.FourCopyBridge', 'OIBridge.FourCopyLocal',
                     'OIBridge.FourCopyBipolar'}, 'source', ', '.join(imports))
# the consuming lines, verbatim
need = [
    ('S1.L', 'link_mem (hcls p) (hprod p) (hgate p) a b', HL),
    ('S1.R', 'inv_mem_of_orth (hcls p).ipW_map (hcl p) (hgate p)', HL),
    ('S1.BS', 'bell_mem (hcls p) (hadm p).1.1 (hgate p)', HL),
    ('S1.BD', 'bell_mem_dual (hcls p) (hadm p).1.2 (hinv p)', HL),
]
for cid, txt, src in need:
    chk(cid, f'kt4_general_ie1 / ie1_all contain the consuming call `{txt}`', txt in src, 'source')
IE = strip_comments((DESIGN / 'FourCopyIE1.lean').read_text(encoding='utf-8'))
pw = IE[IE.find('theorem parity_witnesses'):]
chk('S1.PW', 'parity_witnesses reads hgate only through bell_mem and hinv only through bell_mem_dual',
    'have hbs : bellOf A B ∈ K := bell_mem hcls hprod hgate' in pw
    and 'have hbe : bellOf A B ∈ dualW K := bell_mem_dual hcls hK hinv' in pw, 'source')
lm = IE[IE.find('theorem link_mem'):IE.find('theorem inv_left_ctrl')]
chk('S1.LM', 'link_mem applies hgate to the product state prodState (trn A\' (rot3 a xplus)) (trn B\' (rotX b z3))',
    'hgate _ (hprod _ (orth_mem_eball (isOrth3_trn hcls.2.2.1) (rot3_xplus_mem a)) _' in lm
    and '(orth_mem_eball (isOrth3_trn hcls.2.2.2.1) (rotX_z3_mem b)))' in lm, 'source')
LO = strip_comments((DESIGN / 'FourCopyLocal.lean').read_text(encoding='utf-8'))
bm = LO[LO.find('theorem bell_mem '):LO.find('theorem bell_mem_dual')]
chk('S1.BM', 'bell_mem applies hgate to the product state given by NClass.bell_state',
    'obtain ⟨x, hx, y, hy, hxy⟩ := hcls.bell_state' in bm and 'exact hgate _ (hprod x hx y hy)' in bm, 'source')
bd = LO[LO.find('theorem bell_mem_dual'):]
chk('S1.BDM', 'bell_mem_dual reads hinv only to put the gate image of a sharp product in dualW K (dualW_of_inv)',
    'have h := dualW_of_inv hcls.ipW_map hinv (sharp_mem_dualW hK hb hc)' in bd, 'source')

# ===============================================================================================================
section('S2  the consumed instances, rewritten as statements about tables')

m1, m2 = sp.symbols('m1 m2', real=True)
c1, s1 = (1 - m1 ** 2) / (1 + m1 ** 2), 2 * m1 / (1 + m1 ** 2)
c2, s2 = (1 - m2 ** 2) / (1 + m2 ** 2), 2 * m2 / (1 + m2 ** 2)
RZ, RX = Rz(c1, s1), Rx(c2, s2)
chk('S2.rot', 'Rz(m1), Rx(m2) (rational parametrization of the angles) are rotations: R^T R = I, det R = 1',
    mzero(RZ.T * RZ - I3) and sp.cancel(sp.together(RZ.det() - 1)) == 0 and mzero(RX.T * RX - I3)
    and sp.cancel(sp.together(RX.det() - 1)) == 0, 'identity')
xa = list(RZ * sp.Matrix(xplus))
yb = list(RX * sp.Matrix(z3))
LINK = actC(RZ * RX, phiW)
chk('S2.G7ii', 'cnot (prodState (Rz xplus) (Rx z3)) = actC (Rz Rx) phiW (design G7(ii)), symbolic angles',
    mzero(cnot(prodState(xa, yb)) - LINK), 'identity')
chk('S2.G7iii', 'actC (Rz Rx) phiW = actT (Rx Rz) phiW (design G7(iii)), symbolic angles',
    mzero(LINK - actT(RX * RZ, phiW)), 'identity')
A, B, Ap, Bp = symmat3('A'), symmat3('B'), symmat3('P'), symmat3('S')
u, v = symvec('u', 3), symvec('v', 3)
chk('S2.loc', 'actC M (prodState u v) = prodState (M u) v and actT M (prodState u v) = prodState u (M v), symbolic',
    mzero(actC(A, prodState(u, v)) - prodState(list(A * sp.Matrix(u)), v))
    and mzero(actT(A, prodState(u, v)) - prodState(u, list(A * sp.Matrix(v)))), 'identity')


def nclass(Am, Bm, Apm, Bpm, w):
    return actC(Am, actT(Bm, cnot(actC(Apm, actT(Bpm, w)))))


chk('S2.L', '(L): N (prodState u v) = actC A actT B cnot (prodState (A\' u) (B\' v)) for N-CLASS N, symbolic; with '
    'u = A\'^T Rz xplus, v = B\'^T Rx z3 and A\' A\'^T = B\' B\'^T = I this is actC (A Rz Rx) (actT B phiW)',
    mzero(nclass(A, B, Ap, Bp, prodState(u, v))
          - actC(A, actT(B, cnot(prodState(list(Ap * sp.Matrix(u)), list(Bp * sp.Matrix(v)))))))
    and mzero(actC(A, actT(B, LINK)) - actC(A * RZ * RX, actT(B, phiW))), 'identity')
chk('S2.BS', '(BS): at m1 = m2 = 0 the link table is bellOf A B = actC A (actT B phiW)',
    mzero((actC(A * RZ * RX, actT(B, phiW))).subs({m1: 0, m2: 0}) - actC(A, actT(B, phiW))), 'identity')
chk('S2.BE', '(BD): tens (sharpVec u) (sharpVec v) = 1/4 prodState u v, symbolic, so the gate image of the sharp '
    'product consumed by bell_mem_dual is 1/4 bellOf A B',
    mzero(tens(sharpVec(u), sharpVec(v)) - Q(1, 4) * prodState(u, v)), 'identity')
chk('S2.Bc', 'countercontrol: with phiW replaced by idW, (BS) at the M_D post-local B = reflY is not the M_Q Bell '
    'table (the post-local is read: actT reflY phiW = idW differs from phiW)',
    actT(reflY, phiW) == idW and idW != phiW, 'countercontrol')

# ===============================================================================================================
section('S3  identities behind SECT => OQ1 => CONS (effect side through the inverse gate)')
E, X = symtab('E'), symtab('X')
chk('S3.adjC', 'ipW E (actC M X) = ipW (actC M^T E) X, symbolic M (design G3a)',
    sp.expand(ipW(E, actC(A, X)) - ipW(actC(A.T, E), X)) == 0, 'identity')
chk('S3.adjT', 'ipW E (actT M X) = ipW (actT M^T E) X, symbolic M (design G3b)',
    sp.expand(ipW(E, actT(A, X)) - ipW(actT(A.T, E), X)) == 0, 'identity')
chk('S3.adjN', 'ipW (cnot E) X = ipW E (cnot X) and cnot (cnot X) = X, symbolic (cnot is ipW-self-adjoint)',
    sp.expand(ipW(cnot(E), X) - ipW(E, cnot(X))) == 0 and mzero(cnot(cnot(X)) - X), 'identity')
a4, b4 = symvec('a', 4), symvec('b', 4)
chk('S3.pv', 'pairVal a b w = ipW (a b^T) w, symbolic (a product effect is the table a b^T)',
    sp.expand(pairVal(a4, b4, X) - ipW(tens(a4, b4), X)) == 0, 'identity')
chk('S3.cc', 'countercontrol: ipW E (actC M X) = ipW (actC M E) X fails for a non-symmetric M',
    sp.expand(ipW(E, actC(sp.Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]]), X))
              - ipW(actC(sp.Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]]), E), X)) != 0, 'countercontrol')

# ===============================================================================================================
print()
kinds = ('identity', 'source', 'countercontrol')
print('kinds: ' + ', '.join(f"{k} {sum(1 for c in CHECKS if c[1] == k)}" for k in kinds), flush=True)
failed = [c[0] for c in CHECKS if not c[2]]
if failed:
    print(f"b1_consumed: NO VERDICT -- {len(failed)} of {len(CHECKS)} checks failed: {', '.join(failed)}")
    sys.exit(1)
inst = []
if all(c[2] for c in CHECKS if c[0] in ('S1.L', 'S1.LM', 'S2.G7ii', 'S2.L')):
    inst.append('(L) actC (A_p o rotWord a b) (actT B_p phiW) in K_p for all a, b [link_mem]')
if all(c[2] for c in CHECKS if c[0] in ('S1.BS', 'S1.BM', 'S2.BS')):
    inst.append('(BS) bellOf A_p B_p in K_p [bell_mem; the instance a = b = 0 of (L)]')
if all(c[2] for c in CHECKS if c[0] in ('S1.BD', 'S1.BDM', 'S1.R', 'S2.BE')):
    inst.append('(BD) bellOf A_p B_p in dualW K_p [bell_mem_dual; hinv enters only here, via Lemma R]')
print('VERDICT B1-CONSUMED: on the proof path of kt4_forward_ie1, hgate and hinv are consumed only at:')
for s in inst:
    print('VERDICT B1-CONSUMED:   ' + s)
print(f'b1_consumed: OK -- {len(CHECKS)} checks')
