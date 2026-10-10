PREFIX = 'OIBridge.EffectSpace.'
# OG-1's four named hypotheses, as they bind in the module (G, r, avail from the section `variable`)
OG4 = ('(hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) '
       '(hV4 : SeedOrbitAvailable G r avail)')
HD = '(hd : 0 < d)'
MIX = '(hU : unitEff d ∈ avail) (hM : MixingClosed avail)'
# S1 -- Q-CONE
CONE_INCL = {
    'maxCone_subset_maxConeOf_sharp': ('', 'maxCone (eball d) ⊆ maxConeOf (sharpFamily d)'),
    'maxConeOf_sharp_subset_maxCone': (HD, 'maxConeOf (sharpFamily d) ⊆ maxCone (eball d)'),
}
CONE_EQ = ('maxConeOf_sharpFamily', HD, 'maxConeOf (sharpFamily d) = maxCone (eball d)')
CONE_CONCL = 'sharpFamily d ⊆ avail ∧ maxConeOf (sharpFamily d) = maxCone (eball d)'
GEN = ('sharpFamily_subset_avail', OG4, 'sharpFamily d ⊆ avail')
# S2 -- Q-SET
UPPER = {
    'effect_eq_affine': ('{e : (Fin d → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn (eball d) e)',
                         '∃ (a : ℝ) (v : Fin d → ℝ), Real.sqrt (∑ j, v j ^ 2) ≤ min a (1 - a) ∧ '
                         '∀ x, e x = a + ∑ j, v j * x j'),
    'isEffectOn_of_affine': ('{e : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {a : ℝ} {v : Fin d → ℝ} '
                             '(hv : Real.sqrt (∑ j, v j ^ 2) ≤ min a (1 - a)) (he : ∀ x, e x = a + ∑ j, v j * x j)',
                             'IsEffectOn (eball d) e'),
}
DECOMP_INCL = {
    'fullEffects_subset_unitSpan': (HD, 'fullEffects (eball d) ⊆ unitSpan (sharpFamily d)'),
    'unitSpan_subset_fullEffects': ('', 'unitSpan (sharpFamily d) ⊆ fullEffects (eball d)'),
}
DECOMP_EQ = ('fullEffects_eq_unitSpan', HD, 'fullEffects (eball d) = unitSpan (sharpFamily d)')
SET_CONCL = 'fullEffects (eball d) ⊆ avail'
COUNTER_CONCL = ('PreservesBody (eball d) (fullAut d) ∧ SharpSeed (eball d) (sharpEff (axisVec hd)) ∧ '
                 'BoundaryTransitive (eball d) (fullAut d) ∧ '
                 'SeedOrbitAvailable (fullAut d) (sharpEff (axisVec hd)) (sharpUnitFamily d) ∧ '
                 'unitEff d ∈ sharpUnitFamily d ∧ EffectsOn (eball d) (sharpUnitFamily d) ∧ '
                 '¬ MixingClosed (sharpUnitFamily d) ∧ ¬ fullEffects (eball d) ⊆ sharpUnitFamily d')
# S3 -- frozen definitions
MAXCONEOF_BODY = '{ω | ∀ e ∈ A, ∀ f ∈ A, 0 ≤ prodEffVal e f ω}'
MIXING_BODY = '∀ e ∈ A, ∀ f ∈ A, ∀ α β : ℝ, 0 ≤ α → 0 ≤ β → α + β ≤ 1 → α • e + β • f ∈ A'
FROZEN_WHOLE = ['maxConeOf', 'MixingClosed', 'EffectsOn', 'unitSpan', 'sharpFamily', 'sharpEff', 'sharpVec',
                'fullAut', 'sharpUnitFamily']
# S4 -- premises concluded only of named witnesses
PREMISES = ('SharpSeed', 'PreservesBody', 'BoundaryTransitive', 'SeedOrbitAvailable', 'MixingClosed', 'EffectsOn')
WITNESS_THEOREMS = {
    'sharpEff_sharpSeed': 'SharpSeed (eball d) (sharpEff b)',
    'preservesBody_fullAut': 'PreservesBody (eball d) (fullAut d)',
    'boundaryTransitive_fullAut': 'BoundaryTransitive (eball d) (fullAut d)',
    'not_fullEffects_of_orbit': COUNTER_CONCL,
}
VERDICT = 'eff1_core'
# S5 -- reuse
REUSED = ('maxCone', 'Lor', 'ehom', 'affOf', 'IsEffectOn', 'fullEffects', 'eball', 'mem_eball', 'SharpSeed',
          'PreservesBody', 'BoundaryTransitive', 'SeedOrbitAvailable', 'seedTransport', 'seedOrbit', 'unitEff',
          'prodEffVal', 'pairVal', 'ballEffect', 'directionalFamily', 'lor_ehom', 'lor_pair_bound')
