PREFIX = 'OIBridge.ParityNot.'
REL = 'GateRel'
REL_HEADER = '(N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop'
LANDED_GATE = ('CompositeDimension', 'NativeGate')
GATE_HYP = '(hG : NativeGate (eball d) z N G)'
REL_HYP = '(hR : GateRel N G)'
# S2 -- the parity pairs: theorem -> landed partner in CompositeDimension
PARITY_PAIRS = {
    'finrank_plus_eq_finrank_minus_rel': 'finrank_plus_eq_finrank_minus',
    'not_even_of_gateRel': 'not_even_of_nativeGate',
}
FREE_OF_GATE = ('NativeGate', 'posFwd', 'posInv', 'frame', 'maxCone', 'prodEffVal', 'IsEffectOn', 'prodState',
                'corner')
# S3 -- the NOT at d = 3
NOT_BINDERS = ('{z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} {G : W 3 ≃ₗ[ℝ] W 3} '
               '(hN : IsNot (eball 3) z N) (hR : GateRel N G)')
NOT_GATE_BINDERS = NOT_BINDERS.replace('(hR : GateRel N G)', '(hG : NativeGate (eball 3) z N G)')
PI_FORM = '∃ u : Fin 3 → ℝ, ∑ j, u j ^ 2 = 1 ∧ ∀ x, N x = (2 * ∑ j, u j * x j) • u - x'
NOT_THEOREMS = {
    'finrank_plus_minus_three': 'Module.finrank ℝ (plusSpace N) = 2 ∧ Module.finrank ℝ (minusSpace N) = 2',
    'tangentPlus_three': 'tangentPlus N = 1',
    'piRotation_three': PI_FORM,
    'det_three': 'LinearMap.det N = 1',
}
NOT_COROLLARIES = {
    'tangentPlus_of_nativeGate_three': 'tangentPlus_three',
    'piRotation_of_nativeGate_three': 'piRotation_three',
    'det_of_nativeGate_three': 'det_three',
}
PI_DET = ('det_eq_one_of_piRotation', '{N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} {u : Fin 3 → ℝ} '
          '(hu : ∑ j, u j ^ 2 = 1) (hN : ∀ x, N x = (2 * ∑ j, u j * x j) • u - x)', 'LinearMap.det N = 1')
# S4 -- the controls at d = 3
CONTROL_DEFS = {
    'diagSign': 'fun i => c i * x i',
    'refl3': 'diagSign ![1, 1, -1]',
    'negId3': 'diagSign ![-1, -1, -1]',
}
CONTROL_THEOREMS = {
    'negId3_eq': ('', 'negId3 = -LinearMap.id', ()),
    'isNot_refl3': ('', 'IsNot (eball 3) z3 refl3', ()),
    'isNot_negId3': ('', 'IsNot (eball 3) z3 negId3', ()),
    'not_gateRel_refl3': ('(G : W 3 ≃ₗ[ℝ] W 3)', '¬ GateRel refl3 G', ('finrank_plus_minus_three',)),
    'not_gateRel_negId3': ('(G : W 3 ≃ₗ[ℝ] W 3)', '¬ GateRel negId3 G', ('finrank_plus_minus_three',)),
    'det_refl3': ('', 'LinearMap.det refl3 = -1', ()),
    'det_negId3': ('', 'LinearMap.det negId3 = -1', ()),
    'gateRel_cnot': ('', 'GateRel nflip cnot', ('cnot_relT', 'cnot_relC')),
}
LANDED_CNOT = ('cnot_relT', 'cnot_relC')
# S5 -- the separation witnesses
GATE_DEFS = {
    'sgate': 'fun μ ν => if odd ν then ω (p μ) ν else ω μ ν',
    'odd3': None, 'perm3': None, 'odd5': None, 'perm5': None,
    'gJ3': 'sgateEquiv odd3 perm3 perm3_perm3',
    'gJ5': 'sgateEquiv odd5 perm5 perm5_perm5',
    'w3': '![0, -3 / 5, -4 / 5]',
    'w5': 'fun i => if i = 2 then -3 / 5 else if i = 4 then -4 / 5 else 0',
    'z5': 'fun i => if i = 4 then 1 else 0',
    'x5': 'fun i => if i = 0 then 1 else 0',
    'c5': 'if odd5 j.succ then -1 else 1',
    'n5': 'diagSign c5',
}
WITNESS = {
    3: dict(gate='gJ3', nott='nflip', axis='z3', first='xplus', w='w3', body='eball 3', isnot=None),
    5: dict(gate='gJ5', nott='n5', axis='z5', first='x5', w='w5', body='eball 5', isnot='isNot_n5'),
}
VALUE = '-1 / 10'
SELECTORS = re.compile(r'(?<![\w.\'])\w*_of_nativeGate\w*|(?<![\w.\'])three_of_\w+|(?<![\w.\'])dim_of_\w+')
# S6 -- scope
SCOPE_TOKENS = ('Complex', 'ℂ', 'cnot1', 'nativeGate_cnot1', 'dim_of_nativeGate', 'ne_five_of_nativeGate',
                'dim_of_nativeGateOf', 'three_of_nativeGateOf', 'three_of_nativeGateOf_of_two_le')
