PREFIX = 'OIBridge.RelcSelect.'
CD = LEAN + 'CompositeDimension.lean'
PN = LEAN + 'ParityNot.lean'
GATE_FIELDS = ('frame', 'posFwd', 'posInv', 'relT', 'relC')
DOTTED = ('posFwd', 'posInv', 'relT', 'relC', 'frame')
PAR, BLK, SQZ, C5 = MODULES
# the landed objects the rules read (other than NativeGate's and GateRel's fields), read from D
LANDED_CD_THMS = ('dim_of_nativeGate', 'three_of_nativeGate', 'not_entangling_one', 'blockData_of_nativeGate',
                  'nativeGate_cnot1', 'nativeGate_cnot', 'not_even_of_balanced')
LANDED_PN_DEFS = ('odd5', 'c5', 'n5', 'z5', 'x5')
LANDED_PN_THMS = ('isNot_n5', 'homMap_n5_sign')
# PARITY-NOT-1's NOT n5 and the points of eball 5 the squeezed witness reads, as landed at D
LANDED_N5 = {
    'odd5': 'def odd5 : Fin 6 → Bool | 0 => false | 1 => false | 2 => false | 3 => true | 4 => true | 5 => true',
    'c5': 'def c5 (j : Fin 5) : ℝ := if odd5 j.succ then -1 else 1',
    'n5': 'def n5 : (Fin 5 → ℝ) →ₗ[ℝ] (Fin 5 → ℝ) := diagSign c5',
    'z5': 'def z5 : Fin 5 → ℝ := fun i => if i = 4 then 1 else 0',
    'x5': 'def x5 : Fin 5 → ℝ := fun i => if i = 0 then 1 else 0',
    'isNot_n5': 'theorem isNot_n5 : IsNot (eball 5) z5 n5',
    'homMap_n5_sign': 'theorem homMap_n5_sign (v : HVec 5) (μ : Fin (5 + 1)) : homMap n5 v μ = '
                      '(if odd5 μ then -1 else 1) * v μ'}
# the landed dimension corollaries of the native gate; no declaration of the round names one
LANDED_SELECTORS = ('dim_of_nativeGate', 'dim_of_nativeGateOf', 'dim_of_nativeGateOf_dense', 'ne_two_of_nativeGate',
                    'ne_four_of_nativeGate', 'ne_five_of_nativeGate', 'ne_seven_of_nativeGate',
                    'not_even_of_nativeGate', 'three_of_nativeGate', 'three_of_nativeGate_of_two_le',
                    'three_of_nativeGateOf', 'three_of_nativeGateOf_dense', 'three_of_nativeGateOf_of_two_le',
                    'three_of_nativeGateOf_of_two_le_dense', 'det_of_nativeGate_three',
                    'piRotation_of_nativeGate_three', 'tangentPlus_of_nativeGate_three')
# the landed objects that read `relT`, by name; neither the parity module nor the block module names one
RELT_READERS = ('relT', 'GateRel', 'gate_actT', 'Mfwd_homMap', 'Minv_homMap', 'Minv_Mfwd', 'opGate_comp_homMap',
                'opGate_comp_homMap_rel', 'Lop_eq_zero', 'Lop_injective', 'finrank_plus_eq_finrank_minus',
                'finrank_plus_eq_finrank_minus_rel', 'gateRel_of_nativeGate', 'not_even_of_gateRel')

# --- S1: parity from the control relation (RelcSelectParity) ---
PAR_THM, PAR_ODD = 'finrank_plus_eq_finrank_minus_relC', 'not_even_of_relC'
PAR_BINDERS = ('{z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} '
               '(hN : IsNot (eball d) z N) (hC : %s)')
PAR_CONCL = 'Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N)'
PAR_PROOF = ('opGate_injective_relC', 'opGate_homMap_comp_relC', 'finrank_ker_sub_le_relC', 'finrank_ker_add_le_relC',
             'finrank_ker_relCLeft_sub', 'finrank_ker_relCLeft_add', 'finrank_ker_relCConj_sub_le',
             'finrank_ker_relCConj_add_le', 'balance_of_bounds_relC')
PAR_ODD_PROOF = ('not_even_of_balanced', PAR_THM)
LANDED_BALANCED = 'theorem not_even_of_balanced {a b : ℕ} (hsum : a + b = d + 1) (hbal : a = b) : ¬ Even d'
# the parity module reads none of these
PAR_FREE = RELT_READERS + ('NativeGate', 'CtrlGate', 'frame', 'posFwd', 'posInv', 'maxCone', 'prodEffVal',
                           'IsEffectOn', 'sharpEff', 'corner', 'prodState', 'Entangling')

# --- S2: the selector without the target relation (RelcSelectBlock) ---
CTRL = 'CtrlGate'
CTRL_FIELDS = ['frame', 'posFwd', 'posInv', 'relC']
CTRL_OF_NATIVE = ('theorem ctrlGate_of_nativeGate {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} '
                  '{N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hG : NativeGate Ω z N G) : '
                  'CtrlGate Ω z N G')
SLICE = ('theorem actT_slice_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} '
         '(hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) '
         '(hzc : ∑ j, z j * c j = 0) : actT N (G (tens (lift c) (Minv z G (hom 0)))) = '
         'G (tens (lift c) (Minv z G (hom 0)))')
SEL_FROM = {'blockData_of_ctrlGate': 'blockData_of_nativeGate', 'not_entangling_one_ctrl': 'not_entangling_one',
            'dim_of_ctrlGate': 'dim_of_nativeGate', 'three_of_ctrlGate': 'three_of_nativeGate'}
SEL_PROOF = {'dim_of_ctrlGate': (PAR_THM, 'blockData_of_ctrlGate'),
             'three_of_ctrlGate': ('dim_of_ctrlGate', 'not_entangling_one_ctrl'),
             'blockData_of_ctrlGate': ('blockData_of_orthonormal_ctrl',),
             'blockData_of_orthonormal_ctrl': ('actT_slice_ctrl',),
             'actT_slice_ctrl': ('phi_minusSpace_ctrl', 'homMap_eq_self_of_orth_minusSpace')}
