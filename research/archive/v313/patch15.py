p = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/rd/controls.py'
t = open(p).read()
old = '''"""controls.py -- round V3-13's two retirement controls, read from git objects at named commits.

Usage:
    python3 controls.py history <repository> <commit>
    python3 controls.py callers <repository> <commit> <verifier commit>
    python3 controls.py --self-test
'''
new = '''"""controls.py -- round V3-13's retirement controls, read from git objects at named commits.

Usage:
    python3 controls.py history <repository> <commit>
    python3 controls.py callers <repository> <commit> <verifier commit>
    python3 controls.py pc4s <repository> <D>
    python3 controls.py vacuity <repository> <commit> <D>
    python3 controls.py --self-test
'''
assert t.count(old) == 1; t = t.replace(old, new)
old = '''Both read git objects and nothing else, so a commit gives the same report on any checkout."""'''
new = '''pc4s      The four R7-PC4S predicates of the amendment (lines 17854 and 17999-18001 of the guard at
          <D>), each evaluated with the guard's own definitions that it reaches, taken from the
          guard at <D> and executed with every file read and directory listing served from <D>'s
          tree and recorded. Passes when all four hold, every file read is a record of the
          legacy-records manifest (V3-12's, at <D>) or the migration manifest, read as a lookup,
          every directory listed is a closed namespace of that manifest, and a one-byte change to
          round PC4's seal record makes the unmutated predicate fail.

vacuity   The two self-satisfying predicates of the amendment, R7-OLT's _olt_supersessions and
          R7-OLN's _oln_supersession, taken from the 1,610 transformation of the guard at <D> (the
          record directory's retire.py --census-only, at <commit>) and evaluated on that guard's
          text, on that text with every occurrence of each string they seek outside their own
          definitions removed, and on their own definitions alone, all of which must hold. Also
          reported, not required: the same evaluations on the guard at <D>.

All read git objects and nothing else, so a commit gives the same report on any checkout."""'''
assert t.count(old) == 1; t = t.replace(old, new)
old = "import ast\nimport re\nimport subprocess\nimport sys\n"
new = ("import ast\nimport io\nimport json\nimport os\nimport posixpath\nimport re\nimport subprocess\n"
       "import sys\nimport tempfile\nimport types\n")
