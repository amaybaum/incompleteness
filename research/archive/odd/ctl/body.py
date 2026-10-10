PREFIX = 'OIBridge.OddChar.'
LANDED_GATE = ('CompositeDimension', 'NativeGate')
LANDED_REL = ('ParityNot', 'GateRel')
# the positivity-free sections read none of these
FREE_OF_POS = ('NativeGate', 'posFwd', 'posInv', 'maxCone', 'prodEffVal', 'IsEffectOn', 'sharpEff')
# S1 -- the family (whole normalized definition texts)
FAM_DEFS = {
    'oddK': 'def oddK (k : ℕ) (μ : Fin (2 * k + 1 + 1)) : Bool := decide (k < (μ : ℕ))',
    'cK': 'def cK (k : ℕ) (j : Fin (2 * k + 1)) : ℝ := if oddK k j.succ then -1 else 1',
    'nK': 'def nK (k : ℕ) : (Fin (2 * k + 1) → ℝ) →ₗ[ℝ] (Fin (2 * k + 1) → ℝ) := diagSign (cK k)',
    'zK': 'def zK (k : ℕ) : Fin (2 * k + 1) → ℝ := fun i => if (i : ℕ) = 2 * k then 1 else 0',
    'gRev': 'def gRev (k : ℕ) : W (2 * k + 1) ≃ₗ[ℝ] W (2 * k + 1) := sgateEquiv (oddK k) Fin.rev Fin.rev_rev',
}
FRAME_SUB = {'G': 'gRev k', 'z': '(zK k)'}
FAM_THEOREMS = {
    'oddK_rev': ('(k : ℕ) (μ : Fin (2 * k + 1 + 1))', 'oddK k (Fin.rev μ) = !oddK k μ', ()),
    'isNot_nK': ('(k : ℕ)', 'IsNot (eball (2 * k + 1)) (zK k) (nK k)', ()),
    'gRev_frame': ('(k : ℕ) (a b : Fin 2)', None, ()),
    'gateRel_gRev': ('(k : ℕ)', 'GateRel (nK k) (gRev k)', ('sgate_relT', 'sgate_relC', 'oddK_rev')),
    'finrank_plus_eq_finrank_minus_nK': ('(k : ℕ)', 'Module.finrank ℝ (plusSpace (nK k)) = '
                                         'Module.finrank ℝ (minusSpace (nK k))', ('finrank_plus_eq_finrank_minus_rel',)),
}
# the landed ParityNot objects the family is built from, read from D
LANDED_SGATE = 'def sgate (odd : Fin (d + 1) → Bool) (p : Fin (d + 1) → Fin (d + 1)) (ω : W d) : W d := ' \
               'fun μ ν => if odd ν then ω (p μ) ν else ω μ ν'
LANDED_DIAG = 'fun i => c i * x i'
LANDED_SGATE_REL = {
    'sgate_relT': '{d : ℕ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {odd : Fin (d + 1) → Bool} '
                  '{p : Fin (d + 1) → Fin (d + 1)} (hN : ∀ (v : HVec d) μ, homMap N v μ = (if odd μ then -1 else 1) '
                  '* v μ) (ω : W d) : actT N (sgate odd p (actT N ω)) = sgate odd p ω',
    'sgate_relC': '{d : ℕ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {odd : Fin (d + 1) → Bool} '
                  '{p : Fin (d + 1) → Fin (d + 1)} (hN : ∀ (v : HVec d) μ, homMap N v μ = (if odd μ then -1 else 1) '
                  '* v μ) (hodd : ∀ μ, odd (p μ) = !odd μ) (ω : W d) : '
                  'actC N (sgate odd p (actC N ω)) = actT N (sgate odd p ω)',
}
# S2 -- the characterization
ODD = 'exists_frame_gateRel_iff_odd'
ODD_BINDERS = '(d : ℕ)'
ODD_HEAD = '(∃ (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d), IsNot (eball d) z N ∧ ('
ODD_TAIL = ') ∧ GateRel N G) ↔ Odd d'
ODD_PROOF = ('not_even_of_gateRel', 'cnot1', 'isNot_neg1', 'cnot1_frame', 'gRev', 'isNot_nK', 'gRev_frame',
             'gateRel_gRev')
