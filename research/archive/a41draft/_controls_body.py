
# ---------------------------------------------------------------- the vocabulary lint and the syntax-tree helpers
NUMWORDS = set(_ONES + _TENS[2:]) | {'%s-%s' % (t, o) for t in _TENS[2:] for o in _ONES[1:10]}
CLASS_OK_BEFORE = {'row', 'factorization', 'realizable', 'conjugacy'}
def lint(text):
    """hits of the frozen vocabulary rules; quoted spans ("…", `…`) are not linted"""
    hits = []
    flat = re.sub(r'\s+', ' ', re.sub(r'"[^"\n]*"|“[^”]*”|`[^`\n]*`', '"q"', text))
    for m in re.finditer(r'\b[Cc]lass(es)?\b', flat):
        before = re.findall(r"[\w'-]+", flat[:m.start()])
        if not (before and before[-1].lower() in CLASS_OK_BEFORE) and not flat[m.end():m.end() + 40].startswith(' of the product normalized set'):
            hits.append('bare class: ...%s' % flat[max(0, m.start() - 40):m.end() + 10])
    for m in re.finditer(r'\bstructures\b', flat):
        before = re.findall(r"[\w'{}.-]+", flat[:m.start()])[-4:]
        if before and before[-1] != 'partition' and any(w.lower() in NUMWORDS or w.isdigit() for w in before):
            hits.append('bare structures count: ...%s' % flat[max(0, m.start() - 40):m.end()])
    for m in re.finditer(r'\b(formerly|corrected|no longer)\b', flat, re.I):
        hits.append('history word: %s' % m.group(0))
    return hits
def leftovers(text):
    return SLOT.findall(text) + [m.group(0)[:40] for m in SELECTOR.finditer(text)]
def masked_dump(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            node.value = '<str>'
    return ast.dump(tree, include_attributes=False)
def remove_bugfix_elements(tree):
    """in D's tree of act 38's probe, the check call at line BUGFIX_LINE: remove the vacuous first element of the got
    tuple and of the expected tuple, after verifying they are exactly any(x[2] == GEN_ONE for x in []) and False"""
    calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'check'
             and n.lineno == BUGFIX_LINE]
    assert len(calls) == 1, 'no unique check call at line %d' % BUGFIX_LINE
    got, want = calls[0].args[1], calls[0].args[2]
    assert isinstance(got, ast.Tuple) and isinstance(want, ast.Tuple) and len(got.elts) == len(want.elts) == 5
    g0, w0 = got.elts[0], want.elts[0]
    assert isinstance(g0, ast.Call) and isinstance(g0.args[0], ast.GeneratorExp) and isinstance(g0.args[0].generators[0].iter, ast.List) \
        and g0.args[0].generators[0].iter.elts == [], ast.unparse(g0)
    assert isinstance(w0, ast.Constant) and w0.value is False and ast.literal_eval(want) == (False, False, False, True, True)
    del got.elts[0]; del want.elts[0]
    return tree
def lean_outside_docstring(text):
    a = text.index('/-!'); b = text.index('-/', a) + 2
    return text[:a], text[b:]

# ---------------------------------------------------------------- the ledger
def spans(ledger, blobs):
    out = {}
    for e in ledger:
        text = blobs[e['path']]
        n = text.count(e['old'])
        if n != 1:
            raise ValueError('%s: old occurs %d times in %s at D' % (e['id'], n, e['path']))
        s = text.index(e['old'])
        out.setdefault(e['path'], []).append((s, s + len(e['old']), e))
    for path, lst in out.items():
        lst.sort(key=lambda x: x[0])
        for (s1, e1, a), (s2, e2, b) in zip(lst, lst[1:]):
            if s2 < e1:
                raise ValueError('%s and %s overlap in %s' % (a['id'], b['id'], path))
    return out
