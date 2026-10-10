PREFIX = 'OIBridge.K2Guard.'
# S1 -- the obstruction
FROZEN_WHOLE = ['reflY', 'CandidateCone', 'productSet', 'cnotOrbit', 'idW', 'chainW', 'rotW', 'rotChainW']
REFLY_BODY = 'toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i'
CANDIDATE_BODY = '(∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K) ∧ K ⊆ maxCone (eball 3)'
OBSTRUCTION = ('no_candidateCone_cnot_reflY',
               '(hK : CandidateCone K) (hC : ∀ ω ∈ K, cnot ω ∈ K) (hR : ∀ ω ∈ K, actT reflY ω ∈ K)', 'False')
OBSTRUCTION_PROOF_NAMES = ('chain_eq', 'chain_value')
# S2 -- orientation controls: name -> frozen conclusion
CHAIN = 'cnot (actT reflY (cnot (prodState xplus z3)))'
ROTCHAIN = 'cnot (actT nflip (cnot (prodState xplus z3)))'
PAIR = 'prodEffVal (sharpEff ![-1, 0, 0]) (sharpEff ![0, 0, -1])'
CONTROLS_A = {
    'reflY_mem_eball': 'reflY x ∈ eball 3',
    'det_reflY': 'LinearMap.det reflY = -1',
    'det_nflip': 'LinearMap.det nflip = 1',
    'chain_eq': CHAIN + ' = chainW',
    'chain_value': PAIR + ' chainW = -1 / 2',
    'candidateCone_productSet': 'CandidateCone productSet',
    'reflY_mem_productSet': 'actT reflY ω ∈ productSet',
    'candidateCone_cnotOrbit': 'CandidateCone cnotOrbit',
    'cnot_mem_cnotOrbit': 'cnot ω ∈ cnotOrbit',
    'rotation_chain_value': PAIR + ' (' + ROTCHAIN + ') = 0',
}
ORIENT_VERDICT = 'k2guard_orientation'
ORIENT_CONCL = ('(∀ K : Set (W 3), CandidateCone K → (∀ ω ∈ K, cnot ω ∈ K) → (∀ ω ∈ K, actT reflY ω ∈ K) → False) ∧ '
                'NativeGate (eball 3) z3 nflip cnot ∧ (∀ x ∈ eball 3, reflY x ∈ eball 3) ∧ LinearMap.det reflY = -1 ∧ '
                'LinearMap.det nflip = 1 ∧ (CandidateCone cnotOrbit ∧ ∀ ω ∈ cnotOrbit, cnot ω ∈ cnotOrbit) ∧ '
                '(CandidateCone productSet ∧ ∀ ω ∈ productSet, actT reflY ω ∈ productSet) ∧ '
                + PAIR + ' (' + CHAIN + ') = -1 / 2 ∧ ' + PAIR + ' (' + ROTCHAIN + ') = 0')
# S3 -- the selectors
OG4 = ('(hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) '
       '(hV4 : SeedOrbitAvailable G r avail)')
SELECTORS = {
    'three_of_nativeGate_of_two_le': ('(hd : 2 ≤ d) (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)',
                                      'd = 3', 'dim_of_nativeGate'),
    'three_of_nativeGateOf_of_two_le': ('(hd : 2 ≤ d) (hE : EffectsOn (eball d) avail) ' + OG4 +
                                        ' (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T)',
                                        'd = 3', 'dim_of_nativeGateOf'),
}
TWO_LE = ('two_le_of_entangling', '(hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) '
          '(hE : Entangling (eball d) G)', '2 ≤ d')
LOAD = ('two_le_load_bearing', 'IsNot (eball 1) z1 neg1 ∧ NativeGate (eball 1) z1 neg1 cnot1 ∧ ¬ (2 ≤ 1)')
SATIS = ('two_le_satisfiable', '2 ≤ 3 ∧ IsNot (eball 3) z3 nflip ∧ NativeGate (eball 3) z3 nflip cnot')
ENT_VERDICT = 'k2guard_entangling'
# S4 -- premises
NEVER = ('Entangling', 'NativeGateOf', 'EffectsOn', 'SharpSeed', 'PreservesBody', 'BoundaryTransitive',
         'SeedOrbitAvailable')