IMPORT_OK = re.compile(r'^import (OIBridge\.CompositeDimension|OIBridge\.CompositeInterface|Mathlib\.[\w.]+)$')
# S6 -- field-neutral, no drive, no limit closure
NEUTRAL_TOKENS = ('ℂ', 'Complex', 'RCLike', 'conjTranspose', 'ᴴ', 'PosSemidef', 'trace', 'qubit', 'Bloch', 'Pauli',
                  'density', 'ElementaryDrivability', 'flow', 'Flow', 'rot3', 'J_off_axis', 'LimitClosed', 'closure',
                  'Tendsto', 'Filter', 'TensorProduct', 'Hilbert')
# S7 -- phrases
PHRASES = ('OI supplies', 'derived from OI', 'sourced from OI', 'mixing closure is derived',
           'full effect set is derived', 'effect premise is discharged', 'qubit effect space')
# S8 -- dimension
HD_ONLY = sorted(['maxConeOf_sharp_subset_maxCone', 'maxConeOf_sharpFamily', 'cone_of_orbit', 'maxConeOf_avail_eq',
                  'fullEffects_subset_unitSpan', 'fullEffects_eq_unitSpan', 'fullEffects_subset_avail',
                  'avail_eq_fullEffects', 'not_fullEffects_of_orbit', 'axisVec', 'axisVec_sq', 'lor_decomp',
                  'nonneg_of_sharp', 'eff1_core'])
HD_RE = re.compile(r'0\s*<\s*d(?![\w\'])|(?<![\w\'])d\s*>\s*0|1\s*≤\s*d(?![\w\'])|(?<![\w\'])d\s*≥\s*1'
                   r'|d\s*≠\s*0')
CONTROL_SECTIONS = ('§F', 'verdict')
DIM3 = re.compile(r'(?<![\w\'.])(Fin|eball|W|HVec|sharpFamily|fullAut|fullEffects)\s+3(?![\w\'])'
                  r'|(?<![\w\'.])(ball3|eball_three)(?![\w\'])')
NEGATED = ('¬ BoundaryTransitive (eball 3) G',)
# V -- the frozen decision rule
QSET_TOKENS = ('DERIVED-FULL-EFFECTS', 'CONDITIONAL-FULL-EFFECTS', 'INSUFFICIENT-EVEN-WITH-MIXING')
QCONE_TOKENS = ('CONE-DERIVED', 'CONE-CONDITIONAL', 'CONE-INSUFFICIENT')


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


def insufficient_set(concl):
    """A countermodel with the mixing closure: the four hypotheses, the unit and MixingClosed hold positively and
    some effect is missing."""
    c = norm(concl)
    return all(t in c for t in ('PreservesBody', 'SharpSeed', 'BoundaryTransitive', 'SeedOrbitAvailable')) and \
        re.search(r'(?<!¬ )MixingClosed', c) is not None and '¬ fullEffects (eball d) ⊆' in c and \
        '¬ MixingClosed' not in c


def insufficient_cone(concl):
    c = norm(concl)
    return all(t in c for t in ('PreservesBody', 'SharpSeed', 'BoundaryTransitive', 'SeedOrbitAvailable',
                                'EffectsOn')) and \
        re.search(r'(?<!¬ )MixingClosed', c) is not None and '≠ maxCone (eball d)' in c and '¬ MixingClosed' not in c


