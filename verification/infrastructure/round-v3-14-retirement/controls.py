#!/usr/bin/env python3
"""controls.py -- round V3-14's retirement controls, read from git objects at named commits.

Usage:
    python3 controls.py history <repository> <commit>
    python3 controls.py callers <repository> <commit> <verifier commit>
    python3 controls.py pc4s <repository> <D>
    python3 controls.py vacuity <repository> <commit> <D>
    python3 controls.py v313 <repository> <V3-13 stage 2 commit> <D>
    python3 controls.py --self-test

history   Every Python file the workflow's `Numerical probes` job runs at <commit>, with every
          repository module each imports from its own directory, transitively, scanned for any way
          to reach repository history: an import of subprocess (or of a git binding), a call of
          os.system, os.popen or a subprocess function, a read of the environment, and a string
          constant that is a git subcommand, the word git, a path through .git, or a ref under
          refs/. Prints each site and the count; exits 1 when the count is not zero.

callers   The module-level names tools/v3_verifier.py defines at <verifier commit> and no longer
          defines at <commit>, and every file in <commit>'s tree that refers to one of them through
          the verifier's module or runs the verifier with --project or --mode, round records
          (verification/infrastructure/round-*, verification/programmes/, verification/receipts/)
          set aside. Prints each caller and the count; exits 1 when the count is not zero.

pc4s      The four R7-PC4S predicates of the amendment (lines 17854 and 17999-18001 of the guard at
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
          definitions removed, and on their own definitions alone, all of which must hold; the
          countercontrols, which must fail: each on a text without its strings, and
          _oln_supersession on the guard with the statement it forbids appended. Also reported,
          not required: the same evaluations on the guard at <D>.

v313      The countercontrol for the preservation checker: V3-13's transformed guard, read at its
          stage 2 commit, with a ledger derived from it by a line diff against the guard at <D>, is
          checked by preserve.py against the census at <D>. It passes when S2, S3, S4 and S5 fail
          and S4 names all seven sites V3-13 damaged. The diff-derived ledger serves this
          countercontrol only; it is not the round's ledger.

All read git objects and nothing else, so a commit gives the same report on any checkout."""
import ast
import io
import json
import os
import posixpath
import re
import subprocess
import sys
import tempfile
import types

WORKFLOW = '.github/workflows/verify.yml'
VERIFIER = 'tools/v3_verifier.py'
GITCMD = {'rev-parse', 'rev-list', 'merge-base', 'ls-tree', 'cat-file', 'show', 'log', 'diff-tree',
          'fetch', 'for-each-ref', 'ls-remote', 'diff', 'blame', 'show-ref'}


def git(repo, args):
    return subprocess.run(['git', '-C', repo] + args, capture_output=True, check=True).stdout


