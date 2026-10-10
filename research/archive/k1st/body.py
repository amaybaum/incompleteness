PREFIX = 'OIBridge.SharpTests.'
# S1 -- the predicate
PRED = 'HasTwoSharpTests'
PRED_BODY = ('∃ e f : V →ᵃ[ℝ] ℝ, SharpSeed Ω e ∧ SharpSeed Ω f ∧ (∃ x ∈ Ω, f x ≠ e x) ∧ '
             '(∃ x ∈ Ω, f x ≠ 1 - e x)')
# S2 -- the classification: name -> (explicit binders, conclusion, names its proof must use)
CLASS = {
    'sharpEff_neg_apply': ('(b x : Fin d → ℝ)', 'sharpEff (-b) x = 1 - sharpEff b x', ()),
    'sharpSeed_eq_sharpEff': ('(h : SharpSeed (eball d) e)',
                              '∃ u : Fin d → ℝ, ∑ j, u j ^ 2 = 1 ∧ e = sharpEff u', ('sharp_eq_of_certain',)),
    'sharpSeed_iff': ('(e : (Fin d → ℝ) →ᵃ[ℝ] ℝ)',
                      'SharpSeed (eball d) e ↔ ∃ u : Fin d → ℝ, ∑ j, u j ^ 2 = 1 ∧ e = sharpEff u',
                      ('sharpSeed_eq_sharpEff', 'sharpEff_sharpSeed')),
    'not_sharpSeed_zero': ('(e : (Fin 0 → ℝ) →ᵃ[ℝ] ℝ)', '¬ SharpSeed (eball 0) e', ()),
    'not_hasTwoSharpTests_zero': ('', '¬ HasTwoSharpTests (eball 0)', ('not_sharpSeed_zero',)),
    'eq_or_compl_one': ('(he : SharpSeed (eball 1) e) (hf : SharpSeed (eball 1) f)',
                        '(∀ x ∈ eball 1, f x = e x) ∨ (∀ x ∈ eball 1, f x = 1 - e x)', ('sharpSeed_eq_sharpEff',)),
    'not_hasTwoSharpTests_one': ('', '¬ HasTwoSharpTests (eball 1)', ('eq_or_compl_one',)),
    'hasTwoSharpTests_of_two_le': ('(hd : 2 ≤ d)', 'HasTwoSharpTests (eball d)', ('sharpEff_sharpSeed',)),
    'hasTwoSharpTests_iff': ('', 'HasTwoSharpTests (eball d) ↔ 2 ≤ d',
                             ('not_hasTwoSharpTests_zero', 'not_hasTwoSharpTests_one', 'hasTwoSharpTests_of_two_le')),
}
CLASS_PRINTED = ('sharpEff_neg_apply', 'sharpSeed_iff', 'not_sharpSeed_zero', 'not_hasTwoSharpTests_zero',
                 'eq_or_compl_one', 'not_hasTwoSharpTests_one', 'hasTwoSharpTests_of_two_le', 'hasTwoSharpTests_iff')
CLASS_VERDICT = 'k1sharp_classified'
CLASS_VERDICT_CONCL = (
    '(∀ (d : ℕ) (b x : Fin d → ℝ), sharpEff (-b) x = 1 - sharpEff b x) ∧ '
    '(∀ (d : ℕ) (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ), SharpSeed (eball d) e ↔ ∃ u : Fin d → ℝ, ∑ j, u j ^ 2 = 1 ∧ '
    'e = sharpEff u) ∧ (∀ e : (Fin 0 → ℝ) →ᵃ[ℝ] ℝ, ¬ SharpSeed (eball 0) e) ∧ '
    '(∀ e f : (Fin 1 → ℝ) →ᵃ[ℝ] ℝ, SharpSeed (eball 1) e → SharpSeed (eball 1) f → '
    '(∀ x ∈ eball 1, f x = e x) ∨ (∀ x ∈ eball 1, f x = 1 - e x)) ∧ '
    '(∀ d : ℕ, 2 ≤ d → HasTwoSharpTests (eball d)) ∧ (∀ d : ℕ, HasTwoSharpTests (eball d) ↔ 2 ≤ d)')
# S3 -- the non-implication
CONTROL = 'two_le_load_bearing_relative'
CONTROL_CONCL = ('EffectsOn (eball 1) (fullEffects (eball 1)) ∧ PreservesBody (eball 1) (fullAut 1) ∧ '
                 'SharpSeed (eball 1) (sharpEff z1) ∧ BoundaryTransitive (eball 1) (fullAut 1) ∧ '
                 'SeedOrbitAvailable (fullAut 1) (sharpEff z1) (fullEffects (eball 1)) ∧ '
                 'IsNot (eball 1) z1 neg1 ∧ NativeGateOf (eball 1) (fullEffects (eball 1)) z1 neg1 cnot1 ∧ '
                 '¬ (2 ≤ 1)')
