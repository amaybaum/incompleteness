PREFIX = 'OIBridge.DenseOrbit.'
DEF = 'DenseBoundaryOrbit'
LANDED_DEF = ('OrbitGeneration', 'BoundaryTransitive')
LAST_CLAUSE = '∃ g ∈ G, g x = y'
DENSE_CLAUSE = 'y ∈ closure ((fun g : V ≃ᵃ[ℝ] V => g x) \'\' G)'
# S2 -- the frozen pairs: dense name -> (landed module, landed name)
BALL_PAIRS = {
    'boundary_qnorm_const_of_dense': ('TransitiveBody', 'boundary_qnorm_const'),
    'centroid_mem_interior_of_dense': ('TransitiveBody', 'centroid_mem_interior'),
    'eq_qBall_of_dense': ('TransitiveBody', 'eq_qBall_of_boundaryTransitive'),
    'exists_affine_image_eq_eball_of_dense': ('TransitiveBody', 'exists_affine_image_eq_eball'),
    'chartBody_eq_eball_of_dense': ('TransitiveBody', 'chartBody_eq_eball'),
}
CONE_PAIRS = {
    'maxConeOf_avail_eq_of_dense': ('EffectSpace', 'maxConeOf_avail_eq'),
    'nativeGate_of_avail_dense': ('K1Bridge', 'nativeGate_of_avail'),
    'entangling_of_avail_dense': ('K1Bridge', 'entangling_of_avail'),
    'dim_of_nativeGateOf_dense': ('K1Bridge', 'dim_of_nativeGateOf'),
    'three_of_nativeGateOf_dense': ('K1Bridge', 'three_of_nativeGateOf'),
    'three_of_nativeGateOf_of_two_le_dense': ('K2Guard', 'three_of_nativeGateOf_of_two_le'),
}
PAIRS = dict(BALL_PAIRS, **CONE_PAIRS)
BALL_PRINTED = ('boundary_qnorm_const_of_dense', 'centroid_mem_interior_of_dense', 'eq_qBall_of_dense',
                'exists_affine_image_eq_eball_of_dense', 'chartBody_eq_eball_of_dense')
CONE_PRINTED = tuple(CONE_PAIRS)
# S4 -- the weakening and the strictness witness
WEAK = 'denseBoundaryOrbit_of_boundaryTransitive'
WEAK_BINDERS = ('{V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)} '
                '(hT : BoundaryTransitive Ω G)')
WEAK_CONCL = 'DenseBoundaryOrbit Ω G'
FAMILY = 'ratRefl'
FAMILY_BODY = ('insert (AffineEquiv.refl ℝ (Fin d → ℝ)) (Set.range fun q : {q : Fin d → ℚ // ∑ j, ((q j : ℝ)) ^ 2 ≠ 0} '
               '=> @reflAff d (fun j => (q.1 j : ℝ)) q.2)')
STRICT = {
    'countable_ratRefl': ('', '(ratRefl d).Countable', ()),
    'ratRefl_subset_fullAut': ('', 'ratRefl d ⊆ fullAut d', ()),
    'preservesBody_ratRefl': ('', 'PreservesBody (eball d) (ratRefl d)', ()),
    'denseBoundaryOrbit_ratRefl': ('', 'DenseBoundaryOrbit (eball d) (ratRefl d)', ()),
    'not_boundaryTransitive_ratRefl': ('', '¬ BoundaryTransitive (eball 3) (ratRefl 3)',
                                       ('not_boundaryTransitive_of_countable', 'countable_ratRefl')),
    'countable_seedOrbit_cone': ('', '(seedOrbit (ratRefl 3) (sharpEff (axisVec (by norm_num : 0 < 3)))).Countable ∧ '
                                     'maxConeOf (seedOrbit (ratRefl 3) (sharpEff (axisVec (by norm_num : 0 < 3)))) = '
                                     'maxCone (eball 3)', ('countable_ratRefl', 'denseBoundaryOrbit_ratRefl')),
}
STRICT_PRINTED = (WEAK, 'denseBoundaryOrbit_ratRefl', 'not_boundaryTransitive_ratRefl', 'countable_seedOrbit_cone')
NOGO = ('EffectSpace', 'not_boundaryTransitive_of_countable')
NOGO_STMT = ('{G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))} (hG : G.Countable) : ¬ BoundaryTransitive (eball 3) G')
# S5 -- scope
SCOPE_TOKENS = ('sharpFamily', 'sharpUnitFamily', 'fullEffects', 'MixingClosed', 'unitEff', 'SupportingEffectComplete',
                'KInf1', 'CoversBoundaryFrom', 'conePair', 'ballEffect', 'ball3', 'extremePoints', 'Lorentz',
                'lorentz_of_effects', 'lorentz_of_seedOrbit', 'lorentz_of_available',
                'extreme_of_isBoundaryState_of_transitive')