WITNESS = ('NativeGate', 'IsNot', 'CandidateCone')
WITNESS_OK = {'two_le_load_bearing', 'two_le_satisfiable', 'candidateCone_productSet', 'candidateCone_cnotOrbit',
              ORIENT_VERDICT, ENT_VERDICT}
# S5 -- reuse
REUSED = ('maxCone', 'maxConeOf', 'EffectsOn', 'NativeGate', 'NativeGateOf', 'Entangling', 'EntanglingOf', 'IsNot',
          'prodState', 'actT', 'actC', 'W', 'HVec', 'eball', 'cnot', 'cnotFun', 'nflip', 'phiW', 'xplus', 'z3', 'z1',
          'neg1', 'cnot1', 'sharpEff', 'sharpVec', 'prodEffVal', 'pairVal', 'ehom', 'hom', 'homMap', 'tens',
          'dim_of_nativeGate', 'three_of_nativeGate', 'dim_of_nativeGateOf', 'three_of_nativeGateOf',
          'nativeGate_cnot', 'nativeGate_cnot1', 'isNot_nflip', 'isNot_neg1', 'cnot_prodState_mem_maxCone',
          'cnot_prodState_xplus_z3', 'sharpEff_isEffectOn', 'maxConeOf_avail_eq', 'IsEffectOn', 'pairVal_tens',
          'actT_tens', 'homMap_hom', 'ehom_dot', 'ehom_affOf')
IMPORT_ONLY = 'import OIBridge.K1Bridge'
# S6 -- neutral
NEUTRAL_TOKENS = ('ℂ', 'Complex', 'RCLike', 'conjTranspose', 'ᴴ', 'PosSemidef', 'trace', 'qubit', 'Bloch', 'Pauli',
                  'density', 'ElementaryDrivability', 'flow', 'Flow', 'LimitClosed', 'closure', 'Tendsto', 'Filter',
                  'Dense', 'TensorProduct', 'Hilbert', 'MixingClosed', 'unitSpan')
# S7 -- phrases
PHRASES = ('OI supplies', 'derived from OI', 'sourced from OI', 'local tomography is derived',
           'physical composite cone is identified', 'physical cone is identified', 'the physical cone is',
           'reflections are forbidden', 'reflections are excluded in every', 'reflections are physically forbidden',
           'K2 is discharged', 'K∞-Act is sourced', 'K∞-Copy is derived', 'is derived from 2 ≤ d',
           '2 ≤ d implies entangl', 'equivalent to the entangling', 'every composite must preserve orientation',
           'all composites must preserve orientation', 'qubit')
# S8 -- scope
SELECTOR_SECTION = '§E'
DIM3 = re.compile(r'(?<![\w\'.])(Fin|eball|W|HVec|maxCone)\s+3(?![\w\'])|(?<![\w\'.])(cnot|nflip|reflY|z3|xplus)'
                  r'(?![\w\'])')
TWO_LE_RE = re.compile(r'2\s*≤\s*d(?![\w\'])')
TWO_LE_SECTIONS = ('§E', '§F', 'verdict')
# V -- the frozen decision rule
ORIENT_TOKENS = ('K2-ORIENTATION-OBSTRUCTION-PROVED', 'K2-ORIENTATION-NOT-ESTABLISHED')
ENT_TOKENS = ('K1-ENTANGLING-WEAKENED', 'K1-ENTANGLING-NOT-WEAKENED')


def stmt_parts(texts, name):
    b, c = split_statement(texts.get(name, ''))
    return norm(b), norm(c)


def explicit_binders(b):
    """The binders with every implicit `{...}` group removed: the classification ignores how the variables bind."""
    return norm(re.sub(r'\{[^{}]*\}', ' ', b))


def def_body(text):
    j = text.find(' :=')
    return norm(text[j + 3:]) if j != -1 else ''