ENTANGLING_ONLY = ('not_entangling_one_ctrl', 'three_of_ctrlGate')
ATTAIN = {'nativeGate_cnot1': 'theorem nativeGate_cnot1 : NativeGate (eball 1) z1 neg1 cnot1',
          'nativeGate_cnot': 'theorem nativeGate_cnot : NativeGate (eball 3) z3 nflip cnot'}
# the copy: each declaration of DIM-1's §Q the block module restates, its name there, and the two line edits
COPY_MAP = {
    'gate_corner': 'gate_corner_ctrl', 'gate_corner_symm': 'gate_corner_symm_ctrl', 'Mfwd_Minv': 'Mfwd_Minv_ctrl',
    'lor_Minv': 'lor_Minv_ctrl', 'gate_actC': 'gate_actC_ctrl', 'gate_corner_neg': 'gate_corner_neg_ctrl',
    'gt_corner': 'gt_corner_ctrl', 'gt_corner_neg': 'gt_corner_neg_ctrl', 'gt_center': 'gt_center_ctrl',
    'gt_tangent_corners': 'gt_tangent_corners_ctrl', 'gt_sphere': 'gt_sphere_ctrl',
    'gt_sphere_corner': 'gt_sphere_corner_ctrl', 'Phi_sphere': 'Phi_sphere_ctrl', 'Phi_center': 'Phi_center_ctrl',
    'Phi_center_all': 'Phi_center_all_ctrl', 'Phi_hom_zero_eq_zero': 'Phi_hom_zero_eq_zero_ctrl',
    'Phi_lift_z_eq_zero': 'Phi_lift_z_eq_zero_ctrl', 'blockData_of_orthonormal': 'blockData_of_orthonormal_ctrl',
    'blockData_of_nativeGate': 'blockData_of_ctrlGate', 'not_entangling_one': 'not_entangling_one_ctrl',
    'dim_of_nativeGate': 'dim_of_ctrlGate', 'three_of_nativeGate': 'three_of_ctrlGate'}
COPY_RENAME = dict(COPY_MAP, NativeGate='CtrlGate')
COPY_EDITS = {
    'blockData_of_orthonormal_ctrl': [(
        '            rw [hω, ← gate_actT hN hG, actT_tens, ← Minv_homMap hN hG, homMap_hom, map_zero]',
        '            rw [hω]; exact actT_slice_ctrl hN hG hcl hzl')],
    'dim_of_ctrlGate': [(
        '    have hbal := finrank_plus_eq_finrank_minus hN hG',
        '    have hbal := finrank_plus_eq_finrank_minus_relC hN hG.relC')]}
COPY_NEW = ('CtrlGate', 'ctrlGate_of_nativeGate', 'gt_center_two_ctrl', 'phi_lift_minus_ctrl',
            'phi_bvec_minus_unit_ctrl', 'phi_minusSpace_ctrl', 'homMap_eq_self_of_orth_minusSpace', 'actT_slice_ctrl')
HEADL = re.compile(r"^(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+)?(?:private\s+|protected\s+)?"
                   r"(theorem|lemma|def|abbrev|structure|instance|class|inductive)\s+([A-Za-z_][A-Za-z0-9_'.]*)")

# --- S3: the two positivity clauses one at a time (RelcSelectSqueeze) ---
SQ_DEFS = {
    'sqCls': 'def sqCls : Fin 6 → Bool | 0 => true | 1 => false | 2 => false | 3 => false | 4 => false | 5 => true',
    'sqSig': 'def sqSig : Fin 6 → Fin 6 | 0 => 1 | 1 => 0 | 2 => 2 | 3 => 5 | 4 => 4 | 5 => 3',
    'sqPc': 'def sqPc (m n : Fin 6) : Fin 6 := if odd5 n then perm5 m else m',
    'sqPt': 'def sqPt (m n : Fin 6) : Fin 6 := if sqCls m then n else sqSig n',
    'sqR': 'noncomputable def sqR (m : Fin 6) : ℝ := if sqCls m then 1 else 1 / 10',
    'sqK': 'noncomputable def sqK (n : Fin 6) : ℝ := if sqCls n then 1 else 1 / 2',
    'sqW': 'noncomputable def sqW (m n : Fin 6) : ℝ := sqR m * sqK (sqPt m n)',
    'sqWi': 'noncomputable def sqWi (m n : Fin 6) : ℝ := (if sqCls m then 1 else 10) * (if sqCls n then 1 else 2)',
    'gSqFun': 'noncomputable def gSqFun (ω : W 5) : W 5 := fun m n => sqW m n * ω (sqPc m n) (sqPt m n)',
    'gSqInvFun': 'noncomputable def gSqInvFun (ω : W 5) : W 5 := fun m n => sqWi m n * ω (sqPc m n) (sqPt m n)'}
SQ_GATE_HEAD = 'noncomputable def gSq : W 5 ≃ₗ[ℝ] W 5 where toFun := gSqFun invFun := gSqInvFun'
SQ_VALUE = 'prodEffVal (sharpEff z5) (sharpEff (-x5)) (gSq.symm (prodState z5 x5)) = -1 / 2'
GRD = '{Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}'

# --- S4: the control relation is not replaced by the target relation (RelcSelectC5) ---
C5_DEFS = {
    'oddC5': 'def oddC5 : Fin 6 → Bool | 0 => false | 1 => false | 2 => true | 3 => true | 4 => true | 5 => true',
    'cC5': 'def cC5 (j : Fin 5) : ℝ := if oddC5 j.succ then -1 else 1',
    'nC5': 'def nC5 : (Fin 5 → ℝ) →ₗ[ℝ] (Fin 5 → ℝ) := diagSign cC5',
    'sgnC5': 'def sgnC5 (μ ν : Fin 6) : ℝ := if ((μ = 1 ∨ μ = 3) ∧ (ν = 4 ∨ ν = 5)) ∨ ((μ = 2 ∨ μ = 4) ∧ '
             '(ν = 2 ∨ ν = 3)) then -1 else 1',
    'gC5Fun': 'def gC5Fun (ω : W 5) : W 5 := fun μ ν => sgnC5 μ ν * ω (pcC5 μ ν) (ptC5 μ ν)'}
