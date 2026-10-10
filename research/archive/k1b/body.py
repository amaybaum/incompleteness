PREFIX = 'OIBridge.K1Bridge.'
# OG-1's four named hypotheses, as they bind in the module (G, r, avail from the section `variable`)
OG4 = ('(hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) '
       '(hV4 : SeedOrbitAvailable G r avail)')
HD = '(hd : 0 < d)'
HE = '(hE : EffectsOn (eball d) avail)'
HN = '(hN : IsNot (eball d) z N)'
HT = '(hT : NativeGateOf (eball d) avail z N T)'
HENT = '(hEnt : EntanglingOf (eball d) avail T)'
SEL_BINDERS = HD + ' ' + HE + ' ' + OG4 + ' ' + HN + ' ' + HT
DIM_CONCL = 'd = 1 ∨ d = 3'
THREE_CONCL = 'd = 3'
SELECTORS = {'dim_of_nativeGateOf': (SEL_BINDERS, DIM_CONCL),
             'three_of_nativeGateOf': (SEL_BINDERS + ' ' + HENT, THREE_CONCL)}
SEL_FORBIDDEN = ('MixingClosed', 'unitEff', 'fullEffects', 'sharpFamily', 'unitSpan')
# S1 -- the relative forms
NG_FIELDS = ['frame', 'posFwd', 'posInv', 'relT', 'relC']
CONE_FIELDS = ('posFwd', 'posInv')
G_TO_T = re.compile(r"(?<![\w.'])G(?![\w'])")
JOINT_BODY = '{ω | ω ∈ maxConeOf avail ∧ ω 0 0 = 1}'
# S3 -- transparent composition
TRANSPARENT = {
    'nativeGate_of_avail': ('maxConeOf_avail_eq', 'nativeGate_of_cone_eq'),
    'entangling_of_avail': ('maxConeOf_avail_eq', 'entangling_of_cone_eq'),
    'dim_of_nativeGateOf': ('dim_of_nativeGate', 'nativeGate_of_avail'),
    'three_of_nativeGateOf': ('three_of_nativeGate', 'nativeGate_of_avail', 'entangling_of_avail'),
}
DIM_ARGUMENT_TOKENS = ('finrank', 'plusSpace', 'minusSpace', 'tangentPlus', 'BlockData', 'blockData_of_nativeGate',
                       'p_le_one_of_blockData', 'finrank_plus_eq_finrank_minus', 'not_even_of_nativeGate', 'Even',
                       'Odd', 'lor_face', 'corner_form', 'gate_corner', 'gt_corner', 'Phi', 'NativeGateBall',
                       'eigenspace', 'parity', 'not_entangling_one', 'omega')
# S4 -- premises concluded only of named witnesses
PREMISES = ('SharpSeed', 'PreservesBody', 'BoundaryTransitive', 'SeedOrbitAvailable', 'EffectsOn', 'IsNot',
            'NativeGateOf', 'EntanglingOf', 'MixingClosed')
AXIS_CONCL = 'EffectsOn (eball 3) axisFamily ∧ maxConeOf axisFamily ≠ maxCone (eball 3)'
ZERO_CONCL = 'maxConeOf (sharpFamily 0) ≠ maxCone (eball 0)'
WITNESS_THEOREMS = {'cone_eq_fails_axis': AXIS_CONCL}
TRANSPORT = {'NativeGate': ('nativeGate_of_cone_eq', 'nativeGate_of_avail'),
             'Entangling': ('entangling_of_cone_eq', 'entangling_of_avail')}
TRANSPORT_FROM = {'NativeGate': 'NativeGateOf', 'Entangling': 'EntanglingOf'}
VERDICT = 'k1b_core'
# S5 -- reuse
REUSED = ('maxCone', 'maxConeOf', 'EffectsOn', 'NativeGate', 'Entangling', 'jointStates', 'IsProduct', 'IsNot',
          'prodState', 'corner', 'actT', 'actC', 'W', 'eball', 'sharpFamily', 'axisFamily', 'dim_of_nativeGate',
          'three_of_nativeGate', 'maxConeOf_avail_eq', 'maxConeOf_sharpFamily_zero_ne', 'maxConeOf_axis_ne',
          'unitEff', 'isEffectOn_unitEff', 'sharpEff_isEffectOn', 'PreservesBody', 'SharpSeed',
          'BoundaryTransitive', 'SeedOrbitAvailable', 'IsEffectOn', 'prodEffVal', 'sharpEff', 'fullEffects')