def apply_ledger(values, blobs, ledger=None):
    ledger = LEDGER if ledger is None else ledger
    result = {}
    for path, lst in spans(ledger, blobs).items():
        text, pieces, pos = blobs[path], [], 0
        for s, t, e in lst:
            pieces.append(text[pos:s]); pieces.append(render(e['new'], values)); pos = t
        pieces.append(text[pos:])
        result[path] = ''.join(pieces)
    return result
def apply_workflow(text):
    for old, new in WORKFLOW_EDITS:
        if text.count(old) != 1:
            raise ValueError('workflow anchor not unique: %r' % old[:60])
        text = text.replace(old, new)
    return text

# ---------------------------------------------------------------- agreement and the label
def canonical(meas):
    return json.dumps(meas, sort_keys=True, separators=(',', ':'), ensure_ascii=True) + '\n'
def agree(meas):
    """the frozen decision function: (label, disagreements) from measurements.json alone"""
    dis = []
    pr, ind, hu = meas.get('production'), meas.get('independent'), meas.get('hulls')
    if pr is None or ind is None or hu is None:
        return 'A41-UNDECIDED', ['a path object is missing']
    pc, ic = pr['cases'], ind['cases']
    if set(pc) != set(ic):
        dis.append('the named test cases differ between the paths')
    for c in sorted(set(pc) & set(ic)):
        for n in ('strict', 'relaxed'):
            if _canon(pc[c][n]) != _canon(ic[c][n]):
                dis.append('%s, %s: production %d partition structures (%d alignments), independent %d (%d)' % (
                    c, n, len(pc[c][n]), sum(x[4] for x in pc[c][n]), len(ic[c][n]), sum(x[4] for x in ic[c][n])))
    if pr['coincidences'] != ind['coincidences']:
        dis.append('the coincidences of named test cases differ between the paths')
    if len(pc) != N_CASES or ind.get('n_cases') != N_CASES:
        dis.append('not %d named test cases' % N_CASES)
    if not all(x[2] and x[3] for x in pr['fibres']):
        dis.append('a fibre of the projection has the wrong size')
    for n in ('strict', 'relaxed'):
        s = pr['sig'][n]
        if not s['closed']:
            dis.append('the realizing triples at SIG are not closed under the stabilizer (%s)' % n)
        if not all(s['burnside_agrees']):
            dis.append('an orbit count at SIG disagrees with Burnside\'s count (%s)' % n)
    if list(hu['second_test']) != [hu['distinct_mat'], hu['distinct_gauge']]:
        dis.append('the two hull equality tests disagree: %s against %s' % (hu['second_test'], [hu['distinct_mat'], hu['distinct_gauge']]))
    if not all(x[4] for x in pr['added_reconstructed']):
        dis.append('an added partition structure does not reconstruct')
    return ('A41-CENSUS-CORRECTED', []) if not dis else ('A41-CENSUS-DIVERGES', dis)