SCOPE_STMT_TOKENS = ('neg1', 'z1')
D_EQ = re.compile(r'(?<![\w.\'])d\s*(=|≠)\s*\d')
# S7 -- reuse
IMPORT_ONLY = 'import OIBridge.EffectSpace'
# S8 -- phrases
PHRASES = ('selects d = 3', 'selects `d = 3`', 'selector for d = 3', 'forces d = 3', 'forces `d = 3`',
           'd = 3 is forced', 'd = 3 is selected', 'selects the dimension', 'dimension selection',
           'the relations select', 'positivity selects', 'complex structure is', 'yields a complex structure',
           'gives a complex structure', 'reconstructs ℂ', 'reconstructs the complex', 'J² = −1', 'J^2 = -1',
           'J² = -1', 'only higher-dimensional', 'only obstruction', 'the only counterexample', 'every odd dimension',
           'all odd dimensions', 'physically carried', 'physical NOT', 'positivity follows from',
           'positivity is derived', 'implies positivity', 'OI supplies', 'OI provides', 'derived from OI',
           'sourced from OI', 'premise adopted', 'adopts a premise', 'qubit', 'design (round', 'not for landing')
# V -- the frozen decision rule
REL_TOKENS = ('PARITY-FROM-RELATIONS-PROVED', 'PARITY-FROM-RELATIONS-NOT-ESTABLISHED')
NOT_TOKENS = ('D3-NOT-PI-ROTATION-PROVED', 'D3-NOT-PI-ROTATION-NOT-ESTABLISHED')
SEP_TOKENS = ('POSITIVITY-SEPARATION-PROVED', 'POSITIVITY-SEPARATION-NOT-ESTABLISHED')
ALL_TOKENS = REL_TOKENS + NOT_TOKENS + SEP_TOKENS


def tsub(text, mapping):
    """Token-bounded simultaneous substitution."""
    pat = re.compile(r'(?<![\w.\'])(%s)(?![\w\'])' % '|'.join(re.escape(k) for k in mapping))
    return pat.sub(lambda m: mapping[m.group(1)], text)


def kinds_texts_proofs(mod):
    chunks = decl_chunks(mod)
    return ({n: k for n, (k, _, _) in chunks.items()}, {n: c for n, (_, c, _) in chunks.items()},
            {n: p for n, (_, _, p) in chunks.items()})