def verdicts(chunks):
    """The frozen decision rule. Each question's outcome is read from the module's theorem statements alone.

    Q-CONE  CONE-DERIVED       a theorem with binders exactly `(hd : 0 < d)` and OG-1's four hypotheses and
                               conclusion `sharpFamily d ⊆ avail ∧ maxConeOf (sharpFamily d) = maxCone (eball d)`,
                               and the two inclusions of S1
            CONE-CONDITIONAL   the same conclusion only with the unit and `MixingClosed` added to the binders
            CONE-INSUFFICIENT  a theorem concluding a family with the four hypotheses, the unit, `MixingClosed` and
                               `EffectsOn` whose cone is not `maxCone (eball d)`
    Q-SET   DERIVED-FULL-EFFECTS          a theorem with binders exactly `(hd : 0 < d)` and OG-1's four hypotheses
                                          and conclusion `fullEffects (eball d) ⊆ avail`
            CONDITIONAL-FULL-EFFECTS      that conclusion only with the unit and `MixingClosed` added, together with
                                          the countermodel `not_fullEffects_of_orbit` with its frozen conclusion
            INSUFFICIENT-EVEN-WITH-MIXING a theorem concluding a family with the four hypotheses, the unit and
                                          `MixingClosed` and some effect missing
    A question with no outcome, or with more than one, has no verdict."""
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    concls = {n: norm(split_statement(t)[1]) for n, t in texts.items() if kinds.get(n) == 'theorem'}
    incl = all(stmt_parts(texts, n) == (norm(b), norm(c)) and kinds.get(n) == 'theorem'
               for n, (b, c) in CONE_INCL.items())
    cone = []
    if incl and theorems_with(texts, kinds, HD + ' ' + OG4, CONE_CONCL):
        cone.append('CONE-DERIVED')
    if incl and theorems_with(texts, kinds, HD + ' ' + OG4 + ' ' + MIX, CONE_CONCL):
        cone.append('CONE-CONDITIONAL')
    if any(insufficient_cone(c) for c in concls.values()):
        cone.append('CONE-INSUFFICIENT')
    st = []
    if theorems_with(texts, kinds, HD + ' ' + OG4, SET_CONCL):
        st.append('DERIVED-FULL-EFFECTS')
    if theorems_with(texts, kinds, HD + ' ' + OG4 + ' ' + MIX, SET_CONCL) and \
            stmt_parts(texts, 'not_fullEffects_of_orbit') == (HD, norm(COUNTER_CONCL)):
        st.append('CONDITIONAL-FULL-EFFECTS')
    if any(insufficient_set(c) for c in concls.values()):
        st.append('INSUFFICIENT-EVEN-WITH-MIXING')
    return st, cone


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
        if DIM3.search(code_only(mod[start:nxt])):
            bad.append(name)
    return bad


