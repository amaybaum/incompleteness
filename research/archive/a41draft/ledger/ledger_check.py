"""Checks ledger41.json against the D41 blobs. Exit 0 and a final "ledger_check: OK" when every check holds.

1. every `old` occurs exactly once in D41's blob of its path; spans disjoint; applying the entries in ledger order
   gives the same text as splicing them by their D41 spans; kinds fit their paths; one final "append" entry
2. every rendered `new` (D41 values) carries no slot or selector; vocabulary lint on it
3. the five probes parse, and their ast.dump equals D41's once every str Constant is masked; the one exception is the
   bugfix at dita_local_escape_probe.py line 541, verified to remove exactly the vacuous element and its expected
   False; every changed format string keeps its %-conversions
4. the four Lean modules are byte-identical to D41 outside the leading /-! ... -/ block
5. the census registry parses as JSON, keeps every family's fields other than name and note, and every outcome label
6. ROADMAP.md keeps its line count and the cell separators of every line
7. the rendered/ files equal apply_ledger(D41 values) and carry no leftover slot or selector
8. every selector's false branch renders too (each flag flipped in turn) and passes the lint
9. values_from_measurements on the probes' printed objects (hulls from the D41 stub until run_hulls.log prints its
   object) yields every slot the ledger uses, and the rendering from it equals the rendering from the D41 values
The probes are parsed, never run.
"""
import ast, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import render41 as R41

PROBES = ['verification/lean/dita_hierarchy_probe.py', 'verification/lean/dita_arc_exclusivity_probe.py',
          'verification/lean/dita_local_escape_probe.py', 'verification/lean/dita_torus_probe.py',
          'verification/lean/dita_torus_locus_probe.py']
LEAN = ['verification/lean-mathlib/OIBridge/DitaHierarchy.lean', 'verification/lean-mathlib/OIBridge/DitaArcExclusivity.lean',
        'verification/lean-mathlib/OIBridge/DitaLocalEscape.lean', 'verification/lean-mathlib/OIBridge/DitaTorusLocus.lean']
REGISTRY = 'verification/lean-manuscript-census.json'
ROADMAP = 'verification/ROADMAP.md'
BUGFIX_PATH, BUGFIX_LINE, BUGFIX_ID = 'verification/lean/dita_local_escape_probe.py', 541, 'L21'
KINDS = {p: {'string', 'docstring', 'bugfix'} for p in PROBES}
KINDS.update({p: {'docstring'} for p in LEAN})
KINDS[REGISTRY] = {'registry'}
KINDS[ROADMAP] = {'roadmap', 'append'}

fails = []
def check(name, ok, detail=''):
    print('  %s  %s%s' % ('PASS' if ok else 'FAIL', name, ('  -- ' + str(detail)) if (detail and not ok) else ''))
    if not ok: fails.append(name)

# ---------------------------------------------------------------- vocabulary lint
NUMWORDS = set(R41._ONES + R41._TENS[2:]) | {'%s-%s' % (t, o) for t in R41._TENS[2:] for o in R41._ONES[1:10]}
CLASS_OK_BEFORE = {'row', 'factorization', 'realizable', 'conjugacy'}
def lint(text):
    """hits of the frozen vocabulary rules in one rendered new text"""
    hits = []
    flat = re.sub(r'\s+', ' ', text)
    for m in re.finditer(r'\b[Cc]lass(es)?\b', flat):
        before = re.findall(r"[\w'-]+", flat[:m.start()])
        after = flat[m.end():m.end() + 40]
        if not (before and before[-1].lower() in CLASS_OK_BEFORE) and not after.startswith(' of the product normalized set'):
            hits.append('bare class: ...%s' % flat[max(0, m.start() - 40):m.end() + 10])
    for m in re.finditer(r'\bstructures\b', flat):
        before = re.findall(r"[\w'{}.-]+", flat[:m.start()])[-4:]
        if before and before[-1] != 'partition' and any(w.lower() in NUMWORDS or w.isdigit() or R41.SLOT.fullmatch(w) for w in before):
            hits.append('bare structures count: ...%s' % flat[max(0, m.start() - 40):m.end()])
    for m in re.finditer(r'\b(formerly|now|corrected|no longer)\b', flat, re.I):
        hits.append('history word: %s' % m.group(0))
    for m in re.finditer(r'\b[A-Z]{4,}\b', flat):
        hits.append('capitals: %s' % m.group(0))
    for m in re.finditer(r'[Ee]xact computation over every', flat):
        if not re.match(r'[Ee]xact computation over every (other )?index map \((act 41|acts 40 and 41)\)', flat[m.start():]):
            hits.append('uncited all-alignment certification: ...%s' % flat[m.start():m.start() + 70])
    return hits