def rel_ok(mod, landed):
    """GateRel: a structure with the frozen header and exactly the fields relT and relC, each the landed field."""
    kinds, texts, _ = kinds_texts_proofs(mod)
    t = texts.get(REL, '')
    if kinds.get(REL) != 'structure' or fields(t) != ['relT', 'relC']:
        return False
    hd = norm(t.split(' where', 1)[0])
    if not hd.startswith('structure %s ' % REL) or hd[len('structure %s ' % REL):] != norm(REL_HEADER):
        return False
    return all(landed.get('%s#%s' % (LANDED_GATE[1], f)) == field_line(t, f) for f in ('relT', 'relC'))


def section_decls(mod, labels):
    secs = sections(mod)
    return [(name, mod[start:nxt]) for kind, name, start, se, nxt, cend in spans(mod)
            if section_at(secs, start) in labels]


def mentions(text, toks):
    c = code_only(text)
    return [t for t in toks if token(t, c)]


def parity_bad(mod, landed, names=None, spaces=None, inv_files=None):
    """S2: each parity theorem is its landed partner with the native-gate hypothesis replaced by GateRel; §A free of
    the native gate, the frame and positivity outside gateRel_of_nativeGate; resolution when an inventory is given."""
    bad = []
    for n, l in PARITY_PAIRS.items():
        de, le = effective(mod, n), landed.get(l)
        if de is None or le is None or le.count(GATE_HYP) != 1 or token('NativeGate', de) or \
                de != le.replace(GATE_HYP, REL_HYP):
            bad.append(n)
    for name, body in section_decls(mod, ('§A',)):
        if name != 'gateRel_of_nativeGate' and name != REL and mentions(body, FREE_OF_GATE):
            bad.append(name)
    if names is not None:
        lt = [t for t in inv_files if '\nnamespace %s\n' % LANDED_GATE[0] in t]
        lt = lt[0] if len(lt) == 1 else None
        for n, l in PARITY_PAIRS.items():
            de = effective(mod, n)
            if de is None or lt is None:
                bad.append(n)
                continue
            dsc = scopes_at(mod).get(n, ([], [], []))
            lsc = scopes_at(lt).get(l, ([], [], []))
            dvis, lvis = visible(dsc[1], dsc[2], spaces), visible(lsc[1], lsc[2], spaces)
            if resolve('NativeGate', lvis, names) != ['OIBridge.%s.NativeGate' % LANDED_GATE[0]]:
                bad.append(n + ':NativeGate')
            for t in sorted(set(strip_binders(de))):
                a, b = resolve(t, dvis, names), resolve(t, lvis, names)
                if t == REL:
                    if a != [PREFIX + REL]:
                        bad.append(n + ':' + t)
                elif len(a) > 1 or a != b:
                    bad.append(n + ':' + t)
    return bad


def not_bad(mod):
    """S3: the four d = 3 theorems on IsNot and GateRel alone; §B free of the native gate, the frame and positivity
    outside the three corollaries, each the GateRel theorem with the native-gate hypothesis, through
    gateRel_of_nativeGate."""
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    for n, c in NOT_THEOREMS.items():
        b, cc = split_statement(texts.get(n, ''))
        if kinds.get(n) != 'theorem' or norm(b) != norm(NOT_BINDERS) or norm(cc) != norm(c):
            bad.append(n)
    b, cc = split_statement(texts.get(PI_DET[0], ''))
    if kinds.get(PI_DET[0]) != 'theorem' or norm(b) != norm(PI_DET[1]) or norm(cc) != norm(PI_DET[2]):
        bad.append(PI_DET[0])
    if not token('det_eq_one_of_piRotation', proofs.get('det_three', '')) or \
            not token('piRotation_three', proofs.get('det_three', '')):
        bad.append('det_three')
    for n, base in NOT_COROLLARIES.items():
        b, cc = split_statement(texts.get(n, ''))
        _, bc = split_statement(texts.get(base, ''))
        if kinds.get(n) != 'theorem' or norm(b) != norm(NOT_GATE_BINDERS) or norm(cc) != norm(bc) or \
                norm(bc) != norm(NOT_THEOREMS[base]) or not token('gateRel_of_nativeGate', proofs.get(n, '')) or \
                not token(base, proofs.get(n, '')):
            bad.append(n)
    for name, body in section_decls(mod, ('§B',)):
        if name not in NOT_COROLLARIES and mentions(body, FREE_OF_GATE):
            bad.append(name)
    return bad