def semantic_checks(mod, chunks, prints, tag):
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    proofs = {n: p for n, (_, _, p) in chunks.items()}
    code = code_only(mod)
    # S1
    bad1 = [n for n, (b, c) in CONE_INCL.items()
            if kinds.get(n) != 'theorem' or stmt_parts(texts, n) != (norm(b), norm(c)) or PREFIX + n not in prints]
    n, b, c = CONE_EQ
    if kinds.get(n) != 'theorem' or stmt_parts(texts, n) != (norm(b), norm(c)) or \
            not all(token(m, proofs.get(n, '')) for m in CONE_INCL):
        bad1.append(n)
    if stmt_parts(texts, 'cone_of_orbit') != (norm(HD + ' ' + OG4), norm(CONE_CONCL)):
        bad1.append('cone_of_orbit')
    if stmt_parts(texts, GEN[0]) != (norm(GEN[1]), norm(GEN[2])):
        bad1.append(GEN[0])
    for m in ('cone_of_orbit', GEN[0]):
        if any(t in texts.get(m, '') for t in ('MixingClosed', 'unitEff', 'EffectsOn')):
            bad1.append(m)
    check('S1', 'Q-CONE: both inclusions with their frozen statements, the equality from both by name, the cone '
                'theorem and the generation theorem on OG-1\'s four hypotheses alone%s%s'
          % (tag, (' %s' % bad1[:3]) if bad1 else ''), not bad1)
    # S2
    bad2 = [n for n, (b, c) in list(UPPER.items()) + list(DECOMP_INCL.items())
            if kinds.get(n) != 'theorem' or stmt_parts(texts, n) != (norm(b), norm(c)) or PREFIX + n not in prints]
    n, b, c = DECOMP_EQ
    if kinds.get(n) != 'theorem' or stmt_parts(texts, n) != (norm(b), norm(c)) or \
            not all(token(m, proofs.get(n, '')) for m in DECOMP_INCL):
        bad2.append(n)
    if stmt_parts(texts, 'fullEffects_subset_avail') != (norm(HD + ' ' + OG4 + ' ' + MIX), norm(SET_CONCL)):
        bad2.append('fullEffects_subset_avail')
    if stmt_parts(texts, 'not_fullEffects_of_orbit') != (HD, norm(COUNTER_CONCL)) or \
            PREFIX + 'not_fullEffects_of_orbit' not in prints:
        bad2.append('not_fullEffects_of_orbit')
    check('S2', 'Q-SET: the upper bound and the decomposition in both directions, the equality from both by name, '
                'the conditional generation on the four hypotheses, the unit and MixingClosed, and the countermodel'
                '%s%s' % (tag, (' %s' % bad2[:3]) if bad2 else ''), not bad2)
    # S3
    check('S3', 'the frozen definitions whole; maxConeOf over the given family; MixingClosed sub-convex' + tag,
          all(texts.get(n) == TEXTS.get(n) and kinds.get(n) in ('def', 'noncomputable def') for n in FROZEN_WHOLE)
          and norm(texts.get('maxConeOf', '')).endswith(':= ' + MAXCONEOF_BODY)
          and norm(texts.get('MixingClosed', '')).endswith(':= ' + MIXING_BODY))
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
            cc = norm(split_statement(t)[1])
            for m in re.finditer(r'MixingClosed (\w+)', cc):
                if not (cc[:m.start()].endswith('¬ ') or cc[m.end():].startswith(' →')):
                    bad4.append(n)
            continue
        for c in NEGATED:
            concl = concl.replace(c, '')
        if any(token(p, concl) for p in PREMISES):
            bad4.append(n)
    check('S4', 'the named premises concluded only of the named witnesses by the named control theorems%s%s'
          % (tag, (' %s' % bad4[:3]) if bad4 else ''), not bad4)
    # S5
    local = {n for _, n in decls(mod)}
    clash = sorted(local & set(REUSED))
    imports = re.findall(r'^import .*$', mod, re.M)
    bad_imp = [l for l in imports if not IMPORT_OK.match(l)]
    check('S5', 'landed objects reused, not re-declared; imports whitelisted%s%s'
          % (tag, (' %s' % (clash + bad_imp)[:3]) if clash or bad_imp else ''),
          not clash and not bad_imp and bool(imports))
    # S6
    hits = [t for t in NEUTRAL_TOKENS if token(t, code) or (not t.isidentifier() and t in mod)]
    check('S6', 'field-neutral; no drive, flow or limit-closure token%s%s' % (tag, (' %s' % hits) if hits else ''),
          not hits)
    # S7
    ph = phrase_hits(header(mod))
    check('S7', 'the header carries none of the frozen phrases%s%s' % (tag, (' %s' % ph) if ph else ''), not ph)
    # S8
    hd = hd_violations(texts)
    n3 = numeral3_violations(mod)
    check('S8', '`0 < d` in exactly the frozen statements; no dimension-three object outside the controls and the '
                'verdict%s%s'
          % (tag, (' %s %s' % (hd, n3)) if hd != HD_ONLY or n3 else ''), hd == HD_ONLY and not n3)
    # S9
    names = [p[len(PREFIX):] for p in prints if p.startswith(PREFIX)]
    check('S9', 'exactly the %d frozen #print axioms lines, distinct, each naming a declaration of the module%s'
          % (N_PRINTS, tag),
          len(PRINTS) == N_PRINTS and prints == PRINTS and len(set(prints)) == N_PRINTS and len(names) == N_PRINTS
          and all(n in local for n in names))
    # V
    st, cone = verdicts(chunks)
    check('V', 'exactly one outcome per question by the frozen rule: Q-SET %s, Q-CONE %s%s'
          % ('/'.join(st) or 'none', '/'.join(cone) or 'none', tag), len(st) == 1 and len(cone) == 1)


def phrase_hits(text):
    t = norm(text).lower()
    return [p for p in PHRASES if p.lower() in t]


def note_tokens(note):
    return [t for t in QSET_TOKENS + QCONE_TOKENS if re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(t), note)]


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
    check('N2', 'every frozen statement and definition unchanged%s%s'
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
        st, cone = verdicts(decl_chunks(mod)) if mod is not None else ([], [])
        toks = note_tokens(note)
        check('V', 'the result note states exactly the computed verdicts %s and no other outcome token (found %s)'
              % (st + cone, toks), len(st) == 1 and len(cone) == 1 and sorted(toks) == sorted(st + cone))
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                    show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family after the DIM-1 family',
          census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def print_verdicts(commit):
    mod = show(commit, MOD)
    st, cone = verdicts(decl_chunks(mod)) if mod is not None else ([], [])
    print('VERDICT  Q-SET   %s' % ('/'.join(st) or 'none'))
    print('VERDICT  Q-CONE  %s' % ('/'.join(cone) or 'none'))
    check('V', 'exactly one outcome per question', len(st) == 1 and len(cone) == 1)