C5_TABLES = ('pcC5', 'ptC5')
C5_GATE_HEAD = 'def gC5 : W 5 ≃ₗ[ℝ] W 5 where toFun := gC5Fun invFun := gC5Fun'

# --- S6/S7/S9 ---
D_EQ = re.compile(r'(?<![\w.\'])d\s*(=|≠)\s*\d')
D_EQ_ALLOWED = ('dim_of_ctrlGate', 'three_of_ctrlGate', 'relT_not_dimension_selecting')
SCOPE_TOKENS = ('Complex', 'ℂ') + LANDED_SELECTORS
IMPORTS_OF = {PAR: ['import OIBridge.OddChar'], BLK: ['import OIBridge.RelcSelectParity', 'import OIBridge.ParityNot'],
              SQZ: ['import OIBridge.OddChar'], C5: ['import OIBridge.OddChar']}

# --- S8: the frozen phrases (case-insensitive, backticks removed, whitespace-normalized) ---
PHRASES = (
    # the target relation is not globally redundant; CtrlGate leaves the gate theory as it is
    'redundan', 'superfluous', 'relT is unnecessary', 'relT is not needed', 'relT is never needed',
    'relT plays no role', 'relT can be dropped', 'relT can be removed', 'relT may be dropped', 'drop relT',
    'remove relT', 'removes relT from NativeGate', 'relT is derivable', 'relT is derived', 'relT follows from',
    'relT is implied', 'implies relT', 'derivable from the remaining', 'relT is independent',
    'independent of the remaining', 'equivalent to NativeGate', 'NativeGate is equivalent', 'CtrlGate is equivalent',
    'CtrlGate implies NativeGate', 'every CtrlGate is a NativeGate', 'replaces NativeGate', 'without loss of generality',
    # the control relation is not claimed inverse-stable on its own
    'inverse-stable', 'inverse stable', 'stable under inversion', 'stable under inverses', 'preserved under inversion',
    'preserved by inversion', 'invariant under inversion', 'closed under inversion', 'relC alone transfers',
    'relC transfers to the inverse on its own', 'without relT, relC', 'relC of G.symm follows from relC of G',
    # the control relation is not replaced by the target relation
    'relT can replace relC', 'relT replaces relC', 'relC can be replaced', 'relC is replaceable', 'relT suffices',
    'relT is sufficient', 'relT alone',
    # each positivity clause is read
    'one positivity clause suffices', 'either positivity clause suffices', 'posFwd alone suffices',
    'posInv alone suffices', 'forward positivity alone suffices', 'inverse positivity alone suffices',
    'forward positivity implies inverse positivity', 'inverse positivity implies forward positivity',
    'posFwd implies posInv', 'posInv implies posFwd',
    # the witnesses are witnesses
    'physical gate', 'physical NOT', 'physically realizable', 'physically realized', 'physically carried',
    'physical postulate', 'physical model', 'adopted model', 'adopts a premise', 'premise adopted', 'new postulate',
    'as a postulate', 'is a postulate', 'postulated', 'OI supplies', 'OI provides', 'derived from OI', 'OI selects',
    # minimality only with respect to the audited clauses; the frame is not audited
    'globally minimal', 'minimal hypothesis set', 'minimal set of hypotheses', 'the frame is necessary',
    'the frame is unnecessary', 'the frame is load-bearing', 'the frame is not needed', 'the frame can be dropped',
    'irreducible', 'independent axioms',
    # the selector concludes d = 1 ∨ d = 3; the entangling clause excludes d = 1
    'CtrlGate gives d = 3', 'CtrlGate forces d = 3', 'selects d = 3', 'forces d = 3 without',
    # design leftovers
    'design (round', 'not for landing', 'UNBUILT', 'not been compiled', 'not been checked by the kernel',
    'design module')

# --- V: the frozen decision rule ---
PAR_TOKENS = ('RELC-PARITY-PROVED', 'RELC-PARITY-NOT-ESTABLISHED')
SEL_TOKENS = ('CTRL-SELECTOR-PROVED', 'CTRL-SELECTOR-NOT-ESTABLISHED')
POS_TOKENS = ('POSITIVITY-SEPARATION-PROVED', 'POSITIVITY-SEPARATION-NOT-ESTABLISHED')
REL_TOKENS = ('RELT-NOT-DIMENSION-SELECTING-PROVED', 'RELT-NOT-DIMENSION-SELECTING-NOT-ESTABLISHED')
ALL_TOKENS = PAR_TOKENS + SEL_TOKENS + POS_TOKENS + REL_TOKENS


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def tsub(text, mapping):
    """Token-bounded simultaneous substitution."""
    pat = re.compile(r'(?<![\w.\'])(%s)(?![\w\'])' % '|'.join(re.escape(k) for k in
                                                           sorted(mapping, key=len, reverse=True)))
    return pat.sub(lambda m: mapping[m.group(1)], text)


def kinds_texts_proofs(mod):
    chunks = decl_chunks(mod or '')
    return ({n: k for n, (k, _, _) in chunks.items()}, {n: c for n, (_, c, _) in chunks.items()},
            {n: p for n, (_, _, p) in chunks.items()})


def qualified(name, c):
    """`name` referenced through a namespace (`CompositeDimension.gate_actT`)."""
    return re.search(r'(?<![\w.\'])[A-Z][\w\']*(?:\.[\w\']+)*\.%s(?![\w\'])' % re.escape(name), c) is not None


def mentions(text, toks):
    """The tokens the code of `text` mentions, also through a namespace; a gate field also as a projection
    (`hG.posInv`)."""
    c = code_only(text)
    return [t for t in toks if token(t, c) or qualified(t, c)
            or (t in DOTTED and re.search(r'(?<![\w\'])%s(?![\w\'])' % t, c))]


