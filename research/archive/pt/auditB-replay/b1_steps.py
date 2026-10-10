#!/usr/bin/env python3
"""Thread B (PAIR-ACT), script b1_steps -- step-by-step support for the sufficiency of the weaker gate clauses.

Research only.  Exact arithmetic only (sympy); no floating point, no randomness, no time-dependence in stdout.
Run as:  python3 -I -B b1_steps.py <pt-root> <B1_UNBUILT.lean>

WHAT THIS SCRIPT ESTABLISHES, AND WHAT IT DOES NOT
  B1_UNBUILT.lean is UNBUILT (no Lean toolchain): it is not a kernel proof.  This script checks, exactly, that each of
  its '_cons' declarations is the corresponding design declaration with ONLY the lines that consumed hgate or hinv
  changed (part A, [source]), that the file has no sorry / admit / axiom and uses hgate only in the two lemmas that
  derive the weakenings FROM hgate (part B, [source]), that every lemma name it calls exists in the design or landed
  sources (part C, [source]), and the table-level identities behind the few new lemmas (part D, [identity]).  The
  sufficiency claims themselves are written arguments [W] whose ingredients are design-run lemmas [D] and these checks.

FROZEN EXPECTED DIFFS (fixed before the first run; part A compares against them)
  A1 ie1_all -> ie1_all_cons
     binders removed: hprod, hgate      binders added: hcons
     body: the one line 'link_mem (hcls p) (hprod p) (hgate p) a b' is replaced by
           '⟨(hcons p).link a b, link_target_of_ctrl ((hcons p).link a b)⟩'; every other body line identical, in order
  A2 parity_witnesses -> parity_witnesses_cons
     binders removed: hprod, hgate, hinv   binders added: hbs0, hbe0
     body: 'have hbs : bellOf A B ∈ K := bell_mem hcls hprod hgate' -> 'have hbs : bellOf A B ∈ K := hbs0'
           'have hbe : bellOf A B ∈ dualW K := bell_mem_dual hcls hK hinv' -> 'have hbe : bellOf A B ∈ dualW K := hbe0'
  A3 parity_all -> parity_all_cons
     binders removed: hgate, hinv   binders added: hbs, hbe
     body: the four 'parity_witnesses (hcls .pXX) (hadm .pXX).1.2 (hadm .pXX).1.1 (hgate .pXX) (hinv .pXX)' lines ->
           'parity_witnesses_cons (hcls .pXX) (hadm .pXX).1.2 (hbs .pXX) (hbe .pXX)'
  A4 kt4_general_ie1 -> kt4_general_ie1_cons
     binders removed: hgate   binders added: hcons
     body: the two lines of 'have hinv ... inv_mem_of_orth ...' deleted (Lemma R not used); the bell_mem / bell_mem_dual
           lines replaced by (hcons p).bs / (hcons p).bd; the ie1_all and parity_all calls replaced by their _cons forms
  A5 kt4_forward_ie1 -> kt4_forward_ie1_cons
     binders removed: hgate   binders added: hcons;  body: the kt4_general_ie1 call -> kt4_general_ie1_cons
  A6 link_mem (control half) -> cons_of_oq1.link :  'hgate _ (hprod _ X _ Y)' -> 'h.1 _ X _ Y'; rw/exact lines identical
  A7 bell_mem -> cons_of_oq1.bs :  'exact hgate _ (hprod x hx y hy)' -> 'exact h.1 x hx y hy'; other lines identical
  A8 bell_mem_dual -> oq1_of_sect : 'dualW_of_inv hcls.ipW_map hinv (sharp_mem_dualW hK hb hc)' ->
     'gate_sharp_mem_dualW_of_inv_pos hcls.ipW_map h.2 hb hc'; the scaling lines identical (h renamed hm)
  A9 sharp_mem_dualW -> gate_sharp_mem_dualW_of_inv_pos : 'exact hK hX …' -> 'exact hpos X hX …' after one rewrite
     through the gate (h1); the ipW_tens / prodEffVal_sharp rewrite identical

DECISION RULE (fixed before the first run)
  Each check prints PASS or FAIL; a check passes iff its exact comparison or identity holds.  Countercontrols must
  FAIL their comparison (a mutated copy must be detected).  VERDICT lines print only if every check passed; their text
  is generated from the passed checks.  Otherwise 'b1_steps: NO VERDICT' and exit 1.
"""
import difflib
import re
import sys
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