def blob(repo, commit, path):
    r = subprocess.run(['git', '-C', repo, 'cat-file', 'blob', '%s:%s' % (commit, path)],
                       capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def probe_files(workflow):
    """The Python files the probes job runs, from its working directories and loops."""
    job = workflow[workflow.index('\n  probes:'):]
    nxt = re.search(r'\n  [a-z][a-z0-9-]*:\n', job[1:])
    job = job[:nxt.start() + 1] if nxt else job
    files = []
    for wd, body in re.findall(r'working-directory: (\S+)\n\s+run: \|\n((?:\s{10}.*\n)+)', job):
        names = re.findall(r'[a-z0-9_]+', re.search(r'for p in (.*?); do', body, re.S)
                           .group(1).replace('\\', ' '))
        suffix = '_probe.py' if '${p}_probe.py' in body else '.py'
        files += ['%s/%s%s' % (wd, n, suffix) for n in names]
    return files


def history_sites(src):
    out = []
    for n in ast.walk(ast.parse(src)):
        if isinstance(n, (ast.Import, ast.ImportFrom)):
            mods = [a.name for a in n.names] if isinstance(n, ast.Import) else [n.module or '']
            if any(m.split('.')[0] in ('subprocess', 'pygit2', 'git', 'dulwich') for m in mods):
                out.append((n.lineno, 'import', ast.unparse(n)))
        elif isinstance(n, ast.Call):
            f = ast.unparse(n.func)
            if f in ('os.system', 'os.popen') or f.startswith('subprocess.') or \
                    f.split('.')[-1] in ('check_output', 'Popen', 'check_call'):
                out.append((n.lineno, 'exec', f))
        elif isinstance(n, ast.Attribute) and n.attr in ('environ', 'getenv'):
            out.append((n.lineno, 'env', ast.unparse(n)))
        elif isinstance(n, ast.Constant) and isinstance(n.value, str):
            v = n.value
            if v in GITCMD or v == 'git' or re.search(r'(^|/)\.git(/|$)', v) or \
                    v.startswith('refs/'):
                out.append((n.lineno, 'git', v[:60]))
    return out


def local_imports(path, src):
    d = path.rsplit('/', 1)[0]
    out = []
    for n in ast.walk(ast.parse(src)):
        mods = [a.name for a in n.names] if isinstance(n, ast.Import) else (
            [n.module] if isinstance(n, ast.ImportFrom) and n.module and n.level == 0 else [])
        out += ['%s/%s.py' % (d, m.replace('.', '/')) for m in mods]
    return out


def history(repo, commit, read=None):
    read = read or (lambda p: blob(repo, commit, p))
    named = probe_files(read(WORKFLOW))
    seen, todo, lines = set(), list(named), []
    while todo:
        p = todo.pop()
        if p in seen:
            continue
        src = read(p)
        if src is None:
            continue
        seen.add(p)
        for line, kind, what in history_sites(src):
            lines.append('HISTORY  %s:%d  %s  %s' % (p, line, kind, what))
        todo += local_imports(p, src)
    missing = [p for p in named if p not in seen]
    for p in missing:
        lines.append('MISSING  %s' % p)
    n = sum(1 for x in lines if x.startswith('HISTORY'))
    lines.append('history: %d file(s) run by the probes job (%d named), %d history site(s)%s' % (
        len(seen), len(named), n, ', %d named file(s) missing' % len(missing) if missing else ''))
    return n == 0 and not missing, lines


def defined(src):
    out = set()
    for n in ast.parse(src).body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            out.add(n.name)
        elif isinstance(n, ast.Assign):
            out |= {t.id for t in n.targets if isinstance(t, ast.Name)}
    return out


def callers(repo, commit, before):
    gone = sorted(defined(blob(repo, before, VERIFIER)) - defined(blob(repo, commit, VERIFIER)))
    alts = ['\\b(v3|v3_verifier)\\.%s\\b' % re.escape(g) for g in gone]
    alts.append('v3_verifier\\.py.*--(project|mode)\\b')
    lines = ['callers: names removed from %s: %s' % (VERIFIER, ', '.join(gone) or 'none')]
    r = subprocess.run(['git', '-C', repo, 'grep', '-n', '-I', '-E', '|'.join(alts), commit, '--',
                        '.', ':!verification/infrastructure/round-*', ':!verification/programmes/',
                        ':!verification/receipts/'], capture_output=True)
    if r.returncode not in (0, 1):
        raise SystemExit('controls: git grep failed')
    for hit in r.stdout.decode('utf-8', 'replace').splitlines():
        _c, p, i, line = hit.split(':', 3)
        lines.append('CALLER  %s:%s  %s' % (p, i, line.strip()[:100]))
    n = sum(1 for x in lines if x.startswith('CALLER'))
    lines.append('callers: %d' % n)
    return n == 0, lines


GUARD = 'verification/lean/edge_rigidity_probe.py'
RD = 'verification/infrastructure/round-v3-14-retirement/'
CENSUS = 'verification/infrastructure/round-v3-12-retirement-census/census.json'
LEGACY = 'verification/infrastructure/round-v3-12-retirement-census/legacy-records.json'
PC4S_LINES = (17854, 17999, 18000, 18001)
ROOT = '/virtual'


def raw(repo, commit, path):
    r = subprocess.run(['git', '-C', repo, 'cat-file', 'blob', '%s:%s' % (commit, path)],
                       capture_output=True)
    return r.stdout if r.returncode == 0 else None


SCOPES = (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ClassDef, ast.ListComp,
          ast.SetComp, ast.DictComp, ast.GeneratorExp)


def module_nodes(stmt):
    """The nodes of a top-level statement that run in module scope: nothing inside a nested
    function, lambda, class or comprehension."""
    todo = [stmt]
    while todo:
        n = todo.pop()
        yield n
        for c in ast.iter_child_nodes(n):
            if not isinstance(c, SCOPES):
                todo.append(c)


def bindings(stmt):
    """The module-level names a top-level statement binds."""
    if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return {stmt.name}
    out = set()
    for n in module_nodes(stmt):
        if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store):
            out.add(n.id)
        elif isinstance(n, (ast.Import, ast.ImportFrom)):
            out |= {(a.asname or a.name).split('.')[0] for a in n.names}
    return out