# ---------------------------------------------------------------- the checks on a tree
def check_tree(D, E, diff, report):
    """D, E: {path: text or None}; diff: the name-status lines of D..E; report(name, ok, detail)"""
    meas_text = E.get(RECORD + 'measurements.json')
    meas = json.loads(meas_text) if meas_text else None
    label, dis = agree(meas) if meas is not None else ('A41-UNDECIDED', ['no measurements'])
    report('measurements.json is canonical', meas_text is None or meas_text == canonical(meas))
    note = E.get(RECORD + 'result.md') or ''
    outs = re.findall(r'^\*\*Outcome:\*\* `([A-Z0-9-]+)`$', note, re.M)
    report('the result note carries exactly one outcome line, the label agree() gives', outs == [label], (outs, label))
    corrected = label == 'A41-CENSUS-CORRECTED'
    expected = {('A', p) for p in NEW_FILES} | {('A', RECORD + f) for f in RECORD_FILES} | {('M', WORKFLOW)}
    if meas_text is not None: expected.add(('A', RECORD + 'measurements.json'))
    if corrected: expected |= {('M', p) for p in SURFACE_PATHS}
    got = {tuple(l.split('\t', 1)) for l in diff if l.strip()}
    report('the governed set: D..E changes exactly the frozen paths for the label', got == expected, sorted(got ^ expected))
    for p, blob in NEW_FILE_BLOBS.items():
        report('%s has its frozen blob' % p, E.get(p) is not None and git_blob(E[p].encode('utf-8')) == blob)
    report('the workflow is D\'s with the frozen edit', E.get(WORKFLOW) == apply_workflow(D[WORKFLOW]))
    report('the guard is D\'s', E.get(GUARD) == D[GUARD])
    hist = sorted(p for p in D if p.startswith(HISTORICAL_PREFIXES) or p in HISTORICAL_FILES)
    report('every historical file of acts 36 to 40 is byte-identical to D\'s, and none is added', all(E.get(p) == D[p] for p in hist) and
           not any(p.startswith(HISTORICAL_PREFIXES) and p not in D for p in E), [p for p in hist if E.get(p) != D[p]])
    if corrected:
        values = values_from_measurements(meas)
        rendered = apply_ledger(values, {p: D[p] for p in SURFACE_PATHS})
        for p in SURFACE_PATHS:
            report('%s equals its rendering from measurements.json' % p, E.get(p) == rendered[p])
            report('%s: no template slot or selector left' % p, not leftovers(E.get(p) or ''))
        for p in OLD_PROBES:
            tD = ast.parse(D[p]); tE = ast.parse(E[p])
            if p == BUGFIX_PATH: tD = remove_bugfix_elements(tD)
            report('%s: the syntax tree is D\'s with string constants masked, except the one enumerated bugfix' % p, masked_dump(tD) == masked_dump(tE))
        for p in LEAN_PATHS:
            report('%s: unchanged outside the leading docstring' % p, lean_outside_docstring(E[p]) == lean_outside_docstring(D[p]))
        json.loads(E[CENSUS])
        sentence = render(SENTENCES[label], values)
    else:
        for p in SURFACE_PATHS:
            report('%s is D\'s' % p, E.get(p) == D[p])
        values = {'note.disagreements': '; '.join(dis), 'note.failing': '; '.join(dis)}
        sentence = render(SENTENCES[label], values)
    report('the result note carries the post-round sentence rendered for its label', ('> ' + sentence) in note)
    for shard in SHARD_NAMES:
        report('the result note carries the %s shard\'s final line' % shard, re.search(r'^%s: OK -- REPLAYED' % shard, note, re.M) is not None or label == 'A41-UNDECIDED')
    report('the result note obeys the vocabulary rules', not lint(note), lint(note)[:3])
    return label

# ---------------------------------------------------------------- git
def git(*args, repo='.'):
    return subprocess.run(['git', '-C', repo] + list(args), capture_output=True, check=True).stdout
def git_blob(b):
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()
def tree_texts(commit, paths, repo='.'):
    out = {}
    for p in paths:
        r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (commit, p)], capture_output=True)
        out[p] = r.stdout.decode('utf-8') if r.returncode == 0 else None
    return out
def paths_under(commit, prefixes, repo='.'):
    names = git('ls-tree', '-r', '--name-only', commit, repo=repo).decode().split('\n')
    return [n for n in names if n.startswith(prefixes)]