def body_of(landed, owner, f):
    v = landed.get('%s#%s' % (owner, f))
    p = f + ' : '
    return v[len(p):] if v is not None and v.startswith(p) else None


def on_body(field, gate, body):
    """A landed positivity field at the gate `gate` on the body `body`."""
    s = tsub(field, {'G': gate, 'Ω': '(%s)' % body})
    return s.replace('∈ (%s),' % body, '∈ %s,' % body)


def relations_bad(landed):
    """The landed GateRel is exactly the landed NativeGate relation fields."""
    bad = []
    for f in ('relT', 'relC'):
        a = landed.get('GateRel#' + f)
        if a is None or a != landed.get('NativeGate#' + f):
            bad.append('GateRel#' + f + ' at D')
    if landed.get('GateRel#fields') != 'relT relC':
        bad.append('GateRel fields at D')
    return bad


def thm_bad(kinds, texts, proofs, n, b, c, deps=()):
    bb, cc = split_statement(texts.get(n, ''))
    return kinds.get(n) != 'theorem' or b is None or c is None or norm(bb) != norm(b) or norm(cc) != norm(c) or \
        not all(token(m, proofs.get(n, '')) for m in deps)


def stmt_eq(texts, n, want):
    return want is not None and norm(texts.get(n, '')) == norm(want)


def free_bad(mod, toks, allow=()):
    bad = []
    for kind, name, start, se, nxt, cend in spans(mod or ''):
        if name not in allow and mentions(mod[start:nxt], toks):
            bad.append(name)
    return bad


def nativegate_names_bad(mod, landed, allow=()):
    """No declaration names a landed declaration whose statement takes the native gate."""
    names = set((landed.get('nativeGate#names') or '').split())
    bad = []
    for kind, name, start, se, nxt, cend in spans(mod or ''):
        if name in allow:
            continue
        refs = set()
        for t in IDENT.findall(code_only(mod[start:nxt])):
            refs.add(t)
            if '.' in t and t[0].isupper():
                refs.add(t.split('.')[-1])
        if (refs & names) - {'NativeGate'}:
            bad.append(name)
    return bad


def parity_bad(mods, landed):
    """S1: from IsNot and the landed relC field alone, equal eigenspace dimensions and ¬ Even d; the parity module
    reads neither relT, the frame, positivity, GateRel nor any landed statement over the native gate."""
    mod = mods.get(PAR)
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    relc = body_of(landed, 'NativeGate', 'relC')
    b = None if relc is None else PAR_BINDERS % relc
    if thm_bad(kinds, texts, proofs, PAR_THM, b, PAR_CONCL, PAR_PROOF):
        bad.append(PAR_THM)
    if thm_bad(kinds, texts, proofs, PAR_ODD, b, '¬ Even d', PAR_ODD_PROOF):
        bad.append(PAR_ODD)
    if landed.get('not_even_of_balanced') != norm(LANDED_BALANCED):
        bad.append('not_even_of_balanced at D')
    bad += free_bad(mod, PAR_FREE)
    bad += nativegate_names_bad(mod, landed)
    return bad


def line_decls(text):
    """name -> the declaration's lines: its head line and every following line up to the next unindented line."""
    lines = (text or '').split('\n')
    heads = [(i, HEADL.match(l).group(2)) for i, l in enumerate(lines) if HEADL.match(l)]
    out = {}
    for i, name in heads:
        j = i + 1
        while j < len(lines) and not (lines[j] and not lines[j][0].isspace()):
            j += 1
        body = lines[i:j]
        while body and not body[-1].strip():
            body.pop()
        out[name] = None if name in out else body
    return out


def copy_bad(mod, landed):
    """Every copied declaration is the landed one under the frozen renaming, except the two frozen line edits; the
    module declares nothing else but the frozen new declarations."""
    md = line_decls(mod)
    bad = []
    for old, new in COPY_MAP.items():
        got, src = md.get(new), landed.get('copy#' + old)
        if got is None or src is None:
            bad.append(new)
            continue
        exp = [tsub(l, COPY_RENAME) for l in src.split('\n')]
        allowed, used, ok = list(COPY_EDITS.get(new, [])), [], len(exp) == len(got)
        for e, g in zip(exp, got):
            if e != g:
                if (e, g) in allowed and (e, g) not in used:
                    used.append((e, g))
                else:
                    ok = False
        if not ok or len(used) != len(allowed):
            bad.append(new)
    if sorted(md) != sorted(list(COPY_MAP.values()) + list(COPY_NEW)):
        bad.append('the module declares other declarations')
    return bad