if len(sys.argv) != 3:
    print('usage: b1_steps.py <pt-root> <B1_UNBUILT.lean>')
    sys.exit(2)
ROOT = Path(sys.argv[1]).resolve()
UNB = Path(sys.argv[2]).resolve()
DESIGN = ROOT / 'inputs' / 'fourcopy'
LANDED = ROOT / 'base' / 'verification' / 'lean-mathlib' / 'OIBridge'


def strip_comments(src):
    src = re.sub(r'/-.*?-/', lambda m: '\n' * m.group(0).count('\n'), src, flags=re.S)
    return re.sub(r'--[^\n]*', '', src)


TOP = re.compile(r'^(?:theorem|lemma|def|abbrev|structure|noncomputable def|end|#print|set_option|/-)', re.M)


def get_decl(src, name):
    m = re.search(rf'^(?:theorem|lemma|def|structure)\s+{re.escape(name)}\b', src, re.M)
    if not m:
        return None
    nxt = TOP.search(src, m.end())
    return src[m.start(): nxt.start() if nxt else len(src)].rstrip()


def split_sig_body(decl):
    """signature = text up to the first ':= by' / ':=' that ends a line (or the 'where' line); body = the rest"""
    lines = decl.split('\n')
    for i, ln in enumerate(lines):
        s = ln.rstrip()
        if s.endswith(':= by') or s.endswith(':=') or s.endswith(' where'):
            return '\n'.join(lines[:i + 1]), [x.strip() for x in lines[i + 1:] if x.strip()]
    return decl, []


def binders(sig):
    """top-level (...) and {...} binder groups of a signature, name -> normalized text"""
    out = {}
    depth = 0
    start = None
    opener = None
    flat = ' '.join(sig.split())
    for i, ch in enumerate(flat):
        if ch in '({' and depth == 0:
            start, opener = i, ch
            depth = 1
        elif ch in '({':
            depth += 1
        elif ch in ')}':
            depth -= 1
            if depth == 0 and start is not None:
                grp = flat[start: i + 1]
                mm = re.match(r'[({]\s*([^:]+?)\s*:', grp)
                if mm:
                    for nm in mm.group(1).split():
                        out[nm] = grp
                start = None
    return out


def result_type(sig):
    flat = ' '.join(sig.split())
    depth = 0
    last = 0
    for i, ch in enumerate(flat):
        if ch in '({[':
            depth += 1
        elif ch in ')}]':
            depth -= 1
        elif ch == ':' and depth == 0 and flat[i:i + 2] != ':=':
            last = i
    tail = flat[last + 1:]
    return re.sub(r':=( by)?\s*$', '', tail).strip()


def body_diff(b1, b2):
    sm = difflib.SequenceMatcher(a=b1, b=b2, autojunk=False)
    rem, add = [], []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ('replace', 'delete'):
            rem.extend(b1[i1:i2])
        if tag in ('replace', 'insert'):
            add.extend(b2[j1:j2])
    return rem, add


DSRC = {f: strip_comments((DESIGN / f'{f}.lean').read_text(encoding='utf-8'))
        for f in ('FourCopyHeadline', 'FourCopyIE1', 'FourCopyLocal', 'FourCopyBipolar', 'FourCopyParity',
                  'FourCopyCore', 'FourCopyTables', 'FourCopyBridge', 'FourCopyEuler', 'FourCopyDefs')}
USRC_RAW = UNB.read_text(encoding='utf-8')
USRC = strip_comments(USRC_RAW)