ODD_PROOF_D1_REL = (('nativeGate_cnot1',), ('cnot1_relT', 'cnot1_relC'))
LANDED_ODD = {
    'not_even_of_gateRel': '{d : ℕ} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} '
                           '(hN : IsNot (eball d) z N) (hR : GateRel N G) : ¬ Even d',
    'isNot_neg1': ': IsNot (eball 1) z1 neg1',
    'nativeGate_cnot1': ': NativeGate (eball 1) z1 neg1 cnot1',
    'cnot1_relT': '(ω : W 1) : actT neg1 (cnot1 (actT neg1 ω)) = cnot1 ω',
    'cnot1_relC': '(ω : W 1) : actC neg1 (cnot1 (actC neg1 ω)) = actT neg1 (cnot1 ω)',
}
# S3 -- positivity at k >= 1
POS_DEFS = {
    'xK': 'def xK (k : ℕ) : Fin (2 * k + 1) → ℝ := fun i => if (i : ℕ) = 0 then 1 else 0',
    'wK': 'noncomputable def wK (k : ℕ) : Fin (2 * k + 1) → ℝ := fun i => '
          'if (i : ℕ) = 2 * k - 1 then -3 / 5 else if (i : ℕ) = 2 * k then -4 / 5 else 0',
    'entW': 'def entW (p q : Fin (d + 1)) : W d := fun μ ν => if μ = p then (if ν = q then 1 else 0) else 0',
}
HK = '(k : ℕ) (hk : 1 ≤ k)'
BODY = 'eball (2 * k + 1)'
VALUE = '-1 / 10'
POS_THEOREMS = {
    'sum_wK_sq': (HK, '∑ j, wK k j ^ 2 = 1', ()),
    'pairVal_entW': ('(a b : HVec d) (p q : Fin (d + 1))', 'pairVal a b (entW p q) = a p * b q', ()),
    'gRev_value': (HK, 'prodEffVal (sharpEff (wK k)) (sharpEff (zK k)) (gRev k (prodState (xK k) (zK k))) = '
                   + VALUE, ()),
    'gRev_not_mem_maxCone': (HK, 'gRev k (prodState (xK k) (zK k)) ∉ maxCone (%s)' % BODY,
                             ('gRev_value', 'sharpEff_isEffectOn', 'sum_wK_sq', 'sum_zK_sq')),
    'not_posFwd_gRev': (HK, None, ('gRev_not_mem_maxCone',)),
    'not_nativeGate_gRev': (HK, '¬ NativeGate (%s) (zK k) (nK k) (gRev k)' % BODY, ('not_posFwd_gRev',)),
}
SELECTORS = re.compile(r'(?<![\w.\'])\w*_of_nativeGate\w*|(?<![\w.\'])three_of_\w+|(?<![\w.\'])dim_of_\w+')
# S6 -- scope
SCOPE_TOKENS = ('Complex', 'ℂ', 'posInv', 'Entangling', 'dim_of_nativeGate', 'ne_five_of_nativeGate',
                'three_of_nativeGate', 'dim_of_nativeGateOf', 'three_of_nativeGateOf',
                'three_of_nativeGateOf_of_two_le')
D_EQ = re.compile(r'(?<![\w.\'])d\s*(=|≠)\s*\d')
POSITIVE = re.compile(r'(?<![\w.\'])(NativeGate|maxCone|posFwd)(?![\w\'])')
# S7 -- reuse
IMPORT_ONLY = 'import OIBridge.ParityNot'
# S8 -- phrases
PHRASES = ('individually necessary', 'individually load-bearing', 'separately necessary', 'each necessary',
           'posFwd is necessary', 'posInv is necessary', 'forward positivity is necessary',
           'inverse positivity is necessary', 'forward positivity alone', 'inverse positivity alone',
           'posFwd alone', 'posInv alone', 'forward positivity excludes', 'inverse positivity excludes',
           'positivity selects', 'selects d = 3', 'selects `d = 3`', 'forces d = 3', 'forces `d = 3`',
           'd = 3 is forced', 'd = 3 is selected', 'selects the dimension', 'dimension selection',
           'the relations select', 'positive gates are classified', 'classifies the positive', 'classification of '
           'positive', 'only positive gate', 'relT is necessary', 'relC is necessary', 'the frame is necessary',
           'complex structure is', 'yields a complex structure', 'gives a complex structure', 'reconstructs ℂ',
           'reconstructs the complex', 'J² = −1', 'J^2 = -1', 'J² = -1', 'physically carried', 'physical NOT',
           'physically realizable', 'physically realized', 'positivity follows from', 'positivity is derived',
           'implies positivity', 'OI supplies', 'OI provides', 'derived from OI', 'sourced from OI',
           'premise adopted', 'adopts a premise', 'qubit', 'all odd dimensions', 'design (round', 'not for landing')