GATE = ('nativeGateOf_cnot1', 'NativeGateOf (eball 1) (fullEffects (eball 1)) z1 neg1 cnot1')
NOT_IMPLIED = 'two_le_not_implied'
QUANT = ('∀ (d : ℕ) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))) '
         '(r : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (T : W d ≃ₗ[ℝ] W d), ')
NOT_IMPLIED_CONCL = '¬ (' + QUANT + ' → '.join(SEL_TYPES) + ' → 2 ≤ d)'
NI_VERDICT = 'k1sharp_two_le_not_implied'
NI_VERDICT_CONCL = '(' + CONTROL_CONCL + ') ∧ ' + NOT_IMPLIED_CONCL
CELL2_OBJECTS = ('NativeGateOf', 'IsNot', 'EffectsOn', 'PreservesBody', 'BoundaryTransitive', 'SeedOrbitAvailable',
                 'fullAut', 'fullEffects', 'cnot1', 'neg1', 'z1', 'W')
# S4 -- scope
FORBIDDEN_OBJECTS = ('Entangling', 'EntanglingOf')
PRED_ARG = re.compile(r'HasTwoSharpTests\s+(?!\(eball\s)')
# S5 -- reuse
REUSED = ('SharpSeed', 'IsEffectOn', 'EffectsOn', 'PreservesBody', 'BoundaryTransitive', 'SeedOrbitAvailable',
          'NativeGate', 'NativeGateOf', 'IsNot', 'eball', 'sharpEff', 'sharpVec', 'sharpEff_apply', 'sharpEff_self',
          'sharpEff_sharpSeed', 'sharpEff_isEffectOn', 'sharp_eq_of_certain', 'mem_eball_of_sphere', 'fullAut',
          'fullEffects', 'preservesBody_fullAut', 'boundaryTransitive_fullAut', 'isEffectOn_seedTransport',
          'maxConeOf', 'maxConeOf_fullEffects', 'maxCone', 'z1', 'neg1', 'cnot1', 'isNot_neg1', 'nativeGate_cnot1',
          'W', 'axisVec', 'axisVec_sq', 'seedTransport', 'dim_of_nativeGateOf', 'three_of_nativeGateOf')
IMPORT_ONLY = 'import OIBridge.K1Bridge'
# S6 -- neutral
NEUTRAL_TOKENS = ('ℂ', 'Complex', 'RCLike', 'conjTranspose', 'ᴴ', 'PosSemidef', 'trace', 'qubit', 'Bloch', 'Pauli',
                  'density', 'flow', 'Flow', 'LimitClosed', 'closure', 'Tendsto', 'Filter', 'Dense', 'TensorProduct',
                  'Hilbert', 'MixingClosed', 'commutator', 'Commute')
# S7 -- phrases
PHRASES = ('OI supplies', 'supplied by OI', 'derived from OI', 'sourced from OI', 'StageCompletion supplies',
           'supplied by StageCompletion', 'the observer architecture supplies', 'supplied by the observer architecture',
           'establishes complementarity', 'complementarity is derived', 'is complementarity', 'quantumness',
           'nonclassicality', 'non-classicality', 'establishes incompatibility', 'establishes noncommutativity',
           'every classical theory has', 'equivalent to entanglement', 'implies entanglement',
           'entanglement follows', 'on every convex body', 'for every convex body', 'derives 2 ≤ d',
           '2 ≤ d is derived', '2 ≤ d is sourced', 'qubit')
# S8 -- separation
TWO_LE_RE = re.compile(r'2\s*≤\s*d(?![\w\'])')
TWO_LE_SECTIONS = ('§C', '§D', 'verdict')
# V -- the frozen decision rule
CLASS_TOKENS = ('K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED', 'K1-SHARP-TEST-MULTIPLICITY-NOT-CLASSIFIED')
NI_TOKENS = ('K1-TWO-LE-NOT-IMPLIED', 'K1-TWO-LE-NON-IMPLICATION-NOT-ESTABLISHED')


def stmt_parts(texts, name):
    b, c = split_statement(texts.get(name, ''))
    return norm(b), norm(c)


def explicit_binders(b):
    """The binders with every implicit `{...}` group removed: the classification ignores how the variables bind."""
    return norm(re.sub(r'\{[^{}]*\}', ' ', b))


def def_body(text):
    j = text.find(' :=')
    return norm(text[j + 3:]) if j != -1 else ''


def binder_types(b):
    """The types of the top-level `( ... : T)` binder groups of an explicit binder string, in order."""
    out, depth, start = [], 0, None
    for i, c in enumerate(b):
        if c == '(':
            if depth == 0:
                start = i
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0 and start is not None:
                grp = b[start + 1:i]
                j = grp.find(' : ')
                if j != -1:
                    out.append(norm(grp[j + 3:]))
                start = None
    return out