def selector_bad(mods, landed):
    """S2: CtrlGate is the landed NativeGate without relT, field for field; IsNot and CtrlGate give the landed
    selector's conclusion, and with Entangling d = 3 through the frame-only exclusion of d = 1; the copy is the
    landed proof under the frozen renaming; the parity step is S1's theorem; neither module reads relT."""
    mod = mods.get(BLK)
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    hdr = landed.get('NativeGate#header')
    if kinds.get(CTRL) != 'structure' or hdr is None or \
            norm(def_header(texts.get(CTRL, ''))) != tsub(hdr, {'NativeGate': CTRL}) or \
            fields(texts.get(CTRL, '')) != CTRL_FIELDS or \
            landed.get('NativeGate#fields') != ' '.join(GATE_FIELDS) or \
            any(field_line(texts.get(CTRL, ''), f) is None or
                field_line(texts.get(CTRL, ''), f) != landed.get('NativeGate#' + f) for f in CTRL_FIELDS):
        bad.append(CTRL)
    if not stmt_eq(texts, 'ctrlGate_of_nativeGate', CTRL_OF_NATIVE):
        bad.append('ctrlGate_of_nativeGate')
    if not stmt_eq(texts, 'actT_slice_ctrl', SLICE):
        bad.append('actT_slice_ctrl')
    for new, old in SEL_FROM.items():
        lt = landed.get(old)
        if kinds.get(new) != 'theorem' or lt is None or \
                not stmt_eq(texts, new, tsub(lt, {'NativeGate': CTRL, old: new})):
            bad.append(new)
    for n, deps in SEL_PROOF.items():
        if not all(token(m, proofs.get(n, '')) for m in deps):
            bad.append(n + ' proof')
    for n, want in ATTAIN.items():
        if landed.get(n) != norm(want):
            bad.append(n + ' at D')
    bad += copy_bad(mod, landed)
    bad += free_bad(mod, RELT_READERS)
    bad += free_bad(mod, ('NativeGate',), allow=('ctrlGate_of_nativeGate',))
    bad += nativegate_names_bad(mod, landed)
    bad += free_bad(mod, ('Entangling',), allow=ENTANGLING_ONLY)
    # the parity step the selector cites: S1's statement, and the parity module free of relT
    pk, pt, pp = kinds_texts_proofs(mods.get(PAR))
    relc = body_of(landed, 'NativeGate', 'relC')
    if relc is None or thm_bad(pk, pt, pp, PAR_THM, PAR_BINDERS % relc, PAR_CONCL):
        bad.append(PAR_THM + ' (parity step)')
    if free_bad(mods.get(PAR), RELT_READERS) or nativegate_names_bad(mods.get(PAR), landed):
        bad.append('the parity module reads relT')
    return bad


def sq_conj(landed, gate, inverse):
    """The frozen conclusion of gSq_sep (inverse = False) or gSqInv_sep (inverse = True), from the landed fields."""
    frame, pf, pi = (body_of(landed, 'NativeGate', f) for f in ('frame', 'posFwd', 'posInv'))
    if None in (frame, pf, pi):
        return None
    fr = tsub(frame, {'G': gate, 'z': 'z5'})
    f5, i5 = on_body(pf, gate, 'eball 5'), on_body(pi, gate, 'eball 5')
    if inverse:
        i5 = i5.replace('gSq.symm.symm', 'gSq')
        return 'IsNot (eball 5) z5 n5 ∧ (%s) ∧ GateRel n5 %s ∧ (%s) ∧ ¬ (%s)' % (fr, gate, i5, f5)
    return 'IsNot (eball 5) z5 n5 ∧ (%s) ∧ GateRel n5 %s ∧ (%s) ∧ ¬ (%s)' % (fr, gate, f5, i5)


def positivity_bad(mods, landed):
    """S3: at d = 5 with the landed n5 and z5, gSq has the landed frame, GateRel and the landed posFwd field and
    fails the landed posInv field through the value -1 / 2; gSq.symm has the frame, GateRel and the landed posInv
    field and fails the landed posFwd field; the transfer of relC to the inverse takes relT."""
    mod = mods.get(SQZ)
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    for n, t in SQ_DEFS.items():
        if norm(texts.get(n, '')) != norm(t):
            bad.append(n)
    if not norm(texts.get('gSq', '')).startswith(SQ_GATE_HEAD):
        bad.append('gSq')
    frame, pf, pi, rt, rc = (body_of(landed, 'NativeGate', f) for f in GATE_FIELDS)
    if None in (frame, pf, pi, rt, rc):
        return bad + ['NativeGate fields at D']
    rows = {
        'gSq_frame': ('(a b : Fin 2)', tsub(frame.split(', ', 1)[1], {'G': 'gSq', 'z': 'z5'}), ()),
        'gSq_relT': ('', tsub(rt, {'N': 'n5', 'G': 'gSq'}), ()),
        'gSq_relC': ('', tsub(rc, {'N': 'n5', 'G': 'gSq'}), ()),
        'gateRel_gSq': ('', 'GateRel n5 gSq', ('gSq_relT', 'gSq_relC')),
        'gSq_posFwd': ('', on_body(pf, 'gSq', 'eball 5'), ('gSq_pairVal_nonneg',)),
        'gSq_symm_value': ('', SQ_VALUE, ()),
        'gSq_symm_not_mem_maxCone': ('', 'gSq.symm (prodState z5 x5) ∉ maxCone (eball 5)',
                                     ('gSq_symm_value', 'sharpEff_isEffectOn', 'z5_unit', 'negx5_unit')),
        'gSq_not_posInv': ('', '¬ ' + on_body(pi, 'gSq', 'eball 5'),
                           ('gSq_symm_not_mem_maxCone', 'z5_mem', 'x5_mem')),
        'not_nativeGate_gSq': ('', '¬ NativeGate (eball 5) z5 n5 gSq', ('gSq_not_posInv',)),
        'not_nativeGate_gSqInv': ('', '¬ NativeGate (eball 5) z5 n5 gSq.symm', ('gSq_not_posInv',)),
        'frame_symm': ('{z : Fin d → ℝ} {G : W d ≃ₗ[ℝ] W d} (hF : %s)' % frame, tsub(frame, {'G': 'G.symm'}), ()),
        'relT_symm': ('%s (hN : IsNot Ω z N) (hT : %s)' % (GRD, rt), tsub(rt, {'G': 'G.symm'}), ()),
        'relC_symm_of_relT': ('%s (hN : IsNot Ω z N) (hT : %s) (hC : %s)' % (GRD, rt, rc), tsub(rc, {'G': 'G.symm'}),
                              ()),
        'gateRel_symm': ('%s (hN : IsNot Ω z N) (hR : GateRel N G)' % GRD, 'GateRel N G.symm',
                         ('relT_symm', 'relC_symm_of_relT')),
        'gSq_sep': ('', sq_conj(landed, 'gSq', False),
                    ('isNot_n5', 'gSq_frame', 'gateRel_gSq', 'gSq_posFwd', 'gSq_not_posInv')),
        'gSqInv_sep': ('', sq_conj(landed, 'gSq.symm', True),
                       ('isNot_n5', 'frame_symm', 'gateRel_symm', 'gSq_posFwd', 'gSq_not_posInv'))}
    for n, (b, c, deps) in rows.items():
        if thm_bad(kinds, texts, proofs, n, b, c, deps):
            bad.append(n)
    bad += relations_bad(landed)
    for n, want in LANDED_N5.items():
        if landed.get(n) != norm(want):
            bad.append(n + ' at D')
    bad += free_bad(mod, ('Entangling', CTRL))
    return bad