IMPORT_ONLY = 'import OIBridge.EffectSpace'
# S6 -- field-neutral, no drive, no limit closure, no mixing closure
NEUTRAL_TOKENS = ('ℂ', 'Complex', 'RCLike', 'conjTranspose', 'ᴴ', 'PosSemidef', 'trace', 'qubit', 'Bloch', 'Pauli',
                  'density', 'ElementaryDrivability', 'flow', 'Flow', 'rot3', 'J_off_axis', 'LimitClosed', 'closure',
                  'Tendsto', 'Filter', 'TensorProduct', 'Hilbert', 'MixingClosed', 'unitSpan')
CONTROL_ONLY_TOKENS = ('unitEff', 'axisFamily', 'isEffectOn_unitEff', 'sharpEff_isEffectOn', 'sharpFamily')
# S7 -- phrases
PHRASES = ('OI supplies', 'derived from OI', 'sourced from OI', 'mixing closure is derived',
           'local tomography is derived', 'product form is derived', 'product-test completeness is derived',
           'composite premise is discharged', 'K2 is discharged', 'qubit effect space', 'selects d = 3 from OI')
# S8 -- dimension
HD_ONLY = sorted(['nativeGate_of_avail', 'entangling_of_avail', 'dim_of_nativeGateOf', 'three_of_nativeGateOf',
                  'k1b_core'])
HD_RE = re.compile(r'0\s*<\s*d(?![\w\'])|(?<![\w\'])d\s*>\s*0|1\s*≤\s*d(?![\w\'])|(?<![\w\'])d\s*≥\s*1'
                   r'|d\s*≠\s*0')
CONTROL_SECTIONS = ('§D', 'verdict')
DIM3 = re.compile(r'(?<![\w\'.])(Fin|eball|W|HVec|sharpFamily|fullAut|fullEffects|maxCone)\s+3(?![\w\'])'
                  r'|(?<![\w\'.])(ball3|eball_three)(?![\w\'])')
# V -- the frozen decision rule
TOKENS = ('K1-EFFECT-AVAILABILITY-DISCHARGED', 'K1-BRIDGE-NOT-ESTABLISHED')


def stmt_parts(texts, name):
    b, c = split_statement(texts.get(name, ''))
    return norm(b), norm(c)


def explicit_binders(b):
    """The binders with every implicit `{...}` group removed: the classification ignores how the variables bind."""
    return norm(re.sub(r'\{[^{}]*\}', ' ', b))


def theorems_with(texts, kinds, binders, concl):
    out = []
    for n, t in texts.items():
        if kinds.get(n) != 'theorem':
            continue
        bb, cc = stmt_parts(texts, n)
        if explicit_binders(bb) == norm(binders) and cc == norm(concl):
            out.append(n)
    return sorted(out)


def relative_field(name):
    """DIM-1's field with the gate renamed `T` and, in the two positivity clauses, `maxConeOf avail` for
    `maxCone Ω`."""
    line = field_line(DIM1_NATIVEGATE, name)
    if line is None:
        return None
    line = G_TO_T.sub('T', line)
    if name in CONE_FIELDS:
        line = line.replace('maxCone Ω', 'maxConeOf avail')
    return norm(line)


def def_body(text):
    j = text.find(' :=')
    return norm(text[j + 3:]) if j != -1 else ''


def relative_ok(chunks):
    """S1: the three relative forms are DIM-1's with the family's cone and nothing else changed."""
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    ng = texts.get('NativeGateOf', '')
    if kinds.get('NativeGateOf') != 'structure' or fields(ng) != NG_FIELDS or fields(DIM1_NATIVEGATE) != NG_FIELDS:
        return False
    if any(field_line(ng, f) != relative_field(f) for f in NG_FIELDS):
        return False
    head = norm(def_header(ng))
    if '(avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ))' not in head or '(T : W d ≃ₗ[ℝ] W d)' not in head or \
            'maxCone Ω' in norm(ng):
        return False
    if kinds.get('jointStatesOf') != 'def' or def_body(texts.get('jointStatesOf', '')) != JOINT_BODY or \
            def_body(DIM1_JOINTSTATES).replace('maxCone Ω', 'maxConeOf avail') != JOINT_BODY:
        return False
    want = G_TO_T.sub('T', def_body(DIM1_ENTANGLING)).replace('jointStates Ω', 'jointStatesOf avail')
    if kinds.get('EntanglingOf') != 'def' or def_body(texts.get('EntanglingOf', '')) != want or \
            'jointStatesOf avail' not in want:
        return False
    return True