def compare(cid, fname, dname, uname, rem_binders, add_binders, exp_rem, exp_add):
    d = get_decl(DSRC[fname], dname)
    u = get_decl(USRC, uname)
    if d is None or u is None:
        chk(cid, f'{dname} -> {uname}: both declarations found', False, 'source')
        return
    dsig, dbody = split_sig_body(d)
    usig, ubody = split_sig_body(u)
    bd, bu = binders(dsig), binders(usig)
    ok_b = ({k: v for k, v in bd.items() if k not in rem_binders} == {k: v for k, v in bu.items() if k not in add_binders}
            and set(rem_binders) <= set(bd) and set(add_binders) <= set(bu))
    ok_t = result_type(dsig) == result_type(usig)
    rem, add = body_diff(dbody, ubody)
    ok_d = sorted(rem) == sorted(exp_rem) and sorted(add) == sorted(exp_add)
    chk(cid, f'{fname}.{dname} -> {uname}: binders differ exactly by -{sorted(rem_binders)} +{sorted(add_binders)}, '
        f'same result type, body differs exactly in the frozen lines', ok_b and ok_t and ok_d, 'source',
        f'binders {ok_b}, type {ok_t}, body {ok_d} (removed {len(rem)}, added {len(add)})')


# ===============================================================================================================
section('A  the _cons declarations are the design declarations with only the consuming lines changed')
compare('A1', 'FourCopyHeadline', 'ie1_all', 'ie1_all_cons', ['hprod', 'hgate'], ['hcons'],
        ['link_mem (hcls p) (hprod p) (hgate p) a b'],
        ['⟨(hcons p).link a b, link_target_of_ctrl ((hcons p).link a b)⟩'])
compare('A2', 'FourCopyIE1', 'parity_witnesses', 'parity_witnesses_cons', ['hprod', 'hgate', 'hinv'], ['hbs0', 'hbe0'],
        ['have hbs : bellOf A B ∈ K := bell_mem hcls hprod hgate',
         'have hbe : bellOf A B ∈ dualW K := bell_mem_dual hcls hK hinv'],
        ['have hbs : bellOf A B ∈ K := hbs0', 'have hbe : bellOf A B ∈ dualW K := hbe0'])
compare('A3', 'FourCopyHeadline', 'parity_all', 'parity_all_cons', ['hgate', 'hinv'], ['hbs', 'hbe'],
        [f'(parity_witnesses (hcls .{p}) (hadm .{p}).1.2 (hadm .{p}).1.1 (hgate .{p}) (hinv .{p})'
         for p in ('p01', 'p23', 'p02', 'p13')],
        [f'(parity_witnesses_cons (hcls .{p}) (hadm .{p}).1.2 (hbs .{p}) (hbe .{p})'
         for p in ('p01', 'p23', 'p02', 'p13')])
compare('A4', 'FourCopyHeadline', 'kt4_general_ie1', 'kt4_general_ie1_cons', ['hgate'], ['hcons'],
        ['have hinv : ∀ p, ∀ ω ∈ K p, (N p).symm ω ∈ K p := fun p =>',
         'inv_mem_of_orth (hcls p).ipW_map (hcl p) (hgate p)',
         'have hbs : ∀ p, bellOf (A p) (B p) ∈ K p := fun p => bell_mem (hcls p) (hadm p).1.1 (hgate p)',
         'have hbe : ∀ p, bellOf (A p) (B p) ∈ dualW (K p) := fun p =>',
         'bell_mem_dual (hcls p) (hadm p).1.2 (hinv p)',
         'have hie := ie1_all K N A B A\' B\' hcls (fun p => (hadm p).1.1) hgate hbi hbs hbe h',
         'exact parity_all K N A B A\' B\' hcls hadm hgate hinv hie h'],
        ['have hbs : ∀ p, bellOf (A p) (B p) ∈ K p := fun p => (hcons p).bs',
         'have hbe : ∀ p, bellOf (A p) (B p) ∈ dualW (K p) := fun p => (hcons p).bd',
         'have hie := ie1_all_cons K N A B A\' B\' hcls hcons hbi hbs hbe h',
         'exact parity_all_cons K N A B A\' B\' hcls hadm hbs hbe hie h'])
compare('A5', 'FourCopyHeadline', 'kt4_forward_ie1', 'kt4_forward_ie1_cons', ['hgate'], ['hcons'],
        ['obtain ⟨-, hIE, hpar⟩ := kt4_general_ie1 K N A B A\' B\' hcls hadm hcl hgate hF'],
        ['obtain ⟨-, hIE, hpar⟩ := kt4_general_ie1_cons K N A B A\' B\' hcls hadm hcl hcons hF'])