def selector_types(text):
    """The explicit hypothesis types of the landed relative selector, `2 ≤ d` removed."""
    chunks = decl_chunks(text)
    if SELECTOR_NAME not in chunks:
        return None
    b, c = split_statement(chunks[SELECTOR_NAME][1])
    if norm(c) != 'd = 3':
        return None
    return [t for t in binder_types(explicit_binders(b)) if t != '2 ≤ d']


def classified_cell(chunks):
    """K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED iff: `HasTwoSharpTests` is the frozen definition; every classification
    theorem has exactly its frozen explicit binders and conclusion and names its frozen proof dependencies (the
    equivalence its three directional witnesses); and the cell's verdict has its frozen conclusion. Otherwise
    K1-SHARP-TEST-MULTIPLICITY-NOT-CLASSIFIED. Reads no selector statement."""
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    proofs = {n: p for n, (_, _, p) in chunks.items()}
    ok = kinds.get(PRED) == 'def' and def_body(texts.get(PRED, '')) == norm(PRED_BODY)
    for n, (b, c, deps) in CLASS.items():
        bb, cc = stmt_parts(texts, n)
        ok = ok and kinds.get(n) == 'theorem' and explicit_binders(bb) == norm(b) and cc == norm(c) and \
            all(token(m, proofs.get(n, '')) for m in deps)
    ok = ok and kinds.get(CLASS_VERDICT) == 'theorem' and stmt_parts(texts, CLASS_VERDICT)[1] == norm(CLASS_VERDICT_CONCL)
    return [CLASS_TOKENS[0] if ok else CLASS_TOKENS[1]]


def not_implied_cell(chunks):
    """K1-TWO-LE-NOT-IMPLIED iff: the d = 1 control, the gate instance and the non-implication are theorems with their
    frozen conclusions, the non-implication's hypothesis chain being the landed selector's hypotheses other than
    `2 ≤ d` (frozen from D); the non-implication's proof names the control; and the cell's verdict has its frozen
    conclusion. Otherwise K1-TWO-LE-NON-IMPLICATION-NOT-ESTABLISHED. Reads no classification statement."""
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    proofs = {n: p for n, (_, _, p) in chunks.items()}
    ok = len(SEL_TYPES) == 7
    for n, c in ((CONTROL, CONTROL_CONCL), GATE, (NOT_IMPLIED, NOT_IMPLIED_CONCL), (NI_VERDICT, NI_VERDICT_CONCL)):
        bb, cc = stmt_parts(texts, n)
        ok = ok and kinds.get(n) == 'theorem' and explicit_binders(bb) == '' and cc == norm(c)
    ok = ok and token(CONTROL, proofs.get(NOT_IMPLIED, ''))
    return [NI_TOKENS[0] if ok else NI_TOKENS[1]]


def verdicts(chunks):
    return classified_cell(chunks), not_implied_cell(chunks)