# V -- the frozen decision rule
FAM_TOKENS = ('ODD-FAMILY-PROVED', 'ODD-FAMILY-NOT-ESTABLISHED')
ODD_TOKENS = ('ODD-CHARACTERIZATION-PROVED', 'ODD-CHARACTERIZATION-NOT-ESTABLISHED')
POS_TOKENS = ('HIGHER-ODD-POSFWD-FAILURE-PROVED', 'HIGHER-ODD-POSFWD-FAILURE-NOT-ESTABLISHED')
ALL_TOKENS = FAM_TOKENS + ODD_TOKENS + POS_TOKENS


def tsub(text, mapping):
    """Token-bounded simultaneous substitution."""
    pat = re.compile(r'(?<![\w.\'])(%s)(?![\w\'])' % '|'.join(re.escape(k) for k in mapping))
    return pat.sub(lambda m: mapping[m.group(1)], text)


def kinds_texts_proofs(mod):
    chunks = decl_chunks(mod)
    return ({n: k for n, (k, _, _) in chunks.items()}, {n: c for n, (_, c, _) in chunks.items()},
            {n: p for n, (_, _, p) in chunks.items()})


def section_decls(mod, labels):
    secs = sections(mod)
    return [(name, mod[start:nxt]) for kind, name, start, se, nxt, cend in spans(mod)
            if section_at(secs, start) in labels]


DOTTED = ('posFwd', 'posInv')


def mentions(text, toks):
    """The tokens the code of `text` mentions; a positivity field also as a projection (`hG.posInv`)."""
    c = code_only(text)
    return [t for t in toks if token(t, c) or (t in DOTTED and re.search(r'(?<![\w\'])%s(?![\w\'])' % t, c))]


def landed_field(landed, owner, f, prefix):
    v = landed.get('%s#%s' % (owner, f))
    return v[len(prefix):] if v is not None and v.startswith(prefix) else None


def landed_frame(landed):
    return landed_field(landed, LANDED_GATE[1], 'frame', 'frame : ')


def relations_bad(landed):
    """The landed GateRel is exactly the landed NativeGate relation fields (read from D)."""
    bad = []
    for f in ('relT', 'relC'):
        a = landed.get('%s#%s' % (LANDED_REL[1], f))
        if a is None or a != landed.get('%s#%s' % (LANDED_GATE[1], f)):
            bad.append('GateRel#' + f + ' at D')
    if landed.get('%s#fields' % LANDED_REL[1]) != 'relT relC':
        bad.append('GateRel fields at D')
    return bad


def theorem_bad(kinds, texts, proofs, n, b, c, deps):
    bb, cc = split_statement(texts.get(n, ''))
    return kinds.get(n) != 'theorem' or norm(bb) != norm(b) or c is None or norm(cc) != norm(c) or \
        not all(token(m, proofs.get(n, '')) for m in deps)


def family_bad(mod, landed):
    """S1: the frozen family definitions; IsNot, the landed frame field and GateRel for every k; the landed GateRel
    and sgate objects at D; §A free of the native gate and positivity."""
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    for n, t in FAM_DEFS.items():
        if kinds.get(n) != 'def' or norm(texts.get(n, '')) != norm(t):
            bad.append(n)
    frame = landed_frame(landed)
    if frame is None or not frame.startswith('∀ a b : Fin 2, '):
        return bad + ['NativeGate#frame at D']
    want_frame = tsub(frame[len('∀ a b : Fin 2, '):], FRAME_SUB)
    for n, (b, c, deps) in FAM_THEOREMS.items():
        if theorem_bad(kinds, texts, proofs, n, b, want_frame if c is None else c, deps):
            bad.append(n)
    bad += relations_bad(landed)
    if landed.get('sgate') != norm(LANDED_SGATE) or landed.get('diagSign#toFun') != LANDED_DIAG:
        bad.append('sgate or diagSign at D')
    for n, e in LANDED_SGATE_REL.items():
        if landed.get(n) != norm(e):
            bad.append(n + ' at D')
    for name, body in section_decls(mod, ('§A',)):
        if mentions(body, FREE_OF_POS):
            bad.append(name)
    return bad