def free_loads(stmt):
    """The names a top-level statement may read from module scope. For a function or class: every
    name loaded anywhere in it that is not an argument or a name stored anywhere in it. Otherwise:
    the names loaded in module scope, and those loaded in a nested scope that the nested scope
    does not bind."""
    def loads(x):
        return {n.id for n in ast.walk(x) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}

    def binds(x):
        return {n.arg for n in ast.walk(x) if isinstance(n, ast.arg)} | \
            {n.id for n in ast.walk(x) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store)}
    if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return loads(stmt) - binds(stmt)
    out = set()
    for n in module_nodes(stmt):
        if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load):
            out.add(n.id)
        for c in ast.iter_child_nodes(n):
            if isinstance(c, SCOPES):
                out |= loads(c) - binds(c)
    return out


def closure(tree, roots, before):
    """The top-level statements before line `before` that bind a name the roots need, transitively
    (each such statement's own module-scope reads included), in file order."""
    body = [s for s in tree.body if s.lineno < before]
    binds = [bindings(s) for s in body]
    need, chosen, todo = set(), set(), set(roots)
    while todo:
        nm = todo.pop()
        if nm in need:
            continue
        need.add(nm)
        for i, s in enumerate(body):
            if i not in chosen and nm in binds[i]:
                chosen.add(i)
                todo |= free_loads(s)
    return [body[i] for i in sorted(chosen)]


class VirtualTree:
    """Files and directories of one commit, served under ROOT, every access recorded."""

    def __init__(self, repo, commit, override=None):
        self.repo, self.commit, self.override = repo, commit, override or {}
        self.reads, self.listed = [], []
        names = git(repo, ['ls-tree', '-r', '-z', '--name-only', commit]).decode().split('\0')
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


def shim(ns, vt):
    """The module scope's file system is the virtual tree, and no child process can start."""
    def refused(*_a, **_k):
        raise PermissionError('a child process was started')
    ns['os'], ns['open'] = shim_os(vt), vt.open
    ns['subprocess'] = types.SimpleNamespace(run=refused, check_output=refused, Popen=refused,
                                             call=refused, check_call=refused)


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
            shim(ns, vt)
            exec(compile(ast.Module([st], []), GUARD, 'exec'), ns)
        shim(ns, vt)
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
    lines = text.split('\n')
    out = {}
    for name, (var, sought) in SOUGHT.items():
        fn = [s for s in tree.body if isinstance(s, ast.FunctionDef) and s.name == name][0]
        fn_src = '\n'.join(lines[fn.lineno - 1:fn.end_lineno])
        outside = '\n'.join(lines[:fn.lineno - 1] + lines[fn.end_lineno:])
        n_out = sum(outside.count(x) for x in sought)
        stripped = outside
        for x in sought:
            stripped = stripped.replace(x, '')
        stripped = '\n'.join(lines[:0]) + stripped + '\n' + fn_src
        # the countercontrols: the evaluation can fail, on a text without the strings, or, for the
        # one negative conjunct, on a text carrying the statement it forbids
        counter = [('a text without its strings', evaluate(fn_src, name, var, ''))]
        if name == '_oln_supersession':
            counter.append(('the guard with the forbidden statement appended', evaluate(
                fn_src, name, var, text + "\nif not (_MANIFEST_BASELINE == {'base': _OLT_B\n")))
        out[name] = ([('the guard', evaluate(fn_src, name, var, text)),
                      ('the sought strings removed outside it', evaluate(fn_src, name, var, stripped)),
                      ('its own definition alone', evaluate(fn_src, name, var, fn_src))], n_out,
                     counter)
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
        for name, (evals, n_out, counter) in vacuity_of(text).items():
            for what, v in evals:
                lines.append('%s  %-5s %s on %s: %s' % ('EVAL' if required else 'NOTE', label, name,
                                                        what, 'holds' if v else 'FAILS'))
                ok &= v or not required
            for what, v in counter if required else ():
                lines.append('COUNTERCONTROL  %s on %s: %s' % (name, what, 'holds' if v else 'FAILS'))
                ok &= not v
            lines.append('%s  %-5s %s: %d occurrence(s) of its strings outside its definition'
                         % ('EVAL' if required else 'NOTE', label, name, n_out))
            ok &= n_out == 0 or not required
    lines.append('vacuity: %s' % ('both predicates hold whatever the rest of the 1,610 guard says'
                                  if ok else 'FAILED'))
    return ok, lines