def orientation_cell(chunks):
    """K2-ORIENTATION-OBSTRUCTION-PROVED iff: `reflY` is the frozen diag(1, -1, 1) map and `CandidateCone` the frozen
    family; `no_candidateCone_cnot_reflY` is a theorem with exactly the frozen explicit binders and conclusion `False`;
    and every orientation control is a theorem with its frozen conclusion. Otherwise K2-ORIENTATION-NOT-ESTABLISHED.
    Reads no selector statement."""
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    ok = kinds.get('reflY') == 'def' and REFLY_BODY in norm(texts.get('reflY', ''))
    ok = ok and kinds.get('CandidateCone') == 'def' and def_body(texts.get('CandidateCone', '')) == norm(CANDIDATE_BODY)
    n, b, c = OBSTRUCTION
    bb, cc = stmt_parts(texts, n)
    ok = ok and kinds.get(n) == 'theorem' and explicit_binders(bb) == norm(b) and cc == norm(c)
    for m, concl in CONTROLS_A.items():
        ok = ok and kinds.get(m) == 'theorem' and stmt_parts(texts, m)[1] == norm(concl)
    return [ORIENT_TOKENS[0] if ok else ORIENT_TOKENS[1]]


def entangling_cell(chunks):
    """K1-ENTANGLING-WEAKENED iff: both selectors are theorems with exactly the frozen explicit binders and conclusion
    `d = 3`, neither statement mentions `Entangling`; and the load-bearing control `two_le_load_bearing` has its
    frozen conclusion. Otherwise K1-ENTANGLING-NOT-WEAKENED. Reads no orientation statement."""
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    ok = True
    for n, (b, c, _) in SELECTORS.items():
        bb, cc = stmt_parts(texts, n)
        ok = ok and kinds.get(n) == 'theorem' and explicit_binders(bb) == norm(b) and cc == norm(c) and \
            not token('Entangling', texts.get(n, ''))
    ok = ok and kinds.get(LOAD[0]) == 'theorem' and stmt_parts(texts, LOAD[0])[1] == norm(LOAD[1])
    return [ENT_TOKENS[0] if ok else ENT_TOKENS[1]]


def verdicts(chunks):
    return orientation_cell(chunks), entangling_cell(chunks)