assert t.count(old) == 1; t = t.replace(old, new)
old = "def self_test():"
new = '''GUARD = 'verification/lean/edge_rigidity_probe.py'
RD = 'verification/infrastructure/round-v3-13-retirement/'
CENSUS = 'verification/infrastructure/round-v3-12-retirement-census/census.json'
LEGACY = 'verification/infrastructure/round-v3-12-retirement-census/legacy-records.json'
PC4S_LINES = (17854, 17999, 18000, 18001)
ROOT = '/virtual'


def raw(repo, commit, path):
    r = subprocess.run(['git', '-C', repo, 'cat-file', 'blob', '%s:%s' % (commit, path)],
                       capture_output=True)
    return r.stdout if r.returncode == 0 else None


def bindings(stmt):
    """The module-level names a top-level statement binds."""
    out = set()
    for n in ast.walk(stmt):
        if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store):
            out.add(n.id)
        elif isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n is stmt:
            out.add(n.name)
        elif isinstance(n, (ast.Import, ast.ImportFrom)):
            out |= {(a.asname or a.name).split('.')[0] for a in n.names}
    return out


def closure(tree, roots, before):
    """The top-level statements before line `before` that bind a name the roots need, transitively
    (each such statement's own loads included), in file order."""
    body = [s for s in tree.body if s.lineno < before]
    need, chosen, todo = set(), set(), set(roots)
    while todo:
        nm = todo.pop()
        if nm in need:
            continue
        need.add(nm)
        for i, s in enumerate(body):
            if i not in chosen and nm in bindings(s):
                chosen.add(i)
                todo |= {n.id for n in ast.walk(s) if isinstance(n, ast.Name)
                         and isinstance(n.ctx, ast.Load)}
    return [body[i] for i in sorted(chosen)]


class VirtualTree:
    """Files and directories of one commit, served under ROOT, every access recorded."""

    def __init__(self, repo, commit, override=None):
        self.repo, self.commit, self.override = repo, commit, override or {}
        self.reads, self.listed = [], []
        names = git(repo, ['ls-tree', '-r', '-z', '--name-only', commit]).decode().split('\\0')
        self.files = {n for n in names if n}

    def rel(self, path):
        path = posixpath.normpath(path)
        if not path.startswith(ROOT + '/'):
            raise PermissionError('outside the tree: %s' % path)
        return path[len(ROOT) + 1:]

    def open(self, path, mode='r', encoding=None, **_kw):
        rel = self.rel(path)
        data = self.override.get(rel, raw(self.repo, self.commit, rel))
        if data is None or 'w' in mode or 'a' in mode:
            raise FileNotFoundError(path)
        self.reads.append(rel)
        return io.BytesIO(data) if 'b' in mode else io.StringIO(data.decode(encoding or 'utf-8'))

    def isdir(self, path):
        rel = self.rel(path)
        return any(f.startswith(rel + '/') for f in self.files)

    def exists(self, path):
        rel = self.rel(path)
        return rel in self.files or self.isdir(path)

    def listdir(self, path):
        rel = self.rel(path)
        self.listed.append(rel)
        return sorted({f[len(rel) + 1:].split('/')[0] for f in self.files
                       if f.startswith(rel + '/')})


def shim_os(vt):
    pth = types.SimpleNamespace(**{k: getattr(posixpath, k) for k in (
        'join', 'dirname', 'basename', 'normpath', 'split', 'splitext', 'sep')})
    pth.abspath = posixpath.normpath
    pth.isdir, pth.exists = vt.isdir, vt.exists
    pth.isfile = lambda p: vt.rel(p) in vt.files
    return types.SimpleNamespace(path=pth, listdir=vt.listdir, sep='/')


def run_predicates(repo, d, lines, override=None):
    """(values, reads, listed): the predicates at `lines` of the guard at d, each evaluated with
    the definitions it reaches, over d's tree."""
    src = raw(repo, d, GUARD).decode('utf-8')
    tree = ast.parse(src)
    stmts = {s.lineno: s for s in tree.body}
    vt = VirtualTree(repo, d, override)
    values = []
    for line in lines:
        s = stmts[line]
        expr = s.value if isinstance(s, ast.AugAssign) else s
        roots = {n.id for n in ast.walk(expr) if isinstance(n, ast.Name)}
        ns = {'__file__': ROOT + '/' + GUARD, '__name__': 'controls'}
        for st in closure(tree, roots, line):
            if isinstance(st, (ast.Import, ast.ImportFrom)):
                exec(compile(ast.Module([st], []), GUARD, 'exec'), ns)
                continue
            ns['os'], ns['open'] = shim_os(vt), vt.open
            exec(compile(ast.Module([st], []), GUARD, 'exec'), ns)
        ns['os'], ns['open'] = shim_os(vt), vt.open
        values.append(bool(eval(compile(ast.Expression(expr), GUARD, 'eval'), ns)))
    return values, vt.reads, vt.listed


def pc4s(repo, d):
    manifest = json.loads(raw(repo, d, LEGACY))
    recs, spaces = manifest['records'], manifest['closed_namespaces']
    values, reads, listed = run_predicates(repo, d, PC4S_LINES)
    lines = ['PREDICATE  R7-PC4S line %d  %s' % (l, 'holds' if v else 'FAILS')
             for l, v in zip(PC4S_LINES, values)]
    bad = []
    for r in sorted(set(reads)):
        kind = ('legacy record' if r in recs else
                'lookup' if r == 'verification/migration-manifest.json' else 'NOT A LEGACY RECORD')
        lines.append('READ  %s  %s' % (r, kind))
        if kind.startswith('NOT'):
            bad.append(r)
    for r in sorted(set(listed)):
        kind = 'closed namespace' if r in spaces else 'NOT A CLOSED NAMESPACE'
        lines.append('LISTED  %s  %s' % (r, kind))
        if kind.startswith('NOT'):
            bad.append(r)
    pc4 = 'verification/seals/PC4.json'
    mutated, _r, _l = run_predicates(repo, d, PC4S_LINES[:1],
                                     override={pc4: raw(repo, d, pc4).replace(b'e', b'f', 1)})
    lines.append('COUNTERCONTROL  one byte of %s changed: line %d %s'
                 % (pc4, PC4S_LINES[0], 'holds' if mutated[0] else 'FAILS'))
    ok = all(values) and not bad and pc4 in reads and not mutated[0]
    lines.append('pc4s: %d predicate(s) %s; %d file(s) read, %d legacy record(s); %d directory '
                 'listing(s); %s' % (len(values), 'all hold' if all(values) else 'NOT ALL HOLD',
                                     len(set(reads)), len(set(reads) & set(recs)),
                                     len(set(listed)), 'legacy bytes only' if ok else 'FAILED'))
    return ok, lines


SOUGHT = {
    '_olt_supersessions': ('_OLT_SRC', ('d75427aece402e1629d56d1ca96fbc8d3c8101e8',
                                        'df2fab5770085d7e83543c50c00ffc6a3c2a37d0',
                                        "_seal_field('SI3', 'sealed_head')", '_SI3_MANIFESTED',
                                        '_SI3_MANDATED_BASE')),
    '_oln_supersession': ('_OLN_SRC', ("return (_MANIFEST_BASELINE == {'base': _OLT_B, "
                                       "'authorized': ('OLT',)}",)),
}


def evaluate(fn_src, name, var, text):
    ns = {var: text}
    exec(fn_src, ns)
    return bool(ns[name]())


def vacuity_of(text):
    """Per predicate: (evaluations, occurrences of its strings outside its definition)."""
    tree = ast.parse(text)
    lines = text.split('\\n')
    out = {}
    for name, (var, sought) in SOUGHT.items():
        fn = [s for s in tree.body if isinstance(s, ast.FunctionDef) and s.name == name][0]
        fn_src = '\\n'.join(lines[fn.lineno - 1:fn.end_lineno])
        outside = '\\n'.join(lines[:fn.lineno - 1] + lines[fn.end_lineno:])
        n_out = sum(outside.count(x) for x in sought)
        stripped = outside
        for x in sought:
            stripped = stripped.replace(x, '')
        stripped = '\\n'.join(lines[:0]) + stripped + '\\n' + fn_src
        out[name] = ([('the guard', evaluate(fn_src, name, var, text)),
                      ('the sought strings removed outside it', evaluate(fn_src, name, var, stripped)),
                      ('its own definition alone', evaluate(fn_src, name, var, fn_src))], n_out)
    return out


def vacuity(repo, commit, d):
    with tempfile.TemporaryDirectory() as td:
        paths = {}
        for key, (c, p) in {'retire': (commit, RD + 'retire.py'), 'guard': (d, GUARD),
                            'census': (commit, CENSUS)}.items():
            paths[key] = os.path.join(td, key)
            with open(paths[key], 'wb') as fh:
                fh.write(raw(repo, c, p))
        out = os.path.join(td, 'guard-1610.py')
        r = subprocess.run([sys.executable, paths['retire'], '--census-only', paths['guard'],
                            paths['census'], out], capture_output=True)
        if r.returncode:
            return False, ['vacuity: the 1,610 transformation failed: %s' % r.stdout.decode()[-200:]]
        t1610 = open(out, encoding='utf-8').read()
    lines, ok = [], True
    for label, text, required in (('1,610', t1610, True),
                                  ('D', raw(repo, d, GUARD).decode('utf-8'), False)):
        for name, (evals, n_out) in vacuity_of(text).items():
            for what, v in evals:
                lines.append('%s  %-5s %s on %s: %s' % ('EVAL' if required else 'NOTE', label, name,
                                                        what, 'holds' if v else 'FAILS'))
                ok &= v or not required
            lines.append('%s  %-5s %s: %d occurrence(s) of its strings outside its definition'
                         % ('EVAL' if required else 'NOTE', label, name, n_out))
            ok &= n_out == 0 or not required
    lines.append('vacuity: %s' % ('both predicates hold whatever the rest of the 1,610 guard says'
                                  if ok else 'FAILED'))
    return ok, lines


def self_test():'''
assert t.count(old) == 1; t = t.replace(old, new)
old = """    elif len(argv) == 4 and argv[0] == 'callers':
        ok, lines = callers(argv[1], argv[2], argv[3])
"""
new = """    elif len(argv) == 4 and argv[0] == 'callers':
        ok, lines = callers(argv[1], argv[2], argv[3])
    elif len(argv) == 3 and argv[0] == 'pc4s':
        ok, lines = pc4s(argv[1], argv[2])
    elif len(argv) == 4 and argv[0] == 'vacuity':
        ok, lines = vacuity(argv[1], argv[2], argv[3])
"""
assert t.count(old) == 1; t = t.replace(old, new)
open(p, 'w').write(t)