def odd_want(landed):
    frame = landed_frame(landed)
    return None if frame is None else norm(ODD_HEAD + frame + ODD_TAIL)


def odd_bad(mod, landed):
    """S2: the frozen existential equivalent to `Odd d`, the frame clause the landed frame field read from D; the
    proof through the landed parity theorem, the landed d = 1 objects and the family; §B free of the native gate and
    positivity."""
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    want = odd_want(landed)
    b, c = split_statement(texts.get(ODD, ''))
    pr = proofs.get(ODD, '')
    if kinds.get(ODD) != 'theorem' or norm(b) != ODD_BINDERS or want is None or norm(c) != want or \
            not all(token(m, pr) for m in ODD_PROOF) or \
            not any(all(token(m, pr) for m in alt) for alt in ODD_PROOF_D1_REL):
        bad.append(ODD)
    bad += relations_bad(landed)
    for n, e in LANDED_ODD.items():
        if landed.get(n) != norm(e):
            bad.append(n + ' at D')
    f1 = landed.get('cnot1_frame')
    if f1 is None or want is None or f1 != norm('(a b : Fin 2) : ' + tsub(landed_frame(landed)[
            len('∀ a b : Fin 2, '):], {'G': 'cnot1', 'z': 'z1'})):
        bad.append('cnot1_frame at D')
    for name, body in section_decls(mod, ('§B',)):
        if mentions(body, FREE_OF_POS):
            bad.append(name)
    return bad


def positivity_bad(mod, landed):
    """S3: for k >= 1, the frozen witness, the value -1 / 10, the negation of the landed posFwd field at the body and
    the gate through that value; the gate the family's, with its frame and its relations; §C free of the landed
    dimension corollaries and inverse positivity."""
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    for n in ('oddK', 'zK', 'nK', 'gRev'):
        if kinds.get(n) != 'def' or norm(texts.get(n, '')) != norm(FAM_DEFS[n]):
            bad.append(n)
    for n, t in POS_DEFS.items():
        if norm(texts.get(n, '')) != norm(t):
            bad.append(n)
    frame = landed_frame(landed)
    posfwd = landed_field(landed, LANDED_GATE[1], 'posFwd', 'posFwd : ')
    if frame is None or posfwd is None or not frame.startswith('∀ a b : Fin 2, '):
        return bad + ['NativeGate fields at D']
    want_pf = '¬ ' + tsub(posfwd, {'G': 'gRev k', 'Ω': '(%s)' % BODY}).replace('∈ (%s),' % BODY, '∈ %s,' % BODY)
    for n, (b, c, deps) in POS_THEOREMS.items():
        if theorem_bad(kinds, texts, proofs, n, b, want_pf if c is None else c, deps):
            bad.append(n)
    want_frame = tsub(frame[len('∀ a b : Fin 2, '):], FRAME_SUB)
    for n in ('gRev_frame', 'gateRel_gRev'):
        b, c, deps = FAM_THEOREMS[n]
        if theorem_bad(kinds, texts, proofs, n, b, want_frame if c is None else c, ()):
            bad.append(n)
    bad += relations_bad(landed)
    for name, body in section_decls(mod, ('§C',)):
        if SELECTORS.search(code_only(body)) or mentions(body, ('posInv',)):
            bad.append(name)
    return bad


def fam_cell(mod, landed):
    """ODD-FAMILY-PROVED iff S1: for every k, nK k is a NOT of eball (2k+1) with axis zK k, gRev k satisfies the
    landed frame field and GateRel (nK k) (gRev k), the landed GateRel being the landed relation fields, and §A reads
    neither the native gate nor positivity. Otherwise ODD-FAMILY-NOT-ESTABLISHED. Reads no §B-§C statement."""
    return [FAM_TOKENS[1] if family_bad(mod, landed) else FAM_TOKENS[0]]


def odd_cell(mod, landed):
    """ODD-CHARACTERIZATION-PROVED iff S2: the existential of IsNot, the landed frame field and GateRel is
    equivalent to Odd d, proved through the landed parity theorem one way and the landed d = 1 gate and the family the
    other. Otherwise ODD-CHARACTERIZATION-NOT-ESTABLISHED. Reads no §C statement."""
    return [ODD_TOKENS[1] if odd_bad(mod, landed) else ODD_TOKENS[0]]