# S6 -- reuse
IMPORT_ONLY = 'import OIBridge.K2Guard'
# S7 -- phrases
PHRASES = ('closure of operations', 'operation closure', 'closed under operations', 'operationally closed',
           'closedness of operations', 'closed set of operations', 'OI supplies', 'supplied by OI', 'OI provides',
           'provided by OI', 'derived from OI', 'sourced from OI', 'StageCompletion supplies',
           'the observer architecture supplies', 'K∞-Trans is derived', 'K∞-Trans is sourced', 'replaces K∞-Trans',
           'K∞-Trans is not needed', 'K∞-Trans is unnecessary', 'eliminates K∞-Trans', 'K∞-Trans is redundant',
           'every consumer', 'all consumers', 'all of K∞-Trans', 'composite closedness', 'closedness of the composite',
           'closed composite', 'adopted operation', 'operations are rational', 'physical operations',
           'premise adopted', 'adopts a premise', 'qubit', 'design (round', 'not for landing')
# S8 -- separation
CONE_OBJECTS = ('maxCone', 'maxConeOf', 'NativeGate', 'NativeGateOf', 'Entangling', 'EntanglingOf', 'IsNot',
                'SeedOrbitAvailable', 'SharpSeed', 'EffectsOn', 'sharpEff', 'seedOrbit', 'W')
# V -- the frozen decision rule
BALL_TOKENS = ('KTRANS-DENSE-BALL-PROVED', 'KTRANS-DENSE-BALL-NOT-ESTABLISHED')
CONE_TOKENS = ('KTRANS-DENSE-CONE-PROVED', 'KTRANS-DENSE-CONE-NOT-ESTABLISHED')
STRICT_TOKENS = ('KTRANS-DENSE-STRICTLY-WEAKER', 'KTRANS-DENSE-STRICTLY-WEAKER-NOT-ESTABLISHED')
ALL_TOKENS = BALL_TOKENS + CONE_TOKENS + STRICT_TOKENS
IDENT = re.compile(r'(?<![\w.\'@])[A-Za-z_][\w\'.]*')
BINDER_OPEN, BINDER_CLOSE = '({[⦃', ')}]⦄'


def stmt_parts(texts, name):
    b, c = split_statement(texts.get(name, ''))
    return norm(b), norm(c)


def def_body(text):
    j = text.find(' :=')
    return norm(text[j + 3:]) if j != -1 else ''


def groups(b):
    """The top-level bracketed binder groups of a binder string, in order."""
    out, depth, start = [], 0, None
    for i, c in enumerate(b):
        if c in BINDER_OPEN:
            if depth == 0:
                start = i
            depth += 1
        elif c in BINDER_CLOSE:
            depth -= 1
            if depth == 0 and start is not None:
                out.append(norm(b[start:i + 1]))
                start = None
    return out


def group_names(g):
    """The bound names of a binder group (none for an anonymous instance group)."""
    inner = g[1:-1]
    j = inner.find(' : ')
    if j == -1:
        return []
    return inner[:j].split()


def scopes_at(text):
    """[(position, variable groups in scope, namespaces in scope, opened namespaces in scope)] at each declaration."""
    stack = [([], [], [])]
    out = {}
    lines = text.split('\n')
    pos = 0
    k = 0
    decl_at = {m.start(): m.group(2) for m in DECL.finditer(text)}
    while k < len(lines):
        line = lines[k]
        block = [line]
        j = k + 1
        if line.startswith('variable') or line.startswith('open '):
            while j < len(lines) and lines[j].startswith('  '):
                block.append(lines[j])
                j += 1
        whole = '\n'.join(block)
        m = re.match(r'^(namespace|section|noncomputable section)\b\s*(\S*)', line)
        if m:
            stack.append(([], [m.group(2)] if m.group(1) == 'namespace' else [], []))
        elif re.match(r'^end\b', line):
            if len(stack) > 1:
                stack.pop()
        elif line.startswith('variable'):
            stack[-1][0].extend(groups(whole[len('variable'):]))
        elif line.startswith('open '):
            stack[-1][2].extend(whole[len('open '):].split())
        if pos in decl_at:
            vs = [g for s in stack for g in s[0]]
            nss = [n for s in stack for n in s[1]]
            ops = [o for s in stack for o in s[2]]
            out[decl_at[pos]] = (vs, nss, ops)
        for l in block:
            pos += len(l) + 1
        k = j
    return out