def verdicts(chunks):
    """The frozen decision rule, read from the module's statements alone.

    K1-EFFECT-AVAILABILITY-DISCHARGED  the relative forms are DIM-1's with the family's cone (S1); a theorem with
                                       explicit binders exactly `0 < d`, effect soundness, OG-1's four hypotheses,
                                       `IsNot` and `NativeGateOf` concludes `d = 1 ∨ d = 3`; one with `EntanglingOf`
                                       added concludes `d = 3`; and the two controls are theorems with their frozen
                                       statements: `cone_eq_fails_zero` and `cone_eq_fails_axis`
    K1-BRIDGE-NOT-ESTABLISHED          otherwise"""
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    ok = relative_ok(chunks)
    for n, (b, c) in SELECTORS.items():
        ok = ok and n in theorems_with(texts, kinds, b, c)
    ok = ok and kinds.get('cone_eq_fails_zero') == 'theorem' and \
        stmt_parts(texts, 'cone_eq_fails_zero') == ('', norm(ZERO_CONCL))
    ok = ok and kinds.get('cone_eq_fails_axis') == 'theorem' and \
        stmt_parts(texts, 'cone_eq_fails_axis') == ('', norm(AXIS_CONCL))
    return [TOKENS[0] if ok else TOKENS[1]]


def hd_violations(texts):
    return sorted(n for n, t in texts.items() if HD_RE.search(code_only(t)))


def numeral3_violations(mod):
    secs = sections(mod)
    bad = []
    sp = spans(mod)
    first = sp[0][2] if sp else len(mod)
    if DIM3.search(code_only(mod[:first])):
        bad.append('preamble')
    for kind, name, start, se, nxt, cend in sp:
        if section_at(secs, start) in CONTROL_SECTIONS:
            continue
        if DIM3.search(code_only(mod[start:nxt])) or any(token(t, code_only(mod[start:nxt]))
                                                          for t in CONTROL_ONLY_TOKENS):
            bad.append(name)
    return bad


def semantic_checks(mod, chunks, prints, tag):
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    proofs = {n: p for n, (_, _, p) in chunks.items()}
    code = code_only(mod)
    # S1
    check('S1', 'NativeGateOf, jointStatesOf and EntanglingOf are DIM-1\'s forms with the family\'s cone and '
                'nothing else changed' + tag, relative_ok(chunks))
    # S2
    bad2 = []
    for n, (b, c) in SELECTORS.items():
        if kinds.get(n) != 'theorem' or n not in theorems_with(texts, kinds, b, c) or PREFIX + n not in prints:
            bad2.append(n)
        if any(token(t, texts.get(n, '')) for t in SEL_FORBIDDEN):
            bad2.append(n)
    check('S2', 'the two relative selectors with exactly `0 < d`, effect soundness, the four hypotheses, IsNot and '
                'NativeGateOf (and EntanglingOf), their frozen conclusions, and no mixing, unit or full-effect token'
                '%s%s' % (tag, (' %s' % bad2[:3]) if bad2 else ''), not bad2)
    # S3
    bad3 = [n for n, names in TRANSPARENT.items()
            if kinds.get(n) != 'theorem' or not all(token(m, proofs.get(n, '')) for m in names)]
    bad3 += [t for t in DIM_ARGUMENT_TOKENS if token(t, code)]
    check('S3', 'each selector is the cone equality, the transport and DIM-1\'s selector by name; no dimension '
                'argument token%s%s' % (tag, (' %s' % bad3[:3]) if bad3 else ''), not bad3)
    # S4
    bad4 = []
    for n, (k, t, _) in chunks.items():
        if k in ('theorem', 'lemma'):
            concl = norm(split_statement(t)[1])
        else:
            concl = norm(split_statement(def_header(t))[1])
        if n in WITNESS_THEOREMS:
            if concl != norm(WITNESS_THEOREMS[n]) or k != 'theorem' or PREFIX + n not in prints:
                bad4.append(n)
            continue
        if n == VERDICT:
            cc = concl.replace(norm(AXIS_CONCL), '')
            for p in PREMISES:
                for m in re.finditer(r'(?<![\w.\'])%s(?![\w\'])' % re.escape(p), cc):
                    rest = cc[m.end():]
                    j = rest.find(' →')
                    if j == -1 or any(s in rest[:j] for s in (' ∧ ', ' ∨ ', ') ∧', ') ∨')):
                        bad4.append(n)
            continue
        for p in PREMISES:
            if token(p, concl):
                bad4.append(n)
        for landed, (a, b) in TRANSPORT.items():
            if token(landed, concl):
                binders = norm(split_statement(t)[0])
                if n not in (a, b) or not token(TRANSPORT_FROM[landed], binders):
                    bad4.append(n)
    check('S4', 'the named premises concluded of no hypothesis-bound object; NativeGate and Entangling concluded '
                'only from their relative forms%s%s' % (tag, (' %s' % bad4[:3]) if bad4 else ''), not bad4)
    # S5
    local = {n for _, n in decls(mod)}
    clash = sorted(local & set(REUSED))
    imports = re.findall(r'^import .*$', mod, re.M)
    check('S5', 'landed objects reused, not re-declared; the only import is OIBridge.EffectSpace%s%s'
          % (tag, (' %s' % clash[:3]) if clash else ''), not clash and imports == [IMPORT_ONLY])
    # S6
    hits = [t for t in NEUTRAL_TOKENS if token(t, code) or (not t.isidentifier() and t in mod)]
    check('S6', 'field-neutral; no drive, flow, limit-closure, mixing-closure or unit-span token%s%s'
          % (tag, (' %s' % hits) if hits else ''), not hits)
    # S7
    ph = phrase_hits(header(mod))
    check('S7', 'the header carries none of the frozen phrases%s%s' % (tag, (' %s' % ph) if ph else ''), not ph)
    # S8
    hd = hd_violations(texts)
    n3 = numeral3_violations(mod)
    check('S8', '`0 < d` in exactly the frozen statements; no dimension-three object or control family outside the '
                'controls and the verdict%s%s'
          % (tag, (' %s %s' % (hd, n3)) if hd != HD_ONLY or n3 else ''), hd == HD_ONLY and not n3)
    # S9
    names = [p[len(PREFIX):] for p in prints if p.startswith(PREFIX)]
    check('S9', 'exactly the %d frozen #print axioms lines, distinct, each naming a declaration of the module%s'
          % (N_PRINTS, tag),
          len(PRINTS) == N_PRINTS and prints == PRINTS and len(set(prints)) == N_PRINTS and len(names) == N_PRINTS
          and all(n in local for n in names))
    # V
    v = verdicts(chunks)
    check('V', 'the verdict by the frozen rule: %s%s' % (v[0], tag), len(v) == 1 and v[0] in TOKENS)