def semantic_checks(mod, chunks, prints, tag):
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    proofs = {n: p for n, (_, _, p) in chunks.items()}
    code = code_only(mod)
    # S1
    ok1 = kinds.get(PRED) == 'def' and texts.get(PRED) == TEXTS.get(PRED) and \
        def_body(texts.get(PRED, '')) == norm(PRED_BODY)
    check('S1', 'the predicate is the frozen definition: two sharp seeds separated on states from each other and from '
                'the complement' + tag, ok1)
    # S2
    bad2 = []
    for n, (b, c, deps) in CLASS.items():
        bb, cc = stmt_parts(texts, n)
        if kinds.get(n) != 'theorem' or explicit_binders(bb) != norm(b) or cc != norm(c) or \
                not all(token(m, proofs.get(n, '')) for m in deps):
            bad2.append(n)
    bad2 += [n for n in CLASS_PRINTED if PREFIX + n not in prints]
    if stmt_parts(texts, CLASS_VERDICT)[1] != norm(CLASS_VERDICT_CONCL) or PREFIX + CLASS_VERDICT not in prints:
        bad2.append(CLASS_VERDICT)
    check('S2', 'the classification with its frozen binders, conclusions, proof dependencies and prints; the '
                'equivalence through its three directional witnesses%s%s' % (tag, (' %s' % bad2[:3]) if bad2 else ''),
          not bad2)
    # S3
    bad3 = []
    for n, c in ((CONTROL, CONTROL_CONCL), GATE, (NOT_IMPLIED, NOT_IMPLIED_CONCL), (NI_VERDICT, NI_VERDICT_CONCL)):
        bb, cc = stmt_parts(texts, n)
        if kinds.get(n) != 'theorem' or explicit_binders(bb) != '' or cc != norm(c) or PREFIX + n not in prints:
            bad3.append(n)
    if not token(CONTROL, proofs.get(NOT_IMPLIED, '')):
        bad3.append(NOT_IMPLIED + ' proof')
    check('S3', 'the d = 1 control and the non-implication with their frozen conclusions, over the landed selector\'s '
                'hypotheses%s%s' % (tag, (' %s' % bad3[:3]) if bad3 else ''), not bad3)
    # S4
    bad4 = [t for t in FORBIDDEN_OBJECTS if token(t, code)]
    for m, (k, t, _) in chunks.items():
        if k in ('theorem', 'lemma'):
            if PRED_ARG.search(t):
                bad4.append(m)
            if stmt_parts(texts, m)[1] == norm('2 ≤ d'):
                bad4.append(m)
    check('S4', 'no entangling object; the predicate applied in theorems only to eball; no theorem concluding 2 ≤ d%s%s'
          % (tag, (' %s' % bad4[:3]) if bad4 else ''), not bad4)
    # S5
    local = {n for _, n in decls(mod)}
    clash = sorted(local & set(REUSED))
    imports = re.findall(r'^import .*$', mod, re.M)
    check('S5', 'landed objects reused, not re-declared; the only import is OIBridge.K1Bridge%s%s'
          % (tag, (' %s' % clash[:3]) if clash else ''), not clash and imports == [IMPORT_ONLY])
    # S6
    hits = [t for t in NEUTRAL_TOKENS if token(t, code) or (not t.isidentifier() and t in mod)]
    check('S6', 'field-neutral; no flow, limit, closure or density token%s%s' % (tag, (' %s' % hits) if hits else ''),
          not hits)
    # S7
    ph = phrase_hits(header(mod))
    check('S7', 'the header carries none of the frozen phrases%s%s' % (tag, (' %s' % ph) if ph else ''), not ph)
    # S8
    secs = sections(mod)
    bad8 = []
    for kind, name, start, se, nxt, cend in spans(mod):
        sec = section_at(secs, start)
        body = code_only(mod[start:nxt])
        if (sec in ('§A', '§B', '§C') or name == CLASS_VERDICT) and any(token(t, body) for t in CELL2_OBJECTS):
            bad8.append(name)
        if (sec == '§D' or name == NI_VERDICT) and token(PRED, body):
            bad8.append(name)
        if sec not in TWO_LE_SECTIONS and TWO_LE_RE.search(body):
            bad8.append(name)
    check('S8', 'the cells are separated; 2 ≤ d only in §C, §D and the verdicts%s%s'
          % (tag, (' %s' % bad8[:3]) if bad8 else ''), not bad8)
    # S9
    names = [p[len(PREFIX):] for p in prints if p.startswith(PREFIX)]
    check('S9', 'exactly the %d frozen #print axioms lines, distinct, each naming a declaration of the module%s'
          % (N_PRINTS, tag),
          len(PRINTS) == N_PRINTS and prints == PRINTS and len(set(prints)) == N_PRINTS and len(names) == N_PRINTS
          and all(n in local for n in names))
    # V
    a, b = verdicts(chunks)
    check('V', 'one outcome per cell by the frozen rules: %s, %s%s' % (a, b, tag), len(a) == 1 and len(b) == 1)


def phrase_hits(text):
    t = norm(text).lower()
    return [p for p in PHRASES if p.lower() in t]


def note_tokens(note):
    return [t for t in CLASS_TOKENS + NI_TOKENS if re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(t), note)]


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
    sel = show(D, SELECTOR_SRC)
    check('S3', 'the landed relative selector at D has exactly the frozen hypotheses other than 2 ≤ d',
          sel is not None and selector_types(sel) == SEL_TYPES)
    mod = show(commit, MOD)
    module_checks(mod)
    note = show(commit, RESULT)
    if note is not None:
        ph = phrase_hits(note)
        check('S7', 'the result note carries none of the frozen phrases%s' % ((' %s' % ph) if ph else ''), not ph)
        a, b = verdicts(decl_chunks(mod)) if mod is not None else ([], [])
        toks = note_tokens(note)
        check('V', 'the result note states exactly the computed tokens %s and no other outcome token (found %s)'
              % (a + b, toks), len(a) == 1 and len(b) == 1 and sorted(toks) == sorted(a + b))
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                    show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family after the K2-GUARD-1 family',
          census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def print_verdicts(commit):
    mod = show(commit, MOD)
    a, b = verdicts(decl_chunks(mod)) if mod is not None else ([], [])
    print('VERDICT  CLASSIFIED   %s' % ('/'.join(a) or 'none'))
    print('VERDICT  NOT-IMPLIED  %s' % ('/'.join(b) or 'none'))
    check('V', 'exactly one outcome per cell', len(a) == 1 and len(b) == 1)