lm = split_sig_body(get_decl(DSRC['FourCopyIE1'], 'link_mem'))[1]
co = get_decl(USRC, 'cons_of_oq1') or ''
co_lines = [x.strip() for x in co.split('\n') if x.strip()]
chk('A6', 'cons_of_oq1.link = the control half of link_mem with "hgate _ (hprod _ X _ Y)" read as "h.1 _ X _ Y"',
    'have hmem := hgate _ (hprod _ (orth_mem_eball (isOrth3_trn hcls.2.2.1) (rot3_xplus_mem a)) _' in lm
    and '(orth_mem_eball (isOrth3_trn hcls.2.2.2.1) (rotX_z3_mem b)))' in lm
    and 'have hmem := h.1 _ (orth_mem_eball (isOrth3_trn hcls.2.2.1) (rot3_xplus_mem a)) _' in co_lines
    and '(orth_mem_eball (isOrth3_trn hcls.2.2.2.1) (rotX_z3_mem b))' in co_lines
    and 'rw [hcls.apply_prodState, cnot_prodState_rot, ← actC_actT_comm, actC_comp] at hmem' in lm
    and 'rw [hcls.apply_prodState, cnot_prodState_rot, ← actC_actT_comm, actC_comp] at hmem' in co_lines,
    'source')
bm = split_sig_body(get_decl(DSRC['FourCopyLocal'], 'bell_mem'))[1]
chk('A7', 'cons_of_oq1.bs = bell_mem with "exact hgate _ (hprod x hx y hy)" read as "exact h.1 x hx y hy"',
    bm == ['obtain ⟨x, hx, y, hy, hxy⟩ := hcls.bell_state', 'rw [← hxy]', 'exact hgate _ (hprod x hx y hy)']
    and all(x in co_lines for x in ('obtain ⟨x, hx, y, hy, hxy⟩ := hcls.bell_state', 'rw [← hxy]',
                                    'exact h.1 x hx y hy')), 'source')
bdm = split_sig_body(get_decl(DSRC['FourCopyLocal'], 'bell_mem_dual'))[1]
os_ = split_sig_body(get_decl(USRC, 'oq1_of_sect') or '')[1]
rem8, add8 = body_diff(bdm, [x.replace('hm', 'h') if x.startswith(('have hm', 'rw [hbc] at hm', 'have h1 := mem_dualW.1 hm'))
                             else x for x in os_])
chk('A8', 'oq1_of_sect = bell_mem_dual with the inverse-gate step replaced and "refine ⟨h.1, ?_⟩" prepended '
    '(the scaling lines identical)',
    sorted(rem8) == ['have h := dualW_of_inv hcls.ipW_map hinv (sharp_mem_dualW hK hb hc)']
    and sorted(add8) == sorted(['refine ⟨h.1, ?_⟩', 'have h := gate_sharp_mem_dualW_of_inv_pos hcls.ipW_map h.2 hb hc']),
    'source', f'removed {rem8}, added {add8}')
sm_ = split_sig_body(get_decl(DSRC['FourCopyLocal'], 'sharp_mem_dualW'))[1]
gs_ = split_sig_body(get_decl(USRC, 'gate_sharp_mem_dualW_of_inv_pos') or '')[1]
chk('A9', 'gate_sharp_mem_dualW_of_inv_pos = sharp_mem_dualW read through the gate: the refine line and the '
    'sharpEff_isEffectOn tail identical, "hK hX" -> "hpos X hX" after the rewrite h1',
    sm_[0] == gs_[0] == 'refine mem_dualW.2 fun X hX => ?_'
    and sm_[1] == 'rw [ipW_tens, ← prodEffVal_sharp]' and gs_[-2] == 'rw [h1, ipW_tens, ← prodEffVal_sharp]'
    and sm_[2] == 'exact hK hX _ _ (sharpEff_isEffectOn hb) (sharpEff_isEffectOn hc)'
    and gs_[-1] == 'exact hpos X hX _ _ (sharpEff_isEffectOn hb) (sharpEff_isEffectOn hc)', 'source')