def leftovers(text):
    return R41.SLOT.findall(text) + [m.group(0)[:40] for m in R41.SELECTOR.finditer(text)] + (['[[ … ]] fragment'] if re.search(r'\[\[[^\]]*:\s*[a-z]\w*\.\w+\s*\]\]', text) else [])

# ---------------------------------------------------------------- AST helpers
def masked_dump(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            node.value = '<str>'
    return ast.dump(tree, include_attributes=False)

def str_constants(tree):
    return [n.value for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, str)]

CONV = re.compile(r'%[-#0 +]*(?:\d+|\*)?(?:\.\d+)?[sdirfFeEgGxXoc%]')

def remove_bugfix_elements(tree):
    """in D41's tree, the check call at line 541: remove the vacuous first element of the got tuple and the first
    element of the expected tuple, after verifying they are exactly any(x[2] == GEN_ONE for x in []) and False"""
    calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'check'
             and n.lineno == BUGFIX_LINE]
    assert len(calls) == 1, 'no unique check call at line %d' % BUGFIX_LINE
    c = calls[0]
    got, want = c.args[1], c.args[2]
    assert isinstance(got, ast.Tuple) and isinstance(want, ast.Tuple) and len(got.elts) == len(want.elts) == 5
    g0, w0 = got.elts[0], want.elts[0]
    assert ast.unparse(g0) in ('any((x[2] == GEN_ONE for x in []))', 'any(x[2] == GEN_ONE for x in [])'), ast.unparse(g0)
    assert isinstance(g0.args[0], ast.GeneratorExp) and isinstance(g0.args[0].generators[0].iter, ast.List) \
        and g0.args[0].generators[0].iter.elts == []
    assert isinstance(w0, ast.Constant) and w0.value is False
    assert ast.literal_eval(want) == (False, False, False, True, True)
    del got.elts[0]; del want.elts[0]
    return tree