def controls_bad(mod, landed):
    """S4: the two NOT controls without the relations, and cnot with nflip with them."""
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    for n, body in CONTROL_DEFS.items():
        t = texts.get(n, '')
        got = norm(t.split('toFun x :=', 1)[1].split('\n')[0]) if n == 'diagSign' and 'toFun x :=' in t else \
            def_body(t)
        if kinds.get(n) != 'def' or got != norm(body):
            bad.append(n)
    for n, (b, c, deps) in CONTROL_THEOREMS.items():
        bb, cc = split_statement(texts.get(n, ''))
        if kinds.get(n) != 'theorem' or norm(bb) != norm(b) or norm(cc) != norm(c) or \
                not all(token(m, proofs.get(n, '')) for m in deps):
            bad.append(n)
    for n in LANDED_CNOT:
        if landed.get(n) is None:
            bad.append(n + ' at D')
    if landed.get('cnot_relT') != '(ω : W 3) : actT nflip (cnot (actT nflip ω)) = cnot ω' or \
            landed.get('cnot_relC') != '(ω : W 3) : actC nflip (cnot (actC nflip ω)) = actT nflip (cnot ω)':
        bad.append('cnot relations at D')
    return bad


def sep_bad(mod, landed):
    """S5: for d = 3 and d = 5, the frozen gate and witness; the landed frame field at the gate; GateRel; the value
    -1 / 10; the negation of the landed posFwd field at the gate, through the value; no dimension corollary."""
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    for n, body in GATE_DEFS.items():
        if n not in texts:
            bad.append(n)
        elif body is not None and def_body(texts[n]) != norm(body):
            bad.append(n)
    frame = landed.get('%s#frame' % LANDED_GATE[1])
    posfwd = landed.get('%s#posFwd' % LANDED_GATE[1])
    if frame is None or posfwd is None or not frame.startswith('frame : ∀ a b : Fin 2, ') or \
            not posfwd.startswith('posFwd : '):
        return bad + ['NativeGate fields at D']
    frame = frame[len('frame : ∀ a b : Fin 2, '):]
    posfwd = posfwd[len('posFwd : '):]
    for k, w in WITNESS.items():
        g = w['gate']
        want_frame = tsub(frame, {'G': g, 'z': w['axis']})
        b, c = split_statement(texts.get(g + '_frame', ''))
        if kinds.get(g + '_frame') != 'theorem' or norm(b) != '(a b : Fin 2)' or norm(c) != want_frame:
            bad.append(g + '_frame')
        b, c = split_statement(texts.get('gateRel_' + g, ''))
        if kinds.get('gateRel_' + g) != 'theorem' or norm(b) != '' or norm(c) != 'GateRel %s %s' % (w['nott'], g):
            bad.append('gateRel_' + g)
        val = g + '_value'
        b, c = split_statement(texts.get(val, ''))
        want_val = 'prodEffVal (sharpEff %s) (sharpEff %s) (%s (prodState %s %s)) = %s' % (
            w['w'], w['axis'], g, w['first'], w['axis'], VALUE)
        if kinds.get(val) != 'theorem' or norm(b) != '' or norm(c) != want_val:
            bad.append(val)
        mem = g + '_not_mem_maxCone'
        b, c = split_statement(texts.get(mem, ''))
        if kinds.get(mem) != 'theorem' or norm(c) != '%s (prodState %s %s) ∉ maxCone (%s)' % (
                g, w['first'], w['axis'], w['body']) or not token(val, proofs.get(mem, '')) or \
                not token('sharpEff_isEffectOn', proofs.get(mem, '')):
            bad.append(mem)
        pf = 'not_posFwd_' + g
        want_pf = '¬ ' + tsub(posfwd, {'G': g, 'Ω': '(%s)' % w['body']}).replace('∈ (%s),' % w['body'],
                                                                            '∈ %s,' % w['body'])
        b, c = split_statement(texts.get(pf, ''))
        if kinds.get(pf) != 'theorem' or norm(b) != '' or norm(c) != want_pf or not token(mem, proofs.get(pf, '')):
            bad.append(pf)
        ng = 'not_nativeGate_' + g
        b, c = split_statement(texts.get(ng, ''))
        if kinds.get(ng) != 'theorem' or norm(c) != '¬ NativeGate (%s) %s %s %s' % (
                w['body'], w['axis'], w['nott'], g) or not token(pf, proofs.get(ng, '')):
            bad.append(ng)
        if w['isnot']:
            b, c = split_statement(texts.get(w['isnot'], ''))
            if kinds.get(w['isnot']) != 'theorem' or norm(c) != 'IsNot (%s) %s %s' % (w['body'], w['axis'],
                                                                                        w['nott']):
                bad.append(w['isnot'])
    b, c = split_statement(texts.get('finrank_plus_eq_finrank_minus_n5', ''))
    if norm(c) != 'Module.finrank ℝ (plusSpace n5) = Module.finrank ℝ (minusSpace n5)' or \
            not token('finrank_plus_eq_finrank_minus_rel', proofs.get('finrank_plus_eq_finrank_minus_n5', '')):
        bad.append('finrank_plus_eq_finrank_minus_n5')
    for name, body in section_decls(mod, ('§D', '§E', '§F')):
        if SELECTORS.search(code_only(body)):
            bad.append(name)
    return bad