# countercontrol: a mutated copy (one extra changed line) must be detected by the same comparison
d1 = get_decl(DSRC['FourCopyHeadline'], 'ie1_all')
u1 = get_decl(USRC, 'ie1_all_cons')
u1_mut = u1.replace('have h02 := step .p02 .p13 .p01 .p23 (FourCopyCoherent.target02 h)',
                    'have h02 := step .p02 .p13 .p01 .p23 (FourCopyCoherent.target01 h)')
rem_m, add_m = body_diff(split_sig_body(d1)[1], split_sig_body(u1_mut)[1])
chk('A.cc', 'countercontrol: a copy of ie1_all_cons with one extra changed line is not accepted by the A1 rule',
    not (sorted(rem_m) == ['link_mem (hcls p) (hprod p) (hgate p) a b']
         and sorted(add_m) == ['⟨(hcons p).link a b, link_target_of_ctrl ((hcons p).link a b)⟩']), 'countercontrol')

# ===============================================================================================================
section('B  hygiene of the UNBUILT file')
chk('B1', 'no sorry, admit or axiom in B1_UNBUILT.lean',
    not re.search(r'\b(sorry|admit|axiom)\b', USRC), 'source')
decl_with_hgate = sorted({m.group(1) for m in re.finditer(r'^(?:theorem|def)\s+(\S+)', USRC, re.M)
                          if re.search(r'(?<![A-Za-z0-9_])hgate(?![A-Za-z0-9_])', get_decl(USRC, m.group(1)) or '')})
chk('B2', 'hgate occurs only in cons_of_hgate and prec_of_hgate (the implications FROM hgate); hinv nowhere',
    decl_with_hgate == ['cons_of_hgate', 'prec_of_hgate']
    and not re.search(r'(?<![A-Za-z0-9_])hinv(?![A-Za-z0-9_])', USRC), 'source', str(decl_with_hgate))
chk('B3', 'the file states UNBUILT in its header', 'UNBUILT. No Lean toolchain was available' in USRC_RAW, 'source')

# ===============================================================================================================
section('C  every lemma the UNBUILT file calls exists in the design modules or the landed sources')
CALLED = ['actC_rotWord_phiW', 'actC_actT_comm', 'actC_comp', 'actT_comp', 'actC_id', 'actT_id', 'trn_comp_self',
          'comp_trn_self', 'cross_rel', 'rot_of_words', "rot_of_words'", 'inv_left_ctrl', 'inv_right_ctrl',
          'inv_left_partner', 'inv_right_partner', 'image_eq_of_rot', 'ie1_of_dualW', 'isOrth3_chartOf',
          'isRot3_trn', 'isRot3_of_det', 'det_chartOf', 'bellOf_eq_actC', 'cnotTw_prodState_xplus_z3',
          'det_mul_self_of_orth', 'cnot_prodState_xplus_z3', 'isOrth3_comp', 'isOrth3_reflY', 'isOrth3_trn',
          'det_reflY', 'det_trn', 'actC_reflY_idW', 'actC_mem_of_ie1', 'ie1_dualW', 'gateOf_sharp',
          'smul_mem_dualW', 'gateOf_neg_eq', 'isRot3_comp', 'isRot3_rotYpi', 'kt4_parity_of_witnesses',
          'bidual_of_adm', 'fourCopyCoherent_of_kt4Core', 'kt4_forward_ie1', 'orth_mem_eball', 'rot3_xplus_mem',
          'rotX_z3_mem', 'cnot_prodState_rot', 'ipW_tens', 'prodEffVal_sharp', 'sharpEff_isEffectOn', 'mem_dualW',
          'ipW_smul_left', 'link_mem', 'bell_mem', 'bell_mem_dual', 'inv_mem_of_orth', 'actC_apply', 'actT_apply',
          'gateOf_true', 'gateOf_false']
ALLSRC = '\n'.join(DSRC.values()) + '\n' + '\n'.join(
    strip_comments(p.read_text(encoding='utf-8')) for p in sorted(LANDED.glob('*.lean')))