def relation_bad(mods, landed):
    """S4: at d = 5 with the witness NOT nC5 and the landed z5, gC5 has the landed frame, relT, posFwd and posInv
    fields and fails the landed relC field, so IsNot and those four fields do not give the landed selector's
    conclusion; the module names no part of the landed n5."""
    mod = mods.get(C5)
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    for n, t in C5_DEFS.items():
        if norm(texts.get(n, '')) != norm(t):
            bad.append(n)
    for n in C5_TABLES:
        if norm(texts.get(n, '')) != norm(TEXTS[C5].get(n, '\0')):
            bad.append(n)
    if not norm(texts.get('gC5', '')).startswith(C5_GATE_HEAD):
        bad.append('gC5')
    frame, pf, pi, rt, rc = (body_of(landed, 'NativeGate', f) for f in GATE_FIELDS)
    dimc = split_statement(landed.get('dim_of_nativeGate', ''))[1]
    if None in (frame, pf, pi, rt, rc) or not dimc:
        return bad + ['NativeGate fields or selector at D']
    w = {'G': 'gC5', 'z': 'z5', 'N': 'nC5'}
    sel = ('¬ ∀ (d : ℕ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d), '
           'IsNot (eball d) z N → (%s) → (%s) → (%s) → (%s) → %s'
           % (frame, on_body(pf, 'G', 'eball d'), on_body(pi, 'G', 'eball d'), rt, norm(dimc)))
    rows = {
        'isNot_nC5': ('', 'IsNot (eball 5) z5 nC5', ()),
        'homMap_nC5_sign': ('(v : HVec 5) (μ : Fin (5 + 1))', 'homMap nC5 v μ = (if oddC5 μ then -1 else 1) * v μ',
                            ()),
        'gC5_frame': ('(a b : Fin 2)', tsub(frame.split(', ', 1)[1], w), ()),
        'gC5_relT': ('(ω : W 5)', tsub(rt.split(', ', 1)[1], w), ()),
        'gC5_relC_lhs': ('', 'actC nC5 (gC5 (actC nC5 (OddChar.entW 3 3))) 4 4 = 1', ()),
        'gC5_relC_rhs': ('', 'actT nC5 (gC5 (OddChar.entW 3 3)) 4 4 = -1', ()),
        'gC5_not_relC': ('', '¬ ' + tsub(rc, w), ('gC5_relC_lhs', 'gC5_relC_rhs')),
        'gC5_posFwd': ('', on_body(pf, 'gC5', 'eball 5'), ('gC5_prodEffVal_nonneg',)),
        'gC5_posInv': ('', on_body(pi, 'gC5', 'eball 5'), ('gC5_posFwd',)),
        'c5_sep': ('', 'IsNot (eball 5) z5 nC5 ∧ (%s) ∧ (%s) ∧ (%s) ∧ (%s) ∧ ¬ (%s)'
                   % (tsub(frame, w), tsub(rt, w), on_body(pf, 'gC5', 'eball 5'), on_body(pi, 'gC5', 'eball 5'),
                      tsub(rc, w)),
                   ('isNot_nC5', 'gC5_frame', 'gC5_relT', 'gC5_posFwd', 'gC5_posInv', 'gC5_not_relC')),
        'not_nativeGate_gC5': ('', '¬ NativeGate (eball 5) z5 nC5 gC5', ('gC5_not_relC',)),
        'relT_not_dimension_selecting': ('', sel, ('isNot_nC5', 'gC5_frame', 'gC5_posFwd', 'gC5_posInv',
                                                   'gC5_relT'))}
    for n, (b, c, deps) in rows.items():
        if thm_bad(kinds, texts, proofs, n, b, c, deps):
            bad.append(n)
    if landed.get('z5') != norm(LANDED_N5['z5']):
        bad.append('z5 at D')
    bad += free_bad(mod, ('n5', 'c5', 'odd5', 'isNot_n5', 'homMap_n5_sign', 'Entangling', CTRL))
    return bad


def par_cell(mods, landed):
    """RELC-PARITY-PROVED iff S1. Otherwise RELC-PARITY-NOT-ESTABLISHED. Reads the parity module only."""
    return [PAR_TOKENS[1] if parity_bad(mods, landed) else PAR_TOKENS[0]]


def sel_cell(mods, landed):
    """CTRL-SELECTOR-PROVED iff S2. Otherwise CTRL-SELECTOR-NOT-ESTABLISHED. Reads the block module and, for the
    parity step it cites, the parity theorem's statement and the parity module's freedom from relT."""
    return [SEL_TOKENS[1] if selector_bad(mods, landed) else SEL_TOKENS[0]]


def pos_cell(mods, landed):
    """POSITIVITY-SEPARATION-PROVED iff S3. Otherwise POSITIVITY-SEPARATION-NOT-ESTABLISHED. Reads the squeeze
    module only."""
    return [POS_TOKENS[1] if positivity_bad(mods, landed) else POS_TOKENS[0]]


def rel_cell(mods, landed):
    """RELT-NOT-DIMENSION-SELECTING-PROVED iff S4. Otherwise RELT-NOT-DIMENSION-SELECTING-NOT-ESTABLISHED. Reads the
    C5 module only."""
    return [REL_TOKENS[1] if relation_bad(mods, landed) else REL_TOKENS[0]]


def verdicts(mods, landed):
    return par_cell(mods, landed), sel_cell(mods, landed), pos_cell(mods, landed), rel_cell(mods, landed)


def comments(text):
    """The comment text of a module: every block comment (headers and docstrings) and every line comment."""
    return ' '.join(re.findall(r'/-.*?-/', text or '', flags=re.S) + re.findall(r'--[^\n]*', text or ''))