def effective(text, name):
    """The effective statement of a declaration: the section variables its statement uses (closed under use by the
    included groups, an instance group included with a variable it mentions), in declared order, then its own binders
    and conclusion. None when the declaration is absent."""
    chunks = decl_chunks(text)
    if name not in chunks:
        return None
    stmt = chunks[name][1]
    vs = scopes_at(text).get(name, ([], [], []))[0]
    b, c = split_statement(stmt)
    used = norm(b) + ' : ' + norm(c)
    inc = [False] * len(vs)
    changed = True
    while changed:
        changed = False
        hay = used + ' ' + ' '.join(g for g, i in zip(vs, inc) if i)
        for n, g in enumerate(vs):
            if inc[n]:
                continue
            names = group_names(g)
            if names and any(token(x, hay) for x in names):
                inc[n] = True
                changed = True
            elif not names and g.startswith('[') and any(token(x, g) for gg, i in zip(vs, inc) if i
                                                          for x in group_names(gg)):
                inc[n] = True
                changed = True
    pre = ' '.join(g for g, i in zip(vs, inc) if i)
    return norm(pre + ' ' + norm(b) + ' : ' + norm(c))


_INV_CACHE = {}


def inventory(files):
    """{fully qualified name} of every declaration in the given module texts, with the namespaces they declare."""
    names, spaces = set(), set()
    for text in files:
        if text in _INV_CACHE:
            n, sp = _INV_CACHE[text]
            names |= n
            spaces |= sp
            continue
        n, sp = inventory_one(text)
        if len(_INV_CACHE) < 4096:
            _INV_CACHE[text] = (n, sp)
        names |= n
        spaces |= sp
    return names, spaces


def inventory_one(text):
    names, spaces = set(), set()
    for text in [text]:
        sc = scopes_at(text)
        for kind, name in decls(text):
            nss = sc.get(name, ([], [], []))[1]
            prefix = '.'.join(nss)
            names.add((prefix + '.' if prefix else '') + name)
            for i in range(1, len(nss) + 1):
                spaces.add('.'.join(nss[:i]))
    return names, spaces


def visible(nss, ops, spaces):
    """The namespaces whose members are in scope: every prefix of the current namespace, and each opened namespace,
    resolved against the current namespace prefixes when that names an OIBridge namespace."""
    out = [''] + ['.'.join(nss[:i]) for i in range(1, len(nss) + 1)]
    for o in ops:
        hit = [p + '.' + o for p in ['.'.join(nss[:i]) for i in range(len(nss), 0, -1)] if p + '.' + o in spaces]
        out.append(hit[0] if hit else o)
    return out


def resolve(tok, vis, names):
    return sorted({(v + '.' if v else '') + tok for v in vis} & names)


def top_colon(s):
    """Index of the first colon at bracket depth 0 that is not part of `:=`."""
    depth = 0
    for j, c in enumerate(s):
        if c in BINDER_OPEN:
            depth += 1
        elif c in BINDER_CLOSE:
            depth -= 1
        elif c == ':' and depth == 0 and s[j:j + 2] != ':=':
            return j
    return len(s)


def strip_binders(eff):
    """The identifiers of an effective statement, without the names it binds: the names of its binder groups and the
    names bound by `∃`, `∀` and `fun` in its conclusion."""
    k = top_colon(eff)
    bound = set()
    for g in groups(eff[:k]):
        bound.update(group_names(g))
    for m in re.finditer(r'(?:∃|∀|fun)\s+([^,:=]+?)\s*(?::|,|=>)', eff[k:]):
        bound.update(x for x in m.group(1).split() if re.match(r"^[A-Za-zΩ_][\w']*$", x))
    return [t for t in IDENT.findall(eff) if t not in bound]