def semantic_checks(mod, chunks, prints, tag):
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    proofs = {n: p for n, (_, _, p) in chunks.items()}
    code = code_only(mod)
    # S1
    bad1 = [n for n in FROZEN_WHOLE if texts.get(n) != TEXTS.get(n) or kinds.get(n) not in ('def', 'noncomputable def')]
    if REFLY_BODY not in norm(texts.get('reflY', '')):
        bad1.append('reflY body')
    if def_body(texts.get('CandidateCone', '')) != norm(CANDIDATE_BODY):
        bad1.append('CandidateCone body')
    n, b, c = OBSTRUCTION
    bb, cc = stmt_parts(texts, n)
    if kinds.get(n) != 'theorem' or explicit_binders(bb) != norm(b) or cc != norm(c) or PREFIX + n not in prints or \
            not all(token(m, proofs.get(n, '')) for m in OBSTRUCTION_PROOF_NAMES):
        bad1.append(n)
    check('S1', 'the obstruction over the frozen family with the frozen binders, conclusion False, proved through the '
                'chain%s%s' % (tag, (' %s' % bad1[:3]) if bad1 else ''), not bad1)
    # S2
    bad2 = [m for m, concl in CONTROLS_A.items()
            if kinds.get(m) != 'theorem' or stmt_parts(texts, m)[1] != norm(concl) or PREFIX + m not in prints]
    if stmt_parts(texts, ORIENT_VERDICT)[1] != norm(ORIENT_CONCL):
        bad2.append(ORIENT_VERDICT)
    check('S2', 'the orientation controls with their frozen conclusions and prints%s%s'
          % (tag, (' %s' % bad2[:3]) if bad2 else ''), not bad2)
    # S3
    bad3 = []
    for n, (b, c, dep) in SELECTORS.items():
        bb, cc = stmt_parts(texts, n)
        if kinds.get(n) != 'theorem' or explicit_binders(bb) != norm(b) or cc != norm(c) or \
                not token(dep, proofs.get(n, '')) or token('Entangling', texts.get(n, '')) or PREFIX + n not in prints:
            bad3.append(n)
    n, b, c = TWO_LE
    bb, cc = stmt_parts(texts, n)
    if kinds.get(n) != 'theorem' or explicit_binders(bb) != norm(b) or cc != norm(c):
        bad3.append(n)
    for m, (k, t, _) in chunks.items():
        if k == 'theorem' and m != n and stmt_parts(texts, m)[1] == norm('2 ≤ d'):
            bad3.append(m)
    for m, concl in (LOAD, SATIS):
        if kinds.get(m) != 'theorem' or stmt_parts(texts, m)[1] != norm(concl):
            bad3.append(m)
    check('S3', 'the two 2 ≤ d selectors with the frozen binders, conclusion d = 3, DIM-1 / K1-BRIDGE-1 by name, no '
                'Entangling; 2 ≤ d from the entangling clause only in two_le_of_entangling%s%s'
          % (tag, (' %s' % bad3[:3]) if bad3 else ''), not bad3)
    # S4
    bad4 = []
    for m, (k, t, _) in chunks.items():
        if k in ('theorem', 'lemma'):
            concl = norm(split_statement(t)[1])
        else:
            concl = norm(split_statement(def_header(t))[1])
        if m == ENT_VERDICT:
            for p in NEVER:
                for mm in re.finditer(r'(?<![\w.\'])%s(?![\w\'])' % re.escape(p), concl):
                    rest = concl[mm.end():]
                    j = rest.find(' →')
                    if j == -1 or any(s in rest[:j] for s in (' ∧ ', ' ∨ ', ') ∧', ') ∨')):
                        bad4.append(m)
            continue
        if any(token(p, concl) for p in NEVER):
            bad4.append(m)
        if m not in WITNESS_OK and any(token(p, concl) for p in WITNESS):
            bad4.append(m)
    check('S4', 'no premise concluded of a hypothesis-bound object; witnesses only by the named controls%s%s'
          % (tag, (' %s' % bad4[:3]) if bad4 else ''), not bad4)
    # S5
    local = {n for _, n in decls(mod)}
    clash = sorted(local & set(REUSED))
    imports = re.findall(r'^import .*$', mod, re.M)
    check('S5', 'landed objects reused, not re-declared; the only import is OIBridge.K1Bridge%s%s'
          % (tag, (' %s' % clash[:3]) if clash else ''), not clash and imports == [IMPORT_ONLY])
    # S6
    hits = [t for t in NEUTRAL_TOKENS if token(t, code) or (not t.isidentifier() and t in mod)]
    check('S6', 'field-neutral; no drive, flow, limit, closure or density token%s%s' % (tag, (' %s' % hits) if hits else ''),
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
        if sec == SELECTOR_SECTION and DIM3.search(body):
            bad8.append(name)
        if sec not in TWO_LE_SECTIONS and TWO_LE_RE.search(body):
            bad8.append(name)
    check('S8', 'the selector section is dimension-generic; 2 ≤ d only in §E, §F and the verdicts%s%s'
          % (tag, (' %s' % bad8[:3]) if bad8 else ''), not bad8)
    # S9
    names = [p[len(PREFIX):] for p in prints if p.startswith(PREFIX)]
    check('S9', 'exactly the %d frozen #print axioms lines, distinct, each naming a declaration of the module%s'
          % (N_PRINTS, tag),
          len(PRINTS) == N_PRINTS and prints == PRINTS and len(set(prints)) == N_PRINTS and len(names) == N_PRINTS
          and all(n in local for n in names))
    # V
    o, e = verdicts(chunks)
    check('V', 'one outcome per cell by the frozen rules: %s, %s%s' % (o, e, tag), len(o) == 1 and len(e) == 1)


def phrase_hits(text):
    t = norm(text).lower()
    return [p for p in PHRASES if p.lower() in t]


def note_tokens(note):
    return [t for t in ORIENT_TOKENS + ENT_TOKENS if re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(t), note)]


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
        o, e = verdicts(decl_chunks(mod)) if mod is not None else ([], [])
        toks = note_tokens(note)
        check('V', 'the result note states exactly the computed tokens %s and no other outcome token (found %s)'
              % (o + e, toks), len(o) == 1 and len(e) == 1 and sorted(toks) == sorted(o + e))
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                    show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family after the K1-BRIDGE-1 family',
          census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def print_verdicts(commit):
    mod = show(commit, MOD)
    o, e = verdicts(decl_chunks(mod)) if mod is not None else ([], [])
    print('VERDICT  ORIENTATION  %s' % ('/'.join(o) or 'none'))
    print('VERDICT  ENTANGLING   %s' % ('/'.join(e) or 'none'))
    check('V', 'exactly one outcome per cell', len(o) == 1 and len(e) == 1)