def pos_cell(mod, landed):
    """HIGHER-ODD-POSFWD-FAILURE-PROVED iff S3: for every k >= 1 the family's gate with its frame and relations
    fails the landed posFwd field at eball (2k+1), through the explicit value -1 / 10, without a landed dimension
    corollary. Otherwise HIGHER-ODD-POSFWD-FAILURE-NOT-ESTABLISHED. Reads no §B statement."""
    return [POS_TOKENS[1] if positivity_bad(mod, landed) else POS_TOKENS[0]]


def verdicts(mod, landed):
    return fam_cell(mod, landed), odd_cell(mod, landed), pos_cell(mod, landed)


def semantic_checks(mod, chunks, prints, tag, landed, inv_files):
    texts = {n: c for n, (_, c, _) in chunks.items()}
    bad1 = family_bad(mod, landed)
    check('S1', 'the family: IsNot, the landed frame field and GateRel for every k; §A free of the native gate and '
                'positivity%s%s' % (tag, (' %s' % bad1[:3]) if bad1 else ''), not bad1)
    bad2 = odd_bad(mod, landed)
    check('S2', 'IsNot, the landed frame field and GateRel exist exactly at odd d, through the landed parity theorem '
                'and the landed d = 1 gate%s%s' % (tag, (' %s' % bad2[:3]) if bad2 else ''), not bad2)
    bad3 = positivity_bad(mod, landed)
    check('S3', 'for k >= 1 the family gate fails the landed posFwd field through the value -1 / 10%s%s'
          % (tag, (' %s' % bad3[:3]) if bad3 else ''), not bad3)
    bad6 = []
    for kind, name, start, se, nxt, cend in spans(mod):
        if mentions(mod[start:nxt], SCOPE_TOKENS):
            bad6.append(name)
        if kind in ('theorem', 'lemma'):
            _, c = split_statement(texts.get(name, ''))
            c = norm(c)
            if D_EQ.search(c) or (POSITIVE.search(c) and not c.startswith('¬') and '∉' not in c):
                bad6.append(name)
    check('S6', 'no complex field, dimension selector, inverse positivity or Entangling; no conclusion on d; no '
                'positive gate conclusion%s%s' % (tag, (' %s' % bad6[:3]) if bad6 else ''), not bad6)
    names, spaces = inventory(inv_files + [mod])
    others = inventory(inv_files)[0]
    msc = scopes_at(mod)
    clash = []
    for kind, name in decls(mod):
        sc = msc.get(name, ([], [], []))
        if resolve(name, visible(sc[1], sc[2], spaces), others):
            clash.append(name)
    imports = re.findall(r'^import .*$', mod, re.M)
    check('S7', 'no declaration shares a name with a visible OIBridge declaration; the only import is '
                'OIBridge.ParityNot%s%s' % (tag, (' %s' % clash[:3]) if clash else ''),
          not clash and imports == [IMPORT_ONLY])
    ph = phrase_hits(header(mod))
    check('S8', 'the header carries none of the frozen phrases%s%s' % (tag, (' %s' % ph) if ph else ''), not ph)
    local = {n for _, n in decls(mod)}
    pnames = [p[len(PREFIX):] for p in prints if p.startswith(PREFIX)]
    check('S9', 'exactly the %d frozen #print axioms lines, distinct, each naming a declaration of the module%s'
          % (N_PRINTS, tag),
          len(PRINTS) == N_PRINTS and prints == PRINTS and len(set(prints)) == N_PRINTS and len(pnames) == N_PRINTS
          and all(n in local for n in pnames))
    a, b, c = verdicts(mod, landed)
    check('V', 'one outcome per cell by the frozen rules: %s, %s, %s%s' % (a, b, c, tag),
          len(a) == 1 and len(b) == 1 and len(c) == 1)


def phrase_hits(text):
    t = norm(text).lower()
    return [p for p in PHRASES if p.lower() in t]


def note_tokens(note):
    return [t for t in ALL_TOKENS if re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(t), note)]


_INV = []