def pair_ok(mod, landed, dname, lname):
    """The dense effective statement is the landed one with BoundaryTransitive replaced, and nothing else."""
    de = effective(mod, dname)
    le = landed.get(lname)
    if de is None or le is None:
        return False
    if len(re.findall(r'(?<![\w.\'])BoundaryTransitive(?![\w\'])', le)) != 1 or token('BoundaryTransitive', de):
        return False
    return de == re.sub(r'(?<![\w.\'])BoundaryTransitive(?![\w\'])', DEF, le)


def resolution_bad(mod, dname, lmod_text, lname, names, spaces):
    """The OIBridge identifiers of the pair resolving differently in the two contexts, or ambiguously."""
    bad = []
    de = effective(mod, dname)
    if de is None:
        return [dname]
    dsc = scopes_at(mod).get(dname, ([], [], []))
    lsc = scopes_at(lmod_text).get(lname, ([], [], [])) if lmod_text else ([], [], [])
    dvis, lvis = visible(dsc[1], dsc[2], spaces), visible(lsc[1], lsc[2], spaces)
    le = effective(lmod_text, lname) if lmod_text else None
    if le is None or resolve('BoundaryTransitive', lvis, names) != ['OIBridge.%s.BoundaryTransitive' % LANDED_DEF[0]]:
        bad.append('BoundaryTransitive')
    for t in sorted(set(strip_binders(de))):
        a, b = resolve(t, dvis, names), resolve(t, lvis, names)
        if t == DEF:
            if a != [PREFIX + DEF]:
                bad.append(t)
            continue
        if len(a) > 1 or a != b:
            bad.append(t)
    return bad


def def_ok(mod, landed):
    """DenseBoundaryOrbit: the landed BoundaryTransitive's effective header, its body with the last clause replaced."""
    eff = effective(mod, DEF)
    chunks = decl_chunks(mod)
    if eff is None or chunks.get(DEF, ('',))[0] != 'def':
        return False
    lhead, lbody = landed.get(LANDED_DEF[1] + '#head'), landed.get(LANDED_DEF[1] + '#body')
    body = def_body(chunks[DEF][1])
    hd = norm(def_header(chunks[DEF][1]))
    hd = hd[hd.index(DEF) + len(DEF):]
    return lhead is not None and lbody is not None and norm(hd) == lhead and lbody.endswith(LAST_CLAUSE) and \
        body == lbody[:-len(LAST_CLAUSE)] + DENSE_CLAUSE


def weak_ok(texts, kinds):
    bb, cc = stmt_parts(texts, WEAK)
    return kinds.get(WEAK) == 'theorem' and bb == norm(WEAK_BINDERS) and cc == norm(WEAK_CONCL)


def strict_bad(chunks, landed):
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    proofs = {n: p for n, (_, _, p) in chunks.items()}
    bad = []
    if kinds.get(FAMILY) != 'noncomputable def' or def_body(texts.get(FAMILY, '')) != norm(FAMILY_BODY):
        bad.append(FAMILY)
    for n, (b, c, deps) in STRICT.items():
        bb, cc = stmt_parts(texts, n)
        if kinds.get(n) != 'theorem' or re.sub(r'\{[^{}]*\}', ' ', bb).strip() != b or cc != norm(c) or \
                not all(token(m, proofs.get(n, '')) for m in deps):
            bad.append(n)
    if landed.get(NOGO[1]) != norm(NOGO_STMT):
        bad.append(NOGO[1] + ' at D')
    return bad


def landed_texts(show_d):
    """The landed effective statements the rules read, from D."""
    out = {}
    cache = {}
    for m, n in list(PAIRS.values()) + [NOGO]:
        if m not in cache:
            cache[m] = show_d(LEAN + m + '.lean')
        t = cache[m]
        e = effective(t, n) if t else None
        if e is not None:
            out[n] = e
    t = show_d(LEAN + LANDED_DEF[0] + '.lean')
    if t:
        ch = decl_chunks(t).get(LANDED_DEF[1])
        if ch and ch[0] == 'def':
            vs = scopes_at(t).get(LANDED_DEF[1], ([], [], []))[0]
            hd = norm(def_header(ch[1]))
            hd = hd[hd.index(LANDED_DEF[1]) + len(LANDED_DEF[1]):]
            inst = [g for g in vs]
            out[LANDED_DEF[1] + '#head'] = norm(' '.join(inst) + ' ' + hd)
            out[LANDED_DEF[1] + '#body'] = def_body(ch[1])
    return out