def check_E(E, repo='.'):
    fails = []
    def report(name, ok, detail=''):
        print('  %s  %s%s' % ('PASS' if ok else 'FAIL', name, '' if ok or not detail else '  -- %s' % (detail,)))
        if not ok: fails.append(name)
    hist = sorted(set(paths_under(D_COMMIT, HISTORICAL_PREFIXES, repo)) | set(HISTORICAL_FILES))
    histE = paths_under(E, HISTORICAL_PREFIXES, repo)
    base = sorted(set([WORKFLOW, GUARD, CENSUS] + SURFACE_PATHS + hist))
    D = tree_texts(D_COMMIT, base, repo)
    Et = tree_texts(E, sorted(set(base + histE + NEW_FILES + [RECORD + f for f in RECORD_FILES + ['measurements.json']])), repo)
    diff = git('diff', '--no-renames', '--name-status', D_COMMIT, E, repo=repo).decode().split('\n')
    label = check_tree(D, Et, diff, report)
    print('controls: check E -- %s, label %s' % ('OK' if not fails else 'FAILED (%d)' % len(fails), label))
    return not fails

# ---------------------------------------------------------------- the self-test
def self_test(meas_path=None, repo='.'):
    ok = True; n_mut = 0; missed = []
    here = os.path.dirname(os.path.abspath(__file__))
    def line(good, text):
        nonlocal ok
        print('  %s  %s' % ('PASS' if good else 'FAIL', text)); ok &= bool(good)
    prereg = open(os.path.join(here, 'preregistration.md'), encoding='utf-8').read()
    missing = [s[:60] for s in [e['new'] for e in LEDGER] + [e['old'] for e in LEDGER] + list(SENTENCES.values()) if s not in prereg]
    line(not missing, 'every ledger text and sentence template is carried verbatim by the preregistration' + ('' if not missing else ' -- %s' % missing[:2]))
    blobs = tree_texts(D_COMMIT, SURFACE_PATHS + [WORKFLOW], repo)
    spans(LEDGER, blobs); apply_workflow(blobs[WORKFLOW])
    line(True, "every ledger entry is unique in D's file and the spans are disjoint; the workflow anchors are unique")
    def detects(name, fn):
        nonlocal n_mut
        n_mut += 1
        try: d = fn()
        except Exception: d = True
        if not d: missed.append(name)
    meas_path = meas_path or os.path.join(here, 'measurements.json')
    if os.path.exists(meas_path):
        import copy
        meas = json.load(open(meas_path, encoding='utf-8'))
        label, dis = agree(meas)
        line(label == 'A41-CENSUS-CORRECTED', 'agree() on the measured object: %s' % label)
        def mut(f):
            m = copy.deepcopy(meas); f(m); return agree(m)[0] != 'A41-CENSUS-CORRECTED'
        detects('a changed alignment count', lambda: mut(lambda m: m['production']['cases']['SIG']['strict'][0].__setitem__(4, 1)))
        detects('a dropped named test case', lambda: mut(lambda m: m['independent']['cases'].pop('Pu(u5)')))
        detects('a dropped coincidence', lambda: mut(lambda m: m['production']['coincidences'].pop()))
        detects('a failed Burnside count', lambda: mut(lambda m: m['production']['sig']['strict'].__setitem__('burnside_agrees', [True, False, True, True])))
        detects('an open stabilizer action', lambda: mut(lambda m: m['production']['sig']['relaxed'].__setitem__('closed', False)))
        detects('a wrong fibre size', lambda: mut(lambda m: m['production']['fibres'][0].__setitem__(2, False)))
        detects('the two hull equality tests disagreeing', lambda: mut(lambda m: m['hulls'].__setitem__('second_test', [1, 1])))
        detects('an added partition structure not reconstructing', lambda: mut(lambda m: m['production']['added_reconstructed'][0].__setitem__(4, False)))
        detects('a missing path object', lambda: mut(lambda m: m.pop('hulls')))
        values = values_from_measurements(meas)
        rendered = apply_ledger(values, blobs)
        tD_fix = masked_dump(remove_bugfix_elements(ast.parse(blobs[BUGFIX_PATH])))
        for p in OLD_PROBES:
            tD = masked_dump(remove_bugfix_elements(ast.parse(blobs[p]))) if p == BUGFIX_PATH else masked_dump(ast.parse(blobs[p]))
            line(tD == masked_dump(ast.parse(rendered[p])), '%s: the rendering differs from D in string constants only, but for the enumerated bugfix' % p)
        bug = next(e for e in LEDGER if e['kind'] == 'bugfix')
        undone = rendered[BUGFIX_PATH].replace(render(bug['new'], values), bug['old'], 1)
        detects('the bugfix undone', lambda: masked_dump(ast.parse(undone)) != tD_fix)
        second = rendered[BUGFIX_PATH].replace('(False, False, True, True)', '(False, False, True, False)', 1)
        detects('a second non-string change to an earlier probe', lambda: second != rendered[BUGFIX_PATH] and masked_dump(ast.parse(second)) != tD_fix)
        for p in LEAN_PATHS:
            line(lean_outside_docstring(rendered[p]) == lean_outside_docstring(blobs[p]), '%s: the rendering changes only the leading docstring' % p)
        detects('a Lean byte changed outside the docstring', lambda: lean_outside_docstring(rendered[LEAN_PATHS[0]] + ' ') != lean_outside_docstring(blobs[LEAN_PATHS[0]]))
        json.loads(rendered[CENSUS])
        line(not [p for p in rendered if leftovers(rendered[p])], 'no slot or selector is left in any rendering, and the registry parses')
        detects('a slot with no measured value', lambda: render('{sig.nonexistent}', values) is None)
        detects('a boolean read as a number', lambda: render('{hull.dF_ok}', values) is None)
        detects('pretty-printed measurements', lambda: canonical(meas) != json.dumps(meas, indent=1))
        s = render(SENTENCES['A41-CENSUS-CORRECTED'], values)
        line(not lint(s) and not leftovers(s), 'the corrected sentence renders and obeys the vocabulary rules')
    else:
        line(True, 'no measurements.json beside this file: the measurement-dependent checks are not run')
    detects('a bare class', lambda: bool(lint('the nine classes of the stratum point')))
    detects('a bare structures count', lambda: bool(lint('the twenty structures at SIG')))
    detects('a history word', lambda: bool(lint('the census, formerly eighteen')))
    detects('a quoted class is not a hit', lambda: not lint('act 37\'s "nine classes" are the nine partition orbits'))
    detects('a dropped shard requirement', lambda: apply_workflow(blobs[WORKFLOW]).replace('          test "${A41H_RESULT}" = success\n', '') != apply_workflow(blobs[WORKFLOW]))
    detects('a non-unique ledger anchor', lambda: spans([{'id': 'x', 'path': WORKFLOW, 'old': '\n', 'new': ''}], blobs) is None)
    line(not missed, '%d mutation controls, each detected%s' % (n_mut, '' if not missed else ' -- missed: %s' % missed))
    print('controls: self-test %s' % ('OK' if ok else 'FAILED'))
    return ok

if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['--self-test']: sys.exit(0 if self_test(a[1] if len(a) > 1 else None) else 1)
    if len(a) == 2 and a[0] == 'agree':
        label, dis = agree(json.load(open(a[1], encoding='utf-8'))); print(label); [print('  ' + d) for d in dis]; sys.exit(0)
    if len(a) == 3 and a[0] == 'render':
        meas = json.load(open(a[1], encoding='utf-8'))
        if agree(meas)[0] != 'A41-CENSUS-CORRECTED': print('controls: nothing to render: the label is not corrected'); sys.exit(1)
        blobs = tree_texts(D_COMMIT, SURFACE_PATHS)
        for p, text in apply_ledger(values_from_measurements(meas), blobs).items():
            dest = os.path.join(a[2], p); os.makedirs(os.path.dirname(dest), exist_ok=True); open(dest, 'w', encoding='utf-8').write(text)
        print('controls: rendered %d surfaces' % len(SURFACE_PATHS)); sys.exit(0)
    if len(a) == 2 and a[0] == 'check':
        sys.exit(0 if check_E(a[1]) else 1)
    print(__doc__); sys.exit(2)