def d_inventory_files():
    """Every OIBridge module at D (read once)."""
    if not _INV:
        r = git('ls-tree', '--name-only', D, LEAN)
        _INV.extend(show(D, p) for p in r.stdout.split() if p.endswith('.lean'))
    return list(_INV)


def module_checks(mod, tag='', landed=None, inv_files=None):
    if landed is None:
        landed = LANDED
    if inv_files is None:
        inv_files = d_inventory_files()
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
    semantic_checks(mod, chunks, prints, tag, landed, inv_files)


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


def landed_texts(show_d):
    """The landed texts the rules read, from D: NativeGate's fields, GateRel's fields, sgate, diagSign's map, the
    sgate relation lemmas, the parity theorem and the d = 1 objects, as effective statements."""
    out = {}
    cd = show_d(LEAN + LANDED_GATE[0] + '.lean')
    pn = show_d(LEAN + LANDED_REL[0] + '.lean')
    if not cd or not pn:
        return out
    ch = decl_chunks(cd).get(LANDED_GATE[1])
    if ch and ch[0] == 'structure':
        for f in ('frame', 'posFwd', 'relT', 'relC'):
            v = field_line(ch[1], f)
            if v is not None:
                out['%s#%s' % (LANDED_GATE[1], f)] = v
    pch = decl_chunks(pn)
    ch = pch.get(LANDED_REL[1])
    if ch and ch[0] == 'structure':
        out['%s#fields' % LANDED_REL[1]] = ' '.join(fields(ch[1]))
        for f in ('relT', 'relC'):
            v = field_line(ch[1], f)
            if v is not None:
                out['%s#%s' % (LANDED_REL[1], f)] = v
    if 'sgate' in pch and pch['sgate'][0] == 'def':
        out['sgate'] = norm(pch['sgate'][1])
    if 'diagSign' in pch and 'toFun x :=' in pch['diagSign'][1]:
        out['diagSign#toFun'] = norm(pch['diagSign'][1].split('toFun x :=', 1)[1].split('\n')[0])
    for n in list(LANDED_SGATE_REL) + ['not_even_of_gateRel']:
        e = effective(pn, n)
        if e is not None:
            out[n] = e
    for n in ('isNot_neg1', 'cnot1_frame', 'nativeGate_cnot1', 'cnot1_relT', 'cnot1_relC'):
        e = effective(cd, n)
        if e is not None:
            out[n] = e
    return out


def landed_at_d():
    return landed_texts(lambda p: show(D, p))


def run_check(commit, freeze):
    r = git('diff', '--name-status', '--no-renames', D, commit)
    rows = [l.split('\t') for l in r.stdout.splitlines() if l]
    exec_rows = {p: s for s, p in rows if not p.startswith(RDIR)}
    rec = {p for s, p in rows if p.startswith(RDIR)}
    check('P', 'delta(D, commit) is exactly the governed execution paths plus the record directory',
          r.returncode == 0 and exec_rows == GOVERNED and rec <= RECORD_FILES and PREREG in rec)
    landed = landed_at_d()
    check('L', 'the landed texts read from D are the frozen ones', landed == LANDED)
    mod = show(commit, MOD)
    module_checks(mod, landed=landed)
    note = show(commit, RESULT)
    if note is not None:
        ph = phrase_hits(note)
        check('S8', 'the result note carries none of the frozen phrases%s' % ((' %s' % ph) if ph else ''), not ph)
        a, b, c = verdicts(mod, landed) if mod is not None else ([], [], [])
        toks = note_tokens(note)
        check('V', 'the result note states exactly the computed tokens %s and no other outcome token (found %s)'
              % (a + b + c, toks), len(a) == 1 and len(b) == 1 and len(c) == 1 and sorted(toks) == sorted(a + b + c))
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                    show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family after the PARITY-NOT-1 family',
          census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def print_verdicts(commit):
    mod = show(commit, MOD)
    landed = landed_at_d()
    a, b, c = verdicts(mod, landed) if mod is not None else ([], [], [])
    print('VERDICT  FAM  %s' % ('/'.join(a) or 'none'))
    print('VERDICT  ODD  %s' % ('/'.join(b) or 'none'))
    print('VERDICT  POS  %s' % ('/'.join(c) or 'none'))
    check('V', 'the landed texts read from D are the frozen ones', landed == LANDED)
    check('V', 'exactly one outcome per cell', len(a) == 1 and len(b) == 1 and len(c) == 1)