def rel_cell(mod, landed):
    """PARITY-FROM-RELATIONS-PROVED iff: GateRel is the landed relT and relC and nothing else (S1); each of the two
    parity theorems is its landed NativeGate partner read from D with the native-gate hypothesis replaced by
    GateRel and nothing else, and §A reads neither the native gate, the frame nor positivity (S2). Otherwise
    PARITY-FROM-RELATIONS-NOT-ESTABLISHED. Reads no §B-§F statement."""
    ok = rel_ok(mod, landed) and not parity_bad(mod, landed)
    return [REL_TOKENS[0] if ok else REL_TOKENS[1]]


def not_cell(mod, landed):
    """D3-NOT-PI-ROTATION-PROVED iff: GateRel passes S1; the four d = 3 theorems take IsNot (eball 3) and GateRel alone
    with their frozen conclusions, and §B reads neither the native gate, the frame nor positivity outside the three
    corollaries (S3); and the controls hold (S4). Otherwise D3-NOT-PI-ROTATION-NOT-ESTABLISHED. Reads no §D-§F
    statement."""
    ok = rel_ok(mod, landed) and not not_bad(mod) and not controls_bad(mod, landed)
    return [NOT_TOKENS[0] if ok else NOT_TOKENS[1]]


def sep_cell(mod, landed):
    """POSITIVITY-SEPARATION-PROVED iff: GateRel passes S1, and for each of d = 3 and d = 5 the frozen gate satisfies
    the landed frame field and GateRel, and the negation of the landed posFwd field is proved through the frozen
    value -1 / 10 (S5). Otherwise POSITIVITY-SEPARATION-NOT-ESTABLISHED. Reads no §A-§C statement."""
    ok = rel_ok(mod, landed) and not sep_bad(mod, landed)
    return [SEP_TOKENS[0] if ok else SEP_TOKENS[1]]


def verdicts(mod, landed):
    return rel_cell(mod, landed), not_cell(mod, landed), sep_cell(mod, landed)