def phrase_norm(text):
    return norm(re.sub(r'(?m)^\s*>\s?', '', (text or '').replace('`', ''))).lower()


def phrase_hits(text, whitelist=()):
    t = phrase_norm(text)
    for w in whitelist:
        t = t.replace(phrase_norm(w), ' ')
    return [p for p in PHRASES if p.lower() in t]


def note_tokens(note):
    return [t for t in ALL_TOKENS if re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(t), note)]


def earned_stated(note):
    t = phrase_norm(note)
    return [phrase_norm(e) in t for e in EARNED]


def semantic_checks(mods, tag, landed, inv_files):
    for code, label, fn in (('S1', 'parity from IsNot and relC alone; the parity module free of relT, the frame and '
                                   'positivity', parity_bad),
                            ('S2', 'CtrlGate is NativeGate without relT; IsNot and CtrlGate give d = 1 ∨ d = 3, '
                                   'Entangling d = 3; the copy is the landed proof; no relT read', selector_bad),
                            ('S3', 'at d = 5, gSq fails posInv and gSq.symm fails posFwd with every other clause; '
                                   'the relC transfer takes relT', positivity_bad),
                            ('S4', 'at d = 5, gC5 with nC5 has the frame, relT and both positivity clauses and fails '
                                   'relC; the selector does not follow', relation_bad)):
        b = fn(mods, landed)
        check(code, label + tag + ((' %s' % b[:4]) if b else ''), not b)
    bad6 = []
    for m in MODULES:
        mod = mods.get(m) or ''
        texts = {n: c for n, (_, c, _) in decl_chunks(mod).items()}
        for kind, name, start, se, nxt, cend in spans(mod):
            if mentions(mod[start:nxt], SCOPE_TOKENS):
                bad6.append(name)
            if kind in ('theorem', 'lemma'):
                c = norm(split_statement(texts.get(name, ''))[1])
                if (D_EQ.search(c) and name not in D_EQ_ALLOWED) or \
                        (token('NativeGate', c) and not c.startswith('¬')) or \
                        (token(CTRL, c) and name != 'ctrlGate_of_nativeGate'):
                    bad6.append(name)
    check('S6', 'no complex field or landed dimension selector; only the frozen selector theorems conclude on d; no '
                'native gate concluded%s%s' % (tag, (' %s' % bad6[:4]) if bad6 else ''), not bad6)
    others = inventory(inv_files)[0]
    clash, seen, dup = [], {}, []
    for m in MODULES:
        mod = mods.get(m) or ''
        names, spaces = inventory(inv_files + [mod])
        msc = scopes_at(mod)
        for kind, name in decls(mod):
            sc = msc.get(name, ([], [], []))
            if resolve(name, visible(sc[1], sc[2], spaces), others):
                clash.append(name)
            if name in seen:
                dup.append(name)
            seen[name] = m
    imports_ok_ = all(re.findall(r'^import .*$', mods.get(m) or '', re.M) == IMPORTS_OF[m] for m in MODULES)
    check('S7', 'no declaration shares a name with a visible OIBridge declaration or another module of the round; '
                'the imports are the frozen ones%s%s' % (tag, (' %s' % (clash + dup)[:4]) if clash or dup else ''),
          not clash and not dup and imports_ok_)
    ph = sorted({p for m in MODULES for p in phrase_hits(comments(mods.get(m)))})
    check('S8', 'the comments of the modules carry none of the frozen phrases%s%s' % (tag, (' %s' % ph) if ph else ''),
          not ph)
    ok9 = True
    for m in MODULES:
        mod = mods.get(m) or ''
        prints = re.findall(r'^#print axioms (\S+)', mod, re.M)
        local = {n for _, n in decls(mod)}
        pnames = [p[len(PREFIX):] for p in prints if p.startswith(PREFIX)]
        ok9 = ok9 and prints == PRINTS[m] and len(PRINTS[m]) == N_PRINTS[m] and len(set(prints)) == N_PRINTS[m] \
            and len(pnames) == N_PRINTS[m] and all(n in local for n in pnames)
    check('S9', 'exactly the frozen #print axioms lines of each module (%s), distinct, each naming a declaration of '
                'its module%s' % (', '.join('%d' % N_PRINTS[m] for m in MODULES), tag), ok9)
    v = verdicts(mods, landed)
    check('V', 'one outcome per cell by the frozen rules: %s%s' % (', '.join(x[0] for x in v), tag),
          all(len(x) == 1 for x in v))


_INV = []


def d_inventory_files():
    """Every OIBridge module at D (read once)."""
    if not _INV:
        r = git('ls-tree', '--name-only', D, LEAN)
        _INV.extend(show(D, p) for p in r.stdout.split() if p.endswith('.lean'))
    return list(_INV)


def module_checks(mods, tag='', landed=None, inv_files=None):
    if landed is None:
        landed = LANDED
    if inv_files is None:
        inv_files = d_inventory_files()
    for m in MODULES:
        mod = mods.get(m)
        if mod is None:
            check('N1', '%s present%s' % (m, tag), False)
            continue
        check('N1', '%s declares exactly its frozen declarations%s' % (m, tag), [list(x) for x in decls(mod)] == DECLS[m])
        check('N2', '%s: the preamble and every context block unchanged and in order%s' % (m, tag),
              '\n/-! ### §A' in mod and '\nimport ' in mod and preamble(mod) == PREAMBLE[m]
              and context_lines(mod) == CONTEXT[m])
        texts = {n: c for n, (_, c, _) in decl_chunks(mod).items()}
        bad = sorted(n for n in TEXTS[m] if texts.get(n) != TEXTS[m][n])
        check('N2', '%s: every frozen statement and definition unchanged%s%s'
              % (m, tag, (' (changed: %s)' % ', '.join(bad[:4])) if bad else ''), not bad)
        c = code_only(mod)
        prints = re.findall(r'^#print axioms (\S+)', mod, re.M)
        check('N3', '%s: no sorry, admit, axiom or native_decide; every frozen #print axioms line present%s' % (m, tag),
              not re.search(r'\bsorry\b|\badmit\b|^\s*axiom\b|native_decide', c, re.M)
              and all(p in prints for p in PRINTS[m]))
    semantic_checks(mods, tag, landed, inv_files)