V313_SITES = [180, 181, 193, 232, 233, 292, 304, 305, 25309, 25310, 26777, 26778]


def v313(repo, stage2, d):
    import difflib
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import preserve as pv
    d_text = raw(repo, d, GUARD).decode('utf-8')
    v_text = raw(repo, stage2, GUARD).decode('utf-8')
    census = json.loads(raw(repo, d, CENSUS))
    a, b = d_text.split('\n'), v_text.split('\n')
    sp = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal':
            continue
        if i2 == i1:
            return False, ['v313: a pure insertion at %d; no D-side splice' % i1]
        sp.append({'d_start': i1 + 1, 'd_end': i2, 'old_sha256': pv.sha256('\n'.join(a[i1:i2])),
                   'new': b[j1:j2], 'new_sha256': pv.sha256('\n'.join(b[j1:j2])),
                   'reasons': ['v3-13']})
    led = {'schema': 'v3-14-splice-ledger', 'version': 1, 'base': {'blob': pv.blob(d_text)},
           'output': {'blob': pv.blob(v_text)}, 'splices': sp}
    res = pv.check(d_text, census, led, v_text)
    lines = ['CHECK  %s  %s  %s' % (c, 'holds' if ok else 'FAILS', det) for c, ok, det in res]
    got = {c: ok for c, ok, _d in res}
    s4 = next(det for c, _ok, det in res if c == 'S4')
    named = sorted(int(x) for x in re.findall(r'\d+', s4.split('lines')[-1])) if 'lines' in s4 else []
    ok = got['L1'] and got['L2'] and got['S1'] and not any(got[c] for c in ('S2', 'S3', 'S4', 'S5')) \
        and named == V313_SITES
    lines.append('v313: %s' % ('the checker rejects V3-13\'s guard, naming all seven sites' if ok
                               else 'FAILED'))
    return ok, lines


def self_test():
    fails = []
    wf = ('jobs:\n  probes:\n    steps:\n      - name: Probes\n        working-directory: d\n'
          '        run: |\n          for p in a b; do\n            python3 "${p}_probe.py"\n'
          '          done\n  other:\n    steps: []\n')
    files = {WORKFLOW: wf, 'd/a_probe.py': 'import b_helper\nx = 1\n',
             'd/b_probe.py': 'y = 2\n', 'd/b_helper.py': 'z = 3\n'}
    ok, _ = history('.', 'X', read=files.get)
    if not ok:
        fails.append('clean files reported')
    for bad in ('import subprocess\n', 'import os\nos.system("x")\n', 'import os\nos.environ\n',
                'c = ["git", "log"]\n', 'r = "refs/remotes/origin/main"\n', 'p = ".git/HEAD"\n'):
        ok, _ = history('.', 'X', read=dict(files, **{'d/b_helper.py': bad}).get)
        if ok:
            fails.append('history site through an import not reported: %r' % bad)
    ok, _ = history('.', 'X', read={k: v for k, v in files.items() if k != 'd/b_probe.py'}.get)
    if ok:
        fails.append('a missing named probe not reported')
    if defined('A = 1\ndef f():\n    B = 2\nclass C: pass\n') != {'A', 'f', 'C'}:
        fails.append('module-level names')
    for f in fails:
        print('SELF-TEST  FAIL  %s' % f)
    print('controls: self-test %s' % ('OK' if not fails else 'FAILED'))
    return not fails


def main(argv):
    if argv == ['--self-test']:
        return 0 if self_test() else 1
    if len(argv) == 3 and argv[0] == 'history':
        ok, lines = history(argv[1], argv[2])
    elif len(argv) == 4 and argv[0] == 'callers':
        ok, lines = callers(argv[1], argv[2], argv[3])
    elif len(argv) == 3 and argv[0] == 'pc4s':
        ok, lines = pc4s(argv[1], argv[2])
    elif len(argv) == 4 and argv[0] == 'vacuity':
        ok, lines = vacuity(argv[1], argv[2], argv[3])
    elif len(argv) == 4 and argv[0] == 'v313':
        ok, lines = v313(argv[1], argv[2], argv[3])
    else:
        print(__doc__.split('\n\n')[1])
        return 2
    print('\n'.join(lines))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