def ball_cell(mod, landed):
    """KTRANS-DENSE-BALL-PROVED iff: `DenseBoundaryOrbit` is the landed `BoundaryTransitive` with its last clause
    replaced by orbit-closure membership (S1); the weakening has its frozen binders and conclusion; and each of the
    five TRB-1 pairs pairs with its landed theorem read from D (S2). Otherwise KTRANS-DENSE-BALL-NOT-ESTABLISHED.
    Reads no cone or strictness statement."""
    chunks = decl_chunks(mod)
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    ok = def_ok(mod, landed) and weak_ok(texts, kinds)
    for d, (m, l) in BALL_PAIRS.items():
        ok = ok and kinds.get(d) == 'theorem' and pair_ok(mod, landed, d, l)
    return [BALL_TOKENS[0] if ok else BALL_TOKENS[1]]


def cone_cell(mod, landed):
    """KTRANS-DENSE-CONE-PROVED iff: `DenseBoundaryOrbit` passes S1, and each of the six cone and selector pairs pairs
    with its landed theorem read from D (S2). Otherwise KTRANS-DENSE-CONE-NOT-ESTABLISHED. Reads no ball or strictness
    statement."""
    chunks = decl_chunks(mod)
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    ok = def_ok(mod, landed)
    for d, (m, l) in CONE_PAIRS.items():
        ok = ok and kinds.get(d) == 'theorem' and pair_ok(mod, landed, d, l)
    return [CONE_TOKENS[0] if ok else CONE_TOKENS[1]]


def strict_cell(mod, landed):
    """KTRANS-DENSE-STRICTLY-WEAKER iff: `DenseBoundaryOrbit` passes S1; the weakening (boundary transitivity implies a
    dense boundary orbit) has its frozen binders and conclusion; `ratRefl` is the frozen definition; and the
    strictness theorems have their frozen conclusions, the non-transitivity proved through EFF-1's
    `not_boundaryTransitive_of_countable` with its frozen statement at D. Otherwise
    KTRANS-DENSE-STRICTLY-WEAKER-NOT-ESTABLISHED. Reads no paired statement."""
    chunks = decl_chunks(mod)
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    ok = def_ok(mod, landed) and weak_ok(texts, kinds) and not strict_bad(chunks, landed)
    return [STRICT_TOKENS[0] if ok else STRICT_TOKENS[1]]


def verdicts(mod, landed):
    return ball_cell(mod, landed), cone_cell(mod, landed), strict_cell(mod, landed)