missing = [n for n in CALLED if not re.search(rf'^(?:theorem|lemma|def|abbrev)\s+{re.escape(n)}(?![A-Za-z0-9_\'])',
                                              ALLSRC, re.M)]
chk('C1', f'all {len(CALLED)} called lemma names are declared in the design or landed sources', not missing, 'source',
    f'missing: {missing}' if missing else '')
NCLASS_FIELDS = ['NClass.apply_prodState', 'NClass.bell_state', 'NClass.bell_effect', 'NClass.ipW_map']
missing2 = [n for n in NCLASS_FIELDS if not re.search(rf'^theorem\s+{re.escape(n)}\b', DSRC['FourCopyLocal'], re.M)]
chk('C2', 'the NClass dot-lemmas used (apply_prodState, bell_state, bell_effect, ipW_map) are declared in '
    'FourCopyLocal', not missing2, 'source')
called_in_file = [n for n in CALLED if re.search(rf'(?<![A-Za-z0-9_.]){re.escape(n)}(?![A-Za-z0-9_\'])', USRC)]
chk('C3', 'every listed name is actually used by the UNBUILT file (the list is not padded)',
    len(called_in_file) == len(CALLED), 'source', f'{len(called_in_file)}/{len(CALLED)}')

# ===============================================================================================================
section('D  table-level identities behind the new lemmas')
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: (-1 if (m, n) in NEG else 1) * w[PC[m][n], PT[m][n]])


def homMap(R):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = sp.Matrix(R)
    return M


def actC(R, w):
    return homMap(R) * w


def actT(R, w):
    return w * homMap(R).T


def ipW(E, X):
    return sum(E[m, n] * X[m, n] for m in R4 for n in R4)


def hom(x):
    return sp.Matrix([1] + list(x))


def prodState(x, y):
    return hom(x) * hom(y).T


def nclass(A, B, Ap, Bp, w):
    return actC(A, actT(B, cnot(actC(Ap, actT(Bp, w)))))


def z(v):
    return sp.cancel(sp.together(sp.expand(v))) == 0


def mzero(M):
    return all(z(v) for v in M)


def symmat3(nm):
    return sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'{nm}{i}{j}', real=True))


W = sp.Matrix(4, 4, lambda m, n: sp.Symbol(f'w{m}{n}', real=True))
E = sp.Matrix(4, 4, lambda m, n: sp.Symbol(f'e{m}{n}', real=True))
A, B, Ap, Bp, C, D = (symmat3(c) for c in 'ABPSCD')
reflY = sp.diag(1, -1, 1)
I3 = sp.eye(3)
phiW = sp.diag(1, 1, -1, 1)
chk('D1', 'locEquiv: actC C^T (actT D^T (actC C (actT D w))) = actC (C^T C) (actT (D^T D) w), symbolic (with C^T C = '
    'D^T D = I this is w: the stated inverse)',
    mzero(actC(C.T, actT(D.T, actC(C, actT(D, W)))) - actC(C.T * C, actT(D.T * D, W))), 'identity')
chk('D2', 'nclass_comp_loc: N(A,B,A\',B\') (actC C (actT D w)) = N(A, B, A\' C, B\' D) w, symbolic (a corrected gate keeps '
    'its post-locals)', mzero(nclass(A, B, Ap, Bp, actC(C, actT(D, W))) - nclass(A, B, Ap * C, Bp * D, W)), 'identity')
m1, m2 = sp.symbols('m1 m2', real=True)
c1, s1 = (1 - m1 ** 2) / (1 + m1 ** 2), 2 * m1 / (1 + m1 ** 2)
c2, s2 = (1 - m2 ** 2) / (1 + m2 ** 2), 2 * m2 / (1 + m2 ** 2)
RZ = sp.Matrix([[c1, -s1, 0], [s1, c1, 0], [0, 0, 1]])
RX = sp.Matrix([[1, 0, 0], [0, c2, -s2], [0, s2, c2]])
chk('D3', 'link_target_of_ctrl: actC (A Rz Rx) (actT B phiW) = actC A (actT (B Rx Rz) phiW), symbolic A, B and angles '
    '(the control and target forms of a link are one table)',
    mzero(actC(A * RZ * RX, actT(B, phiW)) - actC(A, actT(B * RX * RZ, phiW))), 'identity')