# ---------------------------------------------------------------- main
def main():
    ledger = R41.load_ledger()
    paths = sorted(set(e['path'] for e in ledger))
    blobs = {p: R41.d41_blob(p) for p in paths}

    print('== 1. the ledger against D41 ==')
    ids = [e['id'] for e in ledger]
    check('entry ids distinct', len(ids) == len(set(ids)))
    check('every entry has the six fields', all(set(e) == {'id', 'path', 'old', 'new', 'kind', 'reason'} for e in ledger))
    multi = [(e['id'], blobs[e['path']].count(e['old'])) for e in ledger if blobs[e['path']].count(e['old']) != 1]
    check('every old occurs exactly once in its D41 blob (%d entries)' % len(ledger), not multi, multi)
    try:
        sp = R41.spans(ledger, blobs); ok, why = True, ''
    except ValueError as ex:
        sp, ok, why = None, False, ex
    check('the spans of each path are disjoint', ok, why)
    badkind = [(e['id'], e['kind']) for e in ledger if e['kind'] not in KINDS.get(e['path'], set())]
    check('every kind fits its path', not badkind, badkind)
    appends = [i for i, e in enumerate(ledger) if e['kind'] == 'append']
    check('exactly one append entry, the last, in ROADMAP.md', appends == [len(ledger) - 1] and ledger[-1]['path'] == ROADMAP, appends)
    a = ledger[-1]
    check('the append keeps its old text and adds after it', a['new'].startswith(a['old'][:-2]) and a['old'].endswith(' |') and a['new'].endswith(' |'))
    bug = [e for e in ledger if e['kind'] == 'bugfix']
    check('the one bugfix entry is census row L21 in dita_local_escape_probe.py at line 541',
          len(bug) == 1 and bug[0]['id'] == BUGFIX_ID and bug[0]['path'] == BUGFIX_PATH
          and blobs[BUGFIX_PATH][:blobs[BUGFIX_PATH].index(bug[0]['old'])].count('\n') + 1 == BUGFIX_LINE)
    files = R41.apply_ledger(R41.D41_VALUES, ledger, blobs)
    seq = dict(blobs)
    for e in ledger:  # sequential application in ledger order
        t = seq[e['path']]
        seq[e['path']] = t.replace(e['old'], R41.render(e['new'], R41.D41_VALUES), 1) if t.count(e['old']) == 1 else None
    check('applying the entries in ledger order equals splicing by D41 spans', all(seq[p] == files[p] for p in paths),
          [p for p in paths if seq[p] != files[p]])

    print('== 2. the rendered new texts ==')
    left, hits = [], []
    for e in ledger:
        r = R41.render(e['new'], R41.D41_VALUES)
        if leftovers(r): left.append((e['id'], leftovers(r)))
        # an append entry carries its old text (act 40's standing clause, D41 text) verbatim: only the addition is linted
        hits += [(e['id'], h) for h in lint(r[len(e['old']) - 2:] if e['kind'] == 'append' else r)]
    check('no rendered new text carries a slot or selector', not left, left)
    check('vocabulary: no bare class, no bare structures count, no history words, no capitals, act 41 cited', not hits, hits)

    print('== 3. the five probes: masked syntax trees ==')
    for p in PROBES:
        name = p.split('/')[-1]
        try:
            new_tree = ast.parse(files.get(p, blobs.get(p)))
        except SyntaxError as ex:
            check('%s parses' % name, False, ex); continue
        check('%s parses' % name, True)
        old_tree = ast.parse(blobs[p])
        if p == BUGFIX_PATH:
            check('%s: the D41 tree differs from the new tree outside strings (the bugfix)' % name,
                  masked_dump(ast.parse(blobs[p])) != masked_dump(ast.parse(files[p])))
            try:
                old_tree = remove_bugfix_elements(old_tree); ok, why = True, ''
            except AssertionError as ex:
                ok, why = False, ex
            check('%s: line 541 carries exactly the vacuous element and its expected False' % name, ok, why)
            nc = [n for n in ast.walk(ast.parse(files[p])) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                  and n.func.id == 'check' and isinstance(n.args[0], ast.Constant)
                  and str(n.args[0].value).startswith('M_COL and M_ROW, the two 2x8 index maps at u = -1')]
            check('%s: the fixed check has four components and expects (False, False, True, True)' % name,
                  len(nc) == 1 and len(nc[0].args[1].elts) == 4 and ast.literal_eval(nc[0].args[2]) == (False, False, True, True)
                  and 'for x in []' not in ast.unparse(nc[0]))
        a_s, b_s = str_constants(old_tree), str_constants(new_tree)
        eq = masked_dump(old_tree) == masked_dump(ast.parse(files[p]))
        check('%s: ast.dump equal with every str constant masked%s' % (name, ' (after the enumerated bugfix)' if p == BUGFIX_PATH else ''), eq)
        changed = [(x, y) for x, y in zip(a_s, b_s) if x != y]
        badconv = [x[:60] for x, y in changed if CONV.findall(x) != CONV.findall(y)]
        check('%s: %d string constants changed, every %%-conversion kept' % (name, len(changed)), eq and not badconv, badconv)

    print('== 4. the Lean modules: bytes outside the leading /-! ... -/ block ==')
    for p in LEAN:
        name = p.split('/')[-1]
        old, new = blobs[p], files.get(p, blobs[p])
        s0 = old.index('/-!'); e0 = old.index('-/', s0) + 2
        s1 = new.index('/-!'); e1 = new.index('-/', s1) + 2
        inside = all(s0 <= s and t <= e0 for s, t, _ in sp.get(p, []))
        check('%s: every span inside the block, bytes outside it unchanged' % name,
              inside and old[:s0] == new[:s1] and old[e0:] == new[e1:] and new.count('/-') == old.count('/-'))

    print('== 5. the census registry ==')
    try:
        jn, jo = json.loads(files[REGISTRY]), json.loads(blobs[REGISTRY]); ok, why = True, ''
    except ValueError as ex:
        ok, why = False, ex
    check('lean-manuscript-census.json parses as JSON', ok, why)
    if ok:
        def walk(o, n, path=''):
            diffs = []
            if isinstance(o, dict):
                if set(o) != set(n): return [path + ' keys']
                for k in o:
                    if o[k] != n[k] and k in ('name', 'note') and isinstance(o[k], str): continue
                    diffs += walk(o[k], n[k], path + '/' + k)
            elif isinstance(o, list):
                if len(o) != len(n): return [path + ' length']
                for i, (x, y) in enumerate(zip(o, n)): diffs += walk(x, y, '%s[%d]' % (path, i))
            elif o != n:
                diffs.append(path)
            return diffs
        d = walk(jo, jn)
        check('only "name" and "note" strings change', not d, d)
        out_o = re.findall(r'Outcome: ([A-Z0-9-]+)\.', blobs[REGISTRY]); out_n = re.findall(r'Outcome: ([A-Z0-9-]+)\.', files[REGISTRY])
        check('every outcome label kept (%d)' % len(out_o), out_o == out_n)
        acc = ['the search at the sorted alignment', 'at the sorted alignment', 'sorted order']
        notes = [x['note'] for x in jn['families'] if any('(act %d, Track B)' % k in x['name'] for k in (36, 37, 38, 40))]
        check('each of the act 36, 37, 38 and 40 notes keeps an account scoped to the sorted alignment and cites act 41',
              len(notes) == 4 and all(any(a_ in n for a_ in acc) and ('(act 41)' in n or '(acts 40 and 41)' in n) for n in notes), len(notes))

    print('== 6. ROADMAP.md ==')
    lo, ln = blobs[ROADMAP].split('\n'), files[ROADMAP].split('\n')
    check('line count kept', len(lo) == len(ln))
    check('the cell separators of every line kept', len(lo) == len(ln) and all(x.count('|') == y.count('|') for x, y in zip(lo, ln)))

    print('== 7. the rendered files ==')
    root = os.path.join(HERE, 'rendered')
    for p in paths:
        f = os.path.join(root, p)
        disk = open(f, encoding='utf-8').read() if os.path.exists(f) else None
        lo_ = [s for s in R41.SLOT.findall(disk or '')]
        sel = [m.group(0)[:40] for m in R41.SELECTOR.finditer(disk or '')]
        check('rendered/%s equals apply_ledger(D41 values), no leftover slot or selector, "[[" count as at D41' % p,
              disk == files[p] and len(lo_) == len(R41.SLOT.findall(blobs[p])) and not sel
              and disk.count('[[') == blobs[p].count('[['), (lo_, sel))

    print('== 8. the false branches ==')
    flags = sorted(set(m.group(3) for e in ledger for m in R41.SELECTOR.finditer(e['new'])))
    for fl in flags:
        v = dict(R41.D41_VALUES); v[fl] = not v[fl]
        errs, hits = [], []
        for e in ledger:
            try:
                r = R41.render(e['new'], v)
                hits += [(e['id'], h) for h in lint(r[len(e['old']) - 2:] if e['kind'] == 'append' else r)]
                if leftovers(r): errs.append((e['id'], leftovers(r)))
            except (KeyError, TypeError) as ex:
                errs.append((e['id'], str(ex)))
        check('%s false: every entry renders, lint clean' % fl, not errs and not hits, errs + hits)

    print('== 9. the rendering from the measured objects ==')
    meas, stub = R41.measurements_from_logs()
    check('the production and independent objects are present in the probe logs', meas['production'] is not None and meas['independent'] is not None)
    if meas['production'] is not None and meas['independent'] is not None:
        try:
            mv = R41.values_from_measurements(meas); ok, why = True, ''
        except (KeyError, ValueError, TypeError) as ex:
            mv, ok, why = None, False, ex
        check('values_from_measurements maps the objects to slots%s' % (' (hulls from the D41 stub)' if stub else ''), ok, why)
        if mv is not None:
            slots = set(m.group(1) for e in ledger for m in R41.SLOT.finditer(e['new'])) | set(
                m.group(3) for e in ledger for m in R41.SELECTOR.finditer(e['new']))
            missing = sorted(x for x in slots if x not in mv)
            check('every slot and flag the ledger uses is derived from the objects (%d)' % len(slots), not missing, missing)
            differ = sorted(k for k in R41.D41_VALUES if k in mv and mv[k] != R41.D41_VALUES[k])
            check('the derived values equal schema41.md\'s D41 values', not differ, differ)
            mf = R41.apply_ledger(mv, ledger, blobs)
            check('the rendering from the measured objects equals the rendering from the D41 values, file by file',
                  all(mf[p] == files[p] for p in paths), [p for p in paths if mf[p] != files[p]])

    print()
    if fails:
        print('ledger_check: FAILED (%d): %s' % (len(fails), fails)); return 1
    print('ledger_check: OK -- %d entries over %d paths' % (len(ledger), len(paths)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