def semantic_checks(mod, chunks, prints, tag, landed, inv_files):
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    check('S1', 'GateRel is the landed relT and relC and nothing else' + tag, rel_ok(mod, landed))
    names, spaces = inventory(inv_files + [mod])
    bad2 = parity_bad(mod, landed, names, spaces, inv_files)
    check('S2', 'each parity theorem is its landed partner with NativeGate replaced by GateRel; §A free of the gate '
                'conditions%s%s' % (tag, (' %s' % bad2[:3]) if bad2 else ''), not bad2)
    bad3 = not_bad(mod)
    check('S3', 'the d = 3 theorems on IsNot and GateRel alone; §B free of the gate conditions%s%s'
          % (tag, (' %s' % bad3[:3]) if bad3 else ''), not bad3)
    bad4 = controls_bad(mod, landed)
    check('S4', 'the reflection and -id carry no relations; cnot with nflip does%s%s'
          % (tag, (' %s' % bad4[:3]) if bad4 else ''), not bad4)
    bad5 = sep_bad(mod, landed)
    check('S5', 'gJ3 and gJ5: landed frame, GateRel, value -1 / 10, landed posFwd negated%s%s'
          % (tag, (' %s' % bad5[:3]) if bad5 else ''), not bad5)
    bad6 = []
    for kind, name, start, se, nxt, cend in spans(mod):
        body = mod[start:nxt]
        if mentions(body, SCOPE_TOKENS) or mentions(texts.get(name, ''), SCOPE_STMT_TOKENS):
            bad6.append(name)
        if kind in ('theorem', 'lemma'):
            _, c = split_statement(texts.get(name, ''))
            if D_EQ.search(c):
                bad6.append(name)
    check('S6', 'no complex field, d = 1 object or dimension selector; no conclusion on d%s%s'
          % (tag, (' %s' % bad6[:3]) if bad6 else ''), not bad6)
    others = inventory(inv_files)[0]
    msc = scopes_at(mod)
    clash = []
    for kind, name in decls(mod):
        sc = msc.get(name, ([], [], []))
        if resolve(name, visible(sc[1], sc[2], spaces), others):
            clash.append(name)
    imports = re.findall(r'^import .*$', mod, re.M)
    check('S7', 'no declaration shares a name with a visible OIBridge declaration; the only import is '
                'OIBridge.EffectSpace%s%s' % (tag, (' %s' % clash[:3]) if clash else ''),
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
    """The landed texts the rules read, from D: the NativeGate fields, the two parity theorems and the two cnot
    relations, as effective statements."""
    out = {}
    t = show_d(LEAN + LANDED_GATE[0] + '.lean')
    if not t:
        return out
    ch = decl_chunks(t).get(LANDED_GATE[1])
    if ch and ch[0] == 'structure':
        for f in ('relT', 'relC', 'frame', 'posFwd'):
            v = field_line(ch[1], f)
            if v is not None:
                out['%s#%s' % (LANDED_GATE[1], f)] = v
    for n in list(PARITY_PAIRS.values()) + list(LANDED_CNOT):
        e = effective(t, n)
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
    check('S1', 'the landed texts read from D are the frozen ones', landed == LANDED)
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
    check('C', 'the census is D\'s with exactly the frozen family after the KTRANS-DENSE-1 family',
          census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def print_verdicts(commit):
    mod = show(commit, MOD)
    landed = landed_at_d()
    a, b, c = verdicts(mod, landed) if mod is not None else ([], [], [])
    print('VERDICT  REL  %s' % ('/'.join(a) or 'none'))
    print('VERDICT  NOT  %s' % ('/'.join(b) or 'none'))
    print('VERDICT  SEP  %s' % ('/'.join(c) or 'none'))
    check('V', 'the landed texts read from D are the frozen ones', landed == LANDED)
    check('V', 'exactly one outcome per cell', len(a) == 1 and len(b) == 1 and len(c) == 1)
