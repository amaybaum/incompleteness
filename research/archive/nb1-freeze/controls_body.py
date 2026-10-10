def blob(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


# ---- the expected tree ------------------------------------------------------------------------------------------
def expected_census(d_census):
    c = json.loads(d_census)
    c['families'].append(json.loads(json.dumps(FAMILY)))
    return (json.dumps(c, indent=2, ensure_ascii=False) + '\n').encode()


def expected_text(d_files, path):
    text = d_files[path].decode()
    if path == WORKFLOW:
        for old, new in WORKFLOW_EDITS:
            if text.count(old) != 1:
                raise ValueError('workflow anchor')
            text = text.replace(old, new)
        return text.encode()
    if path == IMPORTS:
        if text.count(IMPORT_EDIT[0]) != 1:
            raise ValueError('import anchor')
        return text.replace(*IMPORT_EDIT).encode()
    if path == CENSUS:
        return expected_census(d_files[path])
    return d_files[path]


# ---- the checks -------------------------------------------------------------------------------------------------
def statement(module, name):
    for sep in (' ', '\n'):
        k = module.find('theorem ' + name + sep)
        if k >= 0:
            return module[k:module.index(':=', k) + 2]
    return None


def check_module(module, label):
    codes = []
    if not module.startswith(FROZEN['header']):
        codes.append('module:header')
    if re.search(r'^(?:noncomputable )?(?:def|abbrev|instance|structure|class|inductive) ', module, re.M):
        codes.append('module:definition-budget')
    for tok in FORBIDDEN:
        if re.search(r'(?<![A-Za-z_])' + re.escape(tok), module):
            codes.append('module:forbidden:' + tok.strip())
    for opt in re.findall(r'^set_option .*$', module, re.M):
        if opt != ALLOWED_OPTION:
            codes.append('module:set_option')
    names = re.findall(r'^theorem (\S+)', module, re.M)
    for n in names:
        if n not in FROZEN['statements'] and not n.startswith('nb1_shared_'):
            codes.append('module:unknown-name:' + n)
        if module.count('#print axioms OIBridge.NativeGateBall.' + n + '\n') != 1:
            codes.append('module:print-axioms:' + n)
    for n, text in FROZEN['statements'].items():
        if n == VERDICT and label != LABELS[0]:
            if n in names:
                codes.append('module:verdict-under-undecided')
            continue
        if statement(module, n) != text:
            codes.append('module:statement:' + n)
    return codes


def check_note(note, label, module_blob):
    codes = []
    lines = note.split('\n')
    outs = [l for l in lines if l.startswith('**Outcome:**')]
    if outs != ['**Outcome:** `%s`' % label]:
        codes.append('note:outcome-line')
    for lab in LABELS:
        if note.count(SENTENCES[lab]) != (1 if lab == label else 0):
            codes.append('note:sentence:' + lab)
    if note.count(CLAUSE_MENTION) != 1 or note.count(CLAUSE) != 1 \
            or note.index(CLAUSE) < note.index(CLAUSE_MENTION):
        codes.append('note:clause')
    if sum(1 for l in lines if l.strip().strip('`').startswith(PROBE_OK_PREFIX)) != 1:
        codes.append('note:probe-line')
    if '`%s`' % REFERENCE_BLOB not in note or '`%s`' % module_blob not in note:
        codes.append('note:blobs')
    if module_blob != REFERENCE_BLOB and 'departure from the reference implementation' not in note:
        codes.append('note:departure')
    rest = note
    for t in list(SENTENCES.values()) + [CLAUSE]:
        rest = rest.replace(t, '')
    if any(ph.lower() in rest.lower() for ph in FORBIDDEN_NOTE):
        codes.append('note:forbidden-claim')
    return codes


def check_tree(d_files, e_files, changed, probe_blob=PROBE_BLOB):
    """d_files/e_files: path -> bytes (None if absent) for every path consulted; changed: {path: 'A'|'M'|'D'}."""
    codes = []
    note = e_files.get(RDIR + 'result.md')
    if note is None:
        return ['note:absent']
    note = note.decode()
    m = re.search(r'^\*\*Outcome:\*\* `([^`]*)`', note, re.M)
    label = m.group(1) if m and m.group(1) in LABELS else None
    if label is None:
        return ['note:outcome-line']
    module = e_files.get(MODULE)
    if module is None:
        return ['module:absent']
    codes += check_module(module.decode(), label)
    codes += check_note(note, label, blob(module))
    if e_files.get(PROBE) is None or blob(e_files[PROBE]) != probe_blob:
        codes.append('probe:blob')
    for path in (WORKFLOW, IMPORTS, CENSUS):
        try:
            exp = expected_text(d_files, path)
        except ValueError:
            exp = None
        if e_files.get(path) != exp:
            codes.append('surface:' + path)
    want = {RDIR + 'preregistration.md': 'A', RDIR + 'controls.py': 'A', RDIR + 'result.md': 'A',
            MODULE: 'A', PROBE: 'A', IMPORTS: 'M', CENSUS: 'M', WORKFLOW: 'M'}
    if changed != want:
        codes.append('paths')
    return codes


# ---- git access -------------------------------------------------------------------------------------------------
def git(*args):
    return subprocess.run(('git',) + args, capture_output=True, check=True).stdout


def show(commit, path):
    r = subprocess.run(['git', 'show', '%s:%s' % (commit, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def consulted():
    return [RDIR + 'result.md', RDIR + 'preregistration.md', MODULE, PROBE, WORKFLOW, IMPORTS, CENSUS]


def cmd_check(commit, freeze=None):
    d_files = {p: show(D, p) for p in consulted()}
    e_files = {p: show(commit, p) for p in consulted()}
    changed = {}
    for line in git('diff', '--no-renames', '--name-status', D, commit).decode().splitlines():
        st, path = line.split('\t', 1)
        changed[path] = st
    codes = check_tree(d_files, e_files, changed)
    if freeze:
        fdiff = git('diff', '--no-renames', '--name-status', D, freeze).decode().split()
        if fdiff != ['A', RDIR + 'preregistration.md']:
            codes.append('freeze:delta')
        if show(freeze, RDIR + 'preregistration.md') != e_files[RDIR + 'preregistration.md']:
            codes.append('freeze:preregistration')
    if codes:
        print('controls: check FAILED: ' + '; '.join(codes))
        return 1
    print('controls: check OK')
    return 0


# ---- self-test --------------------------------------------------------------------------------------------------
def synthetic_module(label):
    parts = [FROZEN['header'], 'namespace OIBridge\nnamespace NativeGateBall\n\n']
    names = []
    for n, text in FROZEN['statements'].items():
        if n == VERDICT and label != LABELS[0]:
            continue
        parts.append(text + ' by\n  exact placeholder\n\n')
        names.append(n)
    parts.append('end NativeGateBall\nend OIBridge\n\n')
    for n in names:
        parts.append('#print axioms OIBridge.NativeGateBall.%s\n' % n)
    return ''.join(parts).encode()


def synthetic_row(d_files, label):
    e = dict(d_files)
    module = synthetic_module(label)
    e[MODULE] = module
    e[PROBE] = SYNTHETIC_PROBE
    for path in (WORKFLOW, IMPORTS, CENSUS):
        e[path] = expected_text(d_files, path)
    e[RDIR + 'preregistration.md'] = b'frozen'
    note = ['# result', '', '**Outcome:** `%s`' % label, '', SENTENCES[label], '', CLAUSE_MENTION, '', CLAUSE, '',
            '`' + PROBE_OK_PREFIX + ' (synthetic)`', '',
            'reference `%s`, module at E `%s`, departure from the reference implementation' % (REFERENCE_BLOB, blob(module))]
    e[RDIR + 'result.md'] = '\n'.join(note).encode()
    changed = {RDIR + 'preregistration.md': 'A', RDIR + 'controls.py': 'A', RDIR + 'result.md': 'A',
               MODULE: 'A', PROBE: 'A', IMPORTS: 'M', CENSUS: 'M', WORKFLOW: 'M'}
    return e, changed


def self_test():
    here = os.path.dirname(os.path.abspath(__file__))
    prereg = open(os.path.join(here, 'preregistration.md'), encoding='utf-8').read()
    bad = []
    for lab in LABELS:
        if prereg.count(SENTENCES[lab]) != 1:
            bad.append('prereg:sentence:' + lab)
    if prereg.count(CLAUSE) < 1:
        bad.append('prereg:clause')
    if FROZEN['header'].rstrip('\n') not in prereg:
        bad.append('prereg:header')
    for n, text in FROZEN['statements'].items():
        if text not in prereg:
            bad.append('prereg:statement:' + n)
    if WORKFLOW_JOB not in prereg:
        bad.append('prereg:workflow')
    if FAMILY['name'] not in prereg or FAMILY['note'] not in prereg:
        bad.append('prereg:census-family')
    for b in (PROBE_BLOB, REFERENCE_BLOB):
        if b not in prereg:
            bad.append('prereg:blob:' + b)
    if prereg.count(PROBE_OK_PREFIX) < 1:
        bad.append('prereg:probe-line')
    if bad:
        print('controls: self-test FAILED (constants): ' + '; '.join(bad))
        return 1
    print('controls: the frozen constants match the preregistration beside this file')

    d_files = {p: show(D, p) for p in consulted()}
    rows = {}
    for lab in LABELS:
        e, ch = synthetic_row(d_files, lab)
        codes = check_tree(d_files, e, ch, probe_blob=blob(SYNTHETIC_PROBE))
        if codes:
            print('controls: self-test FAILED: synthetic row %s: %s' % (lab, codes))
            return 1
        rows[lab] = (e, ch)
    print('controls: 2 rows hold as frozen')

    muts = []
    def mut(name, code, label, fn):
        muts.append((name, code, label, fn))
    P, U = LABELS
    def edit_file(path, old, new):
        def f(e, ch):
            if old.encode() not in e[path]:
                raise AssertionError('mutation anchor absent: ' + old)
            e[path] = e[path].replace(old.encode(), new.encode(), 1)
        return f
    def append_note(text):
        return lambda e, ch: e.__setitem__(RDIR + 'result.md', e[RDIR + 'result.md'] + text.encode())
    mut('verdict removed under CORE-PROVED', 'module:statement:' + VERDICT, P,
        edit_file(MODULE, 'theorem ' + VERDICT, 'theorem nb1_other'))
    mut('verdict present under UNDECIDED', 'module:verdict-under-undecided', U,
        lambda e, ch: e.__setitem__(MODULE, e[MODULE] + FROZEN['statements'][VERDICT].encode()
                                    + b' by\n  x\n#print axioms OIBridge.NativeGateBall.' + VERDICT.encode() + b'\n'))
    mut('parity weakened by an involution hypothesis', 'module:statement:parity', P,
        edit_file(MODULE, '(P L : V →ₗ[ℝ] V) (hL', '(P L : V →ₗ[ℝ] V) (hP : P ∘ₗ P = LinearMap.id) (hL'))
    mut('the averaging bound weakened', 'module:statement:averaging_bound', P,
        edit_file(MODULE, '((p : ℝ) - 1) * (∑ j, g j ^ 2) + (∑ i, ∑ j, K j i ^ 2) ≤ 0 :=',
                  '((p : ℝ) - 2) * (∑ j, g j ^ 2) + (∑ i, ∑ j, K j i ^ 2) ≤ 0 :='))
    mut('the count loosened', 'module:statement:dim_of_bounds', P,
        edit_file(MODULE, '(hd : p + q + 1 = d) :\n    d = 1 ∨ d = 3 :=', '(hd : p + q + 1 = d) :\n    d ≤ 3 :='))
    mut('the header claims a kernel theorem', 'module:header', P,
        edit_file(MODULE, 'That theorem is not a kernel theorem', 'That theorem is a kernel theorem'))
    mut('an import added to the header', 'module:header', P,
        edit_file(MODULE, 'import Mathlib.Tactic.Ring\n', 'import Mathlib.Tactic.Ring\nimport OIBridge.FactorExchange\n'))
    mut('a definition added', 'module:definition-budget', P,
        edit_file(MODULE, 'end NativeGateBall', 'def extra : Nat := 0\n\nend NativeGateBall'))
    mut('a missing #print axioms', 'module:print-axioms:parity', P,
        edit_file(MODULE, '#print axioms OIBridge.NativeGateBall.parity\n', ''))
    mut('sorry in the module', 'module:forbidden:sorry', P, edit_file(MODULE, 'exact placeholder', 'sorry'))
    mut('an axiom declared', 'module:forbidden:axiom', P,
        edit_file(MODULE, 'end NativeGateBall', 'axiom oneN : True\n\nend NativeGateBall'))
    mut('an unlisted theorem name', 'module:unknown-name:helper', P,
        edit_file(MODULE, 'end NativeGateBall', 'theorem helper : True := trivial\n\nend NativeGateBall'))
    mut('a set_option', 'module:set_option', P,
        edit_file(MODULE, 'namespace NativeGateBall\n', 'namespace NativeGateBall\nset_option maxHeartbeats 0\n'))
    mut('the probe changed', 'probe:blob', P, lambda e, ch: e.__setitem__(PROBE, b'# not the frozen probe\n'))
    mut('the workflow edited beyond the frozen edit', 'surface:' + WORKFLOW, P,
        lambda e, ch: e.__setitem__(WORKFLOW, e[WORKFLOW] + b'# extra\n'))
    mut('the probe shard left out of the aggregate', 'surface:' + WORKFLOW, P,
        edit_file(WORKFLOW, '          test "${NB1_RESULT}" = success\n', ''))
    mut('the import misplaced', 'surface:' + IMPORTS, P,
        lambda e, ch: e.__setitem__(IMPORTS, d_files[IMPORTS] + b'import OIBridge.NativeGateBall\n'))
    mut('the census family made current', 'surface:' + CENSUS, P,
        lambda e, ch: e.__setitem__(CENSUS, b'"status": "current"'.join(e[CENSUS].rsplit(b'"status": "kernel-only"', 1))))
    mut('a manuscript touched', 'paths', P, lambda e, ch: ch.__setitem__('papers/Main.md', 'M'))
    mut('the roadmap touched', 'paths', P, lambda e, ch: ch.__setitem__('verification/ROADMAP.md', 'M'))
    mut('a governed path missing', 'paths', P, lambda e, ch: ch.pop(WORKFLOW))
    mut('two outcome lines', 'note:outcome-line', P, append_note('\n**Outcome:** `%s`\n' % U))
    mut("the other label's sentence", 'note:sentence:' + U, P, append_note('\n' + SENTENCES[U]))
    mut('the clause missing', 'note:clause', P, edit_file(RDIR + 'result.md', CLAUSE, ''))
    mut('the clause before its mention', 'note:clause', P,
        lambda e, ch: e.__setitem__(RDIR + 'result.md', CLAUSE.encode() + b'\n' + e[RDIR + 'result.md'].replace(CLAUSE.encode(), b'')))
    mut('the probe line missing', 'note:probe-line', P, edit_file(RDIR + 'result.md', PROBE_OK_PREFIX, 'probe'))
    mut('the blobs missing', 'note:blobs', P, edit_file(RDIR + 'result.md', REFERENCE_BLOB, 'x'))
    mut('the departure unreported', 'note:departure', P,
        edit_file(RDIR + 'result.md', 'departure from the reference implementation', ''))
    mut('the note claims OI selects d = 3', 'note:forbidden-claim', P, append_note('\nHence OI selects d = 3.\n'))
    mut('the note calls the theorem kernel-proved for every d', 'note:forbidden-claim', U,
        append_note('\nThe ball theorem is a kernel theorem for every d.\n'))
    mut('no result note', 'note:absent', P, lambda e, ch: e.__setitem__(RDIR + 'result.md', None))
    failed = 0
    for name, code, lab, fn in muts:
        e, ch = synthetic_row(d_files, lab)
        fn(e, ch)
        codes = check_tree(d_files, e, ch, probe_blob=blob(SYNTHETIC_PROBE))
        if code not in codes:
            print('controls: self-test FAILED: mutation "%s" did not fail with %s (got %s)' % (name, code, codes))
            failed += 1
    if failed:
        return 1
    print('controls: %d mutation controls fail as required' % len(muts))
    print('controls: self-test OK')
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--self-test']:
        sys.exit(self_test())
    if len(a) in (2, 4) and a[0] == 'check' and (len(a) == 2 or a[2] == '--freeze'):
        sys.exit(cmd_check(a[1], a[3] if len(a) == 4 else None))
    print(__doc__)
    sys.exit(2)