def phrase_hits(text):
    t = norm(text).lower()
    return [p for p in PHRASES if p.lower() in t]


def note_tokens(note):
    return [t for t in TOKENS if re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(t), note)]


def module_checks(mod, tag=''):
    if mod is None:
        check('N1', 'module present' + tag, False)
        return
    check('N1', 'the module declares exactly the frozen declarations' + tag, [list(x) for x in decls(mod)] == DECLS)
    check('N2', 'the preamble unchanged' + tag,
          '\n/-! ### §A' in mod and '\nimport ' in mod and preamble(mod) == PREAMBLE)
    check('N2', 'every context block unchanged and in order' + tag, context_lines(mod) == CONTEXT)
    chunks = decl_chunks(mod)
    texts = {n: c for n, (_, c, _) in chunks.items()}
    bad = sorted(n for n in TEXTS if texts.get(n) != TEXTS[n])
    check('N2', 'every frozen statement, definition and structure unchanged%s%s'
          % (tag, (' (changed: %s)' % ', '.join(bad[:4])) if bad else ''), not bad)
    c = code_only(mod)
    check('N3', 'no sorry, admit, axiom or native_decide' + tag,
          not re.search(r'\bsorry\b|\badmit\b|^\s*axiom\b|native_decide', c, re.M))
    prints = re.findall(r'^#print axioms (\S+)', mod, re.M)
    check('N3', 'every frozen #print axioms line present' + tag, all(p in prints for p in PRINTS))
    semantic_checks(mod, chunks, prints, tag)


def imports_ok(d_text, e_text):
    return d_text is not None and e_text is not None and d_text.count(ANCHOR_IMPORT) == 1 and \
        e_text == d_text.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)


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


def run_check(commit, freeze):
    r = git('diff', '--name-status', '--no-renames', D, commit)
    rows = [l.split('\t') for l in r.stdout.splitlines() if l]
    exec_rows = {p: s for s, p in rows if not p.startswith(RDIR)}
    rec = {p for s, p in rows if p.startswith(RDIR)}
    check('P', 'delta(D, commit) is exactly the governed execution paths plus the record directory',
          r.returncode == 0 and exec_rows == GOVERNED and rec <= RECORD_FILES and PREREG in rec)
    mod = show(commit, MOD)
    module_checks(mod)
    note = show(commit, RESULT)
    if note is not None:
        ph = phrase_hits(note)
        check('S7', 'the result note carries none of the frozen phrases%s' % ((' %s' % ph) if ph else ''), not ph)
        v = verdicts(decl_chunks(mod)) if mod is not None else []
        toks = note_tokens(note)
        check('V', 'the result note states exactly the computed verdict %s and no other outcome token (found %s)'
              % (v, toks), len(v) == 1 and toks == v)
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                    show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family after the EFF-1 family',
          census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def print_verdicts(commit):
    mod = show(commit, MOD)
    v = verdicts(decl_chunks(mod)) if mod is not None else []
    print('VERDICT  %s' % ('/'.join(v) or 'none'))
    check('V', 'exactly one outcome', len(v) == 1)