def semantic_checks(mod, chunks, prints, tag, landed, inv_files):
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    proofs = {n: p for n, (_, _, p) in chunks.items()}
    code = code_only(mod)
    # S1
    check('S1', 'DenseBoundaryOrbit is the landed BoundaryTransitive with its last clause replaced by orbit-closure '
                'membership' + tag, def_ok(mod, landed))
    # S2
    bad2 = [d for d, (m, l) in PAIRS.items() if kinds.get(d) != 'theorem' or not pair_ok(mod, landed, d, l)]
    bad2 += [d for d in BALL_PRINTED + CONE_PRINTED if PREFIX + d not in prints]
    check('S2', 'each of the %d frozen pairs is its landed theorem with BoundaryTransitive replaced and nothing else%s%s'
          % (len(PAIRS), tag, (' %s' % bad2[:3]) if bad2 else ''), not bad2)
    # S3
    names, spaces = inventory(inv_files + [mod])
    bad3 = []
    for d, (m, l) in PAIRS.items():
        lt = [t for t in inv_files if ('\nnamespace %s\n' % m) in t]
        bad3 += ['%s:%s' % (d, t) for t in resolution_bad(mod, d, lt[0] if len(lt) == 1 else None, l, names, spaces)]
    check('S3', 'every OIBridge identifier of every pair resolves to the same unique declaration in both contexts%s%s'
          % (tag, (' %s' % bad3[:3]) if bad3 else ''), not bad3)
    # S4
    bad4 = ([] if weak_ok(texts, kinds) else [WEAK]) + strict_bad(chunks, landed)
    bad4 += [n for n in STRICT_PRINTED if PREFIX + n not in prints]
    check('S4', 'the weakening and the strictness witness with their frozen statements, through EFF-1\'s countable '
                'no-go%s%s' % (tag, (' %s' % bad4[:3]) if bad4 else ''), not bad4)
    # S5
    secs = sections(mod)
    stmts = ' '.join(code_only(t) for t in texts.values())
    bad5 = [t for t in SCOPE_TOKENS if token(t, stmts)]
    for kind, name, start, se, nxt, cend in spans(mod):
        if section_at(secs, start) != '§D' and token(FAMILY, code_only(mod[start:nxt])):
            bad5.append(name)
    check('S5', 'no exact-existence or uncovered object; ratRefl only in §D%s%s'
          % (tag, (' %s' % bad5[:3]) if bad5 else ''), not bad5)
    # S6
    vis_clash = []
    others = inventory(inv_files)[0]
    msc = scopes_at(mod)
    for kind, name in decls(mod):
        sc = msc.get(name, ([], [], []))
        hits = resolve(name, visible(sc[1], sc[2], spaces), others)
        if hits:
            vis_clash.append(name)
    imports = re.findall(r'^import .*$', mod, re.M)
    check('S6', 'no declaration shares a name with a visible OIBridge declaration; the only import is OIBridge.K2Guard'
          '%s%s' % (tag, (' %s' % vis_clash[:3]) if vis_clash else ''), not vis_clash and imports == [IMPORT_ONLY])
    # S7
    ph = phrase_hits(header(mod))
    check('S7', 'the header carries none of the frozen phrases%s%s' % (tag, (' %s' % ph) if ph else ''), not ph)
    # S8
    bad8 = []
    for kind, name, start, se, nxt, cend in spans(mod):
        sec = section_at(secs, start)
        body = code_only(mod[start:nxt])
        if sec == '§B' and any(token(t, body) for t in CONE_OBJECTS):
            bad8.append(name)
        if sec in ('§A', '§B', '§C') and token(FAMILY, body):
            bad8.append(name)
    check('S8', 'no cone or selector object in §B; ratRefl in no consumer section%s%s'
          % (tag, (' %s' % bad8[:3]) if bad8 else ''), not bad8)
    # S9
    local = {n for _, n in decls(mod)}
    pnames = [p[len(PREFIX):] for p in prints if p.startswith(PREFIX)]
    check('S9', 'exactly the %d frozen #print axioms lines, distinct, each naming a declaration of the module%s'
          % (N_PRINTS, tag),
          len(PRINTS) == N_PRINTS and prints == PRINTS and len(set(prints)) == N_PRINTS and len(pnames) == N_PRINTS
          and all(n in local for n in pnames))
    # V
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
    check('S2', 'the landed statements read from D are the frozen ones', landed == LANDED)
    mod = show(commit, MOD)
    module_checks(mod, landed=landed)
    note = show(commit, RESULT)
    if note is not None:
        ph = phrase_hits(note)
        check('S7', 'the result note carries none of the frozen phrases%s' % ((' %s' % ph) if ph else ''), not ph)
        a, b, c = verdicts(mod, landed) if mod is not None else ([], [], [])
        toks = note_tokens(note)
        check('V', 'the result note states exactly the computed tokens %s and no other outcome token (found %s)'
              % (a + b + c, toks), len(a) == 1 and len(b) == 1 and len(c) == 1 and sorted(toks) == sorted(a + b + c))
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                    show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family after the K1-SHARP-TESTS-1 family',
          census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def print_verdicts(commit):
    mod = show(commit, MOD)
    landed = landed_at_d()
    a, b, c = verdicts(mod, landed) if mod is not None else ([], [], [])
    print('VERDICT  BALL    %s' % ('/'.join(a) or 'none'))
    print('VERDICT  CONE    %s' % ('/'.join(b) or 'none'))
    print('VERDICT  STRICT  %s' % ('/'.join(c) or 'none'))
    check('V', 'the landed statements read from D are the frozen ones', landed == LANDED)
    check('V', 'exactly one outcome per cell', len(a) == 1 and len(b) == 1 and len(c) == 1)