def imports_ok(d_text, e_text):
    return d_text is not None and e_text is not None and d_text.count(ANCHOR_IMPORT) == 1 and \
        e_text == d_text.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORTS, 1)


def census_want(d_text):
    d = json.loads(d_text)
    fam = d['families']
    k = [i for i, f in enumerate(fam) if f['modules'] == PREV_FAMILY_MODULES]
    if len(k) != 1:
        return None
    want = dict(d)
    want['families'] = fam[:k[0] + 1] + [CENSUS_FAMILY] + fam[k[0] + 1:]
    return json.dumps(want, indent=2, ensure_ascii=False) + '\n'


def census_ok(d_text, e_text):
    try:
        want = census_want(d_text)
    except Exception:
        return False
    return want is not None and e_text == want


def landed_texts(show_d):
    """The landed texts the rules read, from D: NativeGate's header and fields, IsNot, Entangling, GateRel's fields,
    DIM-1's selector statements and its two native gates, the balance lemma, the objects of n5, the declarations the
    block module copies, and the names of the landed declarations whose statements take the native gate."""
    out = {}
    cd, pn = show_d(CD), show_d(PN)
    if not cd or not pn:
        return out
    cch, pch = decl_chunks(cd), decl_chunks(pn)
    ch = cch.get('NativeGate')
    if ch and ch[0] == 'structure':
        out['NativeGate#header'] = norm(def_header(ch[1]))
        out['NativeGate#fields'] = ' '.join(fields(ch[1]))
        for f in GATE_FIELDS:
            v = field_line(ch[1], f)
            if v is not None:
                out['NativeGate#' + f] = v
    for n, kind in (('IsNot', 'structure'), ('Entangling', 'def')):
        if n in cch and cch[n][0] == kind:
            out[n] = norm(cch[n][1])
    ch = pch.get('GateRel')
    if ch and ch[0] == 'structure':
        out['GateRel#fields'] = ' '.join(fields(ch[1]))
        for f in ('relT', 'relC'):
            v = field_line(ch[1], f)
            if v is not None:
                out['GateRel#' + f] = v
    for n in LANDED_CD_THMS:
        if n in cch and cch[n][0] == 'theorem':
            out[n] = norm(cch[n][1])
    for n in LANDED_PN_DEFS:
        if n in pch and pch[n][0] == 'def':
            out[n] = norm(pch[n][1])
    for n in LANDED_PN_THMS:
        if n in pch and pch[n][0] == 'theorem':
            out[n] = norm(pch[n][1])
    ld = line_decls(cd)
    for old in COPY_MAP:
        if ld.get(old) is not None:
            out['copy#' + old] = '\n'.join(ld[old])
    names = set()
    r = git('ls-tree', '--name-only', D, LEAN)
    for p in sorted(r.stdout.split()):
        if p.endswith('.lean'):
            for n, (k, stmt, _) in decl_chunks(show_d(p) or '').items():
                if token('NativeGate', stmt):
                    names.add(n)
    out['nativeGate#names'] = ' '.join(sorted(names))
    return out


def landed_at_d():
    return landed_texts(lambda p: show(D, p))


def modules_at(commit):
    return {m: show(commit, MODPATH[m]) for m in MODULES}


def run_check(commit, freeze):
    r = git('diff', '--name-status', '--no-renames', D, commit)
    rows = [l.split('\t') for l in r.stdout.splitlines() if l]
    exec_rows = {p: s for s, p in rows if not p.startswith(RDIR)}
    rec = {p for s, p in rows if p.startswith(RDIR)}
    check('P', 'delta(D, commit) is exactly the governed execution paths plus the record directory',
          r.returncode == 0 and exec_rows == GOVERNED and rec <= RECORD_FILES and PREREG in rec)
    landed = landed_at_d()
    check('L', 'the landed texts read from D are the frozen ones', landed == LANDED)
    mods = modules_at(commit)
    module_checks(mods, landed=landed)
    note = show(commit, RESULT)
    if note is not None:
        ph = phrase_hits(note, EARNED + NONINF)
        check('S8', 'the result note less the frozen earned reading and non-inference rule carries none of the frozen '
                    'phrases%s' % ((' %s' % ph) if ph else ''), not ph)
        v = verdicts(mods, landed)
        cells = [x[0] for x in v if len(x) == 1]
        toks = note_tokens(note)
        check('V', 'the result note states exactly the computed tokens %s and no other outcome token (found %s)'
              % (cells, toks), len(cells) == 4 and sorted(toks) == sorted(cells))
        allp = cells == [PAR_TOKENS[0], SEL_TOKENS[0], POS_TOKENS[0], REL_TOKENS[0]]
        st = earned_stated(note)
        check('V', 'the result note states the frozen earned reading %s' % ('(all four cells proved)' if allp else
                                                                             'not at all (a cell not established)'),
              all(st) if allp else not any(st))
        check('V', 'the result note states the frozen non-inference rule',
              all(phrase_norm(n) in phrase_norm(note) for n in NONINF))
    check('I', 'OIBridge.lean is D\'s with exactly the four frozen import lines', imports_ok(show(D, IMPORTS),
                                                                                         show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family after the ODD-CHAR-1 family',
          census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def print_verdicts(commit):
    mods = modules_at(commit)
    landed = landed_at_d()
    v = verdicts(mods, landed)
    for lab, x in zip(('PAR', 'SEL', 'POS', 'REL'), v):
        print('VERDICT  %s  %s' % (lab, '/'.join(x) or 'none'))
    check('V', 'the landed texts read from D are the frozen ones', landed == LANDED)
    check('V', 'exactly one outcome per cell', all(len(x) == 1 for x in v))