chk('D4', 'N-CLASS gates fix the unit entry: N(A,B,A\',B\') w at (0,0) equals w at (0,0), symbolic (normalization is '
    'kept, used by GT-COMP <=> SECT)', z(nclass(A, B, Ap, Bp, W)[0, 0] - W[0, 0]), 'identity')
GATES = {
    'g_cnot': (I3, I3, I3, I3), 'g_D': (I3, reflY, I3, I3), 'g_pre': (I3, I3, I3, reflY), 'g_Tw': (I3, reflY, I3, reflY)}


def ninv(Am, Bm, Apm, Bpm, w):   # inverse for orthogonal locals: actC A'^T actT B'^T cnot actC A^T actT B^T
    return actC(Apm.T, actT(Bpm.T, cnot(actC(Am.T, actT(Bm.T, w)))))


ok_adj = True
ok_eval = True
xs = [sp.Symbol(f'x{i}', real=True) for i in range(3)]
ys = [sp.Symbol(f'y{i}', real=True) for i in range(3)]
a4 = sp.Matrix([sp.Symbol(f'a{i}', real=True) for i in range(4)])
b4 = sp.Matrix([sp.Symbol(f'b{i}', real=True) for i in range(4)])
for g, (Am, Bm, Apm, Bpm) in GATES.items():
    ok_adj = ok_adj and z(ipW(nclass(Am, Bm, Apm, Bpm, E), W) - ipW(E, ninv(Am, Bm, Apm, Bpm, W)))
    ok_adj = ok_adj and mzero(ninv(Am, Bm, Apm, Bpm, nclass(Am, Bm, Apm, Bpm, W)) - W)
    pe = a4 * b4.T
    ok_eval = ok_eval and z(ipW(nclass(Am, Bm, Apm, Bpm, pe), nclass(Am, Bm, Apm, Bpm, prodState(xs, ys)))
                            - (a4.T * hom(xs))[0, 0] * (b4.T * hom(ys))[0, 0])
chk('D5', 'for the four gates of the models: the ipW-adjoint of N (the transpose formula) satisfies ipW (N E) X = '
    'ipW E (adj X) and is the inverse, adj . N = id, symbolic E, X (so the gate image of a product effect pairs with X '
    'as the product effect with N^-1 X)', ok_adj, 'identity')
chk('D6', 'transported evaluation law, the four gates: ipW (N (a b^T)) (N (prodState x y)) = (a.x^)(b.y^), symbolic '
    '(the gate-transported product data satisfy COMP-1\'s evaluation law)', ok_eval, 'identity')
Mbad = sp.Matrix([[1, 1, 0], [0, 1, 0], [0, 0, 1]])   # not orthogonal
chk('D.cc', 'countercontrol: for a non-orthogonal pre-local the ipW-adjoint (transpose formula) is not the inverse: '
    'adj . N != id (orthogonality of the locals is what D5 uses)',
    not mzero(ninv(I3, I3, Mbad, I3, nclass(I3, I3, Mbad, I3, W)) - W), 'countercontrol')

# ===============================================================================================================
print()
kinds = ('identity', 'source', 'countercontrol')
print('kinds: ' + ', '.join(f"{k} {sum(1 for c in CHECKS if c[1] == k)}" for k in kinds), flush=True)
failed = [c[0] for c in CHECKS if not c[2]]
if failed:
    print(f"b1_steps: NO VERDICT -- {len(failed)} of {len(CHECKS)} checks failed: {', '.join(failed)}")
    sys.exit(1)
print('VERDICT B1-STEPS: each consuming step of the design proof has an exact counterpart in B1_UNBUILT.lean that '
      'changes only that step: link_mem (A1, A6), bell_mem (A4, A7), Lemma R (A4: deleted), bell_mem_dual (A4, A8, A9), '
      'parity_witnesses (A2, A3); kt4_general_ie1 and kt4_forward_ie1 are reassembled (A4, A5).  The file is UNBUILT; '
      'the sufficiency statements rest on these diffs, the design-run lemmas they call, and identities D1-D6.')
print(f'b1_steps: OK -- {len(CHECKS)} checks')
